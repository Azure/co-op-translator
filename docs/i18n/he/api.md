# API של Python

ממשק ה-Python הציבורי היציב מיוצא מ-`co_op_translator.api`. רוב האינטגרציות משתמשות באחד מהזרימות העבודה האלה:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Your application reads source content, calls Co-op Translator for translation, and decides where to save the result. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Your MCP host or application model will translate chunks, while Co-op Translator handles chunking and reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | You want the Python API to behave like the CLI and handle discovery, output paths, metadata, cleanup, and writes. | `run_translation` |

רוב המודולים ברמת הבסיס תחת `core`, `config`, `review`, ו-`utils` הם פרטי מימוש המשמשים את נקודות הכניסה של ה-API האלה.

לקוחות MCP משתמשים באותו ממשק ציבורי דרך ה-[MCP Server](mcp.md). השתמש בעמוד זה כאשר אתה קורא ל-Python ישירות, ובמדריך ה-MCP כשאתה חושף את Co-op Translator לסוכן או לעורך. אם אתה מתלבט בין CLI, ממשק Python, ו-MCP, התחל ב-[Choose Your Workflow](workflows.md).

## זרימת שימוש ראשונה ב-API

התחל כאן אם אתה קורא ל-Co-op Translator מתוך קוד Python:

1. קנפג ספק LLM כפי שמתואר ב-[Configuration](configuration.md), אלא אם כן אתה רק מכין קטעי Markdown או פנקסי פתקים להתרגום על ידי מארח-סוכן.
2. החלט האם האפליקציה שלך אחראית על קלט/פלט קבצים.
3. השתמש ב-APIs לתוכן כשהאפליקציה שלך קוראת וכותבת קבצים בודדים.
4. השתמש ב-`run_translation` כאשר Co-op Translator אמור לעבד מאגר כמו ה-CLI.
5. השתמש ב-`run_review` אחרי תרגום אם אתה צריך בדיקות דטרמיניסטיות באוטומציה.

| Goal | API to start with |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## תרחיש 1: לתרגם קבצים או מסמכים בודדים

השתמש בזרימת עבודה זו כאשר כבר יש לך קובץ, חוצץ עורך, payload של פנקס, בקשת MCP, או קלט צינור מותאם. הקוד שלך אחראי על I/O של קבצים:

1. קרא את תוכן המקור.
2. קרא ל-API לתרגום תוכן.
3. אם רוצים, קרא ל-API לשכתוב נתיבי קישורים אם התוכן המתורגם ייכתב לתיקיית תרגום בפרויקט.
4. שמור או החזר את התוצאה מהאפליקציה שלך.

APIs לתרגום תוכן אינם מריצים גילוי פרויקט, אינם כותבים מטא-נתונים, אינם מוסיפים הצהרות אחריות, ואינם משנים קישורים אוטומטית.

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

אם ה-Markdown המתורגם לא יחיה במבנה פרויקט של Co-op Translator, דלג על `rewrite_markdown_paths` ושמור את המחרוזת המתורגמת ישירות.

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

`translate_notebook_content` מתרגם תאי Markdown ושומר על תאים שאינם Markdown ללא שינוי. שכתוב נתיבים מוחל רק על תאי Markdown.

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

`translate_image_content` קורא את תמונת המקור ומחזיר `PIL.Image.Image` מעובדת. הוא אינו כותב מטא-נתונים של תמונה מתורגמת.

## תרחיש 2: לתרגם מאגר שלם

השתמש בזרימת עבודה זו כאשר אתה רוצה שממשק ה-Python יתנהג כמו ה-CLI `translate`. `run_translation` מגלה קבצים נתמכים, מתרגם סוגי תוכן נבחרים, משכתב נתיבים, כותב קבצי פלט, מעדכן מטא-נתונים, ומבצע משימות תחזוקת תרגום כגון ניקוי.

`run_translation` הוא נקודת הכניסה המועדפת לאורקסטרציה של פרויקטים. `translate_project` מיוצא כ_ALIAS_ תאימות עם אותו התנהגות.

תרגם קבצי Markdown במאגר הנוכחי לקוריאנית ויפנית:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

תרגם רק פנקסים משורש פרויקט ספציפי:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

הצג בכמה ייעננו תרגום בלי לכתוב קבצים:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

תרגם מספר שורשים בשיחה אחת:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

כתוב תרגומים לקבוצות פלט מפורשות:

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

השתמש במיקום-ממלא לכל שפה כאשר כל שפה צריכה להכיל ספרייה פנימית מקוננת:

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

אם אף אחד מהשדות `markdown`, `notebook`, או `images` לא מוגדרים, ה-API יתמוך בכל הסוגים הנתמכים: Markdown, פנקסים ותמונות.

## בדיקת פלט מתורגם

