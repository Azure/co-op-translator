"""Tests for markdown evaluation functionality.

This module contains tests for the OpenAIMarkdownEvaluator class and related evaluation utilities.
"""

import re
import pytest
from pathlib import Path
from unittest.mock import AsyncMock, patch, MagicMock

from co_op_translator.core.llm.providers.openai.markdown_evaluator import (
    OpenAIMarkdownEvaluator,
)
from co_op_translator.utils.llm.markdown_utils import generate_evaluation_prompt


# Sample test data for markdown evaluation
SAMPLE_MD_CONTENT = """
# Sample Document

This is a test document with various markdown elements.

```python
def hello():
    return "Hello, world!"
```

> This is an important note

- List item 1
- List item 2

[Link to docs](https://example.com)
"""


class ConcreteMarkdownEvaluator(OpenAIMarkdownEvaluator):
    """A concrete implementation of OpenAIMarkdownEvaluator for testing."""

    async def _run_prompt(self, prompt, index, total):
        # This implementation should be replaced by the mock in tests
        return """{
            "score": 0.9,
            "issues": ["Minor formatting issue"],
            "confidence": 0.95
        }"""


@pytest.fixture
def markdown_evaluator(tmp_path):
    """Create a concrete instance of OpenAIMarkdownEvaluator for testing."""
    with patch(
        "co_op_translator.core.llm.providers.openai.markdown_evaluator.OpenAIConfig"
    ) as mock_config:
        mock_config.get_chat_model_id.return_value = "gpt-4"
        mock_config.get_org_id.return_value = "test-org"
        mock_config.get_api_key.return_value = "test-api-key"

        return ConcreteMarkdownEvaluator(root_dir=tmp_path, use_llm=True, use_rule=True)


class TestGenerateEvaluationPrompt:
    """Test suite for the generate_evaluation_prompt function."""

    def test_generates_complete_prompt_structure(self):
        """Verify the prompt includes all required sections and formatting."""
        # Arrange
        original = "Test content"
        translated = "테스트 콘텐츠"
        language_code = "ko"
        language_name = "Korean"

        # Act
        prompt = generate_evaluation_prompt(
            original, translated, language_code, language_name
        )

        # Assert
        assert isinstance(prompt, str), "Prompt should be a string"
        assert original in prompt, "Original content should be included"
        assert translated in prompt, "Translated content should be included"
        assert language_code in prompt, "Target language should be specified"
        assert language_name in prompt, "Target language name should be specified"

        # Check for required sections (updated to match actual prompt structure)
        required_sections = [
            "ORIGINAL CONTENT SAMPLE",
            "TRANSLATED CONTENT SAMPLE",
            "COMPLETENESS",
            "ACCURACY",
            "JSON object",
        ]
        for section in required_sections:
            assert section in prompt, f"Missing required section: {section}"

    def test_preserves_markdown_structure(self):
        """Ensure markdown syntax is preserved in the evaluation prompt."""
        # Arrange
        test_content = SAMPLE_MD_CONTENT

        # Act
        prompt = generate_evaluation_prompt(test_content, test_content, "ko", "Korean")

        # Assert
        markdown_elements = [
            "```python",  # Code block
            "> ",  # Blockquote
            "- ",  # List item
            "# ",  # Heading
            "[Link to docs]",  # Link
        ]

        for element in markdown_elements:
            assert element in prompt, f"Markdown element not preserved: {element}"

    def test_basic_functionality(self):
        """Test basic functionality of generate_evaluation_prompt."""
        original = "# Hello World\nThis is a test document."
        translated = "# 안녕 세상\n이것은 테스트 문서입니다."
        language_code = "ko"
        language_name = "Korean"

        # Test basic functionality
        prompt = generate_evaluation_prompt(
            original, translated, language_code, language_name
        )

        # Basic validation
        assert prompt is not None
        assert isinstance(prompt, str)
        assert len(prompt) > 0

        # Check content presence
        assert language_code in prompt
        assert language_name in prompt
        assert "translation quality evaluator" in prompt.lower()
        assert "completeness" in prompt.lower()
        assert "accuracy" in prompt.lower()
        assert "JSON object" in prompt
        assert original in prompt
        assert translated in prompt

        # Test with identical content (perfect translation scenario)
        test_content = "# Test\nSample content for evaluation."
        prompt = generate_evaluation_prompt(test_content, test_content, "ko", "Korean")
        assert prompt is not None
        assert "ko" in prompt
        assert "Korean" in prompt
        assert test_content in prompt


class TestOpenAIMarkdownEvaluator:
    """Test suite for the OpenAIMarkdownEvaluator class."""

    @pytest.mark.asyncio
    async def test_initialization_sets_up_kernel_correctly(self, markdown_evaluator):
        """Verify the evaluator is properly initialized."""
        # Act - Evaluator is initialized in the fixture

        # Assert
        assert markdown_evaluator is not None, "Evaluator should be initialized"
        assert hasattr(
            markdown_evaluator, "_run_prompt"
        ), "Should have _run_prompt method"

    @pytest.mark.asyncio
    async def test_run_prompt_executes_with_expected_parameters(
        self, markdown_evaluator
    ):
        """Verify _run_prompt processes prompts with correct parameters."""
        # Arrange
        test_prompt = "Test prompt content"
        test_index = 1
        test_total = 3

        # Act
        result = await markdown_evaluator._run_prompt(
            prompt=test_prompt, index=test_index, total=test_total
        )

        # Assert
        assert result is not None, "Should return a result"
        assert isinstance(result, str), "Result should be a string"


class TestRuleBasedEvaluation:
    """Test suite for rule-based evaluation functionality."""

    @pytest.mark.parametrize(
        "original,translated,expected_score,description",
        [
            ("Short text", "짧은 텍스트", 1.0, "Similar length"),
            (
                "Short text",
                "This is a much longer translated text that might indicate issues",
                0.7,
                "Different length",
            ),
            ("", "", 1.0, "Empty strings"),
            (
                "Test with code: ```print('hi')```",
                "테스트 코드: ```print('hi')```",
                1.0,
                "Code block preservation",
            ),
            (
                "Test with [link](test.md)",
                "[링크](test.md) 테스트",
                1.0,
                "Link preservation",
            ),
        ],
    )
    def test_evaluate_translation_rule_based(
        self, original, translated, expected_score, description
    ):
        """Verify rule-based evaluation handles different translation scenarios."""
        # Arrange
        from co_op_translator.core.llm.markdown_evaluator import (
            evaluate_translation_rule_based,
        )

        # Act
        result = evaluate_translation_rule_based(original, translated, "ko")

        # Assert
        assert "confidence_score" in result, "Result should include confidence_score"
        assert "issues_found" in result, "Result should include issues_found"
        assert isinstance(result["issues_found"], list), "issues_found should be a list"

        # Allow for small variations in the score
        assert (
            abs(result["confidence_score"] - expected_score) < 0.3
        ), f"Expected score around {expected_score} for {description}, got {result['confidence_score']}"

    def test_rule_based_evaluation_with_markdown(self):
        """Verify rule-based evaluation handles markdown content correctly."""
        # Arrange
        from co_op_translator.core.llm.markdown_evaluator import (
            evaluate_translation_rule_based,
        )

        original = SAMPLE_MD_CONTENT
        translated = SAMPLE_MD_CONTENT.replace("Sample Document", "샘플 문서")

        # Act
        result = evaluate_translation_rule_based(original, translated, "ko")

        # Assert
        assert (
            result["confidence_score"] > 0.8
        ), "Markdown structure should be preserved"
