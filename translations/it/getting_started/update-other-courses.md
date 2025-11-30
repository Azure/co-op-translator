<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:42:47+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "it"
}
-->
# Aggiorna la sezione "Altri Corsi" (repository Microsoft Beginners)

Questa guida spiega come rendere la sezione "Altri Corsi" sincronizzata automaticamente usando Co-op Translator, e come aggiornare il modello globale per tutti i repository.

- Si applica a: solo repository Microsoft Beginners
- Funziona con: Co-op Translator CLI e GitHub Actions
- Fonte del modello: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Avvio rapido: Abilita la sincronizzazione automatica nel tuo repository

Aggiungi i seguenti marker intorno alla sezione "Altri Corsi" nel tuo README. Co-op Translator sostituirà tutto ciò che si trova tra questi marker ad ogni esecuzione.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Ogni volta che Co-op Translator viene eseguito—tramite CLI (es. `translate -l "<language codes>"`) o GitHub Actions—aggiorna automaticamente la sezione "Altri Corsi" racchiusa da questi marker.

> [!NOTE]
> Se hai già una lista esistente, basta racchiuderla con gli stessi marker. Alla prossima esecuzione verrà sostituita con il contenuto standardizzato più recente.

---

## Come modificare il contenuto globale

Se vuoi aggiornare il contenuto standardizzato che appare in tutti i repository Beginners:

1. Modifica il modello: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Apri una pull request nel repository Co-op Translator con le tue modifiche
3. Dopo che la PR è stata unita, la versione di Co-op Translator sarà aggiornata
4. Alla prossima esecuzione di Co-op Translator (CLI o GitHub Action) in un repository target, la sezione aggiornata verrà sincronizzata automaticamente

Questo garantisce una fonte unica e affidabile per il contenuto "Altri Corsi" in tutti i repository Beginners.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avvertenza**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->