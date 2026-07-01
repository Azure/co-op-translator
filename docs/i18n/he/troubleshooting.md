# פתרון בעיות

השתמש בעמוד זה כאשר ריצת תרגום מצליחה באופן בלתי צפוי, נכשלת במהלך ההגדרה, או מייצרת פלט שדורש סקירה.

## התחילו כאן

1. הרץ פקודה ממוקדת תחילה, כגון `translate -l "ko" -md`.
2. הוסף `-d` עבור יומני דיבאג בקונסול.
3. הוסף `-s` כדי לשמור את יומני הדיבאג תחת `<root-dir>/logs/`.
4. הרץ את `co-op-review` לאחר התרגום כדי לבדוק עדכניות, מבנה וקישורים מקומיים.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## שגיאות תצורה

### לא נמצא ספק למודל שפה

שגיאה:

```text
No language model configuration found.
```

תיקון:

- הגדר את Azure OpenAI או OpenAI.
- וודא שהמשתנים נמצאים בסביבת ההרצה שבה מתבצעת הפקודה.
- לשימוש מקומי, הכנס אותם ב־`.env` בשורש הפרויקט.

ראה [תצורה](configuration.md).

### תרגום תמונות ללא Azure AI Vision

שגיאה:

```text
Image translation requested but Azure AI Service is not configured.
```

תיקון:

- הוסף את `AZURE_AI_SERVICE_API_KEY`.
- הוסף את `AZURE_AI_SERVICE_ENDPOINT`.
- או הרץ פקודה של טקסט בלבד כגון `translate -l "ko" -md`.

### מפתח או נקודת קצה לא תקינים

התסמינים יכולים לכלול `401`, שגיאות הרשאה מוסתרות, או שגיאות גישה לנקודת הקצה.

תיקון:

- וודא שהמפתח שייך לאותו משאב Azure כמו נקודת הקצה.
- וודא שהמשאב תומך ב-Vision בעת שימוש ב־`-img`.
- וודא ששם הפריסה (deployment) של Azure OpenAI וגרסת ה-API תואמים לפריסה שלך.
- הרץ עם יומני דיבאג: `translate -l "ko" -md -d -s`.

## לא תורגמו קבצים

גורמים נפוצים:

- הדגלים הנבחרים אינם תואמים לקבצים שלך.
- כבר קיימים קבצים מתורגמים.
- קבצי המקור נמצאים בתיקיות שהוחרגו.
- הפקודה רצה משורש פרויקט שגוי.

בדיקות:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

השתמש ב־`--root-dir` כאשר הפקודה מורצת מחוץ לשורש הפרויקט.

## התנהגות קישורים לא צפויה

שכתוב קישורים תלוי בסוגי התוכן הנבחרים:

- `-nb` נכלל: קישורים למחברות יכולים להצביע על מחברות מתורגמות.
- `-nb` לא נכלל: קישורי מחברות יכולים להישאר פונים אל מחברות המקור.
- `-img` נכלל: קישורי תמונה יכולים להצביע על תמונות מתורגמות.
- `-img` לא נכלל: קישורי תמונה יכולים להישאר פונים לתמונות המקור.

הרץ תרגום מלא של התוכן כאשר כל הקישורים הפנימיים צריכים להעדיף פלטים מתורגמים:

```bash
translate -l "ko" -md -nb -img
```

הרץ בדיקת קישורים לאחר התרגום:

```bash
co-op-review -l "ko"
```

## בעיות בהצגת Markdown

אם Markdown המתורגם מוצג באופן שגוי:

- בדוק שה-frontmatter מתחיל ומסתיים ב־`---`.
- בדוק שמספר גדרות הקוד תואם בין קבצי המקור והמתורגמים.
- הרץ `co-op-review` כדי לתפוס בעיות מבנה נפוצות.
- תרגם שוב את הקובץ הספציפי אם הפלט נפגם.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action רץ אך לא נוצר Pull Request

אם `peter-evans/create-pull-request` מדווח שהענף לא מקדים את הבסיס, זרימת העבודה לא מצאה קבצים להתחייבות.

סיבות אפשריות:

- ריצת התרגום לא ייצרה שינויים.
- קובץ `.gitignore` מחריג את `translations/`, `translated_images/`, או מחברות מתורגמות.
- `add-paths` אינו תואם לתיקיות הפלט שנוצרו.
- שלב התרגום יצא מוקדם.

פתרונות:

1. וודא שקיימים קבצים שנוצרו ב־`translations/` או `translated_images/`.
2. וודא שקובץ `.gitignore` אינו מתעלם מפלטים שנוצרו.
3. Use matching `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Temporarily add debug flags to the translate command:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Confirm workflow permissions include:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## איכות התרגום

תרגומים מכניים עשויים להזדקק לביקורת אנושית. השתמש ב־`evaluate` רק כאשר אתה רוצה דירוג איכות ניסיוני ותזרימי עבודה לתיקון מקרים בעלי אמון נמוך.

!!! warning "Experimental"
    `evaluate` can use rule-based and LLM-based checks, and its scoring model and metadata behavior may change. אל תכלול אותו בשערי CI הנדרשים אלא אם זרימת העבודה שלך מוכנה לשינויים.

עבור בדיקות CI דטרמיניסטיות, השתמש במקום זאת ב־`co-op-review`.