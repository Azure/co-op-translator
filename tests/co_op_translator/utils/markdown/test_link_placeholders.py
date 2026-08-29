import pytest

from co_op_translator.utils.markdown.link_placeholders import (
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
    assert "[Overview](#overview)" in protected
    assert list(placeholder_map.values()) == [
        "https://example.com/course?WT.mc_id=test",
        "images/architecture diagram.png",
        "../guides/setup_(advanced).md",
    ]
    assert restore_markdown_link_destinations(protected, placeholder_map) == document


def test_link_destination_placeholders_ignore_escaped_link_syntax():
    document = r"\[not a link](https://example.com/leave-visible)"

    protected, placeholder_map = replace_markdown_link_destinations(document)

    assert protected == document
    assert placeholder_map == {}


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


def test_link_destination_placeholders_leave_anchors_and_bare_urls_visible():
    document = (
        "[Section](#section)\n"
        "[Reference][section]\n\n"
        "[section]: #section\n"
        "Bare: https://example.com/docs?WT.mc_id=bare\n"
    )

    protected, placeholder_map = replace_markdown_link_destinations(document)

    assert protected == document
    assert placeholder_map == {}


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
