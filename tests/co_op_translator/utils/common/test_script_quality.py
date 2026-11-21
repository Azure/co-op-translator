import pytest

from co_op_translator.utils.common.script_quality import (
    REASON_FORBIDDEN_SCRIPT,
    REASON_INSUFFICIENT_REQUIRED,
    ScriptQualityPolicy,
    check_script_quality,
    evaluate_script_quality,
    get_script_quality_policy,
    load_script_quality_policies,
    parse_block_range,
    parse_script_quality_policy,
    strip_non_prose,
)

MEITEI_MAYEK = ScriptQualityPolicy(
    required_ranges=((0xABC0, 0xABFF), (0xAAE0, 0xAAFF)),
    forbidden_ranges=((0x0980, 0x09FF),),
)

# "Co-op Translator automates translation of Markdown files" in Meitei Mayek.
MEITEI_SENTENCE = (
    "Co-op Translator ꯅꯥ Markdown ꯐꯥꯏꯜ ꯑꯃꯁꯨꯡ ꯐꯣꯇꯣꯁꯤꯡ ꯑꯁꯤ ꯂꯣꯜꯇꯥꯡ ꯀꯌꯥ ꯗ "
    "ꯑꯣꯇꯣꯃꯦꯇꯤꯛ ꯑꯣꯏꯅ ꯄꯥꯟꯗꯝ ꯄꯤꯔꯤ꯫ ꯃꯁꯤꯅ ꯐꯣꯔꯃꯦꯇꯤꯡ, ꯂꯤꯡꯛꯁ ꯑꯃꯁꯨꯡ ꯀꯣꯗ "
    "ꯕ꯭ꯂꯣꯛꯁꯤꯡ ꯐꯛꯅꯔꯛꯅ ꯊꯝꯅ ꯄꯥꯟꯗꯝ ꯁꯦꯝꯗꯣꯛꯅꯕ ꯄꯨꯅꯁꯤꯅꯕꯗ Azure AI services ꯁꯤꯖꯤꯟꯅꯩ꯫"
)
ENGLISH_SENTENCE = (
    "Co-op Translator automates the translation of Markdown files and images "
    "into many languages while preserving formatting, links and code blocks."
)
ROMANIZED_SENTENCE = (
    "Co-op Translator na Markdown file amasung photo-sing asi loltang kaya da "
    "automatic oina pandam piri. Masina formatting, links amasung code block "
    "sing phaknarakna thamna pandam semdoknaba punsinnabada Azure AI sijinnei."
)
BENGALI_SCRIPT_SENTENCE = (
    "কো-অপ ট্রান্সলেটর না মার্কডাউন ফাইল অমসুং ফোটোশিং অসি লোলতাং কয়া দা "
    "অটোমেটিক ওইনা পান্দম পিরি। মসিনা ফরমেটিং, লিংকস অমসুং কোদ ব্লকশিং ফকনরকনা।"
)


def test_parse_block_range_accepts_plain_and_u_plus_forms():
    assert parse_block_range("ABC0-ABFF") == (0xABC0, 0xABFF)
    assert parse_block_range("U+AAE0-U+AAFF") == (0xAAE0, 0xAAFF)


@pytest.mark.parametrize("value", ["ABFF-ABC0", "ABC0", "not a range", ""])
def test_parse_block_range_rejects_invalid_values(value):
    with pytest.raises(ValueError):
        parse_block_range(value)


def test_parse_policy_uses_defaults_and_requires_required_blocks():
    policy = parse_script_quality_policy({"required_blocks": ["ABC0-ABFF"]})
    assert policy == ScriptQualityPolicy(required_ranges=((0xABC0, 0xABFF),))
    assert parse_script_quality_policy(None) is None
    assert parse_script_quality_policy({}) is None
    with pytest.raises(ValueError):
        parse_script_quality_policy({"forbidden_blocks": ["0980-09FF"]})
    with pytest.raises(ValueError):
        parse_script_quality_policy(
            {"required_blocks": ["ABC0-ABFF"], "min_required_share": 1.5}
        )


def test_strip_non_prose_removes_code_links_placeholders_and_tags():
    text = (
        "---\ntitle: Hello\n---\n"
        "# ꯈꯦꯗꯥꯠ\n\n"
        "Install with `pip install co-op-translator` and see "
        "[docs](https://example.com/getting-started) or https://example.com.\n"
        "@@CODE_BLOCK_0@@ @@LINE_0003@@ <details><summary>More</summary></details>\n"
        "```python\nprint('hello world')\n```\n&nbsp;"
    )
    stripped = strip_non_prose(text)
    assert "pip install" not in stripped
    assert "example.com" not in stripped
    assert "getting-started" not in stripped
    assert "CODE_BLOCK" not in stripped
    assert "LINE_0003" not in stripped
    assert "summary" not in stripped
    assert "print" not in stripped
    assert "nbsp" not in stripped
    assert "title" not in stripped
    assert "docs" in stripped  # link text is prose and is kept
    assert "ꯈꯦꯗꯥꯠ" in stripped


