from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from co_op_translator.core.llm.model_clients import ModelResponse
from co_op_translator.core.llm.providers.azure.markdown_evaluator import (
    AzureMarkdownEvaluator,
)
from co_op_translator.core.llm.providers.azure.markdown_translator import (
    AzureMarkdownTranslator,
)
from co_op_translator.core.llm.providers.openai.markdown_evaluator import (
    OpenAIMarkdownEvaluator,
)
from co_op_translator.core.llm.providers.openai.markdown_translator import (
    OpenAIMarkdownTranslator,
)
from co_op_translator.utils.markdown.constants import SPLIT_DELIMITER


class RecordingModelClient:
    def __init__(self, response: ModelResponse) -> None:
        self.response = response
        self.calls = []

    async def complete(
        self,
        system_prompt,
        user_content,
        *,
        temperature=None,
    ):
        self.calls.append((system_prompt, user_content, temperature))
        return self.response


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("translator_type", "sleep_target"),
    [
        (
            AzureMarkdownTranslator,
            "co_op_translator.core.llm.providers.azure.markdown_translator.asyncio.sleep",
        ),
        (
            OpenAIMarkdownTranslator,
            "co_op_translator.core.llm.providers.openai.markdown_translator.asyncio.sleep",
        ),
    ],
)
async def test_provider_translators_use_framework_neutral_client(
    tmp_path,
    translator_type,
    sleep_target,
):
    client = RecordingModelClient(ModelResponse("translated", "stop"))
    translator = translator_type(root_dir=tmp_path, model_client=client)

    with patch(sleep_target, new=AsyncMock()):
        result = await translator._run_prompt_once(
            f"system rules{SPLIT_DELIMITER}source content",
            1,
            1,
        )

    assert result == "translated"
    assert client.calls == [("system rules", "source content", None)]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("evaluator_type", "sleep_target"),
    [
        (
            AzureMarkdownEvaluator,
            "co_op_translator.core.llm.providers.azure.markdown_evaluator.asyncio.sleep",
        ),
        (
            OpenAIMarkdownEvaluator,
            "co_op_translator.core.llm.providers.openai.markdown_evaluator.asyncio.sleep",
        ),
    ],
)
async def test_provider_evaluators_use_framework_neutral_client(
    tmp_path,
    evaluator_type,
    sleep_target,
):
    client = RecordingModelClient(ModelResponse('{"score": 1}', "stop"))
    evaluator = evaluator_type(root_dir=tmp_path, model_client=client)

    with patch(sleep_target, new=AsyncMock()):
        result = await evaluator._run_prompt("evaluation prompt", 1, 1)

    assert result == '{"score": 1}'
    assert client.calls == [("", "evaluation prompt", None)]


@pytest.mark.asyncio
async def test_injected_model_client_bypasses_provider_credential_fallback(tmp_path):
    client = RecordingModelClient(ModelResponse("translated", "stop"))
    translator = OpenAIMarkdownTranslator(root_dir=tmp_path, model_client=client)

    with (
        patch(
            "co_op_translator.core.llm.providers.openai.markdown_translator.OpenAIConfig.get_env_sets",
            side_effect=AssertionError("provider fallback should not be queried"),
        ),
        patch(
            "co_op_translator.core.llm.providers.openai.markdown_translator.asyncio.sleep",
            new=AsyncMock(),
        ),
    ):
        result = await translator._run_prompt(
            f"system rules{SPLIT_DELIMITER}source content",
            1,
            1,
        )

    assert result == "translated"
