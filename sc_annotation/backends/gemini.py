"""Google Gemini backend."""

from __future__ import annotations
from .base import LLMBackend


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
    ) -> None:
        from google import genai
        from google.genai import types

        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self._types = types
        self._client = genai.Client(api_key=api_key)

    def complete(self, user_message: str, system_message: str | None = None) -> str:
        config = self._types.GenerateContentConfig(
            max_output_tokens=self.max_tokens,
            temperature=self.temperature,
            system_instruction=system_message,
        )
        response = self._client.models.generate_content(
            model=self.model,
            contents=user_message,
            config=config,
        )
        return response.text.strip()
