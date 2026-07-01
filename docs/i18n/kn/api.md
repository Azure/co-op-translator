# Python API

ಸುರಕ್ಷಿತ ಸಾರ್ವಜನಿಕ Python API ಅನ್ನು `co_op_translator.api` ನಿಂದ ರಫ್ತು ಮಾಡಲಾಗುತ್ತದೆ. ಹೆಚ್ಚು ಎಂಟಿಗ್ರೇಷನ್‌ಗಳು ಈ ಕಾರ್ಯಪ್ರವಾಹಗಳಲ್ಲಿ ಒಂದನ್ನು ಬಳಸುತ್ತವೆ:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ಮೂಲ ವಿಷಯವನ್ನು ಓದುತ್ತದೆ, Co-op Translator ಅನ್ನು ಅನುವಾದಕ್ಕಾಗಿ ಕರೆಸುತ್ತದೆ, ಮತ್ತು ಫಲಿತಾಂಶವನ್ನು কোথೆ ಉಳಿಸುವುದೆಂದು ನಿರ್ಧರಿಸುತ್ತದೆ. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | ನಿಮ್ಮ MCP ಹೋಸ್ಟ್ ಅಥವಾ ಅಪ್ಲಿಕೇಶನ್ ಮಾದರಿ ಚಂಕ್‌ಗಳನ್ನು ಅನುವಾದಿಸುತ್ತದೆ, meðan Co-op Translator ಚಂಕಿಂಗ್ ಮತ್ತು ಪುನರ್‍ರಚನೆಯನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | ನೀವು Python API ಅನ್ನು CLI പോലെ ವ್ಯವಹರಿಸಲು ಮತ್ತು ಕಂಡುಹಿಡಿಯುವಿಕೆ, ಹೊರಹಾಕುವ ಮಾರ್ಗಗಳು, ಮೆಟಾಡೇಟಾ, ಕ್ಲೀನ್‌ಅಪ್ ಮತ್ತು ಬರವಣಿಗೆಗಳನ್ನು ಕೈಗೊಂಡಿರಬೇಕೆಂದು ಬಯಸುತ್ತೀರಿ. | `run_translation` |

`core`, `config`, `review`, ಮತ್ತು `utils` ಅಡಿಗಳಲ್ಲಿನ ತಳಹದಿ-ಮಡಗು ಮಾಡ್ಯೂಲುಗಳು ಈ API ಎಂಟ್ರಿ ಪಾಯಿಂಟ್‌ಗಳೊಂದಿಗೆ ಬಳಕೆಯಾಗುವ ಜಾರಿಗೆಂದಾಗಿವೆ.

MCP ಕ್ಲೈಂಟ್‌ಗಳು ಅದೇ ಸಾರ್ವಜನಿಕ API ಅನ್ನು [MCP Server](mcp.md) ಮೂಲಕ ಬಳಸುತ್ತವೆ. Python ನೇರವಾಗಿ ಕರೆ ಮಾಡುವಾಗ ಈ ಪುಟವನ್ನು ಬಳಸಿರಿ, ಮತ್ತು Co-op Translator ಅನ್ನು ಏಜೆಂಟ್ ಅಥವಾ ಸಂಪಾದಕಕ್ಕೆ ಹೊರಗೆ ಮಾಡಬೇಕಾದಾಗ MCP ಮಾರ್ಗದರ್ಶಿಯನ್ನು ಬಳಸಿ. CLI, Python API ಮತ್ತು MCP ನಡುವೆ ನಿರ್ಣಯ ಮಾಡಬೇಕಾದರೆ, [Choose Your Workflow](workflows.md) ನಿಂದ ಪ್ರಾರಂಭಿಸಿ.

## First-Time API Flow

Python ಕೋಡ್‌ನಿಂದ Co-op Translator ಅನ್ನು ಕರೆಸುತ್ತಿರುವರೆ ಇಲ್ಲಿ ಪ್ರಾರಂಭಿಸಿರಿ:

1. [Configuration](configuration.md) ನಲ್ಲಿ ವಿವರಣೆಯಾಗಿರುವಂತೆ LLM ಒದಗಿಸುವವರನ್ನು ಸಂರಚಿಸಿ, ನೀವು ಕೇವಲ Markdown ಅಥವಾ ನೋಟ್ಬುಕ್ ಚಂಕ್‌ಗಳನ್ನು ಹೋಸ್ಟ್-ಏಜೆಂಟ್ ಅನುವಾದಕ್ಕಾಗಿ ತಯಾರಿಸುತ್ತಿದ್ದರೆ ಮಾತ್ರ ಇದನ್ನು ಬಿಟ್ಟುಬಿಡಿ.
2. ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ಫೈಲ್ I/O ಗೆ ಸ್ವಂತವಾಗಿದೆಯೇ ಎಂದು ನಿರ್ಧರಿಸಿ.
3. ಅಪ್ಲಿಕೇಶನ್ ವೈಯಕ್ತಿಕ ಫೈಲ್‌ಗಳನ್ನು ಓದುತ್ತ ಮತ್ತು ಬರೆಯುತ್ತಿದ್ದರೆ content APIs ಅನ್ನು ಬಳಸಿ.
4. Co-op Translator ಅನ್ನು CLI ವಂತೆ ಪ್ರಾಜೆಕ್ಟ್ ಅನ್ನು پروಸೆಸ್ ಮಾಡಬೇಕಾದರೆ `run_translation` ಅನ್ನು ಬಳಸಿ.
5. ಸ್ವಯಂಚಾಲಿತ ಪರೀಕ್ಷೆಗಳಿಗೆ ನಿಖರ ಪರಿಶೀಲನೆಗಳನ್ನು ಬೇಕಿದ್ದರೆ ಅನುವಾದದ ನಂತರ `run_review` ಅನ್ನು ಬಳಸಿ.

| Goal | API to start with |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Scenario 1: Translate Individual Files or Documents

ನೀವು ಈಗಾಗಲೇ ಫೈಲ್, ಸಂಪಾದಕರ ಬಫರ್, ನೋಟ್ಬುಕ್ ಪೇ‌లోಡ್, MCP ವಿನಂತಿ, ಅಥವಾ ಕಸ್ಟಮ್ ಪೈಪ್‌ಲೈನ್ ಇನ್‌ಪುಟ್ ಹೊಂದಿದ್ದಾಗ ಈ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಬಳಸಿ. ನಿಮ್ಮ ಕೋಡ್ ಫೈಲ್ I/O ಗೆ ಜೀವನದಾಯಕವಾಗಿದೆ:

