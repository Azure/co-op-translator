# Risoluzione dei problemi

Usa questa pagina quando una traduzione ha successo inaspettatamente, fallisce durante la configurazione o produce un output che necessita di revisione.

## Inizia qui

1. Esegui prima un comando mirato, ad esempio `translate -l "ko" -md`.
2. Aggiungi `-d` per i log di debug sulla console.
3. Aggiungi `-s` per salvare i log di debug sotto `<root-dir>/logs/`.
4. Esegui `co-op-review` dopo la traduzione per verificare freschezza, struttura e link locali.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Errori di configurazione

### Nessun provider di modello linguistico

Errore:

```text
No language model configuration found.
```

Soluzione:

- Configura Azure OpenAI, OpenAI o Anthropic.
- Verifica che le variabili siano nell'ambiente in cui viene eseguito il comando.
- Per uso locale, mettile in `.env` nella root del progetto.

Vedi [Configurazione](configuration.md).

### Traduzione di immagini senza Azure AI Vision

Errore:

```text
Image translation requested but Azure AI Service is not configured.
```

Soluzione:

- Aggiungi `AZURE_AI_SERVICE_API_KEY`.
- Aggiungi `AZURE_AI_SERVICE_ENDPOINT`.
- Oppure esegui un comando solo testo come `translate -l "ko" -md`.

### Chiave o endpoint non validi

I sintomi possono includere `401`, errori di permesso oscurati o errori di accesso all'endpoint.

Soluzione:

- Conferma che la chiave appartenga alla stessa risorsa Azure dell'endpoint.
- Conferma che la risorsa supporti Vision quando usi `-img`.
- Conferma che il nome della deployment di Azure OpenAI e la versione dell'API corrispondano alla tua.
- Esegui con i log di debug: `translate -l "ko" -md -d -s`.

## Nessun file è stato tradotto

Cause comuni:

- Le flag selezionate non corrispondono ai tuoi file.
- Esistono già file tradotti.
- I file sorgente sono sotto directory escluse.
- Il comando viene eseguito dalla root del progetto sbagliata.

Controlli:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Usa `--root-dir` quando il comando viene eseguito al di fuori della root del progetto.

## Comportamento imprevisto dei collegamenti

La riscrittura dei collegamenti dipende dai tipi di contenuto selezionati:

- `-nb` incluso: i collegamenti ai notebook possono puntare ai notebook tradotti.
- `-nb` escluso: i collegamenti ai notebook possono continuare a puntare ai notebook sorgente.
- `-img` incluso: i collegamenti alle immagini possono puntare alle immagini tradotte.
- `-img` escluso: i collegamenti alle immagini possono continuare a puntare alle immagini sorgente.

Esegui una traduzione completa dei contenuti quando tutti i collegamenti interni dovrebbero preferire gli output tradotti:

```bash
translate -l "ko" -md -nb -img
```

Esegui la revisione dei collegamenti dopo la traduzione:

```bash
co-op-review -l "ko"
```

## Problemi di rendering del Markdown

Se il Markdown tradotto viene renderizzato in modo errato:

- Verifica che il frontmatter inizi e termini con `---`.
- Verifica che il numero di delimitatori di codice corrisponda tra file sorgente e tradotto.
- Esegui `co-op-review` per individuare problemi comuni di struttura.
- Ritraduci il file specifico se l'output è stato corrotto.

```bash
co-op-review -l "ko" --format github
```

## L'azione GitHub è stata eseguita ma non è stata creata una Pull Request

Se `peter-evans/create-pull-request` segnala che il ramo non è avanti rispetto al base, il workflow non ha trovato file da commitare.

Cause probabili:

- L'esecuzione di traduzione non ha prodotto modifiche.
- `.gitignore` esclude `translations/`, `translated_images/` o notebook tradotti.
- `add-paths` non corrisponde alle directory di output generate.
- Il passo di traduzione è terminato prematuramente.

Rimedi:

1. Conferma che i file generati esistano in `translations/` o `translated_images/`.
2. Conferma che `.gitignore` non ignori gli output generati.
3. Usa `add-paths` corrispondenti:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Aggiungi temporaneamente flag di debug al comando translate:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Conferma che le autorizzazioni del workflow includano:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Qualità della traduzione

Le traduzioni automatiche possono necessitare di revisione umana. Usa `evaluate` solo quando desideri una valutazione della qualità sperimentale e workflow di riparazione per bassa confidenza.

!!! warning "Experimental"
    `evaluate` può usare controlli basati su regole e su LLM, e il suo modello di punteggio e il comportamento dei metadati possono cambiare. Mantienilo fuori dai gate CI obbligatori a meno che il tuo workflow non sia preparato ai cambiamenti.

Per controlli CI deterministici, usa invece `co-op-review`.