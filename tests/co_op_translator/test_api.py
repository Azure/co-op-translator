import json
from unittest.mock import MagicMock

import pytest
from PIL import Image

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
    monkeypatch,
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

    class RecordingReporter:
        rich_enabled = False

        def __init__(self):
            self.estimates = []
            self.messages = []

        def header(self, **kwargs):
            self.messages.append(("header", kwargs))

        def info(self, message):
            self.messages.append(("info", message))

        def success(self, message):
            self.messages.append(("success", message))

        def warning(self, message):
            self.messages.append(("warning", message))

        def print(self, message, **kwargs):
            self.messages.append(("print", message, kwargs))

        def estimate_summary(self, **kwargs):
            self.estimates.append(kwargs)

    reporter = RecordingReporter()
    monkeypatch.setattr(api, "get_progress_reporter", MagicMock(return_value=reporter))

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

    assert len(reporter.estimates) == 1
    estimate = reporter.estimates[0]
    assert estimate["title"] == "Estimated Translation Volume"
    assert estimate["total_tokens"] == 130
    assert estimate["total_words"] == 80
    assert estimate["rows"] == [
        ("Translation: markdown", 130),
        ("Retranslation: outdated markdowns", 0),
    ]
    assert estimate["fallback"].isascii()
    assert (
        estimate["fallback"]
        == "Estimated translation volume before translation: 130 tokens (80 words) "
        "(breakdown: translation: markdown: 130 | retranslation: outdated markdowns: 0)"
    )


def test_run_translation_progress_callback_receives_structured_events(
    monkeypatch, tmp_path
):
    monkeypatch.setattr(api.Config, "check_configuration", MagicMock(return_value=None))
    monkeypatch.setattr(
        api.LLMConfig, "validate_connectivity", MagicMock(return_value=None)
    )
    monkeypatch.setattr(api, "setup_logging", MagicMock(return_value=None))

    translator = MagicMock()
    monkeypatch.setattr(api, "ProjectTranslator", MagicMock(return_value=translator))
    monkeypatch.setattr(
        api,
        "estimate_translation_tokens",
        MagicMock(
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
        ),
    )
    monkeypatch.setattr(
        api,
        "estimate_translation_words",
        MagicMock(
            return_value={
                "markdown": 5,
                "notebook": 0,
                "images": 0,
                "outdated": 0,
                "total": 5,
            }
        ),
    )

    events = []

    api.run_translation(
        language_codes="ko",
        root_dir=str(tmp_path),
        markdown=True,
        dry_run=True,
        progress_callback=events.append,
    )

    payloads = [event.to_dict() for event in events]
    event_types = [payload["type"] for payload in payloads]

    assert event_types[0] == "run_started"
    assert "estimate_ready" in event_types
    assert event_types[-1] == "run_completed"
    assert payloads[0]["schema"] == "co-op.translation.event.v1"
    assert payloads[0]["command"] == "run_translation"
    assert payloads[0]["languages"] == ["ko"]
    assert payloads[event_types.index("estimate_ready")]["total_tokens"] == 10


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
async def test_run_translation_readme_only_uses_readme_translator(
    monkeypatch, tmp_path
):
    (tmp_path / "README.md").write_text("# Hello", encoding="utf-8")

    monkeypatch.setattr(api.Config, "check_configuration", MagicMock(return_value=None))
    monkeypatch.setattr(
        api.LLMConfig, "validate_connectivity", MagicMock(return_value=None)
    )
    monkeypatch.setattr(api, "setup_logging", MagicMock(return_value=None))
    monkeypatch.setattr(
        api, "update_readme_languages_table", MagicMock(return_value=False)
    )
    monkeypatch.setattr(
        api, "update_readme_other_courses", MagicMock(return_value=False)
    )
    project_translator = MagicMock()
    monkeypatch.setattr(api, "ProjectTranslator", project_translator)

    estimate_instance = MagicMock()
    estimate_instance.estimate_tokens.return_value = 10
    estimate_instance.estimate_words.return_value = 5
    run_instance = MagicMock()
    readme_translator = MagicMock(side_effect=[estimate_instance, run_instance])
    monkeypatch.setattr(api, "ReadmeTranslator", readme_translator)

    api.run_translation(
        language_codes="ko",
        root_dir=str(tmp_path),
        readme_only=True,
    )

    assert project_translator.call_count == 0
    assert readme_translator.call_count == 2
    readme_translator.assert_any_call(
        "ko",
        str(tmp_path),
        translations_dir=None,
        image_dir=None,
        add_disclaimer=False,
        lang_subdir=None,
    )
    run_instance.translate.assert_called_once_with(update=False)


