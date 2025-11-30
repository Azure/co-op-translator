<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:46:46+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "he"
}
-->
# עדכון סעיף "קורסים נוספים" (מאגרי Microsoft Beginners)

מדריך זה מסביר כיצד לגרום לסעיף "קורסים נוספים" להתעדכן אוטומטית באמצעות Co-op Translator, וכיצד לעדכן את התבנית הגלובלית לכל המאגר.

- חל על: מאגרי Microsoft Beginners בלבד
- עובד עם: Co-op Translator CLI ו-GitHub Actions
- מקור התבנית: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## התחלה מהירה: הפעלת סינכרון אוטומטי במאגר שלך

הוסף את הסימנים הבאים סביב סעיף "קורסים נוספים" בקובץ README שלך. Co-op Translator יחליף את כל התוכן שבין הסימנים האלה בכל הרצה.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

בכל פעם ש-Co-op Translator רץ — דרך CLI (למשל, `translate -l "<language codes>"`) או GitHub Actions — הוא יעדכן אוטומטית את סעיף "קורסים נוספים" שמוקף בסימנים אלה.

> [!NOTE]
> אם יש לך רשימה קיימת, פשוט עטוף אותה באותם סימנים. ההרצה הבאה תחליף אותה בתוכן המעודכן והסטנדרטי.

---

## כיצד לשנות את התוכן הגלובלי

אם ברצונך לעדכן את התוכן הסטנדרטי שמופיע בכל מאגרי Beginners:

1. ערוך את התבנית: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. פתח בקשת משיכה (pull request) למאגר Co-op Translator עם השינויים שלך
3. לאחר שהבקשה תתמזג, גרסת Co-op Translator תעודכן
4. בפעם הבאה ש-Co-op Translator ירוץ (ב-CLI או GitHub Action) במאגר היעד, הוא יסנכרן אוטומטית את הסעיף המעודכן

כך נשמר מקור אמת יחיד לתוכן "קורסים נוספים" בכל מאגרי Beginners.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->