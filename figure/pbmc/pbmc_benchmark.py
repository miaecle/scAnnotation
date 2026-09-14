import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# Labels
# --------------------------------------------------
groups = ["Single cell", "KNN (k=10)", "Pseudobulk"]
methods = ["Expr", "Z-score", "TF-IDF"]

# --------------------------------------------------
# Data
# rows: groups = [Single cell, KNN, Pseudobulk]
# cols: methods = [Expr, Z-score, TF-IDF]
# --------------------------------------------------
exact = np.array([
    [0.4097, 0.3758, 0.5581],
    [0.3935, 0.3935, 0.5758],
    [0.4210, 0.6661, 0.6806],
])

exact_std = np.array([
    [0.0144, 0.0144, 0.0157],
    [0.0138, 0.0136, 0.0146],
    [0.0114, 0.0119, 0.0102],
])

hierarchy = np.array([
    [1.0919, 0.9323, 1.3177],
    [1.0274, 0.9484, 1.3452],
    [1.1258, 1.5145, 1.5339],
])

hierarchy_std = np.array([
    [0.0258, 0.0274, 0.0288],
    [0.0258, 0.0258, 0.0257],
    [0.0198, 0.0189, 0.0171],
])

l1 = np.array([
    [0.6823, 0.5565, 0.7597],
    [0.6339, 0.5548, 0.7694],
    [0.7048, 0.8484, 0.8532],
])

l1_std = np.array([
    [0.0148, 0.0151, 0.0155],
    [0.0147, 0.0143, 0.0134],
    [0.0117, 0.0091, 0.0084],
])

# --------------------------------------------------
# PBMC Random Guess Baseline
# --------------------------------------------------
random_baseline = {
    "Exact Match": 0.0258,
    "Hierarchy Score": 0.1565,
    "L1 Match": 0.1306,
}

random_baseline_std = {
    "Exact Match": 0.0063,
    "Hierarchy Score": 0.0172,
    "L1 Match": 0.0134,
}

random_baseline_ci = {
    "Exact Match": (0.0145, 0.0387),
    "Hierarchy Score": (0.1242, 0.1903),
    "L1 Match": (0.1065, 0.1581),
}

# --------------------------------------------------
# Plot helper
# --------------------------------------------------
def plot_metric(ax, values, stds, ylabel, baseline, ylim=None):
    x = np.arange(len(groups))
    width = 0.23

    # Bars
    for i, method in enumerate(methods):
        ax.bar(
            x + (i - 1) * width,
            values[:, i],
            width,
            yerr=stds[:, i],
            capsize=3,
            label=method,
        )

    # Random guess baseline
    ax.axhline(
        baseline,
        linestyle="--",
        linewidth=1.6,
        label="Random Guess",
    )

    ax.axhspan(
        random_baseline_ci[ylabel][0],
        random_baseline_ci[ylabel][1],
        alpha=0.30,
    )

    # Axis settings
    ax.set_xticks(x)
    ax.set_xticklabels(groups)
    ax.set_ylabel(ylabel)

    if ylim is not None:
        ax.set_ylim(*ylim)

    # Grid
    ax.grid(
        axis="y",
        linestyle="--",
        linewidth=0.6,
        alpha=0.4,
    )

    # Remove top/right borders
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


# --------------------------------------------------
# Create figure
# --------------------------------------------------
fig, axes = plt.subplots(
    1,
    3,
    figsize=(18, 4.5),
    sharey=False,
)

# --------------------------------------------------
# Plot 1: Exact Match
# --------------------------------------------------
plot_metric(
    axes[0],
    exact,
    exact_std,
    "Exact Match",
    baseline=random_baseline["Exact Match"],
    ylim=(0, 1.0),
)

# --------------------------------------------------
# Plot 2: Hierarchy Score
# --------------------------------------------------
plot_metric(
    axes[1],
    hierarchy,
    hierarchy_std,
    "Hierarchy Score",
    baseline=random_baseline["Hierarchy Score"],
    ylim=(0, 2.0),
)

# --------------------------------------------------
# Plot 3: L1 Match
# --------------------------------------------------
plot_metric(
    axes[2],
    l1,
    l1_std,
    "L1 Match",
    baseline=random_baseline["L1 Match"],
    ylim=(0, 1.0),
)

# --------------------------------------------------
# Shared legend
# --------------------------------------------------
handles, labels = axes[0].get_legend_handles_labels()

# Reorder legend so Random Guess appears first
desired_order = [
    "Random Guess",
    "Expr",
    "Z-score",
    "TF-IDF",
]

label_to_handle = dict(zip(labels, handles))

ordered_handles = [
    label_to_handle[label]
    for label in desired_order
]

fig.legend(
    ordered_handles,
    desired_order,
    loc="upper center",
    bbox_to_anchor=(0.5, 1.04),
    ncol=4,
    frameon=False,
    fontsize=11,
)

# --------------------------------------------------
# Layout
# --------------------------------------------------
fig.tight_layout(
    rect=[0, 0, 1, 0.90]
)

# --------------------------------------------------
# Save
# --------------------------------------------------
fig.savefig(
    "pbmc_benchmark_with_random_baseline.pdf",
    bbox_inches="tight",
)

fig.savefig(
    "pbmc_benchmark_with_random_baseline.png",
    bbox_inches="tight",
    dpi=300,
)

plt.show()