1. ಮೂಲ ವಿಷಯವನ್ನು ಓದಿ.
2. content translation APIಗಳನ್ನು ಕರೆಸಿ.
3. ಅನುವಾದಿತ ವಿಷಯ ಪ್ರಾಜೆಕ್ಟ್ ಅನುವಾದ ಫೋಲ್ಡರ್‌ಗೆ ಬರೆಯಲಾಗುವಿದ್ದರೆ ಐಚ್ಛಿಕವಾಗಿ ಪಾತ್ ಪುನರ್‍ರಚನಾ API ಅನ್ನು ಕರೆಸಿ.
4. ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್‌ನಿಂದ ಫಲಿತಾಂಶವನ್ನು ಉಳಿಸಿ ಅಥವಾ ಹಿಂತಿರುಗಿಸಿ.

content translation API ಗಳು ಪ್ರಾಜೆಕ್ಟ್ ಕಂಡುಹಿಡಿಯುವಿಕೆಯನ್ನು ನಡೆಸುವುದಿಲ್ಲ, ಮೆಟಾಡೇಟಾ ಬರೆಯುವುದಿಲ್ಲ, ನಿರ್ದಿಷ್ಟವಲ್ಲದ ಡಿಸ್ಕ್ಲೈಮರ್‌ಗಳನ್ನು ಸೇರಿಸುವುದಿಲ್ಲ, ಮತ್ತು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಲಿಂಕ್‌ಗಳನ್ನು ಪುನರ್ರಚಿಸುವುದಿಲ್ಲ.

### Markdown File

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

ಅನುವಾದಿತ Markdown Co-op Translator ಪ್ರಾಜೆಕ್ಟ್ ವಿನ್ಯಾಸದಲ್ಲಿ ಇರಿಸಲಿಲ್ಲದೆ ಇದ್ದರೆ, `rewrite_markdown_paths` ಅನ್ನು ಬಿಟ್ಟುಬಿಡಿ ಮತ್ತು ಅನುವಾದಿತ ಸ್ಟ್ರಿಂಗ್ ಅನ್ನು ನೇರವಾಗಿ ಉಳಿಸಿ.

### Notebook File

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

`translate_notebook_content` Markdown ಸೇಲ್‌ಗಳನ್ನು ಅನುವಾದ ಮಾಡುತ್ತದೆ ಮತ್ತು non-Markdown ಸೆಲ್‌ಗಳನ್ನು ಸಂರಕ್ಷಿಸುತ್ತದೆ. ಪಾತ್ ಪುನರ್‍ರಚನೆ ಕೇವಲ Markdown ಸೇಲ್‌ಗಳಿಗೆ ಅನ್ವಯಿಸಲಾಗುತ್ತದೆ.

### Image File

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

`translate_image_content` ಮೂಲ ಚಿತ್ರವನ್ನು ಓದುತ್ತದೆ ಮತ್ತು ರೆಂಡರ್ ಮಾಡಿದ `PIL.Image.Image` ಅನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ. ಇದು ಅನುವಾದಿತ ಚಿತ್ರ ಮೆಟಾಡೇಟಾ ಅನ್ನು ಬರೆಯದು.

## Scenario 2: Translate an Entire Repository

Python API ಅನ್ನು `translate` CLI ಯಂತೆ ವರ್ತಿಸಲು ಬಯಸುತ್ತಿರುವಾಗ ಈ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಬಳಸಿ. `run_translation` ಬೆಂಬಲಿತ ಫೈಲ್‌ಗಳನ್ನು ಕಂಡುಹಿಡಿಯುತ್ತದೆ, ಆಯ್ಕೆಮಾಡಿದ ವಿಷಯ ಪ್ರಕಾರಗಳನ್ನು ಅನುವಾದಿಸುತ್ತದೆ, ಪಾತ್‌ಗಳನ್ನು ಪುನರ್‍ರಚಿಸುತ್ತದೆ, ಔಟ್‌ಪುಟ್ ಫೈಲ್‌ಗಳನ್ನು ಬರೆಯುತ್ತದೆ, ಮೆಟಾಡೇಟಾ ನವೀಕರಿಸುತ್ತದೆ, ಮತ್ತು ಕ್ಲೀನ್‌ಅಪ್ ಆಗಿರುವ ತರಹದ ಅನುವಾದ ನಿರ್ವಹಣಾ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ.

`run_translation` ಪ್ರಾಜೆಕ್ಟ್ ಸಂಯೋಜನೆದ ಪ್ರಮುಖ ಎಂಟ್ರಿಪಾಯಿಂಟ್ ಆಗಿದೆ. `translate_project` ಅನ್ನು ಸಮರೋಪ್ಯದ ಉಲ್ಲೇಖವಾಗಿ ಅದೇ ವರ್ತನೆ ಹೊಂದಿರುವ ಅವಲಂಬನಿಯ ಆಲಿಯಾಸ್ ಆಗಿ ರಫ್ತು ಮಾಡಲಾಗಿದೆ.

ನवंबर Markdown ಫೈಲ್‌ಗಳನ್ನು ಪ್ರಸ್ತುತ ರೆಪೊಸಿಟರಿ‌ನಲ್ಲಿ ಕೊರಿಯನ್ ಮತ್ತು ಜಪಾನೀಸ್‌ಗೆ ಅನುವಾದಿಸಿ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

ನಿರ್ದಿಷ್ಟ ಪ್ರಾಜೆಕ್ಟ್ ರೂಟ್‌ನಿಂದ ಕೇವಲ ನೋಟ್ಬುಕ್‌ಗಳನ್ನು ಅನುವಾದಿಸಿ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

ಫೈಲ್‌ಗಳನ್ನು ಬರೆಯದೆ ಅನುವಾದ ಪ್ರಮಾಣವನ್ನು ಪೂರ್ವದೃಶ್ಯ ಮಾಡಿ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

ಒಂದು ಕರೆದಲ್ಲಿ ಅನೇಕ ವಿಷಯ ರೂಟ್‌ಗಳನ್ನು ಅನುವಾದಿಸಿ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

ಅನುವಾದಗಳನ್ನು ಸ್ಪಷ್ಟ ಔಟ್‌ಪುಟ್ ಗುಂಪುಗಳಲ್ಲಿ ಬರೆಯಿರಿ:

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

