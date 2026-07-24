"""Stage-2 cell type refinement: LLM-queried gene programs, pathway scoring, final reasoning.

Workflow
--------
1. :func:`make_gemini_json_caller` / :func:`make_openai_json_caller` — build a reusable
   JSON-mode caller (once per session).
2. :func:`query_subtype_programs` — ask the LLM for fine-grained subtype programs based
   on a stage-1 label. Also includes commonly confused neighboring cell types so pathway
   scoring can confirm or override the stage-1 call.
3. :func:`filter_programs_to_panel` — intersect gene lists with the dataset's gene panel.
4. :func:`score_gene_programs` — compute mean z-score per program for a cell.
5. :func:`build_stage2_prompt` — build the final prompt combining genes, proteins, and
   pathway scores; instructs the LLM to confirm or correct the stage-1 label.
"""

from __future__ import annotations

import json
import time
from typing import Any, Callable, Optional

import numpy as np
import pandas as pd
import anndata as ad


# ─── Backend factory ────────────────────────────────────────────────────────


def _fmt_numeric(value: float, decimals: int = 3) -> str:
    return f"{value:.{decimals}f}"


def _extract_first_json_object(text: str) -> dict:
    """Parse a JSON object, tolerating extra text around the first object."""
    text = text.strip()
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as exc:
        if "Extra data" not in str(exc):
            raise

        depth = 0
        in_string = False
        escape = False
        for i, ch in enumerate(text):
            if escape:
                escape = False
                continue
            if ch == "\\":
                escape = True
                continue
            if ch == '"':
                in_string = not in_string
                continue
            if in_string:
                continue
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            if depth == 0:
                parsed = json.loads(text[: i + 1])
                break
        else:
            raise
    if not isinstance(parsed, dict):
        raise ValueError(f"Expected a JSON object, got {type(parsed).__name__}. Raw response: {text!r}")
    return parsed


def _validate_programs_payload(programs: dict) -> dict[str, dict[str, object]]:
    """Validate the strict stage-2 schema returned by the LLM.

    Expected form:
    ``{subtype_name: {"genes": [...], "description": "..."}}``.
    """
    if not isinstance(programs, dict):
        raise TypeError(
            f"Expected stage-2 programs to be a dict, got {type(programs).__name__}: {programs!r}"
        )

    validated: dict[str, dict[str, object]] = {}
    for subtype, info in programs.items():
        if not isinstance(info, dict):
            raise TypeError(
                "Each stage-2 subtype entry must be a dict with 'genes' and 'description'; "
                f"got {type(info).__name__} for {subtype!r}: {info!r}"
            )

        if "genes" not in info or "description" not in info:
            raise ValueError(
                f"Stage-2 subtype {subtype!r} must include both 'genes' and 'description': {info!r}"
            )

        genes = info["genes"]
        description = info["description"]

        if not isinstance(genes, list):
            raise TypeError(
                f"Stage-2 subtype {subtype!r} has non-list genes payload {type(genes).__name__}: {genes!r}"
            )
        if not isinstance(description, str) or not description.strip():
            raise ValueError(
                f"Stage-2 subtype {subtype!r} has missing/empty description: {description!r}"
            )

        cleaned_genes = []
        for gene in genes:
            if not isinstance(gene, str) or not gene.strip():
                raise ValueError(
                    f"Stage-2 subtype {subtype!r} contains an invalid gene entry: {gene!r}"
                )
            cleaned_genes.append(gene.strip())

        if not cleaned_genes:
            raise ValueError(f"Stage-2 subtype {subtype!r} has an empty genes list.")

        validated[str(subtype)] = {
            "genes": cleaned_genes,
            "description": description.strip(),
        }

    if not validated:
        raise ValueError("Stage-2 program payload is empty.")

    return validated


