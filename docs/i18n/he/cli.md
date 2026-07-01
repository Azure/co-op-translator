# הפניה ל-CLI

Co-op Translator מתקין נקודות כניסה לשורת הפקודה אלה:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

הפקודות `translate`, `evaluate`, `migrate-links`, ו-`co-op-review` מפנות דרך `co_op_translator.__main__`, שמבחר את מימוש הפקודה בהתבסס על שם הסקריפט שהופעל. שרת ה-MCP משתמש ב-`co_op_translator.mcp.server` ישירות.

אם אתם בוחרים בין CLI, Python API, ו-MCP, התחילו עם [בחרו את תהליך העבודה שלכם](workflows.md).

## First-Time CLI Flow

התחילו כאן אם אתם משתמשים ב-Co-op Translator מהטרמינל:

1. הגדרו ספק LLM כפי שמתואר ב-[הגדרות](configuration.md).
2. בחרו את סוג התוכן שברצונכם לתרגם.
3. הפעילו תחילה פקודה ממוקדת, כמו תרגום Markdown בלבד.
4. השתמשו ב-`--dry-run` לפני שינויים גדולים במאגר.
5. השתמשו ב-`co-op-review` לאחר התרגום כדי לבדוק מבנה ורעננות.

| מטרה | פקודה להתחלה |
| --- | --- |
| תרגום מסמכי Markdown | `translate -l "ko" -md` |
| תרגום מחברות | `translate -l "ko" -nb` |
| תרגום טקסט בתמונות | `translate -l "ko" -img` |
| תצוגה מקדימה של העבודה מבלי לכתוב קבצים | `translate -l "ko" -md --dry-run` |
| סקירת תרגומים קיימים | `co-op-review -l "ko"` |
| עדכון קישורי מחברות ו-Markdown | `migrate-links -l "ko" --dry-run` |
| חשפו כלים ללקוח MCP | תגדירו את ה-[שרת MCP](mcp.md) במקום להריץ פקודות CLI ישירות. |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

```bash
translate -l "ko ja fr"
```

### דוגמאות נפוצות

תרגום של Markdown בלבד:

```bash
translate -l "de" -md
```

תרגום של מחברות בלבד:

```bash
translate -l "zh-CN" -nb
```

תרגום Markdown ותמונות:

```bash
translate -l "pt-BR" -md -img
```

עדכן תרגומים קיימים על ידי מחיקה ויצירה מחדש שלהם:

```bash
translate -l "ko" -u
```

הרץ ללא בקשות אינטראקטיביות:

```bash
translate -l "ko ja" -md -y
```

שמור לוגים:

```bash
translate -l "ko" -s
```

### אפשרויות

