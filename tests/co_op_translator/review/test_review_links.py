from pathlib import Path

from co_op_translator.review.checks.links import check_local_links
from co_op_translator.review.targets import ReviewTarget


def test_review_ignores_link_like_syntax_inside_code(tmp_path):
    source = tmp_path / "guide.md"
    source.write_text("# Guide\n", encoding="utf-8")
    translated = tmp_path / "translations" / "ko" / "guide.md"
    translated.parent.mkdir(parents=True)
    translated.write_text(
        "`[Inline](missing-inline.md)`\n\n"
        "```shell\necho '[Fenced](missing-fenced.md)'\n```\n"
        "[Real](missing.md)\n",
        encoding="utf-8",
    )
    target = ReviewTarget(tmp_path, tmp_path / "translations")

    issues = check_local_links(target, [source], ["ko"])

    assert len(issues) == 1
    assert issues[0].message == "Local target does not exist: missing.md"
    assert issues[0].path == Path("ko/guide.md")
