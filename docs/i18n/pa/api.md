# ਪਾਇਥਨ API

ਸਥਿਰ ਪਬਲਿਕ Python API ਨੂੰ `co_op_translator.api` ਤੋਂ ਐਕਸਪੋਰਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਜ਼ਿਆਦਾਤਰ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਇਹਨਾਂ ਵਿੱਚੋਂ ਕਿਸੇ ਇਕ ਵਰਕਫਲੋ ਨੂੰ ਵਰਤਦੇ ਹਨ:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| ਵੱਖ-ਵੱਖ ਫ਼ਾਇਲਾਂ ਜਾਂ ਦਸਤਾਵੇਜ਼ਾਂ ਦਾ ਅਨੁਵਾਦ | ਤੁਹਾਡੀ ਐਪਲੀਕੇਸ਼ਨ ਸਰੋਤ ਸਮੱਗਰੀ ਨੂੰ ਪੜ੍ਹਦੀ ਹੈ, ਅਨੁਵਾਦ ਲਈ Co-op Translator ਨੂੰ ਕਾਲ ਕਰਦੀ ਹੈ, ਅਤੇ ਨਤੀਜੇ ਨੂੰ ਕਿੱਥੇ ਸੇਵ ਕਰਨਾ ਹੈ ਇਹ ਫੈਸਲਾ ਕਰਦੀ ਹੈ। | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| ਹੋਸਟ-ਏਜੰਟ ਅਨੁਵਾਦ ਲਈ ਸਮੱਗਰੀ ਤਿਆਰ ਕਰੋ | ਤੁਹਾਡਾ MCP ਹੋਸਟ ਜਾਂ ਐਪਲੀਕੇਸ਼ਨ ਮਾਡਲ ਚੰਕਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰੇਗਾ, ਜਦਕਿ Co-op Translator ਚੰਕਿੰਗ ਅਤੇ ਦੁਬਾਰਾ ਨਿਰਮਾਣ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ। | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| ਇੱਕ ਪੂਰੇ ਰਿਪੋਜ਼ਟਰੀ ਦਾ ਅਨੁਵਾਦ ਕਰੋ | ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ ਕਿ Python API CLI ਵਾਂਗ ਵਰਤਾਵ ਕਰੇ ਅਤੇ ਖੋਜ, ਆਉਟਪੁੱਟ ਪਾਥ, ਮੈਟਾ ਡੇਟਾ, ਸਫਾਈ, ਅਤੇ ਲਿਖਾਈਆਂ ਨੂੰ ਸੰਭਾਲੇ। | `run_translation` |

ਜ਼ਿਆਦਾਤਰ ਨੀਵੇਂ-ਲੈਵਲ ਮੋਡੀਊਲ `core`, `config`, `review`, ਅਤੇ `utils` ਹੇਠਾਂ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਵੇਰਵੇ ਹਨ ਜੋ ਇਹਨਾਂ API ਐਂਟਰੀ ਪਾਇੰਟਾਂ ਵੱਲੋਂ ਵਰਤੇ ਜਾਂਦੇ ਹਨ।

MCP ਕਲਾਇੰਟ ਉਹੀ ਪਬਲਿਕ API [MCP ਸਰਵਰ](mcp.md) ਰਾਹੀਂ ਵਰਤਦੇ ਹਨ। ਜਦੋਂ ਤੁਸੀਂ ਸਿੱਧਾ Python ਕਾਲ ਕਰ ਰਹੇ ਹੋ ਤਾਂ ਇਹ ਪੰਨਾ ਵਰਤੋ, ਅਤੇ ਜਦੋਂ Co-op Translator ਨੂੰ ਕਿਸੇ ਏਜੰਟ ਜਾਂ ਐਡੀਟਰ ਲਈ ਉਪਲਬਧ ਕਰਵਾ ਰਹੇ ਹੋ ਤਾਂ MCP ਗਾਈਡ ਵਰਤੋ। ਜੇ ਤੁਸੀਂ CLI, Python API, ਅਤੇ MCP ਵਿਚੋਂ ਫੈਸਲਾ ਕਰ ਰਹੇ ਹੋ, ਤਾਂ [ਆਪਣਾ ਵਰਕਫਲੋ ਚੁਣੋ](workflows.md) ਤੋਂ ਸ਼ੁਰੂ ਕਰੋ।

## ਪਹਿਲੀ ਵਾਰੀ API ਫਲੋ

ਜੇ ਤੁਸੀਂ Python ਕੋਡ ਤੋਂ Co-op Translator ਨੂੰ ਕਾਲ ਕਰ ਰਹੇ ਹੋ ਤਾਂ ਇੱਥੋਂ ਸ਼ੁਰੂ ਕਰੋ:

1. ਇੱਕ LLM ਪ੍ਰਦਾਤਾ ਨੂੰ [ਕੰਫਿਗਰੇਸ਼ਨ](configuration.md) ਵਿੱਚ ਦਿੱਤੇ ਤਰੀਕੇ ਅਨੁਸਾਰ ਸੰਰਚਿਤ ਕਰੋ, ਜਦ ਤੱਕ ਤੁਸੀਂ ਕੇਵਲ Markdown ਜਾਂ ਨੋਟਬੁੱਕ ਚੰਕ ਹੋਸਟ-ਏਜੰਟ ਅਨੁਵਾਦ ਲਈ ਤਿਆਰ ਨਹੀਂ ਕਰ ਰਹੇ ਹੋ।
2. ਫੈਸਲਾ ਕਰੋ ਕਿ ਤੁਹਾਡੀ ਐਪਲੀਕੇਸ਼ਨ ਫਾਇਲ I/O ਦੀ ਮਲਕੀਅਤ ਰੱਖਦੀ ਹੈ ਜਾਂ ਨਹੀਂ।
3. ਜਦੋਂ ਤੁਹਾਡੀ ਐਪਲੀਕੇਸ਼ਨ ਵਿਅਕਤੀਗਤ ਫਾਇਲਾਂ ਨੂੰ ਪੜ੍ਹਦੀ ਅਤੇ ਲਿਖਦੀ ਹੈ ਤਾਂ content APIs ਵਰਤੋ।
4. ਜਦੋਂ Co-op Translator ਨੂੰ CLI ਵਾਂਗ ਇੱਕ ਰਿਪੋਜ਼ਟਰੀ ਪ੍ਰੋਸੈਸ ਕਰਨਾ ਹੋਵੇ ਤਾਂ `run_translation` ਵਰਤੋ।
5. ਅਨੁਵਾਦ ਤੋਂ ਬਾਦ ਜੇ ਤੁਹਾਨੂੰ ਆਟੋਮੇਸ਼ਨ ਵਿੱਚ ਨਿਰਧਾਰਤ ਜਾਂਚਾਂ ਦੀ ਲੋੜ ਹੋਵੇ ਤਾਂ `run_review` ਵਰਤੋਂ।

