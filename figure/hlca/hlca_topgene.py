import matplotlib.pyplot as plt
import numpy as np

# =========================
# Data
# =========================
top_n = [5, 10, 20, 50, 100, 200]

exact = [0.3423, 0.3758, 0.4060, 0.4195, 0.4373, 0.4284]
exact_std = [0.0097, 0.0094, 0.0096, 0.0106, 0.0106, 0.0107]

hierarchy = [2.7841, 2.9027, 2.9564, 2.9989, 3.0403, 3.0201]
hierarchy_std = [0.0282, 0.0251, 0.0254, 0.0274, 0.0276, 0.0270]

# Use equally spaced x positions
x = np.arange(len(top_n))

# =========================
# Plot
# =========================
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# -------- Exact Match --------
axes[0].errorbar(
    x,
    exact,
    yerr=exact_std,
    marker="o",
    linewidth=2,
    markersize=7,
    capsize=5
)

axes[0].set_title("Exact Match", fontsize=18)
axes[0].set_xlabel("Top-N Genes", fontsize=14)
axes[0].set_ylabel("Exact Match", fontsize=14)

axes[0].set_xticks(x)
axes[0].set_xticklabels(top_n)

axes[0].grid(axis="y", linestyle="--", alpha=0.5)
axes[0].tick_params(axis="both", labelsize=12)

# -------- Hierarchy Score --------
axes[1].errorbar(
    x,
    hierarchy,
    yerr=hierarchy_std,
    marker="o",
    linewidth=2,
    markersize=7,
    capsize=5
)

axes[1].set_title("Hierarchy Score", fontsize=18)
axes[1].set_xlabel("Top-N Genes", fontsize=14)
axes[1].set_ylabel("Hierarchy Score", fontsize=14)

axes[1].set_xticks(x)
axes[1].set_xticklabels(top_n)

axes[1].grid(axis="y", linestyle="--", alpha=0.5)
axes[1].tick_params(axis="both", labelsize=12)

# Remove top/right borders
for ax in axes:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

plt.tight_layout()

# Save for paper/presentation
plt.savefig(
    "hlca_topgene.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "hlca_topgene.pdf",
    bbox_inches="tight"
)

plt.show()