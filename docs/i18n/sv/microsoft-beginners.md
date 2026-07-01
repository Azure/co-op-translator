# Microsoft-arkiv för nybörjare

Den här sidan är för underhållare av Microsoft "For Beginners" repositories som använder den delade "Other Courses" README-sektionen.

De flesta användare av Co-op Translator behöver inte den här sidan.

## Automatisk synkronisering av "Other Courses"-sektionen

Lägg till dessa markörer runt "Other Courses"-sektionen i din README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Varje gång Co-op Translator körs via CLI eller GitHub Actions ersätter det innehållet mellan markörerna med den paketerade mallen.

## Uppdatera den delade mallen

Mallens källkod finns på:

```text
src/co_op_translator/templates/other_courses.md
```

För att uppdatera det delade innehållet:

1. Redigera mallen.
2. Öppna en pull request till Co-op Translator.
3. Efter att ändringen har släppts, kör Co-op Translator i mål-repositoriet.

## Råd om Sparse Checkout

Stora kursrepositorier kan bli kostsamma att klona när de innehåller många översatta utdata. Du kan inkludera denna rekommendation i genererade språksektioner:

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