"""Google Gemini backend."""

from __future__ import annotations
from .base import LLMBackend


def _to_int(value) -> int | None:
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


class GeminiBackend(LLMBackend):
    """LLM backend powered by Google Gemini (via google-genai SDK).

    Args:
        model: Gemini model ID, e.g. 'gemini-2.0-flash' or 'gemini-1.5-pro'.
        api_key: Google AI API key. Reads GOOGLE_API_KEY env var if None.
        max_tokens: Maximum output tokens.
        temperature: Sampling temperature (0 = deterministic).
    """

    def __init__(
        self,
        model: str = "gemini-2.5-flash",
        api_key: str | None = None,
        max_tokens: int = 4096,
        temperature: float = 0.0,
        use_context_cache: bool = False,
        context_cache_ttl_seconds: int = 3600,
    ) -> None:
        from google import genai
        from google.genai import types

        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.use_context_cache = use_context_cache
        self.context_cache_ttl_seconds = context_cache_ttl_seconds
        self._types = types
        self._client = genai.Client(api_key=api_key)
        self._context_cache_names: dict[str, str | None] = {}
        if self.context_cache_ttl_seconds <= 0:
            raise ValueError("context_cache_ttl_seconds must be > 0.")

    @staticmethod
    def _is_cache_too_small_error(exc: Exception) -> bool:
        msg = str(exc)
        return "Cached content is too small" in msg or "min_total_token_count" in msg

    @staticmethod
    def _make_cache_lookup_key(
        system_message: str | None,
        cached_user_prefix: str | None,
        cache_key: str | None,
    ) -> str:
        if cache_key:
            return cache_key
        return f"sys::{system_message or ''}\nuser::{cached_user_prefix or ''}"

    def _get_cached_content_name(
        self,
        system_message: str | None,
        cached_user_prefix: str | None = None,
        cache_key: str | None = None,
    ) -> str | None:
        if not self.use_context_cache:
            return None
        if not system_message and not cached_user_prefix:
            return None

        lookup_key = self._make_cache_lookup_key(system_message, cached_user_prefix, cache_key)
        if lookup_key in self._context_cache_names:
            return self._context_cache_names[lookup_key]

        try:
            cache_cfg: dict = {
                "ttl": f"{self.context_cache_ttl_seconds}s",
            }
            if system_message:
                cache_cfg["system_instruction"] = system_message
            if cached_user_prefix:
                cache_cfg["contents"] = cached_user_prefix
            cached_content = self._client.caches.create(
                model=self.model,
                config=self._types.CreateCachedContentConfig(**cache_cfg),
            )
            cache_name = getattr(cached_content, "name", None)
            if not cache_name:
                raise RuntimeError(f"Gemini cache creation returned no name. Raw response: {cached_content!r}")
        except Exception as exc:
            if self._is_cache_too_small_error(exc):
                self._context_cache_names[lookup_key] = None
                return None
            raise

        self._context_cache_names[lookup_key] = cache_name
        return cache_name

    def complete(
        self,
        user_message: str,
        system_message: str | None = None,
        cached_user_prefix: str | None = None,
        cache_key: str | None = None,
    ) -> str:
        cache_name = self._get_cached_content_name(
            system_message=system_message,
            cached_user_prefix=cached_user_prefix,
            cache_key=cache_key,
        )
        config_kwargs: dict = dict(
            max_output_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        if cache_name:
            config_kwargs["cached_content"] = cache_name
        elif system_message:
            config_kwargs["system_instruction"] = system_message

        contents = user_message
        if cached_user_prefix and not cache_name:
            contents = f"{cached_user_prefix}\n\n{user_message}" if user_message else cached_user_prefix

        config = self._types.GenerateContentConfig(**config_kwargs)
        response = self._client.models.generate_content(
            model=self.model,
            contents=contents,
            config=config,
        )
        usage = getattr(response, "usage_metadata", None)
        prompt_tokens = _to_int(getattr(usage, "prompt_token_count", None))
        candidates_tokens = _to_int(getattr(usage, "candidates_token_count", None))
        self._record_usage(
            {
                "provider": "gemini",
                "input_tokens": prompt_tokens,
                "output_tokens": candidates_tokens,
                "total_tokens": _to_int(getattr(usage, "total_token_count", None)),
                "cached_input_tokens": _to_int(getattr(usage, "cached_content_token_count", None)),
                "thoughts_tokens": _to_int(getattr(usage, "thoughts_token_count", None)),
                "cache_used": bool(cache_name),
            }
        )
        text = getattr(response, "text", None)
        if text is None:
            raise RuntimeError(f"Gemini returned no text. Raw response: {response!r}")
        return text.strip()
