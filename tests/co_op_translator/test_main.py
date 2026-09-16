import importlib
import os
from pathlib import Path
import subprocess
import sys
from types import ModuleType
from unittest.mock import Mock

import pytest

COMMAND_MODULES = {
    "translate": ("co_op_translator.cli.translate", "translate_command"),
    "evaluate": ("co_op_translator.cli.evaluate", "evaluate_command"),
    "migrate-links": (
        "co_op_translator.cli.migrate_links",
        "migrate_links_command",
    ),
    "co-op-review": ("co_op_translator.cli.review", "review_command"),
}

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


def _reload_main(monkeypatch):
    monkeypatch.delitem(sys.modules, "co_op_translator.__main__", raising=False)
    for module_name, _ in COMMAND_MODULES.values():
        monkeypatch.delitem(sys.modules, module_name, raising=False)
    return importlib.import_module("co_op_translator.__main__")


def test_importing_main_does_not_load_command_modules(monkeypatch):
    _reload_main(monkeypatch)

    loaded_commands = [
        module_name
        for module_name, _ in COMMAND_MODULES.values()
        if module_name in sys.modules
    ]

    assert loaded_commands == []


@pytest.mark.parametrize(
    ("script_name", "selected_command"),
    [
        ("translate", "translate"),
        ("evaluate", "evaluate"),
        ("migrate-links", "migrate-links"),
        ("co-op-review", "co-op-review"),
        ("python", "translate"),
    ],
)
def test_main_loads_only_the_selected_command(
    monkeypatch, script_name, selected_command
):
    main_module = _reload_main(monkeypatch)
    selected_module, command_name = COMMAND_MODULES[selected_command]
    command = Mock()
    fake_module = ModuleType(selected_module)
    setattr(fake_module, command_name, command)
    monkeypatch.setitem(sys.modules, selected_module, fake_module)
    monkeypatch.setattr(sys, "argv", [script_name])

    main_module.main()

    command.assert_called_once_with()
    for module_name, _ in COMMAND_MODULES.values():
        if module_name != selected_module:
            assert module_name not in sys.modules


@pytest.mark.parametrize("script_name", COMMAND_MODULES)
def test_each_command_can_render_help_without_loading_provider_dependencies(
    script_name,
):
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(REPOSITORY_ROOT / "src")
    probe = f"""
import sys

sys.argv = [{script_name!r}, "--help"]
from co_op_translator.__main__ import main

try:
    main()
except SystemExit as error:
    assert error.code == 0

assert "co_op_translator.core.llm" not in sys.modules
"""

    result = subprocess.run(
        [sys.executable, "-c", probe],
        cwd=REPOSITORY_ROOT,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "Usage:" in result.stdout
