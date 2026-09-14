import numpy as np
import matplotlib.pyplot as plt

x_labels = ["0*", "5", "10", "20", "50", "100"]
x = np.arange(len(x_labels))

exact = np.array([
    0.5581, 0.5968, 0.5984,
    0.5839, 0.5887, 0.5613
])
exact_std = np.array([
    0.0157, 0.0140, 0.0134,
    0.0127, 0.0129, 0.0136
])

hierarchy = np.array([
    1.3177, 1.3597, 1.3903,
    1.3661, 1.3677, 1.3048
])
hierarchy_std = np.array([
    0.0288, 0.0257, 0.0238,
    0.0225, 0.0233, 0.0247
])

l1_match = np.array([
    0.7597, 0.7629, 0.7919,
    0.7823, 0.7790, 0.7435
])
l1_match_std = np.array([
    0.0155, 0.0136, 0.0128,
    0.0121, 0.0125, 0.0134
])

metrics = [
    ("Exact Match", exact, exact_std),
    ("Hierarchy Score", hierarchy, hierarchy_std),
    ("L1 Match", l1_match, l1_match_std),
]

fig, axes = plt.subplots(1, 3, figsize=(13, 4))

for ax, (title, values, stds) in zip(axes, metrics):

    ax.errorbar(
        x,
        values,
        yerr=stds,
        marker="o",
        markersize=6,
        linewidth=1.8,
        capsize=4,
        capthick=1.2,
    )

    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)

    ax.set_xlabel("Number of Neighbors (k)")
    ax.set_ylabel(title)
    ax.set_title(title)

    ax.grid(
        axis="y",
        linestyle="--",
        linewidth=0.6,
        alpha=0.5
    )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig("pbmc_knn.png", dpi=300, bbox_inches="tight")
plt.savefig("pbmc_knn.pdf", bbox_inches="tight")
plt.show()