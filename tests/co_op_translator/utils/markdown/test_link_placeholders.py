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