ಪ್ರತಿಯೊಬ್ಬ ಭಾಷೆಗೆ nested ಉಪಡೈರೆಕ್ಟರಿ ಬೇಕಾಗಿದ್ದಾಗ ಪ್ರತಿ ಭಾಷೆಗೆ ಪ್ಲೇಸ್‌ಹೋಲ್ಡರ್ ಬಳಸಿ:

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

`markdown`, `notebook`, ಅಥವಾ `images` ಗಳಲ್ಲಿ ಯಾವುದೂ ಸೆಟ್ ಮಾಡಲಾಗಿಲ್ಲದಿದ್ದರೆ, API ಎಲ್ಲಾ ಬೆಂಬಲಿತ ಪ್ರಕಾರಗಳನ್ನು ಅನುವಾದಿಸುತ್ತದೆ: Markdown, ನೋಟ್ಬುಕ್‌ಗಳು, ಮತ್ತು ಚಿತ್ರಗಳು.

## Review Translated Output

`run_review` deterministic ಅನುವಾದ ಪರಿಶೀಲನೆಗಳನ್ನು LLM ಅಥವಾ Vision ಸಾಠಕ್ಕಿಲ್ಲದೆ ನಡಿಸುತ್ತದೆ.

!!! note "ಬೆಟಾ"
    `run_review` ಒಂದು ಬೆಟಾ ನಿರ್ದಿಷ್ಟ ಪರಿಶೀಲನಾ API ಆಗಿದೆ. ಅದು ಮಾದರಿ ಒದಗಿಸುವವರನ್ನು ಕರೆಸುವುದಿಲ್ಲ ಅಥವಾ ಫೈಲ್‌ಗಳನ್ನು ಬರೆಯುವುದಿಲ್ಲ, ಆದರೆ ಪರಿಶೀಲನೆಗಳು ಮತ್ತು ಸಮಸ್ಯೆ ಸ್ಕಿಮಾಗಳು ಅಭಿವೃದ್ಧಿ ಆಗಬಹುದು.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

ಮೂಲ ರೆಫ್ನ ವಿರುದ್ಧ ಬದಲಾದ ಫೈಲ್‌ಗಳನ್ನು ಮಾತ್ರ ಪರಿಶೀಲಿಸಿ ಮತ್ತು GitHub-ಶೈಲಿಯ ಔಟ್‌ಪುಟ್ ಅನ್ನು ಮುದ್ರಿಸಿ:

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

## Copy-Paste API Examples

ಫೈಲ್ ಬರವಣಿಗೆಗಳಿಲ್ಲದೆ Markdown ವಿಷಯವನ್ನು ಅನುವಾದಿಸಿ:

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

Markdown ಲಿಂಕ್‌ಗಳನ್ನು ಅನುವಾದಿಸಿ ಮತ್ತು ಪುನರ್‍ರಚಿಸಿ:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

Python ನಿಂದ ರೆಪೊಸಿಟರಿಯನ್ನು ಅನುವಾದಿಸಿ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

ಬಹು ರುಟ್‌ಗಳನ್ನು ಅನುವಾದಿಸಿ:

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

ಗ್ಲಾಸರಿ ಪದಗಳನ್ನು ಸಂರಕ್ಷಿಸಿ:

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

## Public Entry Points

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
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

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## Content Translation APIs

Content translation API ಗಳು ಈಗಾಗಲೇ ಸ್ಮೃತಿಯಲ್ಲಿ ವಿಷಯವನ್ನು ಹೊಂದಿರುವ ಎಂಟಿಗ್ರೇಷನ್‌ಗಳಿಗೆ ಉದ್ದೇಶಿಸಲಾಗಿದೆ, ಉದಾಹರಣೆಗೆ ಒಂದು ಸಂಪಾದಕ ಎಕ್ಸ್ಟೆನ್ಷನ್, MCP ಉಪಕರಣ, ನೋಟ್ಬುಕ್ ಪ್ರಾಸೆಸರ್, ಅಥವಾ ಕಸ್ಟಮ್ ಪೈಪ್‌ಲೈನ್.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Markdown ವಿಷಯವನ್ನು ಮಾತ್ರ ಅನುವಾದಿಸುತ್ತದೆ. ಅದು ಲಿಂಕ್‌ಗಳನ್ನು ಪುನರ್‍ರಚಿಸುವುದಿಲ್ಲ, ಮೆಟಾಡೇಟಾ ಬರೆಯುವುದಿಲ್ಲ, ಅಥವಾ ಡಿಸ್ಕ್ಲೈಮರ್‌ಗಳನ್ನು ಸೇರಿಸುವುದಿಲ್ಲ. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Markdown ಸೇಲ್‌ಗಳನ್ನು ಅನುವಾದಿಸುತ್ತದೆ ಮತ್ತು non-Markdown ಸೇಲ್‌ಗಳನ್ನು ಸಂರಕ್ಷಿಸುತ್ತದೆ. ಅದು ಲಿಂಕ್‌ಗಳನ್ನು ಪುನರ್‍ರಚಿಸುವುದಿಲ್ಲ, ಮೆಟಾಡೇಟಾ ಬರೆಯುವುದಿಲ್ಲ, ಅಥವಾ ಡಿಸ್ಕ್ಲೈಮರ್‌ಗಳನ್ನು ಸೇರಿಸುವುದಿಲ್ಲ. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. ಚಿತ್ರದಲ್ಲಿ ಇರುವ ಪಠ್ಯವನ್ನು ಹೊರತೆಗೆದು ಅನುವಾದಿಸಿ ನಂತರ ರೆಂಡರ್ ಮಾಡಿದ ಚಿತ್ರವನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ. ಅದು ಅನುವಾದಿತ ಚಿತ್ರ ಮೆಟಾಡೇಟಾ ಅನ್ನು ಉಳಿಸುವುದಿಲ್ಲ. |

`translate_markdown_content` ಮತ್ತು `translate_notebook_content` ಐಚ್ಛಿಕ `source_path` ಅನ್ನು ಅವರ ಆಯ್ಕೆಗಳ ಮೂಲಕ ಸ್ವೀಕರಿಸುತ್ತವೆ. ಪಾತ್ ಅನುವಾದಕಕ್ಕೆ ಸಂಧರ್ಭವಾಗಿ ಪಾಸ್ ಆಗುತ್ತದೆ; ಕರೆಯುವವರು ಅನುವಾದದ ನಂತರ ಪ್ರಾಜೆಕ್ಟ್-ವಿಶೇಷ ಪಾತ್ ಪುನರ್‍ರಚನೆಗಾಗಿ ಹೊಣೆಗಾರರಾಗಿರುತ್ತಾರೆ.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

