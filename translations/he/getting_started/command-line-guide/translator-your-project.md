<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:51:47+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "he"
}
-->
# תרגום הפרויקט שלך באמצעות Co-op Translator

**Co-op Translator** הוא כלי שורת פקודה (CLI) שעוזר לך לתרגם קבצי markdown ותמונות בפרויקט שלך לשפות שונות. בסעיף זה מוסבר כיצד להשתמש בכלי, מפורטים אפשרויות השורה השונות, ומוצגים דוגמאות לשימושים שונים.

> [!NOTE]
> לקבלת רשימה מלאה של פקודות ותיאורים מפורטים, עיין ב-[Command reference](./command-reference.md).

---

## תרחישים ופקודות לדוגמה

להלן כמה שימושים נפוצים ל-**Co-op Translator**, יחד עם הפקודות המתאימות להפעלה.

### 1. תרגום בסיסי (שפה יחידה)

כדי לתרגם את כל הפרויקט שלך (קבצי markdown ותמונות) לשפה אחת, למשל קוריאנית, השתמש בפקודה הבאה:

```bash
translate -l "ko"
```

פקודה זו תתרגם את כל קבצי ה-markdown והתמונות לקוריאנית, ותוסיף תרגומים חדשים מבלי למחוק תרגומים קיימים.

> [!TIP]
>
> רוצה לדעת אילו קודי שפות זמינים ב-**Co-op Translator**? בקר ב-[Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) במאגר לפרטים נוספים.

#### דוגמה ב-Phi-3 CookBook

ב-**Phi-3 CookBook**, השתמשתי בשיטה הבאה להוספת תרגום קוריאני לקבצי ה-markdown והתמונות הקיימים.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. תרגום למספר שפות

כדי לתרגם את הפרויקט למספר שפות (למשל ספרדית, צרפתית וגרמנית), השתמש בפקודה הבאה:

```bash
translate -l "es fr de"
```

פקודה זו תתרגם את הפרויקט לספרדית, צרפתית וגרמנית, ותוסיף תרגומים חדשים מבלי להחליף תרגומים קיימים.

#### דוגמה ב-Phi-3 CookBook

ב-**Phi-3 CookBook**, לאחר משיכת השינויים העדכניים ביותר כדי לשקף את הקומיטים האחרונים, השתמשתי בשיטה הבאה לתרגום קבצי markdown ותמונות שהתווספו לאחרונה.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> למרות שבדרך כלל מומלץ לתרגם שפה אחת בכל פעם, במצבים כמו זה שבהם יש צורך להוסיף שינויים ספציפיים, תרגום למספר שפות בו זמנית יכול להיות יעיל.

### 3. עדכון תרגומים (מוחק תרגומים קיימים)

כדי לעדכן תרגומים קיימים (כלומר למחוק את התרגומים הנוכחיים ולהחליפם בחדשים), השתמש באפשרות `-u`. פעולה זו תמחק את כל התרגומים הקיימים לשפות שצוינו ותבצע תרגום מחדש.

```bash
translate -l "ko" -u
```

אזהרה: פקודה זו תבקש ממך אישור לפני שתמשיך במחיקת התרגומים הקיימים.

#### דוגמה ב-Phi-3 CookBook

ב-**Phi-3 CookBook**, השתמשתי בשיטה הבאה לעדכון כל הקבצים המתורגמים בספרדית. אני ממליץ להשתמש בשיטה זו כאשר יש שינויים משמעותיים בתוכן המקורי במספר מסמכי markdown. אם יש רק כמה קבצי markdown מתורגמים שצריך לעדכן, עדיף למחוק ידנית את הקבצים הספציפיים ואז להשתמש בשיטת `-a` להוספת התרגומים המעודכנים.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. תרגום רק תמונות

כדי לתרגם רק את קבצי התמונות בפרויקט שלך, השתמש באפשרות `-img`:

```bash
translate -l "ko" -img
```

פקודה זו תתרגם רק את התמונות לקוריאנית, מבלי להשפיע על קבצי markdown.

### 6. תרגום רק קבצי Markdown

כדי לתרגם רק את קבצי ה-markdown בפרויקט שלך, השתמש באפשרות `-md`:

```bash
translate -l "ko" -md
```

### 7. בדיקת שגיאות בקבצים מתורגמים

