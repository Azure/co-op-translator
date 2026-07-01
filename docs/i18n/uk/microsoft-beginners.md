# Репозиторії Microsoft "For Beginners"

Ця сторінка призначена для підтримувачів репозиторіїв Microsoft "For Beginners", які використовують спільний розділ README "Other Courses".

Більшість користувачів Co-op Translator не потребують цієї сторінки.

## Auto-Sync the Other Courses Section

Додайте ці маркери навколо розділу "Other Courses" у вашому README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Кожного разу, коли Co-op Translator запускається через CLI або GitHub Actions, він замінює вміст між маркерами на упакований шаблон.

## Update the Shared Template

The template source lives at:

```text
src/co_op_translator/templates/other_courses.md
```

Щоб оновити спільний вміст:

1. Відредагуйте шаблон.
2. Відкрийте pull request у Co-op Translator.
3. Після випуску зміни запустіть Co-op Translator у цільовому репозиторії.

## Sparse Checkout Advisory

Великі репозиторії курсів можуть стати дорогими для клонування, якщо вони містять багато перекладених результатів. Ви можете додати цю рекомендацію в згенеровані мовні розділи:

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