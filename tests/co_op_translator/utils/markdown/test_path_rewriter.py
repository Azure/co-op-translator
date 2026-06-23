def test_path_rewriter_requires_explicit_module_import():
    import co_op_translator.utils.markdown as markdown_utils
    from co_op_translator.utils.markdown.path_rewriter import (
        MarkdownPathRewritePolicy,
        rewrite_markdown_paths,
    )

    assert not hasattr(markdown_utils, "MarkdownPathRewritePolicy")
    assert not hasattr(markdown_utils, "rewrite_markdown_paths")
    assert MarkdownPathRewritePolicy is not None
    assert rewrite_markdown_paths is not None