def make_gemini_json_caller(
    model: str = "gemini-3.5-flash",
    api_key: str | None = None,
    max_output_tokens: int = 8192,
    thinking_budget: int | None = 0,
    use_context_cache: bool = False,
    context_cache_ttl_seconds: int = 3600,
    max_retries: int = 3,
    base_sleep: float = 2.0,
    max_sleep: float = 30.0,
    usage_sink: Callable[[dict[str, Any]], None] | None = None,
):
    """Return a callable ``(prompt, system_message, cached_user_prefix=None, cache_key=None) -> dict``.

    Using ``response_mime_type='application/json'`` activates constrained decoding,
    which guarantees structurally valid JSON output regardless of content length.

    Args:
        model: Gemini model ID (e.g. ``'gemini-3.5-flash'``, ``'gemini-3.0-flash'``).
        api_key: Google API key. Reads ``GOOGLE_API_KEY`` env var if ``None``.
        max_output_tokens: Total output token budget for each call.
        thinking_budget:
            ``0``    — disable thinking entirely (recommended for structured lookups;
                       avoids the Gemini 3.5 series consuming most of the output budget
                       on hidden chain-of-thought before a single JSON token is written).
            ``None`` — use the model default (problematic on 3.5-series with small budgets).
            ``int>0`` — explicit cap for tasks that benefit from light reasoning.
    """
    from google import genai
    from google.genai import types as _gtypes

    client = genai.Client(api_key=api_key)
    context_cache_names: dict[str, str | None] = {}
    usage_history: list[dict] = []
    last_usage: dict | None = None
    if context_cache_ttl_seconds <= 0:
        raise ValueError("context_cache_ttl_seconds must be > 0.")

    def _is_cache_too_small_error(exc: Exception) -> bool:
        msg = str(exc)
        return "Cached content is too small" in msg or "min_total_token_count" in msg

    def _make_cache_lookup_key(system_message: str, cached_user_prefix: str | None, cache_key: str | None) -> str:
        if cache_key:
            return cache_key
        return f"sys::{system_message}\nuser::{cached_user_prefix or ''}"

    def _get_cached_content_name(
        system_message: str,
        cached_user_prefix: str | None = None,
        cache_key: str | None = None,
    ) -> str | None:
        if not use_context_cache:
            return None
        if not system_message and not cached_user_prefix:
            return None

        lookup_key = _make_cache_lookup_key(system_message, cached_user_prefix, cache_key)
        if lookup_key in context_cache_names:
            return context_cache_names[lookup_key]

        try:
            cache_cfg: dict = {
                "ttl": f"{context_cache_ttl_seconds}s",
            }
            if system_message:
                cache_cfg["system_instruction"] = system_message
            if cached_user_prefix:
                cache_cfg["contents"] = cached_user_prefix
            cached_content = client.caches.create(
                model=model,
                config=_gtypes.CreateCachedContentConfig(**cache_cfg),
            )
            cache_name = getattr(cached_content, "name", None)
            if not cache_name:
                raise RuntimeError(f"Gemini cache creation returned no name. Raw response: {cached_content!r}")
        except Exception as exc:
            if _is_cache_too_small_error(exc):
                context_cache_names[lookup_key] = None
                return None
            raise

        context_cache_names[lookup_key] = cache_name
        return cache_name

    def _to_int(value) -> int | None:
        if value is None:
            return None
        try:
            return int(value)
        except (TypeError, ValueError):
            return None

    def _record_usage(resp, cache_used: bool) -> None:
        nonlocal last_usage
        usage = getattr(resp, "usage_metadata", None)
        payload = {
            "provider": "gemini",
            "backend": "GeminiJSONCaller",
            "model": model,
            "input_tokens": _to_int(getattr(usage, "prompt_token_count", None)),
            "output_tokens": _to_int(getattr(usage, "candidates_token_count", None)),
            "total_tokens": _to_int(getattr(usage, "total_token_count", None)),
            "cached_input_tokens": _to_int(getattr(usage, "cached_content_token_count", None)),
            "thoughts_tokens": _to_int(getattr(usage, "thoughts_token_count", None)),
            "cache_used": bool(cache_used),
            "recorded_at_unix": time.time(),
        }
        usage_history.append(payload)
        last_usage = payload

    def _call(
        prompt: str,
        system_message: str = "",
        cached_user_prefix: str | None = None,
        cache_key: str | None = None,
        usage_context: dict[str, Any] | None = None,
    ) -> dict:
        cfg: dict = dict(
            max_output_tokens=max_output_tokens,
            temperature=0.0,
            response_mime_type="application/json",
        )
        cache_name = _get_cached_content_name(
            system_message=system_message,
            cached_user_prefix=cached_user_prefix,
            cache_key=cache_key,
        )
        if cache_name:
            cfg["cached_content"] = cache_name
        elif system_message:
            cfg["system_instruction"] = system_message
        if thinking_budget is not None:
            cfg["thinking_config"] = _gtypes.ThinkingConfig(thinking_budget=thinking_budget)

        contents = prompt
        if cached_user_prefix and not cache_name:
            contents = f"{cached_user_prefix}\n\n{prompt}" if prompt else cached_user_prefix

        prompt_payload = {
            "prompt_user_message": contents,
            "prompt_system_message": system_message,
        }

        last_error: Exception | None = None
        total_attempts = max_retries + 1
        for attempt in range(total_attempts):
            started_at = time.time()
            attempt_no = attempt + 1
            try:
                resp = client.models.generate_content(
                    model=model,
                    contents=contents,
                    config=_gtypes.GenerateContentConfig(**cfg),
                )
                _record_usage(resp, cache_used=bool(cache_name))
                text = (resp.text or "").strip()
                if not text:
                    raise ValueError("Gemini returned an empty response.")

                try:
                    parsed = _extract_first_json_object(text)
                    if usage_sink is not None:
                        payload = dict(last_usage or {})
                        payload.update(
                            {
                                **prompt_payload,
                                "attempt": attempt_no,
                                "total_attempts": total_attempts,
                                "attempt_status": "success",
                                "will_retry": False,
                                "duration_ms": int((time.time() - started_at) * 1000),
                                "response_chars": len(text),
                                "recorded_at_unix": time.time(),
                            }
                        )
                        if usage_context:
                            payload.update(usage_context)
                        usage_sink(payload)
                    return parsed
                except Exception as exc:
                    is_final = attempt == max_retries
                    if usage_sink is not None:
                        payload = dict(last_usage or {})
                        payload.update(
                            {
                                **prompt_payload,
                                "attempt": attempt_no,
                                "total_attempts": total_attempts,
                                "attempt_status": "final_failure" if is_final else "format_error",
                                "error_type": type(exc).__name__,
                                "error_message": f"Gemini returned invalid JSON: {exc}",
                                "will_retry": not is_final,
                                "duration_ms": int((time.time() - started_at) * 1000),
                                "response_chars": len(text),
                                "response_text": text,
                                "recorded_at_unix": time.time(),
                            }
                        )
                        if usage_context:
                            payload.update(usage_context)
                        usage_sink(payload)
                    raise ValueError(
                        f"Gemini returned invalid JSON: {exc}\n\nRaw response:\n{text}"
                    ) from exc
            except Exception as exc:
                last_error = exc
                is_final = attempt == max_retries
                if usage_sink is not None and (
                    not isinstance(exc, ValueError)
                    or "invalid JSON" not in str(exc)
                ):
                    payload = dict(last_usage or {})
                    payload.update(
                        {
                            "provider": payload.get("provider", "gemini"),
                            "backend": payload.get("backend", "GeminiJSONCaller"),
                            "model": payload.get("model", model),
                            **prompt_payload,
                            "attempt": attempt_no,
                            "total_attempts": total_attempts,
                            "attempt_status": "final_failure" if is_final else "retry_error",
                            "error_type": type(exc).__name__,
                            "error_message": str(exc),
                            "will_retry": not is_final,
                            "duration_ms": int((time.time() - started_at) * 1000),
                            "recorded_at_unix": time.time(),
                        }
                    )
                    if usage_context:
                        payload.update(usage_context)
                    usage_sink(payload)

                if is_final:
                    break

                sleep_s = min(base_sleep * (2 ** attempt), max_sleep)
                print(
                    f"Stage-2 Gemini JSON query failed ({type(exc).__name__}: {exc}). "
                    f"Retrying {attempt + 1}/{max_retries} after {sleep_s:.1f}s..."
                )
                time.sleep(sleep_s)

        raise RuntimeError(
            f"Stage-2 Gemini JSON query failed after {total_attempts} attempts."
            f"Raw prompt:\n{prompt}\n\n"
        ) from last_error

    def _get_last_usage() -> dict | None:
        return dict(last_usage) if last_usage is not None else None

    def _get_usage_history() -> list[dict]:
        return [dict(item) for item in usage_history]

    _call.get_last_usage = _get_last_usage
    _call.get_usage_history = _get_usage_history
    return _call


