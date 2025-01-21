"""
Provider-related configurations and enums.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, Optional


class LLMProvider(Enum):
    """LLM service providers with their configurations."""

    AZURE_OPENAI = "azure_openai"
    OPENAI = "openai"

    @property
    def display_name(self) -> str:
        """Get a human-readable display name."""
        return self.value.replace("_", " ").title()

    @property
    def env_prefix(self) -> str:
        """Get the environment variable prefix for this provider."""
        return self.value.upper() + "_"


@dataclass
class LLMServiceConfig:
    """Configuration for a specific LLM service."""

    required: bool
    priority: int
    env_vars: Dict[str, Optional[str]]
