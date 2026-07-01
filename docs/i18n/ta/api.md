# Python API

நிறைவடைந்த பொதுச் Python API `co_op_translator.api` இலிருந்து экспорт செய்யப்படுகிறது. பெரும்பாலான ஒருங்கிணைப்புகள் இந்தப் பணிமுறைகளில் ஒன்றை பயன்படுத்துகின்றன:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Your application reads source content, calls Co-op Translator for translation, and decides where to save the result. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Your MCP host or application model will translate chunks, while Co-op Translator handles chunking and reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | You want the Python API to behave like the CLI and handle discovery, output paths, metadata, cleanup, and writes. | `run_translation` |

`core`, `config`, `review`, மற்றும் `utils` உட்பட்ட குறைந்த நிலை மாடியூல்களுக்கு இந்த API நுழைவாயில்கள் பயன்படுத்தும் செயலாக்க விவரங்கள் ஆகும்.

MCP கிளையன்டுகள் அதே பொதுப் API-ஐ [MCP Server](mcp.md) மூலம் பயன்படுத்துகின்றன. Python நேரடியாக அழைக்கும் போது இந்தப் பக்கம் பயன்படும், Co-op Translator-ஐ ஒரு முகவர் அல்லது ஆசிரியரிடம் வெளிப்படுத்தும் போது MCP கையேடைப் பயன்படுத்துங்கள். CLI, Python API, மற்றும் MCP இடையேயான தேர்வில் இருக்கின், முதலில் [Choose Your Workflow](workflows.md) பக்கத்தைப் படியுங்கள்.

## First-Time API Flow

Python குறியீட்டிலிருந்து Co-op Translator ஐ அழிக்கத் தொடங்கினால் இங்கு தொடங்குங்கள்:

1. [Configuration](configuration.md) இல் விளக்கப்பட்டபடி ஒரு LLM வழங்குநரை அமைக்கவும், அல்லது Markdown அல்லது நோட்புக் துண்டுகளை மட்டும் host-agent மொழிபெயர்ப்புக்கு தயார் செய்கிறீர்களானால் இதைத் தவிர்க்கலாம்.
2. உங்கள் பயன்பrogram் கோப்பு I/O-வை கட்டுப்படுத்துகிறதா என்பதனை முடிவு செய்யவும்.
3. உங்கள் பயன்பrogram் தனித்தனி கோப்புகளை வாசித்து எழுதும் பொழுது content APIs-ஐ பயன்படுத்தவும்.
4. Co-op Translator CLI போல ஒரு சேமிப்பகத்தை செயலாக்க வேண்டும் என்றால் `run_translation` ஐ பயன்படுத்தவும்.
5. மாற்றியபிறகு நிரல்முறைச் செயல்களுக்கான தீர்மானமான சோதனைகள் தேவைப்பட்டால் `run_review` ஐ பயன்படுத்தவும்.

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

இந்தப் பணிமுறையைப் பயன்படுத்துங்கள் நீங்கள் ஏற்கனவே ஒரு கோப்பு, எடிட்டர் பஃபர், நோட்புக் பேலோட், MCP கோரிக்கை, அல்லது தனிப்பயன் பைப்லைன் உள்ளீட்டைக் கொண்டிருந்தால். உங்கள் குறியீடு கோப்பு I/O-வை கட்டுப்படுத்தும்:

1. மூல உள்ளடக்கத்தை வாசிக்கவும்.
2. ஒரு content translation API-ஐ அழைக்கவும்.
3. மொழிபெயர்க்கப்பட்ட உள்ளடக்கம் ஒரு திட்ட மொழிபெயர்ப்பு கோப்புறையில் எழுதப்படவிருந்தால் தவிர, வழிசெலுத்தல் மறுஅருமாற்றம் (path rewriting) API-ஐ விரைவில் அழைக்கலாம்.
4. உங்கள் பயன்பrogramில் இருந்து முடிவினை சேமிக்கவோ அல்லது திருப்பிவிடவோ செய்யவும்.

content translation APIs திட்டத் தேடலை இயக்கவோ, மெட்டாடேட்டாவை எழுதவோ, மறுதரிசனங்களை சேர்க்கவோ, இணைப்புகளை தானாக மறுஅருமாற்றம் செய்யவோ முடியாது.

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

மொழிபெயர்க்கப்பட்ட Markdown ஒரு Co-op Translator திட்ட அமைப்பில் থাকবে இல்லையெனில், `rewrite_markdown_paths` ஐ தவிர்த்து மொழிபெயர்க்கப்பட்ட ஸ்ட்ரிங்கை நேரடியாகச் சேமிக்கவும்.

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