ಅದೇ ಆಯ್ಕೆಗಳು ನಿಘಂಟುಗಳಾಗಿ(dictionary) ಪಾಸ್ ಮಾಡಬಹುದಾಗಿದೆ:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

ಏಜೆಂಟ್-ಸಹಾಯಿತ API ಗಳು Co-op Translator ನಿಂದ Azure OpenAI ಅಥವಾ OpenAI ಅನ್ನು ಕರೆಸುವುದಿಲ್ಲ. ಅವು Markdown ಅಥವಾ ನೋಟ್ಬುಕ್ ಚಂಕ್‌ಗಳನ್ನು ಹೋಸ್ಟ್ ಏಜೆಂಟ್ ಅನ್ನು ಅನುವಾದಿಸಲು ತಯಾರಿಸುತ್ತವೆ, ನಂತರ ಅನುವಾದಿತ ಚಂಕ್‌ಗಳಿಂದ ಅಂತಿಮ ವಿಷಯವನ್ನು ಪುನರ್‍ರಚಿಸುತ್ತವೆ.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | ಚಂಕ್‌ಗಳು, ಪ್ರಾಂಪ್ಟ್‌ಗಳು, ಮತ್ತು ಪುನರ್‍ರಚನೆ κατάσταση ಸೇರಿದಂತೆ ಸ್ವಯಂ-ಸಂಯುಕ್ತ Markdown ಕೆಲಸವನ್ನು ಹಿಂತಿರುಗಿಸಿ. |
| `finish_markdown_agent_translation` | ಒಂದು ಕೆಲಸ ಮತ್ತು ಹೋಸ್ಟ್-ಏಜೆಂಟ್ ಅನುವಾದಿತ ಚಂಕ್‌ಗಳದಿಂದ Markdown ಅನ್ನು ಪುನರ್‍ರಚಿಸಿ. |
| `start_notebook_agent_translation` | ಹೋಸ್ಟ್-ಏಜೆಂಟ್ ಅನುವಾದಕ್ಕೆ Markdown-ಸೆಲ್ ಚಂಕ್‌ಗಳೊಂದಿಗೆ ನೋಟ್ಬುಕ್ ಕೆಲಸವನ್ನು ಹಿಂತಿರುಗಿಸಿ. |
| `finish_notebook_agent_translation` | ಕೋಡ್ ಸೆಲ್‌ಗಳು, ಔಟ್‌ಪುಟ್‌ಗಳು ಮತ್ತು ಮೆಟಾಡೇಟಾವನ್ನು ಸಂರಕ್ಷಿಸುತ್ತಾ ನೋಟ್ಬುಕ್ JSON ಅನ್ನು ಪುನರ್‍ರಚಿಸಿ. |

ಈ ಕಾರ್ಯಪ್ರವಾಹವು ಮುಖ್ಯವಾಗಿ MCP ಹೋಸ್ಟ್‌ಗಳಿಗಾಗಿ ಉದ್ದೇಶಿಸಲ್ಪಟ್ಟಿದೆ. ನೀವು ಕೊಠಡಿ ಒದಗಿಸುವ ಕರೆಗಳನ್ನು ನಿರ್ವಹಿಸುವ Co-op Translator ಜೊತೆಗೆ ಉತ್ಪಾದನಾ ರೆಪೊಸಿಟರಿ ಅನುವಾದವನ್ನು ಬೇಕಾದರೆ, `translate_markdown_content`, `translate_notebook_content`, ಅಥವಾ `run_translation` ಅನ್ನು ಬಳಸಿರಿ.

## Path Rewriting APIs

ಪಾತ್ ಪುನರ್‍ರಚನಾ API ಗಳು ಯಾವುದೇ ಅನುವಾದವನ್ನು ನಡೆಸುವುದಿಲ್ಲ. ಅವು ಕರೆತರುವವರು ಮೂಲ ಪಥ, ಅನುವಾದಿತ ಗುರಿ ಪಥ ಮತ್ತು ಪ್ರಾಜೆಕ್ಟ್ ವಿನ್ಯಾಸವನ್ನು ಅರಿತುಕೊಂಡ ನಂತರ ಲಿಂಕ್‌ಗಳು ಮತ್ತು ಫ್ರಂಟ್‌ಮ್ಯಾಟರ್ ಪಥಗಳನ್ನು ನವೀಕರಿಸವುದಕ್ಕೆ ಬಳಸಲಾಗುತ್ತವೆ.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | ಅನುವಾದಿತ ಗುರಿಗಾಗಿ Markdown ಲಿಂಕ್‌ಗಳು ಮತ್ತು ಬೆಂಬಲಿತ ಫ್ರಂಟ್‌ಮ್ಯಾಟರ್ ಪಥ ಕ್ಷೇತ್ರಗಳನ್ನು ಪುನರ್‍ರಚಿಸುತ್ತದೆ. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | ಪ್ರತಿ Markdown ಸೇಲ್‌ಗೆ Markdown ಪಾತ್ ಪುನರ್‍ರಚನೆಯನ್ನು ಅನ್ವಯಿಸುತ್ತದೆ ಮತ್ತು non-Markdown ಸೇಲ್‌ಗಳನ್ನು ಬದಲಾಯಿಸದೆ ಇರಿಸುತ್ತದೆ. |

