"""Visualization helpers for annotation experiment outputs."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix


def save_confusion_matrix(
    results_df: pd.DataFrame,
    save_path: str,
    cell_type_list: list,
) -> None:
    """Generate and save a row-normalized confusion matrix PNG."""
    labels = list(cell_type_list) if cell_type_list else sorted(results_df["true_label"].unique().tolist())
    y_true = results_df["true_label"]
    y_pred_raw = results_df["pred_celltype"].fillna("").astype(str).str.strip()

    valid_labels = set(labels)
    y_pred = y_pred_raw.where(y_pred_raw.isin(valid_labels), "SKIPPED")
    if (y_pred == "SKIPPED").any() and "SKIPPED" not in labels:
        labels.append("SKIPPED")

    cm = confusion_matrix(y_true, y_pred, labels=labels)
    row_sums = cm.sum(axis=1, keepdims=True)
    cm_norm = np.divide(cm.astype(float), row_sums, where=row_sums != 0)

    n = len(labels)
    fig_size = max(8, n * 0.6)
    fig, ax = plt.subplots(figsize=(fig_size, fig_size * 0.85))
    sns.heatmap(
        cm_norm,
        annot=True,
        fmt=".2f",
        xticklabels=labels,
        yticklabels=labels,
        cmap="Blues",
        vmin=0,
        vmax=1,
        ax=ax,
        linewidths=0.4,
        linecolor="#dddddd",
    )
    ax.set_xlabel("Predicted", fontsize=11)
    ax.set_ylabel("True", fontsize=11)
    ax.set_title("Confusion Matrix (row-normalised)", fontsize=13)
    plt.xticks(rotation=45, ha="right", fontsize=8)
    plt.yticks(rotation=0, fontsize=8)
    plt.tight_layout()
    fig.savefig(save_path, dpi=150)
    plt.close(fig)
    print(f"  Confusion matrix saved → {save_path}")