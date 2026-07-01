# ਮੇਨਟੇਨਰ ਗਾਈਡ

ਇਹ ਪੰਨਾ ਸੰਖੇਪ ਵਿੱਚ ਦੱਸਦਾ ਹੈ ਕਿ API, CLI, ਅਤੇ ਦਸਤਾਵੇਜ਼ ਸਾਈਟ ਇਕੱਠੇ ਕਿਵੇਂ ਕੰਮ ਕਰਦੀਆਂ ਹਨ।

## ਪਬਲਿਕ API ਦੀ ਸੀਮਾ

The stable Python API is exported from:

```python
co_op_translator.api
```

The public API is organized into content translation helpers, path rewriting helpers, project orchestration, and review:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

When adding new public APIs, update:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

Avoid documenting lower-level `core` modules as stable API unless the project intends to support them directly.

## CLI entry points

The package defines these Poetry scripts:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` script name ਦੇ ਅਨੁਸਾਰ ਡਿਸਪੈਚ ਕਰਦਾ ਹੈ:

- `translate` `co_op_translator.cli.translate.translate_command` ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ
- `evaluate` `co_op_translator.cli.evaluate.evaluate_command` ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ
- `migrate-links` `co_op_translator.cli.migrate_links.migrate_links_command` ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ
- `co-op-review` `co_op_translator.cli.review.review_command` ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ

`co-op-translator-mcp` `__main__.py` ਨੂੰ ਬਾਈਪਾਸ ਕਰਦਾ ਹੈ ਅਤੇ ਸਿੱਧਾ `co_op_translator.mcp.server:main` ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ।

When adding or changing CLI options, update:

- the relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- CLI-related tests, if behavior changes

## MCP server

The MCP server is implemented in:

```python
co_op_translator.mcp.server
```

ਸਰਵਰ ਜਾਣਬੂਝ ਕੇ ਪਬਲਿਕ Python API ਨੂੰ ਰੈਪ ਕਰਦਾ ਹੈ ਨ ਕਿ ਨਿਚਲੇ-ਪੱਧਰ ਦੇ `core` ਮੋਡੀਊਲਾਂ ਨੂੰ ਕਾਲ ਕਰੇ। ਇਸ ਸੀਮਾ ਨੂੰ ਅਖੰਡ ਰੱਖੋ ਤਾਂ ਜੋ MCP ਕਲਾਇੰਟ, Python ਕਾਲ ਕਰਨ ਵਾਲੇ, ਅਤੇ CLI ਦਾ ਵਿਹਾਰ ਇੱਕੋ ਜਿਹਾ ਰਹੇ।

When adding or changing MCP tools, update:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

Repository translation tools are model-callable through MCP and can write many files. Keep `dry_run=True` as the default and require `confirm_write=True` before non-dry-run project translation.

## Translation flow

The high-level project translation flow is:

1. Parse CLI arguments or API parameters.
2. Validate LLM configuration with `LLMConfig`.
3. Validate Azure AI Vision when image translation is selected.
4. Normalize language codes.
5. Detect legacy language folder aliases.
6. Estimate translation volume.
7. Update README language/course sections when applicable.
8. Delegate project translation to `ProjectTranslator`.
9. `ProjectTranslator` delegates file processing to `TranslationManager`.

`TranslationManager` is composed from focused file-type mixins:

- `ProjectMarkdownTranslationMixin` handles Markdown file reads, content translation, path rewriting, metadata, disclaimers, and writes.
- `ProjectNotebookTranslationMixin` handles notebook file reads, Markdown-cell translation, path rewriting, metadata, disclaimers, and writes.
- `ProjectImageTranslationMixin` handles image discovery, text extraction/translation, rendered image writes, and metadata.

The lower-level content APIs skip the project workflow:

1. `translate_markdown_content` and `translate_notebook_content` translate in-memory content only.
2. `translate_image_content` translates text in a single image and returns a rendered image object.
3. `rewrite_markdown_paths` and `rewrite_notebook_paths` are explicit post-processing helpers. They perform no translation and no project writes.

## Review flow

The deterministic review flow is:

1. Parse CLI arguments or API parameters.
2. Normalize requested language codes.
3. Build one or more review targets from `root_dir`, `root_dirs`, or `groups`.
4. Optionally limit source files with `--changed-from`.
5. Run deterministic checks for structure, translation freshness, Markdown integrity, and local link/image paths.
6. Print either text output or GitHub-flavored Markdown.
7. Exit with a failure when review errors are found.

The review flow does not require API keys and should remain suitable for pull request CI. The pull request workflow writes a check summary on every run and only posts a PR comment when `co-op-review` fails.

## Documentation site

The docs site is configured by:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

The `docs/` directory is the canonical documentation source. Do not add new end-user guides outside this directory unless the project intentionally introduces another published documentation surface.

Build locally:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview locally:

```bash
python -m mkdocs serve
```

The generated site is written to `site/`, which is ignored by git.

## GitHub Pages workflow

`.github/workflows/docs.yml` builds the site on pull requests and deploys it on pushes to `main`.

The workflow installs:

```bash
pip install -r requirements-docs.txt
```

The docs workflow installs only the documentation toolchain. `mkdocs.yml` points `mkdocstrings` at `src/` so public API pages can be rendered from the source tree without installing the full runtime dependency set. If future API docs require importing optional runtime providers during the build, update both `.github/workflows/docs.yml` and this guide together.

## Docs quality bar

Before merging documentation changes, run:

```bash
python -m mkdocs build --strict
git diff --check
```

Use strict builds so broken links, invalid navigation entries, and API rendering issues fail early.