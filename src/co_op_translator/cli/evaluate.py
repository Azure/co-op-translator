"""
Evaluate command implementation for Co-op Translator CLI.
"""

import asyncio
import logging
import click
from pathlib import Path

from co_op_translator.core.project.project_evaluator import ProjectEvaluator
from co_op_translator.config.base_config import Config

logger = logging.getLogger(__name__)


@click.command(name="evaluate")
@click.option(
    "--language-code",
    "-l",
    required=True,
    help='Language code to evaluate translations for (e.g., "es").',
)
@click.option(
    "--root-dir",
    "-r",
    default=".",
    help="Root directory of the project (default is current directory).",
)
@click.option(
    "--min-confidence",
    "-c",
    default=0.7,
    type=float,
    help="Minimum confidence threshold (0.0-1.0) for identifying low confidence translations.",
)
@click.option("--debug", "-d", is_flag=True, help="Enable debug mode.")
def evaluate_command(language_code, root_dir, min_confidence, debug):
    """
    Evaluate translation quality for a specific language.

    This command analyzes translated files and provides confidence scores and identified issues.

    Usage examples:

    1. Evaluate Korean translations:
       evaluate -l "ko"

    2. Evaluate Spanish translations with custom confidence threshold:
       evaluate -l "es" -c 0.8

    3. Evaluate French translations in a specific directory:
       evaluate -l "fr" -r "./my_project"
    """

    try:
        # Check that the required environment variables are set
        Config.check_configuration()

        if debug:
            logging.basicConfig(level=logging.DEBUG)
            logging.debug("Debug mode enabled.")
        else:
            logging.basicConfig(level=logging.INFO)

        # Validate root directory
        root_path = Path(root_dir).resolve()
        if not root_path.exists():
            raise click.ClickException(f"Root directory does not exist: {root_dir}")
        if not root_path.is_dir():
            raise click.ClickException(f"Root path is not a directory: {root_dir}")

        click.echo(f"Evaluating {language_code} translations in {root_path}...")

        # Create evaluator
        evaluator = ProjectEvaluator(
            root_dir=root_path,
            translations_dir=root_path / "translations",
            language_codes=[language_code],
            excluded_dirs=["node_modules", ".git", "__pycache__", "venv"],
        )

        # Run evaluation
        total_files, issue_files, avg_confidence = asyncio.run(
            evaluator.evaluate_project(language_code)
        )

        # Display results
        click.echo(f"\nEvaluation Complete:\n")
        click.echo(f"Total files evaluated: {total_files}")
        click.echo(f"Files with potential issues: {issue_files}")
        click.echo(f"Average confidence score: {avg_confidence:.2f}")

        if issue_files > 0:
            # Get low confidence translations
            low_confidence = asyncio.run(
                evaluator.get_low_confidence_translations(language_code, min_confidence)
            )

            if low_confidence:
                click.echo(f"\nLow confidence translations (below {min_confidence}):")
                for file_path, confidence in low_confidence:
                    click.echo(f" - {file_path} (Score: {confidence:.2f})")

        logger.info(f"Evaluation completed for language: {language_code}")

    except Exception as e:
        if debug:
            logger.exception("An error occurred during evaluation")
        raise click.ClickException(str(e))