def make_openai_json_caller(
    model: str = "gpt-4o",
    api_key: str | None = None,
    base_url: str | None = None,
    max_output_tokens: int = 8192,
    max_retries: int = 3,
    base_sleep: float = 2.0,
    max_sleep: float = 30.0,
    usage_sink: Callable[[dict[str, Any]], None] | None = None,
):
    """Return a callable ``(prompt, system_message, cached_user_prefix=None, cache_key=None) -> dict``.

    This works for OpenAI-compatible APIs such as OpenAI and DeepSeek.
    """
    import openai

    client = openai.OpenAI(api_key=api_key, base_url=base_url) if base_url else openai.OpenAI(api_key=api_key)
    usage_history: list[dict] = []
    last_usage: dict | None = None
    provider = "deepseek" if base_url and "deepseek" in base_url else "openai"
    supports_response_format = True

    def _to_int(value) -> int | None:
        if value is None:
            return None
        try:
            return int(value)
        except (TypeError, ValueError):
            return None

    def _record_usage(resp) -> None:
        nonlocal last_usage
        usage = getattr(resp, "usage", None)
        prompt_details = getattr(usage, "prompt_tokens_details", None)
        completion_details = getattr(usage, "completion_tokens_details", None)
        payload = {
            "provider": provider,
            "backend": "OpenAIJSONCaller",
            "model": model,
            "input_tokens": _to_int(getattr(usage, "prompt_tokens", None)),
            "output_tokens": _to_int(getattr(usage, "completion_tokens", None)),
            "total_tokens": _to_int(getattr(usage, "total_tokens", None)),
            "cached_input_tokens": _to_int(getattr(prompt_details, "cached_tokens", None)),
            "reasoning_tokens": _to_int(getattr(completion_details, "reasoning_tokens", None)),
            "audio_input_tokens": _to_int(getattr(prompt_details, "audio_tokens", None)),
            "audio_output_tokens": _to_int(getattr(completion_details, "audio_tokens", None)),
            "recorded_at_unix": time.time(),
        }
        usage_history.append(payload)
        last_usage = payload

    def _call(
        prompt: str,
        system_message: str = "",
        cached_user_prefix: str | None = None,
        cache_key: str | None = None,
        usage_context: dict[str, Any] | None = None,
    ) -> dict:
        nonlocal supports_response_format
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})

        contents = prompt
        if cached_user_prefix:
            contents = f"{cached_user_prefix}\n\n{prompt}" if prompt else cached_user_prefix
        messages.append({"role": "user", "content": contents})

        prompt_payload = {
            "prompt_user_message": contents,
            "prompt_system_message": system_message,
        }

        last_error: Exception | None = None
        total_attempts = max_retries + 1
        for attempt in range(total_attempts):
            started_at = time.time()
            attempt_no = attempt + 1
            try:
                kwargs: dict = dict(
                    model=model,
                    messages=messages,
                    max_tokens=max_output_tokens,
                    temperature=0.0,
                )
                if supports_response_format:
                    kwargs["response_format"] = {"type": "json_object"}
                resp = client.chat.completions.create(**kwargs)
                _record_usage(resp)
                text = (resp.choices[0].message.content or "").strip()
                if not text:
                    raise ValueError("OpenAI-compatible backend returned an empty response.")
                try:
                    parsed = _extract_first_json_object(text)
                    if usage_sink is not None:
                        payload = dict(last_usage or {})
                        payload.update(
                            {
                                **prompt_payload,
                                "attempt": attempt_no,
                                "total_attempts": total_attempts,
                                "attempt_status": "success",
                                "will_retry": False,
                                "duration_ms": int((time.time() - started_at) * 1000),
                                "response_chars": len(text),
                                "recorded_at_unix": time.time(),
                            }
                        )
                        if usage_context:
                            payload.update(usage_context)
                        usage_sink(payload)
                    return parsed
                except Exception as exc:
                    is_final = attempt == max_retries
                    if usage_sink is not None:
                        payload = dict(last_usage or {})
                        payload.update(
                            {
                                **prompt_payload,
                                "attempt": attempt_no,
                                "total_attempts": total_attempts,
                                "attempt_status": "final_failure" if is_final else "format_error",
                                "error_type": type(exc).__name__,
                                "error_message": f"OpenAI-compatible backend returned invalid JSON: {exc}",
                                "will_retry": not is_final,
                                "duration_ms": int((time.time() - started_at) * 1000),
                                "response_chars": len(text),
                                "response_text": text,
                                "recorded_at_unix": time.time(),
                            }
                        )
                        if usage_context:
                            payload.update(usage_context)
                        usage_sink(payload)
                    raise ValueError(
                        f"OpenAI-compatible backend returned invalid JSON: {exc}"
                    ) from exc
            except Exception as exc:
                if supports_response_format and "response_format" in str(exc).lower():
                    supports_response_format = False
                last_error = exc
                is_final = attempt == max_retries
                if usage_sink is not None and (
                    not isinstance(exc, ValueError)
                    or "invalid JSON" not in str(exc)
                ):
                    payload = dict(last_usage or {})
                    payload.update(
                        {
                            "provider": payload.get("provider", provider),
                            "backend": payload.get("backend", "OpenAIJSONCaller"),
                            "model": payload.get("model", model),
                            **prompt_payload,
                            "attempt": attempt_no,
                            "total_attempts": total_attempts,
                            "attempt_status": "final_failure" if is_final else "retry_error",
                            "error_type": type(exc).__name__,
                            "error_message": str(exc),
                            "will_retry": not is_final,
                            "duration_ms": int((time.time() - started_at) * 1000),
                            "recorded_at_unix": time.time(),
                        }
                    )
                    if usage_context:
                        payload.update(usage_context)
                    usage_sink(payload)

                if is_final:
                    break

                sleep_s = min(base_sleep * (2 ** attempt), max_sleep)
                print(
                    f"Stage-2 JSON query failed ({type(exc).__name__}: {exc}). "
                    f"Retrying {attempt + 1}/{max_retries} after {sleep_s:.1f}s..."
                )
                time.sleep(sleep_s)

        raise RuntimeError(
            f"Stage-2 JSON query failed after {total_attempts} attempts.\n"
            f"Raw prompt:\n{prompt}\n\n"
        ) from last_error

    def _get_last_usage() -> dict | None:
        return dict(last_usage) if last_usage is not None else None

    def _get_usage_history() -> list[dict]:
        return [dict(item) for item in usage_history]

    _call.get_last_usage = _get_last_usage
    _call.get_usage_history = _get_usage_history
    return _call


