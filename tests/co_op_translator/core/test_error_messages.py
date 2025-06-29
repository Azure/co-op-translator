"""
Tests for verifying user-facing error messages in core translator components.
"""

import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path

from co_op_translator.core.llm.markdown_translator import MarkdownTranslator
from co_op_translator.core.project.project_translator import ProjectTranslator
from co_op_translator.core.vision.image_translator import ImageTranslator


class TestMarkdownTranslatorErrorMessages:
    """Test improved error messages in MarkdownTranslator."""

    def test_no_llm_provider_error_message(self):
        """Test error message when no LLM provider is configured."""
        with patch(
            "co_op_translator.config.llm_config.config.LLMConfig.get_available_provider",
            return_value=None,
        ):
            with pytest.raises(ValueError) as exc_info:
                MarkdownTranslator.create()

            error_msg = str(exc_info.value)
            assert "No valid LLM provider configured" in error_msg
            assert ".env file" in error_msg
            assert "API_KEY" in error_msg

    def test_unsupported_provider_error_message(self):
        """Test error message for unsupported provider."""
        with patch(
            "co_op_translator.config.llm_config.config.LLMConfig.get_available_provider",
            return_value="UNSUPPORTED",
        ):
            with pytest.raises(ValueError) as exc_info:
                MarkdownTranslator.create()

            error_msg = str(exc_info.value)
            assert "Unsupported LLM provider 'UNSUPPORTED'" in error_msg
            assert "AZURE_OPENAI" in error_msg
            assert "OPENAI" in error_msg
            assert "check your configuration" in error_msg


class TestProjectTranslatorErrorMessages:
    """Test improved error messages in ProjectTranslator."""

    def test_computer_vision_config_error_message(self, tmp_path, caplog):
        """Test Computer Vision configuration error message."""
        # Set logging level to capture info messages
        caplog.set_level("INFO")

        with patch(
            "co_op_translator.core.vision.image_translator.ImageTranslator.create",
            side_effect=ValueError("CV error"),
        ):
            with patch(
                "co_op_translator.core.llm.text_translator.TextTranslator.create"
            ):
                with patch(
                    "co_op_translator.core.llm.markdown_translator.MarkdownTranslator.create"
                ):
                    translator = ProjectTranslator(
                        "ko", str(tmp_path), markdown_only=False
                    )

                    # Check that it auto-switched to markdown_only
                    assert translator.markdown_only is True

                    # Check improved log message
                    log_text = caplog.text
                    assert "Computer Vision not configured" in log_text
                    assert "AZURE_COMPUTER_VISION_KEY" in log_text

    def test_markdown_only_mode_message(self, tmp_path, caplog):
        """Test markdown-only mode initialization message."""
        # Set logging level to capture info messages
        caplog.set_level("INFO")

        with patch("co_op_translator.core.llm.text_translator.TextTranslator.create"):
            with patch(
                "co_op_translator.core.llm.markdown_translator.MarkdownTranslator.create"
            ):
                translator = ProjectTranslator("ko", str(tmp_path), markdown_only=True)

                # Check improved log message for markdown-only mode
                log_text = caplog.text
                assert "Running in markdown-only mode" in log_text
                assert "Image translation disabled" in log_text


