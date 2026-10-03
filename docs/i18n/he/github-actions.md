# GitHub Actions

השתמש ב‑GitHub Actions כשאתה רוצה שמאגר יתרגם באופן אוטומטי תיעוד ששונה ויפתח בקשת משיכה עם התוצרים שנוצרו.

התחל בהגדרת ברירת המחדל של `GITHUB_TOKEN`, גם עבור מאגרים ארגוניים כאשר המדיניות מאפשרת זאת. ראה את [הגדרת GitHub App](#github-app-setup) אם הארגון שלך דורש זהות של App או אם אתה צריך ריצות אוטומטיות של זרימות עבודה יורדות.

**עריכות ידניות:** הזרימות האלה מתרגמות מחדש קבצי מקור ששונו במלואם ועלולות להחליף ניסוחים שערכו בתרגומים שלהם. סקור כל PR לפני המיזוג. שמירה על שינויים מקובלים ברמת בלוק Markdown מחייבת אינטגרציה מותאמת עם ה[ספק מצב התרגום של Python API](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## בקשת ה-PR הראשונה שלך לתרגום README

התחל עם קובץ שורש אחד `README.md` ושפה יעד אחת. זרימת עבודה זו מתרגמת Markdown בלבד, לכן Azure AI Vision אינו נדרש.

1. העתק את [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([עיין בתבנית ב‑GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) אל `.github/workflows/translate-readme.yml` במאגר שברצונך לתרגם, והתחייב אליו בסניף ברירת המחדל של המאגר. התבנית משתמשת ב‑Action השורש `Azure/co-op-translator@main`, שמתקין את ה‑CLI מאותו ref מקור. נעץ קומיט שסומן לביקורת לצורך ריצות שחזור.
2. פתח את **Actions > Translate README > Run workflow**, בחר שפה, והשאר את **Preview only** מסומן. בדוק את הערכת הטוקן בשלב התצוגה המקדימה. התצוגה המקדימה אינה קוראת לספקי מודלים, אינה כותבת תרגומים ואינה יוצרת PR.
3. הוסף את הסודות עבור [ספק טקסט](#prerequisites), והפעל את האפשרות **אפשר ל-GitHub Actions ליצור ולאשר בקשות משיכה** תחת **הגדרות > פעולות > כללי**. התבנית מבקשת `contents: write` ו־`pull-requests: write` עבור העבודה שלה; אין צורך לשנות את הרשאות ברירת המחדל לכל זרימת עבודה. אם מדיניות הארגון חוסמת הרשאות אלו או הגדרה זו, פנה למנהל לגבי [אפליקציית GitHub](#github-app-setup) מאושרת.
4. הרץ שוב את זרימת העבודה עם **Preview only** לא מסומן. היא תבצע תצוגה מקדימה, תתרגם, תריץ `co-op-review --readme-only`, ותיצור או תעדכן בקשת PR לתרגום רק לאחר שהתרגום והביקורת יצליחו. הסיכום של זרימת העבודה מקשר ל‑PR.
5. בדוק את הניסוח והשינויים בקבצים ב‑PR, ואז מיזג כשהכל מוכן. זרימת העבודה אינה ממזגת אוטומטית.

ה‑PR מכיל רק את `translations/<language>/README.md` ואת קובץ המטא‑מידע של השפה. ה‑README המקורי נשאר ללא שינוי, וקישורים למסמכים אחרים ממשיכים להצביע אל המסמכים המקוריים. גוף ה‑PR מפרט את הקבצים ששונו ואת תוצאות הבדיקה המבנית. אם התרגום או הבדיקה נכשלו, בדוק את סיכום זרימת העבודה ואת יומני השלבים שנכשלו; לא תיווצר בקשת PR. אם אין שינויים, אין צורך ב‑PR חדש.

**הערת ארגון ו‑CI:** GitHub App היא אופציונלית, אינה דרישת בעלות ארגונית. עם `GITHUB_TOKEN`, זרימות עבודה של בקשת משיכה לפתיחה, עדכון או פתיחה מחדש של PR דורשות משתמש עם גישת כתיבה לבחור **Approve workflows to run**. זרימות עבודה של push אינן מופעלות על ידי טוקן זה. עבור CI ללא השגחה לאחר מכן, ראה את [הגדרת GitHub App](#github-app-setup) ואת [כללי הפעלת זרימות העבודה](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) של GitHub.

## דרישות מוקדמות

לפני יצירת זרימת העבודה, הגדר את סודות שירותי ה‑AI שהריצה של התרגום שלך זקוקה להם.

תרגום טקסט דורש ספק מודל שפה אחד:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

תרגום תמונות דורש בנוסף את Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

ראה את [הגדרות](configuration.md) ו‑[הגדרת Azure AI](azure-ai-setup.md) לפרטי תצורה מקומית.

## הגדרה סטנדרטית

לאחר שניסית את זרימת העבודה עבור README, השתמש בהגדרה זו כדי לתרגם קבצי Markdown של מאגר לשפות רבות. היא מריצה בדיקת Markdown לפני פתיחת PR ואינה דורשת Azure AI Vision.

### שלב 1: הוסף סודות למאגר

במאגר היעד שלך, פתח **Settings** > **Secrets and variables** > **Actions**, ואז הוסף את סודות הספק שהזרימה שלך תשתמש בהם.

![בחר סודות Actions](../../assets/github-actions/select-setting-action.png)

### שלב 2: הפעל את הרשאות זרימות העבודה

פתח **Settings** > **Actions** > **General**.

תחת **הרשאות זרימת עבודה**:

1. הפעל את **אפשר ל-GitHub Actions ליצור ולאשר בקשות משיכה**.
2. שמור את ההגדרה.

העבודה שלמטה מבקשת במפורש `contents: write` ו־`pull-requests: write`. השאר את הרשאות ברירת המחדל של זרימות העבודה במאגר ללא שינוי. אם מדיניות הארגון חוסמת יצירת PR, שאל מנהל לגבי [GitHub App](#github-app-setup) מאושר.

### שלב 3: הוסף את זרימת העבודה

צור את `.github/workflows/co-op-translator.yml`:

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest
    env:
      TARGET_LANGUAGES: "es fr de"

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.11"

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ANTHROPIC_MODEL: ${{ secrets.ANTHROPIC_MODEL }}
          ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL }}
        run: |
          translate -l "$TARGET_LANGUAGES" -md -y

      - name: Review Markdown translations
        run: |
          python - <<'PY'
          import os
          from co_op_translator.api import run_review

          run_review(
              language_codes=os.environ["TARGET_LANGUAGES"].split(),
              markdown=True,
              notebook=False,
              output_format="github",
          )
          PY

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "Update translations via Co-op Translator"
          title: "Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.
            Markdown structure, freshness, and local links were reviewed.
            Review translation wording before merging.

            Generated by Co-op Translator.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
```

שנה את `TARGET_LANGUAGES` לשפות שהפרויקט שלך צריך. הבדיקה משתמשת ב‑Python API לבדוק רק Markdown, בהתאמה לשלב התרגום. שגיאה בתרגום או בבדיקה תעצור את העבודה לפני יצירת PR. זרימת העבודה לא תמזג את ה‑PR באופן אוטומטי. עבור מאגרים גדולים, הוסף פילטר `paths:` תחת `on.push` כך שהזרימה תרוץ רק כאשר התיעוד משתנה.

### אופציונלי: מחברות ותמונות

למחברות, הוסף `-nb` לפקודת התרגום והגדר `notebook=True` בשלב הבדיקה. עבור טקסט בתמונות, קבע את שני ה[סודות של Azure AI Vision](#prerequisites), העבר אותם ב־`env` של שלב התרגום, הוסף `-img` לפקודה, והוסף `translated_images/` ל‑`add-paths` של שלב ה‑PR. בדוק את התמונות המתורגמות באופן חזותי; הבדיקה הדטרמיניסטית אינה מאשרת את טקסט התמונה או את הדיוק הלשוני.

## הגדרת GitHub App

השתמש ב‑GitHub App מאושר כאשר הארגון שלך דורש זהות של אפליקציה, או כאשר ה‑PR שנוצר צריך להפעיל CI יורד ללא שלב האישור של `GITHUB_TOKEN`. App אינו מבטל את מדיניות הארגון; המנהלים עדיין שולטים בהתקנה ובהרשאות שלו.

### שלב 1: צור או התקן GitHub App

השתמש ב‑App קיים שמסופק על‑ידי הארגון אם זמין, או צור אחד עם גישת קריאה/כתיבה ל‑**Contents** ול‑**Pull requests**. התקן אותו במאגר היעד עם כל אישור ארגוני נדרש.

תעד:

- מזהה App
- תוכן המפתח הפרטי

אחסן אותם כסודות במאגר:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### שלב 2: יצירת טוקן של App

הוסף שלב זה מייד לפני שלב בקשת ה‑PR הקיים. עבור תבנית ה‑README, השתמש באותו תנאי הצלחה כך שהתצוגה המקדימה ותרגומים שנכשלו לא יבקשו טוקן של App:

```yaml
      - name: Authenticate GitHub App
        id: generate_token
        if: ${{ !inputs.preview && steps.translate.outcome == 'success' && steps.review.outcome == 'success' }}
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.GH_APP_ID }}
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
          permission-contents: write
          permission-pull-requests: write
```

לאחר מכן שנה רק את הקלט `token` של שלב בקשת ה‑PR הקיים ל־`${{ steps.generate_token.outputs.token }}`. השאר בתוקף את תנאי ההצלחה, הסניף, גוף ה‑PR, ו‑`add-paths` ללא שינוי. הטוקן מוגבל כברירת מחדל למאגר הנוכחי. כאשר מתאימים את ההגדרה הסטנדרטית במקום תבנית ה‑README, השמט את ה־`if` שלמעלה: זרימת העבודה ההיא משתמשת בתנאי ההצלחה ברירת המחדל, כך שיצירת הטוקן ויצירת ה‑PR ירוצו רק לאחר שהתרגום והביקורת יצליחו.

ראה את ה‑[create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) הרשמי להתקנה והרשאות הטוקן.

## מגבלות ה‑Runner

לרצנים המתארחים ב‑GitHub יש משך מירבי למשימה. מאגרים גדולים או מספר רב של שפות יעד עלולים לעבור את המגבלה הזו.

עבור עומסי תרגום גדולים:

- תרגם פחות שפות בכל ריצה.
- השתמש בדגלי תוכן כגון `-md`, `-nb`, או `-img`.
- השתמש ב‑runner מאוחסן‑עצמי כאשר גודל המאגר או השיהוי של המודל הופכים רצנים מתארחים לבלתי אמינים.

## בדיקה ב‑CI

השתמש ב־`co-op-review` כאשר בקשת PR אמורה לאמת תרגומים שנוצרו מבלי לקרוא לספקי LLM או Vision.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

הפקודה `co-op-review` היא פקודת בדיקה דטרמיניסטית בבטא. הבדיקות והסכמה של הפלט שלה עשויים להתפתח, אך היא מעוצבת להיות בטוחה לשימוש ב‑CI מכיוון שאינה כותבת קבצים ואינה קוראת לספקי מודלים.