`policy` ಆರ್ಗ್ಯೂಮೆಂಟ್ ಈ ಕ್ಷೇತ್ರಗಳನ್ನು ಹೊಂದಿರುವ ನಿಘಂಟಾಗಿರಬಹುದು:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | ಗುರಿ ಭಾಷೆಯ ಕೋಡ್, ಉದಾಹರಣೆಗೆ `"ko"` ಅಥವಾ `"pt-BR"`. |
| `root_dir` | No | ಮೂಲ ಪ್ರಾಜೆಕ್ಟ್ ರೂಟ್. ಡೀಫಾಲ್ಟ್ `"."`. |
| `translations_dir` | No | ಪಠ್ಯ ಅನುವಾದ ಔಟ್‌ಪುಟ್ ಡೈರೆಕ್ಟರಿ. ಡೀಫಾಲ್ಟ್ `translations` ಅಂದು `root_dir` ಅಡಿಯಲ್ಲಿ. |
| `translated_images_dir` | No | ಅನುವಾದಿತ ಚಿತ್ರ ಔಟ್‌ಪುಟ್ ಡೈರೆಕ್ಟರಿ. ಡೀಫಾಲ್ಟ್ `translated_images` ಅಂದು `root_dir` ಅಡಿಯಲ್ಲಿ. |
| `translation_types` | No | ಸಕ್ರಿಯ ಅನುವಾದ ಪ್ರಕಾರಗಳು. ಡೀಫಾಲ್ಟ್ Markdown, ನೋಟ್ಬುಕ್‌ಗಳು, ಮತ್ತು ಚಿತ್ರಗಳು. |
| `lang_subdir` | No | ಪ್ರತಿ ಭಾಷಾ ಫೋಲ್ಡರ್ ಅಡಿ ಐಚ್ಛಿಕ ಉಪಡೈರೆಕ್ಟರಿ. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | ಅವಭಾಷೆಗಳ ಕೋಡ್‌ಗಳು ಸ್ಪೇಸ್-ವಿಭಜಿತ, ಉದಾಹರಣೆಗೆ `"ko ja fr"`, ಅಥವಾ `"all"`. ಸಮಾನಾರ್ಥಕ ಕೋಡ್‌ಗಳು ಸಾಮಾನ್ಯ BCP 47 ಮೌಲ್ಯಗಳಿಗೆ ಸಾಮಾನ್ಯೀಕರಿಸಲಾಗುತ್ತವೆ. |
| `root_dir` | `str` | `"."` | ಒಂದೇ ಅನುವಾದ ಗುರಿಗಾಗಿ ಪ್ರಾಜೆಕ್ಟ್ ರೂಟ್. `root_dirs` ಅಥವಾ `groups` ಒದಗಿಸಿದಾಗ ನಿರ್ಲಕ್ಷ್ಯಗೊಳ್ಳಲಿದೆ. |
| `update` | `bool` | `False` | ಆಯ್ಕೆಮಾಡಲಾದ ಭಾಷೆಗಳಿಗಾಗಿ ಇರುವ ಅನುವಾದಗಳನ್ನು ಅಳಿಸಿ ಮರುಸೃಷ್ಟಿಸು. |
| `images` | `bool` | `False` | ಚಿತ್ರ ಅನುವಾದವನ್ನು ಸೇರಿಸಿ. Azure AI Vision ಕಾನ್ಫಿಗರೇಶನ್ ಅಗತ್ಯವಿದೆ. |
| `markdown` | `bool` | `False` | Markdown ಅನುವಾದವನ್ನು ಸೇರಿಸಿ. |
| `notebook` | `bool` | `False` | Jupyter ನೋಟ್ಬುಕ್ ಅನುವಾದವನ್ನು ಸೇರಿಸಿ. |
| `debug` | `bool` | `False` | ಡಿಬಗ್ ಲಾಗಿಂಗ್ ಅನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ. |
| `save_logs` | `bool` | `False` | ರೂಟ್ `logs/` ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ DEBUG-ಮಟ್ಟದ ಲಾಗ್ ಫೈಲ್‌ಗಳನ್ನು ಉಳಿಸಿ. |
| `yes` | `bool` | `True` | ಪ್ರೋಗ್ರಾಮ್ಯಾಟಿಕ್ ಮತ್ತು CI ಬಳಕೆಯಿಗಾಗಿ ಪ್ರಾಂಪ್ಟ್‌ಗಳಿಗೆ ಸ್ವಯಂ-ನಿಶ್ಚಯ. |
| `add_disclaimer` | `bool` | `False` | ಅನುವಾದಿತ Markdown ಮತ್ತು ನೋಟ್ಬುಕ್‌ಗಳಿಗೆ ಯಂತ್ರ ಅನುವಾದ ಡಿಸ್ಕ್ಲೈಮರ್‌ಗಳನ್ನು ಸೇರಿಸಿ. |
| `translations_dir` | `str \| None` | `None` | ಕಸ್ಟಮ್ ಪಠ್ಯ ಅನುವಾದ ಔಟ್‌ಪುಟ್ ಡೈರೆಕ್ಟರಿ. ಸಂಬಂಧಿತ ಪಥಗಳು ಪ್ರತಿ ರೂಟ್ ವಿರುದ್ಧ ಪರಿಹರಿಸಲಾಗುತ್ತದೆ. |
| `image_dir` | `str \| None` | `None` | ಕಸ್ಟಮ್ ಅನುವಾದಿತ ಚಿತ್ರ ಔಟ್‌ಪುಟ್ ಡೈರೆಕ್ಟರಿ. ಸಂಬಂಧಿತ ಪಥಗಳು ಪ್ರತಿ ರೂಟ್ ವಿರುದ್ಧ ಪರಿಹರಿಸಲಾಗುತ್ತದೆ. |
| `root_dirs` | `Iterable[str] \| None` | `None` | ಒಂದೇ ಔಟ್‌ಪುಟ್ ಸೆಟ್ಟಿಂಗ್ಗಳನ್ನು ಹಂಚುವ ಅನೇಕ ರೂಟ್‌ಗಳು. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | ಸ್ಪಷ್ಟ `(root_dir, translations_dir)` ಜೋಡಿಗಳು. `root_dirs` ಮೇಲೆ ಪ್ರಾಧಾನ್ಯತೆಯುತವಾಗಿದೆ. |
| `repo_url` | `str \| None` | `None` | README ಭಾಷಾ ಟೇಬಲ್ ಮಾರ್ಗದರ್ಶನವನ್ನು ರೆಂಡರ್ ಮಾಡುವಾಗ ಬಳಸುವ ರೆಪೊಸಿಟರಿ URL. |
| `glossaries` | `Iterable[str] \| None` | `None` | ಅನುವಾದದ ವೇಳೆ ಸಂರಕ್ಷಿಸಲು ಗ್ಲಾಸರಿ ಪದಗಳು. ಪ್ರತಿಲಿಪಿಗಳು ಮತ್ತು ಖಾಲಿ ಪದಗಳನ್ನು ಸಾಮಾನ್ಯೀಕರಿಸಲಾಗುತ್ತದೆ. |
| `dry_run` | `bool` | `False` | ಫೈಲ್‌ಗಳನ್ನು ಬರೆಯದೆ ಅನುವಾದ ಪ್ರಮಾಣವನ್ನು ಅಂದಾಜಿಸಿ ಮತ್ತು ಮೈಗ್ರೇಶನ್ ವರ್ತನೆಯನ್ನು ಪೂರ್ವದೃಶ್ಯ ಮಾಡಿ. |

