import asyncio
import logging
import click
import importlib.resources
import yaml
from co_op_translator.translators.project_translator import ProjectTranslator

logger = logging.getLogger(__name__)

@click.command()
@click.option('--language-codes', '-l', required=True, help='Space-separated language codes for translation (e.g., "es fr de" or "all").')
@click.option('--root-dir', '-r', default='.', help='Root directory of the project (default is current directory).')
@click.option('--add', '-a', is_flag=True, default=True, help='Add new translations without deleting existing ones (default behavior).')
@click.option('--update', '-u', is_flag=True, help='Update translations by deleting and recreating them (Warning: Existing translations will be lost).')
@click.option('--images', '-img', is_flag=True, help='Only translate image files.')
@click.option('--markdown', '-md', is_flag=True, help='Only translate markdown files.')
@click.option('--debug', '-d', is_flag=True, help='Enable debug mode.')
@click.option('--check', '-chk', is_flag=True, help='Check translated files for errors and retry translation if needed.')
def main(language_codes, root_dir, add, update, images, markdown, debug, check):
    """
    CLI for translating project files.

    Usage examples:

    1. Default behavior (add new translations without deleting existing ones):
       translate -l "ko"
       translate -l "es fr de" -r "./my_project"

    2. Add only new Korean image translations (no existing translations are deleted):
       translate -l "ko" -img -a

    3. Update all Korean translations (Warning: This deletes all existing Korean translations before re-translating):
       translate -l "ko" -u

    4. Update only Korean images (Warning: This deletes all existing Korean images before re-translating):
       translate -l "ko" -img -u

    5. Add new markdown translations for Korean without affecting other translations:
       translate -l "ko" -md -a

    6. Check translated files for errors and retry translations if necessary:
       translate -l "ko" -chk

    7. Check translated files for errors and retry translations (only markdown):
       translate -l "ko" -chk -md

    8. Check translated files for errors and retry translations (only images):
       translate -l "ko" -chk -img

    Debug mode example:
    - translate -l "ko" -d: Enable debug logging.
    """

    if debug:
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("Debug mode enabled.")
    else:
        logging.basicConfig(level=logging.CRITICAL)

    # Show warning if 'all' is selected
    if language_codes == "all":
        click.echo("Warning: Translating all languages at once can take a significant amount of time, especially when dealing with large markdown-based open-source projects that have many documents.")
        click.echo("For better efficiency, it's recommended that contributors handle individual languages and upload their translations separately.")
        # Option to proceed or not
        confirmation_all = click.prompt("Do you still want to proceed with translating all languages? Type 'yes' to continue", type=str)
        
        if confirmation_all.lower() != 'yes':
            click.echo("Translation for 'all' languages cancelled.")
            return
        else:
            click.echo("Proceeding with translation for all languages...")

    # Show warning and prompt if update is selected
    if update:
        click.echo(f"Warning: The update command will delete all existing translations for '{language_codes}' and re-translate everything.")
        confirmation_update = click.prompt("Do you want to continue? Type 'yes' to proceed", type=str)
        
        if confirmation_update.lower() != 'yes':
            click.echo("Update cancelled by user.")
            return
        else:
            click.echo("Proceeding with update...")

    # Language code parsing logic
    if language_codes == "all":
        with importlib.resources.path('co_op_translator.fonts', 'font_language_mappings.yml') as mappings_path:
            with open(mappings_path, 'r', encoding='utf-8') as file:
                font_mappings = yaml.safe_load(file)
                language_codes = " ".join([lang_code for lang_code in font_mappings if isinstance(font_mappings[lang_code], dict)])
                logging.debug(f"Loaded language codes from font mapping: {language_codes}")

    # Initialize ProjectTranslator
    translator = ProjectTranslator(language_codes, root_dir)

    if check:
        # Call check_and_retry_translations if --check is passed
        click.echo(f"Checking translated files for errors in {language_codes}...")
        asyncio.run(translator.check_and_retry_translations())
    else:
        # Call translate_project
        translator.translate_project(images=images, markdown=markdown, update=update)

    logger.info(f"Project translation completed for languages: {language_codes}")

if __name__ == '__main__':
    main()