אם ברצונך לבדוק קבצים מתורגמים לשגיאות ולנסות לתרגם מחדש במידת הצורך, השתמש באפשרות `-chk`:

```bash
translate -l "ko" -chk
```

פקודה זו תסרוק את קבצי ה-markdown המתורגמים ותנסה לתרגם מחדש את הקבצים שבהם נמצאו שגיאות.

#### דוגמה ב-Phi-3 CookBook

ב-**Phi-3 CookBook**, השתמשתי בשיטה הבאה לבדיקה של שגיאות תרגום בקבצים הקוריאניים ולביצוע ניסיון אוטומטי לתרגום מחדש לקבצים שבהם זוהו בעיות.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

אפשרות זו בודקת שגיאות תרגום. כיום, אם ההבדל בכמות שברי השורה בין הקובץ המקורי למתורגם עולה על שש, הקובץ מסומן כשגוי בתרגום. אני מתכנן לשפר קריטריון זה בעתיד כדי לאפשר גמישות רבה יותר.

לדוגמה, שיטה זו שימושית לזיהוי קטעים חסרים או תרגומים פגומים, והיא תנסה אוטומטית לתרגם מחדש את הקבצים הללו.

עם זאת, אם כבר ידוע לך אילו קבצים בעייתיים, עדיף למחוק אותם ידנית ולהשתמש באפשרות `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`:

```bash
translate -l "ko" -d
```

פקודה זו תריץ את התרגום במצב דיבאג, ותספק מידע נוסף בלוג שיעזור לך לזהות בעיות במהלך התרגום.

#### דוגמה ב-Phi-3 CookBook

ב-**Phi-3 CookBook**, נתקלתי בבעיה שבה תרגומים עם הרבה קישורים בקבצי markdown גרמו לטעויות עיצוב, כמו תרגומים שבורים והתעלמות משברי שורה. כדי לאבחן את הבעיה, השתמשתי באפשרות `-d` כדי לראות כיצד מתבצע תהליך התרגום.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. תרגום לכל השפות

אם ברצונך לתרגם את הפרויקט לכל השפות הנתמכות, השתמש במילת המפתח all.

> [!WARNING]
> תרגום לכל השפות בבת אחת עלול לקחת זמן רב בהתאם לגודל הפרויקט. לדוגמה, תרגום ה-**Phi-3 CookBook** לספרדית לקח כ-שעתיים. בהתחשב בהיקף, לא פרקטי שאדם אחד יטפל ב-20 שפות. מומלץ לחלק את העבודה בין כמה תורמים, כאשר כל אחד מנהל שפה או שתיים, ולעדכן תרגומים בהדרגה.

```bash
translate -l "all"
```

פקודה זו תתרגם את הפרויקט לכל השפות הזמינות. אם תמשיך, התרגום עלול לקחת זמן רב בהתאם לגודל הפרויקט.

> [!TIP]
>
> ### מחיקה ידנית של קבצים מתורגמים (אופציונלי)
> קבצים מתורגמים מזוהים ומנוקים אוטומטית בעת עדכון קובץ מקור.
>
> עם זאת, אם ברצונך לעדכן תרגום ידנית - למשל, לשחזר קובץ ספציפי או לעקוף את התנהגות המערכת - תוכל להשתמש בפקודה הבאה למחיקת כל הגרסאות של הקובץ בתיקיות השפות השונות.
>
> ### ב-Windows:
> 1. **שימוש ב-Command Prompt**:
>    - פתח את ה-Command Prompt.
>    - עבור לתיקייה שבה נמצאים הקבצים באמצעות הפקודה `cd`.
>    - השתמש בפקודה הבאה למחיקת הקבצים:
>      ```
>      del /s *filename*
>      ```
>      אפשרות `/s` מחפשת גם בתת-תיקיות.
>
> 2. **שימוש ב-PowerShell**:
>    - פתח את PowerShell.
>    - הרץ את הפקודה הבאה:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      החלף `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` בפקודה המתאימה.
>
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     החלף `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` לעדכון השינויים האחרונים בקבצים.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להתייחס למסמך המקורי בשפתו כאל המקור הסמכותי. למידע קריטי מומלץ להיעזר בתרגום מקצועי על ידי אדם. איננו אחראים לכל אי הבנה או פרשנות שגויה הנובעים מהשימוש בתרגום זה.