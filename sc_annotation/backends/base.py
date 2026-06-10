"""Abstract base class for LLM backends."""

from __future__ import annotations
from abc import ABC, abstractmethod


class LLMBackend(ABC):
    """Base class for LLM completion backends.

    Subclasses implement `complete`, accepting an optional system prompt
    and a user message, and returning the model's text response.
    """

    @abstractmethod
    def complete(self, user_message: str, system_message: str | None = None) -> str:
        """Send a prompt to the LLM and return the text response.

        Args:
            user_message: The user-facing prompt content.
            system_message: Optional system-level instruction.

        Returns:
            The model's text response as a plain string.
        """

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(model={getattr(self, 'model', '?')})"