# ─── Step 1: query gene programs ────────────────────────────────────────────

_PROGRAM_SYSTEM = (
    "You are an expert computational biologist specializing in single-cell transcriptomics. "
    "Respond ONLY with a valid JSON object."
)


def query_subtype_programs(
    stage1_label: str,
    json_caller,
    tissue: str = "PBMC",
    n_genes: int = 30,
    stage1_reasoning: str | None = None,
    usage_sink: Callable[[dict[str, Any]], None] | None = None,
    usage_context: dict[str, Any] | None = None,
) -> dict:
    """Query the LLM for fine-grained subtype programs based on a stage-1 annotation.

    The returned programs cover:
    - Fine-grained subtypes of the predicted cell type.
    - The most commonly confused neighboring cell types in the same tissue.

    This means pathway scoring can both confirm the stage-1 label (if the predicted
    subtype scores highest) and detect outright misclassifications (if a neighboring
    type scores much higher).

    Args:
        stage1_label: Cell type string from stage-1 annotation (may be approximate /
            verbose, e.g. "CD8+ Cytotoxic T Cell (likely memory/effector)").
        json_caller: Callable from :func:`make_gemini_json_caller`.
        tissue: Tissue context, e.g. ``"PBMC"``, ``"lymph node"``.
        n_genes: Requested number of marker genes per program.
        stage1_reasoning: Full rationale text from the stage-1 LLM response.
            When provided, the LLM can use it to understand *which* genes and
            proteins drove the stage-1 call, and therefore which subtypes or
            confused neighbors are most relevant to include.

    Returns:
        Raw dict ``{subtype_name: {"genes": [...], "description": "..."}}``.
        Call :func:`filter_programs_to_panel` before passing to :func:`score_gene_programs`.
    """
    reasoning_block = (
        f"\nStage-1 reasoning that led to this annotation:\n{stage1_reasoning}\n"
        if stage1_reasoning
        else ""
    )
    cached_user_prefix = (
        f"This annotation may have minor inaccuracies, or may have been confused with a neighboring type.\n\n"
        f"Return a JSON object with gene programs for:\n"
        f"  1. The fine-grained subtypes of this cell type commonly found in {tissue}.\n"
        f"  2. The most commonly confused neighboring cell types in {tissue} — especially any\n"
        f"     types hinted at by the stage-1 reasoning above.\n\n"
        f"Each key is a subtype/cell-type name; each value contains:\n"
        f'  "genes": list anywhere from 20 to {n_genes} genes most specifically UPREGULATED in that '
        f"subtype (HGNC symbols as they appear in RNA-seq count matrices, e.g. NKG7 not Nkg7)\n"
        f'  "description": one-sentence biological description\n\n'
        f"Include 3-5 subtypes total. Focus on subtypes commonly found in {tissue}.\n"
        f"Return only the JSON."
    )
    prompt = (
        f'A single cell in {tissue} was annotated in a first pass as: "{stage1_label}"\n'
        f"{reasoning_block}"
    )
    full_user_prompt = f"{cached_user_prefix}\n\n{prompt}"
    last_error: Exception | None = None
    max_schema_attempts = 3
    for attempt in range(max_schema_attempts):
        raw_programs = json_caller(
            prompt,
            _PROGRAM_SYSTEM,
            cached_user_prefix=cached_user_prefix,
            cache_key=f"stage2_program_query::{tissue}::{n_genes}",
            usage_context=usage_context,
        )
        try:
            return _validate_programs_payload(raw_programs)
        except Exception as exc:
            last_error = exc
            is_final = attempt == max_schema_attempts - 1
            if usage_sink is not None:
                payload = {
                    "provider": "stage2",
                    "backend": "Stage2SchemaValidator",
                    "model": None,
                    "prompt_user_message": full_user_prompt,
                    "prompt_system_message": _PROGRAM_SYSTEM,
                    "attempt": attempt + 1,
                    "total_attempts": max_schema_attempts,
                    "attempt_status": "final_failure" if is_final else "format_error",
                    "error_type": type(exc).__name__,
                    "error_message": str(exc),
                    "will_retry": not is_final,
                    "duration_ms": 0,
                    "response_text": json.dumps(raw_programs, ensure_ascii=False),
                    "recorded_at_unix": time.time(),
                }
                if usage_context:
                    payload.update(usage_context)
                usage_sink(payload)
            if attempt == max_schema_attempts - 1:
                break
            sleep_s = min(2.0 * (2 ** attempt), 10.0)
            print(
                f"Stage-2 program schema validation failed ({type(exc).__name__}: {exc}). "
                f"Retrying {attempt + 2}/{max_schema_attempts} after {sleep_s:.1f}s..."
            )
            time.sleep(sleep_s)

    raise RuntimeError(
        f"Stage-2 program query returned invalid schema after {max_schema_attempts} attempts.\n"
        f"Expected each subtype to include both 'genes' and 'description'.\n"
        f"Raw prompt:\n{prompt}\n\n"
    ) from last_error


