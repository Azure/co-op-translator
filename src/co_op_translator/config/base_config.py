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
    def load_environment(cls, root_dir='.'):
        """
        Load environment variables from the target project's root directory.
        
        Args:
            root_dir: Root directory of the target project (default is current directory).
        """
        env_path = Path(root_dir) / '.env'
        if env_path.exists():
            load_dotenv(dotenv_path=env_path)
        else:
            logger.debug(f"No .env file found in {env_path}")
    
    @classmethod
    def check_configuration(cls, root_dir='.'):
        """
        Load environment variables and check if all required variables are set across all services.
        Raises an OSError if any required environment variables are missing.
        
        Args:
            root_dir: Root directory of the target project (default is current directory).
        """
        # Load environment variables first
        cls.load_environment(root_dir)
        
        # Check LLM configurations
        LLMConfig.check_configuration()
        
        # Check Vision configurations
        VisionConfig.check_configuration()
        VisionConfig.check_configuration()