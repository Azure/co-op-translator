# Maintainer Guide

This page summarizes how the API, CLI, and documentation site are wired together.

## Public API boundary

The stable Python API is exported from:

```python
co_op_translator.api
```

Currently, that package exports:

```python
from co_op_translator.api import run_review, run_translation
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
```

`src/co_op_translator/__main__.py` dispatches by script name:

- `translate` calls `co_op_translator.cli.translate.translate_command`
- `evaluate` calls `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` calls `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` calls `co_op_translator.cli.review.review_command`

When adding or changing CLI options, update:

- the relevant `src/co_op_translator/cli/*.py` command
- `getting_started/command-reference.md`
- `docs/cli.md`
- CLI-related tests, if behavior changes

## Translation flow

The high-level translation flow is:

1. Parse CLI arguments or API parameters.
2. Validate LLM configuration with `LLMConfig`.
3. Validate Azure AI Vision when image translation is selected.
4. Normalize language codes.
5. Detect legacy language folder aliases.
6. Estimate translation volume.
7. Update README language/course sections when applicable.
8. Delegate project translation to `ProjectTranslator`.
9. `ProjectTranslator` delegates file processing to `TranslationManager`.

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
pip install -r requirements.txt
pip install -r requirements-docs.txt
```

Installing runtime dependencies before docs dependencies lets `mkdocstrings` import the package and render the public Python API reference.

## Docs quality bar

Before merging documentation changes, run:

```bash
python -m mkdocs build --strict
git diff --check
```

Use strict builds so broken links, invalid navigation entries, and API rendering issues fail early.
