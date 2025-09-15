"""
Evaluate command implementation for Co-op Translator CLI.
"""

import asyncio
import logging
import click
from pathlib import Path
import os

from co_op_translator.core.project.project_evaluator import ProjectEvaluator
from co_op_translator.config.base_config import Config
from co_op_translator.utils.common.logging_utils import setup_logging

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
@click.option(
    "--save-logs",
    "-s",
    is_flag=True,
    help="Save logs to the logs/ directory under --root-dir (always at DEBUG level).",
)
@click.option(
    "--fast",
    "-f",
    is_flag=True,
    help="Fast mode: Use only rule-based evaluation without LLM. Faster but less accurate.",
)
@click.option(
    "--deep",
    "-D",
    is_flag=True,
    help="Deep mode: Use only LLM-based evaluation without basic rules. More accurate but slower.",
)
def evaluate_command(
    language_code, root_dir, min_confidence, debug, fast, deep, save_logs
):
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

        # Validate root directory and set up logging
        root_path = Path(root_dir).resolve()
        if not root_path.exists():
            raise click.ClickException(f"Root directory does not exist: {root_dir}")
        if not root_path.is_dir():
            raise click.ClickException(f"Root path is not a directory: {root_dir}")

        log_file_path = setup_logging(
            root_path, debug=debug, save_logs=save_logs, command_name="evaluate"
        )
        if debug:
            logging.debug("Debug mode enabled.")
        if save_logs and log_file_path is not None:
            click.echo(f"📄 Logs will be saved to: {log_file_path}")

        click.echo(f"Evaluating {language_code} translations in {root_path}...")

        # Create evaluator
        # Determine evaluation mode (fast, deep or default mode)
        if fast and deep:
            click.echo(
                "Warning: Both --fast and --deep flags specified. Using default mode (both rule-based and LLM)."
            )
            use_rule = True
            use_llm = True
        elif fast:
            click.echo("Using FAST mode: Rule-based evaluation only (no LLM)")
            use_rule = True
            use_llm = False
        elif deep:
            click.echo(
                "Using DEEP mode: LLM-based evaluation only (more thorough but slower)"
            )
            use_rule = False
            use_llm = True
        else:
            click.echo("Using DEFAULT mode: Both rule-based and LLM evaluation")
            use_rule = True
            use_llm = True

        evaluator = ProjectEvaluator(
            root_dir=root_path,
            translations_dir=root_path / "translations",
            language_codes=[language_code],
            excluded_dirs=["node_modules", ".git", "__pycache__", "venv"],
            use_llm=use_llm,
            use_rule=use_rule,
        )

        # Run evaluation
        total_files, issue_files, avg_confidence = asyncio.run(
            evaluator.evaluate_project(language_code)
        )

        # Display results with color highlighting
        click.echo(f"\n{click.style('Evaluation Complete', fg='green', bold=True)}\n")
        click.echo(f"Total files evaluated: {click.style(str(total_files), fg='blue')}")

        # Color-code the issue count based on severity
        issue_color = "red" if issue_files > 0 else "green"
        click.echo(
            f"Files with potential issues: {click.style(str(issue_files), fg=issue_color, bold=issue_files > 0)}"
        )

        # Color-code the confidence score
        conf_color = (
            "green"
            if avg_confidence >= 0.9
            else "yellow" if avg_confidence >= 0.8 else "red"
        )
        click.echo(
            f"Average confidence score: {click.style(f'{avg_confidence:.2f}', fg=conf_color)}"
        )

        # Get low confidence translations
        low_confidence = asyncio.run(
            evaluator.get_low_confidence_translations(language_code, min_confidence)
        )

        if low_confidence:
            click.echo(
                f"\n{click.style('Files with potential issues', fg='yellow', bold=True)} (confidence below {min_confidence}):"
            )

            # Sort by confidence score (lowest first)
            low_confidence.sort(key=lambda x: x[1])

            for file_path, confidence in low_confidence:
                # Try to show relative path rather than absolute path
                try:
                    # Get full relative path from project root
                    rel_path = str(Path(file_path).relative_to(root_path)).replace(
                        "\\", "/"
                    )

                    # Check if the path already contains translations/language_code
                    # to avoid duplication
                    if rel_path.startswith(f"translations/{language_code}/"):
                        display_path = f"./{rel_path}"
                    else:
                        display_path = f"./translations/{language_code}/{rel_path}"
                except ValueError:
                    display_path = str(file_path).replace("\\", "/")

                # Read file to get issues for reference
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    from co_op_translator.utils.common.metadata_utils import (
                        extract_metadata_from_content,
                    )

                    metadata = extract_metadata_from_content(content)
                    issues = []
                    if metadata and "evaluation" in metadata:
                        # Only check issues field
                        issues = metadata["evaluation"].get("issues", [])

                    # Display file with confidence score
                    conf_color = (
                        "green"
                        if confidence >= 0.9
                        else "yellow" if confidence >= 0.8 else "red"
                    )
                    click.echo(f"\n- {click.style(display_path, bold=True)}")
                    click.echo(
                        f"  Score: {click.style(f'{confidence:.2f}', fg=conf_color)}"
                    )

                    # Show issues as reference information if available
                    if issues:
                        click.echo(f"  Issues found:")
                        for issue in issues:
                            click.echo(f"    - {issue}")
                    else:
                        click.echo(
                            f"  No specific issues identified, but confidence score is low"
                        )
                except Exception as e:
                    logger.error(f"Error reading issues from {file_path}: {e}")

            click.echo("")  # Add empty line for better readability
        elif issue_files > 0:
            click.echo(
                f"\n{click.style('Note:', fg='yellow')} Files with issues were found during evaluation, but none fall below the confidence threshold of {min_confidence}."
            )
            click.echo(
                f"Consider running with a higher threshold: {click.style(f'evaluate -l {language_code} --min-confidence 0.9', bold=True)}"
            )

        else:
            click.echo(
                f"\n{click.style('✓ All translations look good!', fg='green', bold=True)}"
            )

        logger.info(f"Evaluation completed for language: {language_code}")

    except Exception as e:
        if debug:
            logger.exception("An error occurred during evaluation")
        raise click.ClickException(str(e))
