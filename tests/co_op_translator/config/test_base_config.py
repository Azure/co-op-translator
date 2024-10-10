import pytest
import os
from unittest.mock import patch
from co_op_translator.config.base_config import Config

@pytest.fixture
def mock_env_vars():
    """
    Provides a set of common environment variables for the project.
    This function returns mock environment variables that simulate
    the real ones used in the application.
    """
    env_vars = {
        'AZURE_SUBSCRIPTION_KEY': 'fake_subscription_key',
        'AZURE_OPENAI_API_KEY': 'fake_openai_key',
        'AZURE_OPENAI_ENDPOINT': 'https://fake-openai-endpoint.com',
        'AZURE_OPENAI_MODEL_NAME': 'gpt-3.5',
        'AZURE_OPENAI_CHAT_DEPLOYMENT_NAME': 'chat-deployment',
        'AZURE_OPENAI_API_VERSION': 'v1',
        'AZURE_AI_SERVICE_ENDPOINT': 'https://fake-ai-service-endpoint.com'
    }
    return env_vars

def test_config_with_all_env_vars(mock_env_vars):
    """
    Test that verifies if the configuration check passes when
    all required environment variables are properly set.
    """
    with patch.dict(os.environ, mock_env_vars, clear=True):
        Config.check_configuration()

# Parametrized test for missing environment variables
@pytest.mark.parametrize("missing_var, expected_message", [
    ('AZURE_OPENAI_API_KEY', 'AZURE_OPENAI_API_KEY'),
    ('AZURE_SUBSCRIPTION_KEY', 'AZURE_SUBSCRIPTION_KEY'),
    ('AZURE_OPENAI_ENDPOINT', 'AZURE_OPENAI_ENDPOINT')
])

def test_config_missing_single_env_var(mock_env_vars, missing_var, expected_message):
    """
    Test that simulates a missing environment variable scenario.
    This test checks that an appropriate error message is raised
    when one of the required environment variables is missing.
    """
    mock_env_vars.pop(missing_var)
    
    with patch.dict(os.environ, mock_env_vars, clear=True):
        with pytest.raises(EnvironmentError) as excinfo:
            Config.check_configuration()
        
        assert expected_message in str(excinfo.value)

def test_config_missing_multiple_env_vars():
    """
    Test that verifies behavior when all environment variables are missing.
    This ensures that the configuration check raises an error listing all
    the missing variables when none are provided.
    """
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(EnvironmentError) as excinfo:
            Config.check_configuration()

        missing_keys = [
            "AZURE_SUBSCRIPTION_KEY",
            "AZURE_OPENAI_API_KEY",
            "AZURE_OPENAI_ENDPOINT",
            "AZURE_OPENAI_MODEL_NAME",
            "AZURE_OPENAI_CHAT_DEPLOYMENT_NAME",
            "AZURE_OPENAI_API_VERSION",
            "AZURE_AI_SERVICE_ENDPOINT"
        ]
        
        for key in missing_keys:
            assert key in str(excinfo.value)
