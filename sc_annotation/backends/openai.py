"""OpenAI backend (requires `openai` package: pip install openai)."""

from __future__ import annotations
from .base import LLMBackend


class OpenAIBackend(LLMBackend):
    """LLM backend powered by OpenAI.

    Args:
        model: OpenAI model ID, e.g. 'gpt-4o' or 'gpt-4o-mini'.
        api_key: OpenAI API key. Reads OPENAI_API_KEY env var if None.
        max_tokens: Maximum tokens in the response.
        temperature: Sampling temperature (0 = deterministic).
    """

    def __init__(
        self,
        model: str = "gpt-4o",
        api_key: str | None = None,
        max_tokens: int = 1024,
        temperature: float = 0.0,
    ) -> None:
        import openai

        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self._client = openai.OpenAI(api_key=api_key)

    def complete(self, user_message: str, system_message: str | None = None) -> str:
        messages = []
        if system_message is not None:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": user_message})

        response = self._client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        return response.choices[0].message.content.strip()