@pytest.mark.asyncio
async def test_run_translation_readme_only_dry_run_does_not_write(
    monkeypatch, tmp_path
):
    (tmp_path / "README.md").write_text("# Hello", encoding="utf-8")

    monkeypatch.setattr(api.Config, "check_configuration", MagicMock(return_value=None))
    monkeypatch.setattr(
        api.LLMConfig, "validate_connectivity", MagicMock(return_value=None)
    )
    monkeypatch.setattr(api, "setup_logging", MagicMock(return_value=None))
    update_languages = MagicMock(return_value=True)
    update_courses = MagicMock(return_value=True)
    monkeypatch.setattr(api, "update_readme_languages_table", update_languages)
    monkeypatch.setattr(api, "update_readme_other_courses", update_courses)

    estimate_instance = MagicMock()
    estimate_instance.estimate_tokens.return_value = 10
    estimate_instance.estimate_words.return_value = 5
    readme_translator = MagicMock(return_value=estimate_instance)
    monkeypatch.setattr(api, "ReadmeTranslator", readme_translator)

    api.run_translation(
        language_codes="ko",
        root_dir=str(tmp_path),
        readme_only=True,
        dry_run=True,
    )

    assert readme_translator.call_count == 1
    estimate_instance.translate.assert_not_called()
    update_languages.assert_not_called()
    update_courses.assert_not_called()


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
        },
    )

    assert result == "translated:ko:# Hello"
    assert fake.calls == [
        (
            "# Hello",
            "ko",
            {
                "source_path": "docs/guide.md",
            },
        )
    ]


@pytest.mark.asyncio
async def test_translate_notebook_content_uses_content_only_translator(monkeypatch):
    class FakeNotebookTranslator:
        def __init__(self):
            self.calls = []

        async def translate_notebook(self, notebook, language_code, **kwargs):
            self.calls.append((notebook, language_code, kwargs))
            payload = json.loads(notebook)
            payload["metadata"]["translated_to"] = language_code
            return json.dumps(payload)

    notebook = json.dumps(
        {
            "cells": [
                {"cell_type": "markdown", "metadata": {}, "source": ["# Hello\n"]}
            ],
            "metadata": {},
            "nbformat": 4,
            "nbformat_minor": 5,
        }
    )
    fake = FakeNotebookTranslator()
    monkeypatch.setattr(
        api.JupyterNotebookTranslator, "create", MagicMock(return_value=fake)
    )

    result = await api.translate_notebook_content(
        notebook,
        "ko",
        {
            "source_path": "docs/tutorial.ipynb",
        },
    )

    assert json.loads(result)["metadata"]["translated_to"] == "ko"
    assert fake.calls == [
        (
            notebook,
            "ko",
            {
                "source_path": "docs/tutorial.ipynb",
            },
        )
    ]


def test_translate_image_content_uses_content_only_translator(monkeypatch):
    class FakeImageTranslator:
        def __init__(self):
            self.calls = []

        def translate_image(self, image_path, language_code, fast_mode=False):
            self.calls.append((image_path, language_code, fast_mode))
            return Image.new("RGB", (10, 10), "blue")

    fake = FakeImageTranslator()
    create = MagicMock(return_value=fake)
    monkeypatch.setattr(api.ImageTranslator, "create", create)

    result = api.translate_image_content(
        "docs/hero.png",
        "ko",
        {
            "root_dir": "docs",
            "fast_mode": True,
        },
    )

    assert isinstance(result, Image.Image)
    assert result.size == (10, 10)
    assert fake.calls == [("docs/hero.png", "ko", True)]
    create.assert_called_once_with(
        root_dir="docs",
    )


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


def test_rewrite_notebook_paths_uses_target_path(tmp_path):
    root_dir = tmp_path
    source_path = root_dir / "docs" / "tutorial.ipynb"
    target_path = root_dir / "out" / "ko" / "docs" / "tutorial.ipynb"
    image_path = root_dir / "docs" / "images" / "hero.png"

    source_path.parent.mkdir(parents=True)
    image_path.parent.mkdir(parents=True)
    image_path.write_text("image", encoding="utf-8")

    content = json.dumps(
        {
            "cells": [
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": ["# Tutorial\n", "![Hero](images/hero.png)\n"],
                }
            ],
            "metadata": {},
            "nbformat": 4,
            "nbformat_minor": 5,
        }
    )

    rewritten = api.rewrite_notebook_paths(
        content,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ko",
            "root_dir": root_dir,
            "translations_dir": root_dir / "out",
            "translated_images_dir": root_dir / "translated_images",
            "translation_types": ["markdown", "notebook", "images"],
        },
    )

    cell_source = "".join(json.loads(rewritten)["cells"][0]["source"])
    assert "images/hero.png" not in cell_source
    assert "../../../translated_images/ko/hero." in cell_source
    assert cell_source.endswith(".webp)\n")