| Goal | API to start with |
| --- | --- |
| ਇੱਕ Markdown ਸਟਰਿੰਗ ਜਾਂ ਫ਼ਾਇਲ ਦਾ ਅਨੁਵਾਦ ਕਰੋ | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| ਕਿਸੇ ਹੋਸਟ ਏਜੰਟ ਨੂੰ Markdown ਜਾਂ ਨੋਟਬੁੱਕ ਖੰਡਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰਨ ਦਿਓ | `start_markdown_agent_translation` ਜਾਂ `start_notebook_agent_translation` |
| ਅਨੁਵਾਦ ਕੀਤੀਆਂ ਲਿੰਕਾਂ ਨੂੰ ਆਉਟਪੁੱਟ ਪਾਥ ਚੁਣਨ ਤੋਂ ਬਾਅਦ ਦੁਬਾਰਾ ਲਿਖੋ | `rewrite_markdown_paths` ਜਾਂ `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## ਸਥਿਤੀ 1: ਵੱਖ-ਵੱਖ ਫ਼ਾਇਲਾਂ ਜਾਂ ਦਸਤਾਵੇਜ਼ਾਂ ਦਾ ਅਨੁਵਾਦ

ਜਦੋਂ ਤੁਹਾਡੇ ਕੋਲ ਪਹਿਲਾਂ ਹੀ ਕੋਈ ਫਾਇਲ, ਐਡੀਟਰ ਬਫ਼ਰ, ਨੋਟਬੁੱਕ ਪੇਲੋਡ, MCP ਰਿਕਵੇਸਟ, ਜਾਂ ਕਸਟਮ ਪਾਈਪਲਾਈਨ ਇਨਪੁੱਟ ਹੋਵੇ ਤਾਂ ਇਹ ਵਰਕਫਲੋ ਵਰਤੋਂ। ਤੁਹਾਡਾ ਕੋਡ ਫਾਇਲ I/O ਦਾ ਮਾਲਕ ਹੁੰਦਾ ਹੈ:

1. Read the source content.
2. Call a content translation API.
3. ਜੇ ਅਨੁਵਾਦਿਤ ਸਮੱਗਰੀ ਨੂੰ ਪ੍ਰੋਜੈਕਟ ਅਨੁਵਾਦ ਫੋਲਡਰ ਵਿੱਚ ਲਿਖਿਆ ਜਾਣਾ ਹੈ ਤਾਂ ਵਿਕਲਪੀ ਤੌਰ 'ਤੇ ਕਿਸੇ ਪਾਥ ਰਿਰਾਈਟਿੰਗ API ਨੂੰ ਕਾਲ ਕਰੋ।
4. ਨਤੀਜੇ ਨੂੰ ਆਪਣੀ ਐਪਲੀਕੇਸ਼ਨ ਤੋਂ ਸੇਵ ਜਾਂ ਵਾਪਸ ਕਰੋ।

ਕੰਟੈਂਟ ਅਨੁਵਾਦ APIs ਪ੍ਰੋਜੈਕਟ ਖੋਜ ਨਹੀਂ ਚਲਾਉਂਦੇ, ਮੈਟਾਡੇਟਾ ਨਹੀਂ ਲਿਖਦੇ, ਡਿਸਕਲੇਮਰ ਨਹੀਂ ਜੋੜਦੇ, ਅਤੇ ਲਿੰਕਾਂ ਨੂੰ ਆਪਣੇ ਆਪ ਰਿਰਾਈਟ ਨਹੀਂ ਕਰਦੇ।

### Markdown ਫਾਈਲ

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

ਜੇ ਅਨੁਵਾਦ ਕੀਤਾ Markdown Co-op Translator ਪ੍ਰੋਜੈਕਟ ਲੇਆਉਟ ਵਿੱਚ ਨਹੀਂ ਰਹੇਗਾ, ਤਾਂ `rewrite_markdown_paths` ਨੂੰ ਛੱਡੋ ਅਤੇ ਅਨੁਵਾਦ ਕੀਤੀ ਸਤਰ ਸਿੱਧਾ ਸੇਵ ਕਰੋ।

### Notebook ਫਾਈਲ

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

`translate_notebook_content` Markdown ਸੈੱਲਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ ਅਤੇ ਗੈਰ-Markdown ਸੈੱਲਾਂ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖਦਾ ਹੈ। ਪਾਥ ਨੂੰ ਦੁਬਾਰਾ ਲਿਖਣਾ ਸਿਰਫ Markdown ਸੈੱਲਾਂ 'ਤੇ ਲਾਗੂ ਹੁੰਦਾ ਹੈ।

### ਚਿੱਤਰ ਫਾਈਲ

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

`translate_image_content` ਸਰੋਤ ਚਿੱਤਰ ਨੂੰ ਪੜ੍ਹਦਾ ਹੈ ਅਤੇ ਇੱਕ ਰੇਂਡਰ ਕੀਤੀ ਹੋਈ `PIL.Image.Image` ਵਾਪਸ ਕਰਦਾ ਹੈ। ਇਹ ਅਨੁਵਾਦ ਕੀਤੇ ਚਿੱਤਰ ਦਾ ਮੈਟਾ-ਡੇਟਾ ਨਹੀਂ ਲਿਖਦਾ।

## ਸਥਿਤੀ 2: ਪੂਰੇ ਰੀਪੋਜ਼ਿਟਰੀ ਦਾ ਅਨੁਵਾਦ

ਇਸ ਵਰਕਫਲੋ ਨੂੰ ਉਸ ਵੇਲੇ ਵਰਤੋ ਜਦੋਂ ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ ਕਿ Python API `translate` CLI ਵਾਂਗ बिहੇਵ ਕਰੇ। `run_translation` ਸਮਰਥਿਤ ਫਾਇਲਾਂ ਨੂੰ ਖੋਜਦਾ ਹੈ, ਚੁਣੀ ਹੋਈ ਸਮੱਗਰੀ ਦੀਆਂ ਕਿਸਮਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ, ਪਾਥ ਰਿਰਾਈਟ ਕਰਦਾ ਹੈ, ਆਉਟਪੁਟ ਫਾਇਲਾਂ ਲਿਖਦਾ ਹੈ, ਮੈਟਾਡੇਟਾ ਅਪਡੇਟ ਕਰਦਾ ਹੈ, ਅਤੇ ਕਲੀਨਅਪ ਵਰਗੇ ਅਨੁਵਾਦ ਰੱਖ-ਰਖਾਅ ਦੇ ਕੰਮ ਕਰਦਾ ਹੈ।

`run_translation` ਪ੍ਰੋਜੈਕਟ ਆਰਕਸਟ੍ਰੇਸ਼ਨ ਲਈ ਪਸੰਦੀਦਾ ਐਂਟਰੀ ਪਾਇੰਟ ਹੈ। `translate_project` ਨੂੰ ਉਸੇ ਵਿਹਾਰ ਨਾਲ ਇੱਕ ਕੰਪੈਟਿਬਿਲਿਟੀ ਅਲਿਆਸ ਵਜੋਂ ਐਕਸਪੋਰਟ ਕੀਤਾ ਗਿਆ ਹੈ।

ਮੌਜੂਦਾ ਰਿਪੋਜ਼ਿਟਰੀ ਦੀਆਂ Markdown ਫਾਈਲਾਂ ਨੂੰ ਕੋਰੀਅਨ ਅਤੇ ਜਾਪਾਨੀ ਵਿੱਚ ਅਨੁਵਾਦ ਕਰੋ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

ਕੇਵਲ ਇੱਕ ਨਿਰਧਾਰਤ ਪ੍ਰੋਜੈਕਟ ਰੂਟ ਤੋਂ ਨੋਟਬੁੱਕਾਂ ਨੂੰ ਅਨੁਵਾਦ ਕਰੋ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

ਫਾਇਲਾਂ ਨੂੰ ਲਿਖਣ ਤੋਂ ਬਿਨਾਂ ਅਨੁਵਾਦ ਦੀ ਮਾਤਰਾ ਦਾ ਪ੍ਰੀਵਿਊ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

ਇੱਕ ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਲਈ ਸੰਰਚਤ ਪ੍ਰਗਤੀ ਘਟਨਾਵਾਂ ਦਰਜ ਕਰੋ:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # ਆਪਣੇ job-event ਟੇਬਲ ਵਿੱਚ ਪੇਲੋਡ ਸਟੋਰ ਕਰੋ ਜਾਂ ਇਸਨੂੰ ਆਪਣੇ UI ਤੇ ਸਟਰੀਮ ਕਰੋ।


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Events use the versioned schema `co-op.translation.event.v1`. Integrations should
depend on stable fields such as `type` and `stage_key`, not on human-facing
console text or `stage_label`.

ਇੱਕ ਕੌਲ ਵਿੱਚ ਕਈ ਸਮਗਰੀ ਰੂਟਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰੋ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

ਅਨੁਵਾਦਾਂ ਨੂੰ ਵਿਸ਼ੇਸ਼ ਆਉਟਪੁਟ ਗਰੁੱਪਾਂ ਵਿੱਚ ਲਿਖੋ:

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

ਜਦੋਂ ਹਰ ਭਾਸ਼ਾ ਵਿੱਚ ਇੱਕ ਨੈਸਟਡ ਸਬਡਾਇਰੈਕਟਰੀ ਹੋਣੀ ਚਾਹੀਦੀ ਹੋਵੇ ਤਾਂ ਭਾਸ਼ਾ-ਵਾਰ ਪਲੇਸਹੋਲਡਰ ਵਰਤੋਂ:

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

ਜੇ `markdown`, `notebook`, ਜਾਂ `images` ਵਿੱਚੋਂ ਕੋਈ ਵੀ ਸੈੱਟ ਨਹੀਂ ਹੈ, ਤਾਂ API ਸਾਰੀਆਂ ਸਮਰਥਤ ਕਿਸਮਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ: Markdown, ਨੋਟਬੁੱਕਾਂ, ਅਤੇ ਤਸਵੀਰਾਂ.

### ਸਵੀਕਾਰ ਕੀਤੀਆਂ ਮਨੁੱਖੀ ਸੋਧਾਂ ਨੂੰ ਅਨੁਵਾਦ ਸਥਿਤੀ ਪ੍ਰਦਾਤਾ ਨਾਲ ਬਰਕਰਾਰ ਰੱਖੋ

ਮੂਲ ਰੂਪ ਵਿੱਚ, Co-op Translator ਆਪਣਾ ਮੌਜੂਦਾ ਫਾਈਲ-ਸਤਹ ਵਰਤਾਰਾ ਰੱਖਦਾ ਹੈ: ਜਦੋਂ ਇੱਕ
Markdown ਸਰੋਤ ਪੁਰਾਣਾ ਹੋ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਸਾਰੀ ਅਨੁਵਾਦ ਕੀਤੀ ਫਾਈਲ ਮੁੜ-ਤਿਆਰ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਹੋਸਟ ਕੀਤੀਆਂ
ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਵਿਕਲਪਕ ਤੌਰ 'ਤੇ `TranslationStateProvider` ਪਾਸ ਕਰ ਸਕਦੇ ਹਨ ਤਾਂ ਕਿ ਮਨੁੱਖੀ
ਸੋਧਾਂ ਉਹਨਾਂ ਸਰੋਤ ਬਲਾਕਾਂ ਵਿੱਚ ਜੋ ਬਦਲੇ ਨਹੀਂ ਗਏ, ਸੁਰੱਖਿਅਤ ਰਹਿਣ।

ਪ੍ਰਦਾਤਾ ਆਖਰੀ ਸਵੀਕਾਰ ਕੀਤਾ ਸਰੋਤ/ਲਕਸ਼ ਜੋੜਾ ਮੁਹੱਈਆ ਕਰਵਾਉਂਦਾ ਹੈ ਅਤੇ ਹਰ ਨਵੇਂ
ਉਮੀਦਵਾਰ। ਸਵੀਕਾਰਤਾ ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਦੀ ਜ਼ਿੰਮੇਵਾਰੀ ਰਹਿੰਦੀ ਹੈ—ਉਦਾਹਰਣ ਲਈ,
ਅਨੁਵਾਦ ਪੁਲ ਰਿਕਵੇਸਟ ਮਰਜ ਹੋ ਜਾਣ ਤੋਂ ਬਾਅਦ:

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

ਇੱਕ ਵੈਧ ਸਵੀਕਾਰ ਕੀਤੀ ਬੇਸਲਾਈਨ ਵਾਲੀਆਂ Markdown ਫਾਈਲਾਂ ਲਈ, Co-op Translator ਐਲਾਈਨ ਕਰਦਾ ਹੈ
ਉੱਪਰੀ-ਸਤਹ ਦੇ Markdown ਬਲਾਕ। ਬਦਲੇ ਨਾ ਗਏ ਸਰੋਤ ਬਲਾਕ ਮੌਜੂਦਾ ਅਨੁਵਾਦਿਤ
ਬਲਾਕ, ਜਿਸ ਵਿੱਚ ਲੋਕਾਂ ਦੁਆਰਾ ਕੀਤੀਆਂ ਸੋਧਾਂ ਵੀ ਸ਼ਾਮਿਲ ਹਨ; ਬਦਲੇ ਜਾਂ ਜੋੜੇ ਗਏ ਸਰੋਤ ਬਲਾਕ ਅਨੁਵਾਦ ਲਈ ਭੇਜੇ ਜਾਂਦੇ ਹਨ
ਅਨੁਵਾਦ ਲਈ; ਮਿਟਾਏ ਗਏ ਸਰੋਤ ਬਲਾਕ ਹਟਾਏ ਜਾਂਦੇ ਹਨ। ਜੇ ਐਲਾਈਨਮੈਂਟ ਅਸਪੱਸ਼ਟ ਹੈ,
ਟਾਰਗੇਟ ਢਾਂਚਾ ਬਦਲ ਗਿਆ ਹੈ, ਬਲਾਕ ਅਨੁਵਾਦ ਅਵੈਧ ਹੈ, ਜਾਂ ਕੋਈ ਬੇਸਲਾਈਨ ਉਪਲਬਧ ਨਹੀਂ ਹੈ,
ਉਪਲਬਧ ਨਹੀਂ ਹੋਵੇ, Co-op Translator ਸੁਰੱਖਿਅਤ ਤਰੀਕੇ ਨਾਲ ਮੌਜੂਦਾ ਪੂਰੀ-ਫਾਈਲ
ਅਨੁਵਾਦ ਪਾਥ ਤੇ ਵਾਪਸ ਆ ਜਾਂਦਾ ਹੈ।

ਇਹ API ਦਸਤਾਵੇਜ਼ ਅਨੁਵਾਦ ਦੀ ਹਾਲਤ ਸਟੋਰ ਕਰਦਾ ਹੈ, ਨਾ ਕਿ ਕ੍ਰਾਸ-ਡਾਕਯੂਮੈਂਟ ਫਰੇਜ਼ ਜਾਂ
ਸੈਗਮੈਂਟ ਅਨੁਵਾਦ ਮੈਮੋਰੀ। ਇਹ ਇਸ ਵੇਲੇ Markdown ਪ੍ਰੋਜੈਕਟ ਅਨੁਵਾਦ ਤੇ ਲਾਗੂ ਹੁੰਦਾ ਹੈ।
ਨੋਟਬੁੱਕ ਅਤੇ ਚਿੱਤਰ ਦਾ ਵਿਹਾਰ ਅਪਰਿਵਰਤਿਤ ਹੈ। `update=True` ਪਾਸ ਕਰਨ ਨਾਲ
ਹਾਲੇ ਵੀ ਪੂਰੀ ਮੁੜ-ਤਿਆਰੀ ਦੀ ਬੇਨਤੀ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।

ਜੇ ਇੱਕ ਜਾਂ ਵੱਧ ਫਾਇਲਾਂ ਦਾ ਅਨੁਵਾਦ ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਦਾ, ਤਾਂ `run_translation` ਇੱਕ
`RuntimeError` ਉੱਠਾਉਂਦਾ ਹੈ ਪ੍ਰੋਜੈਕਟ ਵਰਕਫਲੋ ਖਤਮ ਹੋਣ ਤੋਂ ਬਾਅਦ, ਇੱਕ
ਕਮੀ ਵਾਲੇ ਨਤੀਜੇ ਨਾਲ ਸਫਲ ਰਨ ਦੀ ਰਿਪੋਰਟ ਕਰਨ ਦੀ ਥਾਂ। ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਨੂੰ ਇਸਨੂੰ ਇਕ ਨਾਕਾਮ
ਜੌਬ ਵਜੋਂ ਮੰਨਣਾ ਚਾਹੀਦਾ ਹੈ ਅਤੇ ਪਿਛਲੀ ਸਵੀਕਾਰ ਕੀਤੀ ਅਨੁਵਾਦ ਸਥਿਤੀ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖਣਾ ਚਾਹੀਦਾ ਹੈ।

## ਅਨੁਵਾਦਿਤ ਆਉਟਪੁੱਟ ਦੀ ਸਮੀਖਿਆ

`run_review` LLM ਜਾਂ Vision ਪ੍ਰਮਾਣਪੱਤਰਾਂ ਦੇ ਬਗੈਰ ਨਿਰਧਾਰਤ ਅਨੁਵਾਦ ਚੈੱਕ ਚਲਾਉਂਦਾ ਹੈ।

!!! note "Beta"
    `run_review` ਇੱਕ ਬੀਟਾ ਨਿਰਧਾਰਤ ਸਮੀਖਿਆ API ਹੈ। ਇਹ ਮਾਡਲ ਪ੍ਰਦਾਤਾਵਾਂ ਨੂੰ ਕਾਲ ਨਹੀਂ ਕਰਦਾ ਅਤੇ ਫਾਈਲਾਂ ਨਹੀਂ ਲਿਖਦਾ, ਪਰ ਚੈੱਕਾਂ ਅਤੇ ਸਮੱਸਿਆ ਸਕੀਮਾਂ ਵਿਕਸਤ ਹੋ ਸਕਦੀਆਂ ਹਨ।

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

README-ਕੇਵਲ ਅਨੁਵਾਦ ਤੋਂ ਬਾਅਦ, ਸਮੀਖਿਆ ਲਈ ਇੱਕੋ ਹੀ ਸਕੋਪ ਵਰਤੋ:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` reviews only `README.md` under each configured source root,
including custom `groups` and output directories. Other documents and nested
READMEs are excluded. A missing source README raises `ValueError`; failed
translation checks raise `RuntimeError`.

