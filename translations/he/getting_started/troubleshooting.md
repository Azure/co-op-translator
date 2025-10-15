<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:32:45+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "he"
}
-->
# מדריך פתרון תקלות ל-Microsoft Co-op Translator

## סקירה כללית
Microsoft Co-Op Translator הוא כלי עוצמתי לתרגום מסמכי Markdown בצורה חלקה. מדריך זה יעזור לך לפתור בעיות נפוצות בשימוש בכלי.

## בעיות נפוצות ופתרונות

### 1. בעיית תגית Markdown
**בעיה:** מסמך ה-Markdown המתורגם כולל תגית `markdown` בראש הקובץ, מה שגורם לבעיות תצוגה.

**פתרון:** כדי לפתור זאת, פשוט מחק את תגית ה-`markdown` מראש הקובץ. כך הקובץ יוצג כראוי.

**שלבים:**
1. פתח את קובץ ה-Markdown (`.md`) המתורגם.
2. אתר את תגית ה-`markdown` בראש המסמך.
3. מחק את התגית.
4. שמור את השינויים.
5. פתח מחדש את הקובץ וודא שהוא מוצג נכון.

### 2. בעיית כתובת URL של תמונות מוטמעות
**בעיה:** כתובות ה-URL של תמונות מוטמעות לא תואמות את שפת המסמך, מה שמוביל לתמונות שגויות או חסרות.

**פתרון:** בדוק את כתובת ה-URL של התמונות וודא שהן תואמות את שפת המסמך. כל התמונות נמצאות בתיקיית `translated_images` ולכל תמונה יש תגית שפה בשם הקובץ.

**שלבים:**
1. פתח את מסמך ה-Markdown המתורגם.
2. אתר את התמונות המוטמעות וכתובות ה-URL שלהן.
3. בדוק שתגית השפה בשם הקובץ תואמת לשפת המסמך.
4. עדכן את הכתובות במידת הצורך.
5. שמור את השינויים ופתח מחדש את המסמך כדי לוודא שהתמונות מוצגות כראוי.

### 3. דיוק התרגום
**בעיה:** התוכן המתורגם אינו מדויק או דורש עריכה נוספת.

**פתרון:** עיין במסמך המתורגם וערוך אותו לשיפור הדיוק והבהירות.

**שלבים:**
1. פתח את המסמך המתורגם.
2. קרא את התוכן בעיון.
3. ערוך את מה שצריך לשיפור הדיוק.
4. שמור את השינויים.

## 4. שגיאת הרשאה Redacted או 404

אם תמונות או טקסט לא מתורגמים לשפה הנכונה ובמצב -d debug מתקבלת שגיאת 401, מדובר בכשל אימות — המפתח לא תקין, פג תוקף או לא משויך לאזור הנכון.

הרץ את Co-op Translator עם [המתג -d debug](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) כדי להבין את שורש הבעיה.

