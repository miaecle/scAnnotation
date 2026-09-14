import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# Labels
# --------------------------------------------------
models = [
    "DS-V4-Flash",
    "DS-V4-Pro",
    "Gemini-3.5-Flash",
    "Qwen-3.7-Plus",
    "GPT-5.6-Luna",
]

x = np.arange(len(models))
width = 0.35

# --------------------------------------------------
# Exact Match
# --------------------------------------------------
exact_stg1 = np.array([0.4385, 0.5011, 0.5660, 0.4374, 0.5145])
exact_tirosh = np.array([0.4642, 0.5067, 0.5738, 0.4642, 0.5414])

exact_std_stg1 = np.array([0.0093, 0.0103, 0.0110, 0.0101, 0.0103])
exact_std_tirosh = np.array([0.0105, 0.0107, 0.0110, 0.0104, 0.0113])

# --------------------------------------------------
# Hierarchy Score
# --------------------------------------------------
hierarchy_stg1 = np.array([3.0794, 3.1857, 3.3154, 3.0604, 3.2025])
hierarchy_tirosh = np.array([3.1365, 3.1924, 3.3289, 3.1107, 3.2338])

hierarchy_std_stg1 = np.array([0.0255, 0.0260, 0.0242, 0.0258, 0.0251])
hierarchy_std_tirosh = np.array([0.0253, 0.0267, 0.0243, 0.0251, 0.0272])

# --------------------------------------------------
# L1 / L2 / L3 for Tirosh only
# --------------------------------------------------
l1_tirosh = np.array([0.9843, 0.9832, 0.9877, 0.9855, 0.9843])
l2_tirosh = np.array([0.9217, 0.9094, 0.9430, 0.9083, 0.9139])
l3_tirosh = np.array([0.7662, 0.7931, 0.8244, 0.7528, 0.7942])

l1_std_tirosh = np.array([0.0041, 0.0042, 0.0037, 0.0038, 0.0041])
l2_std_tirosh = np.array([0.0078, 0.0077, 0.0069, 0.0076, 0.0080])
l3_std_tirosh = np.array([0.0101, 0.0102, 0.0095, 0.0102, 0.0107])

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
# Create figure
# --------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(16, 4.8))

# ==================================================
# Plot 1: Exact Match
# ==================================================
ax = axes[0]

ax.bar(
    x - width / 2,
    exact_stg1,
    width,
    yerr=exact_std_stg1,
    capsize=3,
    label="Stage 1",
)

ax.bar(
    x + width / 2,
    exact_tirosh,
    width,
    yerr=exact_std_tirosh,
    capsize=3,
    label="Tirosh",
)

# Random guess baseline
ax.axhline(
    random_baseline["Exact Match"],
    linestyle="--",
    linewidth=1.5,
    label="Random Guess",
)

ax.axhspan(
    random_baseline_ci["Exact Match"][0],
    random_baseline_ci["Exact Match"][1],
    alpha=0.30,
)

ax.set_xticks(x)
ax.set_xticklabels(models, rotation=30, ha="right")
ax.set_title("Exact Match")
ax.set_ylabel("Exact Match")
ax.set_ylim(0, 0.65)

ax.grid(axis="y", linestyle="--", linewidth=0.6, alpha=0.4)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.legend(frameon=False)

# ==================================================
# Plot 2: Hierarchy Score
# ==================================================
ax = axes[1]

ax.bar(
    x - width / 2,
    hierarchy_stg1,
    width,
    yerr=hierarchy_std_stg1,
    capsize=3,
    label="Stage 1",
)

ax.bar(
    x + width / 2,
    hierarchy_tirosh,
    width,
    yerr=hierarchy_std_tirosh,
    capsize=3,
    label="Tirosh",
)

# Random guess baseline
ax.axhline(
    random_baseline["Hierarchy Score"],
    linestyle="--",
    linewidth=1.5,
    label="Random Guess",
)

ax.axhspan(
    random_baseline_ci["Hierarchy Score"][0],
    random_baseline_ci["Hierarchy Score"][1],
    alpha=0.30,
)

ax.set_xticks(x)
ax.set_xticklabels(models, rotation=30, ha="right")
ax.set_title("Hierarchy Score")
ax.set_ylabel("Hierarchy Score")
ax.set_ylim(0, 3.6)

ax.grid(axis="y", linestyle="--", linewidth=0.6, alpha=0.4)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# ==================================================
# Plot 3: L1 / L2 / L3 trend (Tirosh only)
# ==================================================
ax = axes[2]

levels = ["L1", "L2", "L3", "L4*"]
x_levels = np.arange(len(levels))

for i, model in enumerate(models):
    y = [l1_tirosh[i], l2_tirosh[i], l3_tirosh[i], exact_tirosh[i]]
    yerr = [l1_std_tirosh[i], l2_std_tirosh[i], l3_std_tirosh[i], exact_std_tirosh[i]]

    ax.errorbar(
        x_levels,
        y,
        yerr=yerr,
        marker="o",
        linewidth=1.6,
        capsize=3,
        label=model,
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
ax.set_xticklabels(levels)
ax.set_title("Hierarchical Match Trend (Tirosh)")
ax.set_ylabel("Match Rate")
ax.set_ylim(0, 1.00)

ax.grid(axis="y", linestyle="--", linewidth=0.6, alpha=0.4)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.legend(frameon=False, fontsize=8)

# --------------------------------------------------
# Save and show
# --------------------------------------------------
plt.tight_layout()
plt.savefig("hlca_llm_with_random_baseline.png", dpi=300, bbox_inches="tight")
plt.savefig("hlca_llm_with_random_baseline.pdf", bbox_inches="tight")
plt.show()