ਕੇਵਲ ਉਸ ਫਾਇਲਾਂ ਦੀ ਸਮੀਖਿਆ ਕਰੋ ਜੋ ਇਕ ਬੇਸ ਰੈਫ ਦੇ ਖਿਲਾਫ ਬਦਲੀ ਗਈਆਂ ਹਨ ਅਤੇ GitHub-ਸ਼ੈਲੀ ਦਾ ਆਉਟਪੁੱਟ ਪ੍ਰਿੰਟ ਕਰੋ:

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

## ਕਾਪੀ-ਪੇਸਟ API ਉਦਾਹਰਨਾਂ

ਫਾਇਲਾਂ ਨੂੰ ਲਿਖੇ ਬਿਨਾਂ Markdown ਸਮਗਰੀ ਦਾ ਅਨੁਵਾਦ ਕਰੋ:

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

Translate and rewrite Markdown links:

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

Translate a repository from Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Translate multiple roots:

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

Preserve glossary terms:

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

## ਪਬਲਿਕ ਐਂਟਰੀ ਪੁਆਇੰਟਸ

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

## ਸਮੱਗਰੀ ਅਨੁਵਾਦ APIs

ਕੰਟੈਂਟ ਅਨੁਵਾਦ API ਉਹ ਇੰਟੇਗ੍ਰੇਸ਼ਨਾਂ ਲਈ ਬਣਾਏ ਗਏ ਹਨ ਜਿਹਨਾਂ ਕੋਲ ਪਹਿਲਾਂ ਹੀ ਮੈਮੋਰੀ ਵਿੱਚ ਸਮੱਗਰੀ ਹੁੰਦੀ ਹੈ, ਜਿਵੇਂ ਕਿ ਇੱਕ ਐਡੀਟਰ ਐਕਸਟੇੰਸ਼ਨ, MCP ਟੂਲ, ਨੋਟਬੁੱਕ ਪ੍ਰੋਸੈਸਰ, ਜਾਂ ਕਸਟਮ ਪਾਈਪਲਾਈਨ।

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | ਐਸਿੰਕ। ਸਿਰਫ਼ Markdown ਸਮੱਗਰੀ ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ। ਇਹ ਲਿੰਕਾਂ ਨੂੰ ਦੁਬਾਰਾ ਨਹੀਂ ਲਿਖਦਾ, ਮੈਟਾਡੇਟਾ ਨਹੀਂ ਲਿਖਦਾ, ਅਤੇ ਡਿਸਕਲੇਮਰ ਨਹੀਂ ਜੋੜਦਾ। |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | ਐਸਿੰਕ। Markdown ਸੈੱਲਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ ਅਤੇ ਗੈਰ-Markdown ਸੈੱਲਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਰੱਖਦਾ ਹੈ। ਇਹ ਲਿੰਕਾਂ ਨੂੰ ਦੁਬਾਰਾ ਨਹੀਂ ਲਿਖਦਾ, ਮੈਟਾਡੇਟਾ ਨਹੀਂ ਲਿਖਦਾ, ਅਤੇ ਡਿਸਕਲੇਮਰ ਨਹੀਂ ਜੋੜਦਾ। |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | ਸਮਕਾਲੀ। ਸਰੋਤ ਚਿੱਤਰੋਂ ਟੈਕਸਟ ਕੱਢਦਾ ਅਤੇ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ, ਫਿਰ ਇੱਕ ਰੇਂਡਰ ਕੀਤਾ ਚਿੱਤਰ ਵਾਪਸ ਕਰਦਾ ਹੈ। ਇਹ ਅਨੁਵਾਦਿਤ ਚਿੱਤਰ ਮੈਟਾਡੇਟਾ ਸੇਵ ਨਹੀਂ ਕਰਦਾ। |

