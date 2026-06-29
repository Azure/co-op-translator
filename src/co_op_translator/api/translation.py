import importlib.resources
import logging
import os
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

import click
import yaml
from PIL import Image

from co_op_translator.config.base_config import Config
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.config.vision_config.config import VisionConfig
from co_op_translator.core.agent_translation import (
    finish_markdown_agent_translation as finish_markdown_agent_translation_job,
    finish_notebook_agent_translation as finish_notebook_agent_translation_job,
    start_markdown_agent_translation as start_markdown_agent_translation_job,
    start_notebook_agent_translation as start_notebook_agent_translation_job,
)
from co_op_translator.core.llm.jupyter_notebook_translator import (
    JupyterNotebookTranslator,
)
from co_op_translator.core.llm.markdown_translator import MarkdownTranslator
from co_op_translator.core.project.language_migrator import LanguageFolderMigrator
from co_op_translator.core.project.project_translator import ProjectTranslator
from co_op_translator.core.vision.image_translator import ImageTranslator
from co_op_translator.glossary import glossary_terms_scope
from co_op_translator.utils.common.file_utils import (
    render_updated_readme_languages_table,
    render_updated_readme_other_courses,
    update_readme_languages_table,
    update_readme_other_courses,
)
from co_op_translator.utils.common.lang_utils import normalize_language_codes
from co_op_translator.utils.common.logging_utils import setup_logging
from co_op_translator.utils.common.metadata_utils import (
    normalize_language_codes_in_lang_metadata,
)
from co_op_translator.utils.common.token_estimation import estimate_translation_tokens
from co_op_translator.utils.common.word_estimation import estimate_translation_words
from co_op_translator.utils.markdown.path_rewriter import (
    MarkdownPathRewritePolicy,
    rewrite_markdown_paths as rewrite_markdown_paths_for_project,
)
from co_op_translator.utils.markdown.notebook_path_rewriter import (
    rewrite_notebook_paths as rewrite_notebook_paths_for_project,
)

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class MarkdownTranslationOptions:
    """Options for content-only markdown translation."""

    source_path: str | Path | None = None


@dataclass(frozen=True)
class ImageTranslationOptions:
    """Options for content-only image translation."""

    root_dir: str | Path = "."
    fast_mode: bool = False


@dataclass(frozen=True)
class NotebookTranslationOptions:
    """Options for content-only notebook translation."""

    source_path: str | Path | None = None


def _coerce_markdown_translation_options(
    options: MarkdownTranslationOptions | Mapping[str, object] | None,
) -> MarkdownTranslationOptions:
    if options is None:
        return MarkdownTranslationOptions()
    if isinstance(options, MarkdownTranslationOptions):
        return options
    return MarkdownTranslationOptions(**dict(options))


def _coerce_image_translation_options(
    options: ImageTranslationOptions | Mapping[str, object] | None,
) -> ImageTranslationOptions:
    if options is None:
        return ImageTranslationOptions()
    if isinstance(options, ImageTranslationOptions):
        return options
    return ImageTranslationOptions(**dict(options))


def _coerce_notebook_translation_options(
    options: NotebookTranslationOptions | Mapping[str, object] | None,
) -> NotebookTranslationOptions:
    if options is None:
        return NotebookTranslationOptions()
    if isinstance(options, NotebookTranslationOptions):
        return options
    return NotebookTranslationOptions(**dict(options))


async def translate_markdown_content(
    document: str,
    language_code: str,
    options: MarkdownTranslationOptions | Mapping[str, object] | None = None,
) -> str:
    """Translate markdown content without project path rewriting or file I/O."""

    resolved_options = _coerce_markdown_translation_options(options)
    translator = MarkdownTranslator.create()
    return await translator.translate_markdown(
        document,
        language_code,
        source_path=resolved_options.source_path,
    )


