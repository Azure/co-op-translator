import io
import sys

from co_op_translator.utils.common.console import configure_safe_console_output


def test_configure_safe_console_output_prevents_cp949_encode_errors(monkeypatch):
    raw_stdout = io.BytesIO()
    raw_stderr = io.BytesIO()
    stdout = io.TextIOWrapper(raw_stdout, encoding="cp949", errors="strict")
    stderr = io.TextIOWrapper(raw_stderr, encoding="cp949", errors="strict")

    monkeypatch.setattr(sys, "stdout", stdout)
    monkeypatch.setattr(sys, "stderr", stderr)

    configure_safe_console_output()

    sys.stdout.write("🚀 Translation mode: markdown\n")
    sys.stderr.write("✅ LLM health check passed.\n")
    sys.stdout.flush()
    sys.stderr.flush()

    assert b"Translation mode" in raw_stdout.getvalue()
    assert b"LLM health check passed" in raw_stderr.getvalue()