class TestImageTranslatorErrorMessages:
    """Test improved error messages in ImageTranslator."""

    def test_computer_vision_config_error_message(self):
        """Test Computer Vision configuration error message."""
        with patch(
            "co_op_translator.config.vision_config.config.VisionConfig.get_available_provider",
            side_effect=ValueError("Config error"),
        ):
            with pytest.raises(ValueError) as exc_info:
                ImageTranslator.create()

            error_msg = str(exc_info.value)
            assert "Computer Vision not configured" in error_msg
            assert "AZURE_COMPUTER_VISION_KEY" in error_msg
            assert "AZURE_COMPUTER_VISION_ENDPOINT" in error_msg
            assert ".env file" in error_msg

    @pytest.fixture
    def mock_image_translator(self, tmp_path):
        """Create a mock ImageTranslator instance for testing."""

        class MockImageTranslator(ImageTranslator):
            def __init__(self, default_output_dir, root_dir):
                # Skip the parent __init__ to avoid LLM dependency
                self.default_output_dir = default_output_dir
                self.root_dir = Path(root_dir)
                self.text_translator = MagicMock()  # Mock text translator
                self.font_config = MagicMock()  # Mock font config
                Path(default_output_dir).mkdir(parents=True, exist_ok=True)

            def get_image_analysis_client(self):
                return MagicMock()

        return MockImageTranslator(str(tmp_path), str(tmp_path))

    def test_no_text_detected_error_message(self, mock_image_translator, tmp_path):
        """Test error message when no text is detected in image."""
        # Create a temporary test image file
        test_image = tmp_path / "test.png"
        test_image.touch()

        # Mock the analysis client to return no text
        mock_client = MagicMock()
        mock_result = MagicMock()
        mock_result.read = None
        mock_client.analyze.return_value = mock_result

        with patch.object(
            mock_image_translator, "get_image_analysis_client", return_value=mock_client
        ):
            with pytest.raises(Exception) as exc_info:
                mock_image_translator.extract_line_bounding_boxes(str(test_image))

            error_msg = str(exc_info.value)
            assert f"No text detected in image '{test_image.name}'" in error_msg
            assert "clear, high-contrast text" in error_msg
            assert "text quality is too poor" in error_msg

    def test_image_translation_failure_message(
        self, mock_image_translator, caplog, tmp_path
    ):
        """Test error message for image translation failure."""
        # Create a temporary test image file within the tmp_path
        test_image = tmp_path / "test.png"
        test_image.touch()

        # Set the root_dir to tmp_path to avoid path issues
        mock_image_translator.root_dir = tmp_path

        # Mock PIL Image.open to avoid needing a real image file
        with patch("PIL.Image.open") as mock_image_open:
            mock_image_open.return_value = MagicMock()

            # Mock extract_line_bounding_boxes to raise an exception
            with patch.object(
                mock_image_translator,
                "extract_line_bounding_boxes",
                side_effect=Exception("Test error"),
            ):
                result = mock_image_translator.translate_image(str(test_image), "ko")

                # Should return a path containing the original filename base
                assert "test." in str(result)  # Check for original filename base
                assert ".ko.png" in str(result)  # Check for language code and extension

                # Check improved error message in logs
                log_text = caplog.text
                assert f"Failed to translate image '{test_image.name}'" in log_text
                assert "Test error" in log_text
                assert "Computer Vision API configuration" in log_text


class TestIntegratedErrorMessages:
    """Test error messages in realistic scenarios."""

    def test_missing_api_keys_scenario(self, tmp_path):
        """Test scenario where all API keys are missing."""
        with patch(
            "co_op_translator.config.llm_config.config.LLMConfig.get_available_provider",
            return_value=None,
        ):
            with patch(
                "co_op_translator.config.vision_config.config.VisionConfig.get_available_provider",
                side_effect=ValueError("No CV"),
            ):

                # Test MarkdownTranslator
                with pytest.raises(ValueError) as exc_info:
                    MarkdownTranslator.create()
                assert ".env file" in str(exc_info.value)

                # Test ImageTranslator
                with pytest.raises(ValueError) as exc_info:
                    ImageTranslator.create()
                assert "AZURE_COMPUTER_VISION_KEY" in str(exc_info.value)

    def test_project_initialization_with_missing_services(self, tmp_path, caplog):
        """Test ProjectTranslator initialization when services are missing."""
        # Set logging level to capture info messages
        caplog.set_level("INFO")

        with patch("co_op_translator.core.llm.text_translator.TextTranslator.create"):
            with patch(
                "co_op_translator.core.llm.markdown_translator.MarkdownTranslator.create"
            ):
                with patch(
                    "co_op_translator.core.vision.image_translator.ImageTranslator.create",
                    side_effect=ValueError("No CV"),
                ):

                    translator = ProjectTranslator(
                        "ko ja", str(tmp_path), markdown_only=False
                    )

                    # Should auto-switch to markdown-only
                    assert translator.markdown_only is True
                    assert translator.image_translator is None

                    # Should have helpful error message
                    log_text = caplog.text
                    assert "Computer Vision not configured" in log_text
                    assert "AZURE_COMPUTER_VISION_KEY" in log_text
