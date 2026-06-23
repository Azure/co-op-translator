from unittest.mock import MagicMock

import pytest

from co_op_translator.api import translation as api
from co_op_translator.glossary import get_glossary_terms, set_glossary_terms


@pytest.mark.asyncio
async def test_run_translation_calls_project_translator(tmp_path):
    root_dir = tmp_path

    api.Config.check_configuration = MagicMock(return_value=None)
    api.LLMConfig.validate_connectivity = MagicMock(return_value=None)
    api.setup_logging = MagicMock(return_value=None)

    project_translator_instance = MagicMock()
    project_translator_class = MagicMock(return_value=project_translator_instance)
    api.ProjectTranslator = project_translator_class

    api.run_translation(
        language_codes="ko ja",
        root_dir=str(root_dir),
        update=False,
        images=False,
        markdown=True,
        notebook=False,
        debug=False,
        save_logs=False,
        yes=True,
    )

    assert project_translator_class.call_count == 2
    project_translator_class.assert_any_call(
        "ko ja",
        str(root_dir),
        translation_types=["markdown"],
        add_disclaimer=False,
        translations_dir=None,
        image_dir=None,
        lang_subdir=None,
    )
    project_translator_instance.translate_project.assert_called_once_with(
        update=False,
    )


@pytest.mark.asyncio
async def test_run_translation_with_disclaimer_flag(tmp_path):
    root_dir = tmp_path

    api.Config.check_configuration = MagicMock(return_value=None)
    api.LLMConfig.validate_connectivity = MagicMock(return_value=None)
    api.setup_logging = MagicMock(return_value=None)

    project_translator_instance = MagicMock()
    project_translator_class = MagicMock(return_value=project_translator_instance)
    api.ProjectTranslator = project_translator_class

    api.run_translation(
        language_codes="ko",
        root_dir=str(root_dir),
        markdown=True,
        add_disclaimer=True,
    )

    assert project_translator_class.call_count == 2
    project_translator_class.assert_any_call(
        "ko",
        str(root_dir),
        translation_types=["markdown"],
        add_disclaimer=True,
        translations_dir=None,
        image_dir=None,
        lang_subdir=None,
    )


@pytest.mark.asyncio
async def test_run_translation_with_multiple_root_dirs(tmp_path):
    root1 = tmp_path / "content1"
    root2 = tmp_path / "content2"
    root1.mkdir()
    root2.mkdir()

    api.Config.check_configuration = MagicMock(return_value=None)
    api.LLMConfig.validate_connectivity = MagicMock(return_value=None)
    api.setup_logging = MagicMock(return_value=None)

    project_translator_instance = MagicMock()
    project_translator_class = MagicMock(return_value=project_translator_instance)
    api.ProjectTranslator = project_translator_class

    api.run_translation(
        language_codes="ko",
        markdown=True,
        root_dirs=[str(root1), str(root2)],
    )

    assert project_translator_class.call_count == 4
    called_roots = {call.args[1] for call in project_translator_class.call_args_list}
    assert called_roots == {str(root1), str(root2)}


@pytest.mark.asyncio
async def test_run_translation_with_groups(tmp_path):
    root1 = tmp_path / "content1"
    root2 = tmp_path / "content2"
    out1 = tmp_path / "out1"
    out2 = tmp_path / "out2"
    root1.mkdir()
    root2.mkdir()
    out1.mkdir()
    out2.mkdir()

    api.Config.check_configuration = MagicMock(return_value=None)
    api.LLMConfig.validate_connectivity = MagicMock(return_value=None)
    api.setup_logging = MagicMock(return_value=None)

    project_translator_instance = MagicMock()
    project_translator_class = MagicMock(return_value=project_translator_instance)
    api.ProjectTranslator = project_translator_class

    groups = [
        (str(root1), str(out1)),
        (str(root2), str(out2)),
    ]

    api.run_translation(
        language_codes="ko",
        markdown=True,
        groups=groups,
    )

    assert project_translator_class.call_count == 4
    called = {
        (call.args[1], call.kwargs["translations_dir"])
        for call in project_translator_class.call_args_list
    }
    assert called == {(str(root1), str(out1)), (str(root2), str(out2))}


