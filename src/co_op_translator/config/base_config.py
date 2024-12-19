import os
from dotenv import load_dotenv
import logging
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.config.vision_config.config import VisionConfig

load_dotenv()

logger = logging.getLogger(__name__)

class Config:
    """
    Central configuration class that combines all service-specific configurations.
    """
    
    @classmethod
    def check_configuration(cls):
        """
        Checks if all required environment variables are set across all services.
        Raises an OSError if any required environment variables are missing.
        """
        # Check LLM configurations
        LLMConfig.check_configuration()
        
        # Check Vision configurations
        VisionConfig.check_configuration()