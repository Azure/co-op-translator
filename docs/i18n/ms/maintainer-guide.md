# Panduan Penyelenggara

This page summarizes how the API, CLI, and documentation site are wired together.

## Sempadan API Awam

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

## Titik masuk CLI

The package defines these Poetry scripts:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` dispatches by script name:

- `translate` memanggil `co_op_translator.cli.translate.translate_command`
- `evaluate` memanggil `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` memanggil `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` memanggil `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` melangkau `__main__.py` dan memanggil `co_op_translator.mcp.server:main` secara langsung.

When adding or changing CLI options, update:

- the relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- CLI-related tests, if behavior changes

## Pelayan MCP

The MCP server is implemented in:

```python
co_op_translator.mcp.server
```

The server intentionally wraps the public Python API rather than calling lower-level `core` modules. Keep this boundary intact so MCP clients, Python callers, and the CLI share the same behavior.

When adding or changing MCP tools, update:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

Repository translation tools are model-callable through MCP and can write many files. Keep `dry_run=True` as the default and require `confirm_write=True` before non-dry-run project translation.

## Aliran terjemahan

The high-level project translation flow is:

1. Huraikan argumen CLI atau parameter API.
2. Sahkan konfigurasi LLM dengan `LLMConfig`.
3. Sahkan Azure AI Vision apabila terjemahan imej dipilih.
4. Normalkan kod bahasa.
5. Kesan alias folder bahasa warisan.
6. Anggarkan jumlah terjemahan.
7. Kemas kini bahagian bahasa/kursus dalam README apabila berkenaan.
8. Delegasikan terjemahan projek kepada `ProjectTranslator`.
9. `ProjectTranslator` mendelegasikan pemprosesan fail kepada `TranslationManager`.

`TranslationManager` is composed from focused file-type mixins:

- `ProjectMarkdownTranslationMixin` mengendalikan pembacaan fail Markdown, terjemahan kandungan, penulisan semula laluan, metadata, penafian, dan penulisan.
- `ProjectNotebookTranslationMixin` mengendalikan pembacaan fail notebook, terjemahan sel Markdown, penulisan semula laluan, metadata, penafian, dan penulisan.
- `ProjectImageTranslationMixin` mengendalikan penemuan imej, ekstraksi/terjemahan teks, penulisan imej yang dirender, dan metadata.

The lower-level content APIs skip the project workflow:

1. `translate_markdown_content` dan `translate_notebook_content` menterjemah kandungan dalam memori sahaja.
2. `translate_image_content` menterjemah teks dalam satu imej dan mengembalikan objek imej yang dirender.
3. `rewrite_markdown_paths` dan `rewrite_notebook_paths` adalah pembantu pasca-pemprosesan eksplisit. Mereka tidak menjalankan terjemahan dan tidak melakukan penulisan projek.

## Aliran semakan

The deterministic review flow is:

1. Huraikan argumen CLI atau parameter API.
2. Normalkan kod bahasa yang diminta.
3. Bina satu atau lebih sasaran semakan dari `root_dir`, `root_dirs`, atau `groups`.
4. Secara pilihan, hadkan fail sumber dengan `--changed-from`.
5. Jalankan pemeriksaan deterministik untuk struktur, kesegaran terjemahan, integriti Markdown, dan laluan pautan/imej tempatan.
6. Cetak sama ada keluaran teks atau Markdown berperisa GitHub.
7. Keluar dengan kegagalan apabila ralat semakan ditemui.

The review flow does not require API keys and should remain suitable for pull request CI. The pull request workflow writes a check summary on every run and only posts a PR comment when `co-op-review` fails.

## Laman dokumentasi

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

## Aliran kerja GitHub Pages

`.github/workflows/docs.yml` builds the site on pull requests and deploys it on pushes to `main`.

The workflow installs:

```bash
pip install -r requirements-docs.txt
```

The docs workflow installs only the documentation toolchain. `mkdocs.yml` points `mkdocstrings` at `src/` so public API pages can be rendered from the source tree without installing the full runtime dependency set. If future API docs require importing optional runtime providers during the build, update both `.github/workflows/docs.yml` and this guide together.

## Ambang kualiti dokumen

Before merging documentation changes, run:

```bash
python -m mkdocs build --strict
git diff --check
```

Use strict builds so broken links, invalid navigation entries, and API rendering issues fail early.