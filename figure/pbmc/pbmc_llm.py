import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# Models
# --------------------------------------------------
models = [
    "ds-v4-flash",
    "ds-v4-pro",
    "gm-3.5-flash",
    "qwen3.7-plus",
    "gpt-5.6-luna",
]


# --------------------------------------------------
# Exact Match
# --------------------------------------------------
exact_a = np.array([
    0.5984,
    0.5661,
    0.7677,
    0.5870,
    0.5935,
])

exact_b = np.array([
    0.6339,
    0.5581,
    0.7790,
    0.5968,
    0.6210,
])


# --------------------------------------------------
# Standard deviation
# --------------------------------------------------
exact_std_a = np.array([
    0.0134,
    0.0145,
    0.0125,
    0.0130,
    0.0147,
])

exact_std_b = np.array([
    0.0140,
    0.0156,
    0.0131,
    0.0134,
    0.0150,
])


# --------------------------------------------------
# PBMC Random Guess Baseline
# --------------------------------------------------
random_mean = 0.0258
random_std = 0.0063

random_ci_low = 0.0145
random_ci_high = 0.0387


# --------------------------------------------------
# Plot settings
# --------------------------------------------------
x = np.arange(len(models))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 4.5))


# --------------------------------------------------
# Stage 1
# --------------------------------------------------
ax.bar(
    x - width / 2,
    exact_a,
    width,
    yerr=exact_std_a,
    capsize=3,
    label="Stage 1",
)


# --------------------------------------------------
# Stage 2
# --------------------------------------------------
ax.bar(
    x + width / 2,
    exact_b,
    width,
    yerr=exact_std_b,
    capsize=3,
    label="Stage 2 (Tirosh)",
)


# --------------------------------------------------
# Random Guess Baseline
# --------------------------------------------------
ax.axhline(
    random_mean,
    linestyle="--",
    linewidth=1.6,
    label="Random Guess",
)

# 95% CI of random guess
ax.axhspan(
    random_ci_low,
    random_ci_high,
    alpha=0.30,
)


# --------------------------------------------------
# Axis settings
# --------------------------------------------------
ax.set_xticks(x)
ax.set_xticklabels(
    models,
    rotation=30,
    ha="right",
)

ax.set_ylabel("Exact Match")
ax.set_title("Model Comparison on Exact Match")

ax.set_ylim(0.0, 1.0)


# --------------------------------------------------
# Grid
# --------------------------------------------------
ax.grid(
    axis="y",
    linestyle="--",
    linewidth=0.6,
    alpha=0.4,
)


# --------------------------------------------------
# Remove top/right spines
# --------------------------------------------------
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)


# --------------------------------------------------
# Legend
# --------------------------------------------------
handles, labels = ax.get_legend_handles_labels()

desired_order = [
    "Random Guess",
    "Stage 1",
    "Stage 2 (Tirosh)",
]

label_to_handle = dict(zip(labels, handles))

ordered_handles = [
    label_to_handle[label]
    for label in desired_order
]

ax.legend(
    ordered_handles,
    desired_order,
    frameon=False,
)


# --------------------------------------------------
# Layout
# --------------------------------------------------
plt.tight_layout()


# --------------------------------------------------
# Save
# --------------------------------------------------
plt.savefig(
    "pbmc_llm_with_random_baseline.png",
    dpi=300,
    bbox_inches="tight",
)

plt.savefig(
    "pbmc_llm_with_random_baseline.pdf",
    bbox_inches="tight",
)

plt.show()