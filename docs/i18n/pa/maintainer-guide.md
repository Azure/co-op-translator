# ਮੈਂਟੇਨਰ ਗਾਈਡ

ਇਹ ਪੰਨਾ ਸੰਖੇਪ ਵਿੱਚ ਦਰਸਾਉਂਦਾ ਹੈ ਕਿ API, CLI, ਅਤੇ ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ ਸਾਈਟ ਇਕੱਠੇ ਕਿਵੇਂ ਜੋੜੇ ਗਏ ਹਨ।

## ਪਬਲਿਕ API ਸੀਮਾ

ਸਥਿਰ Python API ਇਹਨਾਂ ਤੋਂ ਐਕਸਪੋਰਟ ਕੀਤੀ ਜਾਂਦੀ ਹੈ:

```python
co_op_translator.api
```

ਪਬਲਿਕ API ਨੂੰ ਸਮੱਗਰੀ ਅਨੁਵਾਦ ਸਹਾਇਕ, ਪਾਥ ਪੂਨਲਿਖਣ ਸਹਾਇਕ, ਪ੍ਰੋਜੈਕਟ ਪ੍ਰਬੰਧਨ, ਅਤੇ ਸਮੀਖਿਆ ਵਿੱਚ ਵਿਵਸਥਿਤ ਕੀਤਾ ਗਿਆ ਹੈ:

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

`TranslationStateProvider` ਹੋਸਟ ਕੀਤੀਆਂ ਇੰਟੇਗ੍ਰੇਸ਼ਨਾਂ ਲਈ ਡਾਟਾ ਟਿਕਾਊਪਨ ਦੀ ਸੀਮਾ ਹੈ।
ਇਹ ਬਣਾਏ ਗਏ ਉਮੀਦਵਾਰਾਂ ਨੂੰ ਮੰਨਿਆ ਗਿਆ ਬੇਸਲਾਈਨ ਤੋਂ ਵੱਖਰਾ ਰੱਖਣਾ ਚਾਹੀਦਾ ਹੈ ਤਾਂ ਕਿ ਇੱਕ
ਅਣਮਰਜ ਕੀਤੀ ਅਨੁਵਾਦ ਸੱਚਾਈ ਦਾ ਸਰੋਤ ਬਣ ਨਾ ਜਾਵੇ।

ਜਦੋਂ ਨਵੇਂ ਪਬਲਿਕ APIs ਜੋੜਦੇ ਹੋ, ਅਪਡੇਟ ਕਰੋ:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

ਨੀਚਲੇ-ਸਤਰ ਦੇ `core` ਮਾਡਿਊਲਾਂ ਨੂੰ ਸਥਿਰ API ਵਜੋਂ ਡੌਕਯੂਮੈਂਟ ਕਰਨ ਤੋਂ ਬਚੋ ਜਦ ਤੱਕ ਪ੍ਰੋਜੈਕਟ ਸਿੱਧੇ ਤੌਰ 'ਤੇ ਉਨ੍ਹਾਂ ਨੂੰ ਸਪੋਰਟ ਕਰਨ ਦੀ ਇੱਛਿਆ ਨਾ ਰੱਖਦਾ ਹੋਵੇ।

## CLI ਐਂਟਰੀ ਪੌਇੰਟ

