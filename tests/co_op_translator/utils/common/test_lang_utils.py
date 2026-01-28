import pytest

from co_op_translator.utils.common.lang_utils import (
    normalize_language_code,
    normalize_language_codes,
    ALIAS_TO_BCP47,
)


def test_normalize_language_code_aliases():
    assert normalize_language_code("tw") == "zh-TW"
    assert normalize_language_code("cn") == "zh-CN"
    assert normalize_language_code("br") == "pt-BR"
    assert normalize_language_code("jp") == "ja"
    assert normalize_language_code("kr") == "ko"
    # generic zh maps to zh-CN per policy
    assert normalize_language_code("zh") == "zh-CN"


def test_normalize_language_code_casing():
    assert normalize_language_code("pt-br") == "pt-BR"
    assert normalize_language_code("PT-br") == "pt-BR"
    assert normalize_language_code("zh-tw") == "zh-TW"
    assert normalize_language_code("EN-us") == "en-US"
    assert normalize_language_code("ja") == "ja"


def test_normalize_language_codes_dedup_order():
    items = ["tw", "zh-TW", "cn", "ZH-cn", "br", "pt-br", "jp", "kr"]
    # Expect deduped canonical order of first occurrences
    out = normalize_language_codes(items)
    assert out == ["zh-TW", "zh-CN", "pt-BR", "ja", "ko"]


def test_alias_table_contains_expected():
    # minimal sanity of important aliases
    for k in ["tw", "cn", "br", "jp", "kr", "zh"]:
        assert k in ALIAS_TO_BCP47
