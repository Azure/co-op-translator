from __future__ import annotations

import asyncio
import logging
import os
import re
from dataclasses import dataclass
from functools import partial
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse

from PIL import Image

from co_op_translator.config.readme_image_config import ReadmeImageConfig
from co_op_translator.config.constants import (
    SUPPORTED_MARKDOWN_EXTENSIONS,
    SUPPORTED_NOTEBOOK_EXTENSIONS,
)
from co_op_translator.core.llm.markdown_translator import MarkdownTranslator
from co_op_translator.core.image_generation import create_readme_image_translator
from co_op_translator.utils.common.file_utils import (
    generate_translated_filename,
    handle_empty_document,
    read_input_file,
)
from co_op_translator.utils.common.lang_utils import normalize_language_codes
from co_op_translator.utils.common.metadata_utils import (
    calculate_file_hash,
    is_image_up_to_date,
    read_text_metadata_for_source,
    save_image_metadata,
    save_text_metadata_for_source,
)
from co_op_translator.utils.common.token_estimation import count_tokens
from co_op_translator.utils.common.task_utils import (
    run_tasks_concurrently,
    validate_concurrency,
)
from co_op_translator.utils.markdown.path_rewriter import (
    MarkdownPathRewritePolicy,
    rewrite_markdown_paths,
)
from co_op_translator.utils.markdown.processing import compare_line_breaks
from co_op_translator.utils.markdown.readme_images import discover_readme_images
from co_op_translator.utils.vision.image_utils import save_optimized_image

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class ReadmeTranslationResult:
    """Result for one README translation target."""

    language_code: str
    source_path: Path
    translated_path: Path
    skipped: bool = False


