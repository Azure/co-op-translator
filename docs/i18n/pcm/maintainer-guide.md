# Guide for Maintaina dem

Dis page dey summarize how the API, CLI, and documentation site dem dey wire together.

## Public API border

Di stable Python API dey exported from:

```python
co_op_translator.api
```

Di public API dem organize into content translation helpers, path rewriting helpers, project orchestration, and review:

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

If you dey add new public APIs, make you update:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

No dey document lower-level `core` modules as stable API unless the project wan support dem directly.

## CLI entry points

Di package get these Poetry scripts:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` dey dispatch by script name:

- `translate` dey call `co_op_translator.cli.translate.translate_command`
- `evaluate` dey call `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` dey call `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` dey call `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` dey bypass `__main__.py` and dey call `co_op_translator.mcp.server:main` direct.

If you dey add or change CLI options, make you update:

- the relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- CLI-related tests, if behavior changes

## MCP server

Di MCP server dey implemented in:

```python
co_op_translator.mcp.server
```

Di server purposely dey wrap the public Python API instead of dey call the lower-level `core` modules. Make you keep this boundary intact so MCP clients, Python callers, and the CLI go share the same behavior.

If you dey add or change MCP tools, make you update:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

Repository translation tools fit callable from MCP and fit write plenti files. Keep `dry_run=True` as the default and require `confirm_write=True` before any non-dry-run project translation.

## How translation dey flow

Di high-level project translation flow be:

1. Parse CLI arguments or API parameters.
2. Make sure say LLM configuration correct with `LLMConfig`.
3. Make sure say Azure AI Vision dey valid when image translation selected.
4. Normalize language codes.
5. Detect legacy language folder aliases.
6. Estimate translation volume.
7. Update README language/course sections when e apply.
8. Delegate project translation to `ProjectTranslator`.
9. `ProjectTranslator` dey delegate file processing to `TranslationManager`.

`TranslationManager` dey composed from focused file-type mixins:

- `ProjectMarkdownTranslationMixin` dey handle Markdown file reads, content translation, path rewriting, metadata, disclaimers, and writes.
- `ProjectNotebookTranslationMixin` dey handle notebook file reads, Markdown-cell translation, path rewriting, metadata, disclaimers, and writes.
- `ProjectImageTranslationMixin` dey handle image discovery, text extraction/translation, rendered image writes, and metadata.

Di lower-level content APIs no dey follow the project workflow:

1. `translate_markdown_content` and `translate_notebook_content` translate in-memory content only.
2. `translate_image_content` translates text in a single image and returns a rendered image object.
3. `rewrite_markdown_paths` and `rewrite_notebook_paths` na explicit post-processing helpers. Dem no perform translation and no write to project.

## Review flow

Di deterministic review flow be:

1. Parse CLI arguments or API parameters.
2. Normalize requested language codes.
3. Build one or more review targets from `root_dir`, `root_dirs`, or `groups`.
4. Optionally limit source files with `--changed-from`.
5. Run deterministic checks for structure, translation freshness, Markdown integrity, and local link/image paths.
6. Print either text output or GitHub-flavored Markdown.
7. Exit with failure if review errors dey found.

Di review flow no need API keys and e suppose still dey suitable for pull request CI. The pull request workflow dey write a check summary on every run and e go only post a PR comment when `co-op-review` fail.

## Documentation site

Di docs site dey configured by:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

The `docs/` directory na di canonical documentation source. No add new end-user guides outside dis directory unless di project mean introduce another published documentation surface.

Build locally:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview locally:

```bash
python -m mkdocs serve
```

Di generated site dey write to `site/`, wey git dey ignore.

## GitHub Pages workflow

`.github/workflows/docs.yml` dey build the site on pull requests and deploy am on pushes to `main`.

The workflow dey install:

```bash
pip install -r requirements-docs.txt
```

Di docs workflow dey install only the documentation toolchain. `mkdocs.yml` dey point `mkdocstrings` to `src/` so public API pages fit render from the source tree without installing the full runtime dependency set. If future API docs go need import optional runtime providers during the build, update both `.github/workflows/docs.yml` and dis guide together.

## Docs quality bar

Before you merge documentation changes, run:

```bash
python -m mkdocs build --strict
git diff --check
```

Use strict builds so broken links, invalid navigation entries, and API rendering issues go fail early.