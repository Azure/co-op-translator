from pathlib import Path

import pytest

from co_op_translator.config.base_config import Config
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.core.llm.markdown_translator import MarkdownTranslator


@pytest.mark.api_key_required
@pytest.mark.asyncio
async def test_live_translation_preserves_windows_path_and_translates_prose(tmp_path):
    """Verify the #589 regression through a configured live model provider."""
    Config.load_environment(Path.cwd())
    try:
        LLMConfig.get_available_provider()
    except ValueError as exc:
        pytest.skip(f"No live model provider is configured: {exc}")

    source = r"Path `C:\docs\`. Translate this sentence. Use `SETTING`."
    translator = MarkdownTranslator.create(root_dir=tmp_path)

    translated = await translator.translate_markdown(
        document=source,
        language_code="es",
        source_path=tmp_path / "windows-path.md",
    )

    assert r"`C:\docs\`" in translated
    assert "`SETTING`" in translated
    assert "Translate this sentence." not in translated
