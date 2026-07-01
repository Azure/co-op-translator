# Репозитории на Microsoft за начинаещи

Тази страница е за поддържачите на Microsoft "For Beginners" репозитории, които използват споделения README раздел "Other Courses".

Повечето потребители на Co-op Translator не се нуждаят от тази страница.

## Автосинхронизиране на секцията "Other Courses"

Добавете тези маркери около секцията "Other Courses" във вашето README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Всеки път когато Co-op Translator се изпълнява чрез CLI или GitHub Actions, той замества съдържанието между маркерите с пакетирания шаблон.

## Актуализиране на споделения шаблон

Източникът на шаблона се намира на:

```text
src/co_op_translator/templates/other_courses.md
```

За да актуализирате споделеното съдържание:

1. Редактирайте шаблона.
2. Отворете pull request към Co-op Translator.
3. След като промяната бъде пусната, стартирайте Co-op Translator в целевия репозиторий.

## Съвет за Sparse Checkout

Големите репозитории с курсове могат да станат скъпи за клониране, когато съдържат много преведени версии. Можете да включите това предупреждение в генерираните езикови секции:

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