# ─── Step 2: filter programs to panel ───────────────────────────────────────

def filter_programs_to_panel(programs: dict, adata: ad.AnnData) -> dict:
    """Intersect each program's gene list with genes present in ``adata``.

    Uses ``adata.var['gene_symbol']`` when available, otherwise ``adata.var_names``.

    Returns:
        ``{subtype: [genes_in_panel, ...]}``.
    """
    programs = _validate_programs_payload(programs)
    symbols = (
        set(adata.var["gene_symbol"].dropna().values)
        if "gene_symbol" in adata.var.columns
        else set(adata.var_names)
    )
    return {
        subtype: [g for g in info["genes"] if g in symbols]
        for subtype, info in programs.items()
    }


# ─── Step 3: pathway scoring ─────────────────────────────────────────────────

def score_gene_programs(
    adata: ad.AnnData,
    cell_indices,
    programs_in_data: dict,
    gene_mask: np.ndarray,
    min_genes: int = 3,
    method: str = "tirosh",
    n_background: int = 50,
    random_state: int = 0,
) -> dict:
    """Score a cell against gene programs.

    Three methods are supported, selectable via ``method``:

    ``'mean_z'``
        Mean of ``(expr - μ) / σ`` over program genes (vs. full dataset population).
        Simple and fast; no background correction.  Can be inflated for globally
        active cells unless the gene_mask already removes housekeeping genes.

    ``'tirosh'`` *(default)*
        Replicates Scanpy ``score_genes`` (Tirosh 2016 / AddModuleScore):
        score = mean_z(program_genes) − mean_z(control_genes), where control
        genes are randomly sampled from the same expression-level bins as the
        program genes.  This cancels out global transcriptional activity bias and
        is the standard in cell type annotation workflows.

    ``'ucell'``
        Mann-Whitney U statistic on per-cell gene ranks, normalised to [0, 1].
        rank(g) = position of gene g in the descending expression ranking of all
        genes in the cell.  U = (Σ rank(g) − n*(n+1)/2) / (n * N) where n =
        program genes, N = total expressed genes.  Rank-based and dropout-robust;
        best practice per 2024 benchmarks (Massimo et al., Bioinformatics 2024).

    Args:
        programs_in_data: ``{subtype: [gene_symbols_in_panel]}``.
        gene_mask: Boolean array ``(n_vars,)`` — True = gene passes filter.
        min_genes: Minimum scoreable genes; returns NaN otherwise.
        method: One of ``'mean_z'``, ``'tirosh'``, ``'ucell'``.
        n_background: (``'tirosh'`` only) control genes per expression bin.
        random_state: (``'tirosh'`` only) seed for background sampling.

    Returns:
        ``{subtype: float}`` — NaN when fewer than ``min_genes`` genes are scoreable.
    """
    from sc_annotation.selection import compute_scores

    if method not in ("mean_z", "tirosh", "ucell"):
        raise ValueError(f"method must be 'mean_z', 'tirosh', or 'ucell'; got {method!r}")

    if method == "ucell":
        return _score_ucell(adata, cell_indices, programs_in_data, gene_mask, min_genes)

    z = compute_scores(adata, cell_indices, "zscore", gene_mask, mask_zeros=False)
    assert np.all(np.isfinite(z[gene_mask])), "infinite z-scores identified"

    # Precompute bin mapping once — shared across all programs in this call
    if method == "tirosh":
        rng = np.random.default_rng(random_state)
        mean_expr = adata.var["mean_expr"][gene_mask]
        bin_ids = _gene_to_bin(mean_expr)
        gene_to_bin_map = {g: int(b) for g, b in bin_ids.items() if not np.isnan(b)}
        bin_pool = _build_background_pool(mean_expr)

    out: dict = {}
    for subtype, genes in programs_in_data.items():
        valid = [g for g in genes if g in z.index and np.isfinite(z[g])]
        if len(valid) < min_genes:
            out[subtype] = float("nan")
            continue
        prog_score = float(z[valid].mean())
        if method == "tirosh":
            ctrl = _sample_background(valid, gene_to_bin_map, bin_pool, n_background, rng)

            if ctrl:
                ctrl_vals = z[ctrl].values
                assert np.all(np.isfinite(ctrl_vals)), "infinite z-scores identified in control genes"
                ctrl_score = float(ctrl_vals.mean())
            else:
                ctrl_score = 0.0
            out[subtype] = prog_score - ctrl_score
        else:
            out[subtype] = prog_score
    return out


