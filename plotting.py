from guppylang.emulator.result import QsysResult
import matplotlib.pyplot as plt


def plot_results(
    sim_result: QsysResult,
    n_strings: int = 4,
    dark_mode: bool = False,
    y_limit: int = 800,
) -> None:
    counts_dict = sim_result.register_counts()["c"]
    sorted_shots = counts_dict.most_common()
    n_most_common_strings = sorted_shots[:n_strings]
    x_axis_values = [f"|{entry[0]}>" for entry in n_most_common_strings]  # basis states
    y_axis_values = [entry[1] for entry in n_most_common_strings]  # counts

    if dark_mode:
        plt.style.use("dark_background")

    fig = plt.figure()
    ax = fig.add_axes((0, 0, 0.4, 0.5))
    color_list = ["teal"] * (len(x_axis_values))
    container = ax.bar(
        x=x_axis_values,
        height=y_axis_values,
        color=color_list,
    )
    ax.bar_label(container, fmt="{:,.0f}")
    ax.set_title(label="Results")
    plt.ylim([0, y_limit])
    plt.xlabel("Basis State")
    plt.ylabel("Number of Shots")
    plt.show()
