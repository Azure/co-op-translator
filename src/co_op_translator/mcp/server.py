from __future__ import annotations

import argparse
import base64
import io
import json
from contextlib import redirect_stderr, redirect_stdout
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any, Callable, TypeVar

from mcp.server.fastmcp import FastMCP
from PIL import Image

from co_op_translator import api as co_op_api
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.config.vision_config.config import VisionConfig
from co_op_translator.utils.common.lang_utils import get_supported_language_codes

T = TypeVar("T")

SERVER_NAME = "Co-op Translator"
DEFAULT_IMAGE_FORMAT = "PNG"
SUPPORTED_IMAGE_FORMATS = {"PNG", "JPEG", "WEBP"}

SERVER_INSTRUCTIONS = """
Use Co-op Translator tools to translate Markdown, Jupyter notebooks, images,
and complete documentation repositories. Content translation tools do not write
files or rewrite links automatically. Project translation tools can write many
files, so non-dry-run calls require confirm_write=true. Agent-assisted
translation tools prepare chunks for the host agent to translate, then
reconstruct the translated content without requiring Co-op Translator LLM
provider credentials.
""".strip()


def _capture_call(
    callback: Callable[[], T],
) -> tuple[T | None, str, str, Exception | None]:
    stdout = io.StringIO()
    stderr = io.StringIO()
    try:
        with redirect_stdout(stdout), redirect_stderr(stderr):
            result = callback()
    except Exception as exc:  # pragma: no cover - exercised by integration paths
        return None, stdout.getvalue(), stderr.getvalue(), exc
    return result, stdout.getvalue(), stderr.getvalue(), None


def _coerce_groups(
    groups: list[dict[str, str | None]] | list[list[str | None]] | None,
) -> list[tuple[str, str | None]] | None:
    if groups is None:
        return None

    coerced: list[tuple[str, str | None]] = []
    for group in groups:
        if isinstance(group, dict):
            root_dir = group.get("root_dir")
            translations_dir = group.get("translations_dir")
        else:
            root_dir = group[0] if len(group) > 0 else None
            translations_dir = group[1] if len(group) > 1 else None

        if not root_dir:
            raise ValueError("Each group must include a root_dir value.")
        coerced.append((root_dir, translations_dir))
    return coerced


def _normalize_image_format(image_format: str | None) -> str:
    normalized = (image_format or DEFAULT_IMAGE_FORMAT).upper()
    if normalized == "JPG":
        normalized = "JPEG"
    if normalized not in SUPPORTED_IMAGE_FORMATS:
        allowed = ", ".join(sorted(SUPPORTED_IMAGE_FORMATS))
        raise ValueError(
            f"Unsupported image_format '{image_format}'. Use one of: {allowed}."
        )
    return normalized


