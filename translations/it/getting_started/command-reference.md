<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:04:58+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "it"
}
-->
# Riferimento comandi

La CLI **Co-op Translator** offre diverse opzioni per personalizzare il processo di traduzione:

Comando                                       | Descrizione
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "codici_lingua"                  | Traduce il tuo progetto nelle lingue specificate. Esempio: translate -l "es fr de" traduce in spagnolo, francese e tedesco. Usa translate -l "all" per tradurre in tutte le lingue supportate.
translate -l "codici_lingua" -u               | Aggiorna le traduzioni eliminando quelle esistenti e ricreandole. Attenzione: questo cancellerà tutte le traduzioni attuali per le lingue specificate.
translate -l "codici_lingua" -img             | Traduce solo i file immagine.
translate -l "codici_lingua" -md              | Traduce solo i file Markdown.
translate -l "codici_lingua" -nb              | Traduce solo i file Jupyter notebook (.ipynb).
translate -l "codici_lingua" --fix            | Ritraduce i file con punteggi di confidenza bassi in base ai risultati di valutazione precedenti.
translate -l "codici_lingua" -d               | Attiva la modalità debug per una registrazione dettagliata.
translate -l "codici_lingua" --save-logs, -s  | Salva i log di livello DEBUG nei file sotto <root_dir>/logs/ (la console resta controllata da -d)
translate -l "codici_lingua" -r "root_dir"    | Specifica la directory principale del progetto
translate -l "codici_lingua" -f               | Usa la modalità veloce per la traduzione delle immagini (fino a 3 volte più veloce, con una leggera perdita di qualità e allineamento).
translate -l "codici_lingua" -y               | Conferma automaticamente tutte le richieste (utile per pipeline CI/CD)
translate -l "codici_lingua" --help           | Mostra i dettagli di aiuto nella CLI con i comandi disponibili
evaluate -l "codice_lingua"                   | Valuta la qualità della traduzione per una lingua specifica e fornisce punteggi di confidenza
evaluate -l "codice_lingua" -c 0.8            | Valuta le traduzioni con una soglia di confidenza personalizzata
evaluate -l "codice_lingua" -f                | Modalità di valutazione veloce (solo basata su regole, senza LLM)
evaluate -l "codice_lingua" -D                | Modalità di valutazione approfondita (solo LLM, più accurata ma più lenta)
evaluate -l "codice_lingua" --save-logs, -s   | Salva i log di livello DEBUG nei file sotto <root_dir>/logs/
migrate-links -l "codici_lingua"              | Rielabora i file Markdown tradotti per aggiornare i link ai notebook (.ipynb). Preferisce i notebook tradotti quando disponibili; altrimenti può usare quelli originali.
migrate-links -l "codici_lingua" -r           | Specifica la directory principale del progetto (predefinita: directory corrente).
migrate-links -l "codici_lingua" --dry-run    | Mostra quali file verrebbero modificati senza scrivere le modifiche.
migrate-links -l "codici_lingua" --no-fallback-to-original | Non riscrivere i link ai notebook originali quando mancano le versioni tradotte (aggiorna solo se esiste la traduzione).
migrate-links -l "codici_lingua" -d           | Attiva la modalità debug per una registrazione dettagliata.
migrate-links -l "codici_lingua" --save-logs, -s | Salva i log di livello DEBUG nei file sotto <root_dir>/logs/
migrate-links -l "all" -y                      | Elabora tutte le lingue e conferma automaticamente l'avviso.

## Esempi di utilizzo

  1. Comportamento predefinito (aggiunge nuove traduzioni senza eliminare quelle esistenti):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Aggiungi solo nuove traduzioni di immagini in coreano (le traduzioni esistenti non vengono eliminate):    translate -l "ko" -img

  3. Aggiorna tutte le traduzioni coreane (Attenzione: questo elimina tutte le traduzioni coreane esistenti prima di ritradurre):    translate -l "ko" -u

  4. Aggiorna solo le immagini coreane (Attenzione: questo elimina tutte le immagini coreane esistenti prima di ritradurre):    translate -l "ko" -img -u

  5. Aggiungi nuove traduzioni Markdown per il coreano senza modificare le altre traduzioni:    translate -l "ko" -md

  6. Correggi le traduzioni con bassa confidenza in base ai risultati di valutazione precedenti: translate -l "ko" --fix

  7. Correggi le traduzioni con bassa confidenza solo per file specifici (markdown): translate -l "ko" --fix -md

  8. Correggi le traduzioni con bassa confidenza solo per file specifici (immagini): translate -l "ko" --fix -img

  9. Usa la modalità veloce per la traduzione delle immagini:    translate -l "ko" -img -f

  10. Correggi le traduzioni con bassa confidenza con soglia personalizzata: translate -l "ko" --fix -c 0.8

  11. Esempio di modalità debug: - translate -l "ko" -d: Attiva la registrazione debug.
  12. Salva i log nei file: translate -l "ko" -s
  13. DEBUG su console e file: translate -l "ko" -d -s

  14. Migra i link ai notebook per le traduzioni coreane (aggiorna i link ai notebook tradotti quando disponibili):    migrate-links -l "ko"

  15. Migra i link con dry-run (nessuna scrittura sui file):    migrate-links -l "ko" --dry-run

  16. Aggiorna i link solo quando esistono notebook tradotti (non usare quelli originali):    migrate-links -l "ko" --no-fallback-to-original

  17. Elabora tutte le lingue con richiesta di conferma:    migrate-links -l "all"

  18. Elabora tutte le lingue e conferma automaticamente:    migrate-links -l "all" -y
  19. Salva i log nei file per migrate-links:    migrate-links -l "ko ja" -s

### Esempi di valutazione

> [!WARNING]  
> **Funzionalità Beta**: La funzionalità di valutazione è attualmente in beta. Questa funzione è stata rilasciata per valutare i documenti tradotti, e i metodi di valutazione e l'implementazione dettagliata sono ancora in sviluppo e soggetti a modifiche.

  1. Valuta le traduzioni coreane: evaluate -l "ko"

  2. Valuta con soglia di confidenza personalizzata: evaluate -l "ko" -c 0.8

  3. Valutazione veloce (solo basata su regole): evaluate -l "ko" -f

  4. Valutazione approfondita (solo LLM): evaluate -l "ko" -D

---

**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.