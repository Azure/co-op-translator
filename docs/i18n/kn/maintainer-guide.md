# ನಿರ್ವಹಕರ ಮಾರ್ಗದರ್ಶಿ

ಈ ಪುಟವು API, CLI ಮತ್ತು ಡಾಕ್ಯುಮೆಂಟೇಷನ್ ಸೈಟ್ ಹೇಗೆ ಒಟ್ಟಿಗೆ ಸಂಯೋಜಿತವಾಗಿವೆ ಎಂಬುದನ್ನು ಸಾರುತ್ತದೆ.

## ಸಾರ್ವಜನಿಕ API ಗಡಿ

ಸ್ಥಿರ Python API ಈ ಜಾಗದಿಂದ ರಫ್ತು ಮಾಡಲ್ಪಡುತ್ತದೆ:

```python
co_op_translator.api
```

ಸಾರ್ವಜನಿಕ API ಅನ್ನು ವಿಷಯ ಅನುವಾದ ಸಹಾಯಕರ, ಮಾರ್ಗ ಪುನರ್ಲಿಖನ ಸಹಾಯಕರ, ಪ್ರಾಜೆಕ್ಟ್ ನಿರ್ವಹಣೆ, ಮತ್ತು ವಿಮರ್ಶೆ ರೂಪದಲ್ಲಿ ಸಂಘಟಿಸಲಾಗುತ್ತದೆ:

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

`TranslationStateProvider` ಹೋಸ್ಟೆಡ್ ಇಂಟಿಗ್ರೇಶನ್‌ಗಳಿಗಾಗಿ ಸ್ಥಾಯಿತ್ವ ಗಡಿಯಾಗಿದೆ.
ಅದು ಉತ್ಪಾದಿತ ಅಭ್ಯರ್ಥಿಗಳನ್ನು ಅಂಗೀಕೃತ ಆಧಾರರೇಖೆಗಳಿಂದ ಪ್ರತ್ಯೇಕವಾಗಿ ಇರಿಸಬೇಕು, ಆದ್ದರಿಂದ ಒಂದು
ಮರ್ಜ್ ಆಗದ ಅನುವಾದವು ಸತ್ಯದ ಮೂಲವಾಗಬಾರದು.

ಹೊಸ ಸಾರ್ವಜನಿಕ APIಗಳನ್ನು ಸೇರಿಸಿದಾಗ, ನವೀಕರಿಸಿ:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- `tests/co_op_translator/` ಅಡಿ ಸಂಬಂಧಿಸಿದ API ಪರೀಕ್ಷೆಗಳು, ಉದಾಹರಣೆಗೆ `test_api.py` ಅಥವಾ `test_review_api.py`

ಪ್ರಾಜೆಕ್ಟ್ ಅದನ್ನು ನೇರವಾಗಿ ಬೆಂಬಲಿಸಲು ಉದ್ದೇಶವಿಲ್ಲದಿದ್ದರೆ ಕಡಿಮೆ-ಮಟ್ಟದ `core` ಮೋಡ್ಯೂಲ್‌ಗಳನ್ನು ಸ್ಥಿರ API ಎಂದು ದಾಖಲುಮಾಡಬೇಡಿ.

## CLI ಪ್ರವೇಶ ಬಿಂದುಗಳು

