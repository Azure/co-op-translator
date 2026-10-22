from __future__ import annotations

import asyncio
import logging
import os
from pathlib import Path

from PIL import Image

from co_op_translator.utils.common.file_utils import (
    delete_translated_images_by_language_code,
    generate_translated_filename,
    get_filename_and_extension,
)
from co_op_translator.utils.common.metadata_utils import (
    is_image_up_to_date,
    save_image_metadata,
)
from co_op_translator.utils.markdown.readme_images import discover_readme_images
from co_op_translator.utils.vision.image_utils import save_optimized_image

logger = logging.getLogger(__name__)


class ProjectImageTranslationMixin:
    README_PIPELINE_METADATA_KEY = "readme_image_translation_pipeline"
    VISION_PIPELINE_FINGERPRINT = "azure-ai-vision"

    def _get_translated_image_path(self, image_path: Path, language_code: str) -> Path:
        translated_filename = generate_translated_filename(
            image_path, language_code, self.root_dir
        )
        return Path(self.image_dir) / language_code / translated_filename

    def _save_original_image_translation(
        self, image_path: Path, translated_path: Path, language_code: str
    ) -> str:
        translated_path.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(image_path) as original_image:
            save_optimized_image(original_image.copy(), translated_path)
        save_image_metadata(
            translated_path,
            image_path,
            language_code,
            self.root_dir,
            image_dir=Path(self.image_dir),
        )
        return str(translated_path)

    def _is_readme_image(self, image_path: Path) -> bool:
        return image_path.resolve() in getattr(self, "readme_image_paths", set())

    def _get_image_translator(self, image_path: Path):
        if self._is_readme_image(image_path):
            readme_translator = getattr(self, "readme_image_translator", None)
            if readme_translator is not None:
                return readme_translator
        return self.image_translator

    def _get_image_pipeline_metadata(
        self, image_path: Path, translator=None
    ) -> dict[str, str]:
        if not self._is_readme_image(image_path):
            return {}
        translator = translator or self._get_image_translator(image_path)
        if translator is getattr(self, "readme_image_translator", None):
            fingerprint = getattr(translator, "metadata_fingerprint", None)
            if fingerprint:
                return {self.README_PIPELINE_METADATA_KEY: fingerprint}
        return {self.README_PIPELINE_METADATA_KEY: self.VISION_PIPELINE_FINGERPRINT}

    async def _run_image_translator(
        self, translator, image_path: Path, language_code: str, fast_mode: bool
    ):
        translate_async = getattr(translator, "translate_image_async", None)
        if translate_async is not None:
            return await translate_async(
                image_path,
                language_code,
                fast_mode=fast_mode,
            )
        return await asyncio.to_thread(
            translator.translate_image,
            image_path,
            language_code,
            fast_mode=fast_mode,
        )

    async def translate_image(
        self, image_path: Path, language_code: str, fast_mode: bool = False
    ) -> str:
        """Translate an image to the target language."""

        image_path = Path(image_path).resolve()
        translated_image_path = self._get_translated_image_path(
            image_path, language_code
        )
        selected_translator = self._get_image_translator(image_path)
        if not selected_translator:
            logger.info(
                f"Image translation skipped for {image_path} due to missing Azure AI Service configuration"
            )
            return str(image_path)

        if image_path.exists() and image_path.is_file():
            logger.info(f"Image exists: {image_path}")
            if os.access(image_path, os.R_OK):
                logger.info(f"Read permission granted for: {image_path}")
            else:
                logger.warning(f"Read permission denied for: {image_path}")
                return str(image_path)
        else:
            logger.error(f"Image does not exist or is not a valid file: {image_path}")
            return str(image_path)

        try:
            if translated_image_path.exists() and is_image_up_to_date(
                image_path,
                translated_image_path,
                self.image_dir,
                expected_metadata=self._get_image_pipeline_metadata(
                    image_path, selected_translator
                ),
            ):
                logger.info(
                    f"Skipping image translation; up-to-date output exists: {translated_image_path}"
                )
                return str(translated_image_path)

            metadata = self._get_image_pipeline_metadata(
                image_path, selected_translator
            )
            try:
                translated_image = await self._run_image_translator(
                    selected_translator,
                    image_path,
                    language_code,
                    fast_mode,
                )
            except Exception:
                readme_translator = getattr(self, "readme_image_translator", None)
                if (
                    selected_translator is not readme_translator
                    or self.image_translator is None
                ):
                    raise
                logger.warning(
                    "README image generation failed for %s; falling back to "
                    "Azure AI Vision.",
                    image_path,
                    exc_info=True,
                )
                selected_translator = self.image_translator
                metadata = self._get_image_pipeline_metadata(
                    image_path, selected_translator
                )
                translated_image = await self._run_image_translator(
                    selected_translator,
                    image_path,
                    language_code,
                    fast_mode,
                )
            translated_image_path.parent.mkdir(parents=True, exist_ok=True)
            save_optimized_image(translated_image, translated_image_path)
            save_image_metadata(
                translated_image_path,
                image_path,
                language_code,
                self.root_dir,
                image_dir=Path(self.image_dir),
                extra_fields=metadata,
            )

            logger.info(
                f"Translated image {image_path} to {language_code} and saved to {translated_image_path}"
            )
            return str(translated_image_path)
        except Exception as e:
            logger.error(f"Failed to translate image {image_path}: {e}", exc_info=True)
            try:
                return self._save_original_image_translation(
                    image_path, translated_image_path, language_code
                )
            except Exception:
                logger.error(
                    f"Failed to save fallback image translation for {image_path}",
                    exc_info=True,
                )
                return str(image_path)

    async def translate_all_image_files(
        self, update: bool = False, fast_mode: bool = False
    ) -> tuple[int, list[str]]:
        """Process and translate all image files in the project directory."""

        modified_count = 0
        errors = []

        logger.info("Starting image translation tasks...")

        self.readme_image_paths = discover_readme_images(
            Path(self.root_dir) / "README.md", Path(self.root_dir)
        )

        if update:
            for language_code in self.language_codes:
                delete_translated_images_by_language_code(language_code, self.image_dir)
                logger.info(
                    f"Deleted all translated images for language: {language_code}"
                )

        image_files = self._filter_source_files()
        tasks = []
        task_info = []

        for image_file_path in image_files:
            image_file_path = image_file_path.resolve()

            if (
                get_filename_and_extension(image_file_path)[1]
                not in self.supported_image_extensions
            ):
                continue

            for language_code in self.language_codes:
                translated_filename = generate_translated_filename(
                    image_file_path, language_code, self.root_dir
                )
                translated_image_path = (
                    Path(self.image_dir) / language_code / translated_filename
                )

                if translated_image_path.exists() and not update:
                    if is_image_up_to_date(
                        image_file_path,
                        translated_image_path,
                        self.image_dir,
                        expected_metadata=self._get_image_pipeline_metadata(
                            image_file_path
                        ),
                    ):
                        logger.info(
                            f"Skipping up-to-date image: {translated_image_path}"
                        )
                        continue

                    logger.info(
                        f"Image metadata mismatch detected: {image_file_path} -> {translated_image_path}"
                    )

                logger.info(
                    f"Translating image: {image_file_path} for language: {language_code}"
                )
                tasks.append(
                    self.translate_image(
                        image_file_path, language_code, fast_mode=fast_mode
                    )
                )
                task_info.append((str(image_file_path), language_code))

        if tasks:
            task_desc = (
                "Translating images (fast mode)" if fast_mode else "Translating images"
            )
            results = await self.process_api_requests_parallel(
                tasks,
                task_desc,
            )
            modified_count = sum(
                1
                for (file_path, _lang_code), result in zip(task_info, results)
                if result != file_path
            )
            errors = [
                f"Failed to translate image file: {file_path} (lang: {lang_code})"
                for (file_path, lang_code), result in zip(task_info, results)
                if result == file_path
            ]
        else:
            logger.warning("No image files found for translation.")

        return modified_count, errors