## Review Parameters

`run_review` ಹೆಚ್ಚಾಗಿ `run_translation` ಸಹಿತವಾದ ಸಹಿ ಸಹಿತವೆಂಬ ಸಿಗ್ನೇಚರ್ ಅನ್ನು ನಕಲಿಸುತ್ತದೆ જેથી ಸ್ವಯಂಕ್ರಿಯೆಗಳು ಅನುವಾದ ಮತ್ತು ವಿಮರ್ಶಾ ಕಾರ್ಯಪ್ರವಾಹಗಳ ನಡುವೆ ಕನಿಷ್ಟ ಶಾಖಾದಲ್ಲಿ ಬದಲಾಯಿಸಿಕೊಳ್ಳಬಹುದು.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | ವಿಮರ್ಶೆಗಾಗಿ ಗುರಿ ಭಾಷಾ ಫೋಲ್ಡರ್‌ಗಳು. ಸ್ಪೇಸ್-ವಿಭಜಿತ ಸ್ಟ್ರಿಂಗ್‌ಗಳು ಮತ್ತು ಇಟರೆಬಲ್ಗಳನ್ನು ಸ್ವೀಕರಿಸಲಾಗುತ್ತದೆ. `"all"` ಕಂಡುಹಿಡಿದ ಎಲ್ಲ ಅನುವಾದ ಭಾಷೆಗಳನ್ನು ವಿಮರ್ಶೆ ಮಾಡುತ್ತದೆ. |
| `root_dir` | `str` | `"."` | ಒಂದೇ ವಿಮರ್ಶಾ ಗುರಿಗಾಗಿ ಪ್ರಾಜೆಕ್ಟ್ ರೂಟ್. `root_dirs` ಅಥವಾ `groups` ಒದಗಿಸಿದಾಗ ನಿರ್ಲಕ್ಷ್ಯಗೊಳ್ಳಲಿದೆ. |
| `markdown` | `bool` | `False` | Markdown ಮತ್ತು MDX ಮೂಲ ಫೈಲ್‌ಗಳನ್ನು ಸೇರಿಸಿ. |
| `notebook` | `bool` | `False` | Jupyter ನೋಟ್ಬುಕ್ ಮೂಲ ಫೈಲ್‌ಗಳನ್ನು ಸೇರಿಸಿ. |
| `images` | `bool` | `False` | ಅನುವಾದ ಆಯ್ಕೆಗಳ ಜೊತೆಗೆ ಸಮಪ್ರಮಾಣಕ್ಕಾಗಿ ಮೀಸಲಾಗಿದೆ. Markdown ನಿಂದ ಚಿತ್ರಗಳಿಗೆ సంబంధించిన ಲಿಂಕ್ ರೆಫರೆನ್ಸ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಲಾಗುತ್ತದೆ. |
| `translations_dir` | `str \| None` | `None` | ಕಸ್ಟಮ್ ಪಠ್ಯ ಅನುವಾದ ಔಟ್‌ಪುಟ್ ಡೈರೆಕ್ಟರಿ. ಸಂಬಂಧಿತರಾದ ಪಥಗಳು ಪ್ರತಿ ಮೂಲದ ವಿರುದ್ಧ ಪರಿಹರಿಸಲಾಗುತ್ತವೆ. |
| `root_dirs` | `Iterable[str] \| None` | `None` | ಒಂದು ಸಮರ್ಪಕ ಔಟ್‌ಪುಟ್ ಸೆಟ್ಟಿಂಗ್‌ಗಳನ್ನು ಹಂಚಿಕೊಳ್ಳುವ ಬಹು ಮೂಲಗಳು. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | ಸ್ಪಷ್ಟ `(root_dir, translations_dir)` ಜೋಡೆಗಳು. `root_dirs` ಮೇಲೆ ಆದ್ಯತೆಯನ್ನು ಹೊಂದುತ್ತದೆ. |
| `changed_from` | `str \| None` | `None` | ಬದಲಾವಣೆಗೊಂಡ ಮೂಲ ಕಡತಗಳಿಗೂ ವಿಮರ್ಶೆ ಸೀಮಿತಗೊಳಿಸಲು ಬಳಸಲಾಗುವ Git ರೆಫ್. |
| `output_format` | `str` | `"text"` | ವಿಮರ್ಶೆ ಔಟ್‌ಪುಟ್ ಫಾರ್ಮ್ಯಾಟ್. ಬೆಂಬಲಿತ ಮೌಲ್ಯಗಳು `"text"` ಮತ್ತು `"github"`. |
| `fail_on_warnings` | `bool` | `False` | ಎಚ್ಚರಿಕೆಗಳನ್ನು ದೋಷಗಳ ಜೊತೆಗೆ ವಿಫಲತೆಗಳಾಗಿ ಪರಿಗಣಿಸು. |
| `debug` | `bool` | `False` | ಡಿಬಗ್ ಲಾಗಿಂಗ್ ಸಕ್ರಿಯಗೊಳಿಸಿ. |
| `save_logs` | `bool` | `False` | ರೂಟ್ `logs/` ಡೈರೆಕ್ಟರಿಯಡಿ DEBUG ಮಟ್ಟದ ಲಾಗ್ ಫೈಲ್‌ಗಳನ್ನು ಉಳಿಸಿ. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## ಸಂರಚನಾ ಅಗತ್ಯಗಳು

Provider-backed translation APIs require provider configuration before translating:

- Markdown ಮತ್ತು ನೋಟ್‌ಬುಕ್ ಅನುವಾದಕ್ಕೆ LLM ಒದಗಿಸುವವರು ಅಗತ್ಯ. Configure either Azure OpenAI or OpenAI.
- ಚಿತ್ರ ಅನುವಾದಕ್ಕೆ LLM ಒದಗಿಸುವವರ ಜೊತೆಗೆ Azure AI Vision ಅಗತ್ಯ.
- `run_translation` ಪ್ರಾಜೆಕ್ಟ್ ಅನುವಾದವನ್ನು ಪ್ರಾರಂಭಿಸುವ ಮೊದಲು ಲಘು ಸಂಪರ್ಕ ಪರಿಶೀಲನೆಗಳನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸುತ್ತದೆ.
- ಎಜೆಂಟ್-ಸಹಾಯಿತ `start_*_agent_translation` ಮತ್ತು `finish_*_agent_translation` APIs do not call Co-op Translator LLM providers. The host application or MCP agent translates the prepared chunks.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, and `run_review` ನಿರ್ಧಾರಾತ್ಮಕವಾಗಿವೆ ಮತ್ತು ಒದಗಿಸುವವರ ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು ಅಗತ್ಯವಿಲ್ಲ.

Required Azure OpenAI variables:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Required OpenAI variables:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Required Azure AI Vision variables for image translation:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` ನಿರ್ಧಾರದ್ಮಕವಾಗಿದೆ ಮತ್ತು Azure OpenAI, OpenAI, ಅಥವಾ Azure AI Vision ಸಂರಚನೆ ಅಗತ್ಯವಿಲ್ಲ.

## ವರ್ತನಾ ಟಿಪ್ಪಣಿಗಳು

- ವಿಷಯ ಅನುವಾದ APIಗಳು ಅನುವಾದವನ್ನು ಪ್ರಾಜೆಕ್ಟ್ ಪಥ ಪುನರ್ಲಿಖನದಿಂದ ಬೇರ್ಪಡಿಸುತ್ತವೆ. ಅನುವಾದಿತ ವಿಷಯಕ್ಕೆ ಗಮ್ಯದ ಸ್ಥಳಕ್ಕೆ ಹೊಂದುವಂತೆ ಪ್ರಾಜೆಕ್ಟ್-ಸಾಪೇಕ್ಷ ಲಿಂಕ್‌ಗಳನ್ನು ಸರಿಹೊಂದಿಸಲು `rewrite_markdown_paths` ಅಥವಾ `rewrite_notebook_paths` ಅನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ಕರೆಸಿಕೊಳ್ಳಿ.
- ಪ್ರಾಜೆಕ್ಟ್ ನಿರ್ವಹಣಾ APIಗಳು ವಿಷಯ ಅನುವಾದ ಸುತ್ತಲಿನ ಪ್ರಾಜೆಕ್ಟ್ ವರ್ತನೆಯನ್ನು ಸೇರಿಸುತ್ತವೆ, ಇದರಲ್ಲಿ ಫೈಲ್ ಪತ್ತೆ, ಬರವಣಿಗೆ, ಪಥ ಪುನರ್ಲೇಖನ, ಮೆಟಾಡೇಟಾ, ಕ್ಲೀನ್‌ಅಪ್ ಮತ್ತು ಐಚ್ಛಿಕ ನಿರಾಕರಣೆಗಳು ಒಳಗೊಂಡಿರುತ್ತವೆ.
- `run_translation` Click ಮುಖಾಂತರ ಪ್ರಗತಿ ಮತ್ತು ಅಂದಾಜು ಸಾರಾಂಶಗಳನ್ನು ಮುದ್ರಿಸುತ್ತದೆ, CLI ಬಳಕೆದಾರ ಅನುಭವಕ್ಕೆ ಹೊಂದಿಕೆಯಾಗುವಂತೆ.
- `dry_run=True` ವಾಸ್ತವ README അപ್‌ಡೇಟ್ಗಳನ್ನು ಕಲ್ಪನೆ ರೂಪದಲ್ಲಿ ಬಳಸಿಕೊಂಡು ಅಂದಾಜುಗಳನ್ನು ಗಣನೆ ಮಾಡುತ್ತದೆ, ಆದರೆ README ಅಥವಾ ಅನುವಾದ ಫೈಲ್‌ಗಳನ್ನು ಬರೆಯುವುದಿಲ್ಲ.
- `groups` ಕ್ರಮವಾಗಿ ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಲ್ಪಡುತ್ತವೆ. ಕೆಲಸ ಪ್ರಾರಂಭ ಮಾಡುವ ಮೊದಲು ಒಟ್ಟು ಏಕ ಅಂದಾಜು ಮುದ್ರಿಸಲಾಗುತ್ತದೆ.
- ಚಿತ್ರ ಅನುವಾದ ಆಯ್ಕೆ ಮಾಡಿದಾಗ, Vision ಸಂರಚನೆ ಇಲ್ಲದಿದ್ದರೆ ಅನುವಾದ ಪ್ರಾರಂಭವಾಗುವ ಮುನ್ನ ದೋಷ ಉಂಟಾಗುತ್ತದೆ.
- ಇತ್ತೀಚಿನ ಅಲಿಯಾಸ್ ಆಧಾರಿತ ಭಾಷಾ ಫೋಲ್‌ಡರ್‌ಗಳನ್ನು ಪತ್ತೆಹಚ್ಚಲಾಗುತ್ತದೆ ಮತ್ತು ರನ್‌ನ一 ಭಾಗವಾಗಿ ಅವುಗಳನ್ನು ಮಾನಕ BCP 47 ಭಾಷಾ ಫೋಲ್ಡರ್ ಹೆಸರಗಳಿಗೆ ಮைக್ರೇಟ್ ಮಾಡಲಾಗಬಹುದು.
- `run_review` ಅನುವಾದಿತ ಫೈಲ್‌ಗಳ ಕೊರತೆ, ಕಳೆದುಹೋಗಿದ ಅಥವಾ ಹಳೆಯ ಅನುವಾದ ಮೆಟಾಡೇಟಾ, ದೋಷಪೂರಿತ Markdown ಫ್ರಂಟ್ಮ್ಯಾಟರ್/ಕೋಡ್ ಫೆನ್ಸ್ಗಳು ಮತ್ತು ಅಮಾನ್ಯ ಅನುವಾದಿತ ನೋಟ್‌ಬುಕ್ JSON ಇರುವಾಗ ವಿಫಲಗೊಳ್ಳುತ್ತದೆ.
- `run_review` ಸ್ಥಳೀಯ Markdown ಮತ್ತು ಚಿತ್ರ ಲಿಂಕ್ ಗುರಿಗಳ ಕೊರತೆಯನ್ನು ಡೀಫಾಲ್ಟ್ ಆಗಿ ಎಚ್ಚರಿಕೆಗಳಾಗಿ ವರದಿ ಮಾಡುತ್ತದೆ.

## ಆಂತರಿಕ ಕರೆ ಹಾದಿ

API CLI ಬಳಸುವ ಅದೇ ಕೋರ್ ಅನುಷ್ಠಾನಕ್ಕೆ ನಿಯೋಜಿಸುತ್ತದೆ:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Focused project translation mixins for Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators under `co_op_translator.core`.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| Class | Module | Responsibility |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | ಪ್ರಾಜೆಕ್ಟ್-ಮಟ್ಟದ ಅನುವಾದ, ಡೈರೆಕ್ಟರಿ ನಿರ್ವಹಣೆ, ಪ್ರತಿ-ಭಾಷೆಯ ಮೆಟಾಡೇಟಾ ಸಾಮಾನ್ಯೀಕರಣ ಮತ್ತು Markdown, ನೋಟ್‌ಬುಕ್ ಮತ್ತು ಚಿತ್ರ ಅನುವಾದಕರಿಗೆ ನಿಯೋಜನೆಗಳನ್ನು ಸಂಯೋಜಿಸುತ್ತದೆ. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, ನೋಟ್‌ಬುಕ್‌ಗಳು, ಚಿತ್ರಗಳು, ಹಳೆಯತನ ಪತ್ತೆ ಮತ್ತು ಅನುವಾದ ಮೆಟಾಡೇಟಾ ನವೀಕರಣಗಳಿಗಾಗಿ ಅಸಿಂಕ್ರೋನಸ್ ಫೈಲ್ ಪ್ರೊಸೆಸಿಂಗ್ ಕೆಲಸಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown ಫೈಲ್ ಓದು, ವಿಷಯ ಅನುವಾದ, ಪಥ ಪುನರ್ಲೇಖನ, ಮೆಟಾಡೇಟಾ, ನಿರಾಕರಣೆಗಳು ಮತ್ತು ಬರವಣಿಗೆಗಳನ್ನು ಸಂಘಟಿಸುತ್ತದೆ. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | ನೋಟ್‌ಬುಕ್ ಫೈಲ್ ಓದು, Markdown-ಕೋಶಗಳ ಅನುವಾದ, ಪಥ ಪುನರ್ಲೇಖನ, ಮೆಟಾಡೇಟಾ, ನಿರಾಕರಣೆಗಳು ಮತ್ತು ಬರವಣಿಗೆಗಳನ್ನು ಸಂಘಟಿಸುತ್ತದೆ. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | ಮೂಲ ಚಿತ್ರ ಪತ್ತೆ, ಚಿತ್ರ ಅನುವಾದ, ಔಟ್‌ಪುಟ್ ಪಥಗಳು, ಮೆಟಾಡೇಟಾ ಮತ್ತು ಬರವಣಿಗೆಗಳನ್ನು ಸಂಘಟಿಸುತ್ತದೆ. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | ಅನುವಾದಿತ Markdown ಜೋಡಿಗಳನ್ನು ಕಂಡುಹಿಡಿಯುತ್ತದೆ, ಅನುವಾದ ಗುಣಮಟ್ಟವನ್ನು ಮೌಲ್ಯಮಾಪನಗೊಳಿಸುತ್ತದೆ, ಮತ್ತು ಕಡಿಮೆ ನಿರ್ಧಾರದ ನಂಬಿಕೆ ಮರುಕರಗೆ ಕಾರ್ಯಪ್ರವಾಹಗಳಿಗಾಗಿ ವಿಶ್ವಾಸ ಮೆಟಾಡೇಟಾವನ್ನು ಓದುತ್ತದೆ. |
| `ReviewRunner` | `co_op_translator.review.runner` | ಮೂಲ ಕಡತಗಳು, ಗುರಿ ಭಾಷೆಗಳು ಮತ್ತು ಸಂರಚಿಸಲಾದ ಅನುವಾದ ಮೂಲಗಳ ಮಧ್ಯೆ ನಿರ್ಧಾರಾತ್ಮಕ ವಿಮರ್ಶೆ ಪರಿಶೀಲನೆಗಳನ್ನು ಸಂಯೋಜಿಸುತ್ತದೆ. |
| `ReviewTarget` | `co_op_translator.review.targets` | ಮೂಲ ರುಟ್ ಮತ್ತು ಆ ರುಟ್‌ಗಾಗಿ ವಿಮರ್ಶೆಗೊಳಿಸಲಾದ ಅನುವಾದ ಔಟ್‌ಪುಟ್ ಡೈರೆಕ್ಟರಿಯನ್ನು ವಿವರಿಸುತ್ತದೆ. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | ಹಳೆಯ ಅಲಿಯಾಸ್ ಭಾಷಾ ಫೋಲ್ಡರ್‌ಗಳು ಪತ್ತೆಹಚ್ಚುತ್ತದೆ ಮತ್ತು ಮಾನಕ BCP 47 ಫೋಲ್ಡರ್ ಮಿಗ್ರೇಶನ್ ಯೋಜನೆಗಳನ್ನು ಪೂರ್ವತಯಾರಿಪಡಿಸುತ್ತದೆ. |
| `Config` | `co_op_translator.config.base_config` | `.env` ಫೈಲ್‌ಗಳನ್ನು ಲೋಡ್ ಮಾಡಿ ಅಗತ್ಯ LLM ಮತ್ತು ಐಚ್ಛಿಕ Vision ಒದಗಿಸುವವರು ಸಂರಚಿಸಲ್ಪಟ್ಟಿದೆಯೆ ಎಂದು ಪರಿಶೀಲಿಸುತ್ತದೆ. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI ಅಥವಾ OpenAI ಅನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪತ್ತೆಹಚ್ಚುತ್ತದೆ, ಅಗತ್ಯ ಪರಿಸರ ಚರಗಳನ್ನು ಮಾನ್ಯಗೊಳಿಸುತ್ತದೆ, ಮತ್ತು ಒದಗಿಸುವವರ ಸಂಪರ್ಕ ಪರಿಶೀಲನೆಗಳನ್ನು ನಡೆಸುತ್ತದೆ. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision ಸಂರಚನೆಯನ್ನು ಪತ್ತೆಹಚ್ಚುತ್ತದೆ ಮತ್ತು ಚಿತ್ರ ಅನುವಾದಕ್ಕಾಗಿ ಸಂಪರ್ಕ ಪರಿಶೀಲನೆಗಳನ್ನು ನಡೆಸುತ್ತದೆ. |