ਪੈਕੇਜ ਇਹਨਾਂ Poetry ਸਕ੍ਰਿਪਟਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` ਸਕ੍ਰਿਪਟ ਨਾਂ ਦੇ ਅਧਾਰ 'ਤੇ ਡਿਸਪੈਚ ਕਰਦਾ ਹੈ:

- `translate` `co_op_translator.cli.translate.translate_command` ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ
- `evaluate` `co_op_translator.cli.evaluate.evaluate_command` ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ
- `migrate-links` `co_op_translator.cli.migrate_links.migrate_links_command` ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ
- `co-op-review` `co_op_translator.cli.review.review_command` ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ

`co-op-translator-mcp` `__main__.py` ਨੂੰ ਬਾਈਪਾਸ ਕਰਦਾ ਹੈ ਅਤੇ ਸਿੱਧਾ `co_op_translator.mcp.server:main` ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ।

CLI ਵਿਕਲਪ ਜੋੜਦੇ ਜਾਂ ਬਦਲਦੇ ਸਮੇਂ, ਅਪਡੇਟ ਕਰੋ:

- the relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- CLI-ਸੰਬੰਧੀ ਟੈਸਟ, ਜੇ ਵਿਵਹਾਰ ਬਦਲਦਾ ਹੈ

## MCP ਸਰਵਰ

MCP ਸਰਵਰ ਇਹਨਾਂ ਵਿੱਚ ਲਾਗੂ ਕੀਤਾ ਗਿਆ ਹੈ:

```python
co_op_translator.mcp.server
```

ਸਰਵਰ ਇਰਾਦਾਪੂਰਕ ਢੰਗ ਨਾਲ ਪਬਲਿਕ Python API ਨੂੰ ਰੈਪ ਕਰਦਾ ਹੈ ਨਾਂ ਕਿ ਨੀਚਲੇ-ਸਤਰ ਦੇ `core` ਮਾਡਿਊਲਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਦੇ। ਇਸ ਸੀਮਾ ਨੂੰ ਅਖੰਡ ਰੱਖੋ ਤਾਂ ਜੋ MCP ਕਲਾਇੰਟਾਂ, Python ਕਾਲਰਾਂ, ਅਤੇ CLI ਇੱਕੋ ਵਹਿਵਾਰ ਸਾਂਝਾ ਕਰਨ।

MCP ਟੂਲ ਜੋੜਦੇ ਜਾਂ ਬਦਲਦੇ ਸਮੇਂ, ਅਪਡੇਟ ਕਰੋ:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

ਰਿਪੋਜ਼ਿਟਰੀ ਅਨੁਵਾਦ ਟੂਲ MCP ਰਾਹੀਂ ਮਾਡਲ-ਕਾਲੇਬਲ ਹੁੰਦੇ ਹਨ ਅਤੇ ਕਈ ਫਾਇਲਾਂ ਲਿਖ ਸਕਦੇ ਹਨ। ਡਿਫੋਲਟ ਵਜੋਂ `dry_run=True` ਰੱਖੋ ਅਤੇ ਗੈਰ-dry-run ਪ੍ਰੋਜੈਕਟ ਅਨੁਵਾਦ ਤੋਂ ਪਹਿਲਾਂ `confirm_write=True` ਦੀ ਲੋੜ ਰੱਖੋ।

## ਅਨੁਵਾਦ ਪ੍ਰਵਾਹ

ਉੱਚ-ਸਤਰ ਪ੍ਰੋਜੈਕਟ ਅਨੁਵਾਦ ਪ੍ਰਵਾਹ ਇਹ ਹੈ:

1. CLI ਆਰਗੂਮੈਂਟ ਜਾਂ API ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਪਾਰਸ ਕਰੋ।
2. `LLMConfig` ਨਾਲ LLM ਸੰਰਚਨਾ ਦੀ ਜਾਂਚ ਕਰੋ।
3. ਜਦੋਂ ਇਮੇਜ ਅਨੁਵਾਦ ਚੁਣਿਆ ਗਿਆ ਹੋਵੇ ਤਾਂ Azure AI Vision ਦੀ ਜਾਂਚ ਕਰੋ।
4. ਭਾਸ਼ਾ ਕੋਡਾਂ ਨੂੰ ਨਾਰਮਲਾਈਜ਼ ਕਰੋ।
5. ਲੈਗਸੀ ਭਾਸ਼ਾ ਫੋਲਡਰ ਉਪਨਾਮਾਂ ਦੀ ਪਹਿਚਾਣ ਕਰੋ।
6. ਅਨੁਵਾਦ ਦੀ ਮਾਤਰਾ ਦਾ ਅੰਦਾਜ਼ਾ ਲਗਾਓ।
7. ਜਦੋਂ ਲਾਗੂ ਹੋਵੇ ਤਾਂ README ਦੀ ਭਾਸ਼ਾ/ਕੋਰਸ ਸੈਕਸ਼ਨਾਂ ਨੂੰ ਅਪਡੇਟ ਕਰੋ।
8. ਪ੍ਰੋਜੈਕਟ ਅਨੁਵਾਦ `ProjectTranslator` ਨੂੰ ਸੌਂਪੋ।
9. `ProjectTranslator` ਫਾਈਲ ਪ੍ਰੋਸੈਸਿੰਗ ਨੂੰ `TranslationManager` ਨੂੰ ਸੌਂਪਦਾ ਹੈ।

`TranslationManager` ਕੇਂਦ੍ਰਿਤ ਫਾਈਲ-ਟਾਈਪ ਮਿਕਸੀਨ ਤੋਂ ਬਣਿਆ ਹੈ:

- `ProjectMarkdownTranslationMixin` Markdown ਫਾਈਲ ਪੜ੍ਹਨ, ਸਮੱਗਰੀ ਅਨੁਵਾਦ, ਪਾਥ ਪੂਨਲਿਖਣ, ਮੈਟਾਡੇਟਾ, ਡਿਸਕਲੇਮਰ, ਅਤੇ ਲਿਖਾਈਆਂ ਸੰਭਾਲਦਾ ਹੈ।
- `ProjectNotebookTranslationMixin` ਨੋਟਬੁੱਕ ਫਾਈਲ ਪੜ੍ਹਨ, Markdown-ਸੈੱਲ ਅਨੁਵਾਦ, ਪਾਥ ਪੂਨਲਿਖਣ, ਮੈਟਾਡੇਟਾ, ਡਿਸਕਲੇਮਰ, ਅਤੇ ਲਿਖਾਈਆਂ ਸੰਭਾਲਦਾ ਹੈ।
- `ProjectImageTranslationMixin` ਇਮੇਜ ਦੀ ਖੋਜ, ਟੈਕਸਟ ਨਿਕਾਲਣ/ਅਨੁਵਾਦ, ਰੇਂਡਰ ਕੀਤੇ ਇਮੇਜ ਲਿਖਾਈਆਂ, ਅਤੇ ਮੈਟਾਡੇਟਾ ਸੰਭਾਲਦਾ ਹੈ।

ਨੀਵਾਂ-ਸਤਰ ਸਮੱਗਰੀ API ਪ੍ਰੋਜੈਕਟ ਵਰਕਫਲੋ ਨੂੰ ਛੱਡ ਦਿੰਦੇ ਹਨ:

1. `translate_markdown_content` ਅਤੇ `translate_notebook_content` ਸਿਰਫ਼ ਮੇਮਰੀ ਅੰਦਰਲੀ ਸਮੱਗਰੀ ਦਾ ਅਨੁਵਾਦ ਕਰਦੇ ਹਨ।
2. `translate_image_content` ਇੱਕ ਹੀ ਇਮੇਜ ਵਿੱਚ ਟੈਕਸਟ ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ ਅਤੇ ਇੱਕ ਰੇਂਡਰ ਕੀਤਾ ਹੋਇਆ ਇਮੇਜ ਓਬਜੈਕਟ ਵਾਪਸ ਕਰਦਾ ਹੈ।
3. `rewrite_markdown_paths` ਅਤੇ `rewrite_notebook_paths` ਖਾਸ ਪੋਸਟ-ਪ੍ਰੋਸੈਸਿੰਗ ਸਹਾਇਕ ਹਨ। ਇਹ ਕੋਈ ਅਨੁਵਾਦ ਜਾਂ ਪ੍ਰੋਜੈਕਟ ਲਿਖਾਈ ਨਹੀਂ ਕਰਦੇ।

## ਸਮੀਖਿਆ ਪ੍ਰਵਾਹ

ਨਿਰਧਾਰਿਤ ਸਮੀਖਿਆ ਪ੍ਰਵਾਹ ਇਹ ਹੈ:

1. CLI ਆਰਗੂਮੈਂਟ ਜਾਂ API ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਪਾਰਸ ਕਰੋ।
2. ਮੰਗੇ ਗਏ ਭਾਸ਼ਾ ਕੋਡਾਂ ਨੂੰ ਨਾਰਮਲਾਈਜ਼ ਕਰੋ।
3. `root_dir`, `root_dirs`, ਜਾਂ `groups` ਤੋਂ ਇੱਕ ਜਾਂ ਵੱਧ ਸਮੀਖਿਆ ਟਾਰਗਟ ਬਣਾਓ।
4. ਵਿਕਲਪਕ ਤੌਰ 'ਤੇ ਸੋਰਸ ਫਾਈਲਾਂ ਨੂੰ `--changed-from` ਨਾਲ ਸੀਮਿਤ ਕਰੋ।
5. ਸਟ੍ਰੱਕਚਰ, ਅਨੁਵਾਦ ਤਾਜਗੀ, Markdown ਅਖੰਡਤਾ, ਅਤੇ ਲੋਕਲ ਲਿੰਕ/ਇਮੇਜ ਪਾਥਾਂ ਲਈ ਨਿਰਧਾਰਿਤ ਚੈੱਕ ਚਲਾਓ।
6. ਜਾਂ ਤਾਂ ਟੈਕਸਟ ਆਊਟਪੁੱਟ ਪ੍ਰਿੰਟ ਕਰੋ ਜਾਂ GitHub-ਫਲੇਵਰਡ Markdown।
7. ਜਦੋਂ ਸਮੀਖਿਆ ਦੀਆਂ ਗਲਤੀਆਂ ਮਿਲਦੀਆਂ ਹਨ ਤਾਂ ਫੇਲ ਨਾਲ ਐਗਜ਼ਿਟ ਕਰੋ।

ਸਮੀਖਿਆ ਪ੍ਰਵਾਹ ਲਈ API ਕੀਜ਼ ਲੋੜੀਂਦੀਆਂ ਨਹੀਂ ਹਨ ਅਤੇ ਇਹ ਲੋਕਲ ਚੈੱਕ ਜਾਂ opt-in consumer CI ਲਈ ਉਪਲਬਧ ਰਹਿੰਦਾ ਹੈ। ਇਹ ਰਿਪੋਜ਼ਿਟਰੀ ਹਰ ਪુલ ਰਿਕਵੇਸਟ 'ਤੇ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ `co-op-review` ਨਹੀਂ ਚਲਾਂਦੀ।

## ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ ਸਾਈਟ

ਡੌਕਸ ਸਾਈਟ ਦੀ ਸੰਰਚਨਾ ਇਹਨਾਂ ਦੁਆਰਾ ਕੀਤੀ ਜਾਂਦੀ ਹੈ:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` ਡਾਇਰੈਕਟਰੀ ਪ੍ਰਮਾਣਿਕ ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ ਸੋਰਸ ਹੈ। ਇਸ ਡਾਇਰੈਕਟਰੀ ਤੋਂ ਬਾਹਰ ਨਵੇਂ end-user ਗਾਈਡਸ ਨਾ ਜੋੜੋ ਜਦ ਤਕ ਪ੍ਰੋਜੈਕਟ ਜਾਣ-ਬੂਝ ਕੇ ਹੋਰ ਕੋਈ ਪ੍ਰਕਾਸ਼ਿਤ ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ ਸਤਹ ਨਹੀਂ ਲਿਆਉਂਦਾ।

ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਬਣਾਓ:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

