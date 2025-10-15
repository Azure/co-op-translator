<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:32:17+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "he"
}
-->
# מדריך פקודות

ה-CLI של **Co-op Translator** מציע מגוון אפשרויות להתאמה אישית של תהליך התרגום:

פקודה                                       | תיאור
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                | מתרגם את הפרויקט שלך לשפות שצוינו. לדוגמה: translate -l "es fr de" מתרגם לספרדית, צרפתית וגרמנית. השתמש ב-translate -l "all" כדי לתרגם לכל השפות הנתמכות.
translate -l "language_codes" -u             | מעדכן תרגומים על ידי מחיקת הקיימים ויצירתם מחדש. אזהרה: פעולה זו תמחק את כל התרגומים הנוכחיים לשפות שצוינו.
translate -l "language_codes" -img           | מתרגם רק קבצי תמונה.
translate -l "language_codes" -md            | מתרגם רק קבצי Markdown.
translate -l "language_codes" -nb            | מתרגם רק קבצי Jupyter notebook (.ipynb).
translate -l "language_codes" --fix          | מתרגם מחדש קבצים עם ציון ביטחון נמוך לפי תוצאות הערכה קודמות.
translate -l "language_codes" -d             | מפעיל מצב ניפוי שגיאות (debug) לקבלת לוגים מפורטים.
translate -l "language_codes" --save-logs, -s| שומר לוגים ברמת DEBUG לקבצים תחת <root_dir>/logs/ (הקונסול נשלט ע"י -d)
translate -l "language_codes" -r "root_dir"  | מציין את תיקיית השורש של הפרויקט
translate -l "language_codes" -f             | מצב מהיר לתרגום תמונות (עד פי 3 מהיר יותר, עם פשרה קלה באיכות וביישור).
translate -l "language_codes" -y             | מאשר אוטומטית את כל ההודעות (שימושי ל-CI/CD)
translate -l "language_codes" --help         | פרטי עזרה ב-CLI המציגים פקודות זמינות
evaluate -l "language_code"                  | מעריך את איכות התרגום לשפה מסוימת ומספק ציון ביטחון
evaluate -l "language_code" -c 0.8           | מעריך תרגומים עם סף ביטחון מותאם אישית
evaluate -l "language_code" -f               | מצב הערכה מהיר (מבוסס חוקים בלבד, ללא LLM)
evaluate -l "language_code" -D               | מצב הערכה מעמיק (מבוסס LLM בלבד, יסודי יותר אך איטי)
evaluate -l "language_code" --save-logs, -s  | שומר לוגים ברמת DEBUG לקבצים תחת <root_dir>/logs/
migrate-links -l "language_codes"            | מעבד מחדש קבצי Markdown מתורגמים לעדכון קישורים למחברות (.ipynb). מעדיף מחברות מתורגמות כשזמינות; אחרת נופל חזרה למקור.
migrate-links -l "language_codes" -r         | מציין את תיקיית השורש של הפרויקט (ברירת מחדל: תיקיה נוכחית).
migrate-links -l "language_codes" --dry-run  | מציג אילו קבצים ישתנו ללא כתיבה בפועל.
migrate-links -l "language_codes" --no-fallback-to-original | לא משנה קישורים למחברות מקוריות כשאין מתורגמות (מעדכן רק כשיש מתורגמות).
migrate-links -l "language_codes" -d         | מפעיל מצב ניפוי שגיאות (debug) לקבלת לוגים מפורטים.
migrate-links -l "language_codes" --save-logs, -s | שומר לוגים ברמת DEBUG לקבצים תחת <root_dir>/logs/
migrate-links -l "all" -y                    | מעבד את כל השפות ומאשר אוטומטית את הודעת האזהרה.

## דוגמאות שימוש

  1. התנהגות ברירת מחדל (הוספת תרגומים חדשים מבלי למחוק קיימים):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. הוספת תרגומי תמונה חדשים לקוריאנית בלבד (ללא מחיקת תרגומים קיימים):    translate -l "ko" -img

  3. עדכון כל התרגומים לקוריאנית (אזהרה: פעולה זו מוחקת את כל התרגומים הקוריאניים הקיימים לפני תרגום מחדש):    translate -l "ko" -u

  4. עדכון תמונות קוריאניות בלבד (אזהרה: פעולה זו מוחקת את כל התמונות הקוריאניות הקיימות לפני תרגום מחדש):    translate -l "ko" -img -u

  5. הוספת תרגומי Markdown חדשים לקוריאנית מבלי להשפיע על תרגומים אחרים:    translate -l "ko" -md

  6. תיקון תרגומים עם ציון ביטחון נמוך לפי תוצאות הערכה קודמות: translate -l "ko" --fix

  7. תיקון תרגומים עם ציון ביטחון נמוך לקבצים מסוימים בלבד (Markdown): translate -l "ko" --fix -md

  8. תיקון תרגומים עם ציון ביטחון נמוך לקבצים מסוימים בלבד (תמונות): translate -l "ko" --fix -img

  9. שימוש במצב מהיר לתרגום תמונות:    translate -l "ko" -img -f

  10. תיקון תרגומים עם ציון ביטחון נמוך וסף מותאם אישית: translate -l "ko" --fix -c 0.8

  11. דוגמת מצב ניפוי שגיאות: - translate -l "ko" -d: הפעלת לוגים מפורטים.
  12. שמירת לוגים לקבצים: translate -l "ko" -s
  13. DEBUG בקונסול ובקובץ: translate -l "ko" -d -s

  14. עדכון קישורי מחברות לתרגומים בקוריאנית (עדכון קישורים למחברות מתורגמות כשזמינות):    migrate-links -l "ko"

  15. עדכון קישורים במצב יבש (ללא כתיבה לקבצים):    migrate-links -l "ko" --dry-run

  16. עדכון קישורים רק כשיש מחברות מתורגמות (ללא נפילה חזרה למקור):    migrate-links -l "ko" --no-fallback-to-original

  17. עיבוד כל השפות עם הודעת אישור:    migrate-links -l "all"

  18. עיבוד כל השפות ואישור אוטומטי:    migrate-links -l "all" -y
  19. שמירת לוגים לקבצים עבור migrate-links:    migrate-links -l "ko ja" -s

### דוגמאות הערכה

> [!WARNING]  
> **פיצ'ר בטא**: פונקציית ההערכה נמצאת כרגע בגרסת בטא. פיצ'ר זה פותח כדי להעריך מסמכים מתורגמים, ושיטות ההערכה והיישום המפורט עדיין בפיתוח ועשויים להשתנות.

  1. הערכת תרגומים לקוריאנית: evaluate -l "ko"

  2. הערכה עם סף ביטחון מותאם אישית: evaluate -l "ko" -c 0.8

  3. הערכה מהירה (מבוססת חוקים בלבד): evaluate -l "ko" -f

  4. הערכה מעמיקה (מבוססת LLM בלבד): evaluate -l "ko" -D

---

**הצהרת אחריות**:
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עשויים להכיל טעויות או אי-דיוקים. יש לראות במסמך המקורי בשפתו המקורית כמקור הסמכותי. למידע קריטי, מומלץ לפנות לתרגום מקצועי על ידי אדם. איננו אחראים לכל אי-הבנה או פירוש שגוי הנובעים מהשימוש בתרגום זה.