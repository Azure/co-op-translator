import json
from pathlib import Path

from co_op_translator.utils.common.file_utils import (
    canonicalize_image_links_in_translations,
)


def write_text(p: Path, content: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def test_markdown_rewrites_aliases_for_multiple_bases(tmp_path: Path):
    translations_dir = tmp_path / "translations"
    image_dir = tmp_path / "images_out"  # custom base dir name

    # Create a markdown file under translations with multiple alias patterns
    md = translations_dir / "ko" / "docs" / "sample.md"
    original = (
        "![t1](translated_images/tw/foo.webp)\n"
        "![t2](translated_images_fast/cn/bar.webp)\n"
        f"![t3]({image_dir.name}/br/baz.webp)\n"
    )
    write_text(md, original)

    md_updated, nb_updated = canonicalize_image_links_in_translations(
        translations_dir=translations_dir, image_dir=image_dir
    )

    # One markdown file updated, no notebooks
    assert md_updated == 1
    assert nb_updated == 0

    updated = md.read_text(encoding="utf-8")
    assert "translated_images/zh-TW/foo.webp" in updated
    assert "translated_images_fast/zh-CN/bar.webp" in updated
    assert f"{image_dir.name}/pt-BR/baz.webp" in updated


def test_notebook_rewrites_aliases(tmp_path: Path):
    translations_dir = tmp_path / "translations"
    image_dir = tmp_path / "translated_images"  # common default base

    nb = translations_dir / "ja" / "nb" / "sample.ipynb"
    nb_content = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "![x](translated_images/cn/a.webp)\n",
                    "text before ",
                    "![y](translated_images_fast/br/b.webp)\n",
                ],
            }
        ],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    nb.parent.mkdir(parents=True, exist_ok=True)
    nb.write_text(json.dumps(nb_content), encoding="utf-8")

    md_updated, nb_updated = canonicalize_image_links_in_translations(
        translations_dir=translations_dir, image_dir=image_dir
    )

    assert md_updated == 0
    assert nb_updated == 1

    updated = nb.read_text(encoding="utf-8")
    assert "translated_images/zh-CN/a.webp" in updated
    assert "translated_images_fast/pt-BR/b.webp" in updated


def test_no_changes_returns_zero(tmp_path: Path):
    translations_dir = tmp_path / "translations"
    image_dir = tmp_path / "images_out"

    md = translations_dir / "fr" / "doc.md"
    write_text(md, "No image paths here.")

    md_updated, nb_updated = canonicalize_image_links_in_translations(
        translations_dir=translations_dir, image_dir=image_dir
    )

    assert (md_updated, nb_updated) == (0, 0)


def test_windows_separators_are_handled(tmp_path: Path):
    translations_dir = tmp_path / "translations"
    image_dir = tmp_path / "images_out"

    md = translations_dir / "de" / "doc.md"
    original = (
        "![t1](translated_images\\tw\\foo.webp)\n"
        "![t2](translated_images_fast\\br\\bar.webp)\n"
        f"![t3]({image_dir.name}\\cn\\baz.webp)\n"
    )
    write_text(md, original)

    md_updated, nb_updated = canonicalize_image_links_in_translations(
        translations_dir=translations_dir, image_dir=image_dir
    )

    assert md_updated == 1
    assert nb_updated == 0

    updated = md.read_text(encoding="utf-8")
    assert "translated_images\\zh-TW\\foo.webp" in updated
    assert "translated_images_fast\\pt-BR\\bar.webp" in updated
    assert f"{image_dir.name}\\zh-CN\\baz.webp" in updated
