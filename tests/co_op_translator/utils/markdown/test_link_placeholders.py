import pytest

from co_op_translator.utils.markdown.link_placeholders import (
    markdown_link_destinations,
    replace_markdown_link_destinations,
    restore_markdown_link_destinations,
)


def test_link_destination_placeholders_round_trip_markdown_exactly():
    document = (
        '[Lesson](https://example.com/course?WT.mc_id=test "Course details")\n'
        "![Diagram](<images/architecture diagram.png>)\n"
        "[Guide](../guides/setup_(advanced).md)\n"
        "[Overview](#overview)\n"
    )

    protected, placeholder_map = replace_markdown_link_destinations(document)

    assert "https://example.com/course?WT.mc_id=test" not in protected
    assert "images/architecture diagram.png" not in protected
    assert "../guides/setup_(advanced).md" not in protected
    assert '"Course details"' in protected
    assert "#overview" not in protected
    assert list(placeholder_map.values()) == [
        "https://example.com/course?WT.mc_id=test",
        "images/architecture diagram.png",
        "../guides/setup_(advanced).md",
        "#overview",
    ]
    assert restore_markdown_link_destinations(protected, placeholder_map) == document


def test_link_destination_placeholders_ignore_escaped_link_syntax_but_protect_url():
    document = r"\[not a link](https://example.com/leave-visible)"

    protected, placeholder_map = replace_markdown_link_destinations(document)

    assert protected == r"\[not a link](@@LINK_DESTINATION_0@@)"
    assert placeholder_map == {
        "@@LINK_DESTINATION_0@@": "https://example.com/leave-visible"
    }
    assert restore_markdown_link_destinations(protected, placeholder_map) == document


def test_link_destination_placeholders_preserve_nested_image_links():
    document = "[![Thumbnail](images/thumb.png)](https://example.com/watch)"

    protected, placeholder_map = replace_markdown_link_destinations(document)

    assert protected == (
        "[![Thumbnail](@@LINK_DESTINATION_0@@)](@@LINK_DESTINATION_1@@)"
    )
    assert list(placeholder_map.values()) == [
        "images/thumb.png",
        "https://example.com/watch",
    ]
    assert restore_markdown_link_destinations(protected, placeholder_map) == document


def test_link_destination_placeholders_protect_reference_definitions():
    document = (
        "[Full][guide], [Collapsed][], and [Shortcut].\n\n"
        '[guide]: https://example.com/guide?WT.mc_id=full "Guide"\n'
        "[Collapsed]: <../docs/collapsed guide.md?WT.mc_id=collapsed#top>\n"
        "[Shortcut]: ../docs/shortcut_(advanced).md\n"
    )

    protected, placeholder_map = replace_markdown_link_destinations(document)

    assert list(placeholder_map.values()) == [
        "https://example.com/guide?WT.mc_id=full",
        "../docs/collapsed guide.md?WT.mc_id=collapsed#top",
        "../docs/shortcut_(advanced).md",
    ]
    assert restore_markdown_link_destinations(protected, placeholder_map) == document


def test_link_destination_placeholders_protect_autolinks_and_html_attributes():
    document = (
        "<https://example.com/docs?WT.mc_id=auto>\n"
        '<a href="https://example.com/html?WT.mc_id=href">Docs</a>\n'
        "<img alt='Diagram' src='../images/diagram.png?WT.mc_id=src#preview'>\n"
    )

    protected, placeholder_map = replace_markdown_link_destinations(document)

    assert list(placeholder_map.values()) == [
        "https://example.com/docs?WT.mc_id=auto",
        "https://example.com/html?WT.mc_id=href",
        "../images/diagram.png?WT.mc_id=src#preview",
    ]
    assert restore_markdown_link_destinations(protected, placeholder_map) == document


def test_html_attributes_are_protected_while_visible_prose_remains_translatable():
    document = (
        "<p>Install <strong>the tool</strong> from "
        '<a href="https://example.com/guide">the guide</a>.</p>'
    )

    protected, placeholder_map = replace_markdown_link_destinations(document)

    assert protected == (
        "<p>Install <strong>the tool</strong> from "
        '<a href="@@LINK_DESTINATION_0@@">the guide</a>.</p>'
    )
    assert placeholder_map == {"@@LINK_DESTINATION_0@@": "https://example.com/guide"}
    assert restore_markdown_link_destinations(protected, placeholder_map) == document


def test_link_destination_placeholders_protect_anchors_and_bare_urls():
    document = (
        "[Section](#section)\n"
        "[Reference][section]\n\n"
        "[section]: #section\n"
        "Bare: https://example.com/docs?WT.mc_id=bare.\n"
    )

    protected, placeholder_map = replace_markdown_link_destinations(document)

    assert protected == (
        "[Section](@@LINK_DESTINATION_0@@)\n"
        "[Reference][section]\n\n"
        "[section]: @@LINK_DESTINATION_1@@\n"
        "Bare: @@LINK_DESTINATION_2@@.\n"
    )
    assert list(placeholder_map.values()) == [
        "#section",
        "#section",
        "https://example.com/docs?WT.mc_id=bare",
    ]
    assert restore_markdown_link_destinations(protected, placeholder_map) == document


def test_bare_url_placeholders_keep_balanced_parentheses_and_ignore_code():
    document = (
        "See https://example.com/reference_(v2)).\n"
        "`https://example.com/inline`\n"
        "```text\nhttps://example.com/fenced\n```\n"
    )

    protected, placeholder_map = replace_markdown_link_destinations(document)

    assert list(placeholder_map.values()) == ["https://example.com/reference_(v2)"]
    assert "`https://example.com/inline`" in protected
    assert "https://example.com/fenced" in protected
    assert restore_markdown_link_destinations(protected, placeholder_map) == document


@pytest.mark.parametrize(
    "translated",
    [
        "[Docs](@@LINK-DESTINATION-0@@)",
        "[Docs]()",
        "[Docs](@@LINK_DESTINATION_0@@@@LINK_DESTINATION_0@@)",
    ],
)
def test_restore_link_destinations_rejects_changed_missing_or_duplicate_placeholders(
    translated,
):
    placeholder_map = {"@@LINK_DESTINATION_0@@": "https://example.com"}

    with pytest.raises(ValueError, match="exactly once"):
        restore_markdown_link_destinations(translated, placeholder_map)


def test_link_parser_ignores_markdown_like_syntax_inside_code():
    document = """Real [guide](guide.md) and `inline [fake](inline.md)`.

```shell
echo '[fake](fenced.md)'
```

    [fake](indented.md)
"""

    assert [item.destination for item in markdown_link_destinations(document)] == [
        "guide.md"
    ]
