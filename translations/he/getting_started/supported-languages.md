<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4ed48f23ec418b31e90a02fe629fcde",
  "translation_date": "2025-06-12T12:14:10+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "he"
}
-->
# שפות נתמכות

הטבלה למטה מפרטת את השפות הנתמכות כיום על ידי **Co-op Translator**. היא כוללת קודי שפות, שמות שפות, וכל בעיה ידועה הקשורה לכל שפה. אם ברצונך להוסיף תמיכה לשפה חדשה, אנא הוסף את קוד השפה המתאים, השם והגופן המתאים בקובץ `font_language_mappings.yml` הממוקם ב-`src/co_op_translator/fonts/` ושלח בקשת משיכה לאחר בדיקה.

| קוד שפה       | שם שפה               | גופן                             | תמיכה ב-RTL | בעיות ידועות |
|---------------|----------------------|---------------------------------|-------------|--------------|
| en            | English              | NotoSans-Medium.ttf              | לא          | לא           |
| fr            | French               | NotoSans-Medium.ttf              | לא          | לא           |
| es            | Spanish              | NotoSans-Medium.ttf              | לא          | לא           |
| de            | German               | NotoSans-Medium.ttf              | לא          | לא           |
| ru            | Russian              | NotoSans-Medium.ttf              | לא          | לא           |
| ar            | Arabic               | NotoSansArabic-Medium.ttf        | כן          | לא           |
| fa            | Persian (Farsi)      | NotoSansArabic-Medium.ttf        | לא          | לא           |
| ur            | Urdu                 | NotoSansArabic-Medium.ttf        | לא          | לא           |
| zh            | Chinese (Simplified) | NotoSansCJK-Medium.ttc           | לא          | לא           |
| mo            | Chinese (Traditional, Macau) | NotoSansCJK-Medium.ttc    | לא          | לא           |
| hk            | Chinese (Traditional, Hong Kong) | NotoSansCJK-Medium.ttc| לא          | לא           |
| tw            | Chinese (Traditional, Taiwan) | NotoSansCJK-Medium.ttc   | לא          | לא           |
| ja            | Japanese             | NotoSansCJK-Medium.ttc           | לא          | לא           |
| ko            | Korean               | NotoSansCJK-Medium.ttc           | לא          | לא           |
| hi            | Hindi                | NotoSansDevanagari-Medium.ttf    | לא          | לא           |
| bn            | Bengali              | NotoSansBengali-Medium.ttf       | לא          | לא           |
| mr            | Marathi              | NotoSansDevanagari-Medium.ttf    | לא          | לא           |
| ne            | Nepali               | NotoSansDevanagari-Medium.ttf    | לא          | לא           |
| pa            | Punjabi (Gurmukhi)   | NotoSansGurmukhi-Medium.ttf      | לא          | לא           |
| pt            | Portuguese (Portugal)| NotoSans-Medium.ttf              | לא          | לא           |
| br            | Portuguese (Brazil)  | NotoSans-Medium.ttf              | לא          | לא           |
| it            | Italian              | NotoSans-Medium.ttf              | לא          | לא           |
| pl            | Polish               | NotoSans-Medium.ttf              | לא          | לא           |
| tr            | Turkish              | NotoSans-Medium.ttf              | לא          | לא           |
| el            | Greek                | NotoSans-Medium.ttf              | לא          | לא           |
| th            | Thai                 | NotoSansThai-Medium.ttf          | לא          | לא           |
| sv            | Swedish              | NotoSans-Medium.ttf              | לא          | לא           |
| da            | Danish               | NotoSans-Medium.ttf              | לא          | לא           |
| no            | Norwegian            | NotoSans-Medium.ttf              | לא          | לא           |
| fi            | Finnish              | NotoSans-Medium.ttf              | לא          | לא           |
| nl            | Dutch                | NotoSans-Medium.ttf              | לא          | לא           |
| he            | Hebrew               | NotoSansHebrew-Medium.ttf        | לא          | לא           |
| vi            | Vietnamese           | NotoSans-Medium.ttf              | לא          | לא           |
| id            | Indonesian           | NotoSans-Medium.ttf              | לא          | לא           |
| ms            | Malay                | NotoSans-Medium.ttf              | לא          | לא           |
| tl            | Tagalog (Filipino)   | NotoSans-Medium.ttf              | לא          | לא           |
| sw            | Swahili              | NotoSans-Medium.ttf              | לא          | לא           |
| hu            | Hungarian            | NotoSans-Medium.ttf              | לא          | לא           |
| cs            | Czech                | NotoSans-Medium.ttf              | לא          | לא           |
| sk            | Slovak               | NotoSans-Medium.ttf              | לא          | לא           |
| ro            | Romanian             | NotoSans-Medium.ttf              | לא          | לא           |
| bg            | Bulgarian            | NotoSans-Medium.ttf              | לא          | לא           |
| sr            | Serbian (Cyrillic)   | NotoSans-Medium.ttf              | לא          | לא           |
| hr            | Croatian             | NotoSans-Medium.ttf              | לא          | לא           |
| sl            | Slovenian            | NotoSans-Medium.ttf              | לא          | לא           |
| uk            | Ukrainian            | NotoSans-Medium.ttf              | לא          | לא           |
| my            | Burmese (Myanmar)    | NotoSans-Medium.ttf              | לא          | לא           |

## הוספת שפה חדשה

כדי להוסיף תמיכה לשפה חדשה:

1. עבור אל [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml).
2. הוסף את קוד השפה, השם, ושם קובץ הגופן המתאים. וודא לכלול את התכונה `rtl` אם השפה היא מימין לשמאל.
3. אם יש צורך להשתמש בגופן חדש, ודא שהגופן חופשי לשימוש בפרויקטים בקוד פתוח על ידי בדיקת תנאי הרישוי וזכויות היוצרים. לאחר האישור, הוסף את קובץ הגופן לתיקיית `src/co_op_translator/fonts/`.
4. בדוק את השינויים שלך באופן מקומי כדי לוודא שהשפה החדשה נתמכת כראוי.
5. שלח בקשת משיכה עם השינויים וציין את הוספת השפה החדשה בתיאור הבקשה.

דוגמה:

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי של אדם. אנו לא נושאים באחריות לכל אי-הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.