`translate_notebook_content` Markdown செல்ஸ்களை மொழிபெயர்க்கிறது மற்றும் non-Markdown செல்ஸ்களை பாதுகாப்பு செய்கிறது. பாதை மறுஅருமாற்றம் yalnızca Markdown செல்ஸ்களுக்கு பொருந்தும்.

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

`translate_image_content` மூல படத்தை வாசித்து ஒரு ரசிக்கப்பட்ட `PIL.Image.Image` ஐ திருப்புகிறது. இது மொழிபெயர்க்கப்பட்ட பட மெட்டாடேட்டாவை எழுதாது.

## Scenario 2: Translate an Entire Repository

இந்தப் பணிமுறையைப் பயன்படுத்துங்கள் Python API `translate` CLI போன்று செயல்பட வேண்டும் என்று நீங்கள் விரும்பினால். `run_translation` ஆதரிக்கப்படும் கோப்புகளை கண்டறிகிறது, தேர்ந்தெடுக்கப்பட்ட உள்ளடக்கு வகைகளை மொழிபெயர்க்கிறது, பாதைகளை மறுஅருமாற்றம் செய்கிறது, வெளியீடு கோப்புகளை எழுதுகிறது, மெட்டாடேட்டாவை புதுப்பிக்கிறது, மற்றும் சுத்திகரிப்பு போன்ற பராமரிப்பு பணிகளை ஆற்றுகிறது.

`run_translation` புதிய திட்ட ஒருங்கிணைப்புக்கான பிரதான நுழைவாயிலாக பரிந்துரைக்கப்படுகிறது. `translate_project` அதே நடத்தையுடன் இணக்கத்திற்கான அலையஸ் ஆக ஏற்றுமதி செய்யப்படுகிறது.

தற்போதைய சேமிப்பகத்தில் Markdown கோப்புகளை கொரியனும் மற்றும் ஜப்பானீசும் மொழிகளில் மொழிபெயர்க்கவும்:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

ஒரு குறிப்பிட்ட project root-இலிருந்து மட்டும் நோட்புக்குகளை மொழிபெயர்க்கவும்:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

கோப்புகளை எழுதாமல் மொழிபெயர்ப்பு அளவீட்டை முன்னோட்டம் செய்யவும்:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

ஒரே அழைப்பில் பல உள்ளடக்க ரூட்டுகளை மொழிபெயர்க்கவும்:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

வெளியீட்டுகளை தெளிவான output குழுக்களில் எழுதவும்:

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

ஒவ்வொரு மொழிக்கும் ஒரு உட்புற அடைவை கொண்டிருக்க வேண்டும் என்றால் per-language placeholder ஐப் பயன்படுத்தவும்:

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

`markdown`, `notebook`, அல்லது `images` எதுவும் அமைக்கப்படவில்லை என்றால், API அனைத்து ஆதரிக்கப்படும் வகைகளையும் மொழிபெயர்க்கும்: Markdown, notebooks, மற்றும் images.

## Review Translated Output

`run_review` தீர்மானமான மொழிபெயர்ப்பு சோதனைகளை LLM அல்லது Vision அனுமதிகள் இல்லாமல் இயக்குகிறது.

!!! note "Beta"
    `run_review` ஒரு பேட்டா தீர்மானமான ரிவியூ API ஆகும். இது மாடல் வழங்குநர்களை அழைக்கவோ கோப்புகளை எழுதவோ செய்யாது, ஆனால் சோதனைகள் மற்றும் பிழை சடங்குகள் எதிர்காலத்தில் எழுந்து மாறக்கூடும்.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

மூல ref-வுடன் மாறியுள்ள கோப்புகள் மட்டுமே பரிசீலித்து GitHub-ஏனும் வடிவில் வெளியீட்டை அச்சிடவும்:

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

கோப்பு எழுதாமலே Markdown உள்ளடக்கத்தை மொழிபெயர்க்கவும்:

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

Markdown இணைப்புகளை மொழிபெயர்க்கவும் மற்றும் மறுஅருமாற்றம் செய்யவும்:

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

Python-இலிருந்து ஒரு சேமிப்பகத்தை மொழிபெயர்க்கவும்:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

பல ரூட்டுகளை மொழிபெயர்க்கவும்:

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

கோசாலரி சொற்களை பாதுகாத்து கொள்ளவும்:

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

