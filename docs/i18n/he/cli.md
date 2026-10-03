# מדריך שורת הפקודה (CLI)

Co-op Translator מתקין נקודות כניסה לשורת הפקודה הבאות:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

הפקודות `translate`, `evaluate`, `migrate-links` ו-`co-op-review` מנותבות דרך `co_op_translator.__main__`, שלפיו נבחר מימוש הפקודה על פי שם הסקריפט שהופעל. שרת ה-MCP משתמש ישירות ב-`co_op_translator.mcp.server`.

אם אתם מתלבטים בין CLI, Python API, ו‑MCP, התחילו עם [בחר את זרימת העבודה](workflows.md).

## פלט למסוף

טרמינלים אינטראקטיביים משתמשים בעיצוב Rich עבור כותרת הפקודה, סרגלי ההתקדמות והסיכומים. פלט ב‑CI ובמצבים לא אינטראקטיביים חוזר אוטומטית לטקסט פשוט.

הגדר את `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` כדי לכפות פלט פשוט, או `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` כדי לכפות פלט Rich. הגדר `CO_OP_TRANSLATOR_NO_PROGRESS=1` כדי לשמור על סיכומים תוך דיכוי פסי התקדמות חיים.

השתמש ב-`translate --json-events progress.ndjson` כאשר מערכת אחרת זקוקה ל
התקדמות הניתנת לקריאה על-ידי מכונה. ה-CLI ממשיך להציג פלט המיועד לבני אדם, בעוד
קובץ NDJSON מקבל אירועי `co-op.translation.event.v1` בגרסאות עם
שדות יציבים כגון `type`, `stage_key`, `completed`, `total`, ו
`current_path`.

## זרימת CLI בפעם הראשונה

התחילו כאן אם אתם משתמשים ב‑Co-op Translator מהטרמינל:

1. קבעו ספק LLM כפי שמתואר ב‑[תצורה](configuration.md).
2. בחרו את סוג התוכן שברצונכם לתרגם.
3. הריצו תחילה פקודה ממוקדת, כגון תרגום Markdown בלבד.
4. השתמשו ב‑`--dry-run` לפני שינויים משמעותיים במאגר.
5. השתמשו ב‑`co-op-review` לאחר התרגום כדי לבדוק מבנה ורעננות.

| מטרה | פקודה להתחלה |
| --- | --- |
| תרגום מסמכי Markdown | `translate -l "ko" -md` |
| תרגום מחברות | `translate -l "ko" -nb` |
| תרגום טקסט בתמונות | `translate -l "ko" -img` |
| תצוגה מקדימה של העבודה ללא כתיבת קבצים | `translate -l "ko" -md --dry-run` |
| סקירת תרגומים קיימים | `co-op-review -l "ko"` |
| עדכון קישורים למחברות ו‑Markdown | `migrate-links -l "ko" --dry-run` |
| הנגשת כלים ללקוח MCP | קבעו את [שרת MCP](mcp.md) במקום להריץ פקודות CLI באופן ישיר. |

## translate

תרגום קבצי Markdown, מחברות וטקסט שבתמונות לשפה אחת או יותר.

```bash
translate -l "ko ja fr"
```

### דוגמאות נפוצות

תרגום Markdown בלבד:

```bash
translate -l "de" -md
```

תרגום מחברות בלבד:

```bash
translate -l "zh-CN" -nb
```

Translate Markdown and images:

```bash
translate -l "pt-BR" -md -img
```

עדכן תרגומים קיימים על ידי מחיקה ויצירה מחדש שלהם:

```bash
translate -l "ko" -u
```

Run without interactive prompts:

```bash
translate -l "ko ja" -md -y
```

שמירת יומנים:

```bash
translate -l "ko" -s
```

כתיבת אירועי התקדמות מובנים:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### אפשרויות

