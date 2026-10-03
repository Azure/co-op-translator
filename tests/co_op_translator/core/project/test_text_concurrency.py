import asyncio
import json
from functools import partial
from unittest.mock import AsyncMock, MagicMock

import pytest

from co_op_translator.core.project.project_translator import ProjectTranslator
from co_op_translator.core.project import project_evaluator
from co_op_translator.core.project.readme_translator import ReadmeTranslator
from co_op_translator.core.project.translation import TranslationManager
from co_op_translator.utils.common.events import translation_event_context
from co_op_translator.utils.common.metadata_utils import (
    calculate_file_hash,
    read_text_metadata_for_source,
)


class ConcurrentProvider:
    def __init__(self):
        self.active = 0
        self.peak = 0

    async def translate_markdown(self, document, language_code, **kwargs):
        self.active += 1
        self.peak = max(self.peak, self.active)
        try:
            await asyncio.sleep(0)
            return document
        finally:
            self.active -= 1

    translate_notebook = translate_markdown


def make_manager(root, provider, concurrency=3):
    return TranslationManager(
        root_dir=root,
        translations_dir=root / "translations",
        image_dir=root / "translated_images",
        language_codes=["ko", "ja"],
        excluded_dirs=["translations", "translated_images"],
        supported_image_extensions=[".png"],
        supported_notebook_extensions=[".ipynb"],
        markdown_translator=provider,
        notebook_translator=provider,
        translation_types=["markdown", "notebook"],
        add_disclaimer=False,
        concurrency=concurrency,
    )


def write_source(path, content):
    if path.suffix == ".ipynb":
        content = json.dumps(
            {
                "cells": [
                    {"cell_type": "markdown", "metadata": {}, "source": [content]}
                ],
                "metadata": {},
                "nbformat": 4,
                "nbformat_minor": 5,
            }
        )
    path.write_text(content, encoding="utf-8")


@pytest.mark.asyncio
@pytest.mark.parametrize("suffix", [".md", ".ipynb"])
@pytest.mark.parametrize("outdated", [False, True])
async def test_concurrent_new_and_outdated_files_preserve_all_metadata(
    tmp_path, suffix, outdated
):
    provider = ConcurrentProvider()
    manager = make_manager(tmp_path, provider)
    sources = [tmp_path / f"guide-{i}{suffix}" for i in range(4)]
    for source in sources:
        write_source(source, "# Original")
    translate_all = (
        manager.translate_all_markdown_files
        if suffix == ".md"
        else manager.translate_all_notebook_files
    )
    assert await translate_all() == (8, [])
    assert provider.peak == 3

    if outdated:
        for source in sources:
            write_source(source, "# Updated")
        provider.peak = 0
        pairs = [
            (source, tmp_path / "translations" / language / source.name)
            for source in sources
            for language in manager.language_codes
        ]
        assert await manager.retranslate_outdated_files(pairs) == 8
        assert provider.peak == 3

    for language in manager.language_codes:
        lang_dir = tmp_path / "translations" / language
        for source in sources:
            output = lang_dir / source.name
            assert output.is_file()
            assert ("Updated" if outdated else "Original") in output.read_text("utf-8")
            assert read_text_metadata_for_source(lang_dir, source.name)[
                "original_hash"
            ] == calculate_file_hash(source)
    assert provider.active == 0
    assert await translate_all() == (0, [])


@pytest.mark.asyncio
async def test_readme_concurrency_preserves_language_order_and_freshness(tmp_path):
    (tmp_path / "README.md").write_text("# Hello", encoding="utf-8")
    provider = ConcurrentProvider()
    translator = ReadmeTranslator(
        "ko ja fr",
        tmp_path,
        markdown_translator=provider,
        add_disclaimer=False,
        concurrency=2,
    )
    results = await translator.translate_async()
    assert [result.language_code for result in results] == ["ko", "ja", "fr"]
    assert all(
        result.translated_path.is_file() and not result.skipped for result in results
    )
    assert provider.peak == 2
    assert all(result.skipped for result in await translator.translate_async())


