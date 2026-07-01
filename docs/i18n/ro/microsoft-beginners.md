# Repozitoriile Microsoft "For Beginners"

Această pagină este pentru menținătorii repo-urilor Microsoft "For Beginners" care folosesc secțiunea comună README "Other Courses".

Majoritatea utilizatorilor Co-op Translator nu au nevoie de această pagină.

## Auto-Sync the Other Courses Section

Adăugați aceste marcatoare în jurul secțiunii "Other Courses" din README-ul vostru:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

De fiecare dată când Co-op Translator rulează prin CLI sau GitHub Actions, înlocuiește conținutul dintre marcatoare cu șablonul pachetizat.

## Update the Shared Template

Sursa șablonului se află la:

```text
src/co_op_translator/templates/other_courses.md
```

Pentru a actualiza conținutul partajat:

1. Editează șablonul.
2. Deschide un pull request către Co-op Translator.
3. După ce schimbarea este lansată, rulează Co-op Translator în repository-ul țintă.

## Sparse Checkout Advisory

Repozitore mari pentru cursuri pot deveni costisitoare de clonat când includ multe rezultate traduse. Puteți include acest aviz în secțiunile generate pentru limbă:

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