async def translate_notebook_content(
    notebook: str | dict[str, object],
    language_code: str,
    options: NotebookTranslationOptions | Mapping[str, object] | None = None,
) -> str:
    """Translate notebook markdown cells without project path rewriting or file I/O."""

    resolved_options = _coerce_notebook_translation_options(options)
    translator = JupyterNotebookTranslator.create()
    return await translator.translate_notebook(
        notebook,
        language_code,
        source_path=resolved_options.source_path,
    )


def start_markdown_agent_translation(
    document: str,
    language_code: str,
    source_path: str | Path | None = None,
) -> dict[str, object]:
    """Prepare provider-free Markdown chunks for host-agent translation."""

    return start_markdown_agent_translation_job(
        document,
        language_code,
        source_path=source_path,
    )


def finish_markdown_agent_translation(
    job: Mapping[str, object],
    translated_chunks: Mapping[str, object] | list[Mapping[str, object]],
) -> dict[str, object]:
    """Reconstruct Markdown from chunks translated by a host agent."""

    return finish_markdown_agent_translation_job(job, translated_chunks)


def start_notebook_agent_translation(
    notebook: str | Mapping[str, object],
    language_code: str,
    source_path: str | Path | None = None,
) -> dict[str, object]:
    """Prepare provider-free notebook Markdown chunks for host-agent translation."""

    return start_notebook_agent_translation_job(
        notebook,
        language_code,
        source_path=source_path,
    )


def finish_notebook_agent_translation(
    job: Mapping[str, object],
    translated_chunks: Mapping[str, object] | list[Mapping[str, object]],
) -> dict[str, object]:
    """Reconstruct a notebook from Markdown chunks translated by a host agent."""

    return finish_notebook_agent_translation_job(job, translated_chunks)


def translate_image_content(
    image_path: str | Path,
    language_code: str,
    options: ImageTranslationOptions | Mapping[str, object] | None = None,
) -> Image.Image:
    """Translate image text and return a rendered image without saving metadata."""

    resolved_options = _coerce_image_translation_options(options)
    translator = ImageTranslator.create(
        root_dir=resolved_options.root_dir,
    )
    return translator.translate_image(
        image_path,
        language_code,
        fast_mode=resolved_options.fast_mode,
    )


def rewrite_notebook_paths(
    content: str,
    source_path: str | Path,
    target_path: str | Path,
    policy: MarkdownPathRewritePolicy | Mapping[str, object],
) -> str:
    """Rewrite markdown-cell paths for a translated project notebook target."""

    return rewrite_notebook_paths_for_project(
        content,
        source_path=source_path,
        target_path=target_path,
        policy=policy,
    )


def rewrite_markdown_paths(
    content: str,
    source_path: str | Path,
    target_path: str | Path,
    policy: MarkdownPathRewritePolicy | Mapping[str, object],
) -> str:
    """Rewrite markdown/frontmatter paths for a translated project target."""

    return rewrite_markdown_paths_for_project(
        content,
        source_path=source_path,
        target_path=target_path,
        policy=policy,
    )


def compute_pretranslation_virtual_inputs(
    root_path: Path,
    translation_types: list[str],
    repo_url: str | None = None,
) -> dict[Path, str]:
    """Return virtual source content for deterministic pre-translation rewrites."""
    if "markdown" not in translation_types:
        return {}

    readme_path = (root_path / "README.md").resolve()
    if not readme_path.exists():
        return {}

    original = readme_path.read_text(encoding="utf-8")
    updated = render_updated_readme_languages_table(original, repo_url=repo_url)
    updated = render_updated_readme_other_courses(updated)
    if updated == original:
        return {}
    return {readme_path: updated}


