import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.config.vision_config.config import VisionConfig

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
