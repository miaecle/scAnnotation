import matplotlib.pyplot as plt
import numpy as np

# =========================
# Data
# =========================
knn_k = [5, 10, 20, 50, 100]

exact = [0.4485, 0.4385, 0.4452, 0.4262, 0.4116]
exact_std = [0.0093, 0.0093, 0.0091, 0.0100, 0.0097]

hierarchy = [3.0962, 3.0794, 3.0638, 3.0347, 2.9687]
hierarchy_std = [0.0249, 0.0255, 0.0241, 0.0259, 0.0261]

# 等间距横坐标，风格和你前面的图一致
x = np.arange(len(knn_k))

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
axes[0].set_xlabel("KNN k", fontsize=14)
axes[0].set_ylabel("Exact Match", fontsize=14)

axes[0].set_xticks(x)
axes[0].set_xticklabels(knn_k)

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
axes[1].set_xlabel("KNN k", fontsize=14)
axes[1].set_ylabel("Hierarchy Score", fontsize=14)

axes[1].set_xticks(x)
axes[1].set_xticklabels(knn_k)

axes[1].grid(axis="y", linestyle="--", alpha=0.5)
axes[1].tick_params(axis="both", labelsize=12)

# 去掉上边框和右边框
for ax in axes:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

plt.tight_layout()

# 保存
plt.savefig("hlca_knn.png", dpi=300, bbox_inches="tight")
plt.savefig("hlca_knn.pdf", bbox_inches="tight")
plt.show()