def _image_to_result(
    image: Image.Image,
    *,
    image_format: str | None = None,
    output_path: str | None = None,
) -> dict[str, Any]:
    resolved_format = _normalize_image_format(image_format)
    buffer = io.BytesIO()
    image.save(buffer, format=resolved_format)

    saved_path = None
    if output_path:
        destination = Path(output_path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        image.save(destination, format=resolved_format)
        saved_path = str(destination)

    return {
        "mime_type": f"image/{resolved_format.lower()}",
        "format": resolved_format,
        "width": image.width,
        "height": image.height,
        "data_base64": base64.b64encode(buffer.getvalue()).decode("ascii"),
        "output_path": saved_path,
    }


def _review_summary_to_dict(summary: Any) -> dict[str, Any]:
    issues = []
    for issue in getattr(summary, "issues", []):
        if is_dataclass(issue):
            raw_issue = asdict(issue)
        else:
            raw_issue = dict(issue)

        severity = raw_issue.get("severity")
        if hasattr(severity, "value"):
            raw_issue["severity"] = severity.value
        path = raw_issue.get("path")
        if path is not None:
            raw_issue["path"] = str(path)
        issues.append(raw_issue)

    return {
        "root_dir": str(summary.root_dir),
        "source_files": [str(path) for path in summary.source_files],
        "languages": list(summary.languages),
        "error_count": summary.error_count,
        "warning_count": summary.warning_count,
        "issues": issues,
        "text": summary.to_text(),
        "github_markdown": summary.to_github_markdown(),
    }


def _translation_result(
    *,
    dry_run: bool,
    stdout: str,
    stderr: str,
    error: Exception | None,
) -> dict[str, Any]:
    return {
        "ok": error is None,
        "dry_run": dry_run,
        "stdout": stdout,
        "stderr": stderr,
        "error": str(error) if error else None,
    }


async def translate_markdown_content(
    document: str,
    language_code: str,
    source_path: str | None = None,
) -> dict[str, Any]:
    """Translate Markdown content without file I/O or project path rewriting."""

    translated = await co_op_api.translate_markdown_content(
        document,
        language_code,
        {"source_path": source_path} if source_path else None,
    )
    return {
        "language_code": language_code,
        "content": translated,
    }


async def translate_notebook_content(
    notebook: str | dict[str, Any],
    language_code: str,
    source_path: str | None = None,
) -> dict[str, Any]:
    """Translate notebook Markdown cells without file I/O or path rewriting."""

    translated = await co_op_api.translate_notebook_content(
        notebook,
        language_code,
        {"source_path": source_path} if source_path else None,
    )
    return {
        "language_code": language_code,
        "notebook": translated,
    }


def start_markdown_agent_translation(
    document: str,
    language_code: str,
    source_path: str | None = None,
) -> dict[str, Any]:
    """Prepare Markdown chunks for host-agent translation without provider calls."""

    return co_op_api.start_markdown_agent_translation(
        document,
        language_code,
        source_path=source_path,
    )


def finish_markdown_agent_translation(
    job: dict[str, Any],
    translated_chunks: dict[str, Any] | list[dict[str, Any]],
) -> dict[str, Any]:
    """Reconstruct Markdown from chunks translated by the host agent."""

    return co_op_api.finish_markdown_agent_translation(job, translated_chunks)


def start_notebook_agent_translation(
    notebook: str | dict[str, Any],
    language_code: str,
    source_path: str | None = None,
) -> dict[str, Any]:
    """Prepare notebook Markdown-cell chunks for host-agent translation."""

    return co_op_api.start_notebook_agent_translation(
        notebook,
        language_code,
        source_path=source_path,
    )


def finish_notebook_agent_translation(
    job: dict[str, Any],
    translated_chunks: dict[str, Any] | list[dict[str, Any]],
) -> dict[str, Any]:
    """Reconstruct a notebook from chunks translated by the host agent."""

    return co_op_api.finish_notebook_agent_translation(job, translated_chunks)


def translate_image_content(
    image_path: str,
    language_code: str,
    root_dir: str = ".",
    fast_mode: bool = False,
    image_format: str = DEFAULT_IMAGE_FORMAT,
    output_path: str | None = None,
) -> dict[str, Any]:
    """Translate text in an image and return an MCP-friendly image payload."""

    image = co_op_api.translate_image_content(
        image_path,
        language_code,
        {
            "root_dir": root_dir,
            "fast_mode": fast_mode,
        },
    )
    result = _image_to_result(
        image,
        image_format=image_format,
        output_path=output_path,
    )
    result.update(
        {
            "language_code": language_code,
            "source_path": image_path,
        }
    )
    return result


def rewrite_markdown_paths(
    content: str,
    source_path: str,
    target_path: str,
    policy: dict[str, Any],
) -> dict[str, Any]:
    """Rewrite Markdown/frontmatter paths for a translated target."""

    rewritten = co_op_api.rewrite_markdown_paths(
        content,
        source_path=source_path,
        target_path=target_path,
        policy=policy,
    )
    return {
        "content": rewritten,
    }


def rewrite_notebook_paths(
    content: str,
    source_path: str,
    target_path: str,
    policy: dict[str, Any],
) -> dict[str, Any]:
    """Rewrite Markdown-cell paths inside a translated notebook target."""

    rewritten = co_op_api.rewrite_notebook_paths(
        content,
        source_path=source_path,
        target_path=target_path,
        policy=policy,
    )
    return {
        "notebook": rewritten,
    }


def run_translation(
    language_codes: str,
    root_dir: str = ".",
    update: bool = False,
    images: bool = False,
    markdown: bool = False,
    notebook: bool = False,
    debug: bool = False,
    save_logs: bool = False,
    yes: bool = True,
    add_disclaimer: bool = False,
    translations_dir: str | None = None,
    image_dir: str | None = None,
    root_dirs: list[str] | None = None,
    groups: list[dict[str, str | None]] | list[list[str | None]] | None = None,
    repo_url: str | None = None,
    glossaries: list[str] | None = None,
    readme_only: bool = False,
    dry_run: bool = True,
    confirm_write: bool = False,
) -> dict[str, Any]:
    """Run repository translation through the public API.

    Non-dry-run calls can write, update, or delete many files. Set
    confirm_write=true when dry_run=false. Set readme_only=true to translate
    only the root README while leaving linked documents in the source tree.
    """

    if not dry_run and not confirm_write:
        raise ValueError(
            "Set confirm_write=true to run project translation with dry_run=false."
        )

    def _run() -> None:
        co_op_api.run_translation(
            language_codes=language_codes,
            root_dir=root_dir,
            update=update,
            images=images,
            markdown=markdown,
            notebook=notebook,
            debug=debug,
            save_logs=save_logs,
            yes=yes,
            add_disclaimer=add_disclaimer,
            translations_dir=translations_dir,
            image_dir=image_dir,
            root_dirs=root_dirs,
            groups=_coerce_groups(groups),
            repo_url=repo_url,
            glossaries=glossaries,
            readme_only=readme_only,
            dry_run=dry_run,
        )

    _, stdout, stderr, error = _capture_call(_run)
    return _translation_result(
        dry_run=dry_run,
        stdout=stdout,
        stderr=stderr,
        error=error,
    )


def translate_project(
    language_codes: str,
    root_dir: str = ".",
    update: bool = False,
    images: bool = False,
    markdown: bool = False,
    notebook: bool = False,
    debug: bool = False,
    save_logs: bool = False,
    yes: bool = True,
    add_disclaimer: bool = False,
    translations_dir: str | None = None,
    image_dir: str | None = None,
    root_dirs: list[str] | None = None,
    groups: list[dict[str, str | None]] | list[list[str | None]] | None = None,
    repo_url: str | None = None,
    glossaries: list[str] | None = None,
    readme_only: bool = False,
    dry_run: bool = True,
    confirm_write: bool = False,
) -> dict[str, Any]:
    """Compatibility alias for run_translation."""

    return run_translation(
        language_codes=language_codes,
        root_dir=root_dir,
        update=update,
        images=images,
        markdown=markdown,
        notebook=notebook,
        debug=debug,
        save_logs=save_logs,
        yes=yes,
        add_disclaimer=add_disclaimer,
        translations_dir=translations_dir,
        image_dir=image_dir,
        root_dirs=root_dirs,
        groups=groups,
        repo_url=repo_url,
        glossaries=glossaries,
        readme_only=readme_only,
        dry_run=dry_run,
        confirm_write=confirm_write,
    )


def run_review(
    language_codes: str | list[str] = "all",
    root_dir: str = ".",
    update: bool = False,
    images: bool = False,
    markdown: bool = False,
    notebook: bool = False,
    debug: bool = False,
    save_logs: bool = False,
    yes: bool = True,
    add_disclaimer: bool = False,
    translations_dir: str | None = None,
    image_dir: str | None = None,
    root_dirs: list[str] | None = None,
    groups: list[dict[str, str | None]] | list[list[str | None]] | None = None,
    repo_url: str | None = None,
    glossaries: list[str] | None = None,
    dry_run: bool = False,
    changed_from: str | None = None,
    output_format: str = "text",
    fail_on_warnings: bool = False,
) -> dict[str, Any]:
    """Run deterministic translation review through the public API."""

    def _run() -> Any:
        return co_op_api.run_review(
            language_codes=language_codes,
            root_dir=root_dir,
            update=update,
            images=images,
            markdown=markdown,
            notebook=notebook,
            debug=debug,
            save_logs=save_logs,
            yes=yes,
            add_disclaimer=add_disclaimer,
            translations_dir=translations_dir,
            image_dir=image_dir,
            root_dirs=root_dirs,
            groups=_coerce_groups(groups),
            repo_url=repo_url,
            glossaries=glossaries,
            dry_run=dry_run,
            changed_from=changed_from,
            output_format=output_format,
            fail_on_warnings=fail_on_warnings,
        )

    summary, stdout, stderr, error = _capture_call(_run)
    result: dict[str, Any] = {
        "ok": error is None,
        "stdout": stdout,
        "stderr": stderr,
        "error": str(error) if error else None,
    }
    if summary is not None:
        result["summary"] = _review_summary_to_dict(summary)
    return result


def get_configuration_status(validate_connectivity: bool = False) -> dict[str, Any]:
    """Return provider availability without exposing secret values."""

    status: dict[str, Any] = {
        "llm": {
            "available": False,
            "provider": None,
            "connectivity_ok": None,
            "error": None,
        },
        "vision": {
            "available": False,
            "provider": None,
            "connectivity_ok": None,
            "error": None,
        },
    }

    try:
        llm_provider = LLMConfig.get_available_provider()
        status["llm"]["available"] = True
        status["llm"]["provider"] = llm_provider.value
        if validate_connectivity:
            status["llm"]["connectivity_ok"] = LLMConfig.validate_connectivity()
    except Exception as exc:  # pragma: no cover - depends on local environment
        status["llm"]["error"] = str(exc)

    try:
        vision_provider = VisionConfig.get_available_provider()
        status["vision"]["available"] = vision_provider is not None
        status["vision"]["provider"] = (
            vision_provider.value if vision_provider else None
        )
        if validate_connectivity and vision_provider is not None:
            status["vision"]["connectivity_ok"] = VisionConfig.validate_connectivity()
    except Exception as exc:  # pragma: no cover - depends on local environment
        status["vision"]["error"] = str(exc)

    return status


def list_supported_languages() -> dict[str, Any]:
    """Return supported language codes used by Co-op Translator."""

    languages = get_supported_language_codes()
    return {
        "count": len(languages),
        "languages": languages,
    }


def get_api_overview() -> dict[str, Any]:
    """Return a concise overview of the MCP tool surface."""

    return {
        "server": SERVER_NAME,
        "workflows": [
            {
                "name": "Translate individual files or documents",
                "tools": [
                    "translate_markdown_content",
                    "translate_notebook_content",
                    "translate_image_content",
                    "rewrite_markdown_paths",
                    "rewrite_notebook_paths",
                ],
            },
            {
                "name": "Translate with the host agent model",
                "tools": [
                    "start_markdown_agent_translation",
                    "finish_markdown_agent_translation",
                    "start_notebook_agent_translation",
                    "finish_notebook_agent_translation",
                ],
            },
            {
                "name": "Translate an entire repository",
                "tools": ["run_translation", "translate_project"],
            },
            {
                "name": "Review translated output",
                "tools": ["run_review"],
            },
        ],
    }


def _json_resource(payload: dict[str, Any]) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2)


