# Microsoft Beginners-repositorier

Denne side er for vedligeholdere af Microsoft "For Beginners"-repositories, der bruger den del af README'en "Andre kurser".

De fleste Co-op Translator-brugere har ikke brug for denne side.

## Automatisk synkronisering af sektionen Andre kurser

Tilføj disse markører omkring sektionen "Andre kurser" i din README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Hver gang Co-op Translator køres via CLI eller GitHub Actions, erstatter den indholdet mellem markørerne med den pakkede skabelon.

## Opdater den delte skabelon

Skabelonkilden ligger på:

```text
src/co_op_translator/templates/other_courses.md
```

For at opdatere det delte indhold:

1. Rediger skabelonen.
2. Åbn en pull request til Co-op Translator.
3. Efter ændringen er frigivet, kør Co-op Translator i det målrettede repository.

## Sparse Checkout-anbefaling

Store kursus-repositories kan blive omkostningstunge at klone, når de indeholder mange oversatte output. Du kan inkludere denne anbefaling i genererede sprogsektioner:

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