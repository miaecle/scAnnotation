import numpy as np
import matplotlib.pyplot as plt


def main():
    # ------------------------------------------------------------
    # Data
    # ------------------------------------------------------------
    top_n = np.array([5, 10, 20, 50, 100])

    exact = np.array([
        0.5516,
        0.5919,
        0.5903,
        0.5984,
        0.5935,
    ])

    exact_std = np.array([
        0.0146,
        0.0137,
        0.0144,
        0.0134,
        0.0139,
    ])

    hierarchy = np.array([
        1.3226,
        1.3887,
        1.3839,
        1.3903,
        1.3806,
    ])

    hierarchy_std = np.array([
        0.0250,
        0.0242,
        0.0254,
        0.0238,
        0.0249,
    ])

    l1_match = np.array([
        0.7710,
        0.7968,
        0.7935,
        0.7919,
        0.7871,
    ])

    l1_match_std = np.array([
        0.0133,
        0.0129,
        0.0132,
        0.0128,
        0.0132,
    ])

    # ------------------------------------------------------------
    # Plot settings
    # ------------------------------------------------------------
    metrics = [
        ("Exact Match", exact, exact_std),
        ("Hierarchy Score", hierarchy, hierarchy_std),
        ("L1 Match", l1_match, l1_match_std),
    ]

    fig, axes = plt.subplots(
        1,
        3,
        figsize=(13, 4),
    )

    for ax, (title, values, stds) in zip(axes, metrics):
        ax.errorbar(
            top_n,
            values,
            yerr=stds,
            marker="o",
            markersize=6,
            linewidth=1.8,
            capsize=4,
            capthick=1.2,
        )

        # Log scale is suitable because 5, 10, 20, 50, 100, 200
        # are not evenly spaced numerically.
        ax.set_xscale("log")

        # Force matplotlib to show exactly these tested values.
        ax.set_xticks(top_n)
        ax.set_xticklabels([str(x) for x in top_n])

        ax.set_xlabel("Top-N Genes")
        ax.set_ylabel(title)
        ax.set_title(title)

        ax.grid(
            axis="y",
            linestyle="--",
            linewidth=0.6,
            alpha=0.5,
        )

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    fig.tight_layout()

    # ------------------------------------------------------------
    # Save figure
    # ------------------------------------------------------------
    fig.savefig(
        "pbmc_topgene.png",
        dpi=300,
        bbox_inches="tight",
    )

    fig.savefig(
        "pbmc_topgene.pdf",
        bbox_inches="tight",
    )

    plt.show()


if __name__ == "__main__":
    main()