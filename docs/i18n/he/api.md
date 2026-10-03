# ממשק ה-API של Python

הממשק הציבורי היציב של Python מיוצא מ-`co_op_translator.api`. רוב האינטגרציות משתמשות באחד מהזרימות עבודה האלה:

| תרחיש | השתמש בזה כאשר | ממשקי API עיקריים |
| --- | --- | --- |
| תרגם קבצים או מסמכים בודדים | היישום שלך קורא את התוכן המקורי, קורא ל-Co-op Translator עבור תרגום, ומחליט היכן לשמור את התוצאה. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| הכן תוכן לתרגום על ידי סוכן המאכסן | המארח MCP שלך או מודל היישום יתרגם את החלקים, בעוד Co-op Translator מטפל בחיתוך החלקים ובשחזור. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| תרגם מאגר שלם | אתה רוצה שממשק ה-Python יתנהג כמו ה-CLI ויטפל בגילוי קבצים, נתיבי פלט, מטא־דאטה, ניקוי וכתיבה. | `run_translation` |

רוב המודולים ברמת הנמוכה תחת `core`, `config`, `review`, ו-`utils` הם פרטי מימוש המשמשים את נקודות הכניסה הללו של ה-API.

לקוחות MCP משתמשים באותו ממשק ציבורי דרך [שרת MCP](mcp.md). השתמש בעמוד הזה כשקוראים ל-Python ישירות, ובמדריך ה-MCP כאשר חושפים את Co-op Translator לסוכן או לעורך. אם אתה מחליט בין CLI, ממשק ה-Python ו-MCP, התחל ב-[בחר את זרימת העבודה שלך](workflows.md).

## זרימת ה-API בפעם הראשונה

התחל כאן אם אתה קורא ל-Co-op Translator מתוך קוד Python:

1. קבע ספק LLM כפי שמתואר ב-[תצורה](configuration.md), אלא אם אתה רק מכין קטעי Markdown או מחברת לתרגום על ידי הסוכן־המארח.
2. החלט האם היישום שלך מנהל קלט/פלט של קבצים.
3. השתמש בממשקי תוכן כאשר היישום שלך קורא וכותב קבצים בודדים.
4. השתמש ב-`run_translation` כאשר Co-op Translator אמור לעבד מאגר בדומה ל-CLI.
5. השתמש ב-`run_review` אחרי תרגום אם אתה צריך בדיקות דטרמיניסטיות באוטומציה.

| מטרה | ממשק ה-API להתחיל איתו |
| --- | --- |
| תרגם מחרוזת Markdown או קובץ בודד | `translate_markdown_content` |
| תרגם מטען מחברת בודדת | `translate_notebook_content` |
| תרגם תמונה אחת | `translate_image_content` |
| אפשר לסוכן־מארח לתרגם קטעי Markdown או מחברת | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| שכתב קישורים מתורגמים לאחר בחירת נתיב פלט | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| תרגם מאגר שלם | `run_translation` |
| סקור פלט מתורגם | `run_review` |

## תרחיש 1: תרגום קבצים או מסמכים בודדים

השתמש בזרימת עבודה זו כאשר כבר יש לך קובץ, חוצץ עורך, מטען מחברת, בקשת MCP, או קלט צינור מותאם אישית. הקוד שלך מנהל את קלט/פלט הקבצים:

1. קרא את תוכן המקור.
2. קרא לממשק API לתרגום תוכן.
3. במידת הצורך קרא לממשק API לשכתוב נתיבים אם התוכן המתורגם יישמר בתיקיית תרגומים של הפרויקט.
4. שמור או החזר את התוצאה מהיישום שלך.

ממשקי ה-API לתרגום תוכן אינם מבצעים גילוי פרויקט, אינם כותבים מטא־דאטה, אינם מוסיפים הצהרות נלוות, ואינם משכתבים קישורים אוטומטית.

### קובץ Markdown

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

אם Markdown המתורגם לא יחיה במבנה פרויקט של Co-op Translator, דלג על `rewrite_markdown_paths` ושמור את המחרוזת המתורגמת ישירות.

### קובץ מחברת

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

