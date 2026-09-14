import numpy as np
import matplotlib.pyplot as plt

methods = ["stg1", "mean_z", "tirosh", "ucell"]
x = np.arange(len(methods))

exact = np.array([0.5984, 0.5952, 0.6339, 0.5855])
exact_std = np.array([0.0134, 0.0144, 0.0140, 0.0139])

hierarchy = np.array([1.3903, 1.3500, 1.4177, 1.3403])
hierarchy_std = np.array([0.0238, 0.0262, 0.0250, 0.0251])

l1_match = np.array([0.7919, 0.7548, 0.7839, 0.7548])
l1_match_std = np.array([0.0128, 0.0137, 0.0130, 0.0130])

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
        fmt="o",
        markersize=6,
        linewidth=1.5,
        capsize=4,
    )

    ax.set_xticks(x)
    ax.set_xticklabels(methods)
    ax.set_title(title)
    ax.set_ylabel(title)

    ax.grid(axis="y", linestyle="--", linewidth=0.6, alpha=0.4)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig("pbmc_program_scoring.png", dpi=300, bbox_inches="tight")
plt.savefig("pbmc_program_scoring.pdf", bbox_inches="tight")
plt.show()