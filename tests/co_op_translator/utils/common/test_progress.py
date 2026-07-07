import io
import logging

from rich.console import Console

from co_op_translator.utils.common.progress import ProgressReporter


def test_rich_header_renders_compact_command_context():
    stream = io.StringIO()
    console = Console(
        file=stream,
        force_terminal=True,
        color_system=None,
        width=100,
    )
    reporter = ProgressReporter(console=console, output_style="rich")

    reporter.header(
        command="translate",
        root_dir="C:/repo",
        languages=["ko", "ja"],
        modes=["markdown", "notebook"],
    )

    output = stream.getvalue()

    assert "Co-op Translator" in output
    assert "Command" in output
    assert "translate" in output
    assert "ko, ja" in output
    assert "markdown, notebook" in output


def test_plain_header_renders_single_line_context():
    stream = io.StringIO()
    console = Console(file=stream, force_terminal=False, color_system=None)
    reporter = ProgressReporter(console=console, output_style="plain")

    reporter.header(
        command="translate",
        root_dir="C:/repo",
        languages=["ko", "ja"],
        modes=["markdown"],
    )

    output = stream.getvalue()

    assert "Co-op Translator | Command: translate" in output
    assert "Target: ko, ja" in output
    assert output.isascii()


def test_plain_estimate_summary_uses_fallback_without_emoji():
    stream = io.StringIO()
    console = Console(file=stream, force_terminal=False, color_system=None)
    reporter = ProgressReporter(console=console, output_style="plain")

    reporter.estimate_summary(
        title="Estimated Translation Volume",
        total_tokens=130,
        total_words=80,
        rows=[("Translation: markdown", 130)],
        fallback=(
            "Estimated translation volume before translation: 130 tokens "
            "(80 words) (breakdown: translation: markdown: 130)"
        ),
    )

    output = stream.getvalue()

    assert "Estimated translation volume before translation" in output
    assert output.isascii()


def test_plain_task_summary_omits_empty_detail():
    stream = io.StringIO()
    console = Console(file=stream, force_terminal=False, color_system=None)
    reporter = ProgressReporter(console=console, output_style="plain")

    with reporter.task("Cleaning orphaned files", total=1, unit="step") as task:
        task.set_detail("None")
        task.update()

    output = stream.getvalue()

    assert "Done: Cleaning orphaned files (1/1 step)" in output
    assert "None" not in output


def test_reporter_mirrors_user_facing_output_to_file_logs(tmp_path):
    stream = io.StringIO()
    console = Console(
        file=stream,
        force_terminal=True,
        color_system=None,
        width=100,
    )
    reporter = ProgressReporter(console=console, output_style="rich")

    root_logger = logging.getLogger()
    original_handlers = list(root_logger.handlers)
    original_level = root_logger.level
    log_path = tmp_path / "output.log"
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setFormatter(logging.Formatter("%(message)s"))

    try:
        for handler in original_handlers:
            root_logger.removeHandler(handler)
        root_logger.setLevel(logging.DEBUG)
        root_logger.addHandler(file_handler)

        reporter.header(
            command="translate",
            root_dir="C:/repo",
            languages="ko",
            modes=["markdown"],
        )
        reporter.success("LLM health check passed.")
        reporter.estimate_summary(
            title="Estimated Translation Volume",
            total_tokens=130,
            total_words=80,
            rows=[("Translation: markdown", 130)],
            fallback=(
                "Estimated translation volume before translation: 130 tokens "
                "(80 words)"
            ),
        )
    finally:
        file_handler.flush()
        file_handler.close()
        root_logger.removeHandler(file_handler)
        for handler in original_handlers:
            root_logger.addHandler(handler)
        root_logger.setLevel(original_level)

    output = log_path.read_text(encoding="utf-8")

    assert "Co-op Translator | Command: translate" in output
    assert "Done: LLM health check passed." in output
    assert "Estimated translation volume before translation" in output
