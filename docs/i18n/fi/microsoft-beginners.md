# Microsoftin "For Beginners" -arkistot

Tämä sivu on Microsoftin "For Beginners" -arkistojen ylläpitäjille, jotka käyttävät jaettua "Other Courses" README-osaa.

Useimmat Co-op Translatorin käyttäjät eivät tarvitse tätä sivua.

## Automaattinen synkronointi Other Courses -osiolle

Lisää nämä tunnisteet "Other Courses" -osion ympärille README-tiedostossasi:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Joka kerta kun Co-op Translator suoritetaan CLI:ssä tai GitHub Actionsissa, se korvaa tunnisteiden välissä olevan sisällön paketoidulla mallilla.

## Päivitä jaettu malli

Mallin lähde sijaitsee:

```text
src/co_op_translator/templates/other_courses.md
```

Päivittääksesi jaetun sisällön:

1. Muokkaa mallia.
2. Avaa pull request Co-op Translatorille.
3. Kun muutos on julkaistu, suorita Co-op Translator kohdearkistossa.

## Sparse Checkout -ohje

Suuret kurssirepositoriot voivat tulla kalliiksi kloonata, jos ne sisältävät paljon käännettyjä tulosteita. Voit lisätä tämän ohjeen luotuihin kieliosioihin:

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