def _gene_to_bin(z: "pd.Series", n_bins: int = 25) -> "pd.Series":
    """Map each finite-z gene to an expression-level bin index (0-based).

    Uses quantile bins (equal-population per bin) so no bin is empty,
    which avoids a common failure mode of equal-width binning on skewed data.
    """
    import pandas as pd

    finite = z[np.isfinite(z)]
    return pd.qcut(finite, q=n_bins, labels=False, duplicates="drop")


def _build_background_pool(z: "pd.Series", n_bins: int = 25) -> dict:
    """Return {bin_id: [gene_symbols]} for all expressed genes."""
    bin_ids = _gene_to_bin(z, n_bins)
    pool: dict = {}
    for gene, b in bin_ids.items():
        if not np.isnan(b):
            pool.setdefault(int(b), []).append(gene)
    return pool


def _sample_background(
    program_genes: list,
    gene_to_bin_map: dict,
    bin_pool: dict,
    n_per_gene: int,
    rng: "np.random.Generator",
) -> list:
    """For each program gene, draw n_per_gene controls from the same expression bin."""
    prog_set = set(program_genes)
    ctrl: list = []
    for g in program_genes:
        b = gene_to_bin_map.get(g)
        if b is None:
            continue
        candidates = [c for c in bin_pool.get(b, []) if c not in prog_set]
        if candidates:
            k = min(n_per_gene, len(candidates))
            ctrl.extend(rng.choice(candidates, size=k, replace=False).tolist())
    return list(set(ctrl))