@pytest.mark.asyncio
async def test_concurrent_progress_attributes_out_of_order_results(tmp_path):
    manager = make_manager(tmp_path, None, concurrency=2)
    second_done = asyncio.Event()
    events = []

    async def first():
        await second_done.wait()
        return "first.md"

    async def second():
        second_done.set()
        return ""

    with translation_event_context(callback=events.append):
        results = await manager.process_text_requests(
            [first, second],
            "Translating markdown files",
            file_info=[("first.md", "ko"), ("second.md", "ja")],
            stage_key="translating_markdown_files",
        )
    assert results == ["first.md", ""]
    progress = [event for event in events if event.type == "stage_progress"]
    assert [(e.current_path, e.language, e.completed) for e in progress] == [
        ("second.md", "ja", 1),
        ("first.md", "ko", 2),
    ]
    finished = [e for e in events if e.type in ("file_failed", "file_completed")]
    assert [(e.type, e.current_path, e.language) for e in finished] == [
        ("file_failed", "second.md", "ja"),
        ("file_completed", "first.md", "ko"),
    ]
    assert all(e.stage_key == "translating_markdown_files" for e in finished)


@pytest.mark.asyncio
@pytest.mark.parametrize("kind", ["markdown", "notebook"])
async def test_failed_results_are_attributed_to_input_files(tmp_path, kind):
    manager = make_manager(tmp_path, ConcurrentProvider(), concurrency=2)
    suffix = ".md" if kind == "markdown" else ".ipynb"
    source = tmp_path / f"guide{suffix}"
    write_source(source, "# Guide")
    done = asyncio.Event()

    async def translate(path, language, **kwargs):
        if language == "ko":
            await done.wait()
            return str(path)
        done.set()
        return ""

    setattr(manager, f"translate_{kind}", translate)
    count, errors = await getattr(manager, f"translate_all_{kind}_files")()
    assert count == 1
    assert len(errors) == 1 and "ja" in errors[0] and source.name in errors[0]
    pairs = [
        (source, tmp_path / "translations" / lang / source.name)
        for lang in ("ko", "ja")
    ]
    assert await manager.retranslate_outdated_files(pairs) == 1


@pytest.mark.asyncio
async def test_formatting_retries_use_concurrency_and_disable_incremental(tmp_path):
    provider = ConcurrentProvider()
    manager = make_manager(tmp_path, provider)
    for i in range(3):
        write_source(tmp_path / f"guide-{i}.md", "# Guide")
    incremental_values = []
    original = manager.translate_markdown

    async def translate(*args, **kwargs):
        incremental_values.append(kwargs["incremental"])
        return await original(*args, **kwargs)

    manager.translate_markdown = translate
    await manager.check_and_retry_translations()
    assert incremental_values == [False] * 6
    assert provider.peak == 3


@pytest.mark.parametrize("invalid", [0, -1, True, 1.5, "2", None])
def test_constructors_reject_invalid_concurrency_before_provider_creation(
    tmp_path, invalid
):
    for construct in (
        partial(ProjectTranslator, "ko", tmp_path),
        partial(ReadmeTranslator, "ko", tmp_path),
        partial(make_manager, tmp_path, None),
    ):
        with pytest.raises(ValueError, match="concurrency must be a positive integer"):
            construct(concurrency=invalid)


@pytest.mark.asyncio
async def test_low_confidence_retranslation_uses_concurrency(tmp_path, monkeypatch):
    translator = ProjectTranslator(
        "ko",
        tmp_path,
        translation_types=["markdown"],
        add_disclaimer=False,
        initialize_translators=False,
        concurrency=2,
    )
    provider = ConcurrentProvider()
    translator.markdown_translator = provider
    translator.translation_manager.markdown_translator = provider
    sources = [tmp_path / f"guide-{i}.md" for i in range(3)]
    for source in sources:
        write_source(source, "# Guide")
    evaluator = MagicMock()
    evaluator.get_low_confidence_translations = AsyncMock(
        return_value=[
            (tmp_path / "translations" / "ko" / source.name, 0.4) for source in sources
        ]
    )
    monkeypatch.setattr(
        project_evaluator, "ProjectEvaluator", MagicMock(return_value=evaluator)
    )
    original = translator.translation_manager.translate_markdown
    incremental_values = []

    async def translate(*args, **kwargs):
        incremental_values.append(kwargs["incremental"])
        return await original(*args, **kwargs)

    translator.translation_manager.translate_markdown = translate
    assert await translator.retranslate_low_confidence_files("ko") == (3, [])
    assert incremental_values == [False] * 3
    assert provider.peak == 2