Content translation APIs என்பது ஏற்கனவே உள்ளடக்கம் நினைவில் இருக்கின்ற ஒருங்கிணைப்புகள் (எ.கா., எடிட்டர் விரிவாக்கம், MCP கருவி, நோட்புக் செயலி, அல்லது தனிப்பயன் பைப் லைன்) இற்காக ஆகும்.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Translates Markdown content only. It does not rewrite links, write metadata, or append disclaimers. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Translates Markdown cells and preserves non-Markdown cells. It does not rewrite links, write metadata, or append disclaimers. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. Extracts and translates image text, then returns a rendered image. It does not save translated image metadata. |

`translate_markdown_content` மற்றும் `translate_notebook_content` ஒரு விருப்பமான `source_path`-ஐ அவர்களின் விருப்பங்களில் ஊதியமாக ஏற்றுக்கொள்கின்றன. பாதை மொழிபெயர்க்குநருக்கு சந்தர்ப்பமாக தரப்படுகிறது; மொழிபெயர்ப்பு முடிந்த பின்னர் எந்த திட்ட-சார்ந்த பாதை மறுஅருமாற்றத்திற்கும் அழைப்பாளர்கள் பொறுப்பேற்க வேண்டும்.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

அதே விருப்புகள் அகராதி (dictionary) களாகவும் கொடுக்கப்படலாம்:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

Agent-assisted APIs Co-op Translator-இலிருந்து Azure OpenAI அல்லது OpenAI-ஐ அழைக்காது. அவைகள் Markdown அல்லது நோட்புக் துண்டுகளை host agent-க்கு மொழிபெயர்ப்புக்கு தயார் செய்து, பின்னர் மொழிபெயர்க்கப்பட்ட துண்டுகளிலிருந்து இறுதி உள்ளடக்கத்தை மீள்கெடுக்கின்றன.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Return a self-contained Markdown job with chunks, prompts, and reconstruction state. |
| `finish_markdown_agent_translation` | Reconstruct Markdown from a job and host-agent translated chunks. |
| `start_notebook_agent_translation` | Return a notebook job with Markdown-cell chunks for host-agent translation. |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON while preserving code cells, outputs, and metadata. |

இந்த பணிமுறை முதன்மையாக MCP hosts க்கானது. நீங்கள் Co-op Translator வழங்குநர் அழைப்புகளை நிர்வகிக்கும் உற்பத்தியியல் சேமிப்பக மொழிபெயர்ப்பை தேவைப்படுமெனில், `translate_markdown_content`, `translate_notebook_content`, அல்லது `run_translation` ஐ பயன்படுத்தவும்.

## Path Rewriting APIs

Path மறுஅருமாற்ற APIs மொழிபெயர்ப்பு செய்கின்றன என்பது இல்லை. அவை இணைப்புகள் மற்றும் frontmatter பாதைகளை மாற்றுகின்றன அழைப்பாளர்கள் மூல பாதை, மொழிபெயர்க்கப்பட்ட இலக்கு பாதை, மற்றும் திட்ட ஒழுங்கை அறிந்த பிறகு.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Rewrites Markdown links and supported frontmatter path fields for a translated target. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Applies Markdown path rewriting to each Markdown cell and leaves non-Markdown cells unchanged. |

`policy` வாது (argument) இந்த புலங்களைக் கொண்ட ஒரு அகராதியாக இருக்கலாம்:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Target language code, such as `"ko"` or `"pt-BR"`. |
| `root_dir` | No | Source project root. Defaults to `"."`. |
| `translations_dir` | No | Text translation output directory. Defaults to `translations` under `root_dir`. |
| `translated_images_dir` | No | Translated image output directory. Defaults to `translated_images` under `root_dir`. |
| `translation_types` | No | Enabled translation types. Defaults to Markdown, notebooks, and images. |
| `lang_subdir` | No | Optional subdirectory under each language folder. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Space-separated target language codes, such as `"ko ja fr"`, or `"all"`. Alias codes are normalized to canonical BCP 47 values. |
| `root_dir` | `str` | `"."` | Project root for a single translation target. Ignored when `root_dirs` or `groups` are supplied. |
| `update` | `bool` | `False` | Delete and recreate existing translations for the selected languages. |
| `images` | `bool` | `False` | Include image translation. Requires Azure AI Vision configuration. |
| `markdown` | `bool` | `False` | Include Markdown translation. |
| `notebook` | `bool` | `False` | Include Jupyter notebook translation. |
| `debug` | `bool` | `False` | Enable debug logging. |
| `save_logs` | `bool` | `False` | Save DEBUG-level log files under the root `logs/` directory. |
| `yes` | `bool` | `True` | Auto-confirm prompts for programmatic and CI usage. |
| `add_disclaimer` | `bool` | `False` | Add machine translation disclaimers to translated Markdown and notebooks. |
| `translations_dir` | `str \| None` | `None` | Custom text translation output directory. Relative paths resolve against each root. |
| `image_dir` | `str \| None` | `None` | Custom translated image output directory. Relative paths resolve against each root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Multiple roots that share the same output settings. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit `(root_dir, translations_dir)` pairs. Takes precedence over `root_dirs`. |
| `repo_url` | `str \| None` | `None` | Repository URL used when rendering README language table guidance. |
| `glossaries` | `Iterable[str] \| None` | `None` | Glossary terms to preserve during translation. Duplicates and blank terms are normalized. |
| `dry_run` | `bool` | `False` | Estimate translation volume and preview migration behavior without writing files. |

