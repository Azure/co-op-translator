from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence

from co_op_translator.utils.markdown.frontmatter import (
    adjust_frontmatter_links,
    get_frontmatter_parser,
)
from co_op_translator.utils.markdown.links import update_links


@dataclass(frozen=True)
class MarkdownPathRewritePolicy:
    """Configuration for rewriting project-relative paths in translated markdown."""

    language_code: str
    root_dir: str | Path = "."
    translations_dir: str | Path | None = None
    translated_images_dir: str | Path | None = None
    translation_types: Sequence[str] | None = None
    lang_subdir: str | Path | None = None


def _resolve_under_root(path: str | Path | None, root_dir: Path, default: str) -> Path:
    if path is None:
        return root_dir / default

    candidate = Path(path)
    if candidate.is_absolute():
        return candidate.resolve()
    return (root_dir / candidate).resolve()


def _coerce_rewrite_policy(
    policy: MarkdownPathRewritePolicy | Mapping[str, object],
) -> MarkdownPathRewritePolicy:
    if isinstance(policy, MarkdownPathRewritePolicy):
        return policy

    values = dict(policy)
    if "image_dir" in values and "translated_images_dir" not in values:
        values["translated_images_dir"] = values.pop("image_dir")
    return MarkdownPathRewritePolicy(**values)


def rewrite_markdown_paths(
    content: str,
    source_path: str | Path,
    target_path: str | Path,
    policy: MarkdownPathRewritePolicy | Mapping[str, object],
) -> str:
    """Rewrite markdown/frontmatter paths for a translated document target.

    This function performs no translation and no file I/O. It only adjusts links
    according to the source document location, target document location, and
    project layout policy.
    """

    rewrite_policy = _coerce_rewrite_policy(policy)

    root_dir = Path(rewrite_policy.root_dir).resolve()
    source = Path(source_path).resolve()
    target = Path(target_path).resolve()
    translations_dir = _resolve_under_root(
        rewrite_policy.translations_dir, root_dir, "translations"
    )
    translated_images_dir = _resolve_under_root(
        rewrite_policy.translated_images_dir, root_dir, "translated_images"
    )
    translation_types = list(
        rewrite_policy.translation_types or ["markdown", "notebook", "images"]
    )
    lang_subdir = (
        Path(rewrite_policy.lang_subdir) if rewrite_policy.lang_subdir else None
    )

    parser = get_frontmatter_parser()
    frontmatter, body = parser.extract_frontmatter(content)
    if frontmatter:
        adjusted_frontmatter = adjust_frontmatter_links(
            frontmatter,
            source,
            rewrite_policy.language_code,
            root_dir,
            translations_dir,
            translated_images_dir,
            translation_types,
            lang_subdir=lang_subdir,
            target_path=target,
        )
        content = parser.reconstruct_content(adjusted_frontmatter, body)

    return update_links(
        source,
        content,
        rewrite_policy.language_code,
        root_dir,
        translations_dir=translations_dir,
        translated_images_dir=translated_images_dir,
        translation_types=translation_types,
        target_path=target,
    )


__all__ = ["MarkdownPathRewritePolicy", "rewrite_markdown_paths"]
