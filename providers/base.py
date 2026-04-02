from abc import ABC, abstractmethod
from typing import Any


class LLMProvider(ABC):
    """
    Port (abstraction) for any LLM backend: Ollama, OpenAI, OpenRouter, etc.
    macgpt should call this interface, not a specific API directly.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def generate(self, system_prompt: str, user_prompt: str, **kwargs: Any) -> str:
        """
        Returns raw model text output.
        """
        raise NotImplementedError

