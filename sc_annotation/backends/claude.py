"""Anthropic Claude backend."""

from __future__ import annotations
from .base import LLMBackend


class ClaudeBackend(LLMBackend):
    """LLM backend powered by Anthropic Claude.

    Args:
        model: Claude model ID, e.g. 'claude-sonnet-4-6' or 'claude-opus-4-7'.
        api_key: Anthropic API key. Reads ANTHROPIC_API_KEY env var if None.
        max_tokens: Maximum tokens in the response.
        temperature: Sampling temperature (0 = deterministic).
    """

    def __init__(
        self,
        model: str = "claude-sonnet-4-6",
        api_key: str | None = None,
        max_tokens: int = 1024,
        temperature: float = 0.0,
    ) -> None:
        import anthropic

        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self._client = anthropic.Anthropic(api_key=api_key)

    def complete(self, user_message: str, system_message: str | None = None) -> str:
        kwargs: dict = dict(
            model=self.model,
            max_tokens=self.max_tokens,
            messages=[{"role": "user", "content": user_message}],
        )
        if system_message is not None:
            kwargs["system"] = system_message
        if self.temperature is not None:
            kwargs["temperature"] = self.temperature

        response = self._client.messages.create(**kwargs)
        return response.content[0].text.strip()