ਲੋਕਲ ਪ੍ਰੀਵਿਊ:

```bash
python -m mkdocs serve
```

ਜਨਰੇਟ ਕੀਤੀ ਸਾਈਟ `site/` ਵਿੱਚ ਲਿਖੀ ਜਾਂਦੀ ਹੈ, ਜੋ git ਵੱਲੋਂ ਨਜ਼ਰਅੰਦਾਜ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।

## GitHub Pages ਵਰਕਫਲੋ

`.github/workflows/docs.yml` ਪูล ਰਿਕਵੇਸਟਾਂ 'ਤੇ ਸਾਈਟ ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ `main` 'ਤੇ ਪੁਸ਼ ਹੋਣ ਤੇ ਡੀਪਲੋਏ ਕਰਦਾ ਹੈ।

ਵਰਕਫਲੋ ਇਹਨਾਂ ਨੂੰ ਇੰਸਟਾਲ ਕਰਦਾ ਹੈ:

```bash
pip install -r requirements-docs.txt
```

ਡੌਕਸ ਵਰਕਫਲੋ ਸਿਰਫ ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ ਟੂਲਚੇਨ ਨੂੰ ਇੰਸਟਾਲ ਕਰਦਾ ਹੈ। `mkdocs.yml` `mkdocstrings` ਨੂੰ `src/` ਵੱਲ ਪੋਇੰਟ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ ਪਬਲਿਕ API ਪੇਜ਼ ਸੋਰਸ ਟ੍ਰੀ ਤੋਂ ਰੇਂਡਰ ਕੀਤੇ ਜਾ ਸਕਣ ਬਿਨਾਂ ਪੂਰੇ ਰਨਟਾਈਮ ਡਿਪੇਂਡੈਂਸੀ ਸੈੱਟ ਨੂੰ ਇੰਸਟਾਲ ਕੀਤੇ। ਜੇ ਅਗਲੇ API ਡੌਕਸ ਨੂੰ ਬਿਲਡ ਦੌਰਾਨ ਵਿਕਲਪਿਕ ਰਨਟਾਈਮ ਪ੍ਰਦਾਤਿਆਂ ਨੂੰ ਇੰਪੋਰਟ ਕਰਨ ਦੀ ਲੋੜ ਪੈ ਸਕਦੀ ਹੈ, ਤਾਂ `.github/workflows/docs.yml` ਅਤੇ ਇਹ ਗਾਈਡ ਦੋਹਾਂ ਨੂੰ ਅਪਡੇਟ ਕਰੋ।

## ਡੌਕਸ ਗੁਣਵੱਤਾ ਬਾਰ

ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ ਬਦਲਾਵ ਮਿਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ, ਚਲਾਓ:

```bash
python -m mkdocs build --strict
git diff --check
```

ਕਠੋਰ ਬਿਲਡ ਵਰਤੋਂ ਤਾਂ ਜੋ ਟੁਟੇ ਹੋਏ ਲਿੰਕ, ਗਲਤ ਨੈਵੀਗੇਸ਼ਨ ਐਂਟਰੀਜ਼, ਅਤੇ API ਰੇਂਡਰਿੰਗ ਸਮੱਸਿਆਵਾਂ ਜਲਦੀ ਫੇਲ ਹੋ ਜਾਣ।