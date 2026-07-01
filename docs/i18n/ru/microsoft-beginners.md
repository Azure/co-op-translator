# Репозитории Microsoft для начинающих

Эта страница предназначена для мейнтейнеров репозиториев Microsoft "For Beginners", которые используют общий раздел README "Other Courses".

Большинству пользователей Co-op Translator эта страница не нужна.

## Автоматическая синхронизация раздела "Other Courses"

Добавьте эти маркеры вокруг раздела "Other Courses" в вашем README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Каждый раз, когда Co-op Translator запускается через CLI или GitHub Actions, он заменяет содержимое между маркерами на упакованный шаблон.

## Обновление общего шаблона

Исходный шаблон находится по адресу:

```text
src/co_op_translator/templates/other_courses.md
```

Чтобы обновить общий контент:

1. Отредактируйте шаблон.
2. Откройте pull request в Co-op Translator.
3. После того, как изменение будет выпущено, запустите Co-op Translator в целевом репозитории.

## Рекомендация по Sparse Checkout

Клонирование больших репозиториев курсов может стать затратным, если они содержат множество переведённых результатов. Вы можете включить эту рекомендацию в сгенерированные языковые разделы:

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