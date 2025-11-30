<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T11:00:23+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "it"
}
-->
# Riferimento comandi

Il CLI **Co-op Translator** offre diverse opzioni per personalizzare il processo di traduzione:

Comando                                      | Descrizione
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                | Traduce il tuo progetto nelle lingue specificate. Esempio: translate -l "es fr de" traduce in spagnolo, francese e tedesco. Usa translate -l "all" per tradurre in tutte le lingue supportate.
translate -l "language_codes" -u             | Aggiorna le traduzioni eliminando quelle esistenti e ricreandole. Attenzione: questo cancellerà tutte le traduzioni correnti per le lingue specificate.
translate -l "language_codes" -img           | Traduce solo i file immagine.
translate -l "language_codes" -md            | Traduce solo i file Markdown.
translate -l "language_codes" -nb            | Traduce solo i file Jupyter notebook (.ipynb).
translate -l "language_codes" --fix          | Ritraduce i file con punteggi di confidenza bassi basandosi sui risultati di valutazioni precedenti.
translate -l "language_codes" -d             | Abilita la modalità debug per un logging dettagliato.
translate -l "language_codes" --save-logs, -s| Salva i log di livello DEBUG in file sotto <root_dir>/logs/ (la console rimane controllata da -d)
translate -l "language_codes" -r "root_dir"  | Specifica la directory radice del progetto
translate -l "language_codes" -f             | Usa la modalità veloce per la traduzione delle immagini (fino a 3 volte più veloce con un leggero compromesso su qualità e allineamento).
translate -l "language_codes" -y             | Conferma automaticamente tutte le richieste (utile per pipeline CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Abilita o disabilita l'aggiunta di una sezione di disclaimer sulla traduzione automatica nei markdown e notebook tradotti (default: abilitato).
translate -l "language_codes" --help         | Mostra i dettagli di aiuto all'interno del CLI con i comandi disponibili
evaluate -l "language_code"                   | Valuta la qualità della traduzione per una lingua specifica e fornisce punteggi di confidenza
evaluate -l "language_code" -c 0.8            | Valuta le traduzioni con una soglia di confidenza personalizzata
evaluate -l "language_code" -f                | Modalità di valutazione veloce (solo basata su regole, senza LLM)
evaluate -l "language_code" -D                | Modalità di valutazione approfondita (basata su LLM, più accurata ma più lenta)
evaluate -l "language_code" --save-logs, -s   | Salva i log di livello DEBUG in file sotto <root_dir>/logs/
migrate-links -l "language_codes"             | Rielabora i file Markdown tradotti per aggiornare i link ai notebook (.ipynb). Preferisce i notebook tradotti quando disponibili; altrimenti può ricorrere ai notebook originali.
migrate-links -l "language_codes" -r          | Specifica la directory radice del progetto (default: directory corrente).
migrate-links -l "language_codes" --dry-run   | Mostra quali file verrebbero modificati senza scrivere cambiamenti.
migrate-links -l "language_codes" --no-fallback-to-original | Non riscrive i link ai notebook originali quando mancano le controparti tradotte (aggiorna solo se esiste la traduzione).
migrate-links -l "language_codes" -d          | Abilita la modalità debug per un logging dettagliato.
migrate-links -l "language_codes" --save-logs, -s | Salva i log di livello DEBUG in file sotto <root_dir>/logs/
migrate-links -l "all" -y                      | Processa tutte le lingue e conferma automaticamente il prompt di avviso.

## Esempi d'uso

  1. Comportamento predefinito (aggiunge nuove traduzioni senza cancellare quelle esistenti):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Aggiunge solo nuove traduzioni immagini in coreano (non cancella traduzioni esistenti):    translate -l "ko" -img

  3. Aggiorna tutte le traduzioni coreane (Attenzione: cancella tutte le traduzioni coreane esistenti prima di ritradurre):    translate -l "ko" -u

  4. Aggiorna solo le immagini coreane (Attenzione: cancella tutte le immagini coreane esistenti prima di ritradurre):    translate -l "ko" -img -u

  5. Aggiunge nuove traduzioni markdown per il coreano senza modificare altre traduzioni:    translate -l "ko" -md

  6. Corregge traduzioni a bassa confidenza basandosi sui risultati di valutazioni precedenti: translate -l "ko" --fix

  7. Corregge traduzioni a bassa confidenza solo per file specifici (markdown): translate -l "ko" --fix -md

  8. Corregge traduzioni a bassa confidenza solo per file specifici (immagini): translate -l "ko" --fix -img

  9. Usa la modalità veloce per la traduzione delle immagini:    translate -l "ko" -img -f

  10. Corregge traduzioni a bassa confidenza con soglia personalizzata: translate -l "ko" --fix -c 0.8

  11. Esempio modalità debug: - translate -l "ko" -d: Abilita il logging di debug.
  12. Salva i log su file: translate -l "ko" -s
  13. DEBUG su console e file: translate -l "ko" -d -s
  14. Traduce senza aggiungere disclaimer di traduzione automatica agli output: translate -l "ko" --no-disclaimer

  15. Migra i link ai notebook per le traduzioni coreane (aggiorna i link ai notebook tradotti quando disponibili):    migrate-links -l "ko"

  15. Migra i link con dry-run (nessuna scrittura su file):    migrate-links -l "ko" --dry-run

  16. Aggiorna i link solo quando esistono notebook tradotti (non ricorre agli originali):    migrate-links -l "ko" --no-fallback-to-original

  17. Processa tutte le lingue con prompt di conferma:    migrate-links -l "all"

  18. Processa tutte le lingue e conferma automaticamente:    migrate-links -l "all" -y
  19. Salva i log su file per migrate-links:    migrate-links -l "ko ja" -s

### Esempi di valutazione

> [!WARNING]  
> **Funzionalità Beta**: La funzionalità di valutazione è attualmente in beta. Questa funzione è stata rilasciata per valutare i documenti tradotti, e i metodi di valutazione e l'implementazione dettagliata sono ancora in fase di sviluppo e soggetti a modifiche.

  1. Valuta le traduzioni coreane: evaluate -l "ko"

  2. Valuta con soglia di confidenza personalizzata: evaluate -l "ko" -c 0.8

  3. Valutazione veloce (solo basata su regole): evaluate -l "ko" -f

  4. Valutazione approfondita (basata su LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->