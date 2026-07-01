# Python API

ਸਥਿਰ ਸਰਜਨਹਾਰਕ Python API `co_op_translator.api` ਤੋਂ ਐਕਸਪੋਰਟ ਕੀਤਾ ਗਿਆ ਹੈ। ਜ਼ਿਆਦਾਤਰ ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਹੇਠਾਂ ਦਿੱਤੇ ਵਰਕਫਲੋਜ਼ ਵਿੱਚੋਂ ਇੱਕ ਵਰਤਦੇ ਹਨ:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | ਤੁਹਾਡੀ ਐਪਲੀਕੇਸ਼ਨ ਸੋర్స్ ਸਮੱਗਰੀ ਨੂੰ ਪੜ੍ਹਦੀ ਹੈ, ਅਨੁਵਾਦ ਲਈ Co-op Translator ਨੂੰ ਕਾਲ ਕਰਦੀ ਹੈ, ਅਤੇ ਨਤੀਜੇ ਨੂੰ ਕਿੱਥੇ ਸੇਵ ਕਰਨਾ ਹੈ ਫੈਸਲਾ ਕਰਦੀ ਹੈ। | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | ਤੁਹਾਡੇ MCP ਹੋਸਟ ਜਾਂ ਐਪਲੀਕੇਸ਼ਨ ਮਾਡਲ ਟੁਕੜਿਆਂ ਦਾ ਅਨੁਵਾਦ ਕਰੇਗਾ, ਜਦਕਿ Co-op Translator chunking ਅਤੇ reconstruction ਨੂੰ ਸੰਭਾਲੇਗਾ। | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ ਕਿ Python API CLI ਵਾਂਗ ਵਰਤਿਆ ਜਾਵੇ ਅਤੇ ਖੋਜ, ਆਉਟਪੁੱਟ ਪાથ, ਮੈਟਾਡੇਟਾ, ਸਫਾਈ ਅਤੇ ਲਿਖਾਈਆਂ ਸੰਭਾਲੇ। | `run_translation` |

ਜ਼ਿਆਦਾਤਰ ਨੀਵੀਂ-ਸਤਹ ਮੋਡੀਊਲ `core`, `config`, `review`, ਅਤੇ `utils` ਹੇਠਾਂ ਇਹਨਾਂ API ਐਂਟਰੀ ਪੁਆਇੰਟਸ ਵੱਲੋਂ ਵਰਤੇ ਜਾਣ ਵਾਲੇ ਇੰਪਲੀਮੇੰਟੇਸ਼ਨ ਵੇਰਵੇ ਹਨ।

MCP ਕਲਾਇਂਟ ਉਹੀ ਪਬਲਿਕ API [MCP Server](mcp.md) ਰਾਹੀਂ ਵਰਤਦੇ ਹਨ। ਜੇ ਤੁਸੀਂ Python ਸਿੱਧਾ ਕਾਲ ਕਰ ਰਹੇ ਹੋ ਤਾਂ ਇਸ ਪੰਨੇ ਨੂੰ ਵਰਤੋਂ, ਅਤੇ ਜੇ Co-op Translator ਨੂੰ ਕਿਸੇ ਏਜੰਟ ਜਾਂ ਐਡੀਟਰ ਨੂੰ ਐਕਸਪੋਜ਼ ਕਰ ਰਹੇ ਹੋ ਤਾਂ MCP ਗਾਈਡ ਵੇਖੋ। ਜੇ ਤੁਸੀਂ CLI, Python API, ਅਤੇ MCP ਵਿੱਚ ਫੈਸਲਾ ਕਰ ਰਹੇ ਹੋ ਤਾਂ [Choose Your Workflow](workflows.md) ਤੋਂ ਸ਼ੁਰੂ ਕਰੋ।

## First-Time API Flow

ਜੇ ਤੁਸੀਂ Python ਕੋਡ ਤੋਂ Co-op Translator ਕਾਲ ਕਰ ਰਹੇ ਹੋ ਤਾਂ ਇੱਥੋਂ ਸ਼ੁਰੂ ਕਰੋ:

1. [Configuration](configuration.md) ਵਿੱਚ ਵਰਣਿਤ ਤੌਰ 'ਤੇ ਇੱਕ LLM ਪ੍ਰਦਾਤਾ ਸੰਰਚਿਤ ਕਰੋ, ਸਿਵਾਏ ਜੇ ਤੁਸੀਂ ਸਿਰਫ Markdown ਜਾਂ ਨੋਟਬੁੱਕ chunk ਹੋਸਟ-ਏਜੰਟ ਅਨੁਵਾਦ ਲਈ ਤਿਆਰ ਕਰ ਰਹੇ ਹੋ।
2. ਫੈਸਲਾ ਕਰੋ ਕਿ ਕੀ ਤੁਹਾਡੀ ਐਪਲੀਕੇਸ਼ਨ ਫਾਇਲ I/O ਦੀ ਮਾਲਕੀ ਕਰਦੀ ਹੈ।
3. ਜਦੋਂ ਤੁਹਾਡੀ ਐਪਲੀਕੇਸ਼ਨ ਵਿਅਕਤੀਗਤ ਫਾਇਲਾਂ ਨੂੰ ਪੜ੍ਹਦੀ ਅਤੇ ਲਿਖਦੀ ਹੈ ਤਾਂ content APIs ਵਰਤੋਂ।
4. ਜਦੋਂ Co-op Translator ਨੂੰ CLI ਵਾਂਗ ਰਿਪੋਜ਼ਿਟਰੀ ਪ੍ਰੋਸੈਸ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ ਤਾਂ `run_translation` ਵਰਤੋਂ।
5. ਜੇ ਤੁਹਾਨੂੰ ਆਟੋਮੇਸ਼ਨ ਵਿੱਚ ਨਿਰਧਾਰਿਤ ਚੈੱਕਾਂ ਦੀ ਲੋੜ ਹੈ ਤਾਂ ਅਨੁਵਾਦ ਦੇ ਬਾਅਦ `run_review` ਵਰਤੋਂ।

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