ಪ್ಯಾಕೇಜ್ ಈ Poetry ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳನ್ನು ನಿರ್ಧರಿಸುತ್ತದೆ:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` ಸ್ಕ್ರಿಪ್ಟ್ ಹೆಸರಿನ ಮೂಲಕ ಡಿಸ್ಪ್ಯಾಚ್ ಮಾಡುತ್ತದೆ:

- `translate` `co_op_translator.cli.translate.translate_command` ಅನ್ನು ಕರೆ ಮಾಡುತ್ತದೆ
- `evaluate` `co_op_translator.cli.evaluate.evaluate_command` ಅನ್ನು ಕರೆ ಮಾಡುತ್ತದೆ
- `migrate-links` `co_op_translator.cli.migrate_links.migrate_links_command` ಅನ್ನು ಕರೆ ಮಾಡುತ್ತದೆ
- `co-op-review` `co_op_translator.cli.review.review_command` ಅನ್ನು ಕರೆ ಮಾಡುತ್ತದೆ

`co-op-translator-mcp` `__main__.py` ಅನ್ನು ಬಾಯ್‌ಪಾಸ್ ಮಾಡಿ ನೇರವಾಗಿ `co_op_translator.mcp.server:main` ಅನ್ನು ಕರೆ ಮಾಡುತ್ತದೆ.

CLI ಆಯ್ಕೆಗಳನ್ನು ಸೇರಿಸುವಾಗ ಅಥವಾ ಬದಲಾಯಿಸುವಾಗ, ನವೀಕರಿಸಿ:

- ಸಂಬಂಧಿಸಿದ `src/co_op_translator/cli/*.py` ಕಮಾಂಡ್
- `docs/cli.md`
- ವರ್ತನೆ ಬದಲಾಗಿದರೆ CLI ಸಂಬಂಧಿತ ಪರೀಕ್ಷೆಗಳು

## MCP server

MCP ಸರ್ವರ್ ಈ ಕಡತಗಳಲ್ಲಿ ಅನುಷ್ಠಾನಗೊಳಿಸಲಾಗಿದೆ:

```python
co_op_translator.mcp.server
```

ಸರ್ವರ್ ಉದ್ದೇಶಪೂರ್ವಕವಾಗಿ ಸಾರ್ವಜನಿಕ Python API ಅನ್ನು ರ್ಯಾಪ್ ಮಾಡುತ್ತದೆ, ಕಡಿಮೆ-ಮಟ್ಟದ `core` ಮೋಡ್ಯೂಲ್‌ಗಳನ್ನು ನೇರವಾಗಿ ಕರೆ ಮಾಡುವ ಬದಲು. MCP ಕ್ಲೈಂಟ್‌ಗಳು, Python ಕರೆಮಾಡುವವರು ಮತ್ತು CLI ಒಂದೇ ವರ್ತನೆಯನ್ನು ಹಂಚಿಕೊಳ್ಳಲು ಈ ಗಡಿಯನ್ನು ಅಕ್ಷುಣ್‌ಮಾಡಿ.

MCP ಉಪಕರಣಗಳನ್ನು ಸೇರಿಸುವಾಗ ಅಥವಾ ಬದಲಾಯಿಸುವಾಗ, ನವೀಕರಿಸಿ:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` ಸಾರ್ವಜನಿಕ API ಮೇಲ್ಮೈ ಬದಲಾಗಿದ್ದಲ್ಲಿ

ರಿಪೊಸಿಟರಿ ಅನುವಾದ ಸಾಧನಗಳು MCP ಮೂಲಕ ಮಾದರಿಗೆ ಕರೆಮಾಡಬಹುದಾಗಿವೆ ಮತ್ತು ಹಲವಾರು ಫೈಲ್‌ಗಳನ್ನು ಬರೆಯಬಹುದು. ಡೀಫಾಲ್ಟ್ ಆಗಿ `dry_run=True` ಇರಲಿ ಮತ್ತು ಡ್ರೈ-ರನ್ ಅಲ್ಲದ ಪ್ರಾಜೆಕ್ಟ್ ಅನುವಾದಕ್ಕೂ ಮುನ್ನ `confirm_write=True` ಇರಬೇಕು.

## ಅನುವಾದ ಪ್ರಕ್ರಿಯೆ

ಪ್ರಾಜೆಕ್ಟ್ ಅನುವಾದದ ಉನ್ನತ-ಮಟ್ಟದ ಕಾರ್ಯಪ್ರವಾಹ ಹೀಗಿದೆ:

1. CLI arguments or API parameters ಅನ್ನು ಪಾರ್ಸ್ ಮಾಡಿ.
2. `LLMConfig` ಮೂಲಕ LLM ಸಂರಚನೆಯನ್ನು ಪರಿಶೀಲಿಸಿ.
3. ಚಿತ್ರ ಅನುವಾದ ಆಯ್ಕೆ ಮಾಡಿದಾಗ Azure AI Vision ಅನ್ನು ಪರಿಶೀಲಿಸಿ.
4. ಭಾಷಾ ಕೋಡ್‌ಗಳನ್ನು ಸಾಮಾನ್ಯೀಕರಿಸಿ.
5. ಹಳೆಯ ಭಾಷಾ ಫೋಲ್ಡರ್ ಮರುನಾಮಗಳನ್ನು ಕಂಡುಹಿಡಿ.
6. ಅನುವಾದ ಪ್ರಮಾಣವನ್ನು ಅಂದಾಜುಮಾಡಿ.
7. ಅನ್ವಯಿಸಿದರೆ README ಭಾಷೆ/ಕೋರ್ಸ್ ವಿಭಾಗಗಳನ್ನು ನವೀಕರಿಸಿ.
8. ಪ್ರಾಜೆಕ್ಟ್ ಅನುವಾದವನ್ನು `ProjectTranslator` ಗೆ ನಿಯೋಜಿಸಿ.
9. `ProjectTranslator` ಫೈಲ್ ಪ್ರಕ್ರಿಯೆಯನ್ನು `TranslationManager` ಗೆ ನಿಯೋಜಿಸುತ್ತದೆ.

`TranslationManager` ನಿರ್ದಿಷ್ಟ ಫೈಲ್-ಪ್ರಕಾರ ಮಿಕ್ಸಿನ್‌ಗಳಿಂದ ರಚಿಸಲಾಗಿದೆ:

- `ProjectMarkdownTranslationMixin` Markdown ಫೈಲ್ ಓದಿಗಳು, ವಿಷಯ ಅನುವಾದ, ಪಥ ಪುನರ್ಲಿಖನ, ಮೆಟಾಡೇಟಾ, ನಿರಾಕರಣಾ ಪ್ರಕಟಣೆಗಳು ಮತ್ತು ಬರವಣಿಗೆಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ.
- `ProjectNotebookTranslationMixin` ನೋಟ್‌ಬುಕ್ ಫೈಲ್ ಓದಿಗಳು, Markdown-ಸೆಲ್ ಅನುವಾದ, ಮಾರ್ಗ ಪುನರ್ಲಿಖನ, ಮೆಟಾಡೇಟಾ, ನಿರಾಕರಣಾ ಪ್ರಕಟಣೆಗಳು ಮತ್ತು ಬರವಣಿಗೆಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ.
- `ProjectImageTranslationMixin` ಚಿತ್ರ ಅನ್ವೇಷಣೆ, ಪಠ್ಯ ತೆಗೆಯುವಿಕೆ/ಅನುವಾದ, ರೆಂಡರ್ ಮಾಡಿದ ಚಿತ್ರ ಬರವಣಿಗೆಗಳು ಮತ್ತು ಮೆಟಾಡೇಟಾ ನಿರ್ವಹಿಸುತ್ತದೆ.

ಕೆಳಮಟ್ಟದ ವಿಷಯ APIಗಳು ಪ್ರಾಜೆಕ್ಟ್ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಬಿಟ್ಟುಹೋಗುತ್ತವೆ:

1. `translate_markdown_content` ಮತ್ತು `translate_notebook_content` ಮೆಮೊರಿಯಲ್ಲಿ ಇರುವ ವಿಷಯವನ್ನು ಮಾತ್ರ ಅನುವಾದಿಸುತ್ತವೆ.
2. `translate_image_content` ಒಂದೇ ಚಿತ್ರದಲ್ಲಿನ ಪಠ್ಯವನ್ನು ಅನುವಾದಿಸಿ ರೆಂಡರ್ ಮಾಡಿದ ಚಿತ್ರ ವಸ್ತುವನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ.
3. `rewrite_markdown_paths` ಮತ್ತು `rewrite_notebook_paths` ಸ್ಪಷ್ಟವಾದ ಪೋಸ್ಟ್-ಪ್ರೋಸೆಸಿಂಗ್ ಸಹಾಯಕರಾಗಿವೆ. ಅವು ಅನುವಾದವನ್ನೂ ಪ್ರಾಜೆಕ್ಟ್ ಬರವಣಿಗೆಯನ್ನೂ ನಡೆಸುವುದಿಲ್ಲ.

## ಪರಿಶೀಲನೆ ಪ್ರಕ್ರಿಯೆ

The deterministic review flow is:

1. CLI ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳು ಅಥವಾ API ಪರಾಮೀಟರ್ಗಳನ್ನು ಪಾರ್ಸ್ ಮಾಡಿ.
2. ವಿನಂತಿಸಿದ ಭಾಷಾ ಕೋಡ್‌ಗಳನ್ನು ಸಾಮಾನ್ಯೀಕರಿಸಿ.
3. `root_dir`, `root_dirs`, ಅಥವಾ `groups` ನಿಂದ ಒಂದು ಅಥವಾ ಹೆಚ್ಚಿನ ವಿಮರ್ಶಾ ಗುರಿಗಳನ್ನು ರಚಿಸಿ.
4. ಐಚ್ಛಿಕವಾಗಿ `--changed-from` ಬಳಸಿ ಮೂಲ ಫೈಲ್‌ಗಳನ್ನು ಸೀಮಿತಗೊಳಿಸಿರಿ.
5. ರಚನೆ, ಅನುವಾದದ ನವೀನತೆ, Markdown ಅಖಂಡತೆ, ಮತ್ತು ಸ್ಥಳೀಯ ಲಿಂಕ್/ಚಿತ್ರ ಮಾರ್ಗಗಳಿಗಾಗಿ ನಿರ್ಧಾರಾತ್ಮಕ ಪರಿಶೀಲನೆಗಳನ್ನು ನಡೆಸಿ.
6. ಪಠ್ಯ ಔಟ್ಪುಟ್ ಅಥವಾ GitHub-ಶೈಲಿಯ Markdown ಯಾವುದನ್ನಾದರೂ ಮುದ್ರಿಸಿ.
7. ವಿಮರ್ಶಾ ದೋಷಗಳು ಕಂಡುಬಂದರೆ ವಿಫಲ ಸ್ಥಿತಿಯೊಂದಿಗೆ ನಿರ್ಗಮಿಸಿರಿ.

ವಿಮರ್ಶೆ ಪ್ರಕ್ರಿಯೆಗೆ API ಕೀ ಅಗತ್ಯವಿಲ್ಲ ಮತ್ತು ಇದು ಸ್ಥಳೀಯ ಪರಿಶೀಲನೆಗಳಿಗೆ ಅಥವಾ ಓಪ್ಟ್-ಇನ್ ಗ್ರಾಹಕ CI ಗೆ ಲಭ್ಯವಿರುತ್ತದೆ. ಈ ರೆಪೊ ಪ್ರತಿಯೊಂದು pull request ಮೇಲೆ `co-op-review` ಅನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಚಲಿಸುವುದಿಲ್ಲ.

## ಡಾಕ್ಯುಮೆಂಟೇಷನ್ ತಾಣ

ಡಾಕ್ಸ್ ಸೈಟ್ ಈ ಕಡತಗಳ ಮೂಲಕ ಕಾನ್ಫಿಗರ್ ಮಾಡಲಾಗಿದೆ:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` ಡೈರೆಕ್ಟರಿ ಪ್ರಾಮಾಣಿಕ ಡಾಕ್ಯುಮೆಂಟ್ ಮೂಲವಾಗಿದೆ. ಪ್ರಾಜೆಕ್ಟ್ ಉದ್ದೇಶಪೂರ್ವಕವಾಗಿ ಮತ್ತೊಂದು ಪ್ರಕಟಿತ ಡಾಕ್ಯುಮೆಂಟ್ ಮೋಡಲನ್ನು ಪರಿಚಯಿಸದಿದ್ದರೆ ಈ ಡೈರೆಕ್ಟರಿಯ ಹೊರಗೆ ಹೊಸ ಅಂತಿಮ ಬಳಕೆದಾರ ಮಾರ್ಗದರ್ಶಿಗಳನ್ನು ಸೇರಿಸಬೇಡಿ.

Build locally:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview locally:

```bash
python -m mkdocs serve
```

ಉತ್ಪಾದಿತ ಸೈಟ್ `site/` ಗೆ ಬರೆಯಲಾಗುತ್ತದೆ, ಇದು git ಮೂಲಕ ನಿರ್ಲಕ್ಷ್ಯಗೊಳ್ಳುತ್ತದೆ.

## GitHub Pages ಕಾರ್ಯಪ್ರವಾಹ

`.github/workflows/docs.yml` ಪುಲ್ ರಿಕ್ವೆಸ್ಟ್‌ಗಳ ಮೇಲೆ ಸೈಟ್ ಅನ್ನು ನಿರ್ಮಿಸುತ್ತದೆ ಮತ್ತು `main` ಗೆ ಪುಷ್ ಆದಾಗ ಅದನ್ನು ವೆಬ್‌ಗೆ ಪ್ರಸಾರಗೊಳಿಸುತ್ತದೆ.

The workflow installs:

```bash
pip install -r requirements-docs.txt
```

ಡಾಕ್ಸ್ ವರ್ಕ್‌ಫ್ಲೋ ಮಾತ್ರ ಡಾಕ್ಯುಮೆಂಟೇಷನ್ ಟೂಲ್‌ಚೈನ್ ಅನ್ನು ಸ್ಥಾಪಿಸುತ್ತದೆ. `mkdocs.yml` `mkdocstrings` ಅನ್ನು `src/` ಕಡೆಗೆ ತೋರಿಸುತ್ತದೆ, ಆದ್ದರಿಂದ ಸಾರ್ವಜನಿಕ API ಪುಟಗಳನ್ನು ಪೂರ್ಣ runtime ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸದೆ ಮೂಲ ಸ್ರೋತದಿಂದ ರೆಂಡರ್ ಮಾಡಬಹುದು. ಭವಿಷ್ಯದ API ಡಾಕ್ಸ್ ನಿರ್ಮಾಣದ ವೇಳೆ ಐಚ್ಛಿಕ runtime ಪೂರೈಕೆದಾರರನ್ನು ಆಮದು ಮಾಡಬೇಕಾಗಿದ್ದರೆ, `.github/workflows/docs.yml` ಮತ್ತು ಈ ಮಾರ್ಗದರ್ಶಿಯನ್ನು തമ്മಿನಲ್ಲಿ ನವೀಕರಿಸಿ.

## ಡಾಕ್ಸ್ ಗುಣಮಟ್ಟ ಮಾನದಂಡ

ಡಾಕ್ಯುಮೆಂಟೇಷನ್ ಬದಲಾವಣೆಗಳನ್ನು ಮರ್ಜ್ ಮಾಡುವ ಮೊದಲು, ಓಡಿಸಿ:

```bash
python -m mkdocs build --strict
git diff --check
```

ಸಮಸ್ಯೆಗೊಳಗಾದ ಲಿಂಕ್‌ಗಳು, ಅಮಾನ್ಯ ನ್ಯಾವಿಗೇಶನ್ ಎಂಟ್ರಿಗಳು ಮತ್ತು API ರೆಂಡರಿಂಗ್ ಸಮಸ್ಯೆಗಳು ವಾಗ್ದಾನಿತವಾಗುವುದಕ್ಕಾಗಿ ಕಠಿಣ ಬಿಲ್ಡ್ಗಳನ್ನು ಬಳಸಿ.