MEITEI_PROSE_LINE = "ꯃꯅꯤꯄꯨꯔꯤ ꯂꯣꯟ ꯃꯅꯤꯄꯨꯔꯤ ꯂꯣꯟ ꯃꯅꯤꯄꯨꯔꯤ ꯂꯣꯟ ꯃꯅꯤꯄꯨꯔꯤ ꯂꯣꯟ꯫\n"
LONG_LATIN_IDENTIFIER = "VeryLongUntranslatedEnglishIdentifierForThisExperiment"


@pytest.mark.parametrize(
    "code",
    [
        pytest.param(
            f"``{LONG_LATIN_IDENTIFIER} `x` ``\n", id="double-backtick-inline"
        ),
        pytest.param(
            f"```{LONG_LATIN_IDENTIFIER} `x` ```\n", id="triple-backtick-inline"
        ),
        pytest.param(f"    {LONG_LATIN_IDENTIFIER}\n", id="indented-code-block"),
        pytest.param(f"~~~\n{LONG_LATIN_IDENTIFIER}\n~~~\n", id="tilde-fence"),
        pytest.param(f"```python\n{LONG_LATIN_IDENTIFIER}\n```\n", id="backtick-fence"),
    ],
)
def test_score_is_unchanged_by_code_spans(code):
    """Code in any CommonMark form must not count as prose (regression)."""
    # The blank line matters: without it an indented line is a lazy paragraph
    # continuation in CommonMark, not a code block.
    text = MEITEI_PROSE_LINE + "\n" + code
    without_code = evaluate_script_quality(MEITEI_PROSE_LINE, MEITEI_MAYEK)
    with_code = evaluate_script_quality(text, MEITEI_MAYEK)

    assert without_code.ok and with_code.ok
    assert with_code.letters == without_code.letters == 40
    assert with_code.required_share == without_code.required_share == 1.0
    assert LONG_LATIN_IDENTIFIER not in strip_non_prose(text)


def test_unclosed_backtick_is_literal_text_and_still_counted():
    """CommonMark treats an unmatched backtick as text, so it stays prose."""
    text = MEITEI_PROSE_LINE + f"`{LONG_LATIN_IDENTIFIER}\n"
    assert LONG_LATIN_IDENTIFIER in strip_non_prose(text)
    assert not evaluate_script_quality(text, MEITEI_MAYEK).ok


def test_valid_meitei_mayek_passes_even_with_latin_product_names():
    result = evaluate_script_quality(MEITEI_SENTENCE, MEITEI_MAYEK)
    assert result.ok
    assert result.reason is None
    assert result.required_share > 0.6
    assert result.forbidden_share == 0


def test_untranslated_english_fails():
    result = evaluate_script_quality(ENGLISH_SENTENCE, MEITEI_MAYEK)
    assert not result.ok
    assert result.reason == REASON_INSUFFICIENT_REQUIRED
    assert result.required_share == 0


def test_latin_transliteration_fails():
    result = evaluate_script_quality(ROMANIZED_SENTENCE, MEITEI_MAYEK)
    assert not result.ok
    assert result.reason == REASON_INSUFFICIENT_REQUIRED


def test_bengali_script_manipuri_fails_as_forbidden():
    result = evaluate_script_quality(BENGALI_SCRIPT_SENTENCE, MEITEI_MAYEK)
    assert not result.ok
    assert result.reason == REASON_FORBIDDEN_SCRIPT
    assert result.forbidden_share > 0.9


def test_short_prose_is_not_judged():
    # A heading made only of product names has too few letters to judge.
    result = evaluate_script_quality("## Azure OpenAI", MEITEI_MAYEK)
    assert result.ok
    assert result.letters < MEITEI_MAYEK.min_letters


def test_code_heavy_chunk_is_judged_on_prose_only():
    text = (
        "```python\n"
        "def translate(markdown: str) -> str:\n    return markdown\n"
        "```\n\n"
        f"{MEITEI_SENTENCE}\n"
    )
    assert evaluate_script_quality(text, MEITEI_MAYEK).ok


def test_result_metadata_and_description():
    failed = evaluate_script_quality(ENGLISH_SENTENCE, MEITEI_MAYEK)
    assert failed.metadata()["reason"] == REASON_INSUFFICIENT_REQUIRED
    assert "0%" in failed.describe()
    passed = evaluate_script_quality(MEITEI_SENTENCE, MEITEI_MAYEK)
    assert "reason" not in passed.metadata()
    assert passed.describe() == "script quality check passed"


def test_manipuri_policy_is_loaded_from_font_mappings():
    policies = load_script_quality_policies()
    assert "mni" in policies
    policy = policies["mni"]
    assert (0xABC0, 0xABFF) in policy.required_ranges
    assert (0xAAE0, 0xAAFF) in policy.required_ranges
    assert (0x0980, 0x09FF) in policy.forbidden_ranges
    assert get_script_quality_policy("MNI") == policy


def test_languages_without_policy_are_not_checked():
    assert get_script_quality_policy("ko") is None
    assert check_script_quality(ENGLISH_SENTENCE, "ko") is None
    assert check_script_quality(ENGLISH_SENTENCE, "mni").ok is False
    assert check_script_quality(MEITEI_SENTENCE, "mni").ok is True