| אפשרות | דרוש | תיאור |
| --- | --- | --- |
| `-l`, `--language-codes` | כן | קודי שפה מופרדים ברווח, כגון `"es fr de"`, או `"all"`. |
| `-r`, `--root-dir` | לא | שורש הפרויקט. ברירת המחדל היא הספריה הנוכחית. |
| `-u`, `--update` | לא | מחק תרגומים קיימים לשפות הנבחרות ויצר אותם מחדש. |
| `-img`, `--images` | לא | תרגם רק קבצי תמונה. |
| `-md`, `--markdown` | לא | תרגם רק קבצי Markdown. |
| `-nb`, `--notebook` | לא | תרגם רק קבצי מחברות Jupyter. |
| `-d`, `--debug` | לא | הפעל רישום דיבאג בקונסול. |
| `-s`, `--save-logs` | לא | שמור לוגים ברמת DEBUG תחת `<root-dir>/logs/`. |
| `-x`, `--fix` | לא | תרגם מחדש קבצי Markdown בעלי ביטחון נמוך בהתבסס על תוצאות הערכות קודמות. |
| `-c`, `--min-confidence` | לא | סף ביטחון עבור `--fix`. ברירת המחדל היא `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | לא | הוסף או השתק הצהרות ויתור של תרגום מכונה. ב-CLI מוגדר כברירת מחדל כמאופשר. |
| `-f`, `--fast` | לא | מצב תמונה מהיר מיושן. |
| `-y`, `--yes` | לא | אשר אוטומטית בקשות, שימושי ב-CI. |
| `--repo-url` | לא | כתובת ה-URL של המאגר שמשמשת בעצה לגבי sparse-checkout בטבלת השפות ב-README. |
| `--migrate-language-folders` | לא | שנה שם תיקיות כינוי ישנות, כמו `cn` או `tw`, לתיקיות תקניות לפי BCP 47. |
| `--dry-run` | לא | הצג תצוגה מקדימה של הגירת תיקיות השפה והערכת תרגום מבלי לכתוב קבצים. |

אם לא סופק דגל סוג, `translate` מעבד Markdown, מחברות ותמונות. תרגום תמונות דורש הגדרת Azure AI Vision.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "ניסיוני"
    `evaluate` הוא ניסיוני. הוא יכול להשתמש בבדיקות איכות מבוססות כלל ובדיקות מבוססות LLM, כותב תוצאות הערכה למטא-נתוני התרגום, והתנהגות מודל הציונים והמטא-נתונים עשויה להשתנות.

```bash
evaluate -l "ko"
```

### דוגמאות נפוצות

השתמש בסף מחמיר יותר לביטחון נמוך:

```bash
evaluate -l "es" -c 0.8
```

הרץ בדיקות מבוססות כללים בלבד:

```bash
evaluate -l "fr" -f
```

הרץ בדיקות מבוססות LLM בלבד:

```bash
evaluate -l "ja" -D
```

### אפשרויות

| אפשרות | דרוש | תיאור |
| --- | --- | --- |
| `-l`, `--language-code` | כן | קוד שפה יחיד להערכה. קודי כינוי מנורמלים. |
| `-r`, `--root-dir` | לא | שורש הפרויקט. ברירת המחדל היא הספריה הנוכחית. |
| `-c`, `--min-confidence` | לא | הסף שמשמש בעת רישום תרגומים בעלי ביטחון נמוך. ברירת המחדל היא `0.7`. |
| `-d`, `--debug` | לא | אפשר רישום דיבאג. |
| `-s`, `--save-logs` | לא | שמור לוגים ברמת DEBUG תחת `<root-dir>/logs/`. |
| `-f`, `--fast` | לא | הערכה מבוססת כללים בלבד. |
| `-D`, `--deep` | לא | הערכה מבוססת LLM בלבד. |

ברירת המחדל, `evaluate` משתמש גם בהערכה מבוססת כללים וגם בהערכה מבוססת LLM. התוצאות נרשמות במטא-נתוני התרגום ומסוכמות בקונסול.

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "בטא"
    `co-op-review` היא פקודת סקירה דטרמיניסטית בגרסת בטא. היא לא קוראת לספקי מודלים ולא כותבת קבצים, אך הבדיקות שלה וסכימת פלט הבעיות עשויות להתפתח.

```bash
co-op-review -l "ko"
```

### דוגמאות נפוצות

סקור תרגומים לקוריאנית ויפנית מהספריה הנוכחית:

```bash
co-op-review -l "ko ja"
```

סקור שורש פרויקט ספציפי:

```bash
co-op-review -l "fr" -r ./my-course
```

סקור רק קבצי המקור ששונו ביחס להפניה בסיסית:

```bash
co-op-review -l "ko" --changed-from origin/main
```

הדפס פלט Markdown בסגנון GitHub לתמציות CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### אפשרויות

| אפשרות | דרוש | תיאור |
| --- | --- | --- |
| `-l`, `--language-code` | לא | קוד שפה לסקירה. ניתן להעביר אותו מספר פעמים או כערך מופרד ברווח. ברירת המחדל היא כל שפות התרגום שהתגלו. |
| `-r`, `--root-dir` | לא | שורש הפרויקט. ברירת המחדל היא הספריה הנוכחית. |
| `--changed-from` | לא | הפניה של Git שנועדה להגביל את הסקירה לקבצי מקור ששונו. |
| `--format` | לא | פורמט פלט: `text` או `github`. ברירת המחדל היא `text`. |

`co-op-review` בודק כרגע קבצים מתורגמים חסרים, מטא-נתוני תרגום חסרים או מיושנים, frontmatter של Markdown ותקינות גדרות הקוד, JSON של מחברת מתורגמת לא תקין, ויעדי קישורים מקומיים ל-Markdown או תמונות חסרים. קישורים חסרים מהווים אזהרות כברירת מחדל; בעיות מבניות ורעננות מביאות לכישלון הפקודה.

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [MCP Server](mcp.md) guide for client configuration, tools, resources, and safety notes.

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

Reprocess translated Markdown files and update notebook links so they point to translated notebooks when available.

```bash
migrate-links -l "ko ja"
```

### דוגמאות נפוצות

תצוגה מקדימה של עדכוני קישורים:

```bash
migrate-links -l "ko" --dry-run
```

עיבוד כל השפות הנתמכות ללא אישור:

```bash
migrate-links -l "all" -y
```

שכתב קישורים רק כאשר קיימות מחברות מתורגמות:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### אפשרויות

| אפשרות | דרוש | תיאור |
| --- | --- | --- |
| `-l`, `--language-codes` | כן | קודי שפה מופרדים ברווח, או `"all"`. |
| `-r`, `--root-dir` | לא | שורש הפרויקט. ברירת המחדל היא הספריה הנוכחית. |
| `--image-dir` | לא | תיקיית תמונות מתורגמות יחסית לשורש. ברירת המחדל היא `translated_images`. |
| `--dry-run` | לא | הצג קבצים שישתנו מבלי לכתוב עדכונים. |
| `--fallback-to-original`, `--no-fallback-to-original` | לא | השתמש בקישורים המקוריים למחברות כאשר מחברות מתורגמות חסרות. מופעל כברירת מחדל. |
| `-d`, `--debug` | לא | אפשר רישום דיבאג. |
| `-s`, `--save-logs` | לא | שמור לוגים ברמת DEBUG תחת `<root-dir>/logs/`. |
| `-y`, `--yes` | לא | אשר אוטומטית בקשות בעת עיבוד כל השפות. |

## Environment

All commands require one configured LLM provider:

```bash
# אז'ור OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# או OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Image translation additionally requires Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## מבנה הפלט

תרגומי טקסט נכתבים תחת:

```text
translations/<language-code>/<original-path>
```

פלט תמונות מתורגם נכתב תחת:

```text
translated_images/<language-code>/<original-path>
```

לדוגמה, תרגום של `README.md` ו-`docs/setup.md` לקוריאנית מייצר:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## דוגמאות CLI להעתקה והדבקה

תרגם Markdown לשלוש שפות:

```bash
translate -l "ko ja fr" -md
```

תרגם מחברות בלבד:

```bash
translate -l "zh-CN" -nb
```

תרגם תמונות בלבד:

```bash
translate -l "pt-BR" -img
```

הצג תצוגה מקדימה של תרגום Markdown מבלי לכתוב קבצים:

```bash
translate -l "de es" -md --dry-run
```

תקן תרגומי Markdown בעלי ביטחון נמוך:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

הרץ תרגום Markdown ידידותי ל-CI:

```bash
translate -l "ko ja" -md -y -s
```

סקור את הפלט המתורגם:

```bash
co-op-review -l "ko ja"
```

תצוגה מקדימה של הגירת קישורים:

```bash
migrate-links -l "ko" --dry-run
```