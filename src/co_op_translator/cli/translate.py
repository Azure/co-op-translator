"""
Translate command implementation for Co-op Translator CLI.
"""

import asyncio
import logging
import click
import importlib.resources
import yaml
import os
from pathlib import Path

from co_op_translator.core.project.project_translator import ProjectTranslator
from co_op_translator.config.base_config import Config
from co_op_translator.config.vision_config.config import VisionConfig
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.utils.common.logging_utils import setup_logging
from co_op_translator.utils.common.file_utils import (
    update_readme_languages_table,
    update_readme_other_courses,
)

logger = logging.getLogger(__name__)


@click.command(name="translate")
@click.option(
    "--language-codes",
    "-l",
    required=True,
    help='Space-separated language codes for translation (e.g., "es fr de" or "all").',
)
@click.option(
    "--root-dir",
    "-r",
    default=".",
    help="Root directory of the project (default is current directory).",
)
@click.option(
    "--update",
    "-u",
    is_flag=True,
    help="Update translations by deleting and recreating them (Warning: Existing translations will be lost).",
)
@click.option("--images", "-img", is_flag=True, help="Only translate image files.")
@click.option("--markdown", "-md", is_flag=True, help="Only translate markdown files.")
@click.option("--notebook", "-nb", is_flag=True, help="Only translate notebook files.")
@click.option("--debug", "-d", is_flag=True, help="Enable debug mode.")
@click.option(
    "--save-logs",
    "-s",
    is_flag=True,
    help="Save logs to the logs/ directory under --root-dir (always at DEBUG level).",
)
@click.option(
    "--fix",
    "-x",
    is_flag=True,
    help="Retranslate files with low confidence scores based on previous evaluation results.",
)
@click.option(
    "--min-confidence",
    "-c",
    default=0.7,
    type=float,
    help="Minimum confidence threshold (0.0-1.0) for identifying translations to fix. Only used with --fix.",
)
@click.option(
    "--add-disclaimer/--no-disclaimer",
    default=True,
    help="Add machine translation disclaimer sections to translated markdown and notebooks (default: enabled).",
)
@click.option(
    "--fast",
    "-f",
    is_flag=True,
    help="Use fast mode for image translation (up to 3x faster at a slight cost to quality and alignment).",
)
@click.option(
    "--yes",
    "-y",
    is_flag=True,
    help="Automatically confirm all prompts (useful for CI/CD pipelines).",
)
def translate_command(
    language_codes,
    root_dir,
    update,
    images,
    markdown,
    notebook,
    debug,
    save_logs,
    fix,
    fast,
    yes,
    min_confidence,
    add_disclaimer,
):
    """
    CLI for translating project files.

    Usage examples:

    1. Default behavior (add new translations without deleting existing ones):
       translate -l "ko"
       translate -l "es fr de" -r "./my_project"

    2. Add only new Korean image translations (no existing translations are deleted):
       translate -l "ko" -img

    3. Add only new Korean notebook translations:
       translate -l "ko" -nb

    4. Update all Korean translations (Warning: This deletes all existing Korean translations before re-translating):
       translate -l "ko" -u

    5. Update only Korean images (Warning: This deletes all existing Korean images before re-translating):
       translate -l "ko" -img -u

    6. Add new markdown translations for Korean without affecting other translations:
       translate -l "ko" -md

    7. Fix low confidence translations based on previous evaluation results:
       translate -l "ko" --fix

    8. Fix low confidence translations with custom threshold:
       translate -l "ko" --fix -c 0.8

    9. Fix low confidence translations for specific files only:
       translate -l "ko" --fix -md

    10. Use fast mode for image translation:
       translate -l "ko" -img -f

    Debug mode example:
    - translate -l "ko" -d: Enable debug logging.
    """

    try:
        # Check that the required environment variables are set
        Config.check_configuration()

        # Build translation types list based on user selection
        translation_types = []
        if markdown:
            translation_types.append("markdown")
        if images:
            translation_types.append("images")
        if notebook:
            translation_types.append("notebook")

        # Default: translate all supported file types if nothing specified
        if not translation_types:
            translation_types = ["markdown", "notebook", "images"]

        # Check Azure AI Service availability if images are included
        if "images" in translation_types:
            cv_available = VisionConfig.check_configuration()
            if not cv_available:
                raise click.ClickException(
                    "Image translation is enabled but Azure AI Service is not configured.\n"
                    "Please add AZURE_AI_SERVICE_API_KEY to your environment variables or use --markdown and/or --notebook flags to exclude images.\n"
                    "See the .env.template file for required variables."
                )

        # Log selected translation mode
        mode_msg = f"🚀 Translation mode: {', '.join(translation_types)}"
        click.echo(mode_msg)

        # Validate root directory early and set up logging
        root_path = Path(root_dir).resolve()
        if not root_path.exists():
            raise click.ClickException(f"Root directory does not exist: {root_dir}")
        if not root_path.is_dir():
            raise click.ClickException(f"Root path is not a directory: {root_dir}")

        log_file_path = setup_logging(
            root_path, debug=debug, save_logs=save_logs, command_name="translate"
        )
        if debug:
            logging.debug("Debug mode enabled.")
        if save_logs and log_file_path is not None:
            click.echo(f"📄 Logs will be saved to: {log_file_path}")

        # Now run the LLM health check; raises on failure
        LLMConfig.validate_connectivity()
        logger.info("LLM health check passed.")
        click.echo("✅ LLM health check passed.")

        # If images are selected, validate Vision connectivity as well
        if "images" in translation_types:
            # Vision health check; raises on failure
            VisionConfig.validate_connectivity()
            logger.info("Vision health check passed.")
            click.echo("✅ Vision health check passed.")

        # Show warning if 'all' is selected
        all_languages_selected = language_codes == "all"
        if all_languages_selected:
            click.echo(
                "Warning: Translating all languages at once can take a significant amount of time, especially when dealing with large markdown-based open-source projects that have many documents."
            )
            click.echo(
                "For better efficiency, it's recommended that contributors handle individual languages and upload their translations separately."
            )
            # Option to proceed or not
            if not yes:
                confirmation_all = click.prompt(
                    "Do you still want to proceed with translating all languages? Type 'yes' to continue",
                    type=str,
                )

                if confirmation_all.lower() != "yes":
                    click.echo("Translation for 'all' languages cancelled.")
                    return
                else:
                    click.echo("Proceeding with translation for all languages...")
            else:
                click.echo("Auto-confirming translation for all languages...")

            try:
                with importlib.resources.path(
                    "co_op_translator.fonts", "font_language_mappings.yml"
                ) as mappings_path:
                    with open(mappings_path, "r", encoding="utf-8") as file:
                        font_mappings = yaml.safe_load(file)
                        if not font_mappings:
                            raise click.ClickException("Empty font mappings file")
                        language_codes = " ".join(
                            [
                                lang_code
                                for lang_code in font_mappings
                                if isinstance(font_mappings[lang_code], dict)
                            ]
                        )
                        if not language_codes:
                            raise click.ClickException(
                                "No valid language codes found in font mappings"
                            )
                        logging.debug(
                            f"Loaded language codes from font mapping: {language_codes}"
                        )
            except (FileNotFoundError, yaml.YAMLError) as e:
                raise click.ClickException(f"Failed to load font mappings: {str(e)}")

        # Show warning and prompt if update is selected
        if update:
            click.echo(
                f"Warning: The update command will delete all existing translations for '{language_codes}' and re-translate everything."
            )
            if not yes:
                confirmation_update = click.prompt(
                    "Do you want to continue? Type 'yes' to proceed", type=str
                )

                if confirmation_update.lower() != "yes":
                    click.echo("Update cancelled by user.")
                    return
                else:
                    click.echo("Proceeding with update...")
            else:
                click.echo("Auto-confirming update operation...")

        # Initialize ProjectTranslator with determined settings
        translator = ProjectTranslator(
            language_codes,
            root_dir,
            translation_types=translation_types,
            add_disclaimer=add_disclaimer,
        )

        # Update README shared sections BEFORE translation
        readme_path = root_path / "README.md"
        try:
            if all_languages_selected:
                if update_readme_languages_table(readme_path):
                    click.echo("✅ Updated README languages table from template.")
                else:
                    click.echo(
                        "ℹ️ README languages table not updated (markers missing or template unavailable)."
                    )
        except Exception as e:
            logger.warning(f"Failed to update README languages table: {e}")

        try:
            if update_readme_other_courses(readme_path):
                click.echo("✅ Updated README 'Other courses' section from template.")
        except Exception as e:
            logger.warning(f"Failed to update README 'Other courses': {e}")

        if fix:
            click.echo(f"Fixing translations with confidence below {min_confidence}...")

            # Fix is only applicable to markdown files, not images
            if images and not markdown:
                click.echo("Note: --fix only applies to markdown files, not images.")

            # Handle language codes
            if language_codes.lower() == "all":
                lang_list = Config.get_language_codes()
            else:
                lang_list = [code.strip() for code in language_codes.split()]

            total_retranslated = 0
            total_errors = 0

            for lang_code in lang_list:

                logger.info(f"Processing language: {lang_code}")

                try:
                    retranslated_count, errors = asyncio.run(
                        translator.retranslate_low_confidence_files(
                            lang_code, min_confidence
                        )
                    )

                    total_retranslated += retranslated_count
                    total_errors += len(errors)

                    if retranslated_count > 0:
                        logger.info(
                            f"{retranslated_count} files were retranslated successfully"
                        )
                    else:
                        logger.info(
                            f"No files with confidence below {min_confidence} were found or needed retranslation"
                        )

                    if errors:
                        logger.warning(
                            f"Errors during retranslation: {len(errors)} errors"
                        )
                        for error in errors:
                            logger.error(f"Error detail: {error}")
                except Exception as e:
                    logger.error(f"Error processing {lang_code}: {str(e)}")

            click.echo(f"\n{click.style('Summary:', fg='blue', bold=True)}")
            click.echo(
                f"Total files retranslated: {click.style(str(total_retranslated), fg='green')}"
            )
            if total_errors > 0:
                click.echo(f"Total errors: {click.style(str(total_errors), fg='red')}")

            logger.info(
                f"Project translation completed for languages: {language_codes}"
            )

        else:
            # Call translate_project with determined settings
            translator.translate_project(
                update=update,
                fast_mode=fast,
            )

            logger.info(
                f"Project translation completed for languages: {language_codes}"
            )

    except Exception as e:
        if debug:
            logger.exception("An error occurred during translation")
        raise click.ClickException(str(e))
