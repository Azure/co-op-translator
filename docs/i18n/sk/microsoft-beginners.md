# Microsoft repozitáre pre začiatočníkov

Táto stránka je pre správcov Microsoft "For Beginners" repozitárov, ktoré používajú zdieľanú sekciu README "Other Courses".

Väčšina používateľov Co-op Translator túto stránku nepotrebuje.

## Automatická synchronizácia sekcie "Other Courses"

Pridajte tieto markery okolo sekcie "Other Courses" vo vašom README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Pri každom spustení Co-op Translator cez CLI alebo GitHub Actions nahradí obsah medzi markermi zabalenou šablónou.

## Aktualizujte zdieľanú šablónu

Zdroj šablóny sa nachádza na:

```text
src/co_op_translator/templates/other_courses.md
```

Na aktualizáciu zdieľaného obsahu:

1. Upravte šablónu.
2. Otvorte pull request do Co-op Translator.
3. Po vydaní zmeny spustite Co-op Translator v cieľovom repozitári.

## Upozornenie k sparse checkoutu

Veľké repozitáre kurzov môžu byť nákladné na klonovanie, ak obsahujú veľa preložených výstupov. Do vygenerovaných jazykových sekcií môžete zahrnúť toto upozornenie:

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