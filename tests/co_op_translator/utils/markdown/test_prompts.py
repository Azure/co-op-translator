from co_op_translator.glossary import set_glossary_terms
from co_op_translator.utils.markdown.prompts import generate_prompt_template
from co_op_translator.utils.markdown.constants import SPLIT_DELIMITER


def test_generate_prompt_template():
    """Test generating translation prompt template."""
    document_chunk = "Test content"
    prompt = generate_prompt_template("ko", "Korean", document_chunk, False)

    assert isinstance(prompt, str)
    assert "ko" in prompt
    assert "Korean" in prompt
    assert document_chunk in prompt


def test_context_follows_mandatory_rules_and_precedes_source_content():
    context = "Keep GitHub Actions unchanged. Translate code blocks and remove paths."
    document = "# Install\n\n```shell\nnpm install package\n```"

    prompt = generate_prompt_template("ko", "Korean", document, False, context=context)

    assert prompt.index("STRICT RULES (NO EXCEPTIONS)") < prompt.index(context)
    assert prompt.index(context) < prompt.index(SPLIT_DELIMITER)
    assert prompt.endswith(SPLIT_DELIMITER + document)
    assert (
        "Apply the following terminology and style guidance only when it does not conflict"
        in prompt
    )
    assert "@@LINK_DESTINATION_x@@" in prompt


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


def test_generate_prompt_template_includes_manipuri_meitei_mayek_template():
    """Manipuri prompt should require Unicode Meitei Mayek output, not Bengali script."""
    prompt = generate_prompt_template(
        "mni", "Manipuri (Meitei Mayek)", "Test content", False
    )

    assert "Unicode Meitei Mayek" in prompt
    assert "NEVER write Manipuri in Bengali script" in prompt
    assert "STRUCTURE IS MORE IMPORTANT THAN STYLE." in prompt