`translate_notebook_content` מתרגם תאי Markdown ושומר על תאים שאינם Markdown. שכתוב נתיבים מוחל רק על תאי Markdown.

### קובץ תמונה

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

`translate_image_content` קורא את תמונת המקור ומחזיר `PIL.Image.Image` מרונדרת. הוא אינו כותב מטא־דאטה של תמונה מתורגמת.

## תרחיש 2: תרגום מאגר שלם

השתמש בזרימת עבודה זו כאשר אתה רוצה שממשק ה-Python יתנהג כמו ה-CLI של `translate`. `run_translation` מגלה קבצים נתמכים, מתרגם סוגי תוכן נבחרים, משכתב נתיבים, כותב קבצי פלט, מעדכן מטא־דאטה, ומבצע משימות תחזוקת תרגום כגון ניקוי.

`run_translation` הוא נקודת הכניסה המועדפת לאורקסטרציית פרויקט. `translate_project` מיוצא ככינוי תאימות עם אותה התנהגות.

תרגם קבצי Markdown במאגר הנוכחי לקוריאנית וליפנית:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

תרגם רק מחברות מתוך שורש פרויקט מסוים:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

הצג תצוגה מקדימה של כמות התרגום ללא כתיבת קבצים:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

הקלט אירועי התקדמות מובנים עבור אינטגרציה:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # אחסן את המטען בטבלת אירועי העבודה שלך או הזרם אותו לממשק המשתמש שלך.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

האירועים משתמשים בסכמה מבוססת גרסה `co-op.translation.event.v1`. אינטגרציות צריכות
להסתמך על שדות יציבים כגון `type` ו-`stage_key`, ולא על טקסט שפונה לבני אדם
בקונסולה או על `stage_label`.

תרגם מספר שורשי תוכן בקריאה אחת:

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

השתמש בממלא מקום לכל שפה כאשר כל שפה צריכה להכיל תיקייה מקוננת:

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

אם אף אחד מהאפשרויות `markdown`, `notebook`, או `images` לא מוגדרות, ה-API מתרגם את כל סוגי הקבצים הנתמכים: Markdown, מחברות, ותמונות.

### שמירת עריכות אנושיות מאושרות בעזרת ספק מצב תרגום

כברירת מחדל, Co-op Translator שומר על ההתנהגות הקיימת ברמת הקובץ: כאשר
מקור Markdown מיושן, כל הקובץ המתורגם מתחדש. אינטגרציות מתארחות
יכולות להעביר באופן אופציונלי `TranslationStateProvider` כדי לשמר
עריכות אנושיות בבלוקים מקורים שלא השתנו.

הספק מספק את זוג המקור/המטרה האחרון שהתקבל ורושם כל חדש
מועמד. האישור נשאר באחריות האינטגרציה—למשל,
לאחר מיזוג בקשת משיכה לתרגום:

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

עבור קבצי Markdown עם בסיס מקובל תקף, Co-op Translator מיישר
בלוקים של Markdown ברמה העליונה. בלוקים מקור שלא השתנו משתמשים מחדש בבלוקים המתורגמים הנוכחיים
כולל עריכות שבוצעו על ידי אנשים; בלוקים מקור ששונו או נוספו נשלחים
לתרגום; בלוקים מקור שנמחקו מוסרים. אם היישור אינו חד־משמעי,
מבנה המטרה השתנה, תרגום בלוק אינו תקף, או אין בסיס תקף,
זמין, Co-op Translator נופל בבטחה חזרה לנתיב התרגום המלא הקיים.
נתיב התרגום.

ממשק ה-API הזה מאחסן מצב תרגום של מסמך, ולא זיכרון תרגום של ביטויים או
קטעים חוצי־מסמכים. זה חל כרגע על תרגום פרויקטי Markdown.
התנהגות מחברות ותמונות ללא שינוי. העברת `update=True`
עדיין מבקשת חידוש מלא.

אם לא ניתן לתרגם קובץ או יותר, `run_translation` מעלה חריגת
`RuntimeError` לאחר סיום זרימת העבודה של הפרויקט במקום לדווח על ריצה
מוצלחת עם פלט חסר. אינטגרציות צריכות להתייחס לזה כעבודה שנכשלה
ולשמור את מצב התרגום המקובל הקודם.

