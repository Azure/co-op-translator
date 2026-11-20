import pytest
from markdown_it import MarkdownIt

from co_op_translator.utils.markdown.spans import (
    mask_markdown_code,
    replace_markdown_code,
    restore_markdown_code,
)


@pytest.mark.parametrize(
    "document",
    [
        r"Path `C:\folder\`. Translate this sentence. Next `SETTING`.",
        r"Path `C:\folder\\`. Translate this sentence. Next `SETTING`.",
        r"Escaped opening \`not code` followed by `real`.",
        r"Use ``a`b\`` and translate prose.",
        r"Use `a\` ordinary text `b`.",
        "Use `x` and `y`.",
        "Use `unmatched opening.",
        "```text\n`C:\\folder\\` literal\n```\nTranslate this.",
        "    `C:\\folder\\` literal\n\nTranslate this.",
    ],
)
def test_code_spans_agree_with_commonmark_and_roundtrip(document):
    protected, placeholders = replace_markdown_code(document)

    assert restore_markdown_code(protected, placeholders) == document

    expected = [
        child.content
        for token in MarkdownIt("commonmark").parse(document)
        for child in (token.children or [])
        if child.type == "code_inline"
    ]
    actual = []
    for marker, literal in placeholders.items():
        if not marker.startswith("@@INLINE_CODE_"):
            continue
        marker_width = len(literal) - len(literal.lstrip("`"))
        content = literal[marker_width:-marker_width].replace("\n", " ")
        if content.startswith(" ") and content.endswith(" ") and content.strip(" "):
            content = content[1:-1]
        actual.append(content)

    assert actual == expected


def test_windows_path_does_not_protect_following_prose():
    document = (
        r"Store files in `C:\queue\`. Все агенты видят эту очередь. "
        r"Use `QUEUE_DIR`. Файл `memory.md` не используется."
    )

    protected, placeholders = replace_markdown_code(document)

    assert list(placeholders.values()) == [
        r"`C:\queue\`",
        "`QUEUE_DIR`",
        "`memory.md`",
    ]
    for prose in ("Все агенты видят эту очередь.", "Файл", "не используется."):
        assert prose in protected
        assert prose in mask_markdown_code(document)
    assert restore_markdown_code(protected, placeholders) == document
