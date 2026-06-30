from pathlib import Path

import pytest

from co_op_translator.core.project.translation import request


def test_resolve_translation_types_defaults_to_all_types():
    assert request.resolve_translation_types() == ("markdown", "notebook", "images")


def test_resolve_translation_types_preserves_existing_explicit_order():
    assert request.resolve_translation_types(
        markdown=True,
        images=True,
        notebook=True,
    ) == ("markdown", "images", "notebook")


def test_build_translation_request_normalizes_language_codes(tmp_path):
    result = request.build_translation_request(
        language_codes="ko tw pt-br",
        root_dir=str(tmp_path),
        markdown=True,
    )

    assert result.language_codes == "ko zh-TW pt-BR"
    assert result.language_list == ("ko", "zh-TW", "pt-BR")
    assert result.translation_types == ("markdown",)
    assert result.root_path == Path(tmp_path).resolve()
    assert result.all_languages_selected is False


def test_build_translation_request_expands_all(monkeypatch, tmp_path):
    monkeypatch.setattr(
        request.Config,
        "get_language_codes",
        lambda: ["ko", "tw", "pt-br"],
    )

    result = request.build_translation_request(
        language_codes="all",
        root_dir=str(tmp_path),
    )

    assert result.language_codes == "ko zh-TW pt-BR"
    assert result.language_list == ("ko", "zh-TW", "pt-BR")
    assert result.translation_types == ("markdown", "notebook", "images")
    assert result.all_languages_selected is True


def test_build_translation_request_rejects_empty_language_codes(tmp_path):
    with pytest.raises(ValueError, match="No valid language codes provided"):
        request.build_translation_request(
            language_codes=" ",
            root_dir=str(tmp_path),
        )


def test_build_translation_request_rejects_empty_all_mapping(monkeypatch, tmp_path):
    monkeypatch.setattr(request.Config, "get_language_codes", lambda: [])

    with pytest.raises(ValueError, match="No valid language codes found"):
        request.build_translation_request(
            language_codes="all",
            root_dir=str(tmp_path),
        )
