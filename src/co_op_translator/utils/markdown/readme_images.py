from __future__ import annotations

from pathlib import Path
from urllib.parse import unquote, urlparse

from markdown_it import MarkdownIt

from co_op_translator.config.constants import SUPPORTED_IMAGE_EXTENSIONS
from co_op_translator.utils.common.file_utils import get_actual_image_path
from co_op_translator.utils.markdown.link_placeholders import (
    markdown_image_destination_spans,
)


def discover_readme_images(readme_path: Path, root_dir: Path) -> set[Path]:
    """Return existing local raster images referenced by the root README."""

    readme_path = Path(readme_path).resolve()
    root_dir = Path(root_dir).resolve()
    if not readme_path.is_file():
        return set()

    document = readme_path.read_text(encoding="utf-8")
    destinations = {
        document[start:end] for start, end in markdown_image_destination_spans(document)
    }
    for token in MarkdownIt("commonmark").parse(document):
        for child in token.children or []:
            if child.type == "image":
                destination = child.attrGet("src")
                if destination:
                    destinations.add(destination)

    images: set[Path] = set()
    for destination in destinations:
        parsed = urlparse(destination)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        if Path(parsed.path).suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
            continue

        image_path = get_actual_image_path(
            unquote(parsed.path),
            readme_path,
            root_dir,
        ).resolve()
        try:
            image_path.relative_to(root_dir)
        except ValueError:
            continue
        if image_path.is_file():
            images.add(image_path)
    return images
