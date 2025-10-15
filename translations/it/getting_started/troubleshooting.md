<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:05:23+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "it"
}
-->
# Guida alla Risoluzione dei Problemi di Microsoft Co-op Translator

## Panoramica
Microsoft Co-Op Translator è uno strumento potente per tradurre documenti Markdown in modo semplice e veloce. Questa guida ti aiuterà a risolvere i problemi più comuni che potresti incontrare durante l'utilizzo dello strumento.

## Problemi Comuni e Soluzioni

### 1. Problema con il Tag Markdown
**Problema:** Il documento Markdown tradotto include un tag `markdown` in cima, causando problemi di visualizzazione.

**Soluzione:** Per risolvere, elimina semplicemente il tag `markdown` all'inizio del file. In questo modo il file Markdown verrà visualizzato correttamente.

**Passaggi:**
1. Apri il file Markdown (`.md`) tradotto.
2. Trova il tag `markdown` in cima al documento.
3. Elimina il tag `markdown`.
4. Salva le modifiche al file.
5. Riapri il file per assicurarti che venga visualizzato correttamente.

### 2. Problema con gli URL delle Immagini Incorporate
**Problema:** Gli URL delle immagini incorporate non corrispondono alla lingua del documento, causando immagini errate o mancanti.

**Soluzione:** Controlla l’URL delle immagini incorporate e assicurati che corrispondano alla lingua del documento. Tutte le immagini si trovano nella cartella `translated_images` e ogni immagine ha un tag della lingua nel nome del file.

**Passaggi:**
1. Apri il documento Markdown tradotto.
2. Identifica le immagini incorporate e i loro URL.
3. Verifica che il tag della lingua nel nome del file dell’immagine corrisponda a quello del documento.
4. Aggiorna gli URL se necessario.
5. Salva le modifiche e riapri il documento per confermare che le immagini vengano visualizzate correttamente.

### 3. Accuratezza della Traduzione
**Problema:** Il contenuto tradotto non è accurato o necessita di ulteriori modifiche.

**Soluzione:** Rivedi il documento tradotto e apporta le modifiche necessarie per migliorarne l’accuratezza e la leggibilità.

**Passaggi:**
1. Apri il documento tradotto.
2. Rivedi attentamente il contenuto.
3. Apporta le modifiche necessarie per migliorare la traduzione.
4. Salva le modifiche.

## 4. Errore di Permessi Redatto o 404

Se immagini o testo non vengono tradotti nella lingua corretta e in modalità debug (-d) ricevi un errore 401, si tratta di un classico errore di autenticazione: la chiave è invalida, scaduta o non collegata alla regione dell’endpoint.

Esegui co-op translator con il [parametro -d debug](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) per capire meglio la causa del problema.

