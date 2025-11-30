<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T11:39:43+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "he"
}
-->
# תרומה ל-Co-op Translator

הפרויקט הזה מקבל בברכה תרומות והצעות. רוב התרומות מחייבות שתסכימו ל
Contributor License Agreement (CLA) שמצהיר שיש לכם את הזכות, ושאתם אכן מעניקים לנו
את הזכויות להשתמש בתרומתכם. לפרטים, בקרו בכתובת https://cla.opensource.microsoft.com.

כשאתם מגישים בקשת משיכה (pull request), בוט CLA יקבע אוטומטית אם אתם צריכים לספק
CLA ויעטר את ה-PR בהתאם (למשל, בדיקת סטטוס, תגובה). פשוט עקבו אחר ההוראות
של הבוט. תצטרכו לעשות זאת רק פעם אחת בכל הרפוזיטוריות שמשתמשות ב-CLA שלנו.

## הגדרת סביבת הפיתוח

כדי להגדיר את סביבת הפיתוח לפרויקט זה, אנו ממליצים להשתמש ב-Poetry לניהול התלויות. אנו משתמשים בקובץ `pyproject.toml` לניהול התלויות של הפרויקט, ולכן, להתקנת התלויות, יש להשתמש ב-Poetry.

### יצירת סביבה וירטואלית

#### שימוש ב-pip

```bash
python -m venv .venv
```

#### שימוש ב-Poetry

```bash
poetry init
```

### הפעלת הסביבה הווירטואלית

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

#### שימוש ב-Poetry (מ-pyproject.toml)

```bash
poetry install
```

### בדיקה ידנית

לפני הגשת PR, חשוב לבדוק את פונקציונליות התרגום עם תיעוד אמיתי:

1. צרו תיקיית בדיקה בתיקיית השורש:
    ```bash
    mkdir test_docs
    ```

2. העתיקו לתיקיית הבדיקה תיעוד Markdown ותמונות שברצונכם לתרגם. לדוגמה:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. התקינו את החבילה מקומית:
    ```bash
    pip install -e .
    ```

4. הריצו את Co-op Translator על מסמכי הבדיקה שלכם:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. בדקו את הקבצים המתורגמים ב-`test_docs/translations` ו-`test_docs/translated_images` כדי לוודא:
   - איכות התרגום
   - שההערות המטא-דאטה נכונות
   - שמבנה ה-Markdown המקורי נשמר
   - שהקישורים והתמונות פועלים כראוי

בדיקה ידנית זו מסייעת לוודא שהשינויים שלכם עובדים היטב בתרחישים אמיתיים.

### משתני סביבה

1. צרו קובץ `.env` בתיקיית השורש על ידי העתקת קובץ `.env.template` המסופק.
1. מלאו את משתני הסביבה לפי ההנחיות.

