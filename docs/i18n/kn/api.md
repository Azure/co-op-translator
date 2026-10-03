# ಪೈಥಾನ್ API

ಸ್ಥಿರ ಸಾರ್ವಜನಿಕ ಪೈಥಾನ್ API ಅನ್ನು `co_op_translator.api` ನಿಂದ ರಫ್ತು ಮಾಡಲಾಗಿದೆ. ಹೆಚ್ಚಿನ ಇಂಟಿಗ್ರೇಷನ್‌ಗಳು ಈ ಕಾರ್ಯಪ್ರವಾಹಗಳಲ್ಲಿ ಒಂದನ್ನು ಬಳಸುತ್ತವೆ:

| ಸನ್ನಿವೇಶ | ಯಾವಾಗ ಇದನ್ನು ಬಳಸಿರಿ | ಮುಖ್ಯ APIಗಳು |
| --- | --- | --- |
| ವೈಯಕ್ತಿಕ ಫೈಲ್‌ಗಳು ಅಥವಾ ದಾಖಲೆಗಳನ್ನು ಅನುವಾದಿಸಿ | ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ಮೂಲ ವಿಷಯವನ್ನು ಓದುತ್ತದೆ, ಅನುವಾದಕ್ಕಾಗಿ Co-op Translator ಅನ್ನು ಕರೆದು ಫಲಿತಾಂಶವನ್ನು ಎಲ್ಲಿ ಉಳಿಸಬೇಕು ಎಂದು ನಿರ್ಧರಿಸುತ್ತದೆ. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| ಹೋಸ್ಟ್-ಏಜೆಂಟ್ ಅನುವಾದಕ್ಕಾಗಿ ವಿಷಯವನ್ನು ತಯಾರಿಸಿ | ನಿಮ್ಮ MCP ಹೋಸ್ಟ್ ಅಥವಾ ಅಪ್ಲಿಕೇಶನ್ ಮಾದರಿ ತುಂಡುಗಳನ್ನು ಅನುವಾದಿಸುತ್ತದೆ, Co-op Translator ತುಂಡುವಿಭಾಗ ಮತ್ತು ಪುನರ್‌ರಚನೆಯನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| ಒಂದು ಸಂಪೂರ್ಣ ರೆಪೊಸಿಟೋರಿಯನ್ನು ಅನುವಾದಿಸಿ | ನೀವು ಪೈಥಾನ್ API ಅನ್ನು CLI ಮಾದರಿಯಂತೆ ವರ್ತಿಸುವಂತೆ ಮಾಡಿ, ಕಂಡುಹಿಡಿತ, ಔಟ್‌ಪುಟ್ ಮಾರ್ಗಗಳು, ಮೆಟಾಡೇಟಾ, ಕ್ಲೀನ್‌ಅಪ್ ಮತ್ತು ಬರವಣಿಗೆಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಬಯಸುವಿರಿ. | `run_translation` |

ಈ API ಎಂಟ್ರಿ ಪಾಯಿಂಟ್‌ಗಳು ಬಳಸುವ ಬಹುತೇಕ ತಳಮಟ್ಟದ ಮಡ್ಯುಲ್‌ಗಳು `core`, `config`, `review`, ಮತ್ತು `utils` ಅಡಿಯಲ್ಲಿ ಅನುಷ್ಠಾನ ವಿವರಗಳಾಗಿವೆ.

MCP ಕ್ಲೈಂಟ್‌ಗಳು [MCP ಸರ್ವರ್](mcp.md) ಮುಖಾಂತರ ಅದೇ ಸಾರ್ವಜನಿಕ API ಅನ್ನು ಬಳಸುತ್ತವೆ. Python ಅನ್ನು ನೇರವಾಗಿ ಕರೆಸುವಾಗ ಈ ಪುಟವನ್ನು ಬಳಸಿ, ಮತ್ತು Co-op Translator ಅನ್ನು ಏಜೆಂಟ್ ಅಥವಾ ಸಂಪಾದಕಕ್ಕೆ ಬಹಿರ್ಗೊಳಿಸುವಾಗ MCP ಮಾರ್ಗದರ್ಶಿಯನ್ನು ಬಳಸಿ. ನೀವು CLI, Python API ಮತ್ತು MCP ನಡುವಿನ ಆಯ್ಕೆ ಮಾಡುತ್ತಿರುವರೆ, [ನಿಮ್ಮ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಆಯ್ಕೆಮಾಡಿ](workflows.md) ಮೂಲಕ ಪ್ರಾರಂಭಿಸಿ.

## ಮೊದಲ ಬಾರಿಗೆ API ಫ್ಲೋ

Python ಕೋಡ್‌ನಿಂದ Co-op Translator ಅನ್ನು ಕರೆಸುತ್ತಿರುವರೆ ಇಲ್ಲಿ ಪ್ರಾರಂಭಿಸಿ:

1. ನೀವು ಕೇವಲ Markdown ಅಥವಾ ನೋಟ್ಬುಕ್ ತುಂಡುಗಳನ್ನು ಹೋಸ್ಟ್-ಏಜೆಂಟ್‌ಗೆ ತಯಾರಿಸುತ್ತಿಲ್ಲದಿದ್ದರೆ, [ಸಂರಚನೆ](configuration.md) ನಲ್ಲಿ ವಿವರವಾಗಿ ನೀಡಿರುವಂತೆ LLM ಪ್ರೊವೈಡರ್ ಅನ್ನು ಸಂರಚಿಸಿ.
2. ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ಫೈಲ್ I/O ಅನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆಯೇ ಎಂದು ನಿರ್ಧರಿಸಿ.
3. ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ವೈಯಕ್ತಿಕ ಫೈಲ್‌ಗಳನ್ನು ಓದುತ್ತಾ ಬರೆಯುತ್ತಾ ಇದ್ದರೆ ವಿಷಯ API ಗಳನ್ನು ಬಳಸಿ.
4. Co-op Translator ಅನ್ನು CLI ನಂತೆ ರೆಪೊಸಿಟರಿ ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಬೇಕಾದಾಗ `run_translation` ಅನ್ನು ಬಳಸಿ.
5. ಸ್ವಯಂಚಾಲಿತ ಕೆಲಸಗಳಲ್ಲಿ ನಿರ್ಧಾರಕಾರಿ ಪರೀಕ್ಷೆಗಳು ಬೇಕಾದರೆ ಅನುವಾದದ ನಂತರ `run_review` ಅನ್ನು ಬಳಸಿ.

| ಗುರಿ | ಪ್ರಾರಂಭಿಸಲು API |
| --- | --- |
| ಒಂದು Markdown ಸ್ಟ್ರಿಂಗ್ ಅಥವಾ ಫೈಲ್ ಅನ್ನು ಅನುವಾದಿಸಿ | `translate_markdown_content` |
| ಒಂದು ನೋಟ್ಬುಕ್ ಪೇಲೋಡ್ ಅನ್ನು ಅನುವಾದಿಸಿ | `translate_notebook_content` |
| ಒಂದು ಚಿತ್ರವನ್ನು ಅನುವಾದಿಸಿ | `translate_image_content` |
| ಹೋಸ್ಟ್ ಏಜೆಂಟ್‌ಗೆ Markdown ಅಥವಾ ನೋಟ್ಬುಕ್ ತುಂಡುಗಳನ್ನು ಅನುವಾದಿಸಲು ಅವಕಾಶ ನೀಡಿ | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| ಔಟ್‌ಪುಟ್ ಮಾರ್ಗ ಆಯ್ಕೆ ಮಾಡಿದ ನಂತರ ಅನುವಾದಿತ ಲಿಂಕ್‌ಗಳನ್ನು ಮರುಬರೆಸಿ | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| ಒಂದು ಪೂರ್ಣ ರೆಪೊಸಿಟೋರಿಯನ್ನು ಅನುವಾದಿಸಿ | `run_translation` |
| ಅನುವಾದಿತ ಔಟ್‌ಪುಟ್ ಅನ್ನು ಪರಿಶೀಲಿಸಿ | `run_review` |

## ಸನ್ನಿವೇಶ 1: ವೈಯಕ್ತಿಕ ಫೈಲ್‌ಗಳು ಅಥವಾ ದಾಖಲೆಗಳನ್ನು ಅನುವಾದಿಸಿ

ನೀವು ಮುಂದೆ ಫೈಲ್, ಸಂಪಾದಕ ಬಫರ್, ನೋಟ್ಬುಕ್ ಪೇಲೋಡ್, MCP ವಿನಂತಿ, ಅಥವಾ ಕಸ್ಟಮ್ ಪೈಪ್‌ಲೈನ್ ಇನ್ಪುಟ್ ಇದ್ದಾಗ ಈ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಬಳಸಿ. ನಿಮ್ಮ ಕೋಡ್ ಫೈಲ್ I/O ಅನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ:

