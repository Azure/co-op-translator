# ನಿರ್ವಹಣಾ ಮಾರ್ಗದರ್ಶಿ

ಈ ಪುಟವು API, CLI, ಮತ್ತು ದಸ್ತಾವೇಜು ತಾಣವು ಹೇಗೆ miteinander ಜೋಡಿಸಲಾಗಿದೆ ಎಂಬುದನ್ನು ಸಾರುತ್ತದೆ.

## ಸಾರ್ವಜನಿಕ API ಗಡಿ

ಸ್ಥಿರ Python API ಈ ಮೂಲಕ ರಫ್ತು ಮಾಡಲ್ಪಡುತ್ತದೆ:

```python
co_op_translator.api
```

ಸಾರ್ವಜನಿಕ API ಅನ್ನು ವಿಷಯ ಅನುವಾದ ಸಹಾಯಕರು, ಪಾಥ್ ಪುನರ್ರಚಿಸುವ ಸಹಾಯಕರು, ಪ್ರಾಜೆಕ್ಟ್ ಸಂಯೋಜನೆ, ಮತ್ತು ವಿಮರ್ಶೆ ಎಂದು ಸಂಘಟಿಸಲಾಗಿದೆ:

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

ಹೊಸ ಸಾರ್ವಜನಿಕ APIಗಳನ್ನು ಸೇರಿಸುವಾಗ, ಈ ಕೆಳಕಂಡುವನ್ನು ನವೀಕರಿಸಿ:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- ಸಂಬಂಧಿತ API ಪರೀಕ್ಷೆಗಳು `tests/co_op_translator/` ಅಡಿಯಲ್ಲಿ, ಉದಾಹರಣೆಗೆ `test_api.py` ಅಥವಾ `test_review_api.py`

ಪ್ರಾಜೆಕ್ಟ್ ಅವುಗಳನ್ನು ನೇರವಾಗಿ ಬೆಂಬಲಿಸಲು ಉದ್ದೇಶಿಸಿಲ್ಲದಿದ್ದರೆ ಕಡಿಮೆ-ಮಟ್ಟದ `core` ಮód್ಯೂಲ್ಗಳನ್ನು ಸ್ಥಿರ API ಆಗಿ ದಾಖಲೆ ಮಾಡಲು ಎಚ್ಛಿಸಬೇಡಿ.

## CLI ಪ್ರವೇಶ ಬಿಂದುಗಳು