`translate_markdown_content` ਅਤੇ `translate_notebook_content` ਆਪਣੇ ਆਪਸ਼ਨਾਂ ਰਾਹੀਂ ਇਕ ਵਿਕਲਪੀ `source_path` ਸੁīਕਾਰ ਕਰਦੇ ਹਨ। ਪਾਥ ਅਨੁਵਾਦਕ ਨੂੰ ਪ੍ਰਸੰਗ ਵਜੋਂ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ; ਕਾਲਰ ਅਨੁਵਾਦ ਤੋਂ ਬਾਅਦ ਕਿਸੇ ਵੀ ਪ੍ਰੋਜੈਕਟ-ਖਾਸ ਪਾਥ ਮੁੜਲਿਖਣ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਰਹਿੰਦੇ ਹਨ।

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

ਉਹੀ ਵਿਕਲਪ ਡਿਕਸ਼ਨਰੀਆਂ ਵਜੋਂ ਦਿੱਤੇ ਜਾ ਸਕਦੇ ਹਨ:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## ਏਜੰਟ-ਸਹਾਇਤ ਅਨੁਵਾਦ APIs

ਏਜੰਟ-ਸਹਾਇਤ APIs Co-op Translator ਤੋਂ ਸੰਰਚਿਤ LLM ਪਰਦਾਤਾ ਨੂੰ ਕਾਲ ਨਹੀਂ ਕਰਦੀਆਂ। ਇਹ ਇੱਕ ਹੋਸਟ ਏਜੰਟ ਲਈ ਅਨੁਵਾਦ ਕਰਨ ਲਈ Markdown ਜਾਂ ਨੋਟਬੁੱਕ ਖੰਡ ਤਿਆਰ ਕਰਦੀਆਂ ਹਨ, ਫਿਰ ਅਨੁਵਾਦ ਕੀਤੀਆਂ ਖੰਡਾਂ ਤੋਂ ਅੰਤਿਮ ਸਮੱਗਰੀ ਨੂੰ ਪੁਨਰ-ਤਿਆਰ ਕਰਦੀਆਂ ਹਨ।

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | ਇੱਕ ਸਵੈ-ਨਿਰਭਰ Markdown ਜੌਬ ਖੰਡਾਂ, ਪ੍ਰੰਪਟਾਂ, ਅਤੇ ਪੁਨਰ-ਨਿਰਮਾਣ ਸਥਿਤੀ ਨਾਲ ਵਾਪਸ ਕਰਦਾ ਹੈ। |
| `finish_markdown_agent_translation` | ਇੱਕ ਜੌਬ ਅਤੇ ਹੋਸਟ-ਏਜੰਟ ਦੁਆਰਾ ਅਨੁਵਾਦ ਕੀਤੀਆਂ ਖੰਡਾਂ ਤੋਂ Markdown ਨੂੰ ਪੁਨਰ-ਨਿਰਮਾਣ ਕਰਦਾ ਹੈ। |
| `start_notebook_agent_translation` | ਹੋਸਟ-ਏਜੰਟ ਅਨੁਵਾਦ ਲਈ Markdown-ਸੈੱਲ ਖੰਡਾਂ ਵਾਲਾ ਨੋਟਬੁੱਕ ਜੌਬ ਵਾਪਸ ਕਰਦਾ ਹੈ। |
| `finish_notebook_agent_translation` | ਕੋਡ ਸੈੱਲ, ਆਉਟਪੁੱਟ ਅਤੇ ਮੈਟਾਡੇਟਾ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖਦਿਆਂ ਨੋਟਬੁੱਕ JSON ਨੂੰ ਪੁਨਰ-ਨਿਰਮਾਣ ਕਰਦਾ ਹੈ। |

ਇਹ ਵਰਕਫਲੋ ਮੁੱਖ ਤੌਰ 'ਤੇ MCP ਹੋਸਟਾਂ ਲਈ ਨਿਰਧਾਰਤ ਹੈ। ਜੇ ਤੁਹਾਨੂੰ ਉਤਪਾਦਨ ਰਿਪੋਜ਼ਟਰੀ ਅਨੁਵਾਦ ਦੀ ਲੋੜ ਹੈ ਜਿਸ ਵਿੱਚ Co-op Translator ਪ੍ਰਦਾਤਾ ਕਾਲਾਂ ਦਾ ਪ੍ਰਬੰਧ ਕਰੇ, ਤਾਂ `translate_markdown_content`, `translate_notebook_content`, ਜਾਂ `run_translation` ਵਰਤੋ।

