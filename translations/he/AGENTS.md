<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:30:09+00:00",
  "source_file": "AGENTS.md",
  "language_code": "he"
}
-->
## סקירה כללית של הפרויקט

Co‑op Translator הוא כלי שורת פקודה ב‑Python ו‑GitHub Actions workflow שמתרגם קבצי Markdown, מחברות Jupyter וטקסט מתוך תמונות למספר שפות. הוא מארגן את הפלטים בתיקיות ייעודיות לכל שפה ושומר על סנכרון בין התרגומים לתוכן המקור. הפרויקט בנוי כספרייה המנוהלת על ידי Poetry עם נקודות כניסה ל‑CLI.

### סקירה ארכיטקטונית

- נקודות כניסה ל‑CLI (`translate`, `migrate-links`, `evaluate`) מפעילות CLI אחיד שמנתב לזרימות תרגום, העברת קישורים והערכה.
- טוען ההגדרות קורא את `.env` ומזהה אוטומטית את ספק ה‑LLM (Azure OpenAI או OpenAI) ואם נדרש, גם את ספק הראייה (Azure AI Service) לחילוץ טקסט מתמונות.
- ליבת התרגום מטפלת ב‑Markdown ובמחברות; צינור הראייה מחלץ טקסט מתמונות כאשר משתמשים ב‑`-img`.
- הפלטים מאורגנים תחת `translations/<lang>/` לטקסט ו‑`translated_images/` לתמונות, תוך שמירה על מבנה המקור.

### טכנולוגיות ומסגרות עיקריות

- Python 3.10–3.12, Poetry לאריזה
- CLI: `click`
- SDKs ל‑LLM/AI: Azure OpenAI, OpenAI
- ראייה: Azure AI Service (Computer Vision)
- HTTP ונתונים: `httpx`, `pydantic`
- עיבוד תמונה: `pillow`, `opencv-python`, `matplotlib`
- כלים: `pytest`, `black`, `ruff`

## פקודות התקנה

### דרישות מקדימות

- Python 3.10–3.12
- מנוי Azure (אופציונלי, לשירותי Azure AI)
- גישה לאינטרנט ל‑APIs של LLM/ראייה (למשל Azure OpenAI/OpenAI, Azure AI Vision)

### אפשרות א': Poetry (מומלץ)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### אפשרות ב': pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## שימוש למשתמשי קצה

### Docker (תמונה שפורסמה)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

הערות:
- נקודת הכניסה ברירת מחדל היא `translate`. ניתן להחליף ל‑`--entrypoint migrate-links` להעברת קישורים.
- ודא ש‑GHCR package מוגדר כ‑Public כדי לאפשר משיכות אנונימיות.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### הגדרת סביבת עבודה

צור קובץ `.env` בשורש המאגר וספק פרטי גישה/נקודות קצה למודל השפה שבחרת ולשירות הראייה (אופציונלי). להנחיות התקנה לפי ספק, ראה `getting_started/set-up-azure-ai.md`.

### משתני סביבה נדרשים

לפחות ספק LLM אחד חייב להיות מוגדר. לתרגום תמונות, יש להגדיר גם את Azure AI Service.

- Azure OpenAI (תרגום טקסט):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (חלופה לתרגום טקסט):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (אופציונלי)
  - `OPENAI_CHAT_MODEL_ID` (נדרש בשימוש עם OpenAI)
  - `OPENAI_BASE_URL` (אופציונלי; ברירת מחדל: `https://api.openai.com/v1`)

- Azure AI Service לחילוץ טקסט מתמונות (נדרש בשימוש ב‑`-img`):
  - `AZURE_AI_SERVICE_API_KEY` (מומלץ) או `AZURE_SUBSCRIPTION_KEY` הישן
  - `AZURE_AI_SERVICE_ENDPOINT`

דוגמת קטע `.env`:

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

הערות:

- הכלי מזהה אוטומטית את ספק ה‑LLM הזמין; הגדר או Azure OpenAI או OpenAI.
- תרגום תמונות דורש גם את `AZURE_AI_SERVICE_API_KEY` וגם את `AZURE_AI_SERVICE_ENDPOINT`.
- ה‑CLI יתריע בבירור אם חסרים משתנים נדרשים.

## תהליך פיתוח

- קוד המקור נמצא תחת `src/co_op_translator`; בדיקות תחת `tests/`.
- CLIs עיקריים (מותקנים דרך entry points):

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

ראה תיעוד שימוש נוסף ב‑`getting_started/`.

## הוראות בדיקה

הרץ בדיקות משורש המאגר. חלק מהבדיקות דורשות פרטי API; דלג עליהן במידת הצורך.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

