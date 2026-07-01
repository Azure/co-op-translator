# Risoluzione dei problemi

Usa questa pagina quando una esecuzione di traduzione riesce inaspettatamente, fallisce durante la configurazione o produce output che necessita di revisione.

## Inizia qui

1. Esegui prima un comando mirato, ad esempio `translate -l "ko" -md`.
2. Aggiungi `-d` per i log di debug sulla console.
3. Aggiungi `-s` per salvare i log di debug in `<root-dir>/logs/`.
4. Esegui `co-op-review` dopo la traduzione per verificare aggiornamento, struttura e link locali.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Errori di configurazione

### Nessun provider di modelli linguistici

Errore:

```text
No language model configuration found.
```

Soluzione:

- Configura Azure OpenAI o OpenAI.
- Verifica che le variabili siano nell'ambiente in cui viene eseguito il comando.
- Per uso locale, inseriscile in `.env` nella radice del progetto.

Vedi [Configurazione](configuration.md).

### Traduzione delle immagini senza Azure AI Vision

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
- Conferma che il nome del deployment Azure OpenAI e la versione API corrispondano al tuo deployment.
- Esegui con i log di debug: `translate -l "ko" -md -d -s`.

## Nessun file è stato tradotto

Cause comuni:

- Le flag selezionate non corrispondono ai tuoi file.
- Sono già presenti file tradotti.
- I file sorgente si trovano in directory escluse.
- Il comando viene eseguito dalla radice del progetto sbagliata.

Controlli:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Usa `--root-dir` quando il comando viene eseguito al di fuori della radice del progetto.

## Comportamento imprevisto dei collegamenti

La riscrittura dei link dipende dai tipi di contenuto selezionati:

- `-nb` incluso: i link ai notebook possono puntare ai notebook tradotti.
- `-nb` escluso: i link ai notebook possono rimanere puntati sui notebook sorgente.
- `-img` incluso: i link alle immagini possono puntare alle immagini tradotte.
- `-img` escluso: i link alle immagini possono rimanere puntati sulle immagini sorgente.

Esegui una traduzione completa dei contenuti quando tutti i link interni devono preferire gli output tradotti:

```bash
translate -l "ko" -md -nb -img
```

Esegui la revisione dei link dopo la traduzione:

```bash
co-op-review -l "ko"
```

## Problemi di rendering del Markdown

Se il Markdown tradotto non viene renderizzato correttamente:

- Controlla che il frontmatter inizi e finisca con `---`.
- Controlla che il numero delle fence di codice corrisponda tra i file sorgente e tradotti.
- Esegui `co-op-review` per individuare problemi strutturali comuni.
- Ritraduci il file specifico se l'output è stato corrotto.

```bash
co-op-review -l "ko" --format github
```

## L'Action di GitHub è stata eseguita ma non è stata creato alcun pull request

Se `peter-evans/create-pull-request` riporta che il branch non è avanti rispetto al base, il workflow non ha trovato file da commitare.

Possibili cause:

- La run di traduzione non ha prodotto cambiamenti.
- `.gitignore` esclude `translations/`, `translated_images/` o i notebook tradotti.
- `add-paths` non corrisponde alle directory di output generate.
- Il passo di traduzione è terminato in anticipo.

Soluzioni:

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

Le traduzioni automatiche possono richiedere una revisione umana. Usa `evaluate` solo quando desideri valutazioni di qualità sperimentali e workflow di riparazione per bassa confidenza.

!!! warning "Sperimentale"
    `evaluate` può usare controlli basati su regole e LLM, e il suo modello di scoring e il comportamento dei metadati possono cambiare. Tienilo fuori dalle pipeline CI obbligatorie a meno che il tuo workflow non sia preparato per i cambiamenti.

Per controlli CI deterministici, usa `co-op-review` invece.