- **הודעת שגיאה:** `Access denied due to invalid subscription key or wrong API endpoint.`
- **סיבות אפשריות:**
  - מפתח המנוי הוסר או לא נכון בבקשה.
  - מפתח AI Services או Subscription Key שייך למשאב Azure אחר (כמו Translator או OpenAI) במקום **Azure AI Vision**.

 **סוג משאב**
  - עבור ל-[Azure Portal](https://portal.azure.com) או [Azure AI Foundry](https://ai.azure.com) וודא שהמשאב הוא מסוג `Azure AI services` → `Vision`.
  - אמת את המפתחות וודא שאתה משתמש במפתח הנכון.

## 5. שגיאות קונפיגורציה (ניהול שגיאות חדש)

החל ממערכת התרגום הסלקטיבית החדשה, Co-op Translator מספק הודעות שגיאה ברורות כאשר שירותים נדרשים לא מוגדרים.

### 5.1. שירות Azure AI לא מוגדר לתרגום תמונות

**בעיה:** ביקשת תרגום תמונות (`-img`) אך שירות Azure AI לא מוגדר כראוי.

**הודעת שגיאה:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**פתרון:**
1. **אפשרות 1:** הגדר את שירות Azure AI
   - הוסף `AZURE_AI_SERVICE_API_KEY` לקובץ ה-`.env`
   - הוסף `AZURE_AI_SERVICE_ENDPOINT` לקובץ ה-`.env`
   - ודא שהשירות נגיש

2. **אפשרות 2:** הסר את בקשת תרגום התמונות
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. קונפיגורציה חסרה

**בעיה:** קונפיגורציה חיונית של LLM חסרה.

**הודעת שגיאה:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**פתרון:**
1. ודא שבקובץ ה-`.env` שלך יש לפחות אחת מהקונפיגורציות הבאות:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` ו-`AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   צריך להגדיר או Azure OpenAI או OpenAI, לא את שניהם.

### 5.3. בלבול בתרגום סלקטיבי

**בעיה:** לא תורגמו קבצים למרות שהפקודה הצליחה.

**סיבות אפשריות:**
- דגלי סוג קובץ שגויים (`-md`, `-img`, `-nb`)
- אין קבצים תואמים בפרויקט
- מבנה תיקיות לא נכון

**פתרון:**
1. **השתמש במצב debug** כדי לראות מה קורה:
   ```bash
   translate -l "ko" -md -d
   ```

2. **בדוק סוגי קבצים** בפרויקט שלך:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **אמת שילובי דגלים**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. מעבר מהמערכת הישנה

### 6.1. מצב Markdown בלבד בוטל

**בעיה:** פקודות שהסתמכו על fallback אוטומטי ל-Markdown בלבד כבר לא עובדות כבעבר.

**התנהגות ישנה:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**התנהגות חדשה:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**פתרון:**
- **היה מפורש** לגבי מה שברצונך לתרגם:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. התנהגות לא צפויה של קישורים

**בעיה:** קישורים בקבצים המתורגמים מפנים למיקומים לא צפויים.

**סיבה:** עיבוד קישורים דינמי משתנה לפי סוגי הקבצים שנבחרו.

**פתרון:**
1. **הבין את התנהגות הקישורים החדשה**:
   - `-nb` כלול: קישורי מחברות מפנים לגרסאות המתורגמות
   - `-nb` לא כלול: קישורי מחברות מפנים לקבצים המקוריים
   - `-img` כלול: קישורי תמונות מפנים לגרסאות המתורגמות
   - `-img` לא כלול: קישורי תמונות מפנים לקבצים המקוריים

2. **בחר את השילוב הנכון** לצורך שלך:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action רץ אך לא נוצר Pull Request (PR)

**סימפטום:** ביומני ה-workflow של `peter-evans/create-pull-request` מופיע:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**סיבות אפשריות:**
- **לא זוהו שינויים:** שלב התרגום לא יצר הבדלים (המאגר כבר מעודכן).
- **פלטים שנדחו:** `.gitignore` מתעלם מקבצים שציפית להעלות (למשל, `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths לא תואם:** הנתיבים שסופקו לפעולה לא תואמים למיקומי הפלט בפועל.
- **לוגיקת workflow/תנאים:** שלב התרגום הסתיים מוקדם או כתב לתיקיות לא צפויות.

**איך לבדוק/לתקן:**
1. **אמת שהפלטים קיימים:** לאחר התרגום, בדוק שיש קבצים חדשים/משתנים ב-`translations/` ו/או `translated_images/`.
   - אם מתרגמים מחברות, ודא שקבצי `.ipynb` נכתבים תחת `translations/<lang>/...`.
2. **בדוק את `.gitignore`:** אל תתעלם מהפלטים שנוצרים. ודא שאינך מתעלם מ:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (אם מתרגמים מחברות)
3. **ודא ש-add-paths תואם לפלטים:** השתמש בערך מרובה שורות וכלול את שתי התיקיות במידת הצורך:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **כפה יצירת PR לצורך בדיקה:** אפשר זמנית קומיטים ריקים כדי לוודא שהכל מחובר נכון:
   ```yaml
   with:
     commit-empty: true
   ```
5. **הרץ עם debug:** הוסף `-d` לפקודת התרגום כדי להדפיס אילו קבצים נמצאו ונכתבו.
6. **הרשאות (GITHUB_TOKEN):** ודא של-workflow יש הרשאות כתיבה ליצירת קומיטים ו-PR:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## רשימת בדיקות מהירה לאיתור תקלות

בעת פתרון בעיות תרגום:

1. **השתמש במצב debug:** הוסף את הדגל `-d` כדי לראות לוגים מפורטים
2. **בדוק את הדגלים שלך:** ודא ש-`-md`, `-img`, `-nb` תואמים למה שאתה רוצה
3. **אמת קונפיגורציה:** בדוק שבקובץ ה-`.env` יש את המפתחות הנדרשים
4. **בדוק בהדרגה:** התחל עם `-md` בלבד, ואז הוסף סוגים נוספים
5. **בדוק מבנה קבצים:** ודא שקבצי המקור קיימים ונגישים

למידע נוסף על פקודות ודגלים זמינים, ראה את [מדריך הפקודות](./command-reference.md).

---

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עשויים להכיל טעויות או אי-דיוקים. יש לראות במסמך המקורי בשפתו המקורית כמקור הסמכותי. למידע קריטי, מומלץ לפנות לתרגום מקצועי על ידי אדם. איננו אחראים לכל אי-הבנות או פירושים שגויים הנובעים מהשימוש בתרגום זה.