## ਰਸਤਾ ਦੁਬਾਰਾ ਲਿਖਣ ਵਾਲੇ APIs

ਪਾਥ ਰੀਰਾਇਟਿੰਗ APIs ਕੋਈ ਅਨੁਵਾਦ ਨਹੀਂ ਕਰਦੀਆਂ। ਇਹ ਲਿੰਕਾਂ ਅਤੇ ਫਰੰਟਮੇਟਰ ਪਾਥਾਂ ਨੂੰ ਅਪਡੇਟ ਕਰਦੀਆਂ ਹਨ ਜਦੋਂ ਕਾਲ ਕਰਨ ਵਾਲੇ ਸਰੋਤ ਪਾਥ, ਅਨੁਵਾਦਿਤ ਟਾਰਗੇਟ ਪਾਥ, ਅਤੇ ਪ੍ਰੋਜੈਕਟ ਲੇਆਉਟ ਨੂੰ ਜਾਣ ਲੈਂਦੇ ਹਨ।

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown ਬਾਡੀ ਅਤੇ ਫਰੰਟਮੇਟਰ | ਅਨੁਵਾਦਿਤ ਟਾਰਗੇਟ ਲਈ Markdown ਲਿੰਕਾਂ ਅਤੇ ਸਮਰਥਿਤ ਫਰੰਟਮੇਟਰ ਪਾਥ ਫੀਲਡਾਂ ਨੂੰ ਦੁਬਾਰਾ ਲਿਖਦਾ ਹੈ। |
| `rewrite_notebook_paths` | ਨੋਟਬੁੱਕ JSON ਵਿੱਚ Markdown ਸੈੱਲ | ਹਰ Markdown ਸੈੱਲ 'ਤੇ Markdown ਪਾਥ ਰੀਰਾਇਟਿੰਗ ਲਗਾਉਂਦਾ ਹੈ ਅਤੇ ਗੈਰ-Markdown ਸੈੱਲਾਂ ਨੂੰ ਬਦਲਦਾ ਨਹੀਂ। |

`policy` ਦਲੀਲ ਇਹ ਖੇਤਰਾਂ ਵਾਲੀ ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਹੋ ਸਕਦੀ ਹੈ:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Target language code, such as `"ko"` or `"pt-BR"`. |
| `root_dir` | No | Source project root. Defaults to `"."`. |
| `translations_dir` | No | Text translation output directory. Defaults to `translations` under `root_dir`. |
| `translated_images_dir` | No | Translated image output directory. Defaults to `translated_images` under `root_dir`. |
| `translation_types` | No | ਸਰਗਰਮ ਅਨੁਵਾਦ ਕਿਸਮਾਂ। ਡੀਫੌਲਟ ਤੌਰ 'ਤੇ Markdown, notebooks, ਅਤੇ images। |
| `lang_subdir` | No | ਹਰ ਭਾਸ਼ਾ ਫੋਲਡਰ ਦੇ ਹੇਠਾਂ ਵਿਕਲਪਿਕ ਸਬਡਾਇਰੈਕਟਰੀ। |

## ਪ੍ਰੋਜੈਕਟ ਅਨੁਵਾਦ ਪੈਰਾਮੀਟਰ

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | ਸਪੇਸ ਨਾਲ ਵੱਖ-ਵੱਖ ਲਿਖੇ ਟਾਰਗੇਟ ਭਾਸ਼ਾ ਕੋਡ, ਜਿਵੇਂ `"ko ja fr"`, ਜਾਂ `"all"`। ਐਲਿਆਸ ਕੋਡ canonical BCP 47 ਮੁੱਲਾਂ ਵਿੱਚ ਨਾਰਮਲਾਈਜ਼ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। |
| `root_dir` | `str` | `"."` | ਇੱਕ ਸਿੰਗਲ ਅਨੁਵਾਦ ਟਾਰਗੇਟ ਲਈ ਪ੍ਰੋਜੈਕਟ ਰੂਟ। ਜਦੋਂ `root_dirs` ਜਾਂ `groups` ਦਿੱਤੇ ਜਾਂਦੇ ਹਨ ਤਾਂ ਇਹ ਅਣਡਿੱਠਾ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। |
| `update` | `bool` | `False` | ਚੁਣੀਆਂ ਗਈਆਂ ਭਾਸ਼ਾਵਾਂ ਲਈ ਮੌਜੂਦਾ ਅਨੁਵਾਦਾਂ ਨੂੰ ਹਟਾਓ ਅਤੇ ਮੁੜ ਬਣਾਓ। |
| `images` | `bool` | `False` | Include image translation. Requires Azure AI Vision configuration. |
| `markdown` | `bool` | `False` | Include Markdown translation. |
| `notebook` | `bool` | `False` | Include Jupyter notebook translation. |
| `debug` | `bool` | `False` | Enable debug logging. |
| `save_logs` | `bool` | `False` | DEBUG-ਸਤਰ ਦੀਆਂ ਲੌਗ ਫਾਇਲਾਂ ਨੂੰ ਰੂਟ `logs/` ਡਾਇਰੈਕਟਰੀ ਹੇਠਾਂ ਸੇਵ ਕਰੋ। |
| `yes` | `bool` | `True` | ਪ੍ਰੋਗਰਾਮੈਟਿਕ ਅਤੇ CI ਵਰਤੋਂ ਲਈ ਪ੍ਰੰਪਟਾਂ ਨੂੰ ਆਟੋ-ਕਨਫਰਮ ਕਰੋ। |
| `add_disclaimer` | `bool` | `False` | ਅਨੁਵਾਦ ਕੀਤੇ Markdown ਅਤੇ ਨੋਟਬੁੱਕਾਂ ਵਿੱਚ ਮਸ਼ੀਨੀ ਅਨੁਵਾਦ ਡਿਸਕਲੇਮਰ ਸ਼ਾਮਲ ਕਰੋ। |
| `translations_dir` | `str \| None` | `None` | ਕਸਟਮ ਟੈਕਸਟ ਅਨੁਵਾਦ ਆਉਟਪੁੱਟ ਡਾਇਰੈਕਟਰੀ। ਸਾਪੇਖ ਪਾਥ ਹਰ ਰੂਟ ਦੇ ਮੁਕਾਬਲੇ ਹੱਲ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। |
| `image_dir` | `str \| None` | `None` | ਕਸਟਮ ਅਨੁਵਾਦ ਕੀਤੀਆਂ ਇਮੇਜਾਂ ਲਈ ਆਉਟਪੁੱਟ ਡਾਇਰੈਕਟਰੀ। ਸਾਪੇਖ ਪਾਥ ਹਰ ਰੂਟ ਦੇ ਮੁਕਾਬਲੇ ਹੱਲ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। |
| `root_dirs` | `Iterable[str] \| None` | `None` | ਕਈ ਰੂਟ ਜੋ ਇੱਕੋ ਆਉਟਪੁੱਟ ਸੈਟਿੰਗਾਂ ਸਾਂਝੀਆਂ ਕਰਦੇ ਹਨ। |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | ਖਾਸ `(root_dir, translations_dir)` ਜੋੜੇ। `root_dirs` ਉੱਤੇ ਪ੍ਰਾਥਮਿਕਤਾ ਰੱਖਦਾ ਹੈ। |
| `repo_url` | `str \| None` | `None` | README ਭਾਸ਼ਾ ਟੇਬਲ ਦੇ ਨਿਰਧਾਰਨ ਸਮੇਂ ਵਰਤੀ ਜਾਣ ਵਾਲੀ ਰਿਪੋਜ਼ਿਟਰੀ URL। |
| `glossaries` | `Iterable[str] \| None` | `None` | ਅਨੁਵਾਦ ਦੌਰਾਨ ਸੁਰੱਖਿਅਤ ਕਰਨ ਲਈ ਗਲੋਸਰੀ ਸ਼ਬਦ। ਨਕਲੀਆਂ ਅਤੇ ਖਾਲੀ ਸ਼ਬਦ ਸਧਾਰਨ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। |
| `dry_run` | `bool` | `False` | ਫਾਈਲਾਂ ਲਿਖਣ ਤੋਂ ਬਿਨਾਂ ਅਨੁਵਾਦ ਦੀ ਮਾਤਰਾ ਦਾ ਅੰਦਾਜ਼ਾ ਅਤੇ ਮਾਈਗ੍ਰੇਸ਼ਨ ਵਿਵਹਾਰ ਦਾ ਪ੍ਰੀਵਿਊ ਕਰੋ। |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | ਇਨਕ੍ਰੀਮੈਂਟਲ Markdown ਅੱਪਡੇਟਸ ਲਈ ਵਿਕਲਪਿਕ accepted-baseline ਅਤੇ candidate ਪਰਸਿਸਟੈਂਸ ਅਡੈਪਟਰ। ਇਸਨੂੰ ਛੱਡ ਦੇਣ ਨਾਲ ਮੌਜੂਦਾ ਫੁੱਲ-ਫਾਈਲ ਵਿਹਾਰ ਹੀ ਕਾਇਮ ਰਹਿੰਦਾ ਹੈ। |

