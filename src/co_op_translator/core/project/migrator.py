"""
Project migration utilities for Co-op Translator.

Handles migration of files between directories when configuration changes.
"""

import logging
import shutil
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Tuple, Optional, Union, Set

logger = logging.getLogger(__name__)


class ProjectMigrator:
    """
    Handles migration of files between directories when project configuration changes.

    This class is responsible for:
    - Detecting configuration changes that affect directory structure
    - Migrating files from old to new directories
    - Providing feedback on migration operations
    """

    def __init__(self, root_dir: Union[str, Path]):
        """
        Initialize the project migrator.

        Args:
            root_dir: Root directory of the project
        """
        self.root_dir = Path(root_dir) if not isinstance(root_dir, Path) else root_dir

    def detect_directory_changes(
        self, old_config: Dict[str, Any], new_config: Dict[str, Any]
    ) -> List[Tuple[str, Path, Path]]:
        """
        Detect changes in directory configurations.

        Args:
            old_config: Previous configuration dictionary
            new_config: Current configuration dictionary

        Returns:
            List of tuples containing (config_key, old_path, new_path) for changed directories
        """
        changes = []

        # Check for directory changes in the config
        directory_keys = ["translations_dir", "images_dir"]

        for key in directory_keys:
            old_value = old_config.get(key)
            new_value = new_config.get(key)

            if old_value != new_value:
                old_path = self.root_dir / old_value
                new_path = self.root_dir / new_value

                if old_path.exists() and old_path != new_path:
                    changes.append((key, old_path, new_path))
                    logger.warning(
                        f"{key.replace('_dir', '').capitalize()} directory changed from '{old_value}' to '{new_value}'"
                    )
                    logger.warning(
                        "Use --migrate flag if you want to migrate files from old to new directories"
                    )
                    logger.warning(
                        f"Previous {key.replace('_dir', '')} directory: {old_path}"
                    )
                    logger.warning(
                        f"New {key.replace('_dir', '')} directory: {new_path}"
                    )

        return changes

    def should_auto_migrate(self, config: Dict[str, Any]) -> bool:
        """
        Check if auto migration is enabled in the configuration.

        Args:
            config: Current configuration dictionary

        Returns:
            bool: True if auto migration is enabled, False otherwise
        """
        try:
            if "migration" in config and isinstance(config["migration"], dict):
                return config["migration"].get("auto_migrate", False)
            return False
        except Exception as e:
            logger.error(f"Error checking auto migration setting: {e}")
            return False

    def should_backup(self, config: Dict[str, Any]) -> bool:
        """
        Check if backup is enabled for migration in the configuration.

        Args:
            config: Current configuration dictionary

        Returns:
            bool: True if backup is enabled, False otherwise
        """
        try:
            if "migration" in config and isinstance(config["migration"], dict):
                return config["migration"].get(
                    "backup", True
                )  # Default to True for safety
            return True  # Default to True if not specified
        except Exception as e:
            logger.error(f"Error checking backup setting: {e}")
            return True  # Default to True for safety

    def is_notify_only(self, config: Dict[str, Any]) -> bool:
        """
        Check if migration should only notify and not perform actual migration.

        Args:
            config: Current configuration dictionary

        Returns:
            bool: True if only notification is enabled, False otherwise
        """
        try:
            if "migration" in config and isinstance(config["migration"], dict):
                return config["migration"].get("notify_only", False)
            return False
        except Exception as e:
            logger.error(f"Error checking notify_only setting: {e}")
            return False

    def migrate_directories(
        self, old_config: Dict[str, Any], new_config: Dict[str, Any]
    ) -> bool:
        """
        Migrate files from old directories to new directories based on configuration changes.

        Args:
            old_config: Previous configuration dictionary
            new_config: Current configuration dictionary

        Returns:
            bool: True if migration was successful, False otherwise
        """
        directory_changes = self.detect_directory_changes(old_config, new_config)

        if not directory_changes:
            logger.info("No directory changes detected that require migration")
            return False

        # Check migration settings
        if self.is_notify_only(new_config):
            logger.info(
                "Migration is set to notify-only mode. Not performing actual migration."
            )
            return False

        migration_performed = False
        should_backup = self.should_backup(new_config)

        # Migrate all changed directories
        for key, old_path, new_path in directory_changes:
            if should_backup:
                # Create backup before migration
                backup_path = self._create_backup(old_path)
                if backup_path:
                    logger.info(f"Created backup of {old_path} at {backup_path}")

            success = self._migrate_directory(old_path, new_path)
            migration_performed = success or migration_performed

        # Update last migrated timestamp
        if migration_performed:
            # This is informational only - the actual history update is done by ProjectConfig.save_config()
            logger.info(f"Migration completed at {datetime.now().isoformat()}")

        return migration_performed

    def _create_backup(self, source_path: Path) -> Optional[Path]:
        """
        Create a backup of a directory before migration.

        Args:
            source_path: Directory path to backup

        Returns:
            Optional[Path]: Path to the backup directory if successful, None otherwise
        """
        if not source_path.exists():
            logger.warning(f"Cannot backup non-existent directory: {source_path}")
            return None

        try:
            # Create backup directory name with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{source_path.name}_backup_{timestamp}"
            backup_path = source_path.parent / backup_name

            # Create backup using shutil.copytree
            shutil.copytree(source_path, backup_path)

            logger.info(f"Created backup of {source_path} at {backup_path}")
            return backup_path
        except Exception as e:
            logger.error(f"Error creating backup: {e}")
            return None

    def _migrate_directory(self, source_path: Path, target_path: Path) -> bool:
        """
        Migrate files from source directory to target directory.

        Args:
            source_path: Source directory path
            target_path: Target directory path

        Returns:
            bool: True if migration was successful, False otherwise
        """
        if not source_path.exists():
            logger.warning(f"Source directory does not exist: {source_path}")
            return False

        # Create target directory if it doesn't exist
        target_path.mkdir(parents=True, exist_ok=True)

        try:
            # Collect all files to migrate
            files_migrated = 0
            errors = 0

            # Walk through all files in the source directory
            for item in source_path.glob("**/*"):
                # Get the relative path from source directory
                relative_path = item.relative_to(source_path)
                # Construct target path
                target_item = target_path / relative_path

                if item.is_file():
                    try:
                        # Create parent directories if they don't exist
                        target_item.parent.mkdir(parents=True, exist_ok=True)
                        # Copy the file
                        shutil.copy2(item, target_item)
                        files_migrated += 1
                        logger.info(f"Migrated file: {item} -> {target_item}")
                    except Exception as e:
                        logger.error(f"Error migrating file {item}: {e}")
                        errors += 1

            logger.info(
                f"Migration completed: {files_migrated} files migrated, {errors} errors from {source_path} to {target_path}"
            )
            return files_migrated > 0

        except Exception as e:
            logger.error(f"Error during migration: {e}")
            return False