1. ಮೂಲ ವಿಷಯವನ್ನು ಓದಿ.
2. ವಿಷಯ ಅನುವಾದ API ಅನ್ನು ಕರೆಸಿ.
3. ಅನುವಾದಿತ ವಿಷಯವನ್ನು ಪ್ರಾಜೆಕ್ಟ್ ಅನುವಾದ ಫೋಲ್ಡರ್‌ನಲ್ಲಿ ಬರೆಯಬೇಕಾದರೆ ಐಚ್ಛಿಕವಾಗಿ ಮಾರ್ಗ ಮರುಬರೆಯುವ API ಅನ್ನು ಕರೆಸಿ.
4. ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್‌ನಿಂದ ಫಲಿತಾಂಶವನ್ನು ಉಳಿಸಿ ಅಥವಾ ಹಿಂತಿರುಗಿಸಿ.

ವಿಷಯ ಅನುವಾದ API ಗಳು ಪ್ರಾಜೆಕ್ಟ್ ಕಂಡುಹಿಡಿಯುವಿಕೆ ನಡೆಸುದಿಲ್ಲ, ಮೆಟಾಡೇಟಾವನ್ನು ಬರೆಯುವುದಿಲ್ಲ, ಖಂಡನೆಗಳನ್ನು ಸೇರಿಸುವುದಿಲ್ಲ ಮತ್ತು ಲಿಂಕ್‌ಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಮರುಬರೆಯುವುದಿಲ್ಲ.

### Markdown ಫೈಲ್

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

ಅನುವಾದಿತ Markdown Co-op Translator ಪ್ರಾಜೆಕ್ಟ್ ವಿನ್ಯಾಸದಲ್ಲಿ ಇರದಿದ್ದಲ್ಲಿ, `rewrite_markdown_paths` ಅನ್ನು ಬಿಟ್ಟುಬಿಡಿ ಮತ್ತು ಅನುವಾದಿತ ಸ್ಟ್ರಿಂಗ್ ಅನ್ನು ನೇರವಾಗಿ ಉಳಿಸಿ.

### ನೋಟ್ಬುಕ್ ಫೈಲ್

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

`translate_notebook_content` Markdown ಸೆಲ್‌ಗಳನ್ನು ಅನುವಾದಿಸುತ್ತದೆ ಮತ್ತು non-Markdown ಸೆಲ್‌ಗಳನ್ನು ಉಳಿಸುತ್ತದೆ. ಮಾರ್ಗ ಮರುಬರೆಯುವಿಕೆಯು ಕೇವಲ Markdown ಸೆಲ್‌ಗಳಿಗೆ ಅನ್ವಯಿಸುತ್ತದೆ.

### ಚಿತ್ರ ಫೈಲ್

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

`translate_image_content` ಮೂಲ ಚಿತ್ರವನ್ನು ಓದುತ್ತದೆ ಮತ್ತು ರೆಂಡರ್ ಮಾಡಿದ `PIL.Image.Image` ಅನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ. ಇದು ಅನುವಾದಿತ ಚಿತ್ರ ಮೆಟಾಡೇಟಾ ಅನ್ನು ಬರೆಯುವುದಿಲ್ಲ.

## ಸನ್ನಿವೇಶ 2: ಸಂಪೂರ್ಣ ರೆಪೊಸಿಟೋರಿಯನ್ನು ಅನುವಾದಿಸಿ

Python API ಅನ್ನು `translate` CLI ಯಂತೆ ವರ್ತಿಸುವಂತೆ ಮಾಡಬೇಕಾದರೆ ಈ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಬಳಸಿರಿ. `run_translation` ಬೆಂಬಲಿಸಲ್ಪಟ್ಟ ಫೈಲ್‌ಗಳನ್ನು ಕಂಡುಹಿಡಿಯುತ್ತದೆ, ಆಯ್ಕೆಯಾದ ವಿಷಯ ಬಗೆಯನ್ನು ಅನುವಾದಿಸುತ್ತದೆ, ಮಾರ್ಗಗಳನ್ನು ಮರುಬರೆಯುತ್ತದೆ, ಔಟ್‌ಪುಟ್ ಫೈಲ್‌ಗಳನ್ನು ಬರೆಯುತ್ತದೆ, ಮೆಟಾಡೇಟಾವನ್ನು ನವೀಕರಿಸುತ್ತದೆ, ಮತ್ತು ಕ್ಲೀನ್‌ಅಪ್ ಮುಂತಾದ ಅನುವಾದ ನಿರ್ವಹಣೆ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ.

`run_translation` ಅನ್ನು ಪ್ರಾಜೆಕ್ಟ್ ಸಮನ್ವಯದ ಪ್ರಾಥಮಿಕ ಎಂಟ್ರಿಪಾಯಿಂಟ್‌ಂತೆ ಪರಿಗಣಿಸಲಾಗುತ್ತದೆ. `translate_project` ಅನ್ನು ಅದೇ ವರ್ತನೆಯೊಂದಿಗೆ ಹೊಂದಾಣಿಕೆಯ ಅಲಿಯಾಸ್ ಆಗಿ ರಫ್ತು ಮಾಡಲಾಗಿದೆ.

ಪ್ರಸ್ತುತ ರೆಪೊಸಿಟೋರಿಯ Markdown ಫೈಲ್‌ಗಳನ್ನು ಕೊರಿಯನ್ ಮತ್ತು ಜಪಾನೀಸ್ ಭಾಷೆಗಳಿಗೆ ಅನುವಾದಿಸಿ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

ನಿರ್ದಿಷ್ಟ ಪ್ರಾಜೆಕ್ಟ್ ರೂಟ್‌ನಿಂದ ಮಾತ್ರ ನೋಟ್ಬುಕ್‌ಗಳನ್ನು ಅನುವಾದ ಮಾಡಿ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

ಫೈಲ್‌ಗಳನ್ನು ಬರೆಯದೆ ಅನುವಾದ ಪ್ರಮಾಣವನ್ನು ಪೂರ್ವದೃಶ್ಯಗೊಳಿಸಿ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

ಒಂದು ಇಂಟಗ್ರೇಷನ್‌ಗಾಗಿ ರಚನಾತ್ಮಕ ಪ್ರಗತಿ ಘಟನೆಗಳನ್ನು ದಾಖಲೆ ಮಾಡಿ:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # ನಿಮ್ಮ job-event ಟೇಬಲ್‌ನಲ್ಲಿ ಪೇಲೋಡ್ ಅನ್ನು ಸಂಗ್ರಹಿಸಿ ಅಥವಾ ಅದನ್ನು ನಿಮ್ಮ UI ಗೆ ಸ್ಟ್ರೀಮ್ ಮಾಡಿ


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

ಈವೆಂಟ್‌ಗಳು ಆವೃತ್ತಿ ಹೊಂದಿದ schema `co-op.translation.event.v1` ಅನ್ನು ಬಳಸುತ್ತವೆ. ಇಂಟಿಗ್ರೇಷನ್‌ಗಳು
ಸ್ಥಿರ ಕ್ಷೇತ್ರಗಳಾದ `type` ಮತ್ತು `stage_key` ಇತ್ಯಾದಿಗಳ ಮೇಲೆ ಅವಲಂಬಿಸಬೇಕು, ಮಾನವ-ಮುಖೀ
ಕನಸೋಲ್ ಪಠ್ಯ ಅಥವಾ `stage_label` ಮೇಲೆ ಅಲ್ಲ.

ಒಂದು ಕರೆನಲ್ಲೇ ಬಹು ವಿಷಯ ರೂಟ್‌ಗಳನ್ನು ಅನುವಾದಿಸಿ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

ಅನುವಾದಗಳನ್ನು ಸ್ಪಷ್ಟ ಔಟ್‌ಪುಟ್ ಗುಂಪುಗಳಲ್ಲಿಗೆ ಬರೆಯಿರಿ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

ಪ್ರತಿ ಭಾಷೆಗೆ ಒಳಹೊರಗಿನ ಉಪ-ಡೈರೆಕ್ಟರಿಯನ್ನು ಹೊಂದಬೇಕಾದರೆ ಪ್ರತಿ-ಭಾಷಾ ಪ್ಲೇಸ್‌ಹೋಲ್ಡರ್ ಅನ್ನು ಬಳಸಿ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

`markdown`, `notebook`, ಅಥವಾ `images` ಯಾವುದೂ ಸೆಟ್ ಆಗದಿದ್ದರೆ, API ಎಲ್ಲ ಬೆಂಬಲಿಸಲ್ಪಟ್ಟ ವಿಧಗಳನ್ನೂ ಅನುವಾದಿಸುತ್ತದೆ: Markdown, notebook ಗಳು, ಮತ್ತು ಚಿತ್ರಗಳು.

### ಅನುವಾದ ಸ್ಥಿತಿ ಪ್ರೊವೈಡರ್ ಮೂಲಕ ಸ್ವೀಕರಿಸಲಾದ ಮಾನವ ಸಂಪಾದನೆಗಳನ್ನು ಉಳಿಸಿ

