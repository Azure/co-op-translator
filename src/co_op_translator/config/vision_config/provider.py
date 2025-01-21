"""
Defines providers for Vision-related services.
"""

from enum import Enum


class VisionProvider(Enum):
    """
    Available Vision service providers.

    Providers are listed in order of priority.
    """

    AZURE_COMPUTER_VISION = "azure_computer_vision"  # Highest priority
    # Future vision services can be added here

    @property
    def display_name(self) -> str:
        """Get a human-readable display name."""
        return self.value.replace("_", " ").title()

    @property
    def env_prefix(self) -> str:
        """Get the environment variable prefix for this provider."""
        return self.value.upper() + "_"