## ਸਮੀਖਿਆ ਪੈਰਾਮੀਟਰ

`run_review` ਇरਾਦੇ ਨਾਲ `run_translation` ਸਿਗਨੇਚਰ ਦੀਆਂ ਸਮਾਨਤਾਂ (ਜਦੋਂ ਸੰਭਵ ਹੋਵੇ) ਦੀ ਨਕਲ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ ਆਟੋਮੇਸ਼ਨ ਘੱਟ ਤੋਂ ਘੱਟ ਸ਼ਾਖਾ ਨਾਲ ਅਨੁਵਾਦ ਅਤੇ ਸਮੀਖਿਆ ਵਰਕਫਲੋਜ਼ ਵਿਚ ਬਦਲ ਸਕੇ।

| ਪੈਰਾਮੀਟਰ | ਕਿਸਮ | ਮੂਲ-ਮੁੱਲ | ਉਦੇਸ਼ |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | ਸਮੀਖਿਆ ਲਈ ਟਾਰਗੇਟ ਭਾਸ਼ਾ ਫੋਲਡਰ। ਸਪੇਸ-ਅਲੱਗ ਕੀਤੇ ਸਤਰ ਅਤੇ iterable ਸਵੀਕਾਰ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। `"all"` ਹਰ ਮਿਲੀ ਹੋਈ ਅਨੁਵਾਦ ਭਾਸ਼ਾ ਦੀ ਸਮੀਖਿਆ ਕਰਦਾ ਹੈ। |
| `root_dir` | `str` | `"."` | ਇੱਕਲ੍ਹੇ ਸਮੀਖਿਆ ਟਾਰਗੇਟ ਲਈ ਪ੍ਰੋਜੈਕਟ ਰੂਟ। ਜਦੋਂ `root_dirs` ਜਾਂ `groups` ਮੁਹੱਈਆ ਕੀਤੇ ਜਾਂਦੇ ਹਨ ਤਾਂ ਇਹ ਨਜ਼ਰਅੰਦਾਜ਼ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। |
| `markdown` | `bool` | `False` | Markdown ਅਤੇ MDX ਸੋਰਸ ਫਾਈਲਾਂ ਸ਼ਾਮਲ ਕਰੋ। |
| `notebook` | `bool` | `False` | Jupyter ਨੋਟਬੁੱਕ ਸੋਰਸ ਫਾਈਲਾਂ ਸ਼ਾਮਲ ਕਰੋ। |
| `images` | `bool` | `False` | ਅਨੁਵਾਦ ਵਿਕਲਪਾਂ ਨਾਲ ਸਮਤੁਲਤਾ ਲਈ ਰਾਖਵਾਲ ਕੀਤੀ ਗਈ। ਇਮੇਜਾਂ ਲਈ ਲਿੰਕ ਸੰਦਰਭ Markdown ਵਿੱਚੋਂ ਜਾਂਚੇ ਜਾਂਦੇ ਹਨ। |
| `translations_dir` | `str \| None` | `None` | ਕਸਟਮ ਟੈਕਸਟ ਅਨੁਵਾਦ ਆਉਟਪੁੱਟ ਡਾਇਰੈਕਟਰੀ। ਸਾਪੇਖ ਪਾਥ ਹਰ ਰੂਟ ਦੇ ਮੁਕਾਬਲੇ ਹੱਲ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। |
| `root_dirs` | `Iterable[str] \| None` | `None` | ਕਈ ਰੂਟ ਜੋ ਇੱਕੋ ਆਉਟਪੁੱਟ ਸੈਟਿੰਗਾਂ ਸਾਂਝੀਆਂ ਕਰਦੇ ਹਨ। |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | ਖਾਸ `(root_dir, translations_dir)` ਜੋੜੇ। `root_dirs` ਉੱਤੇ ਪ੍ਰਾਥਮਿਕਤਾ ਰੱਖਦਾ ਹੈ। |
| `changed_from` | `str \| None` | `None` | ਸਮੀਖਿਆ ਨੂੰ ਬਦਲੇ ਗਏ ਸੋਰਸ ਫਾਈਲਾਂ ਤੱਕ ਸੀਮਿਤ ਕਰਨ ਲਈ ਵਰਤਿਆ ਗਿਆ Git ਰਿਫ਼। |
| `readme_only` | `bool` | `False` | ਹਰ ਸੋਰਸ ਰੂਟ ਹੇਠਾਂ ਸਿਰਫ਼ `README.md` ਦੀ ਸਮੀਖਿਆ ਕਰੋ। ਸੋਰਸ README ਮੌਜੂਦ ਨਾ ਹੋਣ 'ਤੇ `ValueError` ਉਠਾਈ ਜਾਂਦੀ ਹੈ। |
| `output_format` | `str` | `"text"` | ਸਮੀਖਿਆ ਆਉਟਪੁੱਟ ਫਾਰਮੈਟ। ਸਹਾਇਤ ਕੀਤੇ ਮੁੱਲ `"text"` ਅਤੇ `"github"` ਹਨ। |
| `fail_on_warnings` | `bool` | `False` | ਚੇਤਾਵਨੀਆਂ ਨੂੰ ਤਰੁਟੀਆਂ ਦੇ ਨਾਲ-ਨਾਲ ਫੇਲ੍ਹ ਵਜੋਂ ਵਿਵਹਾਰ ਕਰੋ। |
| `debug` | `bool` | `False` | ਡਿਬੱਗ ਲੋਗਿੰਗ ਯੋਗ ਕਰੋ। |
| `save_logs` | `bool` | `False` | ਰੂਟ `logs/` ਡਾਇਰੈਕਟਰੀ ਹੇਠ DEBUG-ਸਤਹ ਲੋਗ ਫਾਈਲਾਂ ਸੇਵ ਕਰੋ। |

ਜੇ `markdown`, `notebook`, ਜਾਂ `images` ਵਿੱਚੋਂ ਕੋਈ ਵੀ ਸੈੱਟ ਨਹੀਂ ਹੈ, ਤਾਂ API ਜਿੱਥੇ ਲਾਗੂ ਹੋਵੇ Markdown, ਨੋਟਬੁੱਕ, ਅਤੇ ਇਮੇਜ ਲਿੰਕ ਸੰਦਰਭਾਂ ਦੀ ਸਮੀਖਿਆ ਕਰਦੀ ਹੈ। ਸਮੀਖਿਆ ਕਿਸੇ LLM ਪ੍ਰਦਾਤਾ ਨੂੰ ਕਾਲ ਨਹੀਂ ਕਰਦੀ ਅਤੇ ਇਸ ਲਈ API ਕੀਜ਼ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ।

## ਸੰਰਚਨਾ ਦੀਆਂ ਲੋੜਾਂ

ਪ੍ਰੋਵਾਈਡਰ-ਸਮਰਥਿਤ ਅਨੁਵਾਦ APIs ਨੂੰ ਅਨੁਵਾਦ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਪ੍ਰੋਵਾਈਡਰ ਸੰਰਚਨਾ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ:

