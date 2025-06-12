<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:44:19+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "my"
}
-->
# שימוש במצב Markdown בלבד

## מבוא
מצב Markdown בלבד מיועד לתרגם רק את תוכן ה-Markdown של הפרויקט שלך. מצב זה מדלג על תהליך תרגום התמונות ומתמקד אך ורק בתוכן הטקסטואלי, מה שהופך אותו לאידיאלי במצבים שבהם תרגום תמונות אינו נדרש או שהמשתני סביבה הדרושים ל-Computer Vision אינם מוגדרים.

## מתי להשתמש
- כאשר משתני הסביבה הקשורים ל-Computer Vision אינם מוגדרים.
- כאשר רוצים לתרגם רק את התוכן הטקסטואלי מבלי לעדכן קישורי תמונות.
- כאשר המשתמש מציין במפורש את אפשרות `-md` בשורת הפקודה.

## כיצד להפעיל
כדי להפעיל את מצב Markdown בלבד, השתמש באפשרות `-md` בפקודה שלך. לדוגמה:
```
translate -l "ko" -md
```

או אם משתני הסביבה הקשורים ל-Computer Vision אינם מוגדרים. הפעלת `translate -l "ko"` תעבור אוטומטית למצב Markdown בלבד.

```
translate -l "ko"
```

פקודה זו מתרגמת את תוכן ה-Markdown לקוריאנית ומעדכנת את קישורי התמונות לנתיבים המקוריים שלהם, במקום לשנותם לנתיבי תמונות מתורגמים.

## התנהגות
במצב Markdown בלבד:
- תהליך התרגום מדלג על שלב תרגום התמונות.
- קישורי התמונות ב-Markdown נשארים ללא שינוי ומצביעים על הנתיבים המקוריים שלהם.

## דוגמאות
### לפני
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.my.png)
```
### אחרי שימוש במצב Markdown בלבד
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.my.png)
```

## פתרון בעיות
- ודא שאפשרות `-md` צוינה נכון בפקודה.
- בדוק כי אין משתני סביבה של Computer Vision שמפריעים לתהליך.

## סיכום
מצב Markdown בלבד מספק דרך פשוטה לתרגם את תוכן הטקסט מבלי לשנות קישורי תמונות. הוא שימושי במיוחד כאשר תרגום תמונות אינו נחוץ או כשעובדים בסביבות שאין בהן הגדרות ל-Computer Vision.

Could you please specify which language "my" refers to? For example, it could be Myanmar (Burmese), Malay, or another language. This will help me provide the correct translation.