def run_translation(
    language_codes: str,
    root_dir: str = ".",
    update: bool = False,
    images: bool = False,
    markdown: bool = False,
    notebook: bool = False,
    debug: bool = False,
    save_logs: bool = False,
    yes: bool = True,
    add_disclaimer: bool = False,
    translations_dir: str | None = None,
    image_dir: str | None = None,
    root_dirs: Iterable[str] | None = None,
    groups: Iterable[tuple[str, str | None]] | None = None,
    repo_url: str | None = None,
    glossaries: Iterable[str] | None = None,
    readme_only: bool = False,
    dry_run: bool = False,
) -> None:
    """Programmatic translation entrypoint mirroring the translate CLI options."""

    def _split_lang_placeholder(path: str) -> tuple[str, str | None]:
        placeholder = "<lang>"
        if placeholder not in path:
            return path, None

        prefix, suffix = path.split(placeholder, 1)
        prefix = prefix.rstrip("/\\")
        suffix = suffix.lstrip("/\\")

        return prefix, (suffix or None)

    def _run_single_group(
        *,
        language_codes: str,
        root_dir: str,
        update: bool,
        images: bool,
        markdown: bool,
        notebook: bool,
        debug: bool,
        save_logs: bool,
        yes: bool,
        add_disclaimer: bool,
        translations_dir: str | None,
        image_dir: str | None,
        lang_subdir: str | None,
        repo_url: str | None,
        readme_only: bool,
        dry_run: bool,
    ) -> None:
        Config.check_configuration()

        translation_types: list[str] = []
        if readme_only:
            if images or notebook:
                raise RuntimeError(
                    "readme_only can only be used with markdown translation."
                )
            translation_types = ["markdown"]
        elif markdown:
            translation_types.append("markdown")
            if images:
                translation_types.append("images")
            if notebook:
                translation_types.append("notebook")
        else:
            if images:
                translation_types.append("images")
            if notebook:
                translation_types.append("notebook")
        if not translation_types:
            translation_types = ["markdown", "notebook", "images"]

        if "images" in translation_types:
            cv_available = VisionConfig.check_configuration()
            if not cv_available:
                raise RuntimeError(
                    "Image translation is enabled but Azure AI Service is not configured.\n"
                    "Please add AZURE_AI_SERVICE_API_KEY to your environment variables or use "
                    "translation_types without 'images'.\n"
                    "See the .env.template file for required variables."
                )

        click.echo(f"🚀 Translation mode: {', '.join(translation_types)}")

        root_path = Path(root_dir).resolve()
        if not root_path.exists():
            raise ValueError(f"Root directory does not exist: {root_dir}")
        if not root_path.is_dir():
            raise ValueError(f"Root path is not a directory: {root_dir}")

        log_file_path = setup_logging(
            root_path, debug=debug, save_logs=save_logs, command_name="translate"
        )
        if debug:
            logging.debug("Debug mode enabled.")
        if save_logs and log_file_path is not None:
            click.echo(f"📄 Logs will be saved to: {log_file_path}")

        LLMConfig.validate_connectivity()
        logger.info("LLM health check passed.")
        click.echo("✅ LLM health check passed.")

        if "images" in translation_types:
            VisionConfig.validate_connectivity()
            logger.info("Vision health check passed.")
            click.echo("✅ Vision health check passed.")

        all_languages_selected = language_codes == "all"
        if all_languages_selected:
            click.echo(
                "Warning: Translating all languages at once can take a significant amount of time, "
                "especially for large projects."
            )
            if yes:
                logger.info("Auto-confirming 'all' languages in non-interactive mode.")
                click.echo("Auto-confirming translation for all languages...")

            try:
                with importlib.resources.path(
                    "co_op_translator.fonts", "font_language_mappings.yml"
                ) as mappings_path:
                    with open(mappings_path, "r", encoding="utf-8") as file:
                        font_mappings = yaml.safe_load(file)
                        if not font_mappings:
                            raise RuntimeError("Empty font mappings file")
                        language_codes = " ".join(
                            [
                                lang_code
                                for lang_code in font_mappings
                                if isinstance(font_mappings[lang_code], dict)
                            ]
                        )
                        if not language_codes:
                            raise RuntimeError(
                                "No valid language codes found in font mappings"
                            )
                        logging.debug(
                            f"Loaded language codes from font mapping: {language_codes}"
                        )
            except (FileNotFoundError, yaml.YAMLError) as e:
                raise RuntimeError(f"Failed to load font mappings: {str(e)}") from e

        if all_languages_selected:
            try:
                lang_list = Config.get_language_codes()
            except Exception:
                lang_list = [
                    code.strip() for code in language_codes.split() if code.strip()
                ]
        else:
            lang_list = [
                code.strip() for code in language_codes.split() if code.strip()
            ]
        lang_list = normalize_language_codes(lang_list) if lang_list else []

        if update:
            if readme_only:
                click.echo(
                    f"Warning: Update mode will delete existing translated README files for '{language_codes}' "
                    f"and re-translate them."
                )
            else:
                click.echo(
                    f"Warning: Update mode will delete all existing translations for '{language_codes}' "
                    f"and re-translate them."
                )

        try:
            effective_translations_dir = (
                (root_path / translations_dir).resolve()
                if translations_dir is not None
                and not Path(translations_dir).is_absolute()
                else (
                    Path(translations_dir).resolve()
                    if translations_dir is not None
                    else (root_path / "translations")
                )
            )
            effective_image_dir = (
                (root_path / image_dir).resolve()
                if image_dir is not None and not Path(image_dir).is_absolute()
                else (
                    Path(image_dir).resolve()
                    if image_dir is not None
                    else (root_path / "translated_images")
                )
            )

            migrator = LanguageFolderMigrator(
                root_path,
                translations_dir=effective_translations_dir,
                image_dir=effective_image_dir,
            )
            alias_entries = migrator.detect_alias_folders()
            if alias_entries:
                canon_set = set(lang_list)
                relevant = [e for e in alias_entries if e.canonical in canon_set]
                if relevant:
                    plan = LanguageFolderMigrator.format_plan(relevant)
                    logger.info("Language folder migration plan:\n%s", plan)
                    click.echo(plan)
                    if dry_run:
                        click.echo("Dry run: no changes will be made.")
                    else:
                        renamed, msgs = migrator.execute(relevant, dry_run=False)
                        logger.info("Auto-migrated %d language folder(s).", renamed)
                        for m in msgs:
                            logger.warning(m)
        except Exception as e:  # pragma: no cover
            logger.warning(f"Language folder migration step skipped: {e}")

        if not dry_run:
            try:
                for lang in lang_list:
                    lang_root = (
                        effective_translations_dir
                        if "effective_translations_dir" in locals()
                        else (root_path / "translations")
                    ) / lang
                    if lang_subdir:
                        lang_root = lang_root / lang_subdir

                    normalize_language_codes_in_lang_metadata(
                        lang_root,
                        lang,
                    )
                    normalize_language_codes_in_lang_metadata(
                        (
                            effective_image_dir
                            if "effective_image_dir" in locals()
                            else (root_path / "translated_images")
                        )
                        / lang,
                        lang,
                    )
                    normalize_language_codes_in_lang_metadata(
                        root_path / "translated_images_fast" / lang,
                        lang,
                    )
            except Exception as e:  # pragma: no cover
                logger.debug(f"Metadata normalization skipped: {e}")

            readme_path = root_path / "README.md"
            try:
                if update_readme_languages_table(readme_path, repo_url=repo_url):
                    click.echo("✅ Updated README languages table from template.")
                else:
                    click.echo(
                        "ℹ️ README languages table not updated (markers missing or template unavailable)."
                    )
            except Exception as e:  # pragma: no cover
                logger.warning(f"Failed to update README languages table: {e}")

            try:
                if update_readme_other_courses(readme_path):
                    click.echo(
                        "✅ Updated README 'Other courses' section from template."
                    )
            except Exception as e:  # pragma: no cover
                logger.warning(f"Failed to update README 'Other courses': {e}")

        translator_kwargs = {
            "translation_types": translation_types,
            "add_disclaimer": add_disclaimer,
            "translations_dir": translations_dir,
            "image_dir": image_dir,
            "lang_subdir": lang_subdir,
        }
        if readme_only:
            translator_kwargs["readme_only"] = True

        translator = ProjectTranslator(
            language_codes,
            root_dir,
            **translator_kwargs,
        )

        if dry_run:
            click.echo("🧪 Dry run complete: no changes made.")
            return

        translator.translate_project(
            update=update,
        )

        logger.info(f"Project translation completed for languages: {language_codes}")

    def _merge_estimates(
        current: dict[str, int],
        incoming: dict[str, int],
    ) -> dict[str, int]:
        merged = dict(current)
        for key in (
            "markdown",
            "notebook",
            "images",
            "outdated_markdown",
            "outdated_notebook",
            "outdated_images",
            "outdated",
            "total",
            "words",
        ):
            merged[key] = int(merged.get(key, 0)) + int(incoming.get(key, 0))
        return merged

    def _echo_estimate_summary(
        est: dict[str, int],
        translation_types: list[str],
    ) -> None:
        translation_parts: list[str] = []
        if "markdown" in translation_types:
            translation_parts.append(f"markdown: {est.get('markdown', 0):,}")
        if "notebook" in translation_types:
            translation_parts.append(f"notebook: {est.get('notebook', 0):,}")
        if "images" in translation_types:
            translation_parts.append(f"images: {est.get('images', 0):,}")

        retranslation_parts: list[str] = []
        if "markdown" in translation_types:
            retranslation_parts.append(
                f"outdated markdowns: {est.get('outdated_markdown', 0):,}"
            )
        if "notebook" in translation_types:
            retranslation_parts.append(
                f"outdated notebooks: {est.get('outdated_notebook', 0):,}"
            )
        if "images" in translation_types:
            retranslation_parts.append(
                f"outdated images: {est.get('outdated_images', 0):,}"
            )

        breakdown_sections: list[str] = []
        if translation_parts:
            breakdown_sections.append(f"translation: {'; '.join(translation_parts)}")
        if retranslation_parts:
            breakdown_sections.append(
                f"retranslation: {'; '.join(retranslation_parts)}"
            )
        breakdown = " | ".join(breakdown_sections) if breakdown_sections else "none"
        click.echo(
            "📊 Estimated translation volume before translation: "
            f"{est.get('total', 0):,} tokens ({est.get('words', 0):,} words) "
            f"(breakdown: {breakdown})"
        )

    def _compute_estimate_for_group(
        *,
        language_codes: str,
        root_dir: str,
        update: bool,
        markdown: bool,
        images: bool,
        notebook: bool,
        add_disclaimer: bool,
        translations_dir: str | None,
        image_dir: str | None,
        lang_subdir: str | None,
        repo_url: str | None,
        readme_only: bool,
    ) -> dict[str, int]:
        translation_types: list[str] = []
        if readme_only:
            if images or notebook:
                raise RuntimeError(
                    "readme_only can only be used with markdown translation."
                )
            translation_types = ["markdown"]
        elif markdown:
            translation_types.append("markdown")
            if images:
                translation_types.append("images")
            if notebook:
                translation_types.append("notebook")
        else:
            if images:
                translation_types.append("images")
            if notebook:
                translation_types.append("notebook")
        if not translation_types:
            translation_types = ["markdown", "notebook", "images"]

        translator_kwargs = {
            "translation_types": translation_types,
            "add_disclaimer": add_disclaimer,
            "translations_dir": translations_dir,
            "image_dir": image_dir,
            "lang_subdir": lang_subdir,
        }
        if readme_only:
            translator_kwargs["readme_only"] = True

        translator = ProjectTranslator(
            language_codes,
            root_dir,
            **translator_kwargs,
        )
        virtual_file_contents = compute_pretranslation_virtual_inputs(
            Path(root_dir).resolve(),
            translation_types,
            repo_url=repo_url,
        )
        est = estimate_translation_tokens(
            translator.translation_manager,
            update=update,
            virtual_file_contents=virtual_file_contents,
        )
        words_est = estimate_translation_words(
            translator.translation_manager,
            update=update,
            virtual_file_contents=virtual_file_contents,
        )

        return {
            "markdown": int(est.get("markdown", 0) or 0),
            "notebook": int(est.get("notebook", 0) or 0),
            "images": int(est.get("images", 0) or 0),
            "outdated_markdown": int(est.get("outdated_markdown", 0) or 0),
            "outdated_notebook": int(est.get("outdated_notebook", 0) or 0),
            "outdated_images": int(est.get("outdated_images", 0) or 0),
            "outdated": int(est.get("outdated", 0) or 0),
            "total": int(est.get("total", 0) or 0),
            "words": int(words_est.get("total", 0) or 0),
        }

    @contextmanager
    def _tqdm_disabled(disabled: bool):
        if not disabled:
            yield
            return

        previous = os.environ.get("TQDM_DISABLE")
        os.environ["TQDM_DISABLE"] = "1"
        try:
            yield
        finally:
            if previous is None:
                os.environ.pop("TQDM_DISABLE", None)
            else:
                os.environ["TQDM_DISABLE"] = previous

    with glossary_terms_scope(glossaries):
        aggregate_template = {
            "markdown": 0,
            "notebook": 0,
            "images": 0,
            "outdated_markdown": 0,
            "outdated_notebook": 0,
            "outdated_images": 0,
            "outdated": 0,
            "total": 0,
            "words": 0,
        }
        translation_types_for_summary: list[str] = []
        if readme_only:
            translation_types_for_summary = ["markdown"]
        elif markdown:
            translation_types_for_summary.append("markdown")
            if images:
                translation_types_for_summary.append("images")
            if notebook:
                translation_types_for_summary.append("notebook")
        else:
            if images:
                translation_types_for_summary.append("images")
            if notebook:
                translation_types_for_summary.append("notebook")
        if not translation_types_for_summary:
            translation_types_for_summary = ["markdown", "notebook", "images"]

        execution_targets: list[tuple[str, str | None, str | None]] = []
        if groups is not None:
            for per_root, per_translations in list(groups):
                per_translations_dir: str | None = per_translations
                per_lang_subdir: str | None = None
                if per_translations is not None:
                    base_part, suffix = _split_lang_placeholder(per_translations)
                    per_translations_dir = base_part or None
                    per_lang_subdir = suffix
                execution_targets.append(
                    (per_root, per_translations_dir, per_lang_subdir)
                )
        elif root_dirs is not None:
            for per_root in list(root_dirs):
                execution_targets.append((per_root, translations_dir, None))
        else:
            execution_targets.append((root_dir, translations_dir, None))

        aggregated_estimate = dict(aggregate_template)
        for per_root, per_translations_dir, per_lang_subdir in execution_targets:
            group_estimate = _compute_estimate_for_group(
                language_codes=language_codes,
                root_dir=per_root,
                update=update,
                markdown=markdown,
                images=images,
                notebook=notebook,
                add_disclaimer=add_disclaimer,
                translations_dir=per_translations_dir,
                image_dir=image_dir,
                lang_subdir=per_lang_subdir,
                repo_url=repo_url,
                readme_only=readme_only,
            )
            aggregated_estimate = _merge_estimates(aggregated_estimate, group_estimate)

        _echo_estimate_summary(aggregated_estimate, translation_types_for_summary)

        multi_group_mode = len(execution_targets) > 1

        for per_root, per_translations_dir, per_lang_subdir in execution_targets:
            with _tqdm_disabled(multi_group_mode):
                _run_single_group(
                    language_codes=language_codes,
                    root_dir=per_root,
                    update=update,
                    images=images,
                    markdown=markdown,
                    notebook=notebook,
                    debug=debug,
                    save_logs=save_logs,
                    yes=yes,
                    add_disclaimer=add_disclaimer,
                    translations_dir=per_translations_dir,
                    image_dir=image_dir,
                    lang_subdir=per_lang_subdir,
                    repo_url=repo_url,
                    readme_only=readme_only,
                    dry_run=dry_run,
                )


def translate_project(*args, **kwargs) -> None:
    """Programmatic project translation entrypoint."""

    return run_translation(*args, **kwargs)