## Review Parameters

`run_review` எண்ணமாக `run_translation` யின் கையொப்பத்தை (signature) சாத்தியமானவராக ஒத்துப்போக்குகிறது, இதனால் தானியங்கி முறைகள் translation மற்றும் review பணிமுறைகளுக்கு குறைந்த கிளைபிரிவுடன் மாறலாம்.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Target language folders to review. Space-separated strings and iterables are accepted. `"all"` reviews every discovered translation language. |
| `root_dir` | `str` | `"."` | Project root for a single review target. Ignored when `root_dirs` or `groups` are supplied. |
| `markdown` | `bool` | `False` | Include Markdown and MDX source files. |
| `notebook` | `bool` | `False` | Include Jupyter notebook source files. |
| `images` | `bool` | `False` | Reserved for parity with translation options. Link references to images are checked from Markdown. |
| `translations_dir` | `str \| None` | `None` | தனிப்பயன் உரை மொழிபெயர்ப்பு வெளியீட்டு அடைவு. சார்பான பாதைகள் ஒவ்வொரு root-க்கும் எதிரொலிக்கின்றன. |
| `root_dirs` | `Iterable[str] \| None` | `None` | அதே வெளியீட்டு அமைப்புகளை பகிரும் பல root-கள். |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | தெளிவான `(root_dir, translations_dir)` ஜோடிகள். இது `root_dirs` விட முன்னுரிமையடைகிறது. |
| `changed_from` | `str \| None` | `None` | மாற்றப்பட்ட மூல கோப்புகளுக்காக சீராய்வை வரம்புப்படுத்த பயன்படுத்தப்படும் Git ref. |
| `output_format` | `str` | `"text"` | சீராய்வு வெளியீட்டு வடிவம். ஆதரிக்கப்படும் மதிப்புகள் `"text"` மற்றும் `"github"`. |
| `fail_on_warnings` | `bool` | `False` | எச்சரவுகளை பிழைகளுடன் சேர்ந்து தோல்விகளாக கருதவும். |
| `debug` | `bool` | `False` | டீபக் பதிவுகளை செயல்படுத்தவும். |
| `save_logs` | `bool` | `False` | DEBUG மட்டத்தில் உள்ள பதிவு கோப்புகளை root `logs/` அடைவில் சேமிக்கவும். |

எந்த `markdown`, `notebook`, அல்லது `images` அமைக்கப்படவில்லை என்றால், API பொருத்தமான இடங்களில் Markdown, நோட்புக்-கள் மற்றும் படம் இணைப்பு குறிப்புகளை மதிப்பாய்வு செய்கிறது. சீராய்வு ஒரு LLM புரொவையிடரை அழைக்காது மற்றும் API சாவிகள் தேவையில்லை.

## கட்டமைப்பு தேவைகள்

புரொவையிடர் ஆதரவான மொழிபெயர்ப்பு API-கள் மொழிபெயர்ப்புக்கு முன் புரொவையிடர் கட்டமைப்பை தேவைப்படுத்துகின்றன:

- Markdown மற்றும் notebook மொழிபெயர்ப்பிற்கு LLM புரொவையிடர் வேண்டும். Azure OpenAI அல்லது OpenAI-இலொன்றை கட்டமைக்கவும்.
- பட மொழிபெயர்ப்பிற்கு LLM புரொவையிடருடன் கூடவே Azure AI Vision தேவை.
- `run_translation` திட்ட மொழிபெயர்ப்பு தொடங்குவதற்கு முன் குறைந்தளவிலான இணைப்பு பரிசோதனைகளை இயக்குகிறது.
- Agent-assisted `start_*_agent_translation` மற்றும் `finish_*_agent_translation` APIs Co-op Translator LLM புரொவையிடர்களை அழைக்காது. ஹோஸ்ட் பயன்பாடு அல்லது MCP முகவர் தயாரிக்கப்பட்ட துண்டுகளை மொழிபெயர்க்கும்.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, மற்றும் `run_review` தீர்மானமானவை மற்றும் புரொவையிடர் அங்கீகாரங்களைத் தேவையாக்காது.

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

`run_review` தீர்மானமானது மற்றும் Azure OpenAI, OpenAI, அல்லது Azure AI Vision கட்டமைப்பை தேவையாக்காது.

## நடத்தல் குறிப்புகள்

- உள்ளடக்க மொழிபெயர்ப்பு API-கள் மொழிபெயர்ப்பை திட்ட பாதை மறுஅவர்த்தனத்திலிருந்து தனித்துப் பராமரிக்கின்றன. மொழிபெயர்க்கப்பட்ட உள்ளடக்கம் இலக்கு இடத்திற்காக திட்ட சார்ந்த இணைப்புகளை சரிசெய்ய வேண்டுமானால், தெளிவாக `rewrite_markdown_paths` அல்லது `rewrite_notebook_paths` ஐ அழைக்கவும்.
- திட்ட ஒழுங்குபடுத்தல் API-கள் உள்ளடக்க மொழிபெயர்ப்பின் சுற்றுச்சூழலில் திட்ட நடத்தையைச் சேர்க்கின்றன; அதில் கோப்பு கண்டறிதல், எழுதுதல், பாதை மறுஅவர்த்தனை, மெட்டாடேட்டா, சுத்திகரிப்பு, மற்றும் விருப்பமான விளக்கக் குறிப்புகள் ஆகியவை உட்பட.
- `run_translation` Click மூலம் முன்னேற்றம் மற்றும் மதிப்பீட்டு சுருக்கங்களை அச்சிடுகிறது, CLI பயனர் அனுபவத்துடன் பொருந்துகிறது.
- `dry_run=True` மெய்நிகர் README புதுப்பிப்புகளைப் பயன்படுத்தி மதிப்பீடுகளை கணக்கிடுகிறது, ஆனால் README அல்லது மொழிபெயர்ப்பு கோப்புகளை எழுதாது.
- `groups` ஒற்றுமையாக செயலாக்கப்படுகின்றன. பணிகள் தொடங்குவதற்கு முன்னரே ஒரு ஒட்டுமொத்த மதிப்பீடு அச்சிடப்படுகிறது.
- பட மொழிபெயர்ப்பு தேர்ந்தெடுக்கப்பட்டால், Vision கட்டமைப்பு காணாமல் இருந்தால் மொழிபெயர்ப்பு தொடங்குவதற்கு முன் பிழை எழுப்பப்படும்.
- உள்ளிருக்கும் alias-அடிப்படையிலான மொழி அடைவுகள் கண்டறியப்பட்டு ஓட்டத்தின் ஒரு பகுதியாக canonical மொழி அடைவு பெயர்களுக்கு இடம்பெயர்க்கப்படலாம்.
- `run_review` மொழிபெயர்க்கப்பட்ட கோப்புகள் காணாமல் இருப்பது, மொழிபெயர்ப்பு மெட்டாடேட்டா காணாமல் இருப்பது அல்லது பழையதானது, தவறுபட்ட Markdown frontmatter/code fences, மற்றும் தவறான மொழிபெயரிக்கப்பட்ட notebook JSON ஆகியவற்றில் தோல்வியடையும்.
- `run_review` இயல்பாக உள்ளூர் Markdown மற்றும் பட இணைப்பு இலக்குகளை காணாமல் இருப்பதை எச்சரிப்புகளாக அறிவிக்கிறது.

## உள்ளக அழைப்பு பாதை

API CLI பயன்படுத்தப்படும் அதே கோர் செயலாக்கத்திற்கு ஒப்படைக்கிறது:

மொழிபெயர்ப்பு:

