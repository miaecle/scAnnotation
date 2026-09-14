import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# Labels
# --------------------------------------------------
groups = ["Single cell", "KNN (k=10)", "Pseudobulk"]
methods = ["Expr", "Z-score", "TF-IDF"]

x = np.arange(len(groups))
width = 0.23

# --------------------------------------------------
# Data
# rows: groups = [Single cell, KNN, Pseudobulk]
# cols: methods = [Expr, Z-score, TF-IDF]
# --------------------------------------------------
exact = np.array([
    [0.2774, 0.2550, 0.4060],
    [0.2886, 0.2774, 0.4150],
    [0.3031, 0.5615, 0.4284],
])

exact_std = np.array([
    [0.0090, 0.0100, 0.0100],
    [0.0088, 0.0095, 0.0099],
    [0.0070, 0.0073, 0.0060],
])

hierarchy = np.array([
    [2.4664, 1.8680, 2.9653],
    [2.4989, 2.0671, 2.9933],
    [2.6040, 3.2159, 3.0515],
])

hierarchy_std = np.array([
    [0.0300, 0.0394, 0.0254],
    [0.0305, 0.0367, 0.0259],
    [0.0176, 0.0192, 0.0142],
])

l1_match = np.array([
    [0.8949, 0.6689, 0.9597],
    [0.8881, 0.7204, 0.9653],
    [0.9083, 0.9787, 0.9810],
])

l1_match_std = np.array([
    [0.0084, 0.0125, 0.0051],
    [0.0087, 0.0115, 0.0046],
    [0.0040, 0.0037, 0.0018],
])

l2_match = np.array([
    [0.7785, 0.5559, 0.8904],
    [0.7796, 0.6163, 0.8926],
    [0.8501, 0.8926, 0.9206],
])

l2_match_std = np.array([
    [0.0105, 0.0128, 0.0080],
    [0.0108, 0.0118, 0.0081],
    [0.0052, 0.0057, 0.0042],
])

l3_match = np.array([
    [0.5157, 0.3881, 0.7092],
    [0.5425, 0.4530, 0.7204],
    [0.5425, 0.7830, 0.7215],
])

l3_match_std = np.array([
    [0.0111, 0.0122, 0.0097],
    [0.0112, 0.0113, 0.0100],
    [0.0065, 0.0072, 0.0053],
])

# --------------------------------------------------
# Random guess baseline
# --------------------------------------------------
random_baseline = {
    "Exact Match": 0.0179,
    "Hierarchy Score": 0.5045,
    "L3 Match": 0.0503,
    "L2 Match": 0.1510,
    "L1 Match": 0.2852,
}

random_baseline_std = {
    "Exact Match": 0.0045,
    "Hierarchy Score": 0.0298,
    "L3 Match": 0.0072,
    "L2 Match": 0.0113,
    "L1 Match": 0.0144,
}

# Optional: 95% CI if you want to annotate or shade later
random_baseline_ci = {
    "Exact Match": (0.0101, 0.0280),
    "Hierarchy Score": (0.4508, 0.5649),
    "L3 Match": (0.0369, 0.0649),
    "L2 Match": (0.1298, 0.1756),
    "L1 Match": (0.2573, 0.3154),
}

# --------------------------------------------------
# Metric list for the first 5 subplots
# --------------------------------------------------
metrics = [
    ("Exact Match", exact, exact_std, (0, 1.0)),
    ("Hierarchy Score", hierarchy, hierarchy_std, (0, 4.0)),
    ("L3 Match", l3_match, l3_match_std, (0, 1.0)),
    ("L2 Match", l2_match, l2_match_std, (0, 1.0)),
    ("L1 Match", l1_match, l1_match_std, (0, 1.0)),
]

# --------------------------------------------------
# Create figure
# --------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 8))
axes = axes.flatten()

# --------------------------------------------------
# First 5 plots: grouped bar charts + random baseline
# --------------------------------------------------
for idx, (ax, (title, values, stds, ylim)) in enumerate(zip(axes[:5], metrics)):
    for i, method in enumerate(methods):
        ax.bar(
            x + (i - 1) * width,
            values[:, i],
            width,
            yerr=stds[:, i],
            capsize=3,
            label=method,
        )

    # Random guess baseline as dashed horizontal line
    ax.axhline(
        random_baseline[title],
        linestyle="--",
        linewidth=1.5,
        label="Random Guess",
    )

    ax.axhspan(
        random_baseline_ci[title][0],
        random_baseline_ci[title][1],
        alpha=0.30,
    )

    ax.set_xticks(x)
    ax.set_xticklabels(groups)
    ax.set_title(title)
    ax.set_ylabel(title)
    ax.set_ylim(*ylim)

    ax.grid(axis="y", linestyle="--", linewidth=0.6, alpha=0.4)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Show legend only in the first subplot to avoid repetition
    if idx == 0:
        ax.legend(frameon=False, fontsize=9)

# --------------------------------------------------
# Sixth plot: line chart for TF-IDF only across L1/L2/L3/L4*
# plus random guess trend
# --------------------------------------------------
ax = axes[5]

level_names = ["L1", "L2", "L3", "L4*"]
x_levels = np.arange(len(level_names))

# TF-IDF is column index 2
tfidf_idx = 2

for g, group_name in enumerate(groups):
    y = [
        l1_match[g, tfidf_idx],   # L1
        l2_match[g, tfidf_idx],   # L2
        l3_match[g, tfidf_idx],   # L3
        exact[g, tfidf_idx],      # L4* / exact
    ]
    yerr = [
        l1_match_std[g, tfidf_idx],
        l2_match_std[g, tfidf_idx],
        l3_match_std[g, tfidf_idx],
        exact_std[g, tfidf_idx],
    ]

    ax.errorbar(
        x_levels,
        y,
        yerr=yerr,
        marker="o",
        linewidth=1.8,
        capsize=3,
        label=group_name,
    )

# Random guess trend
random_y = [
    random_baseline["L1 Match"],
    random_baseline["L2 Match"],
    random_baseline["L3 Match"],
    random_baseline["Exact Match"],
]

random_yerr = [
    random_baseline_std["L1 Match"],
    random_baseline_std["L2 Match"],
    random_baseline_std["L3 Match"],
    random_baseline_std["Exact Match"],
]

ax.errorbar(
    x_levels,
    random_y,
    yerr=random_yerr,
    marker="o",
    linestyle="--",
    linewidth=1.8,
    capsize=3,
    label="Random Guess",
)

ax.set_xticks(x_levels)
ax.set_xticklabels(level_names)
ax.set_title("Hierarchical Match Trend (TF-IDF)")
ax.set_ylabel("Match Rate")
ax.set_ylim(0, 1.0)   # IMPORTANT: must start from 0 so random baseline is visible

ax.grid(axis="y", linestyle="--", linewidth=0.6, alpha=0.4)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.legend(frameon=False, fontsize=9)

# --------------------------------------------------
# Save and show
# --------------------------------------------------
plt.tight_layout()
plt.savefig("hlca_benchmark_with_random_baseline.png", dpi=300, bbox_inches="tight")
plt.savefig("hlca_benchmark_with_random_baseline.pdf", bbox_inches="tight")
plt.show()