`run_review` מריץ בדיקות תרגום דטרמיניסטיות ללא אישורי LLM או Vision.

!!! note "Beta"
    `run_review` הוא API ביקורת דטרמיניסטי בגרסת בטא. הוא אינו קורא לספקי מודלים ואינו כותב קבצים, אך המבדקים וסקימות הבעיות עשויים להשתנות.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

בדוק רק קבצים ששונו ביחס ל-ref בסיס והדפס פלט בפורמט GitHub-flavored:

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

## דוגמאות API להעתקה והדבקה

תרגם תוכן Markdown ללא כתיבה לקבצים:

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

תרגם ושכתב קישורי Markdown:

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

תרגם מאגר מתוך Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

תרגם שורשים מרובים:

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

שמור מונחי מונחון (glossary):

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

## נקודות כניסה ציבוריות

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

## APIs לתרגום תוכן

APIs לתרגום תוכן מיועדים לאינטגרציות שכבר מחזיקות תוכן בזיכרון, כגון תוסף עורך, כלי MCP, מעבד פנקסים, או צינור מותאם אישית.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Translates Markdown content only. It does not rewrite links, write metadata, or append disclaimers. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Translates Markdown cells and preserves non-Markdown cells. It does not rewrite links, write metadata, or append disclaimers. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. Extracts and translates image text, then returns a rendered image. It does not save translated image metadata. |

`translate_markdown_content` ו-`translate_notebook_content` מקבלות דרך האופציות `source_path` אופציונלי. הנתיב מועבר כקונטקסט למתרגם; המתקשרים נשארים אחראים לכל שכתוב נתיבים ספציפי לפרויקט לאחר התרגום.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

אותן אפשרויות ניתנות גם כ-מילונים:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## APIs בסיוע סוכן

APIs בסיוע סוכן אינם קוראים ל-Azure OpenAI או ל-OpenAI מתוך Co-op Translator. הם מכינים קטעי Markdown או פנקסים לתרגום על ידי סוכן מארח, ואז משחזרים את התוכן הסופי מתוך הקטעים המתורגמים.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Return a self-contained Markdown job with chunks, prompts, and reconstruction state. |
| `finish_markdown_agent_translation` | Reconstruct Markdown from a job and host-agent translated chunks. |
| `start_notebook_agent_translation` | Return a notebook job with Markdown-cell chunks for host-agent translation. |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON while preserving code cells, outputs, and metadata. |

זרימת עבודה זו מיועדת בעיקר למארחי MCP. אם אתה צריך תרגום מאגר בפרודקשן עם Co-op Translator שמנהל קריאות לספקים, השתמש ב-`translate_markdown_content`, `translate_notebook_content`, או `run_translation`.

## APIs לשכתוב נתיבים

APIs לשכתוב נתיבים אינם מבצעים תרגום. הם מעדכנים קישורים ושדות frontmatter לאחר שהמתקשרים יודעים את נתיב המקור, נתיב היעד המתורגם, ומבנה הפרויקט.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Rewrites Markdown links and supported frontmatter path fields for a translated target. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Applies Markdown path rewriting to each Markdown cell and leaves non-Markdown cells unchanged. |

הארגומנט `policy` עשוי להיות מילון עם השדות האלה:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Target language code, such as `"ko"` or `"pt-BR"`. |
| `root_dir` | No | Source project root. Defaults to `"."`. |
| `translations_dir` | No | Text translation output directory. Defaults to `translations` under `root_dir`. |
| `translated_images_dir` | No | Translated image output directory. Defaults to `translated_images` under `root_dir`. |
| `translation_types` | No | Enabled translation types. Defaults to Markdown, notebooks, and images. |
| `lang_subdir` | No | Optional subdirectory under each language folder. |

## פרמטרים לתרגום פרויקט

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

## פרמטרים לבדיקה

