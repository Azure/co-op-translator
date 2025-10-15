<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9fac847815936ef6e6c8bfde6d191571",
  "translation_date": "2025-10-15T03:33:37+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-org.md",
  "language_code": "he"
}
-->
# שימוש ב-GitHub Action של Co-op Translator (מדריך לארגונים)

**קהל יעד:** מדריך זה מיועד ל**משתמשים פנימיים של Microsoft** או **צוותים שיש להם גישה לאישורים הנדרשים עבור Co-op Translator GitHub App המובנה** או שיכולים ליצור GitHub App מותאם אישית משלהם.

הפכו את תהליך תרגום התיעוד במאגר שלכם לאוטומטי בקלות בעזרת Co-op Translator GitHub Action. מדריך זה יסביר כיצד להגדיר את הפעולה כך שתיצור Pull Requests עם תרגומים מעודכנים בכל פעם שקבצי Markdown או תמונות במקור משתנים.

> [!IMPORTANT]
> 
> **בחירת המדריך הנכון:**
>
> מדריך זה מפרט הגדרה באמצעות **GitHub App ID ומפתח פרטי**. בדרך כלל תצטרכו את שיטת "מדריך הארגון" הזו אם: **`GITHUB_TOKEN` מוגבל בהרשאות:** ההגדרות בארגון או במאגר שלכם מגבילות את ההרשאות המוגדרות כברירת מחדל ל-`GITHUB_TOKEN`. במיוחד, אם ל-`GITHUB_TOKEN` אין הרשאות `write` הנדרשות (כמו `contents: write` או `pull-requests: write`), תהליך העבודה במדריך הציבורי ([Public Setup Guide](./github-actions-guide-public.md)) ייכשל עקב חוסר הרשאות. שימוש ב-GitHub App ייעודי עם הרשאות מפורשות עוקף מגבלה זו.
>
> **אם זה לא רלוונטי עבורכם:**
>
> אם ל-`GITHUB_TOKEN` הסטנדרטי יש הרשאות מספקות במאגר שלכם (כלומר, אין מגבלות ארגוניות), השתמשו ב**[מדריך ההגדרה הציבורי עם GITHUB_TOKEN](./github-actions-guide-public.md)**. המדריך הציבורי אינו דורש קבלת App ID או מפתח פרטי, ומסתמך רק על `GITHUB_TOKEN` וההרשאות במאגר.

## דרישות מקדימות

לפני הגדרת ה-GitHub Action, ודאו שיש לכם את האישורים לשירותי ה-AI הדרושים.

**1. חובה: אישורי מודל שפה (AI)**
יש צורך באישורים לפחות לאחד ממודלי השפה הנתמכים:

- **Azure OpenAI**: דורש Endpoint, API Key, שמות מודל/פריסה, גרסת API.
- **OpenAI**: דורש API Key, (אופציונלי: Org ID, Base URL, Model ID).
- ראו [מודלים ושירותים נתמכים](../../../../README.md) לפרטים.
- מדריך הגדרה: [הגדרת Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. אופציונלי: אישורי Computer Vision (לתרגום טקסט בתמונות)**

- דרוש רק אם יש צורך לתרגם טקסט מתוך תמונות.
- **Azure Computer Vision**: דורש Endpoint ו-Subscription Key.
- אם לא תספקו, הפעולה תעבוד ב[מצב Markdown בלבד](../markdown-only-mode.md).
- מדריך הגדרה: [הגדרת Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## הגדרה וקונפיגורציה

בצעו את השלבים הבאים כדי להגדיר את Co-op Translator GitHub Action במאגר שלכם:

### שלב 1: התקנה והגדרת אימות GitHub App

ה-Workflow משתמש באימות GitHub App כדי לפעול בבטחה מול המאגר (למשל, יצירת Pull Requests) בשמכם. בחרו אחת מהאפשרויות:

#### **אפשרות א': התקנת Co-op Translator GitHub App המובנה (לשימוש פנימי ב-Microsoft)**

1. עברו לעמוד [Co-op Translator GitHub App](https://github.com/apps/co-op-translator).

1. בחרו **Install** ובחרו את החשבון או הארגון שבו נמצא המאגר שלכם.

    ![התקנת האפליקציה](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.he.png)

1. בחרו **Only select repositories** ובחרו את המאגר הרלוונטי (למשל, `PhiCookBook`). לחצו **Install**. ייתכן שתידרשו לאימות.

    ![אישור התקנה](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.he.png)

1. **קבלת אישורי האפליקציה (נדרש תהליך פנימי):** כדי לאפשר ל-Workflow להזדהות כאפליקציה, תצטרכו שני פרטים מהצוות של Co-op Translator:
  - **App ID:** מזהה ייחודי של האפליקציה. ה-App ID הוא: `1164076`.
  - **Private Key:** יש לקבל את **כל תוכן** קובץ המפתח הפרטי `.pem` מאיש הקשר של המתחזק. **התייחסו למפתח זה כסיסמה ושמרו עליו בסודיות.**

1. המשיכו לשלב 2.

#### **אפשרות ב': שימוש ב-GitHub App מותאם אישית משלכם**

- אם תרצו, תוכלו ליצור ולהגדיר GitHub App משלכם. ודאו שיש לו הרשאות קריאה וכתיבה ל-Contents ול-Pull requests. תצטרכו את ה-App ID ואת המפתח הפרטי שנוצר.

### שלב 2: הגדרת Secrets במאגר

יש להוסיף את האישורים של GitHub App ושל שירותי ה-AI כ-Secrets מוצפנים בהגדרות המאגר.

1. עברו למאגר היעד שלכם ב-GitHub (למשל, `PhiCookBook`).

1. גשו ל-**Settings** > **Secrets and variables** > **Actions**.

1. תחת **Repository secrets**, לחצו **New repository secret** עבור כל Secret מהרשימה למטה.

   ![בחירת הגדרות Action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.he.png)

**Secrets נדרשים (לאימות GitHub App):**

| שם ה-Secret         | תיאור                                            | מקור הערך                                    |
| :------------------- | :----------------------------------------------- | :------------------------------------------- |
| `GH_APP_ID`          | App ID של ה-GitHub App (משלב 1).                | הגדרות GitHub App                           |
| `GH_APP_PRIVATE_KEY` | **כל תוכן** קובץ ה-`.pem` שהורדתם.              | קובץ `.pem` (משלב 1)                        |

**Secrets לשירותי AI (הוסיפו את כל הרלוונטיים לפי הדרישות):**

| שם ה-Secret                        | תיאור                                    | מקור הערך                        |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | מפתח ל-Azure AI Service (Computer Vision)   | Azure AI Foundry                 |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint ל-Azure AI Service (Computer Vision) | Azure AI Foundry                 |
| `AZURE_OPENAI_API_KEY`              | מפתח ל-Azure OpenAI                       | Azure AI Foundry                 |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint ל-Azure OpenAI                   | Azure AI Foundry                 |
| `AZURE_OPENAI_MODEL_NAME`           | שם המודל שלכם ב-Azure OpenAI              | Azure AI Foundry                 |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | שם הפריסה שלכם ב-Azure OpenAI             | Azure AI Foundry                 |
| `AZURE_OPENAI_API_VERSION`          | גרסת API ל-Azure OpenAI                   | Azure AI Foundry                 |
| `OPENAI_API_KEY`                    | API Key ל-OpenAI                          | OpenAI Platform                  |
| `OPENAI_ORG_ID`                     | מזהה ארגון OpenAI                         | OpenAI Platform                  |
| `OPENAI_CHAT_MODEL_ID`              | מזהה מודל OpenAI מסוים                    | OpenAI Platform                  |
| `OPENAI_BASE_URL`                   | כתובת בסיס מותאמת ל-OpenAI API            | OpenAI Platform                  |

![הזנת שם משתנה סביבה](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.he.png)

### שלב 3: יצירת קובץ Workflow

לבסוף, צרו את קובץ ה-YAML שמגדיר את תהליך העבודה האוטומטי.

1. בתיקיית השורש של המאגר, צרו את התיקיה `.github/workflows/` אם אינה קיימת.

1. בתוך `.github/workflows/`, צרו קובץ בשם `co-op-translator.yml`.

1. הדביקו את התוכן הבא ל-co-op-translator.yml.

```
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # Azure AI Service Credentials
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}

          # Azure OpenAI Credentials
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}

          # OpenAI Credentials
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Authenticate GitHub App
        id: generate_token
        uses: tibdex/github-app-token@v1
        with:
          app_id: ${{ secrets.GH_APP_ID }}
          private_key: ${{ secrets.GH_APP_PRIVATE_KEY }}

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ steps.generate_token.outputs.token }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/

```

4.  **התאמת ה-Workflow:**
  - **[!IMPORTANT] שפות יעד:** בשלב `Run Co-op Translator`, **חובה לעבור על רשימת קודי השפות** בפקודת `translate -l "..." -y` ולהתאים אותה לצרכי הפרויקט שלכם. הרשימה בדוגמה (`ar de es...`) היא להמחשה בלבד ויש להחליף או לעדכן.
  - **Trigger (`on:`):** כרגע ה-Workflow רץ על כל Push ל-`main`. במאגרים גדולים, שקלו להוסיף מסנן `paths:` (ראו דוגמה בהערה ב-YAML) כדי להריץ את ה-Workflow רק כאשר קבצים רלוונטיים משתנים, וכך לחסוך זמן ריצה.
  - **פרטי PR:** ניתן להתאים את ה-`commit-message`, `title`, `body`, שם ה-`branch` וה-`labels` בשלב יצירת ה-Pull Request לפי הצורך.

## ניהול אישורים וחידוש

- **אבטחה:** תמיד שמרו אישורים רגישים (API Keys, מפתחות פרטיים) כ-Secrets של GitHub Actions. לעולם אל תחשפו אותם בקובץ ה-Workflow או בקוד המאגר.
- **[!IMPORTANT] חידוש מפתחות (למשתמשי Microsoft פנימיים):** שימו לב שמפתח Azure OpenAI בשימוש פנימי ב-Microsoft עשוי לדרוש חידוש תקופתי (למשל, כל 5 חודשים). ודאו שאתם מעדכנים את ה-Secrets הרלוונטיים (`AZURE_OPENAI_...`) **לפני פקיעתם** כדי למנוע כשלי Workflow.

## הרצת ה-Workflow

> [!WARNING]  
> **מגבלת זמן ריצה ב-GitHub-hosted Runner:**  
> ל-GitHub-hosted runners כמו `ubuntu-latest` יש **מגבלת זמן ריצה של 6 שעות**.  
> במאגרים גדולים, אם תהליך התרגום יחרוג מ-6 שעות, ה-Workflow יופסק אוטומטית.  
> כדי למנוע זאת, שקלו:  
> - שימוש ב-**self-hosted runner** (ללא מגבלת זמן)  
> - הפחתת מספר שפות היעד בכל הרצה

לאחר שמיזגתם את קובץ `co-op-translator.yml` לענף הראשי (או לענף המוגדר ב-`on:`), ה-Workflow ירוץ אוטומטית בכל פעם שיש שינוי בענף זה (ובהתאם למסנן `paths`, אם הוגדר).

אם נוצרו או עודכנו תרגומים, הפעולה תיצור אוטומטית Pull Request עם השינויים, מוכן לסקירה ומיזוג שלכם.

---

**הצהרת אחריות**:
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עשויים להכיל טעויות או אי-דיוקים. המסמך המקורי בשפתו המקורית הוא המקור הסמכותי. למידע קריטי, מומלץ לפנות לתרגום מקצועי על ידי אדם. איננו אחראים לכל אי-הבנה או פירוש שגוי הנובעים מהשימוש בתרגום זה.