# תרגום, עריכה וביקורת של פרויקט קטן

התחל עם שני קבצי Markdown קצרים ושפה יעד אחת. תראה היכן נכתבים התרגומים, מה קורה כאשר המקור משתנה, ואיך לבדוק את התוצאה.

## תוצאות מוקלטות

הדוגמה הופעלה ב-19 בספטמבר 2026 עם Co-op Translator 0.21.0 ו-Azure OpenAI (`gpt-5-mini`). פקודות ה-CLI ללא שינוי הותקשרו דרך `CliRunner` של Click תוך שימוש ב-wheel שנבנה ותלויות Python קיימות.

| שלב | תוצאה |
| --- | --- |
| תצוגה מקדימה | יציאה 0; לא התבצעה בקשת תרגום למודל |
| תרגום ראשוני | יציאה 0; 27.36 שניות |
| סקירה ראשונית | יציאה 0 |
| ערוך README ובצע סקירה | יציאה 1; זוהה תרגום מיושן |
| עדכן תרגום | יציאה 0; 22.17 שניות |
| סקירה לאחר העדכון | יציאה 0; אין שגיאות או אזהרות |
| המדריך ללא שינוי | בתים זהים לפני ואחרי עדכון README |
| הרץ שוב | יציאה 0; ערכי hash זהים עבור כל קבצי התרגום |

מדידות אלו הן של הרצות בודדות, לא הבטחות ביצועים. זמן ההתקנה אינו נכלל; חיוב ספק לא נמדד. הרצה ללא שינויים עדיין עשויה לבצע בדיקת בריאות של הספק.

בדוק את ה-[תרגום ראשוני](../../assets/demo/before.txt), [תרגום מעודכן](../../assets/demo/after.txt), [הבדל תרגום מלא](../../assets/demo/update.diff), [סקירה מיושנת](../../assets/demo/review-stale.txt), [סקירה סופית](../../assets/demo/review-after.txt), ו-[פרטי הריצה](../../assets/demo/results.json). תרגום קובץ מלא עשוי לשנות ניסוחים נוספים, כפי שההבדל הנתפס מראה. שתי התוצרים הטקסטואליים שומרים על ההצהרת אחריות שנוצרה.

סקירה אנושית עדיין חשובה: העדכון שנתפס משתמש ב-`[사용 가이드](guide.md)을`; החלקיק הקוריאני צריך להיות `[사용 가이드](guide.md)를`. התוצרים הטקסטואליים שומרים על פלט זה כפי שהוא במקום להציג תרגום מתוקן כפלט המודל. הביקורת המבנית עוברת למרות בעיית הניסוח הזו.

## 1. הכנת תיקייה קטנה

השתמש ב-Python 3.11–3.14 וב-[הגדרת הסביבה הוירטואלית](configuration.md#local-runtime-setup). התקן את הגרסה ששומשה בדוגמה זו:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

הורד את [README.txt](../../assets/demo/README.txt) ואת [guide.txt](../../assets/demo/guide.txt) אל התיקייה הזו, ושמור אותם כ-`README.md` ו-`guide.md`. אלה מסמכי פרויקט בדויים וקצרים; אין צורך בהתקנת אפליקציה.

ה-README כולל בלוק קוד וקישור ל-`guide.md`. המשפט האחרון שלו הוא:

```text
Notes are saved locally.
```

השאר בתיקייה זו רק את שני מסמכי המקור האלה. כל הפקודות הבאות רצות בתוך `translation-demo` ועובדות ב-Bash ו-PowerShell.

## 2. תצוגה מקדימה ללא הרשאות

```bash
translate -l "ko" -md --dry-run
```

התצוגה המקדימה מעריכה את עבודת התרגום ללא קריאה למודל או כתיבת תרגומים. הערכות טוקן אינן הצעת חיוב. ההרצה הראשונה אמורה לזהות את שני קבצי ה-Markdown בעבודה חדשה.

## 3. בחר ספק ותרגם

הגדר ספק אחד באמצעות [מדריך התצורה](configuration.md): Azure OpenAI, OpenAI, או Anthropic. תרגום טקסט ב-OpenAI וב-Anthropic אינו דורש חשבון Azure. שירותי תמונה אינם נחוצים בדוגמה זו.

אם אתה משתמש בקובץ `.env` מקומי, הוסף את `.env` ל-`.gitignore` של התיקייה הזו. קריאות תרגום משתמשות בחשבון הספק שלך ועשויות לגרום לחיובים.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

פתח את `translations/ko/README.md` ואת `translations/ko/guide.md`. בדוק את הניסוח הקוריאני, את בלוק הקוד, ואת הקישור מה-README המתורגם אל המדריך המתורגם. הניסוח בפלט משתנה בהתאם למודל.

`co-op-review` בודק רעננות, מבנה וקישורים מקומיים. תוצאה שעוברת אינה מאשרת דיוק לשוני. פתר את כל השגיאות המדווחות לפני ההמשך.

תעד את בסיס הקו המוצלח ב-Git (הגדר תחילה את זהות ה-Git שלך אם נדרש):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. שנה את המקור

ב-`README.md`, החלף את `Notes are saved locally.` ב:

```text
Notes are saved locally as Markdown files.
```

השאר את `guide.md` ללא שינוי. ואז הרץ:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

הסקירה אמורה לדווח שהתרגום של README מיושן ולצאת בכישלון. זהו המצב הביניים הצפוי. התצוגה המקדימה צריכה לזהות עבודה עבור README ששונה.

## 5. עדכן ובדוק את ההבדל

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

בדוק את ההבדל האמיתי: ה-CLI המוגדר כברירת מחדל מתרגם מחדש את הקובץ ששונה, כך שהמודל יכול גם לתקן ניסוחים נוספים בקובץ זה. למדריך שלא שונה לא אמור להיות הבדל. הסקירה לא אמורה לדווח עוד שה-README מיושן; חקור כל ממצא אחר במקום להתעלם ממנו.

שימור ברמת הבלוק של עריכות Markdown שנעשו בידי אדם דורש ספק מצב תרגום אופציונלי ב-[Python API](api.md). זה אינו מופעל על ידי פקודות ה-CLI הללו.

## 6. הרץ שוב ללא שינויים

תחייב את המקור והתרגום המעודכנים:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

עם התרגומים הנוכחיים והקונפיגורציה ללא שינוי, המתורגמן מדלג על הקבצים. פקודת Git האחרונה אמורה לא להפיק הבדל ולצאת בהצלחה.

## הצעדים הבאים

- [תרגם רק README ופתח pull request](github-actions.md#your-first-readme-translation-pr).
- [בחר CLI, Python API, או MCP](workflows.md).
- [דווח על בעיית תרגום ללא קידוד](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).