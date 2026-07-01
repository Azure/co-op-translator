# Microsoftovi repozitoriji za začetnike

Ta stran je za vzdrževalce Microsoftovih "For Beginners" repozitorijev, ki uporabljajo skupni razdelek README "Other Courses".

Večini uporabnikov Co-op Translator ta stran ni potrebna.

## Samodejno sinhroniziranje razdelka Other Courses

Dodajte te oznake okoli razdelka "Other Courses" v vašem README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Vsakič, ko Co-op Translator zažene preko CLI ali GitHub Actions, nadomesti vsebino med oznakami s pakiranim predlogom.

## Posodobitev deljenega predloga

Izvor predloge se nahaja na:

```text
src/co_op_translator/templates/other_courses.md
```

Za posodobitev deljene vsebine:

1. Uredite predlogo.
2. Odprite pull request v Co-op Translator.
3. Ko je sprememba izdana, zaženite Co-op Translator v ciljnem repozitoriju.

## Opozorilo o Sparse Checkout

Velika repozitorija tečajev lahko postanejo draga za kloniranje, kadar vključujejo veliko prevedenih izhodov. To opozorilo lahko vključite v ustvarjene jezikovne razdelke:

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