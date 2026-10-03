# תצורה

Co-op Translator דורש ספק מודל שפה אחד. תרגום תמונות דורש בנוסף את Azure AI Vision.

ההגדרה נקראת מתוך משתני סביבה. עבור פרויקטים מקומיים, הניחו אותם בקובץ `.env` בשורש הפרויקט.

להגדרת משאבי Azure, ראו [הגדרת Azure AI](azure-ai-setup.md).

## הגדרת סביבה מקומית

השתמשו בסביבת וירטואלית לפני הרצת ה-CLI מקומית. Co-op Translator תומך ב-Python 3.11 עד 3.14.

לשימוש רגיל ב-CLI, התקינו את החבילה המתפרסמת בתוך סביבת וירטואלית:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### פיתוח המאגר

עבור פיתוח המאגר, התקינו את התלויות משורש הפרויקט במקום זאת:

```bash
poetry install
poetry run translate --help
```

לאחר שה-CLI זמין, הגדירו ספק מודל שפה אחד בקובץ `.env`.

## בחירת ספק

הכלי מזהה ספקים באופן אוטומטי בסדר הבא:

1. Azure OpenAI
2. OpenAI
3. Anthropic

תרגום דורש אישורי ספק, פרט לתצוגות מקדימות כגון `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review` ו-`run_review` הן פעולות תחזוקה דטרמיניסטיות ואינן דורשות אישורי ספק.

## רכיב backend של לקוח המודל

החל מ-Co-op Translator 0.22.0, Azure OpenAI, OpenAI ו-Anthropic משתמשים ב-Microsoft Agent Framework כברירת מחדל. לא נדרש הגדרת backend לשימוש רגיל.

Semantic Kernel נשאר זמין זמנית לצורך תאימות. לבחירתו במפורש, קבעו:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

השימוש ב-Semantic Kernel מפיק אזהרת פינוי. מתוכנן להעביר את Semantic Kernel לתלות אופציונלית ב-0.23.0 ולהסיר את האינטגרציה ב-0.24.0, בכפוף לתוצאות תאימות ומשוב משתמשים. Anthropic דורש `agent-framework`; בחירה מפורשת של `semantic-kernel` עם Anthropic נכשלת בשגיאת תצורה. ערכים לא תקינים נכשלו במהלך אתחול המתרגם הנתמך על ידי ספק במקום לחזור חזרה בשקט. עקבו אחר ההשקה ודווחו על חסמים ב-[GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

השתמשו ב-Azure OpenAI כאשר המודל שלכם מופעל ב-Azure AI Foundry או ב-Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

בדיקת החיבור משתמשת ב-endpoint, מפתח ה-API, גרסת ה-API ושם הפריסה לפני תחילת התרגום.

## OpenAI

השתמשו ב-OpenAI כאשר קוראים ל-OpenAI API ישירות.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` נדרש כי המתרגם צריך מודל צ'אט מפורש לקריאות ה-API.

השאירו את `OPENAI_ORG_ID` ו-`OPENAI_BASE_URL` ללא הגדרה עבור ההגדרה ברירת המחדל. הוסיפו מזהה ארגון רק אם החשבון שלכם זקוק לו, או URL בסיסי רק בעת שימוש בנקודת קצה מותאמת. אל תעתיקו ערכי מציין מיקום עבור הגדרות אופציונליות.

## Anthropic Claude

השתמשו ב-Anthropic כאשר קוראים ל-Claude API ישירות. צרו [מפתח API של Anthropic](https://platform.claude.com/docs/en/get-started) ובחרו [מזהה מודל Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) נתמך.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` ו-`ANTHROPIC_MODEL` נדרשים. אין צורך להגדיר את `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework הוא ה-backend כברירת מחדל.

השאירו את `ANTHROPIC_BASE_URL` לא מוגדר עבור ה-Anthropic API. הגדירו אותו רק בעת שימוש בנקודת קצה מותאמת.

`ANTHROPIC_MAX_TOKENS` ברירת המחדל היא `8192`, מה שמשאיר מקום לסקריפטים עשירים בטוקנים כגון Meitei Mayek. הקטינו אותו אם המודל שלכם או נקודת הקצה התואמת ל-Anthropic מגבילים פלט מתחת לכך.

## Azure AI Vision

תרגום תמונות דורש את Azure AI Vision כך שהכלי יוכל להוציא טקסט מתמונות לפני שמודל השפה המוגדר יתרגם אותו. Anthropic יכול לתרגם את הטקסט המופק בדיוק כמו Azure OpenAI או OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

אם תרגום תמונות נבחר עם `-img`, `images=True`, או ללא מסנן סוג תוכן, הכלי מאמת את תצורת Vision לפני תחילת התרגום.

## ערכות אישורים מרובות

שכבת התצורה תומכת בערכות אישורים מרובות על ידי הוספת סיומת זהה למשתנים:

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

כל ערכה חייבת להיות שלמה. בדיקת הבריאות בוחרת ערכה שעובדת לפני שממשיכים בתרגום.

OpenAI ו-Anthropic תומכים באותה קונבנציה של סיומות. שמרו כל משתנה בערכת אישורים על אותה סיומת, כולל ערכים אופציונליים כגון `OPENAI_BASE_URL_1` או `ANTHROPIC_BASE_URL_1`.

## דרישות פקודות

| פקודה או API | דרוש LLM | דרוש Vision | הערות |
| --- | --- | --- | --- |
| `translate -md` | כן | לא | מתרגם Markdown בלבד. |
| `translate -nb` | כן | לא | מתרגם רק מחברות. |
| `translate -img` | כן | כן | מתרגם תמונות בלבד. |
| `translate` with no type flags | כן | כן | מצב ברירת המחדל כולל Markdown, מחברות ותמונות. |
| `evaluate` | כן | לא | משתמש בהערכת LLM אלא אם נבחר `--fast`. |
| `migrate-links` | לא | לא | מבצע העברת קישורים מקומית ללא קריאות לספק. |
| `co-op-review` | לא | לא | מריץ בדיקות דטרמיניסטיות למבנה תרגום, רעננות, Markdown, מחברות ובדיקות קישורים מקומיות. |
| `run_translation(markdown=True)` | כן | לא | תרגום Markdown תכנותי. |
| `run_translation(images=True)` | כן | כן | תרגום תמונות תכנותי. |
| `run_review(...)` | לא | לא | סקירה דטרמיניסטית תכנותית. |

## תיקיות פלט

תיקיית פלט ברירת מחדל לתרגום טקסט:

```text
translations/<language-code>/<source-relative-path>
```

תיקיית פלט ברירת מחדל לתמונות מתורגמות:

```text
translated_images/<language-code>/<source-relative-path>
```

ממשק ה-Python יכול לעקוף תיקיות אלה עם `translations_dir` ו-`image_dir`.