def _score_ucell(
    adata: ad.AnnData,
    cell_indices,
    programs_in_data: dict,
    gene_mask: np.ndarray | None,
    min_genes: int,
) -> dict:
    """UCell: normalised Mann-Whitney U on per-cell z-score ranks.

    For a program of n genes ranked among N genes with finite z-score:
        U_norm = 1 − (sum_of_ranks − n*(n+1)/2) / (n * N)
    Score is in [0, 1]; 1.0 means all program genes rank at the top of the cell.

    Ranking is done on population z-scores (using the pre-computed mean_expr /
    std_expr in adata.var) rather than raw expression, so that constitutively
    highly-expressed housekeeping genes do not dominate the ranking — consistent
    with how mean_z and tirosh treat cell-specific signal.

    The rank universe is all genes with a finite z-score (gene_mask=None so N is
    stable across programs). The mask is used only to decide which program genes
    are eligible to contribute to a program's score.
    """
    from sc_annotation.selection import compute_scores

    # Z-score the cell against the full population — uses pre-computed mean_expr /
    # std_expr, consistent with mean_z and tirosh.  No mask here so N is the full
    # set of expressed genes and ranks are comparable across programs.
    z_unmasked = compute_scores(adata, cell_indices, "zscore", gene_mask=None, mask_zeros=False)
    # Rank descending: rank 1 = highest z-score (most cell-specific)
    ranks = z_unmasked.rank(ascending=False, method="average")
    N = int(np.isfinite(z_unmasked.values).sum())  # genes with a finite z-score

    # Build set of allowed gene symbols from gene_mask
    if gene_mask is not None:
        var_names = (
            adata.var["gene_symbol"].values
            if "gene_symbol" in adata.var.columns
            else np.asarray(adata.var_names)
        )
        allowed = set(var_names[gene_mask])
    else:
        allowed = None

    out: dict = {}
    for subtype, genes in programs_in_data.items():
        valid = [
            g for g in genes
            if g in ranks.index
            and (allowed is None or g in allowed)
        ]
        if len(valid) < min_genes or N == 0:
            out[subtype] = float("nan")
            continue
        n = len(valid)
        sum_ranks = float(ranks[valid].sum())
        u_norm = 1.0 - (sum_ranks - n * (n + 1) / 2) / (n * N)
        out[subtype] = float(u_norm)
    return out