## סקירת פלט מתורגם

`run_review` מפעיל בדיקות תרגום דטרמיניסטיות ללא אישורי LLM או Vision.

!!! note "בטא"
    `run_review` הוא ממשק סקירה דטרמיניסטי בגרסת בטא. הוא אינו קורא לספקי מודלים או כותב קבצים, אך סכמות הבדיקות והבעיות עשויות להתפתח.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

לאחר תרגום הכולל רק README, השתמש באותו תחום לסקירה:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` מספק סקירה רק של `README.md` תחת כל שורש מקור שהוגדר,
כולל `groups` מותאמים ותיקיות פלט. מסמכים אחרים ו-READMEים מקוננים
מוחרגים. חוסר README מקור מעלה `ValueError`; בדיקות תרגום שנכשלו
מעלות `RuntimeError`.

סקור רק קבצים ששונו ביחס לבסיס הפניה והדפס פלט בסגנון GitHub:

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

תרגם תוכן Markdown ללא כתיבת קבצים:

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

תרגם מספר שורשים:

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

שמור מונחי מילון:

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

## ממשקי API לתרגום תוכן

ממשקי ה-API לתרגום תוכן מיועדים לאינטגרציות שכבר מחזיקות תוכן בזיכרון, כגון תוסף עורך, כלי MCP, מעבד מחברות, או צינור מותאם אישית.

| פונקציה | קלט | פלט | קלט/פלט קבצים | הערות |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | אסינכרוני. מתרגם רק תוכן Markdown. אינו משכתב קישורים, אינו כותב מטא־דאטה, ואינו מוסיף הצהרות נלוות. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | אסינכרוני. מתרגם תאי Markdown ומשמר תאים שאינם Markdown. אינו משכתב קישורים, אינו כותב מטא־דאטה, ואינו מצרף הצהרות נלוות. |
| `translate_image_content` | נתיב תמונה | `PIL.Image.Image` | קורא רק את תמונת המקור | סינכרוני. מוציא ומתרגם טקסט מתמונה, ואז מחזיר תמונה מרונדרת. אינו שומר מטא־דאטה של תמונה מתורגמת. |

`translate_markdown_content` ו-`translate_notebook_content` מקבלים `source_path` אופציונלי דרך האפשרויות שלהם. הנתיב נמסר כהקשר למתרגם; המתקשרים נשארים אחראים על כל שכתוב נתיבים ספציפי לפרויקט לאחר התרגום.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

אותן אפשרויות ניתנות למסירה גם כמילונים (dictionaries):

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## ממשקי API לתרגום בסיוע סוכן

ממשקי API בסיוע סוכן אינם קוראים לספק LLM המוגדר מתוך Co-op Translator. הם מכינים חלקי Markdown או מחברת עבור סוכן־מארח שיתרגם אותם, ולאחר מכן משחזרים את התוכן הסופי מהחלקים המתורגמים.

| פונקציה | מטרה |
| --- | --- |
| `start_markdown_agent_translation` | החזר משימה עצמאית של Markdown עם חלקים, הנחיות, ומצב שחזור. |
| `finish_markdown_agent_translation` | שחזר Markdown ממטלה ומהחלקים המתורגמים על ידי הסוכן המארח. |
| `start_notebook_agent_translation` | החזר משימת מחברת עם חלקי תאי Markdown לתרגום על ידי הסוכן המארח. |
| `finish_notebook_agent_translation` | שחזר JSON של מחברת תוך שמירה על תאי קוד, פלטים, ומטא־דאטה. |

זרימת עבודה זו מיועדת בעיקר למארחי MCP. אם אתה צריך תרגום מאגר יצרני כאשר Co-op Translator מנהל קריאות לספקים, השתמש ב-`translate_markdown_content`, `translate_notebook_content`, או `run_translation`.

## ממשקי API לשכתוב נתיבים

ממשקי ה-API לשכתוב נתיבים אינם מבצעים תרגום. הם מעדכנים קישורים ונתיבי frontmatter לאחר שהמתקשרים יודעים את נתיב המקור, נתיב היעד המתורגם, ומבנה הפרויקט.

| פונקציה | היקף | הערות |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | משכתב קישורי Markdown ושדות נתיב ב-frontmatter הנתמכים עבור יעד מתורגם. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | מיישם שכתוב נתיבים של Markdown על כל תא Markdown ומשאיר תאים שאינם Markdown ללא שינוי. |

הארגומנט `policy` יכול להיות מילון עם השדות האלה:

| שדה | נדרש | מטרה |
| --- | --- | --- |
| `language_code` | כן | קוד שפת יעד, כגון `"ko"` או `"pt-BR"`. |
| `root_dir` | לא | שורש פרויקט המקור. ברירת המחדל היא `"."`. |
| `translations_dir` | לא | תיקיית פלט לתרגום טקסט. ברירת המחדל היא `translations` תחת `root_dir`. |
| `translated_images_dir` | לא | תיקיית פלט לתמונות מתורגמות. ברירת המחדל היא `translated_images` תחת `root_dir`. |
| `translation_types` | לא | סוגי תרגום מופעלים. ברירת המחדל היא Markdown, מחברות, ותמונות. |
| `lang_subdir` | לא | תת־תיקיה אופציונלית תחת כל תיקיית שפה. |

## פרמטרים לתרגום פרויקט

| פרמטר | סוג | ברירת מחדל | מטרה |
| --- | --- | --- | --- |
| `language_codes` | `str` | נדרש | קודי שפה יעד מופרדים ברווח, כגון `"ko ja fr"` או `"all"`. קודי כינויים מנורמלים לערכי BCP 47 קנוניים. |
| `root_dir` | `str` | `"."` | שורש הפרויקט עבור יעד תרגום יחיד. מתעלם כאשר `root_dirs` או `groups` מסופקים. |
| `update` | `bool` | `False` | מחק ויצור מחדש תרגומים קיימים עבור השפות הנבחרות. |
| `images` | `bool` | `False` | כלול תרגום תמונות. מצריך קונפיגורציית Azure AI Vision. |
| `markdown` | `bool` | `False` | כלול תרגום Markdown. |
| `notebook` | `bool` | `False` | כלול תרגום מחברות Jupyter. |
| `debug` | `bool` | `False` | הפעל רישום ניפוי שגיאות (debug logging). |
| `save_logs` | `bool` | `False` | שמור קבצי לוג ברמת DEBUG תחת תיקיית השורש `logs/`. |
| `yes` | `bool` | `True` | מאשר אוטומטית בקשות אישור לשימוש תוכניתי ו־CI. |
| `add_disclaimer` | `bool` | `False` | הוסף הודעות ויתור על תרגום מכונה ל-Markdown ולמחברות המתורגמות. |
| `translations_dir` | `str \| None` | `None` | תיקיית פלט מותאמת לתרגום טקסט. נתיבים יחסיים מתפרשים ביחס לכל שורש. |
| `image_dir` | `str \| None` | `None` | תיקיית פלט מותאמת לתמונות מתורגמות. נתיבים יחסיים מתפרשים ביחס לכל שורש. |
| `root_dirs` | `Iterable[str] \| None` | `None` | מספר שורשים החולקים את אותן הגדרות פלט. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | זוגות מפורשים של `(root_dir, translations_dir)`. בעלי עדיפות על פני `root_dirs`. |
| `repo_url` | `str \| None` | `None` | כתובת ה-URL של המאגר המשמשת בעת יצירת טבלת השפות ב-README. |
| `glossaries` | `Iterable[str] \| None` | `None` | מונחים ממילון לשימור במהלך התרגום. כפילויות ומונחים ריקים מנורמלים. |
| `dry_run` | `bool` | `False` | אומד כמות תרגום ומציג תצוגה מקדימה של התנהגות ההגירה ללא כתיבת קבצים. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | מתאם אחסון אופציונלי ל-accepted-baseline ו-candidate לעדכוני Markdown אינקרמנטליים. השמטתו תשמר את התנהגות הקבצים המלאים הקיימת. |

## פרמטרי סקירה

`run_review` משקפת בכוונה את החתימה של `run_translation` כאשר ניתן, כך שאוטומציה תוכל לעבור בין זרימות עבודה של תרגום וביקורת עם מינימום הסתעפויות.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | תיקיות שפה המיועדות לביקורת. מתקבלות מחרוזות מופרדות ברווחים ואיטרטורים. `"all"` סוקרות כל שפת תרגום שהתגלתה. |
| `root_dir` | `str` | `"."` | שורש הפרויקט למטרת סקירה יחידה. מתעלם במקרה ש-`root_dirs` או `groups` מסופקים. |
| `markdown` | `bool` | `False` | הכלל קבצי מקור של Markdown ו-MDX. |
| `notebook` | `bool` | `False` | הכלל קבצי מקור של מחברות Jupyter. |
| `images` | `bool` | `False` | שמורה לשם התאמה לאפשרויות התרגום. הפניות קישור לתמונות נבדקות מתוך Markdown. |
| `translations_dir` | `str \| None` | `None` | תיקיית פלט מותאמת לתרגום טקסט. נתיבים יחסיים מתפרשים ביחס לכל שורש. |
| `root_dirs` | `Iterable[str] \| None` | `None` | מספר שורשים החולקים את אותן הגדרות פלט. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | זוגות מפורשים של `(root_dir, translations_dir)`. בעלי עדיפות על פני `root_dirs`. |
| `changed_from` | `str \| None` | `None` | רפרנס Git המשמש להגבלת הסקירה לקבצי מקור ששונו. |
| `readme_only` | `bool` | `False` | סוקר רק את `README.md` תחת כל שורש מקור. היעדר קובץ README מקור יגרום להעלאת `ValueError`. |
| `output_format` | `str` | `"text"` | פורמט פלט הסקירה. הערכים הנתמכים הם `"text"` ו-`"github"`. |
| `fail_on_warnings` | `bool` | `False` | לטפל באזהרות ככשלונות בנוסף לשגיאות. |
| `debug` | `bool` | `False` | הפעלת רישום דיבוג. |
| `save_logs` | `bool` | `False` | שמור קבצי לוג ברמת DEBUG תחת תיקיית השורש `logs/`. |

אם לא מוגדרים `markdown`, `notebook` או `images`, ה-API בודק Markdown, מחברות וקישורים לתמונות היכן שמתאים. הסקירה אינה קוראת לספק LLM ואינה דורשת מפתחות API.

## דרישות תצורה

ממשקי תרגום שתומכים בספק דורשים הגדרת ספק לפני התרגום:

- תרגום Markdown ומחברות דורש ספק LLM. הגדר Azure OpenAI, OpenAI, או Anthropic.
- תרגום תמונות דורש Azure AI Vision בנוסף לספק ה-LLM.
- `run_translation` מבצע בדיקות חיבור קלות לפני תחילת תרגום הפרויקט.
- ממשקי ה-API המונחים על ידי סוכן `start_*_agent_translation` ו-`finish_*_agent_translation` אינם קוראים לספקי ה-LLM של Co-op Translator. יישום המאחסן או סוכן MCP מתרגם את החתיכות המוכנות.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, ו-`run_review` הם דטרמיניסטיים ואינם דורשים אישורי ספק.

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

Required Anthropic variables:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` ו-`ANTHROPIC_MAX_TOKENS` אופציונליים. Microsoft Agent Framework הוא לקוח המודל המוגדר כברירת מחדל עבור כל הספקים החל מ-Co-op Translator 0.22.0. ניתן עדיין לבחור זמנית ב-Semantic Kernel באמצעות `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, אך פעולה זו מפיקה אזהרת התיישנות; ראה [תצורה](configuration.md#model-client-backend) לתוכנית ההסרה בשלבים.

משתני Azure AI Vision הנדרשים לתרגום תמונות:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` דטרמיניסטי ואינו דורש תצורת LLM או Azure AI Vision.

