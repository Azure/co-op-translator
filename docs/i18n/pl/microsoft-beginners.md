# Repozytoria Microsoft "For Beginners"

Ta strona jest przeznaczona dla opiekunów repozytoriów Microsoft "For Beginners", które używają wspólnej sekcji README "Other Courses".

Większość użytkowników Co-op Translator nie potrzebuje tej strony.

## Automatyczne synchronizowanie sekcji Other Courses

Add these markers around the "Other Courses" section in your README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Each time Co-op Translator runs through the CLI or GitHub Actions, it replaces the content between the markers with the packaged template.

## Aktualizowanie udostępnionego szablonu

The template source lives at:

```text
src/co_op_translator/templates/other_courses.md
```

To update the shared content:

1. Edytuj szablon.
2. Otwórz pull request do Co-op Translator.
3. Po wydaniu zmiany uruchom Co-op Translator w docelowym repozytorium.

## Zalecenie dotyczące Sparse Checkout

Duże repozytoria kursów mogą stać się kosztowne do sklonowania, gdy zawierają wiele przetłumaczonych materiałów. Możesz dołączyć to zalecenie do wygenerowanych sekcji językowych:

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