ಡೀಫಾಲ್ಟ್ ಆಗಿ, Co-op Translator ತನ್ನ ಇಂದಿನ ಫೈಲ್-ಮಟ್ಟದ ವರ್ತನೆಯನ್ನು ಕಾಯ್ದುಕೊಳ್ಳುತ್ತದೆ:
Markdown ಮೂಲ ಹಳೆಯದಾಗಿದ್ದರೆ, ಸಂಪೂರ್ಣ ಅನುವಾದಿತ ಫೈಲ್ ಮರುರಚಿಸಲಾಗುತ್ತದೆ. ಹೋಸ್ಟ್
ಇಂಟಿಗ್ರೇಷನ್‌ಗಳು ಐಚ್ಛಿಕವಾಗಿ `TranslationStateProvider` ಅನ್ನು ಪಾಸ್ ಮಾಡಬಹುದು
ಬದಲಾಗದ ಮೂಲ ಬ್ಲಾಕ್‌ಗಳಲ್ಲಿ ಮಾಡಿದ ಮಾನವ ಸಂಪಾದನೆಗಳನ್ನು ಉಳಿಸಲು.

ಪ್ರೊವೈಡರ್ ಕೊನೆಗೆ ಸ್ವೀಕರಿಸಿದ ಮೂಲ/ಲಕ್ಷ್ಯ ಜೋಡಿಯನ್ನು ಒದಗಿಸುತ್ತದೆ ಮತ್ತು ಪ್ರತಿ ಹೊಸ
ಅಭ್ಯರ್ಥಿಯನ್ನು ದಾಖಲಿಸುತ್ತದೆ. ಸ್ವೀಕರಿಸುವಿಕೆ ಇಂಟಿಗ್ರೇಷನ್‌ನ ಜವಾಬ್ದಾರಿಯೇ ಆಗಿರುತ್ತದೆ—for example,
ಅನುವಾದ ಪುಲ್ ವಿನಂತಿ ಒಂದು ಮರ್ಜ್ ಆಗಿದ ನಂತರ:

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

ಮಾನ್ಯವಾಗಿ ಸ್ವೀಕರಿಸಿದ ಬೇಸ್‌ಲೈನ್ ಇರುವ Markdown ಫೈಲ್‌ಗಳಿಗಾಗಿ, Co-op Translator ಹೊಂದಿಕೆಯಾಗುತ್ತದೆ
ಟಾಪ್-ಲೆವೆಲ್ Markdown ಬ್ಲಾಕ್‌ಗಳನ್ನು. ಬದಲಾಗದ ಮೂಲ ಬ್ಲಾಕ್‌ಗಳು ಪ್ರಸ್ತುತ ಅನುವಾದಿತ
ಬ್ಲಾಕ್‌ಗಳನ್ನು ಪುನಃ ಬಳಸಿಕೊಂಡು, ಮಾನವರಿಂದ ಮಾಡಿದ ಸಂಪಾದನೆಗಳನ್ನು ಸಹ ಒಳಗೊಂಡಂತೆ; ಬದಲಾಗಿದ ಅಥವಾ ಸೇರ್ಪಡೆ ಮಾಡಿದ ಮೂಲ ಬ್ಲಾಕ್‌ಗಳು ಅನುವಾದಕ್ಕೆ ಕಳುಹಿಸಲಾಗುತ್ತವೆ
ಅನುವಾದಕ್ಕೆ; ಅಳಿಸಲಾದ ಮೂಲ ಬ್ಲಾಕ್‌ಗಳು ತೆಗೆದುಹಾಕಲಾಗುತ್ತವೆ. ಹೊಂದಾಣಿಕೆ ಅನಿಶ್ಚಿತವಾದರೆ,
ಗುರಿ ರಚನೆ ಬದಲಾಗಿದರೆ, ಒಂದು ಬ್ಲಾಕ್ ಅನುವಾದ ಅಮಾನ್ಯವಾಗಿದ್ದರೆ, ಅಥವಾ ಬೇಸ್‌ಲೈನ್
ಲಭ್ಯವಿಲ್ಲದಿದ್ದರೆ, Co-op Translator ಸುರಕ್ಷಿತವಾಗಿ ಇತ್ತೀಚಿನ ಸಂಪೂರ್ಣ-ಫೈಲ್
ಅನುವಾದ ಮಾರ್ಗಕ್ಕೆ ಹಿಂದಿರುಗುತ್ತದೆ.

ಈ API ಡಾಕ್ಯುಮೆಂಟ್ ಅನುವಾದ ಸ್ಥಿತಿಯನ್ನು ಸಂಗ್ರಹಿಸುತ್ತದೆ, ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳ ಮಧ್ಯೆ ಪದ ಅಥವಾ
ಸೆಗ್ಮೆಂಟ್ ಅನುವಾದ ಮೆಮೊರಿ ಅಲ್ಲ. ಇದು ಪ್ರಸ್ತುತ Markdown ಪ್ರಾಜೆಕ್ಟ್ ಅನುವಾದಕ್ಕೆ ಅನ್ವಯಿಸುತ್ತದೆ.
ನೋಟ್ಬುಕ್ ಮತ್ತು ಚಿತ್ರಗಳ ವರ್ತನೆ ಬದಲಾಯಿಲ್ಲ. `update=True` ಅನ್ನು ಪಾಸ್ಸ್ ಮಾಡಿದರೆ
ಇನ್ನೂ ಸಂಪೂರ್ಣ ಪುನರ್ಜನನೆಯನ್ನು ವಿನಂತಿಸುತ್ತದೆ.

ಒಂದು ಅಥವಾ ಹೆಚ್ಚು ಫೈಲ್‌ಗಳನ್ನು ಅನುವಾದಿಸಲಾಗದಿದ್ದರೆ, `run_translation` ಒಂದು
`RuntimeError` ಅನ್ನು ಪ್ರಾಜೆಕ್ಟ್ ಕಾರ್ಯಪ್ರವಾಹ ಮುಗಿಸಿದ ನಂತರ ಎಬ್ಬಿಸುತ್ತದೆ,
ಕಡಿತವಾದ ಔಟ್‌ಪುಟ್ ಜೊತೆಗೆ ಯಶಸ್ವಿ ಓಟವನ್ನು ವರದಿ ಮಾಡುವ ಬದಲಿಗೆ.
ಇಂಟಿಗ್ರೇಷನ್‌ಗಳು ಇದನ್ನು ವಿಫಲವಾದ

## ಅನುವಾದಿತ ಫಲಿತಾಂಶವನ್ನು ಪರಿಶೀಲಿಸಿ

`run_review` ನಿರ್ಧಾರಾತ್ಮಕ ಅನುವಾದ ಪರಿಶೀಲನೆಗಳನ್ನು LLM ಅಥವಾ Vision ಪ್ರಮಾಣಪತ್ರಗಳಿಲ್ಲದೆ ನಡೆಸುತ್ತದೆ.

!!! note "ಬೆಟಾ"
    `run_review` ಒಂದು ಬೆಟಾ ನಿಗದಿತ ವಿಮರ್ಶಾ API. ಇದು ಮಾದರಿ ಪೂರೈಕೆದಾರರನ್ನು ಕರೆ ಮಾಡುವುದಿಲ್ಲ ಅಥವಾ ಫೈಲ್‌ಗಳನ್ನು ಬರೆಯುವುದಿಲ್ಲ, ಆದರೆ ಪರಿಶೀಲನೆಗಳು ಮತ್ತು ಸಮಸ್ಯೆಗಳ ಸ್ಕೀಮಾಗಳು ಬದಲಾಗಬಹುದು.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