> [!TIP]
>
> ### אפשרויות נוספות לסביבת פיתוח
>
> בנוסף להרצת הפרויקט מקומית, ניתן להשתמש גם ב-GitHub Codespaces או ב-VS Code Dev Containers להגדרת סביבת פיתוח חלופית.
>
> #### GitHub Codespaces
>
> ניתן להריץ דוגמאות אלו באופן וירטואלי באמצעות GitHub Codespaces ואין צורך בהגדרות או התקנות נוספות.
>
> הכפתור יפתח מופע VS Code מבוסס דפדפן:
>
> 1. פתחו את התבנית (ייתכן שייקח מספר דקות):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### הרצה מקומית באמצעות VS Code Dev Containers
>
> ⚠️ אפשרות זו תעבוד רק אם ל-Docker Desktop שלכם מוקצה לפחות 16 גיגה-בייט זיכרון RAM. אם יש לכם פחות מ-16 גיגה-בייט, תוכלו לנסות את [אפשרות GitHub Codespaces](../..) או [להגדיר זאת מקומית](../..).
>
> אפשרות קשורה היא VS Code Dev Containers, שיפתח את הפרויקט ב-VS Code המקומי שלכם באמצעות [הרחבת Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. הפעלו את Docker Desktop (התקינו אם לא מותקן)
> 2. פתחו את הפרויקט:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### סגנון קוד

אנו משתמשים ב-[Black](https://github.com/psf/black) כמעצב הקוד של Python שלנו כדי לשמור על סגנון קוד עקבי בפרויקט. Black הוא מעצב קוד ללא פשרות שמעצב אוטומטית את קוד ה-Python כך שיתאים לסגנון Black.

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

Black מותקן אוטומטית בעת הגדרת סביבת הפיתוח:
```bash
poetry install
```

##### שימוש ב-pip

אם אתם משתמשים ב-pip, ניתן להתקין את Black ישירות:
```bash
pip install black
```

#### שימוש ב-Black

##### עם Poetry

1. עצבו את כל קבצי ה-Python בפרויקט:
    ```bash
    poetry run black .
    ```

2. עצבו קובץ או תיקייה ספציפיים:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### עם pip

1. עצבו את כל קבצי ה-Python בפרויקט:
    ```bash
    black .
    ```

2. עצבו קובץ או תיקייה ספציפיים:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> מומלץ להגדיר את העורך שלכם לעצב אוטומטית את הקוד עם Black בעת שמירה. רוב העורכים המודרניים תומכים בכך באמצעות הרחבות או תוספים.

## הרצת Co-op Translator

כדי להריץ את Co-op Translator באמצעות Poetry בסביבתכם, בצעו את השלבים הבאים:

1. נווטו לתיקייה שבה תרצו לבצע בדיקות תרגום או צרו תיקייה זמנית למטרות בדיקה.

2. הריצו את הפקודה הבאה. החליפו את `-l ko` בקוד השפה שאליה תרצו לתרגם. הדגל `-d` מציין מצב דיבוג.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> ודאו שסביבת Poetry שלכם מופעלת (poetry shell) לפני הרצת הפקודה.

## תרמו שפה חדשה

אנו מקבלים בברכה תרומות שמוסיפות תמיכה בשפות חדשות. לפני פתיחת PR, אנא השלימו את השלבים הבאים כדי להבטיח סקירה חלקה.

1. הוסיפו את השפה למיפוי הפונטים
   - ערכו את הקובץ `src/co_op_translator/fonts/font_language_mappings.yml`
   - הוסיפו רשומה עם:
     - `code`: קוד שפה בסגנון ISO (למשל, `vi`)
     - `name`: שם תצוגה ידידותי למשתמש
     - `font`: פונט שנשלח ב-`src/co_op_translator/fonts/` שתומך בכתב
     - `rtl`: `true` אם השפה מימין לשמאל, אחרת `false`

2. כללו קבצי פונטים נדרשים (אם יש צורך)
   - אם נדרש פונט חדש, ודאו תאימות רישיון להפצה בקוד פתוח
   - הוסיפו את קובץ הפונט ל-`src/co_op_translator/fonts/`

3. אימות מקומי
   - הריצו תרגומים על דוגמה קטנה (Markdown, תמונות, פנקסים לפי הצורך)
   - ודאו שהפלט מוצג כראוי, כולל פונטים וכל פריסת RTL אם רלוונטי

4. עדכון התיעוד
   - ודאו שהשפה מופיעה ב-`getting_started/supported-languages.md`
   - אין צורך בשינויים ב-`getting_started/README_languages_template.md`; הוא נוצר מהרשימה הנתמכת

5. פתחו PR
   - תארו את השפה שהוספתם וכל שיקולי פונטים/רישוי
   - צרפו צילומי מסך של הפלט במידת האפשר

דוגמת רשומה ב-YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### בדיקת השפה החדשה

ניתן לבדוק את השפה החדשה על ידי הרצת הפקודה הבאה:

```bash
# צור והפעל סביבה וירטואלית
python -m venv .venv
# חלונות
.venv\Scripts\activate
# מק או לינוקס
source .venv/bin/activate
# התקן את חבילת הפיתוח
pip install -e .
# הפעל את התרגום
translate -l "new_lang"
```

## מנהלים

### הודעת קומיט ואסטרטגיית מיזוג

כדי להבטיח עקביות ובהירות בהיסטוריית הקומיטים של הפרויקט, אנו משתמשים בפורמט הודעת קומיט ספציפי **להודעת הקומיט הסופית** בעת שימוש באסטרטגיית **Squash and Merge**.

כאשר בקשת משיכה (PR) מתמזגת, הקומיטים האישיים יימזגו לקומיט יחיד. הודעת הקומיט הסופית צריכה לעקוב אחרי הפורמט הבא כדי לשמור על היסטוריה נקייה ועקבית.

#### פורמט הודעת קומיט (ל-squash and merge)

אנו משתמשים בפורמט הבא להודעות קומיט:

```bash
<type>: <description> (#<מספר PR>)
```

- **type**: מציין את קטגוריית הקומיט. אנו משתמשים בסוגים הבאים:
  - `Docs`: לעדכוני תיעוד.
  - `Build`: לשינויים במערכת הבנייה או בתלויות, כולל עדכונים לקבצי קונפיגורציה, תהליכי CI, או Dockerfile.
  - `Core`: לשינויים בפונקציונליות הליבה של הפרויקט, במיוחד בקבצים בתיקיית `src/co_op_translator/core`.

- **description**: סיכום תמציתי של השינוי.
- **מספר PR**: מספר בקשת המשיכה הקשורה לקומיט.

**דוגמאות**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> כיום, הקידומות **`Docs`**, **`Core`**, ו-**`Build`** מתווספות אוטומטית לכותרות ה-PR בהתאם לתוויות שהוחלו על קוד המקור ששונה. כל עוד התווית הנכונה הוחלה, בדרך כלל אין צורך לעדכן ידנית את כותרת ה-PR. רק ודאו שהכל נכון והקידומת נוצרה כראוי.

#### אסטרטגיית מיזוג

אנו משתמשים ב-**Squash and Merge** כאסטרטגיית ברירת המחדל לבקשות משיכה. אסטרטגיה זו מבטיחה שהודעות הקומיט יעקבו אחרי הפורמט שלנו, גם אם הקומיטים האישיים לא.

**סיבות**:

- היסטוריה נקייה וקווית של הפרויקט.
- עקביות בהודעות הקומיט.
- הפחתת רעש מקומיטים קטנים (למשל, "תיקון טעות כתיב").

בעת המיזוג, ודאו שהודעת הקומיט הסופית עוקבת אחרי פורמט הודעת הקומיט שתואר לעיל.

**דוגמה ל-Squash and Merge**
אם PR מכיל את הקומיטים הבאים:

- `fix typo`
- `update README`
- `adjust formatting`

הם צריכים להתמזג ל:
`Docs: Improve documentation clarity and formatting (#65)`

### תהליך שחרור

סעיף זה מתאר את הדרך הפשוטה ביותר למנהלים לפרסם גרסה חדשה של Co-op Translator.

#### 1. עדכון הגרסה ב-`pyproject.toml`

1. החליטו על מספר הגרסה הבא (אנו עוקבים אחרי Semantic Versioning: `MAJOR.MINOR.PATCH`).
2. ערכו את `pyproject.toml` ועדכנו את השדה `version` תחת `[tool.poetry]`.
3. פתחו בקשת משיכה ייעודית שמשנה רק את הגרסה (ואת קבצי הנעילה/מטא-דאטה המעודכנים אוטומטית, אם קיימים).
4. לאחר סקירה, השתמשו ב-**Squash and Merge** וודאו שהודעת הקומיט הסופית עוקבת אחרי הפורמט שתואר לעיל.

#### 2. יצירת שחרור ב-GitHub

1. עברו לדף הרפוזיטורי ב-GitHub ופתחו **Releases** → **Draft a new release**.
2. צרו תג חדש (למשל, `v0.13.0`) מהענף `main`.
3. הגדירו את כותרת השחרור לאותה גרסה (למשל, `v0.13.0`).
4. לחצו על **Generate release notes** כדי למלא אוטומטית את יומן השינויים.
5. במידת הצורך, ערכו את הטקסט (למשל, להדגיש שפות נתמכות חדשות או שינויים חשובים).
6. פרסמו את השחרור.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->