# ─── Step 4: stage-2 prompt ──────────────────────────────────────────────────

def build_stage2_prompt(
    stage1_label: str,
    pathway_scores: dict,
    *,
    stage1_reasoning: str | None = None,
    genes_by_expr: list | None = None,
    genes_by_zscore: list | None = None,
    genes_by_tfidf: list | None = None,
    proteins: list | None = None,
    tissue: str = "PBMC",
    n_genes: int = 30,
    n_proteins: int = 15,
    cell_type_list: list | None = None,
) -> str:
    """Build a stage-2 cell type refinement prompt.

    Combines the full stage-1 output (label + reasoning), per-modality gene lists
    (expression, z-score, TF-IDF), optional surface protein markers, and the
    pathway score table. The LLM is instructed to confirm or override the stage-1
    call based on the complete evidence.

    Args:
        stage1_label: Stage-1 predicted cell type (may be verbose / approximate).
        pathway_scores: ``{subtype: score}`` from :func:`score_gene_programs`.
        stage1_reasoning: Full rationale text from the stage-1 LLM response.
            Shown as prior context so the LLM can see what evidence the first
            pass already interpreted.
        genes_by_expr: ``[(gene, expr), ...]`` sorted by raw expression descending.
        genes_by_zscore: ``[(gene, z_score), ...]`` sorted by z-score descending.
        genes_by_tfidf: ``[(gene, tfidf), ...]`` sorted by TF-IDF descending.
        proteins: Optional ``[(protein, z_score), ...]`` from ADT.
        tissue: Tissue context string.
        n_genes: Number of top genes to include per modality.
        n_proteins: Number of top proteins to include.

    Returns:
        User-facing prompt string.
    """
    parts: list[str] = []
    parts.append(f"Tissue context: {tissue}\n")

    parts.append(
        f'Stage-1 annotation: "{stage1_label}"'
        f" — may have minor inaccuracies. "
        f"Use the evidence below to confirm or correct it."
    )
    if stage1_reasoning:
        parts.append(f"\nStage-1 reasoning:\n{stage1_reasoning}")

    if genes_by_expr:
        parts.append(f"\nTop {n_genes} genes by raw expression:")
        for rank, (gene, val) in enumerate(genes_by_expr[:n_genes], 1):
            parts.append(f"  {rank:3d}. {gene:<10s}  ({_fmt_numeric(val)})")

    if genes_by_zscore:
        parts.append(
            f"\nTop {n_genes} cell-specific genes by z-score vs. population "
            f"(higher = more specific to this cell):"
        )
        for rank, (gene, z) in enumerate(genes_by_zscore[:n_genes], 1):
            parts.append(f"  {rank:3d}. {gene:<10s}  z={z:+.2f}")

    if genes_by_tfidf:
        parts.append(
            f"\nTop {n_genes} cell-specific genes by TF-IDF "
            f"(weights by rarity across cells — highlights rare but highly expressed genes):"
        )
        for rank, (gene, _) in enumerate(genes_by_tfidf[:n_genes], 1):
            parts.append(f"  {rank:3d}. {gene}")

    if proteins:
        parts.append("\nSurface proteins (z-score vs. population):")
        for rank, (prot, z) in enumerate(proteins[:n_proteins], 1):
            parts.append(f"  {rank:3d}. {prot:<15s}  z={z:+.2f}")

    valid = sorted(
        [(k, v) for k, v in pathway_scores.items() if np.isfinite(v)],
        key=lambda x: -x[1],
    )
    parts.append(
        "\nPathway scores (LLM-defined gene programs scored against this cell; "
        "higher = more active program):"
    )
    for subtype, score in valid:
        parts.append(f"  {subtype:<25s}: {score:+.3f}")

    if cell_type_list:
        parts.append(
            "\nChoose the cell type from the following list (output exactly one of these names in Line 1):\n"
            + ", ".join(cell_type_list)
        )
        parts.append(
            "\nConsidering all of the above — genes (across all scoring methods), "
            "surface proteins, pathway scores, and the stage-1 reasoning — "
            "confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. "
            "Trust direct gene/protein evidence over the stage-1 label when they conflict.\n"
            "Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words)."
        )
    else:
        parts.append(
            "\nConsidering all of the above — genes (across all scoring methods), "
            "surface proteins, pathway scores, and the stage-1 reasoning — "
            "confirm or correct the stage-1 annotation and give the most specific subtype. "
            "Trust direct gene/protein evidence over the stage-1 label when they conflict.\n"
            "Line 1: final cell type / subtype.  Line 2: brief rationale (<100 words)."
        )
    return "\n".join(parts)