ਇਹ ਵਰਕਫਲੋ ਉਸ ਵੇਲੇ ਵਰਤੋ ਜਦੋਂ ਤੁਹਾਡੇ ਕੋਲ ਪਹਿਲਾਂ ਹੀ ਇੱਕ ਫਾਇਲ, ਐਡੀਟਰ ਬਫਰ, ਨੋਟਬੁੱਕ ਪੇਲੋਡ, MCP ਰਿਕਵੇਸਟ, ਜਾਂ ਕਸਟਮ ਪਾਈਪਲਾਈਨ ਇਨਪੁੱਟ ਹੋਵੇ। ਤੁਹਾਡਾ ਕੋਡ ਫਾਇਲ I/O ਦੀ ਮਾਲਕੀ ਕਰਦਾ ਹੈ:

1. ਸੋర్స్ ਸਮੱਗਰੀ ਪੜ੍ਹੋ।
2. ਇੱਕ content translation API ਕਾਲ ਕਰੋ।
3. ਜੇ ਅਨੁਵਾਦ ਕੀਤਾ ਸਮੱਗਰੀ ਪ੍ਰਾਜੈਕਟ ਅਨੁਵਾਦ ਫੋਲਡਰ ਵਿੱਚ ਲਿਖੀ ਜਾਵੇਗੀ ਤਾਂ ਵਿਕਲਪਕ ਤੌਰ ਤੇ path rewriting API ਕਾਲ ਕਰੋ।
4. ਨਤੀਜਾ ਆਪਣੇ ਐਪਲੀਕੇਸ਼ਨ ਤੋਂ ਸੇਵ ਜਾਂ ਰਿਟਰਨ ਕਰੋ।

content translation APIs ਪ੍ਰੋਜੈਕਟ ਖੋਜ ਨਹੀਂ ਚਲਾਉਂਦੇ, ਮੈਟਾਡੇਟਾ ਨਹੀਂ ਲਿਖਦੇ, ਡਿਸਕਲੇਮਰ ਨਹੀਂ ਜੋੜਦੇ, ਅਤੇ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਲਿੰਕ ਨਹੀਂ ਰੀ-ਰਾਈਟ ਕਰਦੇ।

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

ਜੇ ਅਨੁਵਾਦ ਕੀਤੀ Markdown Co-op Translator ਪ੍ਰੋਜੈਕਟ ਲੇਆਉਟ ਵਿੱਚ ਨਹੀਂ ਰਹੇਗੀ, ਤਾਂ `rewrite_markdown_paths` ਨੂੰ ਸਕਿਪ ਕਰੋ ਅਤੇ ਅਨੁਵਾਦਿਤ ਸਟਰਿੰਗ ਨੂੰ ਸਿੱਧਾ ਸੇਵ ਕਰੋ।

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

`translate_notebook_content` Markdown ਸੈੱਲਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ ਅਤੇ non-Markdown ਸੈੱਲਾਂ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖਦਾ ਹੈ। ਪਾਥ ਰੀਰਾਈਟਿੰਗ ਸਿਰਫ Markdown ਸੈੱਲਾਂ 'ਤੇ ਲਾਗੂ ਹੁੰਦੀ ਹੈ।

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

`translate_image_content` ਸੋర్స్ ਇਮੇਜ ਨੂੰ ਪੜ੍ਹਦਾ ਹੈ ਅਤੇ ਇੱਕ rendered `PIL.Image.Image` ਰਿਟਰਨ ਕਰਦਾ ਹੈ। ਇਹ ਅਨੁਵਾਦਿਤ ਇਮੇਜ ਮੈਟਾਡੇਟਾ ਨਹੀਂ ਲਿਖਦਾ।

## Scenario 2: Translate an Entire Repository

ਇਹ ਵਰਕਫਲੋ ਉਸ ਵੇਲੇ ਵਰਤੋ ਜਦੋਂ ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ ਕਿ Python API `translate` CLI ਵਾਂਗ ਵਿਹਾਰ ਕਰੇ। `run_translation` ਸਹਾਇਕ ਫਾਇਲਾਂ ਦੀ ਖੋਜ ਕਰਦਾ ਹੈ, ਚੁਣੇ ਹੋਏ ਸਮੱਗਰੀ ਟਾਈਪਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ, ਪਾਥ ਰੀਰਾਈਟ ਕਰਦਾ ਹੈ, ਆਉਟਪੁੱਟ ਫਾਇਲਾਂ ਲਿਖਦਾ ਹੈ, ਮੈਟਾਡੇਟਾ ਅੱਪਡੇਟ ਕਰਦਾ ਹੈ, ਅਤੇ ਸਫਾਈ ਵਰਗੀਆਂ ਅਨੁਵਾਦ ਰਖ-ਰਖਾਵਕ ਕਾਰਵਾਈਆਂ ਕਰਦਾ ਹੈ।

