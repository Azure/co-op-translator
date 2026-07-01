# Microsoft algajatele mõeldud hoidlad

See leht on mõeldud Microsofti "For Beginners" hoidlate hooldajatele, kes kasutavad jagatud "Other Courses" README-jaotist.

Enamikul Co-op Translatori kasutajatest seda lehte ei ole vaja.

## Other Courses jaotise automaatne sünkroonimine

Lisage need märgised oma README-s "Other Courses" jaotise ümber:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Iga kord, kui Co-op Translator töötab läbi CLI või GitHub Actionsi, asendab see märkide vahelise sisu pakitud malliga.

## Jagatud malli uuendamine

Malli lähtekood asub:

```text
src/co_op_translator/templates/other_courses.md
```

Jagatud sisu uuendamiseks:

1. Muuda malli.
2. Ava pull request Co-op Translatorile.
3. Pärast muudatuse avaldamist käivitage Co-op Translator sihthoidlas.

## Sparse Checkout nõuanne

Suured kursusehoidlad võivad muutuda kloonimiseks kulukaks, kui need sisaldavad palju tõlgitud väljundeid. Saate lisada selle nõuande genereeritud keelejaotistesse:

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