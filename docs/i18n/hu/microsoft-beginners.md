# Microsoft "For Beginners" tárolók

Ez az oldal a Microsoft "For Beginners" tárolók karbantartóinak szól, amelyek a megosztott "Other Courses" README szakaszt használják.

A legtöbb Co-op Translator felhasználónak nincs szüksége erre az oldalra.

## Az "Other Courses" szakasz automatikus szinkronizálása

Helyezze ezeket a jelölőket a README-ben az "Other Courses" szakasz köré:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Minden alkalommal, amikor a Co-op Translator a CLI-n vagy a GitHub Actions-en fut, a jelölők közötti tartalmat a csomagolt sablonnal helyettesíti.

## A megosztott sablon frissítése

A sablon forrása itt található:

```text
src/co_op_translator/templates/other_courses.md
```

A megosztott tartalom frissítéséhez:

1. Szerkessze a sablont.
2. Nyisson egy pull requestet a Co-op Translatorhoz.
3. Miután a változtatás kiadásra került, futtassa a Co-op Translator programot a cél tárolóban.

## Sparse Checkout tájékoztató

A nagy kurzustárak klónozása költséges lehet, ha sok lefordított kimenetet tartalmaznak. Ezt a figyelmeztetést beillesztheti a generált nyelvi szakaszokba:

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