def create_server() -> FastMCP:
    """Create the Co-op Translator MCP server."""

    mcp = FastMCP(
        SERVER_NAME,
        instructions=SERVER_INSTRUCTIONS,
    )

    for tool in (
        translate_markdown_content,
        translate_notebook_content,
        start_markdown_agent_translation,
        finish_markdown_agent_translation,
        start_notebook_agent_translation,
        finish_notebook_agent_translation,
        translate_image_content,
        rewrite_markdown_paths,
        rewrite_notebook_paths,
        run_translation,
        translate_project,
        run_review,
        get_configuration_status,
        list_supported_languages,
        get_api_overview,
    ):
        mcp.tool()(tool)

    @mcp.resource("co-op://api")
    def api_resource() -> str:
        return _json_resource(get_api_overview())

    @mcp.resource("co-op://supported-languages")
    def supported_languages_resource() -> str:
        return _json_resource(list_supported_languages())

    @mcp.resource("co-op://configuration")
    def configuration_resource() -> str:
        return _json_resource(get_configuration_status(validate_connectivity=False))

    @mcp.prompt()
    def translate_markdown_document_prompt(language_code: str) -> str:
        return (
            "Translate the selected Markdown document with Co-op Translator to "
            f"{language_code}. Use translate_markdown_content first. If the user "
            "provides source and target paths, call rewrite_markdown_paths before "
            "returning or saving the final content."
        )

    @mcp.prompt()
    def agent_assisted_markdown_translation_prompt(language_code: str) -> str:
        return (
            "Translate the selected Markdown document to "
            f"{language_code} without Co-op Translator provider credentials. "
            "Call start_markdown_agent_translation, translate each returned chunk "
            "yourself by following its prompt, then call finish_markdown_agent_translation "
            "with chunk_id and translated_text values. If source and target paths "
            "are available, call rewrite_markdown_paths after finishing."
        )

    @mcp.prompt()
    def translate_repository_prompt(language_codes: str) -> str:
        return (
            "Prepare a repository translation with Co-op Translator for "
            f"{language_codes}. First call run_translation with dry_run=true. "
            "Only call run_translation with dry_run=false when the user explicitly "
            "approves the write and confirm_write=true is set."
        )

    return mcp


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run the Co-op Translator MCP server.")
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse", "streamable-http"],
        default="stdio",
        help="MCP transport to use. Defaults to stdio.",
    )
    args = parser.parse_args(argv)

    create_server().run(transport=args.transport)


if __name__ == "__main__":  # pragma: no cover
    main()