- Markdown ਅਤੇ ਨੋਟਬੁੱਕ ਅਨੁਵਾਦ ਲਈ LLM ਪ੍ਰਦਾਤਾ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। Azure OpenAI, OpenAI, ਜਾਂ Anthropic ਸੰਰਚਿਤ ਕਰੋ।
- ਇਮੇਜ ਅਨੁਵਾਦ ਲਈ LLM ਪ੍ਰਦਾਤਾ ਦੇ ਇਲਾਵਾ Azure AI Vision ਦੀ ਵੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।
- `run_translation` ਪ੍ਰੋਜੈਕਟ ਅਨੁਵਾਦ ਸ਼ੁਰੂ ਹੋਣ ਤੋਂ ਪਹਿਲਾਂ ਹਲਕੀ-ਫੁਲਕੀ ਕਨੈਕਟਿਵਿਟੀ ਚੈੱਕ ਚਲਾਉਂਦਾ ਹੈ।
- ਏਜੰਟ-ਸਹਾਇਤ `start_*_agent_translation` ਅਤੇ `finish_*_agent_translation` APIs Co-op Translator LLM ਪ੍ਰਦਾਤਿਆਂ ਨੂੰ ਕਾਲ ਨਹੀਂ ਕਰਦੀਆਂ। ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨ ਜਾਂ MCP ਏਜੰਟ ਤਿਆਰ ਕੀਤੇ ਗਏ ਚੰਕਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ।
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, ਅਤੇ `run_review` ਨਿਰਣਯਾਤਮਕ ਹਨ ਅਤੇ ਇਨ੍ਹਾਂ ਲਈ ਪ੍ਰੋਵਾਈਡਰ ਕਰੈਡੈਂਸ਼ਿਅਲ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ।

ਜ਼ਰੂਰੀ Azure OpenAI ਵੈਰੀਏਬਲ:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

ਜ਼ਰੂਰੀ OpenAI ਵੈਰੀਏਬਲ:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

ਜ਼ਰੂਰੀ Anthropic ਵੈਰੀਏਬਲ:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` ਅਤੇ `ANTHROPIC_MAX_TOKENS` ਵਿਕਲਪਿਕ ਹਨ। Co-op Translator 0.22.0 ਤੋਂ ਸ਼ੁਰੂ ਹੋਕੇ ਸਾਰੇ ਪ੍ਰੋਵਾਈਡਰਾਂ ਲਈ ਡੀਫੌਲਟ ਮਾਡਲ ਕਲਾਇੰਟ Microsoft Agent Framework ਹੈ। Semantic Kernel ਨੂੰ ਅਜੇ ਵੀ ਅਸਥਾਈ ਤੌਰ 'ਤੇ `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` ਨਾਲ ਚੁਣਿਆ ਜਾ ਸਕਦਾ ਹੈ, ਪਰ ਇਹ ਕਰਨ ਤੇ ਇੱਕ ਡੀਪ੍ਰੀਕੇਸ਼ਨ ਚੇਤਾਵਨੀ ਨਿਕਲਦੀ ਹੈ; ਚਰਣਬੱਧ ਹਟਾਓ ਯੋਜਨਾ ਲਈ [ਕੰਫਿਗਰੇਸ਼ਨ](configuration.md#model-client-backend) ਵੇਖੋ।

ਇਮੇਜ ਅਨੁਵਾਦ ਲਈ ਜ਼ਰੂਰੀ Azure AI Vision ਵੈਰੀਏਬਲ:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` ਨਿਰਣਯਾਤਮਕ ਹੈ ਅਤੇ ਇਸ ਲਈ LLM ਜਾਂ Azure AI Vision ਸੰਰਚਨਾ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ।

## ਵਿਹਾਰ ਟਿੱਪਣੀਆਂ

- ਸਮੱਗਰੀ ਅਨੁਵਾਦ API ਅਨੁਵਾਦ ਨੂੰ ਪ੍ਰੋਜੈਕਟ ਪਾਥ ਮੁੜਲਿਖਣ ਤੋਂ ਅਲੱਗ ਰੱਖਦੇ ਹਨ। ਜਦੋਂ ਅਨੁਵਾਦ ਕੀਤੀ ਸਮੱਗਰੀ ਲਈ ਪ੍ਰੋਜੈਕਟ-ਸਾਪੇਖ ਲਿੰਕਾਂ ਨੂੰ ਟਾਰਗੇਟ ਥਾਂ ਲਈ ਅਨੁਕੂਲ ਕਰਨ ਦੀ ਲੋੜ ਹੋਵੇ ਤਾਂ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ `rewrite_markdown_paths` ਜਾਂ `rewrite_notebook_paths` ਨੂੰ ਕਾਲ ਕਰੋ।
- ਪ੍ਰੋਜੈਕਟ ਔਰਕੇਸਟ੍ਰੇਸ਼ਨ APIs ਸਮੱਗਰੀ ਅਨੁਵਾਦ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਪ੍ਰੋਜੈਕਟ ਵਿਹਾਰ ਜੋੜਦੀਆਂ ਹਨ, ਜਿਸ ਵਿੱਚ ਫਾਈਲ ਖੋਜ, ਲਿਖਤਾਂ, ਪਾਥ ਮੁੜਲਿਖਣਾ, ਮੈਟਾਡੇਟਾ, ਸਫਾਈ, ਅਤੇ ਵਿਕਲਪਿਕ ਡਿਸਕਲੇਮਰ ਸ਼ਾਮਲ ਹਨ।
- `run_translation` CLI ਵਿੱਚ ਵਰਤੇ ਜਾਂਦੇ ਇੱਕੋ Rich-ਬੈਕਡ ਰਿਪੋਰਟਰ ਰਾਹੀਂ ਪ੍ਰਗਤੀ ਅਤੇ ਅਨੁਮਾਨ ਸਾਰ ਸੰਖੇਪ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ। ਗੈਰ-ਇੰਟਰਐਕਟਿਵ ਆਉਟਪੁੱਟ ਸਧਾਰਨ ਟੈਕਸਟ 'ਤੇ ਵਾਪਸ ਆ ਜਾਂਦਾ ਹੈ।
- `dry_run=True` ਵਰਚੁਅਲ README ਅਪਡੇਟਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਮਾਨ ਗਣਨਾ ਕਰਦਾ ਹੈ, ਪਰ README ਜਾਂ ਅਨੁਵਾਦ ਫਾਈਲਾਂ ਨਹੀਂ ਲਿਖਦਾ।
- `groups` ਨੂੰ ਕ੍ਰਮਵਾਰ ਪ੍ਰਕਿਰਿਆ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਕੰਮ ਸ਼ੁਰੂ ਹੋਣ ਤੋਂ ਪਹਿਲਾਂ ਇੱਕ ਇਕੱਠਾ ਅਨੁਮਾਨ ਪ੍ਰਿੰਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।
- ਜਦੋਂ ਇਮੇਜ ਅਨੁਵਾਦ ਚੁਣਿਆ ਜਾਂਦਾ ਹੈ, Vision ਸੰਰਚਨਾ ਮੌਜੂਦ ਨਾ ਹੋਣ 'ਤੇ ਅਨੁਵਾਦ ਸ਼ੁਰੂ ਹੋਣ ਤੋਂ ਪਹਿਲਾਂ ਇੱਕ ਗਲਤੀ ਉਠਦੀ ਹੈ।
- ਮੌਜੂਦਾ alias-ਆਧਾਰਿਤ ਭਾਸ਼ਾ ਫੋਲਡਰਾਂ ਦੀ ਪਹਿਚਾਣ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਅਤੇ ਰਨ ਦੌਰਾਨ ਉਨ੍ਹਾਂ ਨੂੰ ਕੈਨੋਨਿਕਲ ਭਾਸ਼ਾ ਫੋਲਡਰ ਨਾਮਾਂ ਵਿੱਚ ਮਾਈਗ੍ਰੇਟ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।
- `run_review` ਅਨੁਵਾਦਿਤ ਫਾਈਲਾਂ ਦੀ ਗੈਰਹਾਜ਼ਰੀ, ਗਾਇਬ ਜਾਂ ਪੁਰਾਣਾ ਅਨੁਵਾਦ ਮੈਟਾਡੇਟਾ, ਖ਼ਰਾਬ ਬਣਤਰ ਵਾਲੇ Markdown frontmatter/code fences, ਅਤੇ ਅਵੈਧ ਅਨੁਵਾਦ ਕੀਤੀ ਨੋਟਬੁੱਕ JSON 'ਤੇ ਫੇਲ੍ਹ ਕਰਦਾ ਹੈ।
- ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ `run_review` ਸਥਾਨਕ Markdown ਅਤੇ ਇਮੇਜ ਲਿੰਕ ਟਾਰਗੇਟਾਂ ਦੀ ਗੈਰਹਾਜ਼ਰੀ ਨੂੰ ਚੇਤਾਵਨੀ ਵਜੋਂ ਰਿਪੋਰਟ ਕਰਦਾ ਹੈ।

## ਅੰਦਰੂਨੀ ਕਾਲ ਪਾਥ

