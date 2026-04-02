import json
import requests
from typing import Any, Optional

from providers.base import LLMProvider


class OllamaProvider(LLMProvider):
    """
    Adapter for Ollama's local HTTP API.
    """

    def __init__(self, host: str = "http://localhost:11434", model: str = "llama3"):
        self.host = host.rstrip("/")
        self.model = model

    @property
    def name(self) -> str:
        return "ollama"

    def generate(self, system_prompt: str, user_prompt: str, **kwargs: Any) -> str:
        """
        Calls POST /api/generate on the local Ollama server.
        Returns the response text.
        """
        url = f"{self.host}/api/generate"

        prompt = f"{system_prompt}\n\n{user_prompt}".strip()

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }

        # Allow optional tuning (safe defaults)
        if "temperature" in kwargs:
            payload["options"] = payload.get("options", {})
            payload["options"]["temperature"] = kwargs["temperature"]

        resp = requests.post(url, json=payload, timeout=120)
        resp.raise_for_status()

        data = resp.json()
        return (data.get("response") or "").strip()