- **Messaggio di errore**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Possibili cause**:
  - La chiave di sottoscrizione è stata redatta o è errata nella richiesta.
  - La chiave AI Services o Subscription Key potrebbe appartenere a una risorsa Azure diversa (come Translator o OpenAI) invece che a una risorsa **Azure AI Vision**.

 **Tipo di risorsa**
  - Vai su [Azure Portal](https://portal.azure.com) o [Azure AI Foundry](https://ai.azure.com) e assicurati che la risorsa sia di tipo `Azure AI services` → `Vision`.
  - Valida le chiavi e assicurati di utilizzare quella corretta.

## 5. Errori di Configurazione (Nuova Gestione Errori)

Con il nuovo sistema di traduzione selettiva, Co-op Translator ora fornisce messaggi di errore espliciti quando i servizi richiesti non sono configurati.

### 5.1. Azure AI Service non Configurato per la Traduzione di Immagini

**Problema:** Hai richiesto la traduzione delle immagini (flag `-img`) ma Azure AI Service non è configurato correttamente.

**Messaggio di errore:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Soluzione:**
1. **Opzione 1**: Configura Azure AI Service
   - Aggiungi `AZURE_AI_SERVICE_API_KEY` al tuo file `.env`
   - Aggiungi `AZURE_AI_SERVICE_ENDPOINT` al tuo file `.env`
   - Verifica che il servizio sia accessibile

2. **Opzione 2**: Rimuovi la richiesta di traduzione immagini
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Configurazione Necessaria Mancante

**Problema:** Manca la configurazione essenziale per LLM.

**Messaggio di errore:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Soluzione:**
1. Verifica che il tuo file `.env` contenga almeno una delle seguenti configurazioni LLM:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` e `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   È necessario configurare Azure OpenAI OPPURE OpenAI, non entrambi.

### 5.3. Confusione nella Traduzione Selettiva

**Problema:** Nessun file è stato tradotto anche se il comando è andato a buon fine.

**Possibili cause:**
- Flag del tipo di file errati (`-md`, `-img`, `-nb`)
- Nessun file corrispondente nel progetto
- Struttura delle cartelle non corretta

**Soluzione:**
1. **Usa la modalità debug** per vedere cosa succede:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Controlla i tipi di file** nel tuo progetto:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Verifica le combinazioni di flag**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migrazione dal Vecchio Sistema

### 6.1. Modalità Solo Markdown Deprecata

**Problema:** I comandi che si basavano sul fallback automatico solo markdown non funzionano più come previsto.

**Comportamento precedente:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Nuovo comportamento:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Soluzione:**
- **Sii esplicito** su cosa vuoi tradurre:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Comportamento Inatteso dei Link

**Problema:** I link nei file tradotti puntano a posizioni inattese.

**Causa:** L’elaborazione dinamica dei link cambia in base ai tipi di file selezionati.

**Soluzione:**
1. **Comprendi il nuovo comportamento dei link**:
   - `-nb` incluso: I link ai notebook puntano alle versioni tradotte
   - `-nb` escluso: I link ai notebook puntano ai file originali
   - `-img` incluso: I link alle immagini puntano alle versioni tradotte
   - `-img` escluso: I link alle immagini puntano ai file originali

2. **Scegli la combinazione giusta** per il tuo caso d’uso:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action eseguita ma nessuna Pull Request (PR) creata

**Sintomo:** Nei log del workflow per `peter-evans/create-pull-request` compare:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Cause probabili:**
- **Nessuna modifica rilevata:** Il passaggio di traduzione non ha prodotto differenze (il repository è già aggiornato).
- **Output ignorati:** `.gitignore` esclude file che ti aspetti di commettere (es. `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths non corrispondenti:** I percorsi forniti all’action non corrispondono alle posizioni effettive degli output.
- **Logica/condizioni del workflow:** Il passaggio di traduzione è terminato in anticipo o ha scritto in cartelle inattese.

**Come risolvere / verificare:**
1. **Conferma che gli output esistano:** Dopo la traduzione, controlla che nella workspace ci siano file nuovi/modificati in `translations/` e/o `translated_images/`.
   - Se traduci notebook, assicurati che i file `.ipynb` siano effettivamente scritti in `translations/<lang>/...`.
2. **Controlla `.gitignore`:** Non ignorare gli output generati. Assicurati di NON ignorare:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (se traduci notebook)
3. **Assicurati che add-paths corrisponda agli output:** Usa un valore multilinea e includi entrambe le cartelle se necessario:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Forza una PR per il debug:** Permetti temporaneamente commit vuoti per confermare che il wiring sia corretto:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Esegui in modalità debug:** Aggiungi `-d` al comando di traduzione per stampare quali file sono stati trovati e scritti.
6. **Permessi (GITHUB_TOKEN):** Assicurati che il workflow abbia i permessi di scrittura per creare commit e PR:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Checklist Rapida per il Debug

Quando risolvi problemi di traduzione:

1. **Usa la modalità debug**: Aggiungi il flag `-d` per vedere i log dettagliati
2. **Controlla i tuoi flag**: Assicurati che `-md`, `-img`, `-nb` corrispondano a ciò che vuoi fare
3. **Verifica la configurazione**: Controlla che il file `.env` abbia le chiavi richieste
4. **Testa in modo incrementale**: Inizia solo con `-md`, poi aggiungi altri tipi
5. **Controlla la struttura dei file**: Assicurati che i file sorgente esistano e siano accessibili

Per informazioni più dettagliate su comandi e flag disponibili, consulta la [Command Reference](./command-reference.md).

---

**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.