## הערות התנהגות

- ממשקי ה-API לתרגום תוכן שומרים על הפרדת התרגום מעדכון נתיבי הפרויקט. קראו ל-`rewrite_markdown_paths` או `rewrite_notebook_paths` במפורש כאשר יש להתאים קישורים יחסיים של הפרויקט לתוכן המתורגם עבור מיקום יעד.
- ממשקי ה-API לתזמור פרויקטים מוסיפים התנהגות פרויקטית סביב תרגום התוכן, כולל גילוי קבצים, כתיבה, עדכון נתיבים, מטא-נתונים, ניקוי ואזהרות אופציונליות.
- `run_translation` מדפיס סיכומי התקדמות והערכות דרך אותו מדווח מבוסס Rich שבו משתמש ה-CLI. פלט שאינו אינטראקטיבי חוזר לטקסט פשוט.
- `dry_run=True` מחשב הערכות באמצעות עדכוני README וירטואליים, אך אינו כותב את ה-README או את קבצי התרגום.
- `groups` מעובדים ברצף. הערכה מצטברת אחת מודפסת לפני תחילת העבודה.
- כאשר נבחר תרגום תמונות, חוסר בתצורת Vision יגרום לשגיאה לפני תחילת התרגום.
- תיקיות שפה קיימות המבוססות על כינויים מזוהות וניתן להעבירן לשמות תיקיות שפה קנוניים כחלק מהריצה.
- `run_review` נכשל כשיש קבצים מתורגמים חסרים, מטא-נתוני תרגום חסרים או מיושנים, frontmatter של Markdown/מחסומי קוד מעוותים, או JSON לא חוקי של מחברת מתורגמת.
- `run_review` מדווח כברירת מחדל על חוסר ביעדי קישורי Markdown מקומיים וקישורי תמונה כאזהרות.

