"""
Evaluate command implementation for Co-op Translator CLI.
"""

import asyncio
import logging
import click
from pathlib import Path

from co_op_translator.core.project.project_evaluator import ProjectEvaluator
from co_op_translator.config.base_config import Config
from co_op_translator.utils.common.logging_utils import setup_logging
from co_op_translator.utils.common.lang_utils import normalize_language_code
from co_op_translator.utils.common.progress import get_progress_reporter

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
    reporter = get_progress_reporter()

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
            reporter.info(f"Logs will be saved to: {log_file_path}")

        # Normalize to canonical BCP 47 (accept alias input like tw/cn/br)
        canonical_code = normalize_language_code(language_code)

        # Create evaluator
        # Determine evaluation mode (fast, deep or default mode)
        if fast and deep:
            reporter.warning(
                "Both --fast and --deep flags specified. Using default mode "
                "(both rule-based and LLM)."
            )
            use_rule = True
            use_llm = True
            mode_label = "default"
        elif fast:
            use_rule = True
            use_llm = False
            mode_label = "fast"
        elif deep:
            use_rule = False
            use_llm = True
            mode_label = "deep"
        else:
            use_rule = True
            use_llm = True
            mode_label = "default"

        reporter.header(
            command="evaluate",
            root_dir=root_path,
            languages=canonical_code,
            modes=[mode_label],
        )
        reporter.info(f"Evaluating {canonical_code} translations in {root_path}...")

        evaluator = ProjectEvaluator(
            root_dir=root_path,
            translations_dir=root_path / "translations",
            language_codes=[canonical_code],
            excluded_dirs=["node_modules", ".git", "__pycache__", "venv"],
            use_llm=use_llm,
            use_rule=use_rule,
        )

        # Run evaluation
        total_files, issue_files, avg_confidence = asyncio.run(
            evaluator.evaluate_project(canonical_code)
        )

        reporter.key_value_summary(
            title="Evaluation Complete",
            rows=[
                ("Total files evaluated", str(total_files)),
                ("Files with potential issues", str(issue_files)),
                ("Average confidence score", f"{avg_confidence:.2f}"),
            ],
            fallback_lines=[
                "Evaluation Complete",
                f"Total files evaluated: {total_files}",
                f"Files with potential issues: {issue_files}",
                f"Average confidence score: {avg_confidence:.2f}",
            ],
        )

        # Get low confidence translations
        low_confidence = asyncio.run(
            evaluator.get_low_confidence_translations(canonical_code, min_confidence)
        )

        if low_confidence:
            reporter.print(
                "\n[bold yellow]Files with potential issues[/bold yellow] "
                f"(confidence below {min_confidence}):"
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
                    if rel_path.startswith(f"translations/{canonical_code}/"):
                        display_path = f"./{rel_path}"
                    else:
                        display_path = f"./translations/{canonical_code}/{rel_path}"
                except ValueError:
                    display_path = str(file_path).replace("\\", "/")

                # Read centralized metadata to get issues for reference
                try:
                    from co_op_translator.utils.common.metadata_utils import (
                        read_text_metadata_for_source,
                        extract_metadata_from_content,
                    )

                    trans_path = Path(file_path)
                    lang_dir = root_path / "translations" / canonical_code
                    try:
                        rel = trans_path.resolve().relative_to(lang_dir)
                        orig_path = root_path / rel
                    except Exception:
                        orig_path = None

                    metadata = {}
                    if orig_path is not None:
                        metadata = read_text_metadata_for_source(lang_dir, orig_path)
                    if not metadata:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                        metadata = extract_metadata_from_content(content)

                    issues = []
                    if metadata and "evaluation" in metadata:
                        # Only check issues field
                        issues = metadata["evaluation"].get("issues", [])

                    reporter.print(f"\n- {display_path}", markup=False)
                    reporter.print(f"  Score: {confidence:.2f}")

                    # Show issues as reference information if available
                    if issues:
                        reporter.print("  Issues found:")
                        for issue in issues:
                            reporter.print(f"    - {issue}", markup=False)
                    else:
                        reporter.print(
                            "  No specific issues identified, but confidence score is low"
                        )
                except Exception as e:
                    logger.error(f"Error reading issues from {file_path}: {e}")

            reporter.print("")  # Add empty line for better readability
        elif issue_files > 0:
            reporter.warning(
                "Files with issues were found during evaluation, but none fall "
                f"below the confidence threshold of {min_confidence}."
            )
            reporter.info(
                "Consider running with a higher threshold: "
                f"evaluate -l {canonical_code} --min-confidence 0.9"
            )

        else:
            reporter.success("All translations look good.")

        logger.info(f"Evaluation completed for language: {canonical_code}")

    except Exception as e:
        if debug:
            logger.exception("An error occurred during evaluation")
        raise click.ClickException(str(e))