ಪ್ಯಾಕೇಜ್ ಈ Poetry ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುತ್ತದೆ:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` ಸ್ಕ್ರಿಪ್ಟ್ ಹೆಸರಿನ ಪ್ರಕಾರ ಪ್ರಸರಣ ಮಾಡುವುದಾಗಿದೆ:

- `translate` ಕರೆಮಾಡುತ್ತದೆ `co_op_translator.cli.translate.translate_command`
- `evaluate` ಕರೆಮಾಡುತ್ತದೆ `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` ಕರೆಮಾಡುತ್ತದೆ `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` ಕರೆಮಾಡುತ್ತದೆ `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` `__main__.py` ಅನ್ನು ಬೈಸ್ಪಾಸ್ ಮಾಡಿ ನೇರವಾಗಿ `co_op_translator.mcp.server:main` ಅನ್ನು ಕರೆಮಾಡುತ್ತದೆ.

CLI ಆಯ್ಕೆಗಳನ್ನು ಸೇರಿಸುವಾಗ ಅಥವಾ ಬದಲಾಯಿಸುವಾಗ, ಈಗಳನ್ನು ನವೀಕರಿಸಿ:

- ಸಂಬಂಧಿತ `src/co_op_translator/cli/*.py` ಕಮಾಂಡ್
- `docs/cli.md`
- CLI ಸಂಬಂಧಿತ ಟೆಸ್ಟ್‌ಗಳು, ಕ್ರಮಾಚರಣೆ ಬದಲಾಗುವಲ್ಲಿ

## MCP ಸರ್ವರ್

MCP ಸರ್ವರ್ಗೆ ಅನುಷ್ಠಾನ ಈಲ್ಲಿ ಇದೆ:

```python
co_op_translator.mcp.server
```

ಸರ್ವರ್ ಉದ್ದೇಶಪೂರ್ವಕವಾಗಿ ಕಡಿಮೆ-ಮಟ್ಟದ `core` ಮód್ಯೂಲ್ಗಳನ್ನು ಕರೆಮಾಡುವುದಲ್ಲದೆ ಸಾರ್ವಜನಿಕ Python API ಅನ್ನು ಆವರಿಸುತ್ತವೆ. ಈ ಗಡಿಯನ್ನು ಅಹಿತಕರವಾಗದಂತೆ ಇಡಿರಿ zodat MCP ಕ್ಲೈಂಟ್‌ಗಳು, Python ಕರೆಮಾಡುವವರು, ಮತ್ತು CLI ಒಂದೇ ನಡವಳಿಕೆಯನ್ನು ಹಂಚಿಕೊಳ್ಳುತ್ತವೆ.

MCP ಉಪಕರಣಗಳನ್ನು ಸೇರಿಸುವಾಗ ಅಥವಾ ಬದಲಾಯಿಸುವಾಗ, ಈಗಳನ್ನು ನವೀಕರಿಸಿ:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- ಸಾರ್ವಜನಿಕ API ಮೇಲ್ಮೈ ಬದಲಾಗಿದೆಯಾದರೆ `docs/api.md`

ರೆಪೊಸಿಟರಿ ಅನುವಾದ ಉಪಕರಣಗಳು MCP ಮೂಲಕ ಮಾದರಿ-ಕರೆಮಾಡಬಹುದಾಗಿದ್ದು ಮತ್ತು ಬಹುಕಾಲಿನ ಫೈಲುಗಳನ್ನು ಬರೆಯಬಹುದು. ಡೀಫಾಲ್ಟ್ ಆಗಿ `dry_run=True` ಇಡುವುದನ್ನು ಕಾಪಾಡಿ ಮತ್ತು ನಾನ್-ಡ್ರೈ-ರನ್ ಪ್ರಾಜೆಕ್ಟ್ ಅನುವಾದದ ಮೊದಲು `confirm_write=True` ಅನ್ನು ಆವಶ್ಯಕವಾಗಿರಿ.

## ಅನುವಾದ ಪ್ರವಾಹ

ಹೈ-ಲೆವೆಲ್ ಪ್ರಾಜೆಕ್ಟ್ ಅನುವಾದ ಪ್ರವಾಹ ಇವುಗಳು:

1. CLI_arguments ಅಥವಾ API ಪೆರಾಮೀಟರ್ಗಳನ್ನು ಪರ್ಸ್ ಮಾಡಿ.
2. `LLMConfig` ಸಹಾಯದಿಂದ LLM ಸಂರಚನೆಯನ್ನು ಮಾನ್ಯಗೊಳಿಸಿ.
3. ಚಿತ್ರ ಅನುವಾದ ಆಯ್ಕೆಮಾಡಿದಾಗ Azure AI Vision ಅನ್ನು ಮಾನ್ಯಗೊಳಿಸಿ.
4. ಭಾಷಾ ಕೋಡ್‌ಗಳನ್ನು ನಿಯಮೀಕರಿಸಿ.
5. ಪರಂಪರೆಯ ಭಾಷಾ ಫೋಲ್ಡರ್ ಉಪನಾಮಗಳನ್ನು ಸনಿಖ್ಯಿಸಿ.
6. ಅನುವಾದ ಪ್ರಮಾಣವನ್ನು ಅಂದಾಜಿಸಿ.
7. ಅನ್ವಯವಾಗುವಾಗ README ಭಾಷೆ/ಕೋರ್ಸ್ ವಿಭಾಗಗಳನ್ನು ನವೀಕರಿಸಿ.
8. ಪ್ರಾಜೆಕ್ಟ್ ಅನುವಾದವನ್ನು `ProjectTranslator` ಗೆ ನಿಯೋಜಿಸಿ.
9. `ProjectTranslator` ಫೈಲ್ ಪ್ರಕ್ರಿಯೆಯನ್ನು `TranslationManager`ವರಿಗೆ ನಿಯೋಜಿಸುತ್ತದೆ.

`TranslationManager` ಗಮನಕೇಂದ್ರಿತ ಫೈಲ್-ಟೈಪ್ ಮಿಕ್ಸಿನ್‌ಗಳಿಂದ ರಚಿಸಲಾಗಿದೆ:

- `ProjectMarkdownTranslationMixin` Markdown ಫೈಲ್ ಓದು, ವಿಷಯ ಅನುವಾದ, ಪಾಥ್ ಪುನರ್ರಚನೆ, ಮೆಟಾಡೇಟಾ, ಡಿಸ್ಕ್ಲೇಮರ್, ಮತ್ತು ಬರವಣಿಗೆಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ.
- `ProjectNotebookTranslationMixin` ನೋಟ್‌ಬುಕ್ ಫೈಲ್ ಓದು, Markdown-ಸೆಲ್‌ಗಳ ಅನುವಾದ, ಪಾಥ್ ಪುನರ್ರಚನೆ, ಮೆಟಾಡೇಟಾ, ಡಿಸ್ಕ್ಲೇಮರ್, ಮತ್ತು ಬರವಣಿಗೆಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ.
- `ProjectImageTranslationMixin` ಚಿತ್ರ ಕಂಡುಹಿಡಿಯುವಿಕೆ, ಪಠ್ಯ ನಿರ್ಗಮನ/ಅನುવાદ, ರೆಂಡರ್ ಮಾಡಿದ ಚಿತ್ರಗಳ ಬರವಣಿಗೆ, ಮತ್ತು ಮೆಟಾಡೇಟಾ ನಿರ್ವಹಿಸುತ್ತದೆ.

ಕೆಳ ಮಟ್ಟದ ವಿಷಯ APIಗಳು ಪ್ರಾಜೆಕ್ಟ್ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಆಗಲಾಗಿದೆ:

1. `translate_markdown_content` ಮತ್ತು `translate_notebook_content` ಕೇವಲ ಮೆಮೊರಿಯಲ್ಲಿ ಇರುವ ವಿಷಯವನ್ನು ಅನುವಾದಿಸುತ್ತವೆ.
2. `translate_image_content` ಒಂದೇ ಚಿತ್ರದಲ್ಲಿ ಪಠ್ಯವನ್ನು ಅನುವಾದಿಸಿ ರೆಂಡರ್ ಮಾಡಿದ ಚಿತ್ರ αντικೋಬ್ಜೆಕ್ಟ್ ಅನ್ನು ರಿಟರ್ನ್ ಮಾಡುತ್ತದೆ.
3. `rewrite_markdown_paths` ಮತ್ತು `rewrite_notebook_paths` ಸ್ಪಷ್ಟವಾದ ನಂತರ-ಪ್ರಕ್ರಿಯೆ ಸಹಾಯಕಗಳು. ಅವು ಯಾವುದೇ ಅನುವಾದವನ್ನು ಮಾಡುತ್ತವೆ ಅಥವಾ ಯಾವುದೇ ಪ್ರಾಜೆಕ್ಟ್ ಬರವಣಿಗೆಗಳನ್ನು ಮಾಡುತ್ತವೆ.

## ವಿಮರ್ಶೆ ಪ್ರಕ್ರಿಯೆ

ನಿರ್ಧಾರಾತ್ಮಕ ವಿಮರ್ಶೆ ಪ್ರಕ್ರಿಯೆ ಇವುಗಳು:

1. CLI_arguments ಅಥವಾ API ಪೆರಾಮೀಟರ್ಗಳನ್ನು ಪರ್ಸ್ ಮಾಡಿ.
2. ವಿನಂತಿಸಿದ ಭಾಷಾ ಕೋಡ್‌ಗಳನ್ನು ನಿಯಮೀಕರಿಸಿ.
3. `root_dir`, `root_dirs`, ಅಥವಾ `groups` ರಿಂದ ಒಂದು ಅಥವಾ ಹೆಚ್ಚಿನ ವಿಮರ್ಶಾ ಗುರಿಗಳನ್ನು ನಿರ್ಮಿಸಿ.
4. ಐಚ್ಛಿಕವಾಗಿ स्रोत ファイルಗಳನ್ನು `--changed-from` ಮೂಲಕ ಮಿತಿ ಮಾಡಬಹುದು.
5. ರಚನೆ, ಅನುವಾದ تازಾಗಿರಿಕೆ, Markdown ಅಖಂಡತೆ, ಮತ್ತು ಸ್ಥಳೀಯ ಲಿಂಕ್/ಚಿತ್ರ ಪಾತ್‌ಗಳಿಗಾಗಿ ನಿರ್ಧಾರಾತ್ಮಕ ತಪಾಸಣೆಗಳನ್ನು ನಡೆಸಿ.
6. ಪಠ್ಯ ಔಟ್ಪುಟ್ ಅಥವಾ GitHub-ಶೈಲಿಯ Markdown ಪ್ರಿಂಟ್ ಮಾಡಿ.
7. ವಿಮರ್ಶಾ ದೋಷಗಳು ಕಂಡುಬಂದಾಗ ವೈಫಲ್ಯದಿಂದ ನಿರ್ಗಮಿಸಿ.

ವಿಮರ್ಶೆ ಪ್ರಕ್ರಿಯೆ API ಕೀಲಿಗಳನ್ನು ಅಗತ್ಯವಿಲ್ಲದೆ ಇರಬೇಕು ಮತ್ತು ಪುಲ್ ವಿನಂತಿ CI ಗಾಗಿ ಯೋಗ್ಯವಾಗಿರಬೇಕು. ಪುಲ್ ವಿನಂತಿ ವರ್ಕ್‌ಫ್ಲೋ ಪ್ರತಿ ಓಟದ ಮೇಲೆ ಒಂದು ಚೆಕ್ ಸಾರಾಂಶವನ್ನು ಬರೆಯುತ್ತದೆ ಮತ್ತು ಮಾತ್ರ `co-op-review` ವೈಫಲ್ಯ ಆಗುವಾಗ PR ಕಾಮೆಂಟ್ ಅನ್ನು ಪೋಸ್ಟ್ ಮಾಡುತ್ತದೆ.

## ದಸ್ತಾವೇಜು ತಾಣ

ದಸ್ತಾವೇಜು ತಾಣವನ್ನು ಈ ಮೂಲಕ ಸಂರಚಿಸಲಾಗಿದೆ:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` ಡೈರೆಕ್ಟರಿ ಕ್ಯಾನೊನಿಕಲ್ ದಸ್ತಾವೇಜು ಮೂಲವಾಗಿದೆ. ಪ್ರಾಜೆಕ್ಟ್ ಉದ್ದೇಶಪೂರ್ವಕವಾಗಿ ಮತ್ತೊಂದು ಪ್ರಕಟಿತ ದಾಖಲೆ ಸತಹವನ್ನು ಪರಿಚಯಿಸದಿದ್ದರೆ ಈ ಡೈರೆಕ್ಟರಿಗಿಂತ ಹೊರಗೆ ಹೊಸ ಅಂತಿಮ-ಬಳಕೆದಾರ ಮಾರ್ಗದರ್ಶಿಗಳನ್ನು ಸೇರಿಸಬೇಡಿ.

ಸ್ಥಾನೀಯವಾಗಿ ಬಿಲ್ಡ್ ಮಾಡಿ:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

ಸ್ಥಾನೀಯವಾಗಿ ಪೂರ್ವದೃಶ್ಯ ಮಾಡಿ:

```bash
python -m mkdocs serve
```

ರಚಿತ ತಾಣ `site/` ಗೆ ಬರೆಯಲ್ಪಡುತ್ತದೆ, ಅದು git ಮೂಲಕ ನಿರ್ಲಕ್ಷ್ಯಗೊಳಿಸಲಾಗುತ್ತದೆ.

## GitHub Pages ಕಾರ್ಯಪ್ರವಾಹ

`.github/workflows/docs.yml` ಪುಲ್ ರಿಕ್ವೆಸ್ಟ್‌ಗಳ ಮೇಲೆ ತಾಣವನ್ನು ಬಿಲ್ಡ್ ಮಾಡುತ್ತದೆ ಮತ್ತು `main` ಗೆ ಪುಶ್ ಆದಾಗ ಅದನ್ನು ಡಿಪ್ಲಾಯ್ ಮಾಡುತ್ತದೆ.

ವರ್ಕ್‌ಫ್ಲೋ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡುತ್ತದೆ:

```bash
pip install -r requirements-docs.txt
```

ದಾಖಲೆಗಳ ವರ್ಕ್‌ಫ್ಲೋ ಕೇವಲ ದಸ್ತಾವೇಜು ಟೂಲ್‌ಚೈನ್ ಅನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡುತ್ತದೆ. `mkdocs.yml` `mkdocstrings` ಅನ್ನು `src/` ಕಡೆ ಸೂಚಿಸುತ್ತದೆ ಆದಕಾರಣ ಸಾರ್ವಜನಿಕ API ಪುಟಗಳನ್ನು ಸಂಪೂರ್ಣ ರನ್‌ಟೈಮ್ ನಿರ್ಭರತೆಗಳನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡದೆ ಮೂಲ ತುಂಡುಗಳಿಂದ ರೆಂಡರ್ ಮಾಡಬಹುದು. ಭವಿಷ್ಯದಲ್ಲಿನ API ದಸ್ತಾವೇಜುಗಳು ಬಿಲ್ಡ್ ಸಮಯದಲ್ಲಿ ಐಚ್ಛಿಕ ರನ್‌ಟೈಮ್ ಪ್ರೊವೈಡರ್‌ಗಳನ್ನು ಐಂಪೋರ್ಟ್ ಮಾಡಬೇಕಾಗಿದ್ದರೆ `.github/workflows/docs.yml` ಮತ್ತು ಈ ಮಾರ್ಗದರ್ಶಿಯನ್ನು ಎರಡನ್ನೂ ನವೀಕರಿಸಿ.

## ದಸ್ತಾವೇಜುಗಳ ಗುಣಮಟ್ಟದ ಮಾನದಂಡ

ದಸ್ತಾವೇಜು ಬದಲಾವಣೆಗಳನ್ನು ಮರ್ಜ್ ಮಾಡುವ ಮೊದಲು, ಈನ್ನು ಓಡಿಸಿ:

```bash
python -m mkdocs build --strict
git diff --check
```

 brوSTRICT ಬಿಲ್ಡ್‌ಗಳನ್ನು ಬಳಸಿ যাতে ಮುರಿದ ಲಿಂಕ್‌ಗಳು, ಅಮಾನ್ಯ ನ್ಯಾವಿಗೇಶನ್ ಎಂಟ್ರಿಗಳು, ಮತ್ತು API ರೆಂಡರಿಂಗ್ ಸಮಸ್ಯೆಗಳು ಮೊದಲೇ ತಪ್ಪಾಗಿ ಪತ್ತೆಯಾಗುವ<void>.</void>