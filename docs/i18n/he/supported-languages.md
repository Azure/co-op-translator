# שפות נתמכות

Co-op Translator תומך בקודי השפה הבאים עבור פלטי תרגום של טקסט, מחברות ותמונות.

אם ברצונך להוסיף שפה חדשה, עדכן את המיפויים של שפה ופונט תחת `src/co_op_translator/fonts/` ובדוק את השפה לפני פתיחת pull request.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | אנגלית | NotoSans-Medium.ttf | לא | לא |
| fr | צרפתית | NotoSans-Medium.ttf | לא | לא |
| es | ספרדית | NotoSans-Medium.ttf | לא | לא |
| de | גרמנית | NotoSans-Medium.ttf | לא | לא |
| ru | רוסית | NotoSans-Medium.ttf | לא | לא |
| ar | ערבית | NotoSansArabic-Medium.ttf | כן | לא |
| fa | פרסית (פארסי) | NotoSansArabic-Medium.ttf | כן | לא |
| ur | אורדו | NotoSansArabic-Medium.ttf | כן | לא |
| zh-CN | סינית (מפושטת) | NotoSansCJK-Medium.ttc | לא | לא |
| zh-MO | סינית (מסורתית, מקאו) | NotoSansCJK-Medium.ttc | לא | לא |
| zh-HK | סינית (מסורתית, הונג קונג) | NotoSansCJK-Medium.ttc | לא | לא |
| zh-TW | סינית (מסורתית, טאיוואן) | NotoSansCJK-Medium.ttc | לא | לא |
| ja | יפנית | NotoSansCJK-Medium.ttc | לא | לא |
| ko | קוריאנית | NotoSansCJK-Medium.ttc | לא | לא |
| hi | הינדי | NotoSansDevanagari-Medium.ttf | לא | לא |
| bn | בנגלית | NotoSansBengali-Medium.ttf | לא | לא |
| mr | מרטהית | NotoSansDevanagari-Medium.ttf | לא | לא |
| ne | נפאלית | NotoSansDevanagari-Medium.ttf | לא | לא |
| pa | פנג'אבי (גורמוקי) | NotoSansGurmukhi-Medium.ttf | לא | לא |
| pt-PT | פורטוגזית (פורטוגל) | NotoSans-Medium.ttf | לא | לא |
| pt-BR | פורטוגזית (ברזיל) | NotoSans-Medium.ttf | לא | לא |
| it | איטלקית | NotoSans-Medium.ttf | לא | לא |
| lt | ליטאית | NotoSans-Medium.ttf | לא | לא |
| pl | פולנית | NotoSans-Medium.ttf | לא | לא |
| tr | טורקית | NotoSans-Medium.ttf | לא | לא |
| el | יוונית | NotoSans-Medium.ttf | לא | לא |
| th | תאילנדית | NotoSansThai-Medium.ttf | לא | לא |
| sv | שוודית | NotoSans-Medium.ttf | לא | לא |
| da | דנית | NotoSans-Medium.ttf | לא | לא |
| no | נורווגית | NotoSans-Medium.ttf | לא | לא |
| fi | פינית | NotoSans-Medium.ttf | לא | לא |
| nl | הולנדית | NotoSans-Medium.ttf | לא | לא |
| he | עברית | NotoSansHebrew-Medium.ttf | כן | לא |
| vi | וייטנאמית | NotoSans-Medium.ttf | לא | לא |
| id | אינדונזית | NotoSans-Medium.ttf | לא | לא |
| ms | מלאית | NotoSans-Medium.ttf | לא | לא |
| tl | טאגאלוג (פיליפינית) | NotoSans-Medium.ttf | לא | לא |
| sw | סוואהילי | NotoSans-Medium.ttf | לא | לא |
| hu | הונגרית | NotoSans-Medium.ttf | לא | לא |
| cs | צ'כית | NotoSans-Medium.ttf | לא | לא |
| sk | סלובקית | NotoSans-Medium.ttf | לא | לא |
| ro | רומנית | NotoSans-Medium.ttf | לא | לא |
| bg | בולגרית | NotoSans-Medium.ttf | לא | לא |
| sr | סרבית (קירילית) | NotoSans-Medium.ttf | לא | לא |
| hr | קרואטית | NotoSans-Medium.ttf | לא | לא |
| sl | סלובנית | NotoSans-Medium.ttf | לא | לא |
| uk | אוקראינית | NotoSans-Medium.ttf | לא | לא |
| my | בורמזית (מיאנמר) | NotoSansMyanmar-Medium.ttf | לא | לא |
| ta | טמילית | NotoSansTamil-Medium.ttf | לא | לא |
| et | אסטונית | NotoSans-Medium.ttf | לא | לא |
| pcm | פידג'ין ניגרי | NotoSans-Medium.ttf | לא | לא |
| te | טלוגו | NotoSans-Medium.ttf | לא | לא |
| ml | מלאיאלאם | NotoSans-Medium.ttf | לא | לא |
| kn | קנאדה | NotoSans-Medium.ttf | לא | לא |
| km | חמרית | NotoSansKhmer-Medium.ttf | לא | לא |

## הוספת שפה

כדי להוסיף תמיכה בשפה חדשה:

1. הוסף את קוד השפה ושם התצוגה לכלי ניהול השפות.
2. הוסף או מיפוי של גופן ב-`src/co_op_translator/fonts/font_language_mappings.yml`.
3. בדוק את פלט תרגום ה-Markdown והתמונות.
4. פתח בקשת משיכה (pull request) עם המיפוי והערות האימות.