כיסוי אופציונלי (דורש `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## הנחיות סגנון קוד

- מעצב: Black (מוגדר ב‑`pyproject.toml`, אורך שורה 88)
- בודק סגנון: Ruff (מוגדר ב‑`pyproject.toml`, אורך שורה 120)
- בדיקות טיפוס: mypy (הגדרה קיימת; הפעל אם מותקן)

פקודות:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

ארגן קוד Python תחת `src/`, בדיקות תחת `tests/`, והעדף ייבוא מפורש בתוך מרחב השמות של החבילה (`co_op_translator.*`).

## בנייה ופריסה

תוצרי בנייה מתפרסמים תחת `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

אוטומציה באמצעות GitHub Actions נתמכת; ראה:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### תמונת קונטיינר (GHCR)

- תמונה רשמית: `ghcr.io/azure/co-op-translator:<tag>`
- תגיות: `latest` (ב‑main), תגיות סמנטיות כמו `vX.Y.Z`, ותגית `sha`
- Multi-arch: תמיכה ב‑`linux/amd64, linux/arm64` דרך Buildx
- תבנית Dockerfile: בניית dependency wheels בשלב builder (עם `build-essential` ו‑`python3-dev`) והתקנה מ‑wheelhouse מקומי בשלב הריצה (`pip install --no-index --find-links=/wheels`)
- תהליך עבודה: `.github/workflows/docker-publish.yml` בונה ודוחף ל‑GHCR

## שיקולי אבטחה

- שמור מפתחות API ונקודות קצה ב‑`.env` או בחנות הסודות של ה‑CI; לעולם אל תעלה סודות למאגר.
- לתרגום תמונות, יש צורך במפתחות/נקודות קצה של Azure AI Vision; אחרת דלג על `-img`.
- בדוק מכסות/הגבלות ספק לפני הרצת אצוות תרגום גדולות.

## הנחיות Pull Request

### לפני שליחה

1. **בדוק את השינויים שלך:**
   - הרץ מחברות רלוונטיות במלואן
   - ודא שכל התאים פועלים ללא שגיאות
   - בדוק שהפלטים מתאימים

2. **עדכוני תיעוד:**
   - עדכן את `README.md` אם הוספת מושגים חדשים
   - הוסף הערות במחברות עבור קוד מורכב
   - ודא שתאי markdown מסבירים את המטרה

3. **שינויים בקבצים:**
   - הימנע מהעלאת קבצי `.env` (השתמש ב‑`.env.example`)
   - אל תעלה תיקיות `venv/` או `__pycache__/`
   - שמור פלטי מחברות כאשר הם מדגימים מושגים
   - הסר קבצים זמניים וגיבויים (`*-backup.ipynb`)

4. **סגנון ועיצוב:**
   - פעל לפי הנחיות הסגנון והעיצוב
   - הרץ `poetry run black .` ו‑`poetry run ruff check .` לבדוק בעיות סגנון ועיצוב

5. **הוסף/עדכן בדיקות ועזרה ל‑CLI:**
   - הוסף או עדכן בדיקות כאשר משנים התנהגות
   - שמור את עזרת ה‑CLI מעודכנת בהתאם לשינויים


### הודעת קומיט ואסטרטגיית מיזוג

אנו משתמשים ב‑Squash and Merge כברירת מחדל. הודעת הקומיט הסופית צריכה להיות בפורמט:

```bash
<type>: <description> (#<PR number>)
```

סוגים מותרים:
- `Docs` — עדכוני תיעוד
- `Build` — מערכת בנייה, תלויות, קונפיגורציה/CI
- `Core` — פונקציונליות ותכונות ליבה (למשל `src/co_op_translator/core`)

דוגמאות:
- `Docs: עדכון הוראות התקנה להבהרה (#50)`
- `Core: שיפור טיפול בתרגום תמונות (#60)`

הערות:
- כותרות PR מקבלות לעיתים קידומת אוטומטית לפי תוויות; ודא שהקידומת נכונה.

### פורמט כותרת PR

השתמש בכותרות ברורות ותמציתיות. העדף את אותו מבנה כמו הודעת הקומיט הסופית:
- `Docs: עדכון הוראות התקנה להבהרה`
- `Core: שיפור טיפול בתרגום תמונות`

## ניפוי באגים ופתרון תקלות

- בעיות נפוצות ופתרונות: `getting_started/troubleshooting.md`
- שפות נתמכות והערות (כולל גופנים/בעיות ידועות): `getting_started/supported-languages.md`
- לבעיות קישורים במחברות, הרץ מחדש: `migrate-links -l "all" -y`

## הערות לסוכנים

- העדף Poetry לסביבות ניתנות לשחזור; אחרת השתמש ב‑`requirements.txt`.
- בהרצת CLIs ב‑CI, ספק סודות נדרשים דרך משתני סביבה או הזרקת `.env`.
- לצרכני מונורפו, מאגר זה פועל כחבילה עצמאית; אין צורך בתיאום תתי‑חבילות.

- הנחיות multi-arch: שמור על `linux/arm64` כאשר יש משתמשי ARM (Apple Silicon/שרתים מבוססי ARM); אחרת `linux/amd64` בלבד מספק.
- הפנה משתמשים ל‑Docker Quick Start ב‑`README.md` כאשר הם מעדיפים שימוש בקונטיינר; כלול דוגמאות Bash ו‑PowerShell בשל הבדלי מרכאות.

---

**הצהרת אחריות**:
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עשויים להכיל טעויות או אי-דיוקים. יש לראות במסמך המקורי בשפתו המקורית כמקור הסמכותי. למידע קריטי, מומלץ לפנות לתרגום מקצועי על ידי אדם. איננו אחראים לכל אי-הבנות או פירושים שגויים הנובעים מהשימוש בתרגום זה.