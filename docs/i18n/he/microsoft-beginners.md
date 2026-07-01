# מאגרי Microsoft למתחילים

עמוד זה מיועד לאחראים על מאגרי Microsoft "For Beginners" שמשתמשים בסעיף README המשותף "Other Courses".

רוב משתמשי Co-op Translator אינם צריכים עמוד זה.

## סנכרון אוטומטי של הסעיף Other Courses

הוסף את הסימונים האלה סביב הסעיף "Other Courses" ב-README שלך:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

בכל פעם ש-Co-op Translator רץ דרך ה-CLI או GitHub Actions, הוא מחליף את התוכן שבין הסימונים בתבנית הארוזה.

## עדכון התבנית המשותפת

קוד המקור של התבנית נמצא ב:

```text
src/co_op_translator/templates/other_courses.md
```

כדי לעדכן את התוכן המשותף:

1. ערוך את התבנית.
2. פתח Pull Request ל-Co-op Translator.
3. לאחר שהשינוי שוחרר, הרץ את Co-op Translator במאגר היעד.

## אזהרת Sparse Checkout

מאגרי קורסים גדולים עלולים להיות יקרים לשכפול (clone) כאשר הם כוללים תוצרים מתורגמים רבים. ניתן לכלול אזהרה זו בסעיפי שפה המיוצרים:

```markdown
> **Prefer to Clone Locally?**
>
> This repository includes many language translations, which can significantly increase download size. To clone without translations, use sparse checkout:
>
> ```bash
> git clone --filter=blob:none --sparse https://github.com/org/repo.git
> cd repo
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
```