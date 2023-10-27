from pathlib import Path
import numpy as np
import training_data_1color
import training_data_2color
import training_data_3color
import plotting
import sklearn.utils
import matplotlib.pyplot as plt
from time import time
import os.path

def main(
        n_traces,
        n_frames,
        n_colors,
        n_states,
        balance_classes,
        reduce_memory,
        state_mode,
        n_states_mode,
        parallel_asynchronous,
        x_name,
        y_name,
        outdir
):
    """
    Simulation scripts are inspired by the 2-color training sets used for the DeepFRET-Model.
    Main additions:
        Single-channel and 3-color FRET training sets
        Bleaching classes for individual dyes (2- and 3-color FRET)
        State mode (for training state transition classifiers)
        Separate number of states modes (for training number of oberserved states classifiers)
        Reworked 'Scrambled' class termed 'Artifact'
        Fixed noise calculation of individual FRET states (looping over unrounded states lead to erroneous labeling)
        Balancing based on total number of labeled frames in the data set
    For original scripts, please see:
    https://github.com/komodovaran/DeepFRET-Model.git

    n_traces: Number of traces
    n_timesteps: Number of frames per trace
    n_colors: Number of colors (1-color, 2-color or 3-color data possible)
    balance_classes: Balance classes based on minimum number of labeled frames
    reduce_memory: Include/exclude trace parameters beside countrates
    state_mode: Label dynamic traces according to state occupancy, used for training state classifiers
    n_states_model: Label each trace according to number of observed traces, used for number of states classifier
    parallel_asynchronous: parallel processing (faster)
    outdir: Output directory
    """
    if not os.path.isdir(outdir):
        os.mkdir(outdir)
    print("Generating traces...")
    start = time()
    if n_colors == 1 and not state_mode:
        training_data = training_data_1color.simulate_1color_traces(
            n_traces=int(n_traces),
            max_n_states=n_states,
            n_frames=n_frames,
            state_mode=state_mode,
            n_states_mode=n_states_mode,
            reduce_memory=reduce_memory,
            parallel_asynchronous=parallel_asynchronous
        )
        targets = training_data["label"].values
        if reduce_memory:
            training_data = training_data[["DD"]].values
        else:
            training_data = training_data[
                ["DD", "DA", "E", "E_true", "label", "_noise_level", "_min_E_diff", "trans_mean"]].values
    elif n_colors == 2 or (n_colors == 1 and state_mode):
        training_data = training_data_2color.simulate_2color_traces(
            n_traces=int(n_traces),
            max_n_states=n_states,
            n_frames=n_frames,
            state_mode=state_mode,
            n_states_mode=n_states_mode,
            reduce_memory=reduce_memory,
            parallel_asynchronous=parallel_asynchronous,
        )
        targets = training_data["label"].values
        if reduce_memory:
            if state_mode or n_states_mode:
                training_data = training_data[["DD", "DA"]].values
            else:
                training_data = training_data[["DD", "DA", "AA"]].values
        else:
            training_data = training_data[
                ["DD", "DA", "AA", "E", "E_true", "label", "_noise_level", "_min_E_diff", "trans_mean"]].values
    elif n_colors == 3:
        training_data = training_data_3color.simulate_3color_traces(
            n_traces=int(n_traces),
            max_n_states=n_states,
            n_frames=n_frames,
            state_mode=state_mode,
            n_states_mode=n_states_mode,
            reduce_memory=reduce_memory,
            parallel_asynchronous=parallel_asynchronous
        )
        targets = training_data["label"].values
        if reduce_memory:
            if state_mode or n_states_mode:
                training_data = training_data[["BB", "BG", "BR", "GG", "GR"]].values
            else:
                training_data = training_data[["BB", "BG", "BR", "GG", "GR", "RR"]].values
        else:
            training_data = training_data[
                ["BB", "BG", "BR", "GG", "GR", "label", "_noise_level", "_min_E_diff", "trans_mean", "E",
                 "E_true"]].values
    else:
        raise ValueError

    stop = time()
    training_data = training_data.reshape(-1, n_frames, training_data.shape[1])
    targets = targets.reshape(-1, n_frames, 1)
    print("spent {:.2f} s to generate".format((stop - start)))
    print("Labels: ", set(targets.ravel()))
    print(f"Number of categories: {set(targets.ravel())}")
    if balance_classes and not state_mode:
        targets = targets.astype(int)
        # prebalance = scipy.stats.itemfreq(y[:, :, 0])[:, 1]
        prebalance = np.unique(targets[:, :, 0], return_counts=True)[1]
        limit = np.min(prebalance)
        cum_labels = np.zeros(len(prebalance)).astype(int)
        balanced_training_data = []
        balanced_targets = []
        for i in range(len(training_data)):
            yi = targets[i, :, :]
            label, freq = np.unique(yi, return_counts=True)
            try:
                if all(cum_labels[label] < limit):
                    xi = training_data[i, :, :]
                    balanced_training_data.append(xi)
                    balanced_targets.append(yi)
                    cum_labels[label] += freq
            except IndexError:
                print("Not all classes sampled...")
                return

        training_data, targets = [np.array(arr) for arr in (balanced_training_data, balanced_targets)]
        sklearn.utils.shuffle(training_data, targets)
    if state_mode:
        plotting.plot_trace_label_distribution(X=training_data, y=targets, method="state_classes", outdir=outdir)
    elif n_states_mode:
        plotting.plot_trace_label_distribution(X=training_data, y=targets, method="n_states_classes", outdir=outdir)
    else:
        if n_colors == 1:
            plotting.plot_trace_label_distribution(X=training_data, y=targets, n_colors=1, outdir=outdir)
        elif n_colors == 2:
            plotting.plot_trace_label_distribution(X=training_data, y=targets, n_colors=2, outdir=outdir)
        else:
            plotting.plot_trace_label_distribution(X=training_data, y=targets, n_colors=3, outdir=outdir)

    if np.any(np.isnan(training_data)):
        raise ValueError

    for obj, name in zip((training_data, targets), (x_name, y_name)):
        path = str(Path(outdir).joinpath(name))
        np.savez_compressed(path, obj)

    print(f"Number of channels: {training_data.shape[-1]}")
    print(f"Generated {training_data.shape[0]} traces")