1. நினைவகத்தில் மொழிபெயர்ப்பிற்காக `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, அல்லது `translate_image_content`.
2. தெளிவான பாதை பின்-செயலாக்கத்திற்கு `co_op_translator.api.translation.rewrite_markdown_paths` அல்லது `rewrite_notebook_paths`.
3. முழு திட்ட ஒழுங்கமைப்பிற்கு `co_op_translator.api.translation.run_translation`.
4. `co_op_translator.config.Config`, `LLMConfig`, மற்றும் `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Markdown, notebook, மற்றும் படங்களுக்கு குறித்த நோக்கிலோடு திட்ட மொழிபெயர்ப்பு மிக்சின்கள்.
8. `co_op_translator.core` கீழ் Markdown, notebook, text, மற்றும் image மொழிபெயர்ப்பிகள்.

மதிப்பாய்வு:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. `co_op_translator.review.checks` கீழ் தீர்மானமான சோதனைகள்

பதிவாளர்களுக்கு பயனுள்ள பின்வரும் வகைகள் உள்ளன, ஆனால் அவை package-நிலை நிலையான API ஆக ஏற்றுமதி செய்யப்படவில்லை.

| வகுப்பு | மாட்யூல் | பொறுப்பு |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | திட்ட நிலை மொழிபெயர்ப்பு, அடைவு மேலாண்மை, மொழி-தொகைக்கு இணக்கமான மெட்டாடேட்டா ஒருமைப்படுத்தல், மற்றும் Markdown, notebook, மற்றும் image மொழிபெயர்ப்பிகளுக்கு பணியை ஒப்படைப்பு. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, notebook, படங்கள், பழையதானதைக் கண்டறிதல், மற்றும் மொழிபெயர்ப்பு மெட்டாடேட்டா புதுப்பிப்புகளுக்கான அசிங்க் கோப்பு செயலாக்க பணிகளை நிறைவேற்றுகிறது. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown கோப்புகளை வாசித்தல், உள்ளடக்க மொழிபெயர்ப்பு, பாதை மறுஅவர்த்தனை, மெட்டாடேட்டா, விளக்கக் குறிப்புகள், மற்றும் எழுதுதல்களை ஒருங்கிணைக்கிறது. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | notebook கோப்புகளை வாசித்தல், Markdown செல்களின் மொழிபெயர்ப்பு, பாதை மறுஅவர்த்தனை, மெட்டாடேட்டா, விளக்கக் குறிப்புகள், மற்றும் எழுதுதல்களை ஒருங்கிணைக்கிறது. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | மூலப் பட கண்டறிதல், பட மொழிபெயர்ப்பு, வெளியீட்டு பாதைகள், மெட்டாடேட்டா மற்றும் எழுதுதல்களை ஒருங்கிணைக்கிறது. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | மொழிபெயர்க்கப்பட்ட Markdown ஜோடிகளை கண்டறிந்து, மொழிபெயர்ப்பு தரத்தை மதிப்பீடு செய்து, குறைந்த நம்பகத்தன்மை திருத்த பணிகளுக்கான நம்பிக்கை மெட்டாடேட்டாவை வாசிக்கிறது. |
| `ReviewRunner` | `co_op_translator.review.runner` | மூல கோப்புகள், இலக்கு மொழிகள், மற்றும் கட்டமைக்கப்பட்ட மொழிபெயர்ப்பு ரூட்டுகள் இடையே தீர்மானமான சீராய்வு சோதனைகளை ஒழுங்குபடுத்துகிறது. |
| `ReviewTarget` | `co_op_translator.review.targets` | ஒரு மூல root மற்றும் அந்த root க்கான மதிப்பாய்வு செய்யப்பட்ட மொழிபெயர்ப்பு வெளியீட்டு அடைவை விவரிக்கிறது. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | பழைய alias மொழி அடைவுகளை கண்டறிந்து canonical BCP 47 அடைவுகளுக்கான இடம்பெயர்ப்பு திட்டங்களை தயாரிக்கிறது. |
| `Config` | `co_op_translator.config.base_config` | `.env` கோப்புகளை ஏற்றுகிறது மற்றும் தேவையான LLM மற்றும் விருப்பமான Vision புரொவையிடர்கள் கட்டமைக்கப்பட்டுள்ளனவா என சரிபார்க்கிறது. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI அல்லது OpenAI-ஐ தன்னிச்சையாக கண்டறிகிறது, தேவையான சூழல் மாறிகளை சரிபார்க்கிறது, மற்றும் புரொவையிடர் இணைப்பு பரிசோதனைகள் நடத்துகிறது. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision கட்டமைப்பை கண்டறிந்து பட மொழிபெயர்ப்பிற்கான இணைப்பு பரிசோதனைகளை இயக்குகிறது. |