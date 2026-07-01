# Riferimento CLI

Co-op Translator installa questi punti di ingresso da riga di comando:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

I comandi `translate`, `evaluate`, `migrate-links` e `co-op-review` vengono instradati tramite `co_op_translator.__main__`, che seleziona l'implementazione del comando in base al nome dello script invocato. Il server MCP utilizza direttamente `co_op_translator.mcp.server`.

Se stai decidendo tra CLI, API Python e MCP, inizia con [Scegli il tuo flusso di lavoro](workflows.md).

## Flusso iniziale della CLI

Inizia qui se usi Co-op Translator da un terminale:

1. Configura un provider LLM come descritto in [Configurazione](configuration.md).
2. Scegli il tipo di contenuto che vuoi tradurre.
3. Esegui prima un comando mirato, come la traduzione solo di Markdown.
4. Usa `--dry-run` prima di modifiche ampie al repository.
5. Usa `co-op-review` dopo la traduzione per verificare struttura e aggiornamento.

| Obiettivo | Comando da usare |
| --- | --- |
| Tradurre documenti Markdown | `translate -l "ko" -md` |
| Tradurre notebook | `translate -l "ko" -nb` |
| Tradurre testo nelle immagini | `translate -l "ko" -img` |
| Anteprima del lavoro senza scrivere file | `translate -l "ko" -md --dry-run` |
| Rivedere traduzioni esistenti | `co-op-review -l "ko"` |
| Aggiornare link di notebook e Markdown | `migrate-links -l "ko" --dry-run` |
| Esporre strumenti a un client MCP | Configura il [Server MCP](mcp.md) anziché eseguire direttamente i comandi CLI. |

## translate

Traduci file Markdown, notebook e testo nelle immagini in una o più lingue di destinazione.

```bash
translate -l "ko ja fr"
```

### Esempi comuni

Traduci solo Markdown:

```bash
translate -l "de" -md
```

Traduci solo notebook:

```bash
translate -l "zh-CN" -nb
```

Traduci Markdown e immagini:

```bash
translate -l "pt-BR" -md -img
```

Aggiorna traduzioni esistenti eliminandole e ricreandole:

```bash
translate -l "ko" -u
```

Esegui senza prompt interattivi:

```bash
translate -l "ko ja" -md -y
```

Salva i log:

```bash
translate -l "ko" -s
```

### Opzioni

| Opzione | Obbligatorio | Descrizione |
| --- | --- | --- |
| `-l`, `--language-codes` | Sì | Codici lingua separati da spazi, come `"es fr de"`, oppure `"all"`. |
| `-r`, `--root-dir` | No | Radice del progetto. Predefinita la directory corrente. |
| `-u`, `--update` | No | Elimina le traduzioni esistenti per le lingue selezionate e le ricrea. |
| `-img`, `--images` | No | Traduci solo i file immagine. |
| `-md`, `--markdown` | No | Traduci solo i file Markdown. |
| `-nb`, `--notebook` | No | Traduci solo i file notebook Jupyter. |
| `-d`, `--debug` | No | Abilita il logging di debug nella console. |
| `-s`, `--save-logs` | No | Salva i log a livello DEBUG in `<root-dir>/logs/`. |
| `-x`, `--fix` | No | Ritraduci i file Markdown a bassa confidenza basandosi sui risultati di valutazioni precedenti. |
| `-c`, `--min-confidence` | No | Soglia di confidenza per `--fix`. Predefinita `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Aggiungi o sopprimi i disclaimer della traduzione automatica. Abilitati per impostazione predefinita nella CLI. |
| `-f`, `--fast` | No | Modalità immagine veloce deprecata. |
| `-y`, `--yes` | No | Conferma automaticamente i prompt, utile in CI. |
| `--repo-url` | No | URL del repository usato nell'avviso di sparse-checkout della tabella lingue del README. |
| `--migrate-language-folders` | No | Rinomina cartelle alias legacy, come `cn` o `tw`, in cartelle canoniche BCP 47. |
| `--dry-run` | No | Anteprima della migrazione delle cartelle linguistiche e delle stime di traduzione senza scrivere file. |

Se non viene fornito alcun flag di tipo, `translate` elabora Markdown, notebook e immagini. La traduzione delle immagini richiede la configurazione di Azure AI Vision.

## evaluate

Valuta la qualità delle traduzioni Markdown per una lingua.

!!! warning "Sperimentale"
    `evaluate` è sperimentale. Può usare controlli qualitativi basati su regole e su LLM, scrive i risultati della valutazione nei metadati di traduzione e il suo modello di scoring e il comportamento dei metadati potrebbero cambiare.

```bash
evaluate -l "ko"
```

### Esempi comuni

Usa una soglia di bassa confidenza più restrittiva:

```bash
evaluate -l "es" -c 0.8
```

Esegui solo verifiche basate su regole:

```bash
evaluate -l "fr" -f
```

Esegui solo verifiche basate su LLM:

```bash
evaluate -l "ja" -D
```

### Opzioni

| Opzione | Obbligatorio | Descrizione |
| --- | --- | --- |
| `-l`, `--language-code` | Sì | Singolo codice lingua da valutare. I codici alias vengono normalizzati. |
| `-r`, `--root-dir` | No | Radice del progetto. Predefinita la directory corrente. |
| `-c`, `--min-confidence` | No | Soglia usata per elencare le traduzioni a bassa confidenza. Predefinita `0.7`. |
| `-d`, `--debug` | No | Abilita il logging di debug. |
| `-s`, `--save-logs` | No | Salva i log a livello DEBUG in `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Solo valutazione basata su regole. |
| `-D`, `--deep` | No | Solo valutazione basata su LLM. |