@pytest.mark.asyncio
async def test_run_translation_dry_run_groups_shows_single_aggregated_estimate(
    tmp_path,
):
    root1 = tmp_path / "content1"
    root2 = tmp_path / "content2"
    out1 = tmp_path / "out1"
    out2 = tmp_path / "out2"
    root1.mkdir()
    root2.mkdir()
    out1.mkdir()
    out2.mkdir()

    api.Config.check_configuration = MagicMock(return_value=None)
    api.LLMConfig.validate_connectivity = MagicMock(return_value=None)
    api.setup_logging = MagicMock(return_value=None)

    translators = [MagicMock() for _ in range(4)]
    api.ProjectTranslator = MagicMock(side_effect=translators)

    api.estimate_translation_tokens = MagicMock(
        side_effect=[
            {
                "markdown": 65,
                "notebook": 0,
                "images": 0,
                "outdated_markdown": 0,
                "outdated_notebook": 0,
                "outdated_images": 0,
                "outdated": 0,
                "total": 65,
            },
            {
                "markdown": 65,
                "notebook": 0,
                "images": 0,
                "outdated_markdown": 0,
                "outdated_notebook": 0,
                "outdated_images": 0,
                "outdated": 0,
                "total": 65,
            },
        ]
    )
    api.estimate_translation_words = MagicMock(
        side_effect=[
            {
                "markdown": 40,
                "notebook": 0,
                "images": 0,
                "outdated": 0,
                "total": 40,
            },
            {
                "markdown": 40,
                "notebook": 0,
                "images": 0,
                "outdated": 0,
                "total": 40,
            },
        ]
    )

    echo_mock = MagicMock()
    api.click.echo = echo_mock

    groups = [
        (str(root1), str(out1)),
        (str(root2), str(out2)),
    ]

    api.run_translation(
        language_codes="ko",
        markdown=True,
        groups=groups,
        dry_run=True,
    )

    estimate_lines = [
        call.args[0]
        for call in echo_mock.call_args_list
        if call.args
        and "Estimated translation volume before translation" in call.args[0]
    ]
    assert len(estimate_lines) == 1
    grouped_progress_lines = [
        call.args[0]
        for call in echo_mock.call_args_list
        if call.args and "Translating all groups" in call.args[0]
    ]
    assert grouped_progress_lines == []
    assert (
        estimate_lines[0]
        == "📊 Estimated translation volume before translation: 130 tokens (80 words) "
        "(breakdown: translation: markdown: 130 | retranslation: outdated markdowns: 0)"
    )


@pytest.mark.asyncio
async def test_run_translation_dry_run_uses_virtual_readme_without_writing(tmp_path):
    readme_path = tmp_path / "README.md"
    readme_path.write_text(
        "\n".join(
            [
                "# Sample",
                "",
                "<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->",
                "old languages",
                "<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->",
                "",
                "<!-- CO-OP TRANSLATOR OTHER COURSES START -->",
                "old courses",
                "<!-- CO-OP TRANSLATOR OTHER COURSES END -->",
                "",
            ]
        ),
        encoding="utf-8",
    )

    api.Config.check_configuration = MagicMock(return_value=None)
    api.LLMConfig.validate_connectivity = MagicMock(return_value=None)
    api.setup_logging = MagicMock(return_value=None)
    api.update_readme_languages_table = MagicMock(return_value=True)
    api.update_readme_other_courses = MagicMock(return_value=True)

    project_translator_instance = MagicMock()
    project_translator_class = MagicMock(return_value=project_translator_instance)
    api.ProjectTranslator = project_translator_class

    token_estimate_mock = MagicMock(
        return_value={
            "markdown": 10,
            "notebook": 0,
            "images": 0,
            "outdated_markdown": 0,
            "outdated_notebook": 0,
            "outdated_images": 0,
            "outdated": 0,
            "total": 10,
        }
    )
    word_estimate_mock = MagicMock(
        return_value={
            "markdown": 5,
            "notebook": 0,
            "images": 0,
            "outdated": 0,
            "total": 5,
        }
    )
    api.estimate_translation_tokens = token_estimate_mock
    api.estimate_translation_words = word_estimate_mock

    original_readme = readme_path.read_text(encoding="utf-8")

    api.run_translation(
        language_codes="ko",
        root_dir=str(tmp_path),
        markdown=True,
        dry_run=True,
        repo_url="https://github.com/example/repo",
    )

    virtual_inputs = token_estimate_mock.call_args.kwargs["virtual_file_contents"]
    assert readme_path.resolve() in virtual_inputs
    assert virtual_inputs[readme_path.resolve()] != original_readme
    assert "old languages" not in virtual_inputs[readme_path.resolve()]
    assert "old courses" not in virtual_inputs[readme_path.resolve()]
    assert readme_path.read_text(encoding="utf-8") == original_readme
    api.update_readme_languages_table.assert_not_called()
    api.update_readme_other_courses.assert_not_called()


