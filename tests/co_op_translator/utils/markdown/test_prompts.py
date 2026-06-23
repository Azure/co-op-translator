from co_op_translator.glossary import set_glossary_terms
from co_op_translator.utils.markdown.prompts import generate_prompt_template


def test_generate_prompt_template():
    """Test generating translation prompt template."""
    document_chunk = "Test content"
    prompt = generate_prompt_template("ko", "Korean", document_chunk, False)

    assert isinstance(prompt, str)
    assert "ko" in prompt
    assert "Korean" in prompt
    assert document_chunk in prompt


def test_generate_prompt_template_includes_japanese_language_template():
    """Japanese prompt should include strict markdown-preservation template text."""
    document_chunk = "This document uses [Co-op Translator](https://github.com/Azure/co-op-translator)."

    prompt = generate_prompt_template("ja", "Japanese", document_chunk, False)

    assert "STRUCTURE IS MORE IMPORTANT THAN STYLE." in prompt
    assert "NEVER rewrite links as plain text" in prompt


def test_generate_prompt_template_without_language_template_for_non_configured_language():
    """Languages without a dedicated template should use the default prompt only."""
    prompt = generate_prompt_template("ko", "Korean", "Test content", False)

    assert "STRUCTURE IS MORE IMPORTANT THAN STYLE." not in prompt


def test_generate_prompt_template_includes_glossary_when_configured():
    try:
        set_glossary_terms(["Co-op Translator"])
        prompt = generate_prompt_template("ko", "Korean", "Test content", False)
        assert "GLOSSARY" in prompt
        assert "Co-op Translator" in prompt
    finally:
        set_glossary_terms([])
