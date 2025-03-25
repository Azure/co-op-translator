import asyncio
import logging
import click
import importlib.resources
import yaml
from co_op_translator.core.project.project_translator import ProjectTranslator
from co_op_translator.config.base_config import Config
from co_op_translator.config.vision_config.config import VisionConfig
import os
from pathlib import Path

logger = logging.getLogger(__name__)


@click.command()
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
@click.option("--debug", "-d", is_flag=True, help="Enable debug mode.")
@click.option(
    "--check",
    "-chk",
    is_flag=True,
    help="Check translated files for errors and retry translation if needed.",
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
def main(language_codes, root_dir, update, images, markdown, debug, check, fast, yes):
    """
    CLI for translating project files.

    Usage examples:

    1. Default behavior (add new translations without deleting existing ones):
       translate -l "ko"
       translate -l "es fr de" -r "./my_project"

    2. Add only new Korean image translations (no existing translations are deleted):
       translate -l "ko" -img

    3. Update all Korean translations (Warning: This deletes all existing Korean translations before re-translating):
       translate -l "ko" -u

    4. Update only Korean images (Warning: This deletes all existing Korean images before re-translating):
       translate -l "ko" -img -u

    5. Add new markdown translations for Korean without affecting other translations:
       translate -l "ko" -md

    6. Check translated files for errors and retry translations if necessary:
       translate -l "ko" -chk

    7. Check translated files for errors and retry translations (only markdown):
       translate -l "ko" -chk -md

    8. Check translated files for errors and retry translations (only images):
       translate -l "ko" -chk -img

    9. Use fast mode for image translation:
       translate -l "ko" -img -f

    Debug mode example:
    - translate -l "ko" -d: Enable debug logging.
    """

    try:
        # Check that the required environment variables are set
        Config.check_configuration()

        # Initialize translation mode
        cv_available = VisionConfig.check_configuration()

        # Determine translation mode based on flags and CV availability
        if not images and not markdown:
            # Default: translate both if possible
            markdown = True
            images = cv_available
        elif images and not cv_available:
            # User requested images but CV not available
            images = False
            click.echo(
                "Computer Vision is not configured: Image translation will be disabled."
            )
            click.echo(
                "To enable image translation, please add Computer Vision credentials to your environment variables."
            )
            click.echo("See the .env.template file for required variables.")

        # Log selected translation mode
        mode_msg = "🚀 Translation mode: "
        if markdown and images:
            mode_msg += "markdown and images"
        elif markdown:
            mode_msg += "markdown only"
        elif images:
            mode_msg += "images only"
        click.echo(mode_msg)

        if debug:
            logging.basicConfig(level=logging.DEBUG)
            logging.debug("Debug mode enabled.")
        else:
            logging.basicConfig(level=logging.CRITICAL)

        # Validate root directory
        root_path = Path(root_dir).resolve()
        if not root_path.exists():
            raise click.ClickException(f"Root directory does not exist: {root_dir}")
        if not root_path.is_dir():
            raise click.ClickException(f"Root path is not a directory: {root_dir}")
        if not os.access(root_path, os.R_OK | os.W_OK):
            raise click.ClickException(
                f"Insufficient permissions for directory: {root_dir}"
            )

        # Show warning if 'all' is selected
        if language_codes == "all":
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
            language_codes, root_dir, markdown_only=markdown and not images
        )

        if check:
            # Call check_and_retry_translations if --check is passed
            click.echo(f"Checking translated files for errors in {language_codes}...")
            asyncio.run(translator.check_and_retry_translations())
        else:
            # Call translate_project with determined settings
            translator.translate_project(
                images=images, markdown=markdown, update=update, fast_mode=fast
            )

        logger.info(f"Project translation completed for languages: {language_codes}")

    except Exception as e:
        if debug:
            logger.exception("An error occurred during translation")
        raise click.ClickException(str(e))


if __name__ == "__main__":
    main()