@pytest.mark.asyncio
async def test_run_translation_accepts_glossaries_and_restores_previous_terms(tmp_path):
    root_dir = tmp_path

    api.Config.check_configuration = MagicMock(return_value=None)
    api.LLMConfig.validate_connectivity = MagicMock(return_value=None)
    api.setup_logging = MagicMock(return_value=None)

    project_translator_instance = MagicMock()
    project_translator_class = MagicMock(return_value=project_translator_instance)
    api.ProjectTranslator = project_translator_class

    observed_terms: list[list[str]] = []

    def fake_estimate_tokens(*args, **kwargs):
        observed_terms.append(get_glossary_terms())
        return {
            "markdown": 10,
            "notebook": 0,
            "images": 0,
            "outdated_markdown": 0,
            "outdated_notebook": 0,
            "outdated_images": 0,
            "outdated": 0,
            "total": 10,
        }

    api.estimate_translation_tokens = MagicMock(side_effect=fake_estimate_tokens)
    api.estimate_translation_words = MagicMock(
        return_value={
            "markdown": 5,
            "notebook": 0,
            "images": 0,
            "outdated": 0,
            "total": 5,
        }
    )

    set_glossary_terms(["Existing Term"])
    try:
        api.run_translation(
            language_codes="ko",
            root_dir=str(root_dir),
            markdown=True,
            glossaries=[" Co-op Translator ", "Co-op Translator", "Azure AI"],
        )

        assert observed_terms == [["Co-op Translator", "Azure AI"]]
        assert get_glossary_terms() == ["Existing Term"]
        project_translator_instance.translate_project.assert_called_once_with(
            update=False,
        )
    finally:
        set_glossary_terms([])


@pytest.mark.asyncio
async def test_translate_markdown_content_uses_content_only_translator(monkeypatch):
    class FakeMarkdownTranslator:
        def __init__(self):
            self.calls = []

        async def translate_markdown(self, document, language_code, **kwargs):
            self.calls.append((document, language_code, kwargs))
            return f"translated:{language_code}:{document}"

    fake = FakeMarkdownTranslator()
    monkeypatch.setattr(api.MarkdownTranslator, "create", MagicMock(return_value=fake))

    result = await api.translate_markdown_content(
        "# Hello",
        "ko",
        {
            "source_path": "docs/guide.md",
            "add_metadata": False,
            "add_disclaimer": True,
        },
    )

    assert result == "translated:ko:# Hello"
    assert fake.calls == [
        (
            "# Hello",
            "ko",
            {
                "source_path": "docs/guide.md",
                "add_metadata": False,
                "add_disclaimer": True,
            },
        )
    ]


def test_rewrite_markdown_paths_uses_target_path(tmp_path):
    root_dir = tmp_path
    source_path = root_dir / "docs" / "guide.md"
    target_path = root_dir / "out" / "ko" / "docs" / "guide.md"
    image_path = root_dir / "docs" / "images" / "hero.png"

    source_path.parent.mkdir(parents=True)
    image_path.parent.mkdir(parents=True)
    source_path.write_text("# Guide", encoding="utf-8")
    image_path.write_text("image", encoding="utf-8")

    content = """---
title: Guide
image: images/hero.png
---
# Guide

![Hero](images/hero.png)
"""

    rewritten = api.rewrite_markdown_paths(
        content,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ko",
            "root_dir": root_dir,
            "translations_dir": root_dir / "out",
            "translated_images_dir": root_dir / "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    assert "translated_images/ko/hero." in rewritten
    assert "images/hero.png" not in rewritten
    assert "../../../translated_images/ko/" in rewritten
