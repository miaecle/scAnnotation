"""Abstract base class for LLM backends."""

from __future__ import annotations

import time
from abc import ABC, abstractmethod
from typing import Any, Callable


class LLMBackend(ABC):
    """Base class for LLM completion backends.

    Subclasses implement ``complete`` and should call ``_record_usage`` with
    provider-specific token/accounting fields after each successful request.
    """

    @abstractmethod
    def complete(self, user_message: str, system_message: str | None = None) -> str:
        """Send a prompt to the LLM and return the text response."""

    def _record_usage(self, usage: dict[str, Any] | None) -> None:
        payload = dict(usage or {})
        payload.setdefault("backend", self.__class__.__name__)
        payload.setdefault("model", getattr(self, "model", None))
        payload["recorded_at_unix"] = time.time()

        if not hasattr(self, "_usage_history"):
            self._usage_history: list[dict[str, Any]] = []
        self._usage_history.append(payload)
        self._last_usage = payload

    def get_last_usage(self) -> dict[str, Any] | None:
        if not hasattr(self, "_last_usage"):
            return None
        return dict(self._last_usage)

    def get_usage_history(self) -> list[dict[str, Any]]:
        if not hasattr(self, "_usage_history"):
            return []
        return [dict(item) for item in self._usage_history]

    def clear_usage_history(self) -> None:
        self._usage_history = []
        self._last_usage = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(model={getattr(self, 'model', '?')})"


def complete_with_retry(
    backend: LLMBackend,
    user_message: str,
    system_message: str | None = None,
    max_retries: int = 3,
    base_sleep: float = 5.0,
    max_sleep: float = 60.0,
    usage_sink: Callable[[dict[str, Any]], None] | None = None,
    usage_context: dict[str, Any] | None = None,
    complete_kwargs: dict[str, Any] | None = None,
    response_validator: Callable[[str], None] | None = None,
) -> str:
    """Call an LLM backend with exponential-backoff retries.

    Retries transient API/network failures from ``backend.complete``. If all
    attempts fail, raises ``RuntimeError`` so the current experiment stops.
    """
    last_error: Exception | None = None
    total_attempts = max_retries + 1
    last_response: str | None = None

    for attempt in range(total_attempts):
        try:
            if complete_kwargs:
                response = backend.complete(
                    user_message,
                    system_message=system_message,
                    **complete_kwargs,
                )
            else:
                response = backend.complete(user_message, system_message=system_message)
            last_response = response
            if response_validator is not None:
                response_validator(response)
            if usage_sink is not None:
                usage_getter = getattr(backend, "get_last_usage", None)
                if callable(usage_getter):
                    usage = usage_getter()
                    if usage:
                        payload = dict(usage)
                        if usage_context:
                            payload.update(usage_context)
                        usage_sink(payload)
            return response
        except Exception as exc:
            last_error = exc
            if attempt == max_retries:
                break

            sleep_s = min(base_sleep * (2 ** attempt), max_sleep)
            print(
                f"LLM request failed ({type(exc).__name__}: {exc}). "
                f"Retrying {attempt + 1}/{max_retries} after {sleep_s:.1f}s..."
            )
            time.sleep(sleep_s)

    print("========User message========")
    print(user_message)
    if last_response is not None:
        print("========Last response========")
        print(last_response)
    raise RuntimeError(
        f"LLM request failed after {total_attempts} attempts."
    ) from last_error
