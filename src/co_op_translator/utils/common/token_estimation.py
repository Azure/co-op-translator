from pathlib import Path
from typing import Any, Literal
import logging

import tiktoken

from co_op_translator.config.constants import SUPPORTED_MARKDOWN_EXTENSIONS
from co_op_translator.config.llm_config.azure_openai import AzureOpenAIConfig
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.config.llm_config.openai import OpenAIConfig
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.utils.common.file_utils import (
    filter_files,
    generate_translated_filename,
    get_filename_and_extension,
    read_input_file,
)

logger = logging.getLogger(__name__)


def _resolve_model_name() -> str | None:
    """Resolve the best-effort model name for tokenizer selection."""
    try:
        provider = LLMConfig.get_available_provider()
        if provider == LLMProvider.AZURE_OPENAI:
            return AzureOpenAIConfig.get_model_name() or None
        if provider == LLMProvider.OPENAI:
            return OpenAIConfig.get_chat_model_id()
    except Exception:
        return None
    return None


def _get_encoding() -> tiktoken.Encoding | None:
    model = _resolve_model_name()
    try:
        if model:
            return tiktoken.encoding_for_model(model)
    except Exception:
        pass
    try:
        return tiktoken.get_encoding("cl100k_base")
    except Exception:
        return None


_ENCODING: tiktoken.Encoding | None = None


def count_tokens(text: str) -> int:
    """Return token count for the given text using best-effort encoding."""
    if not text:
        return 0

    global _ENCODING
    if _ENCODING is None:
        _ENCODING = _get_encoding()

    if _ENCODING is None:
        return max(1, len(text) // 4)

    try:
        return len(_ENCODING.encode(text))
    except Exception as e:
        logger.debug(f"Tokenization failed, falling back to heuristic: {e}")
        return max(1, len(text) // 4)


def _get_estimation_source_text(
    file_path: Path,
    virtual_file_contents: dict[Path, str] | None = None,
) -> str:
    if virtual_file_contents:
        try:
            resolved_path = file_path.resolve()
        except Exception:
            resolved_path = file_path
        if resolved_path in virtual_file_contents:
            return virtual_file_contents[resolved_path].strip()
    return read_input_file(file_path)


def estimate_tokens_for_sources(
    files: list[Path],
    virtual_file_contents: dict[Path, str] | None = None,
) -> int:
    total = 0
    for file_path in files:
        try:
            text = _get_estimation_source_text(
                file_path,
                virtual_file_contents=virtual_file_contents,
            )
            try:
                total += count_tokens(text)
            except Exception:
                total += len(text.split())
        except Exception:
            continue
    return total


def estimate_tokens_for_images(translation_manager: Any, update: bool) -> int:
    count = 0
    image_files = filter_files(
        translation_manager.root_dir,
        translation_manager.excluded_dirs,
    )
    for image_file_path in image_files:
        image_file_path = Path(image_file_path).resolve()
        _, ext = get_filename_and_extension(image_file_path)
        if ext not in translation_manager.supported_image_extensions:
            continue

        for language_code in translation_manager.language_codes:
            translated_filename = generate_translated_filename(
                image_file_path,
                language_code,
                translation_manager.root_dir,
            )
            translated_image_path = (
                Path(translation_manager.image_dir)
                / language_code
                / translated_filename
            )
            if not update and translated_image_path.exists():
                continue
            count += 1

    return count * 10


def _collect_outdated_translations(
    translation_manager: Any,
    update: bool,
) -> list[tuple[Path, Path]]:
    if not update:
        return list(translation_manager.get_outdated_translations())

    files: list[tuple[Path, Path]] = []
    for lang_code in translation_manager.language_codes:
        translation_dir = translation_manager._get_language_root(lang_code)
        if not translation_dir.exists():
            continue

        trans_files: list[Path] = []
        for ext in SUPPORTED_MARKDOWN_EXTENSIONS:
            trans_files.extend(translation_dir.rglob(f"*{ext}"))
        for ext in translation_manager.supported_notebook_extensions:
            trans_files.extend(translation_dir.rglob(f"*{ext}"))

        for trans_file in trans_files:
            try:
                rel = trans_file.relative_to(translation_dir)
                original = translation_manager.root_dir / rel
                if original.exists():
                    files.append((original, trans_file))
            except Exception:
                continue

    return files


def estimate_tokens_for_outdated(
    translation_manager: Any,
    outdated_files: list[tuple[Path, Path]],
    content_type: Literal["markdown", "notebook"],
    virtual_file_contents: dict[Path, str] | None = None,
) -> int:
    if content_type == "markdown":
        allowed_extensions = SUPPORTED_MARKDOWN_EXTENSIONS
    else:
        allowed_extensions = translation_manager.supported_notebook_extensions

    sources = [
        original
        for original, _ in outdated_files
        if original.suffix.lower() in allowed_extensions
    ]
    return estimate_tokens_for_sources(
        sources,
        virtual_file_contents=virtual_file_contents,
    )


def estimate_tokens_for_outdated_images(
    translation_manager: Any,
    outdated_images: list[tuple[Path, Path, str]] | None = None,
) -> int:
    try:
        images = (
            outdated_images
            if outdated_images is not None
            else translation_manager.get_outdated_images()
        )
        return len(images) * 10
    except Exception:
        return 0


def estimate_translation_tokens(
    translation_manager: Any,
    update: bool = False,
    virtual_file_contents: dict[Path, str] | None = None,
) -> dict[str, int]:
    """Return token estimate breakdown from translation manager state."""
    breakdown = {
        "outdated_markdown": 0,
        "outdated_notebook": 0,
        "outdated_images": 0,
        "markdown": 0,
        "notebook": 0,
        "images": 0,
    }

    if ("markdown" in translation_manager.translation_types) or (
        "notebook" in translation_manager.translation_types
    ):
        outdated = _collect_outdated_translations(translation_manager, update)
        if outdated:
            breakdown["outdated_markdown"] = estimate_tokens_for_outdated(
                translation_manager,
                outdated,
                "markdown",
                virtual_file_contents=virtual_file_contents,
            )
            breakdown["outdated_notebook"] = estimate_tokens_for_outdated(
                translation_manager,
                outdated,
                "notebook",
                virtual_file_contents=virtual_file_contents,
            )

    if "images" in translation_manager.translation_types:
        breakdown["outdated_images"] = estimate_tokens_for_outdated_images(
            translation_manager,
        )

    if "markdown" in translation_manager.translation_types:
        markdown_pending = translation_manager._gather_pending_markdown(update=update)
        if markdown_pending:
            breakdown["markdown"] = estimate_tokens_for_sources(
                markdown_pending,
                virtual_file_contents=virtual_file_contents,
            )

    if "notebook" in translation_manager.translation_types:
        notebook_pending = translation_manager._gather_pending_notebooks(update=update)
        if notebook_pending:
            breakdown["notebook"] = estimate_tokens_for_sources(
                notebook_pending,
                virtual_file_contents=virtual_file_contents,
            )

    if "images" in translation_manager.translation_types:
        try:
            breakdown["images"] = estimate_tokens_for_images(
                translation_manager,
                update=update,
            )
        except Exception:
            breakdown["images"] = 0

    outdated_total = (
        breakdown["outdated_markdown"]
        + breakdown["outdated_notebook"]
        + breakdown["outdated_images"]
    )
    total = sum(breakdown.values())
    return {**breakdown, "outdated": outdated_total, "total": total}
