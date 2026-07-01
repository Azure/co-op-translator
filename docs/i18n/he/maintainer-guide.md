# מדריך למתחזקים

עמוד זה מסכם כיצד ה-API, ה-CLI ואתר התיעוד קשורים זה לזה.

## גבול ה-API הציבורי

ממשק ה-Python היציב מיוצא מ:

```python
co_op_translator.api
```

ה-API הציבורי מאורגן לעוזרי תרגום תוכן, עוזרי שכתוב נתיבים, אורקסטרציה של פרויקטים וביקורת:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

בעת הוספת APIs ציבוריים חדשים, עדכן:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- מבחני API רלוונטיים תחת `tests/co_op_translator/`, כגון `test_api.py` או `test_review_api.py`

הימנע מתיעוד מודולי `core` ברמת נמוכה כממשק יציב אלא אם הפרויקט מתכוון לתמוך בהם ישירות.

## נקודות כניסה של CLI

החבילה מגדירה את הסקריפטים הבאים ב-Poetry:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` מנתב לפי שם הסקריפט:

- `translate` מפעיל את `co_op_translator.cli.translate.translate_command`
- `evaluate` מפעיל את `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` מפעיל את `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` מפעיל את `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` עוקף את `__main__.py` וקורא ישירות ל-`co_op_translator.mcp.server:main`.

בעת הוספה או שינוי של אפשרויות CLI, עדכן:

- את קובץ הפקודה הרלוונטי `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- מבחנים הקשורים ל-CLI, אם ההתנהגות משתנה

## שרת MCP

שרת ה-MCP מיושם ב:

```python
co_op_translator.mcp.server
```

השרת עוטף בכוונה את ה-API של Python הציבורי במקום לקרוא למודולי `core` ברמת נמוכה. שמרו על גבול זה שלם כדי שלקוחות MCP, קוראי Python ו-CLI ישתפו את אותה התנהגות.

בעת הוספה או שינוי כלי MCP, עדכן:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` אם ממשק ה-API הציבורי משתנה

כלי תרגום המאגר ניתנים לקריאה במודל דרך MCP ויכולים לכתוב קבצים רבים. השאר את `dry_run=True` כברירת מחדל ודרש `confirm_write=True` לפני תרגום פרויקט שאינו `dry_run`.

## זרימת התרגום

הזרימה ברמה גבוהה של תרגום הפרויקט היא:

1. נתח את ארגומנטי ה-CLI או את הפרמטרים של ה-API.
2. אמת את תצורת ה-LLM באמצעות `LLMConfig`.
3. אמת את Azure AI Vision כאשר נבחר תרגום תמונה.
4. נרמל קודי שפה.
5. גלה כינויים של תיקיות שפה ישנות.
6. הערך את נפח התרגום.
7. עדכן את חלקי השפה/הקורס ב-README כאשר הדבר רלוונטי.
8. העבר את תרגום הפרויקט ל-`ProjectTranslator`.
9. `ProjectTranslator` מעביר עיבוד קבצים ל-`TranslationManager`.

`TranslationManager` מורכב ממיקסינים ממוקדי סוג קובץ:

- `ProjectMarkdownTranslationMixin` מטפל בקריאות קבצי Markdown, בתרגום תוכן, בשכתוב נתיבים, במטה-נתונים, בהצהרות ובכתיבה.
- `ProjectNotebookTranslationMixin` מטפל בקריאות קבצי notebook, בתרגום תאי Markdown, בשכתוב נתיבים, במטה-נתונים, בהצהרות ובכתיבה.
- `ProjectImageTranslationMixin` מטפל בגילוי תמונות, בהפקת ותרגום טקסט, בכתיבת תמונות מעובדות ובמטא-נתונים.

ממשקי התוכן ברמת נמוכה מדלגים על זרימת העבודה של הפרויקט:

1. `translate_markdown_content` ו-`translate_notebook_content` מתרגמים תוכן בזיכרון בלבד.
2. `translate_image_content` מתרגם טקסט בתמונה יחידה ומחזיר אובייקט תמונה מעובדת.
3. `rewrite_markdown_paths` ו-`rewrite_notebook_paths` הם עזרי עיבוד-לאחר מפורשים. הם לא מבצעים תרגום ולא כותבים קבצים בפרויקט.

## זרימת הביקורת

זרימת הביקורת הדטרמיניסטית היא:

1. נתח את ארגומנטי ה-CLI או את הפרמטרים של ה-API.
2. נרמל את קודי השפה המבוקשים.
3. בנה יעד או יעדים לביקורת מתוך `root_dir`, `root_dirs`, או `groups`.
4. באופן אופציונלי הגבילו קבצי מקור באמצעות `--changed-from`.
5. הרץ בדיקות דטרמיניסטיות למבנה, לרעננות התרגום, לשלמות Markdown ולנתיבים מקומיים של קישורים/תמונות.
6. הדפס או פלט טקסטואלי או Markdown בסגנון GitHub.
7. סיים בכישלון כאשר נמצאו שגיאות בביקורת.

זרימת הביקורת אינה דורשת מפתחות API וכדאי שתישאר מתאימה ל-CI של בקשות משיכה. זרימת העבודה של בקשת המשיכה כותבת סיכום בדיקה בכל ריצה ורק מפרסמת תגובה ל-PR כאשר `co-op-review` נכשל.

## אתר התיעוד

אתר התיעוד מוגדר על ידי:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

ספריית `docs/` היא מקור התיעוד הקנוני. אל תוסיפו מדריכים חדשים למשתמש הקצה מחוץ לתיקייה הזו אלא אם הפרויקט מציג בכוונה משטח תיעוד מפורסם נוסף.

Build locally:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview locally:

```bash
python -m mkdocs serve
```

האתר שנוצר נכתב לתיקייה `site/`, שנכללת ברשימת ההשמטה של git.

## זרימת העבודה של GitHub Pages

`.github/workflows/docs.yml` בונה את האתר עבור בקשות משיכה ומפרסם אותו כאשר יש דחיפה לענף `main`.

זרימת העבודה מתקינה:

```bash
pip install -r requirements-docs.txt
```

זרימת העבודה של התיעוד מתקינה רק את כלי התיעוד. `mkdocs.yml` מצביע את `mkdocstrings` אל `src/` כך שעמודי ה-API הציבורי יכולים להיווצר מתוך עץ המקור מבלי להתקין את כל ערכת התלויות של זמן הריצה. אם תיעוד API עתידי ידרש לייבא ספקי זמן ריצה אופציונליים במהלך הבנייה, עדכן גם את `.github/workflows/docs.yml` וגם מדריך זה יחד.

## רמת איכות התיעוד

לפני מיזוג שינויים בתיעוד, הרץ:

```bash
python -m mkdocs build --strict
git diff --check
```

השתמש בבניות מחמירות כדי שקישורים שבורים, כניסות ניווט לא תקינות ובעיות בהצגת ה-API ייכשלו מוקדם.