| אפשרות | נדרש | תיאור |
| --- | --- | --- |
| `-l`, `--language-codes` | כן | קודי שפה מופרדים ברווח, כגון `"es fr de"`, או `"all"`. |
| `-r`, `--root-dir` | לא | ספריית שורש של הפרויקט. ברירת המחדל היא הספרייה הנוכחית. |
| `-u`, `--update` | לא | מחק תרגומים קיימים לשפות הנבחרות ויצר אותם מחדש. |
| `-img`, `--images` | לא | תרגם רק קבצי תמונה. |
| `-md`, `--markdown` | לא | תרגם רק קבצי Markdown. |
| `-nb`, `--notebook` | לא | תרגם רק קבצי Jupyter notebook. |
| `-d`, `--debug` | לא | הפעל רישום ברמת דיבוג בקונסול. |
| `-s`, `--save-logs` | לא | שמור יומני רישום ברמת DEBUG תחת `<root-dir>/logs/`. |
| `--json-events` | לא | כתוב אירועי התקדמות של תרגום בפורמט לקריאה מכנית כ‑NDJSON. |
| `-x`, `--fix` | לא | תרגם מחדש קבצי Markdown בעלי ביטחון נמוך בהתאם לתוצאות ההערכה הקודמות. |
| `-c`, `--min-confidence` | לא | סף ביטחון עבור `--fix`. ברירת המחדל היא `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | לא | הוסף או השבת הודעות הבהרה של תרגום ממכונה. ברירת המחדל ב‑CLI היא שהן מאופשרות. |
| `-f`, `--fast` | לא | מצב מהיר לתמונות מיושן. |
| `-y`, `--yes` | לא | אשר אוטומטית הודעות, מועיל ב‑CI. |
| `--repo-url` | לא | כתובת המאגר המשמש בעצת sparse-checkout בטבלת השפות ב‑README. |
| `--migrate-language-folders` | לא | שנה שמות תיקיות כינויים ישנות, כגון `cn` או `tw`, לתיקיות תקניות לפי BCP 47. |
| `--dry-run` | לא | הצג תצוגה מקדימה של הגירת תיקיות שפה והערכות תרגום ללא כתיבת קבצים. |

אם לא נמסר דגל סוג, `translate` מעבד Markdown, מחברות ותמונות. תרגום תמונות דורש תצורת Azure AI Vision.

## evaluate

הערכת איכות תרגומי Markdown עבור שפה אחת.

!!! warning "נסיוני"
    `evaluate` היא ניסיונית. היא יכולה להשתמש בבדיקות איכות מבוססות חוקים ובבדיקות מבוססות LLM, כותבת תוצאות הערכה למטא-נתוני התרגום, ומודל הניקוד שלה והתנהגות המטא-נתונים עלולים להשתנות.

```bash
evaluate -l "ko"
```

### דוגמאות נפוצות

השתמש בסף ביטחון נמוך מחמיר יותר:

```bash
evaluate -l "es" -c 0.8
```

הרץ בדיקות מבוססות-כללים בלבד:

```bash
evaluate -l "fr" -f
```

הרץ בדיקות מבוססות LLM בלבד:

```bash
evaluate -l "ja" -D
```

### אפשרויות

| אפשרות | נדרש | תיאור |
| --- | --- | --- |
| `-l`, `--language-code` | כן | קוד שפה יחיד להערכה. קודי כינוי מנורמלים. |
| `-r`, `--root-dir` | לא | ספריית השורש של הפרויקט. ברירת המחדל היא הספרייה הנוכחית. |
| `-c`, `--min-confidence` | לא | סף המשמש בעת רישום תרגומים בעלי ביטחון נמוך. ברירת המחדל היא `0.7`. |
| `-d`, `--debug` | לא | הפעל רישום דיבוג. |
| `-s`, `--save-logs` | לא | שמור יומני רישום ברמת DEBUG תחת `<root-dir>/logs/`. |
| `-f`, `--fast` | לא | הערכה מבוססת-כללים בלבד. |
| `-D`, `--deep` | לא | הערכה מבוססת LLM בלבד. |

כברירת מחדל, `evaluate` משתמש הן בהערכה מבוססת-כללים והן בהערכה מבוססת LLM. התוצאות נכתבות למטא-נתוני התרגום ומסוכמות בקונסול.

## co-op-review

הרץ בדיקות תחזוקה של תרגום דטרמיניסטיות ללא אישורי API.

!!! note "בטא"
    `co-op-review` היא פקודת סקירה דטרמיניסטית בבטא. היא לא קוראת לספקי מודלים או כותבת קבצים, אבל הבדיקות שלה וסכמת פלט הבעיות עשויות להתפתח.

```bash
co-op-review -l "ko"
```

### דוגמאות נפוצות

סקור תרגומים לקוריאנית ויפנית מהספרייה הנוכחית:

```bash
co-op-review -l "ko ja"
```

סקור שורש פרויקט מסוים:

```bash
co-op-review -l "fr" -r ./my-course
```

סקור רק את ה‑README לאחר תרגום מסוג README בלבד:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` מתעלם ממסמכים אחרים ו‑READMEים מקוננים. הוא נכשל אם השורש
`README.md` חסר. בשילוב עם `--changed-from`, הוא בודק רק את ה‑README
כאשר קובץ המקור הזה השתנה. תרגום מסוג README בלבד משאיר את קובץ ה‑README המקורי
ללא שינוי, כולל כל סימני מקטעים משותפים.

