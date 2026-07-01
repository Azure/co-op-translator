# Repositori Microsoft "For Beginners"

Questa pagina è per i manutentori dei repository Microsoft "For Beginners" che utilizzano la sezione README condivisa "Other Courses".

La maggior parte degli utenti di Co-op Translator non ha bisogno di questa pagina.

## Sincronizzazione automatica della sezione "Other Courses"

Aggiungi questi marker intorno alla sezione "Other Courses" nel tuo README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Ogni volta che Co-op Translator viene eseguito tramite la CLI o GitHub Actions, sostituisce il contenuto tra i marker con il template confezionato.

## Aggiorna il template condiviso

La sorgente del template si trova in:

```text
src/co_op_translator/templates/other_courses.md
```

Per aggiornare il contenuto condiviso:

1. Modifica il template.
2. Apri una pull request verso Co-op Translator.
3. Dopo il rilascio della modifica, esegui Co-op Translator nel repository di destinazione.

## Avviso sul Sparse Checkout

I grandi repository dei corsi possono diventare costosi da clonare quando includono molte versioni tradotte. Puoi includere questo avviso nelle sezioni linguistiche generate:

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