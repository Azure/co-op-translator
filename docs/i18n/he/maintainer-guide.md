# מדריך למתחזקים

עמוד זה מסכם כיצד ה-API, ה-CLI ואתר התיעוד משולבים יחד.

## גבול ה-API הציבורי

ה-API היציב של Python מיוצא מ:

```python
co_op_translator.api
```

ה-API הציבורי מאורגן לעזרי תרגום תוכן, עזרי שכתוב נתיבים, תזמור פרויקטים וביקורת:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
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

`TranslationStateProvider` הוא גבול ההתמדה עבור אינטגרציות מתארחות.
עליו לשמור מועמדים שנוצרו נפרדים מבסיסי קו-הבסיס שהתקבלו כך ש-
תרגום שלא מוזג לא יהפוך למקור האמת.

בעת הוספת API ציבוריים חדשים, עדכן:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- מבחני API רלוונטיים תחת `tests/co_op_translator/`, כגון `test_api.py` או `test_review_api.py`

הימנע מתיעוד מודולים ברמה נמוכה יותר `core` כ-API יציב אלא אם הפרויקט מתכוון לתמוך בהם ישירות.

## נקודות כניסה של ה-CLI

החבילה מגדירה סקריפטים של Poetry אלה:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` מנתב לפי שם הסקריפט:

- `translate` קורא ל- `co_op_translator.cli.translate.translate_command`
- `evaluate` קורא ל- `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` קורא ל- `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` קורא ל- `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` מעקף את `__main__.py` ומפעיל את `co_op_translator.mcp.server:main` ישירות.

בעת הוספה או שינוי של אפשרויות CLI, עדכן:

- את הפקודה הרלוונטית ב-`src/co_op_translator/cli/*.py`
- `docs/cli.md`
- מבחני הקשורים ל-CLI, אם ההתנהגות משתנה

## שרת MCP

שרת ה-MCP ממומש ב:

```python
co_op_translator.mcp.server
```

השרת עוטף בכוונה את ה-API הציבורי של Python במקום לקרוא למודולים ברמה נמוכה יותר `core`. שמור על הגבול הזה כך שלקוחות MCP, קוראי Python וה-CLI ישתפו את אותה ההתנהגות.

בעת הוספה או שינוי של כלי ה-MCP, עדכן:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` אם משטח ה-API הציבורי משתנה

כלי תרגום המאגר ניתנים לקריאה על ידי המודל דרך MCP ויכולים לכתוב קבצים רבים. שמרו על `dry_run=True` כברירת מחדל ודרשו `confirm_write=True` לפני תרגום פרויקט שלא ב-dry-run.

## זרימת התרגום

הזרימה ברמת גבוהה של תרגום הפרויקט היא:

1. ניתוח ארגומנטים של CLI או פרמטרים של ה-API.
2. אימות תצורת LLM עם `LLMConfig`.
3. אימות Azure AI Vision כשנבחר תרגום תמונה.
4. נרמול קודי שפה.
5. זיהוי כינויים של תיקיות שפה ישנות.
6. הערכת נפח התרגום.
7. עדכון חלקי README של שפה/קורס כאשר זה רלוונטי.
8. העבר את תרגום הפרויקט ל-`ProjectTranslator`.
9. `ProjectTranslator` מעביר את עיבוד הקבצים ל-`TranslationManager`.

`TranslationManager` מורכב ממיקסינים ממוקדים לפי סוגי קבצים:

- `ProjectMarkdownTranslationMixin` מטפל בקריאת קבצי Markdown, בתרגום התוכן, בשכתוב נתיבים, במטא-דאטה, בהצהרות פטור מאחריות, ובכתיבה.
- `ProjectNotebookTranslationMixin` מטפל בקריאת קבצי מחברת, בתרגום תאי Markdown, בשכתוב נתיבים, במטא-דאטה, בהצהרות פטור מאחריות, ובכתיבה.
- `ProjectImageTranslationMixin` מטפל בגילוי תמונות, בחילוץ/תרגום טקסט, בכתיבת תמונות מעובדות, ובמטא-דאטה.

ה-API של התוכן ברמה נמוכה יותר מדלג על תהליך העבודה של הפרויקט:

1. `translate_markdown_content` ו-`translate_notebook_content` מתרגמים תוכן בזיכרון בלבד.
2. `translate_image_content` מתרגם טקסט בתמונה יחידה ומחזיר אובייקט תמונה מעובדת.
3. `rewrite_markdown_paths` ו-`rewrite_notebook_paths` הן עזרי עיבוד פוסט-עיבוד מפורשים. הן אינן מבצעות תרגום ואינן כותבות קבצים בפרויקט.

## זרימת הביקורת

הזרימה הדטרמיניסטית של הביקורת היא:

1. ניתוח ארגומנטים של CLI או פרמטרים של ה-API.
2. נרמול קודי השפה המבוקשים.
3. בנה יעד ביקורת אחד או יותר מתוך `root_dir`, `root_dirs`, או `groups`.
4. באופן אופציונלי הגבל קבצי מקור עם `--changed-from`.
5. הרץ בדיקות דטרמיניסטיות למבנה, עדכניות התרגום, שלמות Markdown, ונתיבי קישורים/תמונות מקומיים.
6. הדפס פלט טקסטואלי או Markdown בסגנון GitHub.
7. צא עם שגיאה כאשר נמצאו שגיאות בביקורת.

זרימת הביקורת אינה דורשת מפתחות API ונשארת זמינה לבדיקות מקומיות או ל-CI צרכני אופציונלי. מאגר זה אינו מריץ את `co-op-review` אוטומטית על כל בקשת משיכה.

## אתר התיעוד

אתר התיעוד מוגדר על ידי:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

תיקיית `docs/` היא מקור התיעוד הקנוני. אל תוסיפו מדריכי משתמש חדשים מחוץ לתיקיה זו אלא אם הפרויקט מתכוון במודע להציג ממשק תיעוד נוסף מפורסם.

בנייה מקומית:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

תצוגה מקומית:

```bash
python -m mkdocs serve
```

האתר שנוצר נכתב לתיקייה `site/`, אשר מוזנחת על ידי git.

## זרימת העבודה של GitHub Pages

`.github/workflows/docs.yml` בונה את האתר עבור בקשות משיכה ומפרסם אותו כאשר דוחפים ל-`main`.

זרימת העבודה מתקינה:

```bash
pip install -r requirements-docs.txt
```

זרימת העבודה של התיעוד מתקינה רק את שרשרת הכלים של התיעוד. `mkdocs.yml` מצביע על `mkdocstrings` אל `src/` כך שניתן להפיק דפי API ציבוריים מעץ המקור בלי להתקין את כל חבילת התלויות בזמן הריצה. אם מסמכי API עתידיים ידרשו לייבא ספקי runtime אופציונליים במהלך הבנייה, עדכן גם את `.github/workflows/docs.yml` וגם מדריך זה.

## רף איכות התיעוד

לפני מיזוג שינויים בתיעוד, הרץ:

```bash
python -m mkdocs build --strict
git diff --check
```

השתמש בבנייה קפדנית כדי שקישורים שבורים, כניסות ניווט לא תקינות ובעיות בהצגת ה-API ייכשלו בשלב מוקדם.