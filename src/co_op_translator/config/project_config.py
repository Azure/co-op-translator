"""
Project configuration handler for Co-op Translator.
Manages custom directory structures and exclusion patterns.
"""

import yaml
import logging
import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

from co_op_translator.config.constants import EXCLUDED_DIRS

logger = logging.getLogger(__name__)

# Default configuration values
DEFAULT_CONFIG = {
    "translations_dir": "translations",
    "images_dir": "images",
    "exclude_dirs": EXCLUDED_DIRS.copy(),
    "exclude_patterns": [],
    "migration": {
        "auto_migrate": False,  # 자동 마이그레이션 비활성화
        "backup": True,  # 마이그레이션 전 백업 활성화
        "notify_only": False,  # 알림만 하지 않고 마이그레이션 수행
    },
    "history": {
        "last_config": {},  # 마지막으로 적용된 설정
        "migrated_at": None,  # 마지막 마이그레이션 시간
    },
}

CONFIG_FILENAMES = ["co-op-translator.yml"]


class ProjectConfig:
    """Manages project configuration for Co-op Translator."""

    def __init__(self, root_dir=None):
        """
        Initialize project configuration with optional root directory.

        Args:
            root_dir: Path to the project root directory. If None, uses current directory.
        """
        self.root_dir = Path(root_dir) if root_dir else Path.cwd()
        self._config = self._load_config()
        self._previous_config = self._get_previous_config()

    def _load_config(self) -> Dict[str, Any]:
        """
        Load configuration from YAML file or use defaults.
        Checks multiple possible filenames (with and without leading dot).

        Returns:
            Dict[str, Any]: Configuration dictionary.
        """
        config_path = None
        found = False

        for filename in CONFIG_FILENAMES:
            potential_path = self.root_dir / filename
            logger.debug(f"Searching for configuration file at: {potential_path}")

            if potential_path.exists():
                config_path = potential_path
                found = True
                break

        if not found:
            logger.debug(
                f"No configuration file found in {self.root_dir}, using defaults"
            )
            return DEFAULT_CONFIG.copy()

        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)

            if config is None:
                return DEFAULT_CONFIG.copy()

            # Merge with defaults to ensure all fields exist
            merged_config = DEFAULT_CONFIG.copy()
            if isinstance(config, dict):
                # Process configuration values, supporting both hierarchical and flat structures
                # First, handle direct keys (flat structure)
                for key, value in config.items():
                    if key in merged_config and key not in ["folders", "exclude"]:
                        merged_config[key] = value

                # Then, handle hierarchical structure (with higher precedence)
                if "folders" in config and isinstance(config["folders"], dict):
                    folders = config["folders"]
                    if "translations" in folders:
                        merged_config["translations_dir"] = folders["translations"]
                    if "images" in folders:
                        merged_config["images_dir"] = folders["images"]

                if "exclude" in config and isinstance(config["exclude"], dict):
                    exclude = config["exclude"]
                    if "dirs" in exclude and isinstance(exclude["dirs"], list):
                        merged_config["exclude_dirs"] = exclude["dirs"]
                    if "patterns" in exclude and isinstance(exclude["patterns"], list):
                        merged_config["exclude_patterns"] = exclude["patterns"]

                # Automatically exclude translations and images directories to prevent re-translation
                if (
                    merged_config["translations_dir"]
                    not in merged_config["exclude_dirs"]
                ):
                    merged_config["exclude_dirs"].append(
                        merged_config["translations_dir"]
                    )

                # Also exclude images directory if it's not already in the exclude list
                if merged_config["images_dir"] not in merged_config["exclude_dirs"]:
                    merged_config["exclude_dirs"].append(merged_config["images_dir"])

            logger.info(f"Loaded custom configuration from {config_path}")
            logger.debug(
                f"Configuration details: translations_dir={merged_config.get('translations_dir')}, "
                f"images_dir={merged_config.get('images_dir')}, "
                f"exclude_dirs={merged_config.get('exclude_dirs')}, "
                f"exclude_patterns={merged_config.get('exclude_patterns')}"
            )
            return merged_config

        except Exception as e:
            logger.error(f"Error loading configuration file '{config_path}': {e}")
            logger.info(f"Using default configuration instead: {DEFAULT_CONFIG}")
            return DEFAULT_CONFIG.copy()

    def _get_previous_config(self) -> Dict[str, Any]:
        """
        Get the previous configuration from history if available.
        Otherwise, return a copy of the default configuration.

        Returns:
            Dict[str, Any]: The previous configuration
        """
        if "history" in self._config and "last_config" in self._config["history"]:
            last_config = self._config["history"]["last_config"]
            if last_config and isinstance(last_config, dict):
                # Create a combined config with defaults and the saved last config
                previous = DEFAULT_CONFIG.copy()

                # Handle direct keys (except history and nested structures)
                for key, value in last_config.items():
                    if (
                        key not in ["history", "migration"]
                        and key in previous
                        and not isinstance(value, dict)
                    ):
                        previous[key] = value

                # Handle nested folder structure
                if "folders" in last_config and isinstance(
                    last_config["folders"], dict
                ):
                    folders = last_config["folders"]
                    if "translations" in folders:
                        previous["translations_dir"] = folders["translations"]
                    if "images" in folders:
                        previous["images_dir"] = folders["images"]

                # Handle nested exclude structure
                if "exclude" in last_config and isinstance(
                    last_config["exclude"], dict
                ):
                    exclude = last_config["exclude"]
                    if "dirs" in exclude and isinstance(exclude["dirs"], list):
                        previous["exclude_dirs"] = exclude["dirs"]
                    if "patterns" in exclude and isinstance(exclude["patterns"], list):
                        previous["exclude_patterns"] = exclude["patterns"]

                logger.info(f"Using previous configuration from history")
                return previous

        # If no valid history found, use default config
        logger.info(f"No previous configuration history found, using defaults")
        return DEFAULT_CONFIG.copy()

    def save_config(self):
        """
        Save the current configuration to the YAML file, including history.
        This should be called after any configuration changes that need to be persisted.
        """
        # Update history with current config before saving
        if "history" not in self._config:
            self._config["history"] = {}

        # Structure the config for saving as YAML
        # We want to keep the hierarchical structure for the YAML file
        save_config = {}

        # Create hierarchical structure
        save_config["folders"] = {
            "translations": self._config.get("translations_dir"),
            "images": self._config.get("images_dir"),
        }

        save_config["exclude"] = {
            "dirs": self._config.get("exclude_dirs"),
            "patterns": self._config.get("exclude_patterns"),
        }

        # Add migration settings
        if "migration" in self._config:
            save_config["migration"] = self._config["migration"]
        else:
            save_config["migration"] = DEFAULT_CONFIG["migration"]

        # Create a flat version of the current config for the history
        flat_current_config = {
            "translations_dir": self._config.get("translations_dir"),
            "images_dir": self._config.get("images_dir"),
            "exclude_dirs": self._config.get("exclude_dirs"),
            "exclude_patterns": self._config.get("exclude_patterns"),
        }

        # Update history
        save_config["history"] = {
            "last_config": flat_current_config,
            "migrated_at": datetime.datetime.now().isoformat(),
        }

        # Write to the config file
        config_path = self.root_dir / CONFIG_FILENAMES[0]
        with open(config_path, "w") as f:
            yaml.safe_dump(save_config, f, default_flow_style=False, sort_keys=False)

        logger.info(f"Configuration saved to {config_path} with updated history")

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
