import json
from pathlib import Path

import pytest

from co_op_translator.core.project import ReadmeTranslator


class FakeMarkdownTranslator:
    def __init__(self):
        self.calls = []
        self.disclaimer_calls = []

    async def translate_markdown(self, document, language_code, source_path=None):
        self.calls.append((document, language_code, Path(source_path)))
        return document

    async def generate_disclaimer(self, language_code):
        self.disclaimer_calls.append(language_code)
        return f"Disclaimer for {language_code}"


def _write_readme_project(root: Path) -> None:
    (root / "docs").mkdir()
    (root / "docs" / "guide.md").write_text("# Guide", encoding="utf-8")
    (root / "docs" / "tutorial.ipynb").write_text("{}", encoding="utf-8")
    (root / "assets").mkdir()
    (root / "assets" / "manual.pdf").write_text("pdf", encoding="utf-8")
    (root / "images").mkdir()
    (root / "images" / "hero.png").write_text("image", encoding="utf-8")
    (root / "README.md").write_text(
        "\n".join(
            [
                "# Course",
                "",
                "[Guide](docs/guide.md#quick-start)",
                "[Notebook](docs/tutorial.ipynb?view=1#cell)",
                "[Manual](assets/manual.pdf)",
                "![Hero](images/hero.png)",
                "[Korean](./translations/ko/README.md)",
                "[Anchor](#course)",
                "[Web](https://example.com/docs.md)",
                "",
            ]
        ),
        encoding="utf-8",
    )


@pytest.mark.asyncio
async def test_readme_translator_writes_only_root_readme_with_source_links(tmp_path):
    _write_readme_project(tmp_path)
    markdown_translator = FakeMarkdownTranslator()
    translator = ReadmeTranslator(
        "ko",
        root_dir=tmp_path,
        add_disclaimer=False,
        markdown_translator=markdown_translator,
    )

    results = await translator.translate_async()

    translated_path = tmp_path / "translations" / "ko" / "README.md"
    translated_text = translated_path.read_text(encoding="utf-8")

    assert len(results) == 1
    assert results[0].translated_path == translated_path
    assert results[0].skipped is False
    assert markdown_translator.calls == [
        (
            (tmp_path / "README.md").read_text(encoding="utf-8").strip(),
            "ko",
            (tmp_path / "README.md").resolve(),
        )
    ]
    assert "[Guide](../../docs/guide.md#quick-start)" in translated_text
    assert "[Notebook](../../docs/tutorial.ipynb?view=1#cell)" in translated_text
    assert "[Manual](../../assets/manual.pdf)" in translated_text
    assert "[Korean](./README.md)" in translated_text
    assert "[Anchor](#course)" in translated_text
    assert "[Web](https://example.com/docs.md)" in translated_text
    assert not (tmp_path / "translations" / "ko" / "docs" / "guide.md").exists()


@pytest.mark.asyncio
async def test_readme_translator_saves_metadata_and_skips_current_readme(tmp_path):
    _write_readme_project(tmp_path)
    markdown_translator = FakeMarkdownTranslator()
    translator = ReadmeTranslator(
        ["ko"],
        root_dir=tmp_path,
        add_disclaimer=False,
        markdown_translator=markdown_translator,
    )

    first = await translator.translate_async()
    second = await translator.translate_async()

    metadata_path = tmp_path / "translations" / "ko" / ".co-op-translator.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))

    assert first[0].skipped is False
    assert second[0].skipped is True
    assert len(markdown_translator.calls) == 1
    assert metadata["README.md"]["source_file"] == "README.md"
    assert metadata["README.md"]["language_code"] == "ko"


@pytest.mark.asyncio
async def test_readme_translator_update_retranslates_current_readme(tmp_path):
    _write_readme_project(tmp_path)
    markdown_translator = FakeMarkdownTranslator()
    translator = ReadmeTranslator(
        "ko",
        root_dir=tmp_path,
        add_disclaimer=False,
        markdown_translator=markdown_translator,
    )

    await translator.translate_async()
    results = await translator.translate_async(update=True)

    assert results[0].skipped is False
    assert len(markdown_translator.calls) == 2


@pytest.mark.asyncio
async def test_readme_translator_estimates_only_pending_readmes(tmp_path):
    _write_readme_project(tmp_path)
    markdown_translator = FakeMarkdownTranslator()
    translator = ReadmeTranslator(
        "ko ja",
        root_dir=tmp_path,
        add_disclaimer=False,
        markdown_translator=markdown_translator,
    )

    initial_tokens = translator.estimate_tokens()
    initial_words = translator.estimate_words()
    await translator.translate_readme("ko")

    assert initial_tokens > translator.estimate_tokens()
    assert initial_words > translator.estimate_words()
    assert translator.get_pending_language_codes() == ["ja"]
    assert translator.get_pending_language_codes(update=True) == ["ko", "ja"]


@pytest.mark.asyncio
async def test_readme_translator_appends_disclaimer(tmp_path):
    _write_readme_project(tmp_path)
    markdown_translator = FakeMarkdownTranslator()
    translator = ReadmeTranslator(
        "ko",
        root_dir=tmp_path,
        add_disclaimer=True,
        markdown_translator=markdown_translator,
    )

    await translator.translate_async()

    translated_text = (tmp_path / "translations" / "ko" / "README.md").read_text(
        encoding="utf-8"
    )
    assert "<!-- CO-OP TRANSLATOR DISCLAIMER START -->" in translated_text
    assert "Disclaimer for ko" in translated_text
    assert markdown_translator.disclaimer_calls == ["ko"]


@pytest.mark.asyncio
async def test_readme_translator_requires_root_readme(tmp_path):
    translator = ReadmeTranslator(
        "ko",
        root_dir=tmp_path,
        markdown_translator=FakeMarkdownTranslator(),
    )

    with pytest.raises(FileNotFoundError, match="README.md not found"):
        await translator.translate_async()
