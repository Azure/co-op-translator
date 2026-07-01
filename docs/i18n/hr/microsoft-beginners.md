# Microsoft Repozitoriji za Početnike

Ova stranica je namijenjena održavateljima Microsoftovih "For Beginners" repozitorija koji koriste zajednički odjeljak README-a "Other Courses".

Većina korisnika Co-op Translatora ne treba ovu stranicu.

## Automatsko sinkroniziranje odjeljka "Other Courses"

Dodajte ove markere oko odjeljka "Other Courses" u vašem README-u:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Svaki put kad Co-op Translator pokrene putem CLI-ja ili GitHub Actions, zamijeni sadržaj između markera s pakiranim predloškom.

## Ažurirajte zajednički predložak

Izvor predloška nalazi se na:

```text
src/co_op_translator/templates/other_courses.md
```

Za ažuriranje zajedničkog sadržaja:

1. Uredite predložak.
2. Otvorite pull request za Co-op Translator.
3. Nakon što je promjena objavljena, pokrenite Co-op Translator u ciljanom repozitoriju.

## Savjet za Sparse Checkout

Veliki repozitoriji tečajeva mogu postati skupi za kloniranje kada sadrže mnogo prevedenih rezultata. Možete uključiti ovu obavijest u generirane jezične odjeljke:

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