class ReadmeTranslator:
    """Translate only the root README.md without running project-wide workflows."""

    def __init__(
        self,
        language_codes: str | Iterable[str],
        root_dir: str | Path = ".",
        *,
        translations_dir: str | Path | None = None,
        image_dir: str | Path | None = None,
        add_disclaimer: bool = True,
        lang_subdir: str | Path | None = None,
        markdown_translator=None,
        readme_image_translator=None,
        initialize_translator: bool = True,
        concurrency: int = 1,
        context: str | None = None,
    ):
        validate_concurrency(concurrency)
        self.concurrency = concurrency
        raw_language_codes = (
            language_codes.split()
            if isinstance(language_codes, str)
            else list(language_codes)
        )
        self.language_codes = normalize_language_codes(raw_language_codes)
        if not self.language_codes:
            raise ValueError("No valid language codes provided")

        self.root_dir = Path(root_dir).resolve()
        self.translations_dir = self._resolve_under_root(
            translations_dir,
            "translations",
        )
        self.image_dir = self._resolve_under_root(image_dir, "translated_images")
        self.add_disclaimer = add_disclaimer
        self.lang_subdir = Path(lang_subdir) if lang_subdir else None
        self.context = context
        self.source_path = (self.root_dir / "README.md").resolve()
        self.markdown_translator = markdown_translator
        if self.markdown_translator is None and initialize_translator:
            self.markdown_translator = self._create_markdown_translator()
        self.readme_image_translator = readme_image_translator
        if self.readme_image_translator is None and initialize_translator:
            self._initialize_readme_image_translator()
        self.readme_image_paths = self._discover_readme_images()

    def _resolve_under_root(
        self,
        path: str | Path | None,
        default: str,
    ) -> Path:
        if path is None:
            return self.root_dir / default

        candidate = Path(path)
        if candidate.is_absolute():
            return candidate.resolve()
        return (self.root_dir / candidate).resolve()

    def _initialize_markdown_translator(self) -> None:
        if self.markdown_translator is None:
            self.markdown_translator = self._create_markdown_translator()

    def _initialize_readme_image_translator(self) -> None:
        if self.readme_image_translator is None and ReadmeImageConfig.is_enabled():
            self.readme_image_translator = create_readme_image_translator()
            self.readme_image_paths = self._discover_readme_images()

    def _discover_readme_images(self) -> set[Path]:
        if self.readme_image_translator is None:
            return set()
        return discover_readme_images(self.source_path, self.root_dir)

    def _create_markdown_translator(self):
        if self.context is None:
            return MarkdownTranslator.create()
        return MarkdownTranslator.create(context=self.context)

    def _get_language_root(self, language_code: str) -> Path:
        lang_dir = self.translations_dir / language_code
        if self.lang_subdir:
            lang_dir = lang_dir / self.lang_subdir
        return lang_dir

    def get_translated_path(self, language_code: str) -> Path:
        return self._get_language_root(language_code) / "README.md"

    def _get_translated_image_path(self, image_path: Path, language_code: str) -> Path:
        filename = generate_translated_filename(
            image_path, language_code, self.root_dir
        )
        return self.image_dir / language_code / filename

    def _readme_pipeline_fingerprint(self) -> str:
        if self.readme_image_translator is None:
            return "disabled"
        return getattr(
            self.readme_image_translator,
            "metadata_fingerprint",
            self.readme_image_translator.__class__.__name__,
        )

    def _readme_text_metadata(self) -> dict[str, str]:
        return {
            "readme_image_translation_pipeline": (self._readme_pipeline_fingerprint())
        }

    def _readme_image_metadata(self) -> dict[str, str]:
        return {
            "readme_image_translation_pipeline": (self._readme_pipeline_fingerprint())
        }

    def _is_current(self, language_code: str, source_hash: str | None = None) -> bool:
        translated_path = self.get_translated_path(language_code)
        if not translated_path.exists():
            return False

        metadata = read_text_metadata_for_source(
            self._get_language_root(language_code),
            "README.md",
        )
        if metadata.get("original_hash") != (
            source_hash or calculate_file_hash(self.source_path)
        ):
            return False

        stored_pipeline = metadata.get("readme_image_translation_pipeline")
        if self.readme_image_translator is None:
            return stored_pipeline in (None, "disabled")
        if stored_pipeline != self._readme_pipeline_fingerprint():
            return False
        return all(
            is_image_up_to_date(
                image_path,
                self._get_translated_image_path(image_path, language_code),
                self.image_dir,
                expected_metadata=self._readme_image_metadata(),
            )
            for image_path in self.readme_image_paths
        )

    def get_pending_language_codes(
        self,
        *,
        update: bool = False,
        source_hash: str | None = None,
    ) -> list[str]:
        if update:
            return list(self.language_codes)
        return [
            language_code
            for language_code in self.language_codes
            if not self._is_current(language_code, source_hash=source_hash)
        ]

    def estimate_tokens(
        self,
        *,
        update: bool = False,
        source_text: str | None = None,
        source_hash: str | None = None,
    ) -> int:
        if not self.source_path.exists():
            return 0

        text = (
            source_text
            if source_text is not None
            else read_input_file(self.source_path)
        )
        pending_languages = self.get_pending_language_codes(
            update=update,
            source_hash=source_hash,
        )
        return count_tokens(text) * len(pending_languages)

    def estimate_words(
        self,
        *,
        update: bool = False,
        source_text: str | None = None,
        source_hash: str | None = None,
    ) -> int:
        if not self.source_path.exists():
            return 0

        text = (
            source_text
            if source_text is not None
            else read_input_file(self.source_path)
        )
        pending_languages = self.get_pending_language_codes(
            update=update,
            source_hash=source_hash,
        )
        return len(re.findall(r"\S+", text)) * len(pending_languages)

    async def _append_disclaimer(self, content: str, language_code: str) -> str:
        if not self.add_disclaimer:
            return content

        disclaimer = await self.markdown_translator.generate_disclaimer(language_code)
        if not disclaimer:
            return content

        start_marker = "<!-- CO-OP TRANSLATOR DISCLAIMER START -->"
        end_marker = "<!-- CO-OP TRANSLATOR DISCLAIMER END -->"
        disclaimer_block = f"{start_marker}\n{disclaimer}\n{end_marker}"
        return content + "\n\n---\n\n" + disclaimer_block

    def _rewrite_paths(
        self,
        content: str,
        language_code: str,
        translated_path: Path,
    ) -> str:
        content = self._rewrite_document_links_to_source(content, translated_path)
        return rewrite_markdown_paths(
            content,
            source_path=self.source_path,
            target_path=translated_path,
            policy=MarkdownPathRewritePolicy(
                language_code=language_code,
                root_dir=self.root_dir,
                translations_dir=self.translations_dir,
                translated_images_dir=self.image_dir,
                translation_types=[
                    "markdown",
                    "notebook",
                    *(["images"] if self.readme_image_translator else []),
                ],
                lang_subdir=self.lang_subdir,
            ),
        )

    def _rewrite_document_links_to_source(
        self,
        content: str,
        translated_path: Path,
    ) -> str:
        target_dir = translated_path.parent
        link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

        def replace_link(match: re.Match[str]) -> str:
            label = match.group(1)
            link = match.group(2)
            parsed = urlparse(link)
            path = parsed.path

            if self._should_skip_document_link(link, parsed):
                return match.group(0)

            source_target = (
                (self.root_dir / path.lstrip("/")).resolve()
                if path.startswith("/")
                else (self.source_path.parent / path).resolve()
            )
            relative_path = os.path.relpath(source_target, target_dir).replace(
                os.path.sep,
                "/",
            )
            rewritten_link = relative_path
            if parsed.query:
                rewritten_link += f"?{parsed.query}"
            if parsed.fragment:
                rewritten_link += f"#{parsed.fragment}"

            return f"[{label}]({rewritten_link})"

        return link_pattern.sub(replace_link, content)

    def _should_skip_document_link(self, link: str, parsed) -> bool:
        path = parsed.path
        if path in ("", ".", "./") or link.startswith("#"):
            return True
        if parsed.scheme or "@" in link or link.endswith((".com", ".org", ".net")):
            return True
        if re.fullmatch(r"\.?/?translations/[A-Za-z-]+/README\.md", path):
            return True

        suffix = Path(path).suffix.lower()
        return suffix not in (
            *SUPPORTED_MARKDOWN_EXTENSIONS,
            *SUPPORTED_NOTEBOOK_EXTENSIONS,
        )

    async def _translate_readme_images(
        self, language_code: str, *, update: bool = False
    ) -> None:
        if self.readme_image_translator is None:
            return

        expected_metadata = self._readme_image_metadata()
        for image_path in self.readme_image_paths:
            translated_path = self._get_translated_image_path(image_path, language_code)
            if not update and is_image_up_to_date(
                image_path,
                translated_path,
                self.image_dir,
                expected_metadata=expected_metadata,
            ):
                continue

            translated_path.parent.mkdir(parents=True, exist_ok=True)
            try:
                translate_async = getattr(
                    self.readme_image_translator,
                    "translate_image_async",
                    None,
                )
                if translate_async is not None:
                    translated_image = await translate_async(
                        image_path,
                        language_code,
                        fast_mode=False,
                    )
                else:
                    translated_image = await asyncio.to_thread(
                        self.readme_image_translator.translate_image,
                        image_path,
                        language_code,
                        fast_mode=False,
                    )
                save_optimized_image(translated_image, translated_path)
                save_image_metadata(
                    translated_path,
                    image_path,
                    language_code,
                    self.root_dir,
                    image_dir=self.image_dir,
                    extra_fields=expected_metadata,
                )
            except Exception:
                logger.error(
                    "README image generation failed for %s; preserving the "
                    "source image in the translated output.",
                    image_path,
                    exc_info=True,
                )
                with Image.open(image_path) as original_image:
                    save_optimized_image(original_image.copy(), translated_path)
                save_image_metadata(
                    translated_path,
                    image_path,
                    language_code,
                    self.root_dir,
                    image_dir=self.image_dir,
                )

    async def translate_readme(
        self,
        language_code: str,
        *,
        update: bool = False,
    ) -> ReadmeTranslationResult:
        if not self.source_path.exists():
            raise FileNotFoundError(f"README.md not found under {self.root_dir}")

        self._initialize_readme_image_translator()
        language_code = normalize_language_codes([language_code])[0]
        translated_path = self.get_translated_path(language_code)

        if not update and self._is_current(language_code):
            return ReadmeTranslationResult(
                language_code=language_code,
                source_path=self.source_path,
                translated_path=translated_path,
                skipped=True,
            )

        self._initialize_markdown_translator()

        document = read_input_file(self.source_path)
        translated_path.parent.mkdir(parents=True, exist_ok=True)

        if not document:
            handle_empty_document(self.source_path, translated_path)
            save_text_metadata_for_source(
                self._get_language_root(language_code),
                self.source_path,
                language_code,
                root_dir=self.root_dir,
                extra_fields=self._readme_text_metadata(),
            )
            return ReadmeTranslationResult(
                language_code=language_code,
                source_path=self.source_path,
                translated_path=translated_path,
            )

        translated_content = await self.markdown_translator.translate_markdown(
            document,
            language_code,
            source_path=self.source_path,
        )
        translated_content = self._rewrite_paths(
            translated_content,
            language_code,
            translated_path,
        )
        if not translated_content:
            raise RuntimeError(
                "Markdown translation returned empty content for README.md"
            )

        if compare_line_breaks(document, translated_content):
            logger.warning("README translation line-break check failed. Retrying.")
            translated_content = await self.markdown_translator.translate_markdown(
                document,
                language_code,
                source_path=self.source_path,
            )
            translated_content = self._rewrite_paths(
                translated_content,
                language_code,
                translated_path,
            )
            if not translated_content:
                raise RuntimeError(
                    "Markdown translation retry returned empty content for README.md"
                )
            if compare_line_breaks(document, translated_content):
                raise RuntimeError(
                    "Markdown translation retry produced incomplete content for README.md"
                )

        await self._translate_readme_images(language_code, update=update)
        translated_content = await self._append_disclaimer(
            translated_content,
            language_code,
        )
        translated_path.write_text(translated_content, encoding="utf-8")
        save_text_metadata_for_source(
            self._get_language_root(language_code),
            self.source_path,
            language_code,
            root_dir=self.root_dir,
            extra_fields=self._readme_text_metadata(),
        )
        return ReadmeTranslationResult(
            language_code=language_code,
            source_path=self.source_path,
            translated_path=translated_path,
        )

    async def translate_async(
        self,
        *,
        update: bool = False,
    ) -> list[ReadmeTranslationResult]:
        self._initialize_readme_image_translator()
        self.readme_image_paths = self._discover_readme_images()
        return await run_tasks_concurrently(
            [
                partial(self.translate_readme, language_code, update=update)
                for language_code in self.language_codes
            ],
            self.concurrency,
        )

    def translate(self, *, update: bool = False) -> list[ReadmeTranslationResult]:
        return asyncio.run(self.translate_async(update=update))
