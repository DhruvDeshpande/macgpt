import os
from dataclasses import dataclass


@dataclass
class RouteDecision:
    provider: str
    model: str
    reason: str = ""


class ModelRouter:
    """
    OpenRouter-style routing logic.

    - Chooses between "fast" and "smart" models
    - Uses simple heuristics on the user request
    - Models are configurable via environment variables
    """

    def __init__(self):
        self.provider = os.getenv("MACGPT_PROVIDER", "ollama").strip().lower()

        # Default model (what you currently have)
        self.default_model = os.getenv("MACGPT_MODEL", "llama3:latest").strip()

        # Tiered models (same for now, different later)
        self.fast_model = os.getenv("MACGPT_FAST_MODEL", self.default_model).strip()
        self.smart_model = os.getenv("MACGPT_SMART_MODEL", self.default_model).strip()

    def decide(self, user_request: str) -> RouteDecision:
        text = (user_request or "").strip()
        lower = text.lower()

        # Heuristics
        is_long = len(text) > 120
        has_multiple_steps = any(
            kw in lower for kw in [" and ", " then ", " after that ", " also "]
        )
        comparative = any(
            kw in lower for kw in ["most recent", "largest", "smallest", "older than", "newer than"]
        )
        simple_file_ops = any(
            kw in lower for kw in ["pdf", "downloads", "desktop", "file", "folder", "open", "list", "find"]
        )

        # Decision logic
        if is_long or has_multiple_steps or comparative:
            return RouteDecision(
                provider=self.provider,
                model=self.smart_model,
                reason="smart: complex or multi-step request"
            )

        if simple_file_ops:
            return RouteDecision(
                provider=self.provider,
                model=self.fast_model,
                reason="fast: simple file operation"
            )

        return RouteDecision(
            provider=self.provider,
            model=self.smart_model,
            reason="smart: default fallback"
        )