`run_review` מתוכנן לשקף בכוונה את חתימת `run_translation` ככל האפשר כדי שאוטומציה תוכל להחליף בין זרימות תרגום וביקורת עם מינימום הסתעפויות.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Target language folders to review. Space-separated strings and iterables are accepted. `"all"` reviews every discovered translation language. |
| `root_dir` | `str` | `"."` | Project root for a single review target. Ignored when `root_dirs` or `groups` are supplied. |
| `markdown` | `bool` | `False` | Include Markdown and MDX source files. |
| `notebook` | `bool` | `False` | Include Jupyter notebook source files. |
| `images` | `bool` | `False` | Reserved for parity with translation options. Link references to images are checked from Markdown. |
| `translations_dir` | `str \| None` | `None` | תיקיית פלט מותאמת לתרגום טקסט. נתיבים יחסיים מפורשים ביחס לכל שורש. |
| `root_dirs` | `Iterable[str] \| None` | `None` | שורשי מקור מרובים שמשתפים את אותן הגדרות פלט. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | זוגות מפורשים `(root_dir, translations_dir)`. תופסים עדיפות על פני `root_dirs`. |
| `changed_from` | `str \| None` | `None` | הפניה ב-Git המשמשת להגבלת הבדיקה לקבצי מקור ששונו. |
| `output_format` | `str` | `"text"` | פורמט פלט הבדיקה. הערכים הנתמכים הם `"text"` ו-`"github"`. |
| `fail_on_warnings` | `bool` | `False` | להתייחס לאזהרות ככישלון בנוסף לשגיאות. |
| `debug` | `bool` | `False` | הפעלת רישומי דיבוג. |
| `save_logs` | `bool` | `False` | שמור קבצי לוג ברמת DEBUG תחת ספריית השורש `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## דרישות תצורה

ממשקי ה-API לתרגום המבוססים על ספק דורשים תצורת ספק לפני התרגום:

- Markdown and notebook translation require an LLM provider. Configure either Azure OpenAI or OpenAI.
- Image translation requires Azure AI Vision in addition to the LLM provider.
- `run_translation` runs lightweight connectivity checks before project translation begins.
- Agent-assisted `start_*_agent_translation` and `finish_*_agent_translation` APIs do not call Co-op Translator LLM providers. The host application or MCP agent translates the prepared chunks.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, and `run_review` are deterministic and do not require provider credentials.

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

## הערות על ההתנהגות

- ממשקי ה-API לתרגום תוכן מפרידים בין התרגום לבין שכתוב נתיבי הפרויקט. קראו במפורש ל-`rewrite_markdown_paths` או `rewrite_notebook_paths` כאשר יש להתאים קישורים יחסיים לפרויקט למיקום יעד.
- ממשקי האורקסטרציה של הפרויקט מוסיפים התנהגות פרויקטית סביב תרגום התוכן, כולל גילוי קבצים, כתיבות, שכתוב נתיבים, מטא-דאטה, ניקוי והצהרות ויתור אופציונליות.
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

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` עבור תרגום בזיכרון.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` לעיבוד נתיבים מפורש לאחר מכן.
3. `co_op_translator.api.translation.run_translation` לתזמור מלא של הפרויקט.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. מיקסינים ממוקדים לתרגום פרויקט עבור Markdown, notebooks, ותמונות.
8. מתרגמי Markdown, notebook, טקסט ותמונות תחת `co_op_translator.core`.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. בדיקות דטרמיניסטיות תחת `co_op_translator.review.checks`

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| מחלקה | מודול | אחריות |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | מתאם תרגום ברמת הפרויקט, ניהול תיקיות, נירמול מטא-נתונים לפי שפה, והפניה למתרגמי Markdown, notebook, ותמונות. |
| `TranslationManager` | `co_op_translator.core.project.translation` | מבצע את עבודת העיבוד האסינכרוני של קבצים עבור Markdown, notebooks ותמונות, גילוי תוכן מיושן, ועדכוני מטא-נתוני תרגום. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | מתזמר קריאות קבצי Markdown, תרגום תוכן, שכתוב נתיבים, מטא-דאטה, הצהרות ויתור, וכתיבות. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | מתזמר קריאות קבצי notebook, תרגום תאי Markdown, שכתוב נתיבים, מטא-דאטה, הצהרות ויתור, וכתיבות. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | מתזמר גילוי תמונות מקור, תרגום תמונות, נתיבי פלט, מטא-דאטה, וכתיבות. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | מוצא זוגות Markdown מתורגמים, מעריך איכות התרגום, וקורא מטא-נתוני אמינות עבור זרימות עבודה לתיקון תרגומים בעלי אמינות נמוכה. |
| `ReviewRunner` | `co_op_translator.review.runner` | מתאם בדיקות סקירה דטרמיניסטיות על פני קבצי מקור, שפות יעד, ושורשי תרגום מוגדרים. |
| `ReviewTarget` | `co_op_translator.review.targets` | מתאר שורש מקור ואת ספריית פלט התרגום הנבדקת עבור שורש זה. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | מאתר תיקיות שפה ישנות המבוססות על כינויים ומכין תוכניות העברה לשמות תיקיות שפה קנוניים לפי BCP 47. |
| `Config` | `co_op_translator.config.base_config` | טוען קבצי `.env` ובודק האם ספקי LLM הנדרשים וספקי Vision האופציונליים מוגדרים. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | מאתר אוטומטית Azure OpenAI או OpenAI, מאמת משתני סביבה נדרשים, ומריץ בדיקות חיבור לספק. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | מאתר תצורת Azure AI Vision ומריץ בדיקות חיבור לתרגום תמונות. |