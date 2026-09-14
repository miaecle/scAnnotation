"""Human-readable report exporters used by the pipeline."""

from __future__ import annotations

import json
import os
from typing import Any


def save_inspect_pretty(records: list[dict[str, Any]], save_path: str) -> None:
    """Write a human-readable Markdown view of inspect traces."""
    base, _ = os.path.splitext(save_path)
    pretty_path = f"{base}_pretty.md"

    def _render_value(value: Any) -> str:
        if isinstance(value, (dict, list)):
            return json.dumps(value, ensure_ascii=False, indent=2)
        return str(value)

    with open(pretty_path, "w", encoding="utf-8") as fh:
        fh.write("# Inspect Traces\n\n")
        fh.write(f"Total records: {len(records)}\n\n")

        for i, record in enumerate(records, start=1):
            fh.write(f"## Record {i}\n\n")

            meta_keys = [
                "stage",
                "row_idx",
                "cell_idx",
                "cell_barcode",
                "true_label",
                "stage1_label",
                "error_type",
                "error_code",
                "error_message",
            ]
            for key in meta_keys:
                if key in record:
                    fh.write(f"- {key}: {_render_value(record[key])}\n")

            body_keys = [
                "stage1_reasoning",
                "prompt_prefix",
                "prompt",
                "full_prompt",
                "output",
            ]
            for key in body_keys:
                if key in record:
                    fh.write(f"\n### {key}\n\n")
                    fh.write("```text\n")
                    fh.write(_render_value(record[key]))
                    fh.write("\n```\n")

            fh.write("\n")

    print(f"Inspect pretty report saved -> {pretty_path}")


def save_stage2_program_cache_pretty(payload: dict[str, Any], save_path: str) -> None:
    """Write a human-readable Markdown view of stage-2 precomputed programs."""
    base, _ = os.path.splitext(save_path)
    pretty_path = f"{base}_pretty.md"

    programs_by_cell_type = payload.get("programs_by_cell_type", {})

    with open(pretty_path, "w", encoding="utf-8") as fh:
        fh.write("# Stage-2 Precomputed Programs\n\n")
        fh.write(f"- tissue: {payload.get('tissue', '')}\n")
        fh.write(f"- n_program_genes: {payload.get('n_program_genes', '')}\n")
        fh.write(f"- n_cached_cell_types: {payload.get('n_cached_cell_types', 0)}\n\n")

        if not isinstance(programs_by_cell_type, dict) or not programs_by_cell_type:
            fh.write("No precomputed programs were saved.\n")
            print(f"Stage-2 precomputed programs pretty report saved -> {pretty_path}")
            return

        for cell_type in sorted(programs_by_cell_type.keys()):
            fh.write(f"## {cell_type}\n\n")
            subtype_map = programs_by_cell_type.get(cell_type, {})
            if not isinstance(subtype_map, dict) or not subtype_map:
                fh.write("No subtype programs.\n\n")
                continue

            for subtype in sorted(subtype_map.keys()):
                info = subtype_map.get(subtype, {})
                description = ""
                genes: list[str] = []
                if isinstance(info, dict):
                    description = str(info.get("description", "")).strip()
                    raw_genes = info.get("genes", [])
                    if isinstance(raw_genes, list):
                        genes = [str(g) for g in raw_genes]

                fh.write(f"### {subtype}\n\n")
                fh.write(f"Description: {description or '(empty)'}\n\n")
                fh.write("Genes:\n")
                if genes:
                    # Chunk long gene lists so each line stays readable in Markdown.
                    for i in range(0, len(genes), 12):
                        fh.write(f"- {', '.join(genes[i:i+12])}\n")
                else:
                    fh.write("- (none)\n")
                fh.write("\n")

    print(f"Stage-2 precomputed programs pretty report saved -> {pretty_path}")
