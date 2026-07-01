# Microsoft Beginners Repositories

Šis puslapis skirtas Microsoft "For Beginners" saugyklų prižiūrėtojams, kurie naudoja bendrą "Other Courses" README skiltį.

Daugumai Co-op Translator naudotojų šis puslapis nereikalingas.

## Auto-Sync the Other Courses Section

Pridėkite šiuos žymeklius aplink "Other Courses" skiltį jūsų README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Kiekvieną kartą, kai Co-op Translator paleidžiamas per CLI arba GitHub Actions, jis pakeičia turinį tarp žymeklių supakuotu šablonu.

## Update the Shared Template

Šablono šaltinis yra:

```text
src/co_op_translator/templates/other_courses.md
```

Norėdami atnaujinti bendrą turinį:

1. Redaguokite šabloną.
2. Atidarykite pull request į Co-op Translator.
3. Po pakeitimo išleidimo, paleiskite Co-op Translator tikslinėje saugykloje.

## Sparse Checkout Advisory

Didelės kursų saugyklos gali tapti brangios klonuoti, jei jose yra daug išverstų rezultatų. Galite įtraukti šį įspėjimą sugeneruotose kalbų skiltyse:

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