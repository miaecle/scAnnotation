"""OpenRouter backend via the OpenAI-compatible OpenRouter API."""

from __future__ import annotations

from .openai import OpenAIBackend


class OpenRouterBackend(OpenAIBackend):
    """LLM backend powered by OpenRouter.

    Args:
        model: OpenRouter model ID, e.g. ``'deepseek/deepseek-v4-flash'``.
        api_key: OpenRouter API key. Reads ``OPENROUTER_API_KEY`` env var if None.
        max_tokens: Maximum tokens in the response.
        temperature: Sampling temperature (0 = deterministic).
    """

    def __init__(
        self,
        model: str = "openai/gpt-4o-mini",
        api_key: str | None = None,
        max_tokens: int = 1024,
        temperature: float = 0.0,
    ) -> None:
        super().__init__(
            model=model,
            api_key=api_key,
            max_tokens=max_tokens,
            temperature=temperature,
            base_url="https://openrouter.ai/api/v1",
            provider_name="openrouter",
        )