Per impostazione predefinita, `evaluate` utilizza sia la valutazione basata su regole che quella basata su LLM. I risultati vengono scritti nei metadati di traduzione e riassunti nella console.

## co-op-review

Esegui controlli deterministici di manutenzione delle traduzioni senza credenziali API.

!!! note "Beta"
    `co-op-review` è un comando di revisione deterministico in beta. Non chiama provider di modelli né scrive file, ma i suoi controlli e lo schema di output delle issue potrebbero evolversi.

```bash
co-op-review -l "ko"
```

### Esempi comuni

Rivedi traduzioni in coreano e giapponese dalla directory corrente:

```bash
co-op-review -l "ko ja"
```

Rivedi una specifica radice di progetto:

```bash
co-op-review -l "fr" -r ./my-course
```

Rivedi solo i file sorgente modificati rispetto a un ref base:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Stampa output in Markdown in stile GitHub per riassunti CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Opzioni

| Opzione | Obbligatorio | Descrizione |
| --- | --- | --- |
| `-l`, `--language-code` | No | Codice lingua da revisionare. Può essere passato più volte o come valore separato da spazi. Predefinito: tutte le lingue di traduzione rilevate. |
| `-r`, `--root-dir` | No | Radice del progetto. Predefinita la directory corrente. |
| `--changed-from` | No | Ref git usato per limitare la revisione ai file sorgente modificati. |
| `--format` | No | Formato di output: `text` o `github`. Predefinito `text`. |

`co-op-review` attualmente controlla la presenza di file tradotti mancanti, metadati di traduzione mancanti o obsoleti, frontmatter del Markdown e integrità dei blocchi di codice, JSON di notebook tradotto non valido e destinazioni di link locali a file Markdown o immagini mancanti. I link mancanti sono avvisi per impostazione predefinita; i problemi di struttura e di aggiornamento fanno fallire il comando.

## co-op-translator-mcp

Esegui il server MCP di Co-op Translator per agenti, editor e client compatibili MCP.

```bash
co-op-translator-mcp
```

Il trasporto predefinito è `stdio`. Consulta la guida del [Server MCP](mcp.md) per la configurazione del client, gli strumenti, le risorse e le note sulla sicurezza.

### Opzioni

| Opzione | Obbligatorio | Descrizione |
| --- | --- | --- |
| `--transport` | No | Trasporto MCP: `stdio`, `streamable-http`, o `sse`. Predefinito `stdio`. |

## migrate-links

Rielabora i file Markdown tradotti e aggiorna i link dei notebook in modo che puntino ai notebook tradotti quando disponibili.

```bash
migrate-links -l "ko ja"
```

### Esempi comuni

Anteprima degli aggiornamenti dei link:

```bash
migrate-links -l "ko" --dry-run
```

Elabora tutte le lingue supportate senza conferma:

```bash
migrate-links -l "all" -y
```

Riscrivi i link solo quando esistono notebook tradotti:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Opzioni

| Opzione | Obbligatorio | Descrizione |
| --- | --- | --- |
| `-l`, `--language-codes` | Sì | Codici lingua separati da spazi, oppure `"all"`. |
| `-r`, `--root-dir` | No | Radice del progetto. Predefinita la directory corrente. |
| `--image-dir` | No | Cartella delle immagini tradotte relativa alla radice. Predefinita `translated_images`. |
| `--dry-run` | No | Mostra i file che verrebbero modificati senza scrivere aggiornamenti. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Usa i link originali dei notebook quando i notebook tradotti mancano. Abilitato per impostazione predefinita. |
| `-d`, `--debug` | No | Abilita il logging di debug. |
| `-s`, `--save-logs` | No | Salva i log a livello DEBUG in `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Conferma automaticamente i prompt quando si elaborano tutte le lingue. |

## Ambiente

Tutti i comandi richiedono un provider LLM configurato:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# O OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

La traduzione delle immagini richiede inoltre Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Layout di output

Le traduzioni testuali vengono scritte in:

```text
translations/<language-code>/<original-path>
```

L'output delle immagini tradotte viene scritto in:

```text
translated_images/<language-code>/<original-path>
```

Ad esempio, traducendo `README.md` e `docs/setup.md` in coreano si ottiene:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Esempi CLI per copia-incolla

Traduci Markdown in tre lingue:

```bash
translate -l "ko ja fr" -md
```

Traduci solo i notebook:

```bash
translate -l "zh-CN" -nb
```

Traduci solo le immagini:

```bash
translate -l "pt-BR" -img
```

Anteprima della traduzione Markdown senza scrivere file:

```bash
translate -l "de es" -md --dry-run
```

Ripara traduzioni Markdown a bassa confidenza:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Esegui la traduzione Markdown in modalità CI-friendly:

```bash
translate -l "ko ja" -md -y -s
```

Rivedi l'output tradotto:

```bash
co-op-review -l "ko ja"
```

Anteprima della migrazione dei link:

```bash
migrate-links -l "ko" --dry-run
```