from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

from co_op_translator.core.project.translation.incremental_markdown import (
    MarkdownBlock,
    split_markdown_blocks,
)
from co_op_translator.review.models import ReviewIssue, ReviewSeverity
from co_op_translator.review.targets import ReviewTarget
from co_op_translator.utils.markdown.spans import markdown_code_spans

WORD_PATTERN = re.compile(r"[A-Za-z][A-Za-z'-]*")
MARKUP_PATTERN = re.compile(r"[\s#>*_|~\-]+")
FENCE_PATTERN = re.compile(r"^\s*(?:~~~|```)", re.MULTILINE)


def _markdown_documents(path: Path) -> list[str]:
    if path.suffix.lower() != ".ipynb":
        return [path.read_text(encoding="utf-8")]
    notebook = json.loads(path.read_text(encoding="utf-8"))
    documents = []
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "markdown":
            source = cell.get("source", [])
            documents.append(
                "".join(source) if isinstance(source, list) else str(source)
            )
    return documents


def _prose_blocks(document: str) -> list[MarkdownBlock]:
    return [
        block
        for block in split_markdown_blocks(document)
        if block.kind not in {"code", "frontmatter", "thematic_break"}
        and MARKUP_PATTERN.sub("", block.text)
    ]


def _normalized_block(text: str) -> str:
    return " ".join(text.split()).casefold()


def _protected_literals(document: str) -> Counter[str]:
    return Counter(
        document[span.start : span.end] for span in markdown_code_spans(document)
    )


def _issue(target, source_file, language, check, severity, message) -> ReviewIssue:
    return ReviewIssue(
        check=check,
        severity=severity,
        path=target.display_source_path(source_file),
        language=language,
        message=message,
    )


def check_translation_completeness(
    target: ReviewTarget, source_files: list[Path], languages: list[str]
) -> list[ReviewIssue]:
    """Run deterministic structural and unchanged-prose heuristics."""

    issues: list[ReviewIssue] = []
    for source_file in source_files:
        for language in languages:
            if language.lower().startswith("en"):
                continue
            translated_path = target.translated_path(source_file, language)
            if not translated_path.exists():
                continue
            try:
                source_documents = _markdown_documents(source_file)
                translated_documents = _markdown_documents(translated_path)
            except (OSError, json.JSONDecodeError):
                continue

            source_blocks = [
                block for doc in source_documents for block in _prose_blocks(doc)
            ]
            target_blocks = [
                block for doc in translated_documents for block in _prose_blocks(doc)
            ]
            if len(target_blocks) < len(source_blocks):
                issues.append(
                    _issue(
                        target,
                        source_file,
                        language,
                        "missing-blocks",
                        ReviewSeverity.ERROR,
                        f"Translation has {len(source_blocks) - len(target_blocks)} fewer prose block(s) than the source.",
                    )
                )

            source_counts = Counter(
                _normalized_block(block.text)
                for block in source_blocks
                if len(_normalized_block(block.text)) >= 40
            )
            target_counts = Counter(
                _normalized_block(block.text)
                for block in target_blocks
                if len(_normalized_block(block.text)) >= 40
            )
            duplicate_count = sum(
                max(0, count - source_counts.get(text, 0))
                for text, count in target_counts.items()
                if count > 1
            )
            if duplicate_count:
                issues.append(
                    _issue(
                        target,
                        source_file,
                        language,
                        "duplicated-blocks",
                        ReviewSeverity.WARNING,
                        f"Translation contains {duplicate_count} unexpected duplicated prose block(s).",
                    )
                )

            target_text = Counter(
                _normalized_block(block.text) for block in target_blocks
            )
            unchanged = sum(
                1
                for block in source_blocks
                if len(WORD_PATTERN.findall(block.text)) >= 5
                and target_text[_normalized_block(block.text)] > 0
            )
            if unchanged:
                issues.append(
                    _issue(
                        target,
                        source_file,
                        language,
                        "suspicious-untranslated-prose",
                        ReviewSeverity.WARNING,
                        f"Found {unchanged} source prose block(s) unchanged in the translation.",
                    )
                )

            source_spans = [markdown_code_spans(doc) for doc in source_documents]
            target_spans = [markdown_code_spans(doc) for doc in translated_documents]
            if sum(len(FENCE_PATTERN.findall(doc)) for doc in source_documents) != sum(
                len(FENCE_PATTERN.findall(doc)) for doc in translated_documents
            ):
                continue
            if [len(spans) for spans in source_spans] != [
                len(spans) for spans in target_spans
            ]:
                continue
            source_literals = Counter(
                doc[span.start : span.end]
                for doc, spans in zip(source_documents, source_spans)
                for span in spans
            )
            target_literals = Counter(
                doc[span.start : span.end]
                for doc, spans in zip(translated_documents, target_spans)
                for span in spans
            )
            missing_literals = sum(
                max(0, count - target_literals.get(literal, 0))
                for literal, count in source_literals.items()
            )
            if missing_literals:
                issues.append(
                    _issue(
                        target,
                        source_file,
                        language,
                        "protected-literals",
                        ReviewSeverity.ERROR,
                        f"Translation changed or removed {missing_literals} protected code literal(s).",
                    )
                )
    return issues
