import numpy as np
import matplotlib.pyplot as plt


def main():
    # --------------------------------------------------
    # Labels
    # --------------------------------------------------
    methods = ["stg1", "mean_z", "tirosh", "ucell"]
    x = np.arange(len(methods))

    # --------------------------------------------------
    # Data
    # --------------------------------------------------
    exact = np.array([0.4385, 0.4832, 0.4642, 0.4899])
    exact_std = np.array([0.0093, 0.0102, 0.0105, 0.0112])

    hierarchy = np.array([3.0794, 3.1611, 3.1365, 3.1667])
    hierarchy_std = np.array([0.0255, 0.0244, 0.0253, 0.0272])

    l1_match = np.array([0.9776, 0.9821, 0.9843, 0.9799])
    l1_match_std = np.array([0.0048, 0.0043, 0.0041, 0.0046])

    l2_match = np.array([0.9105, 0.9183, 0.9217, 0.9195])
    l2_match_std = np.array([0.0081, 0.0074, 0.0078, 0.0077])

    l3_match = np.array([0.7528, 0.7774, 0.7662, 0.7774])
    l3_match_std = np.array([0.0099, 0.0094, 0.0101, 0.0109])

    # --------------------------------------------------
    # Create figure
    # --------------------------------------------------
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.8))

    # ==================================================
    # Plot 1: Exact Match (discrete points, no line)
    # ==================================================
    ax = axes[0]

    ax.errorbar(
        x,
        exact,
        yerr=exact_std,
        fmt="o",           # 点
        linestyle="none",  # 不连线
        markersize=8,
        capsize=4,
        capthick=1.2,
    )

    ax.set_xticks(x)
    ax.set_xticklabels(methods)
    ax.set_title("Exact Match")
    ax.set_ylabel("Exact Match")
    ax.set_ylim(0.42, 0.51)

    ax.grid(axis="y", linestyle="--", linewidth=0.6, alpha=0.4)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # ==================================================
    # Plot 2: Hierarchy Score (discrete points, no line)
    # ==================================================
    ax = axes[1]

    ax.errorbar(
        x,
        hierarchy,
        yerr=hierarchy_std,
        fmt="o",           # 点
        linestyle="none",  # 不连线
        markersize=8,
        capsize=4,
        capthick=1.2,
    )

    ax.set_xticks(x)
    ax.set_xticklabels(methods)
    ax.set_title("Hierarchy Score")
    ax.set_ylabel("Hierarchy Score")
    ax.set_ylim(3.02, 3.22)

    ax.grid(axis="y", linestyle="--", linewidth=0.6, alpha=0.4)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # ==================================================
    # Plot 3: Hierarchical Match Trend (line plot)
    # ==================================================
    ax = axes[2]

    levels = ["L1", "L2", "L3", "L4*"]
    x_levels = np.arange(len(levels))

    for i, method in enumerate(methods):
        y = [l1_match[i], l2_match[i], l3_match[i], exact[i]]
        yerr = [l1_match_std[i], l2_match_std[i], l3_match_std[i], exact_std[i]]

        ax.errorbar(
            x_levels,
            y,
            yerr=yerr,
            marker="o",
            linewidth=1.8,
            capsize=4,
            label=method,
        )

    ax.set_xticks(x_levels)
    ax.set_xticklabels(levels)
    ax.set_title("Hierarchical Match Trend")
    ax.set_ylabel("Match Rate")
    ax.set_ylim(0.40, 1.00)

    ax.grid(axis="y", linestyle="--", linewidth=0.6, alpha=0.4)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(frameon=False, fontsize=9)

    # --------------------------------------------------
    # Save and show
    # --------------------------------------------------
    plt.tight_layout()
    plt.savefig("hlca_program_scoring.png", dpi=300, bbox_inches="tight")
    plt.savefig("hlca_program_scoring.pdf", bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()