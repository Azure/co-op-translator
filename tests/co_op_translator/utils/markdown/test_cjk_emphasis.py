from co_op_translator.utils.markdown.cjk_emphasis import normalize_cjk_emphasis_markers


def test_normalize_cjk_emphasis_markers_for_italic_and_bold():
    """CJK-adjacent emphasis markers should be normalized to HTML tags."""
    content = "これは*重要*です。これは**太字**です。"

    normalized = normalize_cjk_emphasis_markers(content)

    assert "これは<em>重要</em>です" in normalized
    assert "これは<strong>太字</strong>です" in normalized


def test_normalize_cjk_emphasis_markers_keeps_non_cjk_markdown_emphasis():
    """Non-CJK emphasis formatting should remain unchanged."""
    content = "This is *important* and **bold** text."

    normalized = normalize_cjk_emphasis_markers(content)

    assert normalized == content


def test_normalize_cjk_emphasis_markers_skips_non_cjk_target_language():
    """Normalization should not run when target language is not CJK."""
    content = "これは*重要*です。これは**太字**です。"

    normalized = normalize_cjk_emphasis_markers(content, language_code="fr")

    assert normalized == content


def test_normalize_cjk_emphasis_markers_runs_for_zh_regional_codes():
    """Normalization should run for regional Chinese codes (e.g., zh-TW)."""
    content = "這是*重點*。"

    normalized = normalize_cjk_emphasis_markers(content, language_code="zh-TW")

    assert "這是<em>重點</em>。" == normalized


def test_normalize_cjk_emphasis_markers_converts_bold_italic_triple_asterisk():
    """Triple-asterisk emphasis should convert to combined strong+em tags."""
    content = "これは***重要***です。"

    normalized = normalize_cjk_emphasis_markers(content, language_code="ja")

    assert "これは<strong><em>重要</em></strong>です。" == normalized


def test_normalize_cjk_emphasis_markers_converts_one_sided_bold_italic_boundaries():
    """Triple-asterisk emphasis should normalize with one-sided CJK boundaries."""
    content = "Start ***重要*** and これは***Configure*** end。"

    normalized = normalize_cjk_emphasis_markers(content, language_code="ja")

    assert "<strong><em>重要</em></strong>" in normalized
    assert "これは<strong><em>Configure</em></strong>" in normalized


def test_normalize_cjk_emphasis_markers_converts_one_sided_cjk_boundaries():
    """Emphasis should normalize when either left or right boundary is CJK."""
    content = "Start **太字** and *強調*です。次にこれは**Bold** end。"

    normalized = normalize_cjk_emphasis_markers(content, language_code="ja")

    assert "<strong>太字</strong>" in normalized
    assert "<em>強調</em>です" in normalized
    assert "これは<strong>Bold</strong>" in normalized


def test_normalize_cjk_emphasis_markers_does_not_convert_underscore_patterns():
    """Underscore-delimited fragments should remain unchanged to avoid identifier mutations."""
    content = "変数_name_を確認します。"

    normalized = normalize_cjk_emphasis_markers(content, language_code="ja")

    assert normalized == content


def test_normalize_cjk_emphasis_markers_skips_inline_code_spans():
    """Inline code spans should not be rewritten by emphasis normalization."""
    content = "説明 `漢*字*語` と本文の漢*字*語"

    normalized = normalize_cjk_emphasis_markers(content, language_code="ja")

    assert "`漢*字*語`" in normalized
    assert "本文の漢<em>字</em>語" in normalized


def test_normalize_cjk_emphasis_markers_skips_multibacktick_inline_code_spans():
    """Inline code with multi-backtick delimiters should also be preserved."""
    content = "説明 ``漢`*字*`語`` と本文の漢*字*語"

    normalized = normalize_cjk_emphasis_markers(content, language_code="ja")

    assert "``漢`*字*`語``" in normalized
    assert "本文の漢<em>字</em>語" in normalized