## מסלול קריאה פנימי

ה-API סומך על אותה מימוש ליבה המשמש את ה-CLI:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. מיקסינים ממוקדים לתרגום פרויקטים עבור Markdown, מחברות ותמונות.
8. מתרגמי Markdown, מחברות, טקסט ותמונות תחת `co_op_translator.core`.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

המחלקות הבאות מועילות למתחזקים, אך אינן מיוצאות כ-API יציב ברמת החבילה.

| Class | Module | Responsibility |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | מתאם תרגום ברמת הפרויקט, ניהול תיקיות, נירמול מטה-נתונים לפי שפה, והפניה למתרגמי Markdown, מחברות ותמונות. |
| `TranslationManager` | `co_op_translator.core.project.translation` | מבצע את עבודת עיבוד הקבצים האסינכרונית עבור Markdown, מחברות, תמונות, זיהוי תוכן מיושן, ועדכוני מטה-נתוני תרגום. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | מתזמר קריאות קבצי Markdown, תרגום תוכן, שכתוב נתיבים, מטה-נתונים, הודעות ויתור וכתיבות. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | מתזמר קריאות קבצי מחברת, תרגום תאי Markdown, שכתוב נתיבים, מטה-נתונים, הודעות ויתור וכתיבות. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | מתזמר גילוי תמונות מקור, תרגום תמונות, נתיבי פלט, מטה-נתונים וכתיבות. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | מאתר זוגות Markdown מתורגמים, מעריך איכות תרגום, וקורא מטה-נתוני ביטחון עבור זרימות עבודה לתיקון עם ביטחון נמוך. |
| `ReviewRunner` | `co_op_translator.review.runner` | מתאם בדיקות סקירה דטרמיניסטיות על פני קבצי מקור, שפות יעד, ושורשי תרגום מוגדרים. |
| `ReviewTarget` | `co_op_translator.review.targets` | מתאר שורש מקור ותיקיית פלט התרגום שנבדקת עבור אותו שורש. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | מזהה תיקיות שפה ותיקות על בסיס כינויים ומכין תוכניות העברה לשמות תיקיות קנוניים לפי BCP 47. |
| `Config` | `co_op_translator.config.base_config` | טוען `.env` קבצים ובודק האם ספקי LLM הנדרשים וספקי Vision האופציונליים מוגדרים. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | מגלה אוטומטית Azure OpenAI, OpenAI או Anthropic, מאמת משתני סביבה נדרשים, ומריץ בדיקות חיבור לספק. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | מזהה קונפיגורציית Azure AI Vision ומריץ בדיקות חיבור לתרגום תמונות. |