# Microsoft репозиторијуми за почетнике

Ова страница је намењена одржаваоцима Microsoft "For Beginners" репозиторијума који користе заједнички одељак README-а "Other Courses".

Већини корисника Co-op Translator-а ова страница није потребна.

## Аутоматско синхронизовање одељка Other Courses

Додајте ове маркере око одељка "Other Courses" у вашем README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Сваки пут када се Co-op Translator покрене преко CLI-а или GitHub Actions, он замењује садржај између маркера упакованим шаблоном.

## Ажурирање заједничког шаблона

Извор шаблона се налази на:

```text
src/co_op_translator/templates/other_courses.md
```

За ажурирање заједничког садржаја:

1. Уредите шаблон.
2. Отворите pull request ка Co-op Translator-у.
3. Након што се промена објави, покрените Co-op Translator у циљном репозиторијуму.

## Савет о Sparse Checkout-у

Велики репозиторијуми курсева могу постати скупи за клонирање када садрже много преведених материјала. Можете укључити ово упозорење у генерисане језичке одељке:

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