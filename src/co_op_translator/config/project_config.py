"""
Project configuration handler for Co-op Translator.
Manages custom directory structures and exclusion patterns.
"""

import os
import yaml
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional

from co_op_translator.config.constants import EXCLUDED_DIRS

logger = logging.getLogger(__name__)

DEFAULT_CONFIG = {
    "translations_dir": "translations",
    "images_dir": "translated_images",
    "exclude_dirs": list(EXCLUDED_DIRS),
    "exclude_patterns": ["*.tmp", "*.swp", "*.bak", "*~"],
}

CONFIG_FILENAME = ".co-op-translator.yml"


class ProjectConfig:
    """Manages project configuration for Co-op Translator."""

    def __init__(self, root_dir: str = None):
        """
        Initialize project configuration.

        Args:
            root_dir (str, optional): Root directory of the project. If None,
                                     uses current working directory.
        """
        self.root_dir = Path(root_dir or os.getcwd()).resolve()
        self._config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """
        Load configuration from YAML file or use defaults.

        Returns:
            Dict[str, Any]: Configuration dictionary.
        """
        config_path = self.root_dir / CONFIG_FILENAME

        if not config_path.exists():
            logger.debug(
                f"No configuration file found at {config_path}, using defaults"
            )
            return DEFAULT_CONFIG.copy()

        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)

            # If loaded config is None (empty file), use default config
            if config is None:
                return DEFAULT_CONFIG.copy()

            # Merge with defaults to ensure all fields exist
            merged_config = DEFAULT_CONFIG.copy()
            if isinstance(config, dict):
                # Update with user values
                for key, value in config.items():
                    if key in merged_config:
                        merged_config[key] = value

            logger.info(f"Loaded custom configuration from {config_path}")
            return merged_config

        except Exception as e:
            logger.error(f"Error loading configuration file: {e}")
            return DEFAULT_CONFIG.copy()

    @property
    def translations_dir(self) -> Path:
        """Get the translations directory path relative to root."""
        return Path(
            self._config.get("translations_dir", DEFAULT_CONFIG["translations_dir"])
        )

    @property
    def images_dir(self) -> Path:
        """Get the translated images directory path relative to root."""
        return Path(self._config.get("images_dir", DEFAULT_CONFIG["images_dir"]))

    @property
    def exclude_dirs(self) -> List[str]:
        """Get directories to exclude from translation."""
        return self._config.get("exclude_dirs", DEFAULT_CONFIG["exclude_dirs"])

    @property
    def exclude_patterns(self) -> List[str]:
        """Get file patterns to exclude from translation."""
        return self._config.get("exclude_patterns", DEFAULT_CONFIG["exclude_patterns"])

    def get_absolute_translations_dir(self) -> Path:
        """Get absolute path to translations directory."""
        return self.root_dir / self.translations_dir

    def get_absolute_images_dir(self) -> Path:
        """Get absolute path to translated images directory."""
        return self.root_dir / self.images_dir

    def save_config(self) -> bool:
        """
        Save current configuration to file.

        Returns:
            bool: True if successful, False otherwise.
        """
        config_path = self.root_dir / CONFIG_FILENAME
        try:
            with open(config_path, "w", encoding="utf-8") as f:
                yaml.dump(self._config, f, default_flow_style=False, sort_keys=False)
            logger.info(f"Configuration saved to {config_path}")
            return True
        except Exception as e:
            logger.error(f"Error saving configuration file: {e}")
            return False

    def update_config(self, new_config: Dict[str, Any]) -> bool:
        """
        Update configuration with new values.

        Args:
            new_config (Dict[str, Any]): New configuration values.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            for key, value in new_config.items():
                if key in self._config:
                    self._config[key] = value
            return self.save_config()
        except Exception as e:
            logger.error(f"Error updating configuration: {e}")
            return False
