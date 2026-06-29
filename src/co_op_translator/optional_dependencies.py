from __future__ import annotations


class MissingOptionalDependencyError(ImportError):
    """Raised when a feature requires an optional install extra."""


def raise_for_optional_dependency(
    *,
    feature: str,
    extra: str,
    exc: Exception | None = None,
) -> None:
    message = (
        f"{feature} requires the optional '{extra}' dependencies. "
        f"Install them with: pip install \"co-op-translator[{extra}]\""
    )
    raise MissingOptionalDependencyError(message) from exc