API ਉਹੀ ਕੋਰ ਈੰਪਲੀਮੇਂਟੇਸ਼ਨ ਨੂੰ ਡੈਲੀਗੇਟ ਕਰਦੀ ਹੈ ਜੋ CLI ਵੱਲੋਂ ਵਰਤੀ ਜਾਂਦੀ ਹੈ:

ਅਨੁਵਾਦ:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` ਇਨ-ਮੇਮੋਰੀ ਅਨੁਵਾਦ ਲਈ।
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` ਸਪੱਸ਼ਟ ਪਾਥ ਪੋਸਟ-ਪ੍ਰੋਸੈਸਿੰਗ ਲਈ।
3. `co_op_translator.api.translation.run_translation` ਪੂਰੇ ਪ੍ਰੋਜੈਕਟ ਔਰਕੇਸਟ੍ਰੇਸ਼ਨ ਲਈ।
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Markdown, ਨੋਟਬੁੱਕ ਅਤੇ ਇਮੇਜ ਲਈ ਕੇਂਦਰਿਤ ਪ੍ਰੋਜੈਕਟ ਅਨੁਵਾਦ ਮਿਕਸਿਨਜ਼।
8. `co_op_translator.core` ਹੇਠਾਂ Markdown, ਨੋਟਬੁੱਕ, ਟੈਕਸਟ, ਅਤੇ ਇਮੇਜ ਅਨੁਵਾਦਕ।

ਸਮੀਖਿਆ:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. `co_op_translator.review.checks` ਹੇਠ ਨਿਰਣਯਾਤਮਕ ਜਾਂਚਾਂ

ਹੇਠ ਲਿਖੀਆਂ ਕਲਾਸਾਂ ਰੱਖ-ਰਖਾਅ ਕਰਨ ਵਾਲਿਆਂ ਲਈ ਲਾਭਦਾਇਕ ਹਨ, ਪਰ ਇਹ ਪੈਕੇਜ-ਲੈਵਲ ਸਥਿਰ API ਵਜੋਂ ਨਿਕਾਸ ਨਹੀਂ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ।

| ਕਲਾਸ | ਮੌਡੀਊਲ | ਜ਼ਿੰਮੇਵਾਰੀ |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | ਪ੍ਰੋਜੈਕਟ-ਸਤਰ ਅਨੁਵਾਦ, ਡਾਇਰੈਕਟਰੀ ਪ੍ਰਬੰਧਨ, ਪ੍ਰਤੀ-ਭਾਸ਼ਾ ਮੈਟਾਡੇਟਾ ਨਾਰਮਲਾਈਜੇਸ਼ਨ, ਅਤੇ Markdown, ਨੋਟਬੁੱਕ ਅਤੇ ਇਮੇਜ ਅਨੁਵਾਦਕਾਂ ਨੂੰ ਅਸਾਇਨ ਕਰਨ ਦੀ ਕੋਆਰਡੀਨੇਸ਼ਨ ਕਰਦਾ ਹੈ। |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, ਨੋਟਬੁੱਕ, ਇਮੇਜ, stale ਪਤਾ ਕਰਨ ਅਤੇ ਅਨੁਵਾਦ ਮੈਟਾਡੇਟਾ ਅੱਪਡੇਟਸ ਲਈ async ਫਾਈਲ ਪ੍ਰੋਸੈਸਿੰਗ ਕੰਮ ਨਿਭਾਉਂਦਾ ਹੈ। |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown ਫਾਈਲ ਪੜ੍ਹਾਈ, ਸਮੱਗਰੀ ਅਨੁਵਾਦ, ਪਾਥ ਮੁੜਲਿਖਣਾ, ਮੈਟਾਡੇਟਾ, ਡਿਸਕਲੇਮਰ, ਅਤੇ ਲਿਖਤਾਂ ਨੂੰ ਸੰਚਾਲਿਤ ਕਰਦਾ ਹੈ। |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | ਨੋਟਬੁੱਕ ਫਾਈਲ ਪੜ੍ਹਾਈ, Markdown-ਸੈੱਲ ਅਨੁਵਾਦ, ਪਾਥ ਮੁੜਲਿਖਣਾ, ਮੈਟਾਡੇਟਾ, ਡਿਸਕਲੇਮਰ, ਅਤੇ ਲਿਖਤਾਂ ਨੂੰ ਸੰਚਾਲਿਤ ਕਰਦਾ ਹੈ। |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | ਸਰੋਤ ਇਮੇਜ ਖੋਜ, ਇਮੇਜ ਅਨੁਵਾਦ, ਆਉਟਪੁੱਟ ਪਾਥ, ਮੈਟਾਡੇਟਾ, ਅਤੇ ਲਿਖਤਾਂ ਨੂੰ ਸੰਚਾਲਿਤ ਕਰਦਾ ਹੈ। |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | ਅਨੁਵਾਦ ਕੀਤੇ Markdown ਜੋੜਿਆਂ ਨੂੰ ਲੱਭਦਾ ਹੈ, ਅਨੁਵਾਦ ਗੁਣਵੱਤਾ ਦਾ ਮੁਲਾਂਕਣ ਕਰਦਾ ਹੈ, ਅਤੇ ਘੱਟ-ਭਰੋਸੇ ਵਾਲੇ ਮੁਰੰਮਤ ਵਰਕਫਲੋਜ਼ ਲਈ ਭਰੋਸਾ ਮੈਟਾਡੇਟਾ ਪੜ੍ਹਦਾ ਹੈ। |
| `ReviewRunner` | `co_op_translator.review.runner` | ਸੋਰਸ ਫਾਈਲਾਂ, ਟਾਰਗੇਟ ਭਾਸ਼ਾਵਾਂ, ਅਤੇ ਸੰਰਚਿਤ ਅਨੁਵਾਦ ਰੂਟਾਂ 'ਤੇ ਨਿਰਣਯਾਤਮਕ ਸਮੀਖਿਆ ਜਾਂਚਾਂ ਨੂੰ ਕੋਆਰਡੀਨੇਟ ਕਰਦਾ ਹੈ। |
| `ReviewTarget` | `co_op_translator.review.targets` | ਇੱਕ ਸੋਰਸ ਰੂਟ ਅਤੇ ਉਸ ਰੂਟ ਲਈ ਸਮੀਖਿਆ ਕੀਤੀ ਜਾਣ ਵਾਲੀ ਅਨੁਵਾਦ ਆਉਟਪੁੱਟ ਡਾਇਰੈਕਟਰੀ ਨੂੰ ਵਰਨਨ ਕਰਦਾ ਹੈ। |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | ਲੈਗੇਸੀ alias ਭਾਸ਼ਾ ਫੋਲਡਰਾਂ ਦੀ ਪਹਿਚਾਣ ਕਰਦਾ ਹੈ ਅਤੇ ਕੈਨੋਨਿਕਲ BCP 47 ਫੋਲਡਰ ਮਾਈਗ੍ਰੇਸ਼ਨ ਯੋਜਨਾਵਾਂ ਤਿਆਰ ਕਰਦਾ ਹੈ। |
| `Config` | `co_op_translator.config.base_config` | `.env` ਫਾਈਲਾਂ ਲੋਡ ਕਰਦਾ ਹੈ ਅਤੇ ਜਾਂਚਦਾ ਹੈ ਕਿ ਜ਼ਰੂਰੀ LLM ਅਤੇ ਵਿਕਲਪਿਕ Vision ਪ੍ਰੋਵਾਈਡਰ ਸੰਰਚਿਤ ਹਨ ਜਾਂ ਨਹੀਂ। |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI, OpenAI, ਜਾਂ Anthropic ਨੂੰ ਆਟੋ-ਡਿਟੈਕਟ ਕਰਦਾ ਹੈ, ਜ਼ਰੂਰੀ ਇਨਵਾਇਰਨਮੈਂਟ ਵੈਰੀਏਬਲ ਚੈੱਕ ਕਰਦਾ ਹੈ ਅਤੇ ਪ੍ਰੋਵਾਈਡਰ ਕਨੈਕਟਿਵਿਟੀ ਜਾਂਚਾਂ ਚਲਾਉਂਦਾ ਹੈ। |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision ਸੰਰਚਨਾ ਦੀ ਪਹਿਚਾਣ ਕਰਦਾ ਹੈ ਅਤੇ ਇਮੇਜ ਅਨੁਵਾਦ ਲਈ ਕਨੈਕਟਿਵਿਟੀ ਜਾਂਚਾਂ ਚਲਾਉਂਦਾ ਹੈ। |