README-ಮಾತ್ರದ ಅನುವಾದದ ನಂತರ, ಪರಿಶೀಲನೆಗಾಗಿ ಅದೇ ವ್ಯಾಪ್ತಿಯನ್ನು ಬಳಸಿ:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` ಪ್ರತಿ ಸಂರಚಿತ ಮೂಲ ರೂಟ್‌ ಅಡಿಯಲ್ಲಿ ಮಾತ್ರ `README.md` ಅನ್ನು ಪರಿಶೀಲಿಸುತ್ತದೆ,
ಕಸ್ಟಮ್ `groups` ಮತ್ತು ಔಟ್‌ಪುಟ್ ಡೈರೆಕ್ಟರಿಗಳನ್ನು ಒಳಗೊಂಡಿದೆ. ಇತರ ದಾಖಲೆಗಳು ಮತ್ತು ಒಳಗಿನ
READMEಗಳು ಹೊರಗಿಡಲ್ಪಟ್ಟಿವೆ. ಕಾಣೆಯಾದ ಮೂಲ README `ValueError`; ವಿಫಲವಾದ
ಅನುವಾದ ತಪಾಸಣೆಗಳು `RuntimeError` ಅನ್ನು ಎತ್ತುತ್ತವೆ.

ಬೇಸ್ ರೆಫ್ ವಿರುದ್ದ ಬದಲಾಗಿದ್ದ ಫೈಲ್‌ಗಳನ್ನು ಮಾತ್ರ ಪರಿಶೀಲಿಸಿ ಮತ್ತು GitHub-ಶೈಲಿಯ ಔಟ್‌ಪುಟ್ ಮುದ್ರಿಸಿ:

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## ಕಾಪಿ-ಪೇಸ್ಟ್ API ಉದಾಹರಣೆಗಳು

ಫೈಲ್ ಬರವಣಿಕೆಗಳನ್ನು ನಡೆಸದೆ Markdown ವಿಷಯವನ್ನು ಅನುವಾದಿಸಿ:

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

Markdown ಲಿಂಕ್‌ಗಳನ್ನು ಅನುವಾದಿಸಿ ಮತ್ತು ಮರುರಚಿಸಿ:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

Python ನಿಂದ ರಿಪೊಸಿಟರಿಯನ್ನು ಅನುವಾದಿಸಿ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

ಬಹು ಮೂಲಗಳನ್ನು ಅನುವಾದಿಸಿ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

ಗ್ಲಾಸರಿ ಪದಗಳನ್ನು ಉಳಿಸಿ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## ಸಾರ್ವಜನಿಕ ಪ್ರವೇಶ ಬಿಂದುಗಳು

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## ವಿಷಯ ಅನುವಾದ API ಗಳು

Content translation APIs ಎಂಬವುಗಳು ಮೆಮೊರಿಯಲ್ಲಿ ಈಗಾಗಲೇ ವಿಷಯವಿರುವ ಇಂಟಿಗ್ರೇಶನ್‌ಗಳಿಗೆ ಉದ್ದೇಶಿಸಲಾಗಿದೆ, ಉದಾಹರಣೆಗೆ ಸಂಪಾದಕ ವಿಸ್ತರಣೆ, MCP tool, ನೋಟ್ಬುಕ್ ಪ್ರೊಸೆಸರ್ ಅಥವಾ ಕಸ್ಟಮ್ ಪೈಪ್‌ಲೈನ್.

| ಕಾರ್ಯ | ಇನ್ಪುಟ್ | ಔಟ್‌ಪುಟ್ | ಫೈಲ್ I/O | ಟಿಪ್ಪಣಿಗಳು |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | ಇಲ್ಲ | ಅಸಿಂಕ್ರೋನಸ್. Markdown ವಿಷಯವನ್ನು ಮಾತ್ರ ಅನುವಾದಿಸುತ್ತದೆ. ಇದು ಲಿಙ্ক್‌ಗಳನ್ನು ಮರುಬರೆಯುವುದಿಲ್ಲ, ಮೆಟಾಡೇಟಾವನ್ನು ಬರೆಯುವುದಿಲ್ಲ, ಅಥವಾ ಡಿಸ್ಕ್ಲೈಮರ್‌ಗಳನ್ನು ಸೇರಿಸುವುದಿಲ್ಲ. |
| `translate_notebook_content` | Notebook JSON `str` ಅಥವಾ `dict` | Notebook JSON `str` | ಇಲ್ಲ | ಅಸಿಂಕ್ರೋನಸ್. Markdown ಸೆಲ್‌ಗಳನ್ನು ಅನುವಾದಿಸುತ್ತದೆ ಮತ್ತು ಮಾರ್ಕ್ಡೌನ್ ಅಲ್ಲದ ಸೆಲ್‌ಗಳನ್ನು ಉಳಿಸುತ್ತದೆ. ಇದು ಲಿಂಕ್‌ಗಳನ್ನು ಮರುಬರೆಯುವುದಿಲ್ಲ, ಮೆಟಾಡೇಟಾವನ್ನು ಬರೆಯುವುದಿಲ್ಲ, ಅಥವಾ ಡಿಸ್ಕ್ಲೈಮರ್‌ಗಳನ್ನು ಸೇರಿಸುವುದಿಲ್ಲ. |
| `translate_image_content` | ಚಿತ್ರದ ಪಥ | `PIL.Image.Image` | ಮೂಲ ಚಿತ್ರವನ್ನು ಮಾತ್ರ ಓದುತ್ತದೆ | ಸಿಂಕ್ರೋನಸ್. ಚಿತ್ರದ ಪಠ್ಯವನ್ನು ಹೊರತೆಗೆದು ಅನುವಾದಿಸಿ, ನಂತರ ರೆಂಡರ್ ಮಾಡಿದ ಚಿತ್ರವನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ. ಇದು ಅನುವಾದಿತ ಚಿತ್ರ ಮೆಟಾಡೇಟಾವನ್ನು ಉಳಿಸುವುದಿಲ್ಲ. |

`translate_markdown_content` ಮತ್ತು `translate_notebook_content` ಅವರ ಆಯ್ಕೆಗಳ ಮೂಲಕ ಐಚ್ಛಿಕ `source_path` ಅನ್ನು ಸ್ವೀಕರಿಸುತ್ತವೆ. ಮಾರ್ಗವನ್ನು ಅನುವಾದಕರಿಗೆ ಸಂದರ್ಭವಾಗಿ ಒದಗಿಸಲಾಗುತ್ತದೆ; ಕರೆಮಾಡುವವರು ಅನುವಾದದ ನಂತರ ಯಾವುದೇ ಯೋಜನೆ-ನಿರ್ದಿಷ್ಟ ಮಾರ್ಗದ ಪುನರ್‌ರಚನೆಗೆ ಜವಾಬ್ದಾರಿಯಾಗಿರುತ್ತಾರೆ.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

ಅದೇ ಆಯ್ಕೆಗಳನ್ನು ಡಿಕ್ಷನರಿಗಳಾಗಿ ನೀಡಬಹುದು:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## ಏಜೆಂಟ್-ಸಹಾಯಿತ ಅನುವಾದ APIಗಳು

ಏಜೆಂಟ್-ಸಹಾಯಕಿತ APIs ಗಳು Co-op Translator ನಿಂದ ಸಂರಚಿಸಲಾದ LLM ಪೂರೈಕೆದಾರರನ್ನು ಕರೆ ಮಾಡುವುದಿಲ್ಲ. ಅವುಗಳು ಹೋಸ್ಟ್ ಏಜೆಂಟ್‌ಗೆ ಅನುವಾದಿಸಲು Markdown ಅಥವಾ notebook ತುಂಡುಗಳನ್ನು ಸಿದ್ಧಪಡಿಸುತ್ತವೆ, ನಂತರ ಅನುವಾದಿಸಿದ ತುಂಡುಗಳಿಂದ ಅಂತಿಮ ವಿಷಯವನ್ನು ಪುನರ್‌ರಚಿಸುತ್ತವೆ.

| ಕಾರ್ಯ | ಉದ್ದೇಶ |
| --- | --- |
| `start_markdown_agent_translation` | ಚಂಕಗಳು, ಪ್ರಾಂಪ್ಟ್‌ಗಳು ಮತ್ತು ಪುನರ್‌ರಚನೆಯ ಸ್ಥಿತಿಯನ್ನು ಒಳಗೊಂಡ ಸ್ವಯಂ-ಸಂರಚಿತ Markdown ಕಾರ್ಯವನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ. |
| `finish_markdown_agent_translation` | ಒಂದು ಕೆಲಸ ಮತ್ತು ಹೋಸ್ಟ್-ಏಜೆಂಟ್‌ನ ಅನುವಾದಿಸಿದ ಚಂಕಗಳಿಂದ Markdown ಅನ್ನು ಮರುರಚಿಸುವುದು. |
| `start_notebook_agent_translation` | ಹೋಸ್ಟ್-ಏಜೆಂಟ್ ಅನುವಾದಕ್ಕಾಗಿ Markdown ಸೆಲ್ ಚಂಕಗಳನ್ನೊಳಗೊಂಡ ನೋಟ್‌ಬುಕ್ ಕೆಲಸವನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ. |
| `finish_notebook_agent_translation` | ಕೋಡ್ ಸೆಲ್‌ಗಳು, ಔಟ್‌ಪುಟ್‌ಗಳು ಮತ್ತು ಮೆಟಾಡೇಟಾವನ್ನು ಉಳಿಸಿಕೊಂಡು ನೋಟ್‌ಬುಕ್ JSON ಅನ್ನು ಮರುರಚಿಸುವುದು. |

ಈ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಮುಖ್ಯವಾಗಿ MCP ಹೋಸ್ಟ್ಗಳಿಗಾಗಿ ಉದ್ದೇಶಿಸಲಾಗಿದೆ. ನೀವು ಪ್ರೊವೈಡರ್ ಕರೆಗಳನ್ನು ನಿರ್ವಹಿಸುವ Co-op Translator ಜೊತೆಗೆ ಉತ್ಪಾದನಾ ರಿಪೊಜಿಟರಿ ಭಾಷಾಂತರಣೆ ಬೇಕಾದರೆ, `translate_markdown_content`, `translate_notebook_content`, ಅಥವಾ `run_translation` ಬಳಸಿ.

## ಪಥ ಮರುಬರೆಹ APIಗಳು

ಮಾರ್ಗ ಮರುಬರಹ APIಗಳು ಯಾವುದೇ ಅನುವಾದವನ್ನು ನಡೆಸುವುದಿಲ್ಲ. ಅವುಗಳು ಕರೆದವರು ಮೂಲ ಮಾರ್ಗ, ಅನುವಾದಿತ ಗುರಿ ಮಾರ್ಗ ಮತ್ತು ಪ್ರಾಜೆಕ್ಟ್ ರಚನೆಯನ್ನು ತಿಳಿದುಕೊಂಡ ನಂತರ ಲಿಂಕ್‌ಗಳು ಮತ್ತು ಫ್ರಂಟ್‌ಮ್ಯಾಟರ್ ಮಾರ್ಗಗಳನ್ನು ನವೀಕರಿಸುತ್ತವೆ.

| ಕಾರ್ಯ | ವ್ಯಾಪ್ತಿ | ಟಿಪ್ಪಣಿಗಳು |
| --- | --- | --- |
| `rewrite_markdown_paths` | ಮಾರ್ಕ್‌ಡೌನ್ ದೇಹ ಮತ್ತು ಫ್ರಂಟ್‌ಮ್ಯಾಟರ್ | ಅನುವಾದಿತ ಗುರಿಯಿಗಾಗಿ ಮಾರ್ಕ್‌ಡೌನ್ ಲಿಂಕ್‌ಗಳು ಮತ್ತು ಬೆಂಬಲಿತ ಫ್ರಂಟ್‌ಮ್ಯಾಟರ್ ಮಾರ್ಗ ಕ್ಷೇತ್ರಗಳನ್ನು ಮರುಬರೆಹಿಸುತ್ತದೆ. |
| `rewrite_notebook_paths` | ನೋಟ್‌ಬುಕ್ JSON ನಲ್ಲಿ ಮಾರ್ಕ್‌ಡೌನ್ ಸೆಲ್‌ಗಳು | ಪ್ರತಿ ಮಾರ್ಕ್‌ಡೌನ್ ಸೆಲ್‌ಗೆ ಮಾರ್ಕ್‌ಡೌನ್ ಮಾರ್ಗ ಮರುಬರೆಹಣೆಯನ್ನು ಅನ್ವಯಿಸುತ್ತದೆ ಮತ್ತು ಅ-ಮಾರ್ಕ್‌ಡೌನ್ ಸೆಲ್‌ಗಳನ್ನು ಬದಲಾಯಿಸದೇ ಬಿಡುತ್ತದೆ. |

`policy` ಆರ್ಗ್ಯುಮೆಂಟ್ ಈ ಕ್ಷೇತ್ರಗಳನ್ನು ಒಳಗೊಂಡಿರುವ ಶಬ್ದಕೋಶವಾಗಿರಬಹುದು:

| ಕ್ಷೇತ್ರ | ಅವಶ್ಯಕತೆ | ಉದ್ದೇಶ |
| --- | --- | --- |
| `language_code` | ಹೌದು | ಗುರಿ ಭಾಷಾ ಕೋಡ್, ಉದಾಹರಣೆಗೆ `"ko"` ಅಥವಾ `"pt-BR"`. |
| `root_dir` | ಇಲ್ಲ | ಮೂಲ ಪ್ರಾಜೆಕ್ಟ್ ರೂಟ್. ಡೀಫಾಲ್ಟ್ `"."`. |
| `translations_dir` | ಇಲ್ಲ | ಟೆಕ್ಸ್ಟ್ ಅನುವಾದ ಔಟ್‌ಪುಟ್ ಡೈರೆಕ್ಟರಿ. ಡೀಫಾಲ್ಟ್ `translations` ಅನ್ನು `root_dir` ಅಡಿಯಲ್ಲಿ. |
| `translated_images_dir` | ಇಲ್ಲ | ಅನುವಾದಿತ ಚಿತ್ರ ಔಟ್‌ಪುಟ್ ಡೈರೆಕ್ಟರಿ. ಡೀಫಾಲ್ಟ್ `translated_images` ಅನ್ನು `root_dir` ಅಡಿಯಲ್ಲಿ. |
| `translation_types` | ಇಲ್ಲ | ಸಕ್ರಿಯ ಅನುವಾದ ಪ್ರಕಾರಗಳು. ಡೀಫಾಲ್ಟ್: Markdown, ನೋಟ್ಬುಕ್ಸ್ ಮತ್ತು ಚಿತ್ರಗಳು. |
| `lang_subdir` | ಇಲ್ಲ | ಪ್ರತಿಯೊಂದು ಭಾಷಾ ಫೋಲ್ಡರ್ ಅಡಿಯಲ್ಲಿ ಐಚ್ಛಿಕ ಉಪಡೈರೆಕ್ಟರಿ. |

## ಪ್ರಾಜೆಕ್ಟ್ ಅನುವಾದ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳು

| ಪ್ಯಾರಾಮೀಟರ್ | ಪ್ರಕಾರ | ಡೀಫಾಲ್ಟ್ | ಉದ್ದೇಶ |
| --- | --- | --- | --- |
| `language_codes` | `str` | ಆವಶ್ಯಕ | ಖಾಲಿ ಸ್ಥಳದಿಂದ ವಿಭಜಿಸಲಾದ ಗುರಿ ಭಾಷೆ ಕೋಡ್‌ಗಳು, ಉದಾಹರಣೆಗೆ `"ko ja fr"`, ಅಥವಾ `"all"`. ಅಲಿಯಾಸ್ ಕೋಡ್‌ಗಳನ್ನು ಕ್ಯಾನೋನಿಕಲ್ BCP 47 ಮೌಲ್ಯಗಳಿಗೆ ಸಾಮಾನ್ಯೀಕರಿಸಲಾಗುತ್ತದೆ. |
| `root_dir` | `str` | `"."` | ಒಂದು ಅನುವಾದ ಗುರಿಗಾಗಿ ಪ್ರಾಜೆಕ್ಟ್ ರೂಟ್. `root_dirs` ಅಥವಾ `groups` ಒದಗಿಸಿದಾಗ ನಿರ್ಲಕ್ಷಿಸಲಾಗುತ್ತದೆ. |
| `update` | `bool` | `False` | ಆಯ್ದ ಭಾಷೆಗಳಿಗಾಗಿ ಇರುವ ಅನುವಾದಗಳನ್ನು ಅಳಿಸಿ ಮತ್ತು ಪುನರ್‌ಸೃಷ್ಟಿಸಿ. |
| `images` | `bool` | `False` | ಚಿತ್ರ ಅನುವಾದವನ್ನು ಒಳಗೊಳಿಸಿ. Azure AI Vision ಸಂರಚನೆ ಅಗತ್ಯವಿದೆ. |
| `markdown` | `bool` | `False` | Markdown ಅನುವಾದವನ್ನು ಸೇರಿಸಿ. |
| `notebook` | `bool` | `False` | Jupyter notebook ಅನುವಾದವನ್ನು ಸೇರಿಸಿ. |
| `debug` | `bool` | `False` | ಡಿಬಗ್ ಲಾಗಿಂಗ್ ಅನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ. |
| `save_logs` | `bool` | `False` | DEBUG-ಮಟ್ಟದ ಲಾಗ್ ಫೈಲ್‌ಗಳನ್ನು ರೂಟ್ `logs/` ಡೈರೆಕ್ಟರಿಯ ಕೆಳಗೆ ಸಂರಕ್ಷಿಸಿ. |
| `yes` | `bool` | `True` | ಪ್ರೋಗ್ರಾಮ್ಯಾಟಿಕ್ ಮತ್ತು CI ಬಳಕೆಯಿಗಾಗಿ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ದೃಢೀಕರಿಸಿ. |
| `add_disclaimer` | `bool` | `False` | ಅನುವಾದಿತ Markdown ಮತ್ತು ನೋಟ್ಬುಕ್‌ಗಳಿಗೆ ಯಂತ್ರ ಮೂಲಕ ಅನುವಾದವಾಗಿದೆ ಎಂಬ ನಿರಾಕರಣಾ ಸೂಚನೆಗಳನ್ನು ಸೇರಿಸಿ. |
| `translations_dir` | `str \| None` | `None` | ಕಸ್ಟಮ್ ಪಠ್ಯ ಅನುವಾದ ಔಟ್‌ಪುಟ್ ಡೈರೆಕ್ಟರಿ. ಸಾಪೇಕ್ಷ ಪಥಗಳು ಪ್ರತಿ ರೂಟ್ ಅನ್ನು ಆಧರಿಸಿ ಪರಿಹರಿಸಲಾಗುತ್ತವೆ. |
| `image_dir` | `str \| None` | `None` | ಕಸ್ಟಮ್ ಅನುವಾದಿತ ಚಿತ್ರ ಔಟ್‌ಪುಟ್ ಡೈರೆಕ್ಟರಿ. ಸಾಪೇಕ್ಷ پಥಗಳು ಪ್ರತಿ ರೂಟ್ ಅನ್ನು ಆಧರಿಸಿ ಪರಿಹರಿಸಲಾಗುತ್ತವೆ. |
| `root_dirs` | `Iterable[str] \| None` | `None` | ಒದೇ ಔಟ್‌ಪುಟ್ ಸೆಟ್ಟಿಂಗ್‌ಗಳನ್ನು ಹಂಚಿಕೊಳ್ಳುವ ಹಲವಾರು ರೂಟ್‌ಗಳು. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | ನಿರ್ದಿಷ್ಟ `(root_dir, translations_dir)` ಜೋಡಿಗಳು. ಇವು `root_dirs`ಗಿಂತ ಪ್ರಾಮುಖ್ಯತೆಯನ್ನು ಹೊಂದುತ್ತವೆ. |
| `repo_url` | `str \| None` | `None` | README ಭಾಷಾ ಟೇಬಲ್ ಮಾರ್ಗದರ್ಶನವನ್ನು ರೆಂಡರ್ ಮಾಡುವಾಗ ಬಳಸುವ ರೆಪೊಸಿಟರಿ URL. |
| `glossaries` | `Iterable[str] \| None` | `None` | ಅನುವಾದದ ವೇಳೆ ಉಳಿಸಬೇಕಾದ ಶಬ್ದಕೋಶ ಪದಗಳು. ನಕಲುಗಳು ಮತ್ತು ಖಾಲಿ ಪದಗಳು ಸಾಮಾನ್ಯೀಕರಿಸಲ್ಪಡುತ್ತವೆ. |
| `dry_run` | `bool` | `False` | ಫೈಲ್‌ಗಳನ್ನು ಬರೆಯದೆ ಅನುವಾದ ಪ್ರಮಾಣವನ್ನು ಅಂದಾಜಿಸಿ ಮತ್ತು ಮೈಗ್ರೇಶನ್ ವರ್ತನೆಯನ್ನು ಪೂರ್ವದೃಶ್ಯ ಮಾಡಿ. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | ಕ್ರಮೇಣ Markdown ನವೀಕರಣಗಳಿಗೆ ಐಚ್ಛಿಕ accepted-baseline ಮತ್ತು candidate persistence adapter. ಇದನ್ನು ಹೊರಹಾಕಿದರೆ ಇರುವ ಸಂಪೂರ್ಣ-ಫೈಲ್ ವರ್ತನೆ ಉಳಿಯುತ್ತದೆ. |

## ವಿಮರ್ಶೆ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳು

`run_review` ಉದ್ದೇಶಪೂರ್ವಕವಾಗಿ ಸಾಧ್ಯವಾದಷ್ಟು `run_translation` ಸಿಗ್ನೇಚರ್ ಅನ್ನು ಪ್ರತಿಬಿಂಬಿಸುತ್ತದೆ, ಅದರಿಂದ ಸ್ವಯಂಚಾಲನೆ ಕನಿಷ್ಠ branching‌ನೊಂದಿಗೆ ಭಾಷಾಂತರ ಮತ್ತು ವಿಮರ್ಶಾ ವರ್ಕ್‌ಫ್ಲೋಗಳ ನಡುವೆ ಬದಲಾಯಿಸಬಹುದು.

| ಪ್ಯಾರಾಮೀಟರ್ | ಪ್ರಕಾರ | ಡೀಫಾಲ್ಟ್ | ಉದ್ದೇಶ |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | ವಿಮರ್ಶೆ ಮಾಡಲು ಗುರಿ ಭಾಷಾ ಫೋಲ್ಡರ್‌ಗಳು. ಸ್ಪೇಸ್ ಮೂಲಕ ವಿಭಜಿಸಿದ ಸ್ಟ್ರಿಂಗ್‌ಗಳು ಮತ್ತು ಇಟರೇಬಲ್ಸ್‌ ಅನ್ನು ಒಪ್ಪಿಕೊಳ್ಳಲಾಗುತ್ತದೆ. `"all"` ಕಂಡುಹಿಡಿದ ಪ್ರತಿಯೊಂದು ಭಾಷಾ ಅನುವಾದವನ್ನೂ ವಿಮರ್ಶೆ ಮಾಡುತ್ತದೆ. |
| `root_dir` | `str` | `"."` | ಒಂದು ವಿಮರ್ಶಾ ಗುರಿಗಾಗಿ ಪ್ರಾಜೆಕ್ಟ್ ರೂಟ್. `root_dirs` ಅಥವಾ `groups` ನೀಡಿದಾಗ ನಿರ್ಲಕ್ಷಿಸಲಾಗುತ್ತದೆ. |
| `markdown` | `bool` | `False` | Markdown ಮತ್ತು MDX ಮೂಲ ಫೈಲ್‌ಗಳನ್ನು ಸೇರಿಸಿ. |
| `notebook` | `bool` | `False` | Jupyter ನೋಟ್‌ಬುಕ್ ಮೂಲ ಫೈಲ್‌ಗಳನ್ನು ಸೇರಿಸಿ. |
| `images` | `bool` | `False` | ಭಾಷಾಂತರ ಆಯ್ಕೆಗಳೊಂದಿಗೆ ಸಮತೋಲನಕ್ಕಾಗಿ ಮೀಸಲಾಗಿರುತ್ತದೆ. ಚಿತ್ರಗಳ ಲಿಂಕ್ ಉಲ್ಲೇಖಗಳನ್ನು Markdown ನಿಂದ ಪರಿಶೀಲಿಸಲಾಗುತ್ತದೆ. |
| `translations_dir` | `str \| None` | `None` | ಕಸ್ಟಮ್ ಪಠ್ಯ ಭಾಷಾಂತರ ಔಟ್‌ಪುಟ್ ಡೈರೆಕ್ಟರಿ. ಸಂಬಂಧಿತ ಪಥಗಳು ಪ್ರತಿ ರೂಟ್‌ಗೆ ಎದುರಾಗಿ ನಿರ್ಧರೆಯಾಗುತ್ತವೆ. |
| `root_dirs` | `Iterable[str] \| None` | `None` | ಒದೇ ಔಟ್‌ಪುಟ್ ಸೆಟ್ಟಿಂಗ್‌ಗಳನ್ನು ಹಂಚಿಕೊಳ್ಳುವ ಹಲವಾರು ರೂಟ್‌ಗಳು. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | ಸ್ಪಷ್ಟವಾದ `(root_dir, translations_dir)` ಜೋಡಿಗಳು. `root_dirs` ಮೇಲೆ ಪ್ರಾಧಾನ್ಯತೆ ಪಡೆಯುತ್ತದೆ. |
| `changed_from` | `str \| None` | `None` | ವಿಮರ್ಶೆಯನ್ನು ಬದಲಾದ ಮೂಲ ಫೈಲ್‌ಗಳಿಗೆ ಮಿತಿ ಹಾಕಲು ಬಳಸುವ Git ref. |
| `readme_only` | `bool` | `False` | ಪ್ರತಿ ಮೂಲ ರೂಟ್‌ನ ಅಡಿಯಲ್ಲಿ ಕೇವಲ `README.md` ಅನ್ನು ವಿಮರ್ಶೆ ಮಾಡಿ. ಮೂಲ README ಲಭ್ಯವಿಲ್ಲದಿದ್ದರೆ `ValueError` ಎಸೆದುಬಿಡುತ್ತದೆ. |
| `output_format` | `str` | `"text"` | ವಿಮರ್ಶಾ ಔಟ್‌ಪುಟ್ ಫಾರ್ಮಾಟ್. ಬೆಂಬಲಿತ ಮೌಲ್ಯಗಳು `"text"` ಮತ್ತು `"github"`. |
| `fail_on_warnings` | `bool` | `False` | ಎಚ್ಚರಿಕೆಗಳನ್ನು ದೋಷಗಳ ಜೊತೆ ಜೊತೆಗೆ ವಿಫಲತೆಗಳಾಗಿ ಪರಿಗಣಿಸಿ. |
| `debug` | `bool` | `False` | ಡೀಬಗ್ ಲಾಗಿಂಗ್ ಸಕ್ರಿಯಗೊಳಿಸಿ. |
| `save_logs` | `bool` | `False` | ರೂಟ್‌ನ `logs/` ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ DEBUG ಮಟ್ಟದ ಲಾಗ್ ಫೈಲ್‌ಗಳನ್ನು ಉಳಿಸಿ. |

`markdown`, `notebook`, ಅಥವಾ `images` ಯಾವುದೂ ಸೆಟ್ ಆಗಿರದಿದ್ದಲ್ಲಿ, API ಅನ್ವಯಿಸುವ ಸ್ಥಳಗಳಲ್ಲಿ Markdown, ನೋಟ್‌ಬುಕ್‌ಗಳು ಮತ್ತು ಚಿತ್ರ ಲಿಂಕ್ ಉಲ್ಲೇಖಗಳನ್ನು ಪರಿಶೀಲಿಸುತ್ತದೆ. ವಿಮರ್ಶೆ LLM ಪ್ರೊವೈಡರ್ ಅನ್ನು ಕರೆಮಾಡುವುದಿಲ್ಲ ಮತ್ತು API ಕೀಗಳನ್ನು ಅಗತ್ಯವಿಲ್ಲ.

## ಸಂರಚನಾ ಅಗತ್ಯಗಳು

ಪ್ರೊವೈಡರ್-ಬೆಂಬಲಿತ ಅನುವಾದ APIಗಳಿಗಾಗಿ ಅನುವಾದ ಆರಂಭಿಸುವ ಮೊದಲು ಪ್ರೊವೈಡರ್ ಸಂರಚನೆ ಅಗತ್ಯವಿದೆ:

- Markdown ಮತ್ತು ನೋಟ್‌ಬುಕ್ ಅನುವಾದಕ್ಕೆ LLM ಪ್ರೊವೈಡರ್ ಅವಶ್ಯಕ. Azure OpenAI, OpenAI, ಅಥವಾ Anthropic ಅನ್ನು ಸಂರಚಿಸಿ.
- ಚಿತ್ರ ಅನುವಾದಕ್ಕೆ LLM ಪ್ರೊವೈಡರ್ ಜೊತೆಗೆ Azure AI Vision ಅಗತ್ಯ.
- `run_translation` ಪ್ರಾಜೆಕ್ಟ್ ಅನುವಾದ ಪ್ರಾರಂಭವಾಗುವುದಕ್ಕಿಂತ ಮುಂಚೆ ಲಘು-ತೂಕದ ಸಂಪರ್ಕ ಪರಿಶೀಲನೆಗಳನ್ನು ನಡೆಸುತ್ತದೆ.
- ಏಜೆಂಟ್ ಸಹಾಯಿತ `start_*_agent_translation` ಮತ್ತು `finish_*_agent_translation` API ಗಳು Co-op Translator LLM ಪ್ರೊವೈಡರ್‌ಗಳನ್ನು ಕರೆಮಾಡುವುದಿಲ್ಲ. ಹೋಸ್ಟ್ ಅಪ್ಲಿಕೇಶನ್ ಅಥವಾ MCP ಏಜೆಂಟ್ ಸಿದ್ಧಪಡಿಸಿದ ಚಂಕ್ಸ್‌ಗಳನ್ನು ಅನುವಾದಿಸುತ್ತದೆ.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, ಮತ್ತು `run_review` ನಿಯತಸ್ವಭಾವದಿರುತ್ತವೆ ಮತ್ತು ಪ್ರೊವೈಡರ್ ಕ್ರಿಡೆನ್ಷಿಯಲ್‌ಗಳನ್ನು ಅಗತ್ಯವಿಲ್ಲ.

ಆವಶ್ಯಕ Azure OpenAI ವ್ಯಾರಿಯಬಲ್ಗಳು:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

ಆವಶ್ಯಕ OpenAI ವ್ಯಾರಿಯಬಲ್ಗಳು:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

ಆವಶ್ಯಕ Anthropic ವ್ಯಾರಿಯಬಲ್ಗಳು:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` ಮತ್ತು `ANTHROPIC_MAX_TOKENS` ಐಚ್ಛಿಕವಾಗಿವೆ. Co-op Translator 0.22.0 ನಿಂದ ಪ್ರಾರಂಭವಾಗುವ ಎಲ್ಲಾ ಪ್ರೊವೈಡರ್‌ಗಳಿಗಾಗಿ ಡೀಫಾಲ್ಟ್ ಮಾದರಿ ಕ್ಲೈಂಟ್ Microsoft Agent Framework ಆಗಿದೆ. Semantic Kernel ಅನ್ನು ತಾತ್ಕಾಲಿಕವಾಗಿ `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` ಮೂಲಕ ಇನ್ನೂ ಆಯ್ಕೆಮಾಡಬಹುದು, ಆದರೆ ಹಾಗಾದರೆ ನಿರಾಕರಣಾ ಎಚ್ಚರಿಕೆ ಉಂಟಾಗುತ್ತದೆ; ಹಂತಬದ್ಧ ತೆಗೆದುಹಾಕುವ ಯೋಜನೆಗಾಗಿ [ಸಂರಚನೆ](configuration.md#model-client-backend) ಅನ್ನು ನೋಡಿ.

ಚಿತ್ರ ಅನುವಾದಕ್ಕಾಗಿ ಅಗತ್ಯ Azure AI Vision ವ್ಯಾರಿಯಬಲ್ಗಳು:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` ನಿಯತಸ್ವಭಾವದಿರುತ್ತದೆ ಮತ್ತು LLM ಅಥವಾ Azure AI Vision ಸಂರಚನೆಯನ್ನು ಅಗತ್ಯವಿಲ್ಲ.

## ವರ್ತನೆ ಟಿಪ್ಪಣಿಗಳು

- ವಿಷಯ ಅನುವಾದ API ಗಳು ಅನುವಾದವನ್ನು ಪ್ರಾಜೆಕ್ಟ್ ಪಥ ಪುನರ್-ರಚನೆಯಿಂದ ಪ್ರತ್ಯೇಕವಾಗಿ ಇಡುತ್ತವೆ. ಅನುವಾದಿತ ವಿಷಯಕ್ಕೆ ಗುರಿ ಸ್ಥಳಕ್ಕಾಗಿ ಪ್ರಾಜೆಕ್ಟ್-ಸಾಪೇಕ್ಷ ಲಿಂಕ್‌ಗಳನ್ನು ತಿದ್ದುಗೊಳ್ಳಬೇಕಾದರೆ ಸ್ಪಷ್ಟವಾಗಿ `rewrite_markdown_paths` ಅಥವಾ `rewrite_notebook_paths` ಅನ್ನು ಕರೆ ಮಾಡಿ.
- ಪ್ರಾಜೆಕ್ಟ್ ಸಂಯೋಜನಾ API ಗಳು ವಿಷಯ ಅನುವಾದದ ಸುತ್ತಲೂ ಪ್ರಾಜೆಕ್ಟ್ ವರ್ತನೆಯನ್ನು ಸೇರಿಸುತ್ತವೆ, ಇದರಲ್ಲಿ ಫೈಲ್ ಕಂಡು ಹಿಡಿಯುವುದು, ಬರಹ, ಪಥ ಪುನರ್-ರಚನೆ, ಮೆಟಾಡೇಟಾ, ಶುದ್ಧತೆ, ಮತ್ತು ಐಚ್ಛಿಕ ಡಿಸ್ಕ್ಲೈಮರ್‌ಗಳು ಸೇರಿವೆ.
- `run_translation` CLI ಬಳಕೆ ಮಾಡುವ ಅದೇ Rich-ಬ್ಯಾಕ್ಡ್ ರಿಪೋರ್ಟರ್ ಮೂಲಕ ಪ್ರಗತಿ ಮತ್ತು ಅಂದಾಜು ಸಾರಾಂಶಗಳನ್ನು ಮುದ್ರಿಸುತ್ತದೆ. ಅಂತರಕ್ರಿಯೆಯಿಲ್ಲದ ಔಟ್‌ಪುಟ್ ಸಾದಾ ಪಠ್ಯಕ್ಕೆ ಮರಳುತ್ತದೆ.
- `dry_run=True` ವರ್ಚ್ಯುಯಲ್ README ಅಪ್ಡೇಟ್‌ಗಳನ್ನು ಬಳಸಿ ಅಂದಾಜುಗಳನ್ನು ಲೆಕ್ಕಿಸುತ್ತದೆ, ಆದರೆ README ಅಥವಾ ಅನುವಾದ ಫೈಲ್‌ಗಳನ್ನು ಬರೆಯುವುದಿಲ್ಲ.
- `groups` ಕ್ರಮವಾಗಿ ಪ್ರಕ್ರಿಯಗೊಳ್ಳುತ್ತವೆ. ಕೆಲಸ ಪ್ರಾರಂಭವಾಗುವ ಮೊದಲು ಒಟ್ಟು ಸಂಗ್ರಹಿತ ಅಂದಾಜು ಮುದ್ರಿಸಲಾಗುತ್ತದೆ.
- ಚಿತ್ರ ಅನುವಾದವನ್ನು ಆಯ್ಕೆ ಮಾಡಿದಾಗ, Vision ಸಂರಚನೆ ಇಲ್ಲದಿದ್ದರೆ ಅನುವಾದ ಪ್ರಾರಂಭವಾಗುವುದಕ್ಕಿಂತ ಮುಂಚೆ ದೋಷ ಉಂಟಾಗುತ್ತದೆ.
- ಪ್ರಸ್ತುತ ಅಲಿಯಾಸ್-ಆಧಾರಿತ ಭಾಷಾ ಫೋಲ್ಡರ್‌ಗಳನ್ನು ಗುರುತಿಸಲಾಗುತ್ತದೆ ಮತ್ತು ರನ್‌ನ ಭಾಗವಾಗಿ ಅವುಗಳನ್ನು ಮಾನ್ಯ (canonical) ಭಾಷಾ ಫೋಲ್ಡರ್ ಹೆಸರಿಗೆ ಮೈಗ್ರೇಟು ಮಾಡಬಹುದು.
- `run_review` ಅನುವಾದಿತ ಫೈಲ್‌ಗಳು ಲಭ್ಯವಿಲ್ಲದಿದ್ದಾಗ, ಅನುವಾದ ಮೆಟಾಡೇಟಾ ಕಾಣೆಯಿರುವುದು ಅಥವಾ ಹಳೆಯದಾಗಿರುವುದು, Markdown ಫ್ರಂಟ್‌ಮ್ಯಾಟರ್/ಕೋಡ್ ಫೆನ್ಸುಗಳು ದುಶ್ಫಾರ್ಮ್ಯಾಟ್ ಆಗಿರುವುದು, ಅಥವಾ ಅನುವಾದಿತ ನೋಟ್‌ಬುಕ್ JSON ಅಮಾನ್ಯವಾದರೆ ವಿಫಲಗೊಳ್ಳುತ್ತದೆ.
- `run_review` ಡೀಫಾಲ್ಟ್‌గా ಸ್ಥಳೀಯ Markdown ಮತ್ತು ಚಿತ್ರ ಲಿಂಕ್ ಗುರಿಗಳು ಇಲ್ಲದಿರುವುದನ್ನು ಎಚ್ಚರಿಕೆಗಳಾಗಿ ವರದಿ ಮಾಡುತ್ತದೆ.

## ಆಂತರಿಕ ಕರೆ ಮಾರ್ಗ

API CLI ಬಳಕೆಮಾಡುವ ಅದೇ ಕೋರ್ ಅನುಷ್ಠಾನಕ್ಕೆ ಕಾರ್ಯ ಹಂಚಿಕೊಡುತ್ತದೆ:

ಅನುವಾದ:

1. in-memory ಅನುವಾದಕ್ಕಾಗಿ `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, ಅಥವಾ `translate_image_content`.
2. ಸ್ಪಷ್ಟ ಪಥದ ನಂತರದ ಪ್ರಕ್ರಿಯೆಗಾಗಿ `co_op_translator.api.translation.rewrite_markdown_paths` ಅಥವಾ `rewrite_notebook_paths`.
3. ಸಂಪೂರ್ಣ ಪ್ರಾಜೆಕ್ಟ್ ಸಂಯೋಜನೆಯಿಗಾಗಿ `co_op_translator.api.translation.run_translation`.
4. `co_op_translator.config.Config`, `LLMConfig`, ಮತ್ತು `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Markdown, ನೋಟ್‌ಬುಕ್‌ಗಳು ಮತ್ತು ಚಿತ್ರಗಳಿಗೆ ಕೇಂದ್ರೀಕೃತ ಪ್ರಾಜೆಕ್ಟ್ ಅನುವಾದ ಮಿಕ್ಸಿನ್‌ಗಳು.
8. `co_op_translator.core` ಒಳಗಿನ Markdown, ನೋಟ್‌ಬುಕ್, ಪಠ್ಯ ಮತ್ತು ಚಿತ್ರ ಅನುವಾದಕಾರರು.

ವಿಮರ್ಶೆ:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. `co_op_translator.review.checks` ಅಡಿಯಲ್ಲಿ ನಿಯತದೃಢ ಪರಿಶೀಲನೆಗಳು

ಕೆಳಗಿನ ಕ್ಲಾಸ್ಗಳು ನಿರ್ವಹಕರಿಗೆ ಉಪಯುಕ್ತವಾಗಿವೆ, ಆದರೆ ಪ್ಯಾಕೇಜ್-ಮಟ್ಟದ ಸ್ಥಿರ API ಆಗಿ ರಫ್ತು ಮಾಡಿಲ್ಲ.

| ಕ್ಲಾಸ್ | ಮಾಡ್ಯೂಲ್ | ಜವಾಬ್ದಾರಿ |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | ಪ್ರಾಜೆಕ್ಟ್-ಮಟ್ಟದ ಅನುವಾದ, ಡೈರೆಕ್ಟರಿ ನಿರ್ವಹಣೆ, ಪ್ರತಿ-ಭಾಷೆಯ ಮೆಟಾಡೇಟಾ ಸಾಮಾನ್ಯೀಕರಣ ಮತ್ತು Markdown, ನೋಟ್‌ಬುಕ್ ಮತ್ತು ಚಿತ್ರ ಅನುವಾದಕರಿಗೆ ಕಾರ್ಯನಿರ್ವಹಣೆಯನ್ನು ಅರ್ಪಿಸುತ್ತದೆ. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, ನೋಟ್‌ಬುಕ್‌ಗಳು, ಚಿತ್ರಗಳು, ಹಳೆಯತೆ ಪತ್ತೆ ಮತ್ತು ಅನುವಾದ ಮೆಟಾಡೇಟಾ ಅಪ್ಡೇಟ್‌ಗಳಿಗಾಗಿ ಅಸಿಂಕ್ ಫೈಲ್ ಪ್ರೊಸೆಸ್ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown ಫೈಲ್ ಓದು, ವಿಷಯ ಅನುವಾದ, ಪಥ ಪುನರ್-ರಚನೆ, ಮೆಟಾಡೇಟಾ, ಡಿಸ್ಕ್ಲೈಮರ್‌ಗಳು ಮತ್ತು ಬರಹಗಳನ್ನು ಸಂಯೋಜಿಸುತ್ತದೆ. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | ನೋಟ್‌ಬುಕ್ ಫೈಲ್ ಓದು, Markdown-ಸೆಲ್ ಅನುವಾದ, ಪಥ ಪುನರ್-ರಚನೆ, ಮೆಟಾಡೇಟಾ, ಡಿಸ್ಕ್ಲೈಮರ್‌ಗಳು ಮತ್ತು ಬರಹಗಳನ್ನು ಸಂಯೋಜಿಸುತ್ತದೆ. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | ಮೂಲ ಚಿತ್ರ ಕಂಡುಹಿಡಿತ, ಚಿತ್ರ ಅನುವಾದ, ಔಟ್‌ಪುಟ್ ಪಥಗಳು, ಮೆಟಾಡೇಟಾ ಮತ್ತು ಬರಹಗಳನ್ನು ಸಂಯೋಜಿಸುತ್ತದೆ. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | ಅನುವಾದಿತ Markdown ಜೋಡಿಗಳನ್ನು ಕಂಡುಹಿಡಿಯುತ್ತದೆ, ಅನುವಾದ ಗುಣಮಟ್ಟವನ್ನು ಮೌಲ್ಯಮಾಪನ ಮಾಡುತ್ತದೆ, ಮತ್ತು ಕಡಿಮೆ ವಿಶ್ವಾಸದ ಮರೆಮರಮಾ ಕಾರ್ಯಪ್ರವಾಹಗಳಿಗಾಗಿ ವಿಶ್ವಾಸ ಮೆಟಾಡೇಟಾವನ್ನು ಓದುತ್ತದೆ. |
| `ReviewRunner` | `co_op_translator.review.runner` | ಮೂಲ ಫೈಲ್‌ಗಳು, ಗುರಿ ಭಾಷೆಗಳು ಮತ್ತು ಸಂರಚಿಸಲಾದ ಅನುವಾದ ರೂಟ್‌ಗಳಾದ್ಯಂತ ನಿಯತದೃಢ ವಿಮರ್ಶಾ ಪರಿಶೀಲನೆಗಳನ್ನು ಸಂಯೋಜಿಸುತ್ತದೆ. |
| `ReviewTarget` | `co_op_translator.review.targets` | ಒಂದು ಮೂಲ ರೂಟ್ ಮತ್ತು ಆ ರೂಟ್‌ಗಾಗಿ ವಿಮರ್ಶೆ ಮಾಡಲಾದ ಅನುವಾದ ಔಟ್‌ಪುಟ್ ಡೈರೆಕ್ಟರಿಯ ವಿವರವನ್ನು ನೀಡುತ್ತದೆ. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | ಪರಂಪರೆಯ ಅಲಿಯಾಸ್ ಭಾಷಾ ಫೋಲ್ಡರ್‌ಗಳನ್ನು ಪತ್ತೆಮಾಡಿ ಮಾನ್ಯ BCP 47 ಫೋಲ್ಡರ್ ಮೈಗ್ರೇಶನ್ ಯೋಜನೆಗಳನ್ನು ಸಿದ್ಧಪಡಿಸುತ್ತದೆ. |
| `Config` | `co_op_translator.config.base_config` | `.env` ಫೈಲ್‌ಗಳನ್ನು ಲೋಡ್ ಮಾಡಿ ಅಗತ್ಯವಿರುವ LLM ಮತ್ತು ಐಚ್ಛಿಕ Vision ಪ್ರೊವೈಡರ್‌ಗಳು ಸಂರಚಿಸಲ್ಪಟ್ಟಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸುತ್ತದೆ. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI, OpenAI ಅಥವಾ Anthropic ಅನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪತ್ತೆಮಾಡುತ್ತದೆ, ಅಗತ್ಯ ಪರಿಸರ ವ್ಯಾರಿಯಬಲ್ಗಳನ್ನು ಮಾನ್ಯಗೊಳಿಸುತ್ತದೆ ಮತ್ತು ಪ್ರೊವೈಡರ್ ಸಂಪರ್ಕ ಪರಿಶೀಲನೆಗಳನ್ನು ನಡೆಸುತ್ತದೆ. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision ಸಂರಚನೆಯನ್ನು ಪತ್ತೆಮಾಡಿ ಚಿತ್ರ ಅನುವಾದಕ್ಕಾಗಿ ಸಂಪರ್ಕ ಪರೀಕ್ಷೆಗಳನ್ನು ನಡೆಸುತ್ತದೆ. |
