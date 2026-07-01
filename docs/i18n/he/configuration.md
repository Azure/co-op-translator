# הגדרות

Co-op Translator דורש ספק של מודל שפה אחד. תרגום תמונות דורש בנוסף את Azure AI Vision.

התצורה נקראת מתוך משתני סביבה. עבור פרויקטים מקומיים, מקמו אותם בקובץ `.env` בשורש הפרויקט.

להגדרת משאבי Azure, ראה [הגדרת Azure AI](azure-ai-setup.md).

## הגדרת הסביבה המקומית

השתמשו בסביבת וירטואלית לפני הרצת ה-CLI באופן מקומי. Co-op Translator תומך ב-Python 3.10 עד 3.12.

להרצת ה-CLI באופן רגיל, התקינו את החבילה שפורסמה בתוך סביבת וירטואלית:

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

לעבודה על הריפוזיטורי, התקינו תלויות משורש הפרויקט במקום זאת:

```bash
poetry install
poetry run translate --help
```

לאחר שה-CLI זמין, הגדירו ספק אחד של מודל שפה בקובץ `.env`.

## בחירת ספק

הכלי מזהה באופן אוטומטי את הספקים לפי הסדר הבא:

1. Azure OpenAI
2. OpenAI

אם אף אחד מהספקים אינו מוגדר, `translate`, `evaluate`, `migrate-links`, ו-`run_translation` ייכשלו במהלך בדיקות התצורה. `co-op-review` ו-`run_review` הן בדיקות תחזוקה דטרמיניסטיות ואינן דורשות אישורים של ספק.

## Azure OpenAI

יש להשתמש ב-Azure OpenAI כאשר המודל שלכם מותקן ב-Azure AI Foundry או ב-Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

בדיקת הקישוריות בודקת את נקודת הקצה, מפתח ה-API, גרסת ה-API ושם הפריסה לפני תחילת התרגום.

## OpenAI

יש להשתמש ב-OpenAI כאשר קוראים ישירות ל-OpenAI API.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # אופציונלי
OPENAI_BASE_URL="..."        # אופציונלי
```

`OPENAI_CHAT_MODEL_ID` נדרש מכיוון שהמתרגם צריך מודל צ'אט מפורש לקריאות API.

## Azure AI Vision

תרגום תמונות דורש את Azure AI Vision כדי שהכלי יוכל להוציא טקסט מתמונות לפני תרגומו.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

אם תרגום תמונות נבחר עם `-img`, `images=True`, או ללא מסנן סוג-תוכן, הכלי מאמת את תצורת Vision לפני תחילת התרגום.

## מספר ערכות אישורים

שכבת התצורה תומכת במספר ערכות אישורים על ידי הוספת סיומת למשתנים עם אותו אינדקס:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

כל ערכה חייבת להיות מלאה. בדיקת הבריאות (health check) בוחרת ערכה שפועלת לפני שהתרגום מתקדם.

## דרישות פקודות

| פקודה או API | נדרש LLM | נדרש Vision | הערות |
| --- | --- | --- | --- |
| `translate -md` | כן | לא | מתרגם רק Markdown. |
| `translate -nb` | כן | לא | מתרגם רק מחברות. |
| `translate -img` | כן | כן | מתרגם רק תמונות. |
| `translate` ללא דגלי סוג | כן | כן | מצב ברירת המחדל כולל Markdown, מחברות ותמונות. |
| `evaluate` | כן | לא | משתמש בהערכה באמצעות LLM אלא אם נבחרה `--fast`. |
| `migrate-links` | כן | לא | מבצע העברת קישורים, אבל עדיין מריץ בדיקות תצורה משותפות. |
| `co-op-review` | לא | לא | מריץ בדיקות דטרמיניסטיות של מבנה תרגום, עדכניות, Markdown, מחברות, ובדיקות קישורים מקומיים. |
| `run_translation(markdown=True)` | כן | לא | תרגום Markdown תכנותי. |
| `run_translation(images=True)` | כן | כן | תרגום תמונות תכנותי. |
| `run_review(...)` | לא | לא | בדיקה דטרמיניסטית תכנותית. |

## תיקיות פלט

פלט ברירת המחדל של תרגום טקסט:

```text
translations/<language-code>/<source-relative-path>
```

פלט ברירת המחדל לתמונות מתורגמות:

```text
translated_images/<language-code>/<source-relative-path>
```

ממשק ה-Python יכול לדרוס תיקיות אלו עם `translations_dir` ו-`image_dir`.