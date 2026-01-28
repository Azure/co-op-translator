import os
import logging
from pathlib import Path
from dotenv import load_dotenv
import importlib.resources
import yaml
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.config.vision_config.config import VisionConfig
from co_op_translator.utils.common.lang_utils import normalize_language_code

logger = logging.getLogger(__name__)


class Config:
    """
    Central configuration class that combines all service-specific configurations.
    """

    @classmethod
    def load_environment(cls, root_dir="."):
        """
        Load environment variables from the target project's root directory.

        Args:
            root_dir: Root directory of the target project (default is current directory).
        """
        env_path = Path(root_dir) / ".env"
        if env_path.exists():
            load_dotenv(dotenv_path=env_path)
        else:
            logger.debug(f"No .env file found in {env_path}")

    @staticmethod
    def check_configuration():
        """
        Check if all required services are properly configured.

        Raises:
            ValueError: If no LLM service is properly configured
        """

        LLMConfig.check_configuration()

        # Vision configuration is optional
        VisionConfig.check_configuration()

    @staticmethod
    def get_language_codes() -> list[str]:
        """
        Return the full list of supported language codes from the packaged font mappings,
        normalized to canonical BCP 47 (e.g., zh-TW, zh-CN, pt-BR, pt-PT).

        Falls back to an empty list on error.
        """
        try:
            with importlib.resources.path(
                "co_op_translator.fonts", "font_language_mappings.yml"
            ) as mappings_path:
                with open(mappings_path, "r", encoding="utf-8") as file:
                    font_mappings = yaml.safe_load(file) or {}
                    # Only include entries with a dict mapping and normalize
                    seen: set[str] = set()
                    ordered: list[str] = []
                    for key, meta in font_mappings.items():
                        if not isinstance(meta, dict):
                            continue
                        key_str = str(key)
                        canon = normalize_language_code(key_str)
                        # Optional developer warning when a non-canonical key is present
                        try:
                            if os.getenv("COOP_STRICT_CANON_KEYS") == "1" and (
                                not canon or canon != key_str
                            ):
                                logger.warning(
                                    "Non-canonical or invalid language code '%s' in font_language_mappings.yml (normalized to '%s')",
                                    key_str,
                                    canon,
                                )
                        except Exception:
                            # Do not fail on logging issues
                            pass
                        if canon and canon not in seen:
                            seen.add(canon)
                            ordered.append(canon)
                    return ordered
        except Exception as e:
            logger.warning(f"Failed to load language codes from font mappings: {e}")
            return []
