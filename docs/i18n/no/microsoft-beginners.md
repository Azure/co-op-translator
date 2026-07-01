# Microsoft "For Beginners"-repositorier

Denne siden er for vedlikeholdere av Microsoft "For Beginners"-repositorier som bruker den delte README-delen "Other Courses".

De fleste brukere av Co-op Translator trenger ikke denne siden.

## Automatisk synkronisering av 'Other Courses'-delen

Legg disse markørene rundt 'Other Courses'-delen i README-en din:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Hver gang Co-op Translator kjører via CLI eller GitHub Actions, erstatter den innholdet mellom markørene med den pakkede malen.

## Oppdater den delte malen

Malens kilde ligger på:

```text
src/co_op_translator/templates/other_courses.md
```

For å oppdatere det delte innholdet:

1. Rediger malen.
2. Åpne en pull request mot Co-op Translator.
3. Etter at endringen er utgitt, kjør Co-op Translator i mål-repositoriet.

## Råd om 'sparse checkout'

Store kursrepositorier kan bli kostbare å klone når de inkluderer mange oversatte utdata. Du kan inkludere denne advarselen i genererte språkseksjoner:

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