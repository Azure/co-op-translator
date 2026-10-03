# בחר את זרימת העבודה שלך

ניתן להשתמש ב‑Co-op Translator בשלוש דרכים: ה‑CLI, ה‑Python API והשרת MCP. כולן חולקות את אותן יכולות תרגום, אך כל אחת מתאימה לזרימת עבודה שונה.

השתמש בעמוד זה כאשר אתה מחליט מאיפה להתחיל.

**אם אתה עורך תרגומים ידנית:** זרימות העבודה המוגדרות כברירת מחדל של ה‑CLI ושל Actions יתרגמו מחדש קבצי מקור ששונו בשלמותם, ולכן הניסוח שלך באותם קבצים עלול להימחק. בדוק את ה‑diff לפני שתקבל עדכון. לשמירה על רמת בלוק Markdown של עריכות שהתקבלו, השתמש בספק מצב התרגום של [ספק מצב התרגום של Python API](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## החלטה מהירה

| אם אתה רוצה... | השתמש ב‑ | התחל כאן |
| --- | --- | --- |
| לתרגם או לסקור מאגר מתוך טרמינל | CLI | [מדריך ה-CLI](cli.md) |
| להוסיף תרגום לסקריפט Python, לשירות, ל‑notebook, או לעבודת CI | Python API | [Python API](api.md) |
| לאפשר לסוכן, עורך, או לקוח התואם MCP לתרגם תוכן עבורך | MCP Server | [MCP Server](mcp.md) |
| לתרגם מסמך Markdown אחד, notebook, או תמונה שהאפליקציה שלך כבר טענתה | Python API או MCP Server | [Python API](api.md) או [MCP Server](mcp.md) |
| לתרגם מאגר שלם עם תיקיות פלט סטנדרטיות ומטא‑נתונים | CLI או `run_translation` | [מדריך ה-CLI](cli.md) או [Python API](api.md) |

## השתמש ב‑CLI כאשר

בחר ב‑CLI כאשר אדם או משימת CI מנהלים את תרגום המאגר מהמעטפת (shell).

ה‑CLI הוא הנתיב הישיר ביותר כשאתה רוצה ש‑Co-op Translator יגלה קבצי פרויקט, ייצור פלטים מתורגמים, ישמור על מבנה הפרויקט, יעדכן מטא‑נתונים, ויריץ פקודות סקירה.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

דוגמה זו מתרגמת Markdown ופנקסי רשימות (notebooks). הוסף את `-img` רק לאחר תצורה של [Azure AI Vision](configuration.md#azure-ai-vision). להרצה ראשונית של Markdown בלבד, עקוב אחר [התרגום הראשון שלך](first-translation.md).

מקרים מתאימים:

- אתה מתרגם מאגר מהטרמינל שלך.
- אתה רוצה פקודה שניתנת לחזרה עבור זרימות עבודה של CI או שחרור.
- אתה רוצה גילוי פרויקט מובנה, נתיבי פלט, מטא‑נתונים, ניקוי, וסקירה.
- אתה מעדיף ממשק פקודות על פני כתיבת קוד Python.

## השתמש ב‑Python API כאשר

בחר ב‑Python API כאשר הקוד שלך צריך לשלוט בזרימת העבודה.

ה‑API שימושי לאפליקציות, סקריפטים לאוטומציה, פנקסי רשימות (notebooks), שירותים וצינורות מותאמים אישית. הוא מאפשר לך לקרוא ל‑APIs ברמת נמוכה לתרגום תוכן עבור קבצים יחידים, או להריץ את אותה אורקסטרציה ברמת המאגר שבה משתמש ה‑CLI.

תרגם מסמך Markdown אחד והחליט היכן לשמור אותו:

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

הרץ תרגום מאגר מ‑Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

מקרים מתאימים:

- האפליקציה שלך כבר קוראת קבצים, buffers, פנקסי רשימות, או בתים של תמונה.
- אתה צריך אימות מותאם, אחסון, רישום לוגים, ניסיונות מחדש, או זרימות אישור.
- אתה רוצה לתרגם מסמך יחיד, פנקס רשימות, או תמונה מבלי לעבד מאגר שלם.
- אתה רוצה תרגום מאגר, אבל מתוך אוטומציה ב‑Python במקום פקודת shell.

## השתמש ב‑MCP Server כאשר

בחר בשרת MCP כאשר סוכן, עורך, או לקוח תואם MCP אמורים לקרוא לכלי Co-op Translator.

בהתקנה מקומית רגילה, המשתמש לא שומר שרת פועל ידנית. לקוח ה‑MCP מפעיל את `co-op-translator-mcp` על גבי `stdio` כאשר הוא צריך את הכלים.

דוגמאות של בקשות משתמש שסוכן יכול להתמודד איתן:

- "תרגם קובץ Markdown זה לקוריאנית ושמור על נכונות הקישורים."
- "תרגם קובץ Markdown זה לקוריאנית באמצעות זרימת העבודה MCP בעזרת סוכן, תוך שימוש במודל שלך לקטעים המתורגמים."
- "תרגם את ה‑notebook הזה לקוריאנית, שמור על תאי קוד, והשתמש ב‑Co-op Translator MCP כדי לשחזר את ה‑notebook."
- "תרגם את הטקסט בתמונה זו ליפנית ושמור את התוצאה."
- "הרץ תרגום מאגר ב‑dry-run לספרדית ותגיד לי מה ישתנה."
- "סקור האם הפלט של התרגום לקוריאנית מעודכן."

עבור Markdown ופנקסי רשימות (notebooks), MCP יכול לפעול בשני מצבים:

| מצב | השתמש כאשר | כלים עיקריים |
| --- | --- | --- |
| בסיוע סוכן | כאשר סוכן ה‑MCP המארח צריך לתרגם קטעים עם המודל שלו, ללא אישורי ספק ה‑LLM של Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| נתמך על ידי ספק | כאשר Co-op Translator צריך לקרוא ישירות ל‑Azure OpenAI, OpenAI, או Anthropic. | `translate_markdown_content`, `translate_notebook_content` |

צורת קריאת כלי Markdown ב‑MCP הנתמך על ידי ספק:

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

צורת קריאת כלי התמונות ב‑MCP:

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

תרגום מאגר מתבצע ב‑dry-run כברירת מחדל דרך MCP:

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

- אתה רוצה זרימות עבודה לתרגום בשפה טבעית בתוך סוכן או עורך.
- אתה רוצה תרגום Markdown או notebook שבו מודל הסוכן המארח מתרגם קטעים שהוכנו.
- אתה רוצה שהסוכן יתרגם תוכן נבחר במקום מאגר שלם.
- אתה רוצה שלב אישור לפני כתיבות רוחב‑מאגר.
- אתה רוצה ממשק יחיד שמחשף כלים ל‑Markdown, notebook, תמונה, סקירה, ושכתוב נתיבים.

## איך הם מתחברים יחד

ה‑CLI הוא ברירת המחדל הטובה ביותר לאנשים המתרגמים מאגרים. ה‑Python API הוא הטוב ביותר כאשר הקוד שלך שולט בזרימת העבודה. שרת ה‑MCP הוא הטוב ביותר כאשר סוכן או עורך שולט בזרימת העבודה.

שלוש הדרכים משתמשות באותו API ציבורי של Co-op Translator, כך שאפשר להתחיל ב‑CLI, לבצע אוטומטיזציה עם Python מאוחר יותר, ולחשוף את אותן יכולות ללקוחות MCP כאשר אתה צריך זרימות עבודה המונחות על‑ידי סוכן.