# Guide for people wey dey maintain

Dis page dey summarize how di API, CLI, and documentation site dem take connect together.

## Public API boundary

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
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
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

`TranslationStateProvider` na di persistence boundary for hosted integrations.
E must keep generated candidates separate from accepted baselines so make an
wey no don merge translation no go become di source of truth.

When you dey add new public APIs, update:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests wey dey under `tests/co_op_translator/`, like `test_api.py` or `test_review_api.py`

Try no dey document lower-level `core` modules as stable API unless di project mean say e go support dem direct.

## CLI entry points

Di package define these Poetry scripts:

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

When you dey add or change CLI options, update:

- di relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- CLI-related tests, if behaviour changes

## MCP server

Di MCP server dey implemented in:

```python
co_op_translator.mcp.server
```

Di server purposely dey wrap di public Python API instead of calling lower-level `core` modules. Keep dis boundary intact so MCP clients, Python callers, and the CLI go share di same behaviour.

When you dey add or change MCP tools, update:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if di public API surface change

Repository translation tools fit call model through MCP and fit write plenti files. Make `dry_run=True` remain di default and require `confirm_write=True` before any non-dry-run project translation.

## Translation flow

Di high-level project translation flow na:

1. Parse CLI arguments or API parameters.
2. Validate LLM configuration with `LLMConfig`.
3. Validate Azure AI Vision when image translation dey selected.
4. Normalize language codes.
5. Detect legacy language folder aliases.
6. Estimate translation volume.
7. Update README language/course sections when e apply.
8. Delegate project translation to `ProjectTranslator`.
9. `ProjectTranslator` dey delegate file processing to `TranslationManager`.

`TranslationManager` na composed from focused file-type mixins:

- `ProjectMarkdownTranslationMixin` dey handle Markdown file reads, content translation, path rewriting, metadata, disclaimers, and writes.
- `ProjectNotebookTranslationMixin` dey handle notebook file reads, Markdown-cell translation, path rewriting, metadata, disclaimers, and writes.
- `ProjectImageTranslationMixin` dey handle image discovery, text extraction/translation, rendered image writes, and metadata.

Di lower-level content APIs skip di project workflow:

1. `translate_markdown_content` and `translate_notebook_content` translate in-memory content only.
2. `translate_image_content` translates text in a single image and returns a rendered image object.
3. `rewrite_markdown_paths` and `rewrite_notebook_paths` na explicit post-processing helpers. Dem no perform translation and no do project writes.

## Review flow

Di deterministic review flow na:

1. Parse CLI arguments or API parameters.
2. Normalize requested language codes.
3. Build one or more review targets from `root_dir`, `root_dirs`, or `groups`.
4. Optionally limit source files with `--changed-from`.
5. Run deterministic checks for structure, translation freshness, Markdown integrity, and local link/image paths.
6. Print either text output or GitHub-flavored Markdown.
7. Exit with a failure when review errors dey found.

Di review flow no need API keys and e still dey available for local checks or opt-in consumer CI. This repository no dey run `co-op-review` automatically on every pull request.

## Documentation site

Di docs site dey configured by:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

The `docs/` directory na di canonical documentation source. No add new end-user guides outside dis directory unless di project purposely introduce another published documentation surface.

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

`.github/workflows/docs.yml` dey build di site on pull requests and dey deploy am on pushes to `main`.

Di workflow dey install:

```bash
pip install -r requirements-docs.txt
```

Di docs workflow install only di documentation toolchain. `mkdocs.yml` point `mkdocstrings` at `src/` so public API pages fit render from the source tree without installing the full runtime dependency set. If future API docs need to import optional runtime providers during di build, update both `.github/workflows/docs.yml` and dis guide together.

## Docs quality bar

Before you merge documentation changes, run:

```bash
python -m mkdocs build --strict
git diff --check
```

Use strict builds so broken links, invalid navigation entries, and API rendering issues go fail early.