סקור רק קבצי המקור שהשתנו ביחס ל‑ref בסיסי:

```bash
co-op-review -l "ko" --changed-from origin/main
```

הדפס פלט Markdown בסגנון GitHub לסיכומי CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### אפשרויות

| אפשרות | נדרש | תיאור |
| --- | --- | --- |
| `-l`, `--language-code` | לא | קוד שפה לסקירה. ניתן להעביר מספר פעמים או כערך מופרד ברווח. ברירת המחדל היא כל שפות התרגום שהתגלו. |
| `-r`, `--root-dir` | לא | ספריית השורש של הפרויקט. ברירת המחדל היא הספרייה הנוכחית. |
| `--changed-from` | לא | Git ref המשמש להגבלת הסקירה לקבצי מקור שהשתנו. |
| `--readme-only` | לא | סקור רק את תרגום קובץ השורש `README.md`. |
| `--format` | לא | פורמט הפלט: `text` או `github`. ברירת המחדל היא `text`. |

`co-op-review` בודק כעת קבצים מתורגמים חסרים, מטא-נתוני תרגום חסרים או מיושנים, שלמות frontmatter של Markdown וסגירות גדרות הקוד, JSON של מחברות מתורגמות לא תקין, ויעדי קישורים מקומיים ב‑Markdown או בתמונות חסרים. קישורים חסרים הם אזהרות כברירת מחדל; בעיות מבניות ורעננות גורמות לכישלון הפקודה.

## co-op-translator-mcp

הרץ את שרת ה‑Co-op Translator MCP עבור סוכנים, עורכים ולקוחות תואמי MCP.

```bash
co-op-translator-mcp
```

אמצעי התקשורת ברירת המחדל הוא `stdio`. עיין במדריך [MCP Server](mcp.md) עבור הגדרת הלקוח, כלים, משאבים והערות בטיחות.

### אפשרויות

| אפשרות | נדרש | תיאור |
| --- | --- | --- |
| `--transport` | לא | העברת MCP: `stdio`, `streamable-http`, או `sse`. ברירת המחדל היא `stdio`. |

## migrate-links

עבד מחדש קבצי Markdown מתורגמים ועדכן קישורים למחברות כך שיצביעו למחברות מתורגמות כשזמינות.

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

כתוב מחדש קישורים רק כאשר מחברות מתורגמות קיימות:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### אפשרויות

| אפשרות | נדרש | תיאור |
| --- | --- | --- |
| `-l`, `--language-codes` | כן | קודי שפה מופרדים ברווח, או `"all"`. |
| `-r`, `--root-dir` | לא | ספריית השורש של הפרויקט. ברירת המחדל היא הספרייה הנוכחית. |
| `--image-dir` | לא | תיקיית תמונות מתורגמות יחסית לשורש. ברירת המחדל היא `translated_images`. |
| `--dry-run` | לא | הצג קבצים שישתנו ללא כתיבת עדכונים. |
| `--fallback-to-original`, `--no-fallback-to-original` | לא | השתמש בקישורים המקוריים למחברות כאשר מחברות מתורגמות חסרות. מאופשר כברירת מחדל. |
| `-d`, `--debug` | לא | הפעל רישום דיבוג. |
| `-s`, `--save-logs` | לא | שמור יומני רישום ברמת DEBUG תחת `<root-dir>/logs/`. |
| `-y`, `--yes` | לא | אשר אוטומטית הודעות בעת עיבוד כל השפות. |

## סביבה

כאשר פקודה דורשת אישורי ספק, קבעו אחד מערכי הספקים האלה. `translate --dry-run` ו‑`co-op-review` אינם דורשים אישורי ספק:

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

# או Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

תרגום תמונות דורש בנוסף את Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## פריסת הפלט

תרשומים טקסטיים נכתבים תחת:

```text
translations/<language-code>/<original-path>
```

פלט תמונות מתורגמות נכתב תחת:

```text
translated_images/<language-code>/<original-path>
```

לדוגמה, תרגום של `README.md` ו־`docs/setup.md` לקוריאנית מייצר:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## דוגמאות להעתקה והדבקה (CLI)

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

תצוגת תרגום Markdown ללא כתיבת קבצים:

```bash
translate -l "de es" -md --dry-run
```

תקן תרגומי Markdown בעלי ביטחון נמוך:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

הרץ תרגום Markdown ידידותי ל‑CI:

```bash
translate -l "ko ja" -md -y -s
```

סקור פלט מתורגם:

```bash
co-op-review -l "ko ja"
```

תצוגה מקדימה של הגירת קישורים:

```bash
migrate-links -l "ko" --dry-run
```