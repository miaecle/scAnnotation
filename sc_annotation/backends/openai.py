"""OpenAI-compatible backend (requires `openai` package: pip install openai)."""

from __future__ import annotations
from .base import LLMBackend


def _to_int(value) -> int | None:
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


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
        base_url: str | None = None,
        provider_name: str = "openai",
    ) -> None:
        import openai

        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self._provider_name = provider_name
        if base_url is not None:
            self._client = openai.OpenAI(api_key=api_key, base_url=base_url)
        else:
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
        usage = getattr(response, "usage", None)
        prompt_details = getattr(usage, "prompt_tokens_details", None)
        completion_details = getattr(usage, "completion_tokens_details", None)
        self._record_usage(
            {
                "provider": self._provider_name,
                "input_tokens": _to_int(getattr(usage, "prompt_tokens", None)),
                "output_tokens": _to_int(getattr(usage, "completion_tokens", None)),
                "total_tokens": _to_int(getattr(usage, "total_tokens", None)),
                "cached_input_tokens": _to_int(getattr(prompt_details, "cached_tokens", None)),
                "reasoning_tokens": _to_int(getattr(completion_details, "reasoning_tokens", None)),
                "audio_input_tokens": _to_int(getattr(prompt_details, "audio_tokens", None)),
                "audio_output_tokens": _to_int(getattr(completion_details, "audio_tokens", None)),
            }
        )
        return response.choices[0].message.content.strip()
