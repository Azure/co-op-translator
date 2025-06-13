<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:38:02+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "he"
}
-->
# תרומה ל-Co-op Translator

הפרויקט הזה מקבל תרומות והצעות. רוב התרומות דורשות שתסכים להסכם רישיון תורם (CLA) המצהיר שיש לך את הזכות, ושאתה אכן מעניק לנו את הזכויות להשתמש בתרומתך. לפרטים, בקר בכתובת https://cla.opensource.microsoft.com.

כשאתה מגיש בקשת משיכה, בוט CLA יזהה אוטומטית אם עליך לספק CLA ויעטר את בקשת המשיכה בהתאם (למשל, בדיקת סטטוס, תגובה). פשוט עקוב אחרי ההוראות שהבוט מספק. תצטרך לעשות זאת רק פעם אחת בכל הרפוזיטוריות שמשתמשות ב-CLA שלנו.

## הגדרת סביבת פיתוח

כדי להגדיר את סביבת הפיתוח לפרויקט הזה, אנו ממליצים להשתמש ב-Poetry לניהול תלותים. אנחנו משתמשים ב-`pyproject.toml` לניהול תלותות הפרויקט, ולכן, להתקנת תלותות, יש להשתמש ב-Poetry.

### יצירת סביבת וירטואלית

#### שימוש ב-pip

```bash
python -m venv .venv
```

#### שימוש ב-Poetry

```bash
poetry init
```

### הפעלת סביבת הווירטואלית

#### עבור pip ו-Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### שימוש ב-Poetry

```bash
poetry shell
```

### התקנת החבילה והחבילות הנדרשות

#### שימוש ב-Poetry (מהקובץ pyproject.toml)

```bash
poetry install
```

### בדיקות ידניות

לפני הגשת בקשת משיכה, חשוב לבדוק את פונקציונליות התרגום עם תיעוד אמיתי:

1. צור תיקיית בדיקה בתיקיית השורש:
    ```bash
    mkdir test_docs
    ```

2. העתק לתיקיית הבדיקה תיעוד Markdown ותמונות שברצונך לתרגם. לדוגמה:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. התקן את החבילה מקומית:
    ```bash
    pip install -e .
    ```

4. הרץ את Co-op Translator על מסמכי הבדיקה שלך:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. בדוק את הקבצים המתורגמים ב-`test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`.
1. מלא את משתני הסביבה לפי ההנחיות.

> [!TIP]
>
> ### אפשרויות נוספות לסביבת פיתוח
>
> בנוסף להרצת הפרויקט מקומית, ניתן להשתמש גם ב-GitHub Codespaces או VS Code Dev Containers להגדרת סביבת פיתוח חלופית.
>
> #### GitHub Codespaces
>
> ניתן להפעיל את הדוגמאות האלה וירטואלית באמצעות GitHub Codespaces, ואין צורך בהגדרות נוספות.
>
> הכפתור יפתח מופע VS Code מבוסס דפדפן:
>
> 1. פתח את התבנית (יכול לקחת מספר דקות):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### הרצה מקומית באמצעות VS Code Dev Containers
>
> ⚠️ אפשרות זו תעבוד רק אם ל-Docker Desktop שלך מוקצה לפחות 16GB זיכרון RAM. אם יש לך פחות מ-16GB RAM, תוכל לנסות את אפשרות [GitHub Codespaces](../..) או [להגדיר זאת מקומית](../..).
>
> אפשרות קשורה היא VS Code Dev Containers, שיפתח את הפרויקט ב-VS Code המקומי שלך באמצעות [הרחבת Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. הפעל את Docker Desktop (התקן אם עדיין לא מותקן)
> 2. פתח את הפרויקט:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### סגנון קוד

אנו משתמשים ב-[Black](https://github.com/psf/black) כפורמטור הקוד שלנו בפייתון לשמירה על סגנון קוד אחיד בפרויקט. Black הוא פורמטור קוד נוקשה שמבצע עיצוב אוטומטי של קוד פייתון בהתאם לסגנון Black.

#### קונפיגורציה

הגדרות Black מצוינות בקובץ `pyproject.toml` שלנו:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### התקנת Black

ניתן להתקין את Black באמצעות Poetry (מומלץ) או pip:

##### שימוש ב-Poetry

Black מותקן אוטומטית כשמגדירים את סביבת הפיתוח:
```bash
poetry install
```

##### שימוש ב-pip

אם אתה משתמש ב-pip, ניתן להתקין את Black ישירות:
```bash
pip install black
```

#### שימוש ב-Black

##### עם Poetry

1. עצב את כל קבצי הפייתון בפרויקט:
    ```bash
    poetry run black .
    ```

2. עצב קובץ או תיקייה ספציפיים:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### עם pip

1. עצב את כל קבצי הפייתון בפרויקט:
    ```bash
    black .
    ```

2. עצב קובץ או תיקייה ספציפיים:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> מומלץ להגדיר את העורך שלך לעצב קוד אוטומטית עם Black בעת שמירה. רוב העורכים המודרניים תומכים בכך באמצעות תוספים או הרחבות.

## הרצת Co-op Translator

כדי להריץ את Co-op Translator באמצעות Poetry בסביבתך, בצע את השלבים הבאים:

1. עבור לתיקייה שבה ברצונך לבצע בדיקות תרגום או צור תיקייה זמנית למטרות בדיקה.

2. הרץ את הפקודה הבאה. הדגל `-l ko` with the language code you wish to translate into. The `-d` מציין מצב דיבאג.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> ודא שסביבת Poetry שלך מופעלת (poetry shell) לפני הרצת הפקודה.

## אחראים על הפרויקט

### הודעת קומיט ואסטרטגיית מיזוג

כדי להבטיח אחידות ובהירות בהיסטוריית הקומיטים של הפרויקט, אנו משתמשים בפורמט הודעת קומיט ספציפי **להודעת הקומיט הסופית** בעת שימוש באסטרטגיית **Squash and Merge**.

כאשר בקשת משיכה (PR) מתמזגת, הקומיטים האישיים ישולבו לקומיט יחיד. הודעת הקומיט הסופית צריכה לעקוב אחרי הפורמט הבא לשמירה על היסטוריה נקייה ואחידה.

#### פורמט הודעת קומיט (ל-squash and merge)

אנו משתמשים בפורמט הבא להודעות קומיט:

```bash
<type>: <description> (#<PR number>)
```

- **type**: מציין את קטגוריית הקומיט. אנו משתמשים בסוגים הבאים:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `fix typo`
- `update README`
- `adjust formatting`

They should be squashed into:
`Docs: Improve documentation clarity and formatting (#65)`

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתירגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו הוא המקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי של אדם. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.