`run_translation` ਪ੍ਰੋਜੈਕਟ ਓਰਕੇਸਟਰੇਸ਼ਨ ਲਈ ਪਸੰਦੀਦਾ ਐਂਟਰੀ ਪੁਆਇੰਟ ਹੈ। `translate_project` ਇਕ compatibility alias ਵਜੋਂ ਨਿਕਾਸ ਕੀਤਾ ਗਿਆ ਹੈ ਜਿਸਦਾ ਵਿਹਾਰ ਉਸੇ ਤਰ੍ਹਾਂ ਹੈ।

ਮੌਜੂਦਾ ਰਿਪੋਜ਼ਿਟਰੀ ਵਿੱਚ Markdown ਫਾਇਲਾਂ ਨੂੰ Korean ਅਤੇ Japanese ਵਿੱਚ ਅਨੁਵਾਦ ਕਰੋ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

ਕਿਸੇ ਨਿਰਧਾਰਤ ਪ੍ਰੋਜੈਕਟ ਰੂਟ ਤੋਂ ਸਿਰਫ ਨੋਟਬੁੱਕ ਅਨੁਵਾਦ ਕਰੋ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

ਫਾਇਲਾਂ ਨੂੰ ਲਿਖੇ ਬਿਨਾਂ ਅਨੁਵਾਦ ਦੀ ਮਾਤਰਾ ਪ੍ਰੀਵਿュー ਕਰੋ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

ਇੱਕ ਕਾਲ ਵਿੱਚ ਬਹੁਤ ਸਾਰੇ content roots ਦਾ ਅਨੁਵਾਦ ਕਰੋ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

ਅਨੁਵਾਦਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ ਆਉਟਪੁੱਟ ਗਰੁੱਪਾਂ ਵਿੱਚ ਲਿਖੋ:

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

ਜਦੋਂ ਹਰ ਭਾਸ਼ਾ ਵਿੱਚ nested subdirectory ਹੋਵੇ ਤਾਂ ਪ੍ਰਤੀ-ਭਾਸ਼ਾ placeholder ਵਰਤੋ:

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

ਜੇ `markdown`, `notebook`, ਜਾਂ `images` 'ਚੋਂ ਕੋਈ ਵੀ ਸੈਟ ਨਹੀਂ ਹੈ, ਤਾਂ API ਸਾਰੇ ਸਪੋਰਟਡ ਟਾਈਪਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ: Markdown, notebooks, ਅਤੇ images।

## Review Translated Output

`run_review` ਨਿਰਧਾਰਿਤ ਅਨੁਵਾਦ ਚੈੱਕ ਚਲਾਉਂਦਾ ਹੈ ਬਿਨਾਂ LLM ਜਾਂ Vision ਕ੍ਰੇਡੈਂਸ਼ਲਾਂ ਦੇ।

!!! note "ਬੀਟਾ"
    `run_review` ਇੱਕ ਬੀਟਾ ਨਿਰਧਾਰਿਤ ਰਿਵਿਊ API ਹੈ। ਇਹ ਮਾਡਲ ਪ੍ਰਦਾਤਾਵਾਂ ਨੂੰ ਕਾਲ ਨਹੀਂ ਕਰਦਾ ਅਤੇ ਫਾਇਲਾਂ ਨਹੀਂ ਲਿਖਦਾ, ਪਰ ਚੈੱਕ ਅਤੇ ਇਸ਼ੂ ਸਕੀਮਾਂ ਵਿਕਸਤ ਹੋ ਸਕਦੀਆਂ ਹਨ।

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

ਸਿਰਫ ਉਹ ਫਾਇਲਾਂ ਰਿਵਿਊ ਕਰੋ ਜੋ base ref ਦੇ ਖਿਲਾਫ਼ ਬਦਲੀ ਗਈਆਂ ਹਨ ਅਤੇ GitHub-ਸ਼ੈਲੀ ਵਾਲਾ ਆਉਟਪੁੱਟ ਪ੍ਰਿੰਟ ਕਰੋ:

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

ਫਾਇਲ ਲਿਖੇ ਬਿਨਾਂ Markdown ਸਮੱਗਰੀ ਦਾ ਅਨੁਵਾਦ ਕਰੋ:

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

Markdown ਲਿੰਕਾਂ ਦਾ ਅਨੁਵਾਦ ਅਤੇ ਰੀਰਾਈਟ ਕਰੋ:

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

Python ਤੋਂ ਇੱਕ ਰਿਪੋਜ਼ਿਟਰੀ ਅਨੁਵਾਦ ਕਰੋ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

ਕਈ ਰੂਟਸ ਅਨੁਵਾਦ ਕਰੋ:

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

Glossary terms ਨੂੰ ਬਰਕਰਾਰ ਰੱਖੋ:

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

Content translation APIs ਉਹ ਇੰਟਿਗ੍ਰੇਸ਼ਨਾਂ ਲਈ ਹਨ ਜਿਨ੍ਹਾਂ ਕੋਲ ਪਹਿਲਾਂ ਹੀ ਸਮੱਗਰੀ memory ਵਿੱਚ ਹੁੰਦੀ ਹੈ, ਜਿਵੇਂ ਕਿ ਇੱਕ ਐਡੀਟਰ ਐਕਸਟੇੰਸ਼ਨ, MCP ਟੂਲ, ਨੋਟਬੁੱਕ ਪ੍ਰੋਸੈਸਰ, ਜਾਂ ਕਸਟਮ ਪਾਈਪਲਾਈਨ।

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. ਸਿਰਫ Markdown ਸਮੱਗਰੀ ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ। ਇਹ ਲਿੰਕਾਂ ਨੂੰ ਰੀਰਾਈਟ ਨਹੀਂ ਕਰਦਾ, ਮੈਟਾਡੇਟਾ ਨਹੀਂ ਲਿਖਦਾ, ਜਾਂ ਡਿਸਕਲੇਮਰ ਨਹੀਂ ਜੋੜਦਾ। |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Markdown ਸੈੱਲਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ ਅਤੇ non-Markdown ਸੈੱਲਾਂ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖਦਾ ਹੈ। ਇਹ ਲਿੰਕਾਂ ਨੂੰ ਰੀਰਾਈਟ ਨਹੀਂ ਕਰਦਾ, ਮੈਟਾਡੇਟਾ ਨਹੀਂ ਲਿਖਦਾ, ਜਾਂ ਡਿਸਕਲੇਮਰ ਨਹੀਂ ਜੋੜਦਾ। |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. ਇਮੇਜ ਤੋਂ ਟੈਕਸਟ ਨੂੰ ਨਿਕਾਲਦਾ ਅਤੇ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ, ਫਿਰ ਇੱਕ ਰੇਂਡਰ ਕੀਤਾ ਇਮੇਜ ਵਾਪਸ ਕਰਦਾ ਹੈ। ਇਹ ਅਨੁਵਾਦਿਤ ਇਮੇਜ ਮੈਟਾਡੇਟਾ ਸੇਵ ਨਹੀਂ ਕਰਦਾ। |

`translate_markdown_content` ਅਤੇ `translate_notebook_content` ਵਿਕਲਪਾਂ ਰਾਹੀਂ ਇੱਕ ਵਿਕਲਪਿਕ `source_path` ਨੂੰ ਸਵੀਕਾਰਦੇ ਹਨ। ਪਾਥ ਅਨੁਵਾਦਕ ਨੂੰ ਸੰਦਰਭ ਵਜੋਂ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ; ਕਾਲਰਾਂ ਨੂੰ ਅਨੁਵਾਦ ਦੇ ਬਾਅਦ ਕਿਸੇ ਵੀ ਪ੍ਰੋਜੈਕਟ-ਨਿਰਧਾਰਤ ਪਾਥ ਰੀਰਾਈਟਿੰਗ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਰਹਿਣਾ ਪੈਂਦਾ ਹੈ।

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

ਉਹੀ ਵਿਕਲਪ ਡਿਕਸ਼ਨਰੀਜ਼ ਵਜੋਂ ਵੀ ਪਾਸ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

Agent-assisted APIs Co-op Translator ਤੋਂ Azure OpenAI ਜਾਂ OpenAI ਨੂੰ ਕਾਲ ਨਹੀਂ ਕਰਦੇ। ਇਹ Markdown ਜਾਂ ਨੋਟਬੁੱਕ chunk ਹੋਸਟ-ਏਜੰਟ ਲਈ ਤਿਆਰ ਕਰਦੇ ਹਨ, ਫਿਰ ਹੋਸਟ-ਏਜੰਟ ਦੁਆਰਾ ਅਨੁਵਾਦ ਕੀਤੇ ਚੰਕਾਂ ਤੋਂ ਅੰਤਿਮ ਸਮੱਗਰੀ ਨੂੰ ਦੁਬਾਰਾ ਬਣਾਉਂਦੇ ਹਨ।

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | chunks, prompts, ਅਤੇ reconstruction state ਨਾਲ ਇੱਕ self-contained Markdown ਜਾਬ ਵਾਪਸ ਕਰੋ। |
| `finish_markdown_agent_translation` | ਇੱਕ ਜਾਬ ਅਤੇ ਹੋਸਟ-ਏਜੰਟ ਦੁਆਰਾ ਅਨੁਵਾਦ ਕੀਤੇ ਚੰਕਾਂ ਤੋਂ Markdown ਨੂੰ ਦੁਬਾਰਾ ਬਣਾਓ। |
| `start_notebook_agent_translation` | ਹੋਸਟ-ਏਜੰਟ ਅਨੁਵਾਦ ਲਈ Markdown-cell chunks ਵਾਲਾ ਇੱਕ ਨੋਟਬੁੱਕ ਜਾਬ ਵਾਪਸ ਕਰੋ। |
| `finish_notebook_agent_translation` | ਕੋਡ ਸੈੱਲ, ਆਉਟਪੁੱਟ, ਅਤੇ ਮੈਟਾਡੇਟਾ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖਦਿਆਂ ਨੋਟਬੁੱਕ JSON ਨੂੰ ਦੁਬਾਰਾ ਬਣਾਓ। |

ਇਹ ਵਰਕਫਲੋ ਮੁੱਖ ਤੌਰ 'ਤੇ MCP ਹੋਸਟਾਂ ਲਈ ਇਰਾਦਾ ਹੈ। ਜੇ ਤੁਹਾਨੂੰ ਪ੍ਰੋਡਕਸ਼ਨ ਰਿਪੋਜ਼ਿਟਰੀ ਅਨੁਵਾਦ ਚਾਹੀਦਾ ਹੈ ਜਿਸ ਵਿੱਚ Co-op Translator ਪ੍ਰਦਾਤਾ ਕਾਲਾਂ ਦਾ ਪ੍ਰਬੰਧ ਕਰੇ, ਤਾਂ `translate_markdown_content`, `translate_notebook_content`, ਜਾਂ `run_translation` ਵਰਤੋਂ।

## Path Rewriting APIs

Path rewriting APIs ਕੋਈ ਅਨੁਵਾਦ ਨਹੀਂ ਕਰਦੀਆਂ। ਉਹ ਕਾਲਰਾਂ ਨੂੰ ਸੋర్స్ ਪਾਥ, ਅਨੁਵਾਦਿਤ ਟਾਰਗੇਟ ਪਾਥ, ਅਤੇ ਪ੍ਰੋਜੈਕਟ ਲੇਆਉਟ ਦੇ ਪਤਾ ਹੋਣ ਤੋਂ ਬਾਅਦ ਲਿੰਕਾਂ ਅਤੇ frontmatter ਪਾਥਾਂ ਨੂੰ ਅਪਡੇਟ ਕਰਦੀਆਂ ਹਨ।

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | ਅਨੁਵਾਦਿਤ ਟਾਰਗੇਟ ਲਈ Markdown ਲਿੰਕਾਂ ਅਤੇ ਸਹਾਇਕ frontmatter ਪਾਥ ਫੀਲਡਾਂ ਨੂੰ ਰੀਰਾਈਟ ਕਰਦਾ ਹੈ। |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | ਹਰ Markdown ਸੈੱਲ ਤੇ Markdown ਪਾਥ ਰੀਰਾਈਟਿੰਗ ਲਾਗੂ ਕਰਦਾ ਹੈ ਅਤੇ non-Markdown ਸੈੱਲਾਂ ਨੂੰ ਬਦਲਦਾ ਨਹੀਂ। |

`policy` ਆਰਗੁਮੈਂਟ ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਹੋ ਸਕਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਇਹ ਫੀਲਡਜ਼ ਹਨ:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | ਟਾਰਗੇਟ ਭਾਸ਼ਾ ਕੋਡ, ਉਦਾਹਰਨ ਲਈ `"ko"` ਜਾਂ `"pt-BR"`। |
| `root_dir` | No | ਸੋర్స్ ਪ੍ਰੋਜੈਕਟ ਰੂਟ। ਡਿਫਾਲਟ `"."` ਹੈ। |
| `translations_dir` | No | ਟੈਕਸਟ ਅਨੁਵਾਦ ਆਉਟਪੁੱਟ ਡਾਇਰੈਕਟਰੀ। ਡਿਫਾਲਟ `root_dir` ਥੱਲੇ `translations` ਹੈ। |
| `translated_images_dir` | No | ਅਨੁਵਾਦਿਤ ਇਮੇਜ ਆਉਟਪੁੱਟ ਡਾਇਰੈਕਟਰੀ। ਡਿਫਾਲਟ `root_dir` ਥੱਲੇ `translated_images` ਹੈ। |
| `translation_types` | No | ਸਰਗਰਮ ਅਨੁਵਾਦ ਟਾਈਪ। ਡਿਫਾਲਟ Markdown, notebooks, ਅਤੇ images ਹੈ। |
| `lang_subdir` | No | ਹਰ ਭਾਸ਼ਾ ਫੋਲਡਰ ਹੇਠਾਂ ਇੱਕ ਵਿਕਲਪਿਕ ਸਬਡਾਇਰੈਕਟਰੀ। |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | ਖਾਲੀ-ਸਪੇਸ ਨਾਲ ਵੱਖ ਕੀਤੇ ਹੋਏ ਟਾਰਗੇਟ ਭਾਸ਼ਾ ਕੋਡ, ਉਦਾਹਰਨ ਲਈ `"ko ja fr"` ਜਾਂ `"all"`। ਅਲਿਆਸ ਕੋਡਾਂ ਨੂੰ canonical BCP 47 ਮੁੱਲਾਂ ਵਿੱਚ ਨਾਰਮਲਾਈਜ਼ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। |
| `root_dir` | `str` | `"."` | ਇੱਕ ਸਿੰਗਲ ਅਨੁਵਾਦ ਟਾਰਗੇਟ ਲਈ ਪ੍ਰੋਜੈਕਟ ਰੂਟ। `root_dirs` ਜਾਂ `groups` ਦਿੱਤੇ ਜਾਣ 'ਤੇ ਨਜ਼ਰਅੰਦਾਜ਼ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। |
| `update` | `bool` | `False` | ਚੁਣੀਆਂ ਭਾਸ਼ਾਵਾਂ ਲਈ ਮੌਜੂਦਾ ਅਨੁਵਾਦਾਂ ਨੂੰ ਮਿਟਾ ਕੇ ਦੁਬਾਰਾ ਬਣਾਓ। |
| `images` | `bool` | `False` | ਇਮੇਜ ਅਨੁਵਾਦ ਸ਼ਾਮਲ ਕਰੋ। Azure AI Vision ਸੰਰਚਨਾ ਲੋੜੀਦੀ ਹੈ। |
| `markdown` | `bool` | `False` | Markdown ਅਨੁਵਾਦ ਸ਼ਾਮਲ ਕਰੋ। |
| `notebook` | `bool` | `False` | Jupyter notebook ਅਨੁਵਾਦ ਸ਼ਾਮਲ ਕਰੋ। |
| `debug` | `bool` | `False` | ਡੀਬੱਗ ਲੌਗਿੰਗ ਸਖ਼ਤੀ ਕਰੋ। |
| `save_logs` | `bool` | `False` | ਰੂਟ `logs/` ਡਾਇਰੈਕਟਰੀ ਹੇਠਾਂ DEBUG-ਲੈਵਲ ਲੌਗ ਫਾਇਲਾਂ ਸੇਵ ਕਰੋ। |
| `yes` | `bool` | `True` | ਪ੍ਰੋਗਰਾਮੈਟਿਕ ਅਤੇ CI ਉਪਯੋਗ ਲਈ ਪ੍ਰਾਪਟ ਪੂਸ਼ਟੀ ਆਟੋ-ਕਨਫਰਮ ਕਰੋ। |
| `add_disclaimer` | `bool` | `False` | ਅਨੁਵਾਦਿਤ Markdown ਅਤੇ notebooks ਵਿੱਚ ਮਸ਼ੀਨ ਅਨੁਵਾਦ ਡਿਸਕਲੇਮਰ ਜੋੜੋ। |
| `translations_dir` | `str \| None` | `None` | ਕਸਟਮ ਟੈਕਸਟ ਅਨੁਵਾਦ ਆਉਟਪੁੱਟ ਡਾਇਰੈਕਟਰੀ। ਰਿਲਟਿਵ ਪਾਥ ਹਰ ਰੂਟ ਦੇ ਖਿਲਾਫ਼ ਸੁਲਝਾਏ ਜਾਂਦੇ ਹਨ। |
| `image_dir` | `str \| None` | `None` | ਕਸਟਮ ਅਨੁਵਾਦਿਤ ਇਮੇਜ ਆਉਟਪੁੱਟ ਡਾਇਰੈਕਟਰੀ। ਰਿਲਟਿਵ ਪਾਥ ਹਰ ਰੂਟ ਦੇ ਖਿਲਾਫ਼ ਸੁਲਝਾਏ ਜਾਂਦੇ ਹਨ। |
| `root_dirs` | `Iterable[str] \| None` | `None` | ਇਕੋ ਆਉਟਪੁੱਟ ਸੈਟਿੰਗਾਂ ਵਾਲੇ ਬਹੁਤ ਸਾਰੇ ਰੂਟ। |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | ਵਿਸ਼ੇਸ਼ `(root_dir, translations_dir)` ਜੋੜੇ। `root_dirs` ਤੋਂ ਪਹਿਲਤਾ ਰੋਪਿਆ ਜਾਂਦਾ ਹੈ। |
| `repo_url` | `str \| None` | `None` | README ਭਾਸ਼ਾ ਟੇਬਲ ਮਾਰਗਦਰਸ਼ਨ ਰੈਂਡਰ ਕਰਨ ਵੇਲੇ ਵਰਤਿਆ ਜਾਣ ਵਾਲਾ ਰਿਪੋ URL। |
| `glossaries` | `Iterable[str] \| None` | `None` | ਅਨੁਵਾਦ ਦੌਰਾਨ ਬਰਕਰਾਰ ਰੱਖਣ ਲਈ glossary ਸ਼ਬਦ। duplicates ਅਤੇ ਖਾਲੀ ਸ਼ਬਦ ਨਾਰਮਲਾਈਜ਼ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। |
| `dry_run` | `bool` | `False` | ਫਾਇਲਾਂ ਲਿਖੇ ਬਿਨਾਂ ਅਨੁਵਾਦ ਮਾਤਰਾ ਦਾ ਅਨੁਮਾਨ ਲਗਾਓ ਅਤੇ ਮਾਈਗ੍ਰੇਸ਼ਨ ਵਿਵਹਾਰ ਪ੍ਰੀਵਿュー ਕਰੋ। |

## Review Parameters

`run_review` ਜਾਣ ਬੁਝ ਕੇ `run_translation` ਦੇ ਸਿਗਨੇਚਰ ਨੂੰ ਸੰਭਵ ਹੱਦ ਤੱਕ ਮਿਰਰ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ ਆਟੋਮੇਸ਼ਨ ਅਨੁਵਾਦ ਅਤੇ ਰਿਵਿਊ ਵਰਕਫਲੋਜ਼ ਵਿਚ ਘੱਟ branching ਨਾਲ ਸਵਿੱਚ ਕਰ ਸਕੇ।

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | ਰਿਵਿਊ ਕਰਨ ਲਈ ਟਾਰਗੇਟ ਭਾਸ਼ਾ ਫੋਲਡਰ। ਖਾਲੀ-ਸਪੇਸ ਵਾਲੇ ਸਟਰਿੰਗ ਅਤੇ Iterable ਦੋਹਾਂ ਮਨਜ਼ੂਰ ਹਨ। `"all"` ਹਰ ਖੋਜ ਕੀਤੀ ਅਨੁਵਾਦ ਭਾਸ਼ਾ ਨੂੰ ਰਿਵਿਊ ਕਰਦਾ ਹੈ। |
| `root_dir` | `str` | `"."` | ਇੱਕ ਸਿੰਗਲ ਰਿਵਿਊ ਟਾਰਗੇਟ ਲਈ ਪ੍ਰੋਜੈਕਟ ਰੂਟ। `root_dirs` ਜਾਂ `groups` ਦਿੱਤੇ ਜਾਣ 'ਤੇ ਨਜ਼ਰਅੰਦਾਜ਼ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। |
| `markdown` | `bool` | `False` | Markdown ਅਤੇ MDX ਸੋਰਸ ਫਾਇਲਾਂ ਸ਼ਾਮਲ ਕਰੋ। |
| `notebook` | `bool` | `False` | Jupyter notebook ਸੋਰਸ ਫਾਇਲਾਂ ਸ਼ਾਮਲ ਕਰੋ। |
| `images` | `bool` | `False` | ਅਨੁਵਾਦ ਵਿਕਲਪਾਂ ਨਾਲ ਪੈਰਿਟੀ ਲਈ ਰਿਜ਼ਰਵ ਕੀਤਾ ਗਿਆ। Markdown ਤੋਂ ਇਮੇਜ ਰੈਫਰਨਸ ਦੀ ਜਾਂਚ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। |
| `translations_dir` | `str \| None` | `None` | ਕਸਟਮ ਟੈਕਸਟ ਅਨੁਵਾਦ ਆਉਟਪੁੱਟ ਡਾਇਰੈਕਟਰੀ। Relative paths resolve against each root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Multiple roots that share the same output settings. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit `(root_dir, translations_dir)` pairs. Takes precedence over `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref used to limit review to changed source files. |
| `output_format` | `str` | `"text"` | Review output format. Supported values are `"text"` and `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Treat warnings as failures in addition to errors. |
| `debug` | `bool` | `False` | Enable debug logging. |
| `save_logs` | `bool` | `False` | Save DEBUG-level log files under the root `logs/` directory. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Configuration Requirements

ਪਰੋਵਾਈਡਰ-ਸਹਾਇਤ ਅਨੁਵਾਦ API-ਾਂ ਨੂੰ ਅਨੁਵਾਦ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਪਰੋਵਾਈਡਰ ਕਨਫਿਗਰੇਸ਼ਨ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ:

- Markdown ਅਤੇ ਨੋਟਬੁੱਕ ਅਨੁਵਾਦ ਲਈ ਇੱਕ LLM ਪ੍ਰੋਵਾਈਡਰ ਲੋੜੀਂਦਾ ਹੈ। Azure OpenAI ਜਾਂ OpenAI ਵਿੱਚੋਂ ਕਿਸੇ ਇੱਕ ਨੂੰ ਕਨਫਿਗਰ ਕਰੋ।
- ਇਮੇਜ ਅਨੁਵਾਦ ਲਈ LLM ਪ੍ਰੋਵਾਈਡਰ ਦੇ ਇਲਾਵਾ Azure AI Vision ਦੀ ਵੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।
- `run_translation` ਪ੍ਰਾਜੈਕਟ ਅਨੁਵਾਦ ਸ਼ੁਰੂ ਹੋਣ ਤੋਂ ਪਹਿਲਾਂ ਹਲਕੀ ਸੰਪਰਕ ਜਾਂਚਾਂ ਚਲਾਂਦਾ ਹੈ।
- Agent-assisted `start_*_agent_translation` and `finish_*_agent_translation` APIs Co-op Translator LLM providers ਨੂੰ ਕਾਲ ਨਹੀਂ ਕਰਦੀਆਂ। ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨ ਜਾਂ MCP ਏਜੰਟ ਤਿਆਰ ਕੀਤੀਆਂ ਹਿੱਸਿਆਂ ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ।
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, and `run_review` ਨਿਰਧਾਰਤ ਹਨ ਅਤੇ ਪ੍ਰੋਵਾਈਡਰ ਪ੍ਰਮਾਣਿਕਤਾ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ।

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

`run_review` is deterministic and does not require Azure OpenAI, OpenAI, or Azure AI Vision configuration.

## Behavior Notes

- Content translation APIs keep translation separate from project path rewriting. Call `rewrite_markdown_paths` or `rewrite_notebook_paths` explicitly when translated content needs project-relative links adjusted for a target location.
- Project orchestration APIs add project behavior around content translation, including file discovery, writes, path rewriting, metadata, cleanup, and optional disclaimers.
- `run_translation` prints progress and estimate summaries through Click, matching the CLI user experience.
- `dry_run=True` computes estimates using virtual README updates, but does not write the README or translation files.
- `groups` are processed sequentially. A single aggregate estimate is printed before work begins.
- When image translation is selected, missing Vision configuration raises an error before translation starts.
- Existing alias-based language folders are detected and can be migrated to canonical language folder names as part of the run.
- `run_review` fails on missing translated files, missing or stale translation metadata, malformed Markdown frontmatter/code fences, and invalid translated notebook JSON.
- `run_review` reports missing local Markdown and image link targets as warnings by default.

## Internal Call Path

The API delegates to the same core implementation used by the CLI:

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

| ਕਲਾਸ | ਮੋਡੀਊਲ | ਜਿੰਮੇਵਾਰੀ |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | ਪਰਾਜੈਕਟ-ਸਤਰੀਅ ਅਨੁਵਾਦ, ਡਾਇਰੈਕਟਰੀ ਪ੍ਰਬੰਧਨ, ਪ੍ਰਤੀ-ਭਾਸ਼ਾ ਮੈਟਾਡੇਟਾ ਨਾਰਮਲਾਈਜ਼ੇਸ਼ਨ, ਅਤੇ Markdown, ਨੋਟਬੁੱਕ, ਅਤੇ ਇਮੇਜ ਟਰਾਂਸਲੇਟਰਾਂ ਨੂੰ ਡੈਲੀਗੇਟ ਕਰਨ ਲਈ ਕੋਆਰਡੀਨੇਟ ਕਰਦਾ ਹੈ। |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, ਨੋਟਬੁੱਕ, ਇਮੇਜ, stale ਪਤਾ ਲਗਾਉਣਾ, ਅਤੇ ਅਨੁਵਾਦ ਮੈਟਾਡੇਟਾ ਅੱਪਡੇਟਸ ਲਈ ਅਸਿੰਕ ਫਾਇਲ ਪ੍ਰੋਸੈਸਿੰਗ ਕੰਮ ਨੂੰ ਅੰਜਾਮ ਦਿੰਦਾ ਹੈ। |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown ਫਾਈਲ ਪੜ੍ਹਾਈ, ਸਮੱਗਰੀ ਅਨੁਵਾਦ, ਪਾਥ ਰੀਰਾਈਟਿੰਗ, ਮੈਟਾਡੇਟਾ, ਡਿਸਕਲੇਮਰ, ਅਤੇ ਲਿਖਤਾਂ ਦੀ ਯੋਜਨਾ ਬਣਾਉਂਦਾ ਹੈ। |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | ਨੋਟਬੁੱਕ ਫਾਈਲ ਪੜ੍ਹਾਈ, Markdown-ਸੈੱਲ ਅਨੁਵਾਦ, ਪਾਥ ਰੀਰਾਈਟਿੰਗ, ਮੈਟਾਡੇਟਾ, ਡਿਸਕਲੇਮਰ, ਅਤੇ ਲਿਖਤਾਂ ਦੀ ਯੋਜਨਾ ਬਣਾਉਂਦਾ ਹੈ। |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | ਸਰੋਤ ਇਮੇਜ ਖੋਜ, ਇਮੇਜ ਅਨੁਵਾਦ, ਆਉਟਪੁੱਟ ਪਾਥ, ਮੈਟਾਡੇਟਾ, ਅਤੇ ਲਿਖਤਾਂ ਦੀ ਯੋਜਨਾ ਬਣਾਉਂਦਾ ਹੈ। |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | ਅਨੁਵਾਦਿਤ Markdown ਜੋੜਿਆਂ ਨੂੰ ਲੱਭਦਾ ਹੈ, ਅਨੁਵਾਦ ਗੁਣਵੱਤਾ ਦਾ ਮੁਲਾਂਕਣ ਕਰਦਾ ਹੈ, ਅਤੇ ਘੱਟ-ਭਰੋਸੇ ਵਾਲੇ ਰੀਪੇਅਰ ਵਰਕਫਲੋ ਲਈ ਭਰੋਸਾ ਮੈਟਾਡੇਟਾ ਪੜ੍ਹਦਾ ਹੈ। |
| `ReviewRunner` | `co_op_translator.review.runner` | ਸਰੋਤ ਫਾਇਲਾਂ, ਟਾਰਗਟ ਭਾਸ਼ਾਵਾਂ, ਅਤੇ ਕਨਫਿਗਰ ਕੀਤੇ translation roots ਵਿੱਚ ਨਿਰਧਾਰਤ ਸਮੀਖਿਆ ਜਾਂਚਾਂ ਨੂੰ ਕੋਆਰਡੀਨੇਟ ਕਰਦਾ ਹੈ। |
| `ReviewTarget` | `co_op_translator.review.targets` | ਇੱਕ ਸਰੋਤ root ਅਤੇ ਉਸ root ਲਈ ਸਮੀਖਿਆ ਕੀਤੀ ਗਈ ਅਨੁਵਾਦ ਆਉਟਪੁੱਟ ਡਾਇਰੈਕਟਰੀ ਦਾ ਵੇਰਵਾ ਦਿੰਦਾ ਹੈ। |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | legacy alias ਭਾਸ਼ਾ ਫੋਲਡਰਾਂ ਦੀ ਪਹਿਚਾਣ ਕਰਦਾ ਹੈ ਅਤੇ canonical BCP 47 ਫੋਲਡਰ ਮਾਈਗ੍ਰੇਸ਼ਨ ਯੋਜਨਾਵਾਂ ਤਿਆਰ ਕਰਦਾ ਹੈ। |
| `Config` | `co_op_translator.config.base_config` | `.env` ਫਾਈਲਾਂ ਲੋਡ ਕਰਦਾ ਹੈ ਅਤੇ ਜਾਂਚਦਾ ਹੈ ਕਿ ਲੋੜੀਂਦੇ LLM ਅਤੇ ਵਿਕਲਪੀ Vision ਪ੍ਰੋਵਾਈਡਰ ਕਨਫਿਗਰ ਕੀਤੇ ਗਏ ਹਨ ਜਾਂ ਨਹੀਂ। |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI ਜਾਂ OpenAI ਨੂੰ ਆਟੋ-ਡਿਟੈਕਟ ਕਰਦਾ ਹੈ, ਲੋੜੀਂਦੇ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲਾਂ ਦੀ ਵੈਧਤਾ ਜਾਂਚਦਾ ਹੈ, ਅਤੇ ਪ੍ਰੋਵਾਈਡਰ ਕੰਨੈਕਟਿਵਿਟੀ ਜਾਂਚਾਂ ਚਲਾਉਂਦਾ ਹੈ। |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision ਸੰਰਚਨਾ ਦਾ ਪਤਾ ਲਗਾਉਂਦਾ ਹੈ ਅਤੇ ਇਮੇਜ ਅਨੁਵਾਦ ਲਈ ਕੰਨੈਕਟਿਵਿਟੀ ਜਾਂਚਾਂ ਚਲਾਉਂਦਾ ਹੈ। |