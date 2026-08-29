import json
import os
from pathlib import Path
import subprocess
import sys

import pytest

PROVIDER_ENV_PREFIXES = ("AZURE_OPENAI_", "AZURE_AI_SERVICE_", "OPENAI_")
PROVIDER_ENV_NAMES = {"AZURE_SUBSCRIPTION_KEY"}


@pytest.fixture
def credential_free_env() -> dict[str, str]:
    env = {
        key: value
        for key, value in os.environ.items()
        if key not in PROVIDER_ENV_NAMES
        and not any(key.startswith(prefix) for prefix in PROVIDER_ENV_PREFIXES)
    }
    repo_dir = Path(__file__).resolve().parents[2]
    source_dir = repo_dir / "src"
    test_support_dir = repo_dir / "tests" / "subprocess_no_credentials"
    existing_pythonpath = env.get("PYTHONPATH")
    env["PYTHONPATH"] = os.pathsep.join([str(test_support_dir), str(source_dir)])
    if existing_pythonpath:
        env["PYTHONPATH"] += os.pathsep + existing_pythonpath
    return env


@pytest.fixture
def sample_project(tmp_path: Path) -> Path:
    (tmp_path / "README.md").write_text("# Sample\n", encoding="utf-8")
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "guide.md").write_text("# Guide\n\nHello.\n", encoding="utf-8")
    return tmp_path


def _run_python(
    arguments: list[str],
    *,
    env: dict[str, str],
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *arguments],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
        timeout=60,
    )


def _assert_no_dry_run_outputs(root_dir: Path) -> None:
    assert not (root_dir / "translations").exists()
    assert not (root_dir / "translated_images").exists()
    assert not (root_dir / "logs").exists()


def _project_snapshot(root_dir: Path) -> dict[str, bytes]:
    return {
        path.relative_to(root_dir).as_posix(): path.read_bytes()
        for path in root_dir.rglob("*")
        if path.is_file()
    }


def test_cli_dry_run_does_not_require_credentials_or_write_files(
    sample_project: Path,
    credential_free_env: dict[str, str],
):
    before = _project_snapshot(sample_project)
    events_path = sample_project / "events.ndjson"
    result = _run_python(
        [
            "-m",
            "co_op_translator",
            "-l",
            "all",
            "-r",
            str(sample_project),
            "--dry-run",
            "--update",
            "--save-logs",
            "--json-events",
            str(events_path),
        ],
        env=credential_free_env,
    )

    assert result.returncode == 0, result.stderr
    assert "Estimated tokens before translation:" in result.stdout
    assert "Dry run complete: no changes made." in result.stdout
    _assert_no_dry_run_outputs(sample_project)
    assert not events_path.exists()
    assert _project_snapshot(sample_project) == before


def test_api_dry_run_does_not_require_credentials_or_write_files(
    sample_project: Path,
    credential_free_env: dict[str, str],
):
    before = _project_snapshot(sample_project)
    events_path = sample_project / "events.ndjson"
    script = (
        "from co_op_translator.api import run_translation; "
        f"run_translation(language_codes='ko', root_dir={str(sample_project)!r}, "
        "readme_only=True, dry_run=True, save_logs=True, "
        f"json_events_path={str(events_path)!r})"
    )

    result = _run_python(["-c", script], env=credential_free_env)

    assert result.returncode == 0, result.stderr
    assert "Estimated translation volume before translation:" in result.stdout
    assert "Dry run complete: no changes made." in result.stdout
    _assert_no_dry_run_outputs(sample_project)
    assert not events_path.exists()
    assert _project_snapshot(sample_project) == before


def test_cli_dry_run_rejects_unestimated_fix_mode(
    sample_project: Path,
    credential_free_env: dict[str, str],
):
    before = _project_snapshot(sample_project)
    result = _run_python(
        [
            "-m",
            "co_op_translator",
            "-l",
            "ko",
            "-r",
            str(sample_project),
            "--markdown",
            "--fix",
            "--dry-run",
        ],
        env=credential_free_env,
    )

    assert result.returncode != 0
    assert "--fix cannot be combined with --dry-run" in result.stderr
    assert _project_snapshot(sample_project) == before


def test_api_image_dry_run_skips_vision_credentials(
    sample_project: Path,
    credential_free_env: dict[str, str],
):
    before = _project_snapshot(sample_project)
    script = (
        "from co_op_translator.api import run_translation; "
        f"run_translation(language_codes='all', root_dir={str(sample_project)!r}, "
        "images=True, dry_run=True, save_logs=True)"
    )

    result = _run_python(["-c", script], env=credential_free_env)

    assert result.returncode == 0, result.stderr
    assert "Dry run complete: no changes made." in result.stdout
    _assert_no_dry_run_outputs(sample_project)
    assert _project_snapshot(sample_project) == before


def test_mcp_dry_run_does_not_require_credentials_or_write_files(
    sample_project: Path,
    credential_free_env: dict[str, str],
):
    before = _project_snapshot(sample_project)
    script = (
        "import anyio, json, os, sys\n"
        "from mcp import ClientSession, StdioServerParameters\n"
        "from mcp.client.stdio import stdio_client\n"
        "async def main():\n"
        " params = StdioServerParameters(command=sys.executable, "
        "args=['-m', 'co_op_translator.mcp.server', '--transport', 'stdio'], "
        "env=dict(os.environ));\n"
        " async with stdio_client(params) as (read, write):\n"
        "  async with ClientSession(read, write) as session:\n"
        "   await session.initialize();\n"
        "   result = await session.call_tool('run_translation', arguments={"
        "'language_codes': 'ko', "
        f"'root_dir': {str(sample_project)!r}, "
        "'markdown': True, 'dry_run': True, 'save_logs': True});\n"
        "   print(json.dumps(result.model_dump(mode='json')));\n"
        "anyio.run(main)"
    )

    result = _run_python(["-c", script], env=credential_free_env)

    assert result.returncode == 0, result.stderr
    envelope = json.loads(result.stdout)
    assert envelope["isError"] is False
    payload = json.loads(envelope["content"][0]["text"])
    assert payload["ok"] is True
    assert payload["dry_run"] is True
    assert "Dry run complete: no changes made." in payload["stdout"]
    assert payload["events"]
    assert any(event["type"] == "run_completed" for event in payload["events"])
    assert all(event["type"] != "run_failed" for event in payload["events"])
    _assert_no_dry_run_outputs(sample_project)
    assert _project_snapshot(sample_project) == before
