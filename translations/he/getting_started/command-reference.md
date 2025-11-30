<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T11:42:04+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "he"
}
-->
# הפניה לפקודות

ממשק השורת פקודה של **Co-op Translator** מציע מספר אפשרויות להתאמת תהליך התרגום:

פקודה                                       | תיאור
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | מתרגם את הפרויקט שלך לשפות שצוינו. לדוגמה: translate -l "es fr de" מתרגם לספרדית, צרפתית וגרמנית. השתמש ב-translate -l "all" כדי לתרגם לכל השפות הנתמכות.
translate -l "language_codes" -u              | מעדכן תרגומים על ידי מחיקת התרגומים הקיימים ויצירתם מחדש. אזהרה: פעולה זו תמחק את כל התרגומים הנוכחיים לשפות שצוינו.
translate -l "language_codes" -img            | מתרגם רק קבצי תמונה.
translate -l "language_codes" -md             | מתרגם רק קבצי Markdown.
translate -l "language_codes" -nb             | מתרגם רק קבצי Jupyter notebook (.ipynb).
translate -l "language_codes" --fix           | מתרגם מחדש קבצים עם ציוני ביטחון נמוכים בהתבסס על תוצאות הערכה קודמות.
translate -l "language_codes" -d              | מפעיל מצב דיבוג לרישום מפורט.
translate -l "language_codes" --save-logs, -s | שומר יומני DEBUG לקבצים תחת <root_dir>/logs/ (הקונסולה נשלטת עדיין על ידי -d)
translate -l "language_codes" -r "root_dir"   | מגדיר את תיקיית השורש של הפרויקט
translate -l "language_codes" -f              | משתמש במצב מהיר לתרגום תמונות (עד פי 3 מהיר יותר עם פגיעה קלה באיכות וביישור).
translate -l "language_codes" -y              | מאשר אוטומטית את כל ההנחיות (שימושי לצינורות CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | מאפשר או מבטל הוספת סעיף ויתור תרגום מכונה ל-Markdown ולמחברות המתורגמות (ברירת מחדל: מופעל).
translate -l "language_codes" --help          | מציג פרטים על הפקודות הזמינות בממשק השורת פקודה
evaluate -l "language_code"                  | מעריך את איכות התרגום לשפה מסוימת ומספק ציוני ביטחון
evaluate -l "language_code" -c 0.8           | מעריך תרגומים עם סף ביטחון מותאם אישית
evaluate -l "language_code" -f               | מצב הערכה מהיר (מבוסס כללים בלבד, ללא LLM)
evaluate -l "language_code" -D               | מצב הערכה עמוק (מבוסס LLM בלבד, יסודי יותר אך איטי יותר)
evaluate -l "language_code" --save-logs, -s  | שומר יומני DEBUG לקבצים תחת <root_dir>/logs/
migrate-links -l "language_codes"             | מעבד מחדש קבצי Markdown מתורגמים כדי לעדכן קישורים למחברות (.ipynb). מעדיף מחברות מתורגמות כשזמינות; אחרת יכול לחזור למחברות המקוריות.
migrate-links -l "language_codes" -r          | מגדיר את תיקיית השורש של הפרויקט (ברירת מחדל: התיקייה הנוכחית).
migrate-links -l "language_codes" --dry-run   | מציג אילו קבצים ישתנו מבלי לכתוב שינויים.
migrate-links -l "language_codes" --no-fallback-to-original | לא משכתב קישורים למחברות המקוריות כאשר חסרות מחברות מתורגמות (מעדכן רק כשקיימות מתורגמות).
migrate-links -l "language_codes" -d          | מפעיל מצב דיבוג לרישום מפורט.
migrate-links -l "language_codes" --save-logs, -s | שומר יומני DEBUG לקבצים תחת <root_dir>/logs/
migrate-links -l "all" -y                      | מעבד את כל השפות ומאשר אוטומטית את ההנחיה לאזהרה.

## דוגמאות שימוש

  1. התנהגות ברירת מחדל (הוספת תרגומים חדשים מבלי למחוק קיימים):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. הוספת תרגומי תמונות חדשים בקוריאנית בלבד (ללא מחיקת תרגומים קיימים):    translate -l "ko" -img

  3. עדכון כל התרגומים בקוריאנית (אזהרה: פעולה זו תמחק את כל התרגומים הקיימים לפני התרגום מחדש):    translate -l "ko" -u

  4. עדכון רק תמונות בקוריאנית (אזהרה: פעולה זו תמחק את כל התמונות הקיימות לפני התרגום מחדש):    translate -l "ko" -img -u

  5. הוספת תרגומי Markdown חדשים לקוריאנית מבלי להשפיע על תרגומים אחרים:    translate -l "ko" -md

  6. תיקון תרגומים עם ביטחון נמוך בהתבסס על תוצאות הערכה קודמות: translate -l "ko" --fix

  7. תיקון תרגומים עם ביטחון נמוך לקבצים ספציפיים בלבד (Markdown): translate -l "ko" --fix -md

  8. תיקון תרגומים עם ביטחון נמוך לקבצים ספציפיים בלבד (תמונות): translate -l "ko" --fix -img

  9. שימוש במצב מהיר לתרגום תמונות:    translate -l "ko" -img -f

  10. תיקון תרגומים עם ביטחון נמוך עם סף מותאם אישית: translate -l "ko" --fix -c 0.8

  11. דוגמת מצב דיבוג: - translate -l "ko" -d: הפעלת רישום דיבוג.
  12. שמירת יומנים לקבצים: translate -l "ko" -s
  13. DEBUG בקונסולה ו-DEBUG בקבצים: translate -l "ko" -d -s
  14. תרגום ללא הוספת ויתורי תרגום מכונה לפלט: translate -l "ko" --no-disclaimer

  15. העברת קישורים למחברות בתרגומים לקוריאנית (עדכון קישורים למחברות מתורגמות כשזמינות):    migrate-links -l "ko"

  15. העברת קישורים עם הרצה יבשה (ללא כתיבת קבצים):    migrate-links -l "ko" --dry-run

  16. עדכון קישורים רק כאשר קיימות מחברות מתורגמות (ללא חזרה למחברות המקוריות):    migrate-links -l "ko" --no-fallback-to-original

  17. עיבוד כל השפות עם בקשת אישור:    migrate-links -l "all"

  18. עיבוד כל השפות ואישור אוטומטי:    migrate-links -l "all" -y
  19. שמירת יומנים לקבצים עבור migrate-links:    migrate-links -l "ko ja" -s

### דוגמאות הערכה

> [!WARNING]  
> **תכונה בבטא**: פונקציית ההערכה נמצאת כרגע בבטא. תכונה זו שוחררה כדי להעריך מסמכים מתורגמים, ושיטות ההערכה והיישום המפורט עדיין בפיתוח ועשויים להשתנות.

  1. הערכת תרגומים לקוריאנית: evaluate -l "ko"

  2. הערכה עם סף ביטחון מותאם אישית: evaluate -l "ko" -c 0.8

  3. הערכה מהירה (מבוססת כללים בלבד): evaluate -l "ko" -f

  4. הערכה עמוקה (מבוססת LLM בלבד): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->