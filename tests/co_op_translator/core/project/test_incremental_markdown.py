from pathlib import Path

import pytest

from co_op_translator.core.project.translation.incremental_markdown import (
    DISCLAIMER_END,
    DISCLAIMER_START,
    build_incremental_markdown,
    split_markdown_blocks,
    strip_managed_disclaimer,
)
from co_op_translator.core.project.translation.manager import TranslationManager
from co_op_translator.core.project.translation.memory import TranslationBaseline


class RecordingProvider:
    def __init__(self, baseline: TranslationBaseline | None):
        self.baseline = baseline
        self.candidates = []

    def load_baseline(self, **kwargs):
        return self.baseline

    def record_candidate(self, **kwargs):
        self.candidates.append(kwargs)


class BlockTranslator:
    def __init__(self):
        self.calls = []

    async def translate_markdown(
        self, document, language_code, source_path=None, **kwargs
    ):
        self.calls.append((document, language_code, Path(source_path)))
        if document.strip() == "New source paragraph.":
            return "새 원문 문단입니다."
        return f"FULL:{document}"

    async def generate_disclaimer(self, language_code):
        return ""


@pytest.mark.asyncio
async def test_incremental_markdown_preserves_human_edits_and_translates_changes():
    baseline = TranslationBaseline(
        source_text="# Title\n\nStable paragraph.\n\nOld source paragraph.\n",
        target_text="# 제목\n\n안정된 문단입니다.\n\n이전 원문 문단입니다.\n",
    )
    current_source = "# Title\n\nStable paragraph.\n\nNew source paragraph.\n"
    current_target = (
        "# 사람이 다듬은 제목\n\n사람이 다듬은 문단입니다.\n\n이전 원문 문단입니다.\n"
    )
    calls = []

    async def translate_block(block):
        calls.append(block)
        return "새 원문 문단입니다.\n"

    result = await build_incremental_markdown(
        baseline=baseline,
        current_source=current_source,
        current_target=current_target,
        translate_block=translate_block,
    )

    assert result.mode == "incremental"
    assert result.content == (
        "# 사람이 다듬은 제목\n\n"
        "사람이 다듬은 문단입니다.\n\n"
        "새 원문 문단입니다.\n"
    )
    assert calls == ["New source paragraph.\n"]
    assert result.preserved_units == 2
    assert result.translated_units == 1
    assert result.deleted_units == 1


@pytest.mark.asyncio
async def test_incremental_markdown_translates_insertions_and_removes_deletions():
    baseline = TranslationBaseline(
        source_text="# Title\n\nKeep.\n\nDelete me.\n",
        target_text="# 제목\n\n유지합니다.\n\n삭제합니다.\n",
    )

    async def translate_block(block):
        assert block == "Added.\n\n"
        return "추가합니다.\n\n"

    result = await build_incremental_markdown(
        baseline=baseline,
        current_source="# Title\n\nKeep.\n\nAdded.\n\n",
        current_target="# 사람이 다듬은 제목\n\n유지합니다.\n\n삭제합니다.\n",
        translate_block=translate_block,
    )

    assert result.mode == "incremental"
    assert result.content == "# 사람이 다듬은 제목\n\n유지합니다.\n\n추가합니다.\n\n"
    assert result.added_units == 0
    assert result.translated_units == 1
    assert result.deleted_units == 1


@pytest.mark.asyncio
async def test_incremental_markdown_counts_pure_insertions():
    baseline = TranslationBaseline(
        source_text="# Title\n\nKeep.\n",
        target_text="# 제목\n\n유지합니다.\n",
    )

    async def translate_block(block):
        assert block == "Added.\n\n"
        return "추가합니다.\n\n"

    result = await build_incremental_markdown(
        baseline=baseline,
        current_source="# Title\n\nAdded.\n\nKeep.\n",
        current_target="# 사람이 다듬은 제목\n\n유지합니다.\n",
        translate_block=translate_block,
    )

    assert result.mode == "incremental"
    assert result.added_units == 1
    assert result.deleted_units == 0
    assert result.content == "# 사람이 다듬은 제목\n\n추가합니다.\n\n유지합니다.\n"


@pytest.mark.asyncio
async def test_incremental_markdown_falls_back_for_changed_target_structure():
    baseline = TranslationBaseline(
        source_text="# Title\n\nParagraph.\n",
        target_text="# 제목\n\n문단입니다.\n",
    )

    result = await build_incremental_markdown(
        baseline=baseline,
        current_source="# Title\n\nChanged.\n",
        current_target="# 제목\n\n- 사람이 추가한 목록\n",
        translate_block=lambda block: None,
    )

    assert result.mode == "full"
    assert result.fallback_reason == "current_target_structure_changed"


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("baseline", "reason"),
    [
        (TranslationBaseline(source_text="", target_text=""), "empty_baseline"),
        (
            TranslationBaseline(
                source_text="# Title\n\nParagraph.\n",
                target_text="# 제목\n\n- 목록\n",
            ),
            "baseline_structure_mismatch",
        ),
    ],
)
async def test_incremental_markdown_rejects_invalid_baselines(baseline, reason):
    async def translate_block(block):
        raise AssertionError("invalid baselines must not invoke translation")

    result = await build_incremental_markdown(
        baseline=baseline,
        current_source="# Title\n\nChanged.\n",
        current_target="# 제목\n\n문단입니다.\n",
        translate_block=translate_block,
    )

    assert result.mode == "full"
    assert result.fallback_reason == reason


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("translated", "reason"),
    [
        ("", "empty_block_translation"),
        ("- 구조가 바뀐 목록\n", "translated_block_structure_mismatch"),
    ],
)
async def test_incremental_markdown_rejects_invalid_block_translation(
    translated, reason
):
    baseline = TranslationBaseline(
        source_text="# Title\n\nOld.\n",
        target_text="# 제목\n\n이전.\n",
    )

    async def translate_block(block):
        return translated

    result = await build_incremental_markdown(
        baseline=baseline,
        current_source="# Title\n\nChanged.\n",
        current_target="# 제목\n\n사람이 다듬은 이전 문단.\n",
        translate_block=translate_block,
    )

    assert result.mode == "full"
    assert result.fallback_reason == reason


@pytest.mark.asyncio
async def test_incremental_markdown_falls_back_for_ambiguous_duplicate_blocks():
    baseline = TranslationBaseline(
        source_text="# Title\n\nRepeat.\n\nRepeat.\n",
        target_text="# 제목\n\n반복 1.\n\n반복 2.\n",
    )

    async def translate_block(block):
        return "변경.\n"

    result = await build_incremental_markdown(
        baseline=baseline,
        current_source="# Title\n\nRepeat.\n\nChanged.\n",
        current_target="# 제목\n\n반복 1.\n\n반복 2.\n",
        translate_block=translate_block,
    )

    assert result.mode == "full"
    assert result.fallback_reason == "ambiguous_duplicate_blocks"


def test_strip_managed_disclaimer_keeps_translated_content():
    content = (
        "# 제목\n\n본문입니다.\n\n---\n"
        f"{DISCLAIMER_START}\n자동 생성 안내\n{DISCLAIMER_END}\n"
    )

    assert strip_managed_disclaimer(content) == "# 제목\n\n본문입니다.\n"
    assert [
        block.kind for block in split_markdown_blocks(strip_managed_disclaimer(content))
    ] == [
        "heading:h1",
        "paragraph",
    ]


def test_split_markdown_blocks_covers_supported_top_level_structures():
    content = (
        "---\ntitle: Guide\n---\n"
        "> Quote\n\n"
        "- Item\n\n"
        "| A |\n| --- |\n| B |\n\n"
        "```python\nprint('hello')\n```\n\n"
        "<section>HTML</section>\n\n"
        "---\n"
    )

    assert [block.kind for block in split_markdown_blocks(content)] == [
        "frontmatter",
        "blockquote",
        "list",
        "table",
        "code",
        "html",
        "thematic_break",
    ]
    assert split_markdown_blocks("\n\n")[0].kind == "text"


def test_strip_managed_disclaimer_ignores_incomplete_markers():
    plain = "# 제목\n"
    incomplete = f"# 제목\n\n{DISCLAIMER_START}\n안내만 있음\n"

    assert strip_managed_disclaimer(plain) == plain
    assert strip_managed_disclaimer(incomplete) == incomplete


@pytest.mark.asyncio
async def test_translation_manager_records_incremental_candidate(tmp_path):
    source_path = tmp_path / "docs" / "guide.md"
    source_path.parent.mkdir()
    source_path.write_text(
        "# Title\n\nStable paragraph.\n\nNew source paragraph.\n",
        encoding="utf-8",
    )
    target_path = tmp_path / "translations" / "ko" / "docs" / "guide.md"
    target_path.parent.mkdir(parents=True)
    target_path.write_text(
        "# 사람이 다듬은 제목\n\n사람이 다듬은 문단입니다.\n\n이전 원문 문단입니다.\n",
        encoding="utf-8",
    )
    provider = RecordingProvider(
        TranslationBaseline(
            source_text="# Title\n\nStable paragraph.\n\nOld source paragraph.\n",
            target_text="# 제목\n\n안정된 문단입니다.\n\n이전 원문 문단입니다.\n",
        )
    )
    translator = BlockTranslator()
    manager = TranslationManager(
        root_dir=tmp_path,
        translations_dir=tmp_path / "translations",
        image_dir=tmp_path / "translated_images",
        language_codes=["ko"],
        excluded_dirs=["translations", "translated_images"],
        supported_image_extensions=[],
        supported_notebook_extensions=[],
        markdown_translator=translator,
        translation_types=["markdown"],
        add_disclaimer=False,
        translation_state_provider=provider,
    )

    result = await manager.translate_markdown(source_path, "ko")

    assert Path(result) == target_path
    assert target_path.read_text(encoding="utf-8") == (
        "# 사람이 다듬은 제목\n\n" "사람이 다듬은 문단입니다.\n\n" "새 원문 문단입니다."
    )
    assert [call[0] for call in translator.calls] == ["New source paragraph."]
    assert len(provider.candidates) == 1
    assert provider.candidates[0]["update"].mode == "incremental"


@pytest.mark.asyncio
async def test_translation_manager_can_force_full_translation(tmp_path):
    source_path = tmp_path / "docs" / "guide.md"
    source_path.parent.mkdir()
    source_path.write_text("# Title\n\nSource paragraph.\n", encoding="utf-8")
    target_path = tmp_path / "translations" / "ko" / "docs" / "guide.md"
    target_path.parent.mkdir(parents=True)
    target_path.write_text("# 사람이 다듬은 제목\n\n문단입니다.\n", encoding="utf-8")
    provider = RecordingProvider(
        TranslationBaseline(
            source_text="# Title\n\nSource paragraph.\n",
            target_text="# 제목\n\n문단입니다.\n",
        )
    )
    translator = BlockTranslator()
    manager = TranslationManager(
        root_dir=tmp_path,
        translations_dir=tmp_path / "translations",
        image_dir=tmp_path / "translated_images",
        language_codes=["ko"],
        excluded_dirs=["translations", "translated_images"],
        supported_image_extensions=[],
        supported_notebook_extensions=[],
        markdown_translator=translator,
        translation_types=["markdown"],
        add_disclaimer=False,
        translation_state_provider=provider,
    )

    await manager.translate_markdown(source_path, "ko", incremental=False)

    assert target_path.read_text(encoding="utf-8") == (
        "FULL:# Title\n\nSource paragraph."
    )
    assert [call[0] for call in translator.calls] == ["# Title\n\nSource paragraph."]
    assert provider.candidates[0]["update"].mode == "full"
