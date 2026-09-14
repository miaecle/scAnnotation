import numpy as np
import matplotlib.pyplot as plt

rows = ["Single cell", "KNN (k=10)", "Pseudobulk"]
cols = ["Expr", "Z-score", "TF-IDF"]

exact = np.array([
    [0.4097, 0.3758, 0.5581],
    [0.3935, 0.3935, 0.5758],
    [0.4210, 0.6661, 0.6806],
])

hierarchy = np.array([
    [1.0919, 0.9323, 1.3177],
    [1.0274, 0.9484, 1.3452],
    [1.1258, 1.5145, 1.5339],
])

l1_match = np.array([
    [0.6823, 0.5565, 0.7597],
    [0.6339, 0.5548, 0.7694],
    [0.7048, 0.8484, 0.8532],
])

metrics = [
    ("Exact Match", exact),
    ("Hierarchy Score", hierarchy),
    ("L1 Match", l1_match),
]

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

for ax, (title, data) in zip(axes, metrics):
    im = ax.imshow(data, aspect="auto")

    ax.set_xticks(np.arange(len(cols)))
    ax.set_yticks(np.arange(len(rows)))
    ax.set_xticklabels(cols)
    ax.set_yticklabels(rows)
    ax.set_title(title)

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ax.text(
                j, i, f"{data[i, j]:.4f}",
                ha="center", va="center"
            )

    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

plt.tight_layout()
plt.show()

plt.savefig("pbmc_heatmap.pdf", bbox_inches="tight")
plt.savefig("pbmc_heatmap.png", bbox_inches="tight", dpi=300)