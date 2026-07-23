"""DeepSeek backend via the OpenAI-compatible DeepSeek API."""

from __future__ import annotations

from .openai import OpenAIBackend


class DeepSeekBackend(OpenAIBackend):
    """LLM backend powered by DeepSeek.

    Args:
        model: DeepSeek model ID, e.g. ``'deepseek-v4-flash'`` if available on
            your account or another DeepSeek-compatible model name.
        api_key: DeepSeek API key. Reads ``DEEPSEEK_API_KEY`` env var if None.
        max_tokens: Maximum tokens in the response.
        temperature: Sampling temperature (0 = deterministic).
    """

    def __init__(
        self,
        model: str = "deepseek-chat",
        api_key: str | None = None,
        max_tokens: int = 1024,
        temperature: float = 0.0,
    ) -> None:
        super().__init__(
            model=model,
            api_key=api_key,
            max_tokens=max_tokens,
            temperature=temperature,
            base_url="https://api.deepseek.com",
            provider_name="deepseek",
        )
