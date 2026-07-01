# בחר את זרימת העבודה שלך

Co-op Translator ניתן להשתמש בשלושה אופנים: ה-CLI, ממשק ה-API של Python, ושרת ה-MCP. הם חולקים את אותן יכולות תרגום, אך כל אחד מתאים לזרימת עבודה שונה.

השתמש בעמוד זה כאשר אתה מחליט מהיכן להתחיל.

## החלטה מהירה

| אם אתה רוצה... | השתמש ב- | התחל כאן |
| --- | --- | --- |
| לתרגם או לסקור מאגר מתוך טרמינל | CLI | [מדריך ה-CLI](cli.md) |
| להוסיף תרגום לסקריפט Python, שירות, פנקס רשימות, או משימת CI | ממשק ה-API של Python | [ממשק ה-API של Python](api.md) |
| לאפשר לסוכן, עורך, או לקוח תואם MCP לתרגם תוכן עבורך | שרת MCP | [שרת MCP](mcp.md) |
| לתרגם מסמך Markdown אחד, פנקס רשימות, או תמונה שהאפליקציה שלך כבר טענה | ממשק ה-API של Python או שרת MCP | [ממשק ה-API של Python](api.md) או [שרת MCP](mcp.md) |
| לתרגם מאגר שלם עם תיקיות יציאה סטנדרטיות ומטא-נתונים | CLI או `run_translation` | [מדריך ה-CLI](cli.md) או [ממשק ה-API של Python](api.md) |

## השתמש ב-CLI כאשר

בחר ב-CLI כאשר אדם או משימת CI מנהלים את תרגום המאגר משורת הפקודה.

ה-CLI הוא הנתיב הישיר ביותר כאשר אתה רוצה ש-Co-op Translator יאתר קבצי פרויקט, ייצור תוצרי תרגום, ישמור על מבנה הפרויקט, יעדכן מטא-נתונים ויריץ פקודות סקירה.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

מקרים מתאימים:

- אתה מתרגם מאגר מהטרמינל.
- אתה רוצה פקודה שניתן להריץ שוב עבור תהליכי CI או שחרור.
- אתה רוצה גילוי פרויקטים מובנה, נתיבי יציאה, מטא-נתונים, ניקוי וביקורת.
- אתה מעדיף ממשק שורת פקודה על פני כתיבת קוד Python.

## השתמש בממשק ה-API של Python כאשר

בחר בממשק ה-API של Python כאשר הקוד שלך צריך לשלוט בזרימת העבודה.

הממשק שימושי עבור יישומים, סקריפטים לאוטומציה, פנקסי רשימות, שירותים וצינורות מותאמים. הוא מאפשר לך לקרוא ל-APIs של תרגום תוכן ברמת בסיס עבור קבצים בודדים, או להריץ את אותה אורקסטרציה ברמת מאגר שמשתמש בה-CLI.

לתרגם מסמך Markdown אחד ולקבוע היכן לשמור אותו:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


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
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

להריץ תרגום מאגר מ-Python:

```python
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

מקרים מתאימים:

- האפליקציה שלך כבר קוראת קבצים, buffers, פנקסי רשימות או נתוני תמונה.
- אתה צריך אימות מותאם אישית, אחסון, רישום לוגים, ניסיונות חוזרים, או תהליכי אישור.
- אתה רוצה לתרגם מסמך, פנקס רשימות או תמונה אחת מבלי לעבד מאגר שלם.
- אתה רוצה לתרגם מאגר, אבל באמצעות אוטומציה ב-Python במקום פקודת שורת פקודה.

## השתמש בשרת ה-MCP כאשר

בחר בשרת ה-MCP כאשר סוכן, עורך, או לקוח תואם MCP צריך לקרוא לכלי Co-op Translator.

בהגדרה מקומית רגילה, המשתמש לא מחזיק שרת פועל באופן ידני. לקוח ה-MCP מפעיל את `co-op-translator-mcp` על פני `stdio` כשהוא צריך את הכלים.

דוגמאות לבקשות משתמש שסוכן יכול לטפל בהן:

- "תרגם את קובץ Markdown הזה לקוריאנית ושמור על תקינות הקישורים."
- "תרגם את קובץ Markdown הזה לקוריאנית באמצעות זרימת עבודה של MCP בסיוע סוכן, תוך שימוש בדגם שלך עבור החלקים המתורגמים."
- "תרגם את הפנקס הזה לקוריאנית, שמור על תאי קוד, והשתמש ב-Co-op Translator MCP לשחזר את הפנקס."
- "תרגם את הטקסט בתמונה זו ליפנית ושמור את התוצאה."
- "הפעל סימולציה של תרגום מאגר לספרדית ואמור לי מה ישתנה."
- "סקור האם פלט התרגום לקוריאנית מעודכן."

לגבי Markdown ופנקסי רשימות, MCP יכול לעבוד בשני מצבים:

| מצב | השתמש כאשר | כלים עיקריים |
| --- | --- | --- |
| בסיוע סוכן | הסוכן המארח של MCP צריך לתרגם חלקים באמצעות הדגם שלו, ללא אישורי ספק LLM של Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| בהסתמכות על ספק | Co-op Translator צריך לקרוא ל-Azure OpenAI או ל-OpenAI ישירות. | `translate_markdown_content`, `translate_notebook_content` |

צורת קריאת כלי Markdown ב-MCP בהסתמכות על ספק:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

צורת קריאת כלי תמונה ב-MCP:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

תרגום מאגר מתבצע בסימולציה כברירת מחדל דרך MCP:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

מקרים מתאימים:

- אתה רוצה תהליכי תרגום בשפה טבעית בתוך סוכן או עורך.
- אתה רוצה תרגום Markdown או פנקסי רשימות שבו דגם הסוכן המארח מתרגם חלקים מוכנים.
- אתה רוצה שהסוכן יתרגם תוכן נבחר במקום מאגר שלם.
- אתה רוצה שלב אישור לפני כתיבה על כל המאגר.
- אתה רוצה ממשק אחד שיחשוף כלים עבור Markdown, פנקסי רשימות, תמונות, סקירה ושכתוב נתיבים.

## איך הם משתלבים יחד

ה-CLI הוא הבחירה הטובה כברירת מחדל עבור בני אדם המתרגמים מאגרים. ממשק ה-API של Python הוא הטוב ביותר כאשר הקוד שלך שולט בזרימת העבודה. שרת ה-MCP הוא הטוב ביותר כאשר סוכן או עורך שולט בזרימת העבודה.

שלושת הנתיבים משתמשים באותו ממשק ציבורי של Co-op Translator, כך שאתה יכול להתחיל ב-CLI, לאוטומט עם Python מאוחר יותר, ולחשוף את אותן יכולות ללקוחות MCP כאשר אתה צריך זרימות עבודה מונעות סוכן.