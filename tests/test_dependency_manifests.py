from pathlib import Path

from packaging.requirements import Requirement
from packaging.utils import canonicalize_name
from packaging.version import Version
import yaml

import tomllib

REPO_ROOT = Path(__file__).resolve().parents[1]


def _poetry_dependency_names() -> tuple[set[str], set[str]]:
    config = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    poetry = config["tool"]["poetry"]
    runtime = set(poetry["dependencies"])
    runtime.discard("python")
    development = set(poetry["group"]["dev"]["dependencies"])
    return (
        {canonicalize_name(name) for name in runtime},
        {canonicalize_name(name) for name in development},
    )


def _requirements(path: Path) -> dict[str, Requirement]:
    parsed = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith(("#", "-r ")):
            continue
        requirement = Requirement(line)
        parsed[canonicalize_name(requirement.name)] = requirement
    return parsed


def _pinned_version(requirement: Requirement) -> Version:
    pins = [
        Version(specifier.version)
        for specifier in requirement.specifier
        if specifier.operator == "=="
    ]
    assert len(pins) == 1, f"Expected one exact pin for {requirement.name}"
    return pins[0]


def test_direct_dependencies_are_present_in_requirements_files():
    runtime_names, development_names = _poetry_dependency_names()
    runtime_requirements = _requirements(REPO_ROOT / "requirements.txt")
    development_requirements = _requirements(REPO_ROOT / "requirements-dev.txt")

    assert runtime_names <= runtime_requirements.keys()
    assert development_names <= (
        runtime_requirements.keys() | development_requirements.keys()
    )


def test_supported_python_range_matches_ci_matrix():
    config = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    workflow = yaml.safe_load(
        (REPO_ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    )

    assert config["tool"]["poetry"]["dependencies"]["python"] == ">=3.11,<3.15"
    assert workflow["jobs"]["test"]["strategy"]["matrix"]["python-version"] == [
        "3.11",
        "3.12",
        "3.13",
        "3.14",
    ]


def test_export_uses_modern_numpy_release():
    numpy_requirement = _requirements(REPO_ROOT / "requirements.txt")["numpy"]

    assert _pinned_version(numpy_requirement) >= Version("2.0")


def test_typing_extensions_range_supports_semantic_kernel():
    typing_requirement = _requirements(REPO_ROOT / "requirements.txt")[
        "typing-extensions"
    ]

    assert _pinned_version(typing_requirement) >= Version("4.15.0")


def test_ai_sdk_exports_are_on_current_compatible_generations():
    requirements = _requirements(REPO_ROOT / "requirements.txt")

    assert Version("2.25") <= _pinned_version(requirements["openai"]) < Version("3")
    assert _pinned_version(requirements["semantic-kernel"]) >= Version("1.44.1")
    assert _pinned_version(requirements["agent-framework-core"]) >= Version("1.16.0")
    assert _pinned_version(requirements["agent-framework-openai"]) >= Version("1.14.1")


def test_optional_agent_framework_provider_exports_are_development_only():
    runtime = _requirements(REPO_ROOT / "requirements.txt")
    development = _requirements(REPO_ROOT / "requirements-dev.txt")

    assert "agent-framework-anthropic" not in runtime
    assert "agent-framework-ollama" not in runtime
    assert "agent-framework-anthropic" in development
    assert "agent-framework-ollama" in development


def test_runtime_export_preserves_required_extras():
    requirements = _requirements(REPO_ROOT / "requirements.txt")

    assert requirements["az-ai-healthcheck"].extras == {"vision"}
    assert requirements["pyjwt"].extras == {"crypto"}
