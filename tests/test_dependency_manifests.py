from pathlib import Path

from packaging.requirements import Requirement
from packaging.utils import canonicalize_name
from packaging.version import Version

try:
    import tomllib
except ImportError:  # pragma: no cover - Python 3.10
    import tomli as tomllib


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


def test_direct_dependencies_are_present_in_requirements_files():
    runtime_names, development_names = _poetry_dependency_names()
    runtime_requirements = _requirements(REPO_ROOT / "requirements.txt")
    development_requirements = _requirements(REPO_ROOT / "requirements-dev.txt")

    assert runtime_names <= runtime_requirements.keys()
    assert development_names <= (
        runtime_requirements.keys() | development_requirements.keys()
    )


def test_numpy_range_supports_python_312_compatible_release():
    numpy_requirement = _requirements(REPO_ROOT / "requirements.txt")["numpy"]

    assert Version("1.26.0") in numpy_requirement.specifier


def test_typing_extensions_range_supports_semantic_kernel():
    typing_requirement = _requirements(REPO_ROOT / "requirements.txt")[
        "typing-extensions"
    ]

    assert Version("4.13.0") in typing_requirement.specifier
