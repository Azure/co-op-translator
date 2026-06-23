# Examples

These examples use the real CLI and Python API entry points from this repository.

## Translate Markdown with the CLI

```bash
translate -l "ko ja fr" -md
```

This translates Markdown files only and writes output under:

```text
translations/ko/
translations/ja/
translations/fr/
```

## Translate notebooks only

```bash
translate -l "zh-CN" -nb
```

Notebook links can later be normalized with:

```bash
migrate-links -l "zh-CN"
```

## Translate images only

```bash
translate -l "pt-BR" -img
```

Image translation requires both an LLM provider and Azure AI Vision.

## Preview without writing files

```bash
translate -l "de es" -md --dry-run
```

Dry runs are useful when checking token estimates, migration plans, or CI wiring.

## Repair low-confidence translations

First evaluate translations:

```bash
evaluate -l "ko" -c 0.8
```

Then retranslate Markdown files below the threshold:

```bash
translate -l "ko" --fix -c 0.8 -md
```

## Run from Python

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

## Translate Markdown content from Python

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

This translates the Markdown string only. It does not rewrite links or write translation files.

## Translate then rewrite Markdown paths

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

## Translate multiple roots from Python

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

## Use explicit output groups

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

## Preserve glossary terms

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

Glossary terms are scoped to the API call and restored afterward.

## CI-friendly translation command

```bash
translate -l "ko ja" -md -y -s
```

This auto-confirms prompts and saves DEBUG-level logs under `logs/`.
