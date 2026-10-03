# Server MCP

Co-op Translator include un server del Model Context Protocol per agenti, editor e client compatibili con MCP.

Per la configurazione locale predefinita, gli utenti non mantengono un server separato in esecuzione manualmente. Configurano il loro client MCP e il client avvia automaticamente `co-op-translator-mcp` tramite `stdio` quando ha bisogno degli strumenti di Co-op Translator.

Se stai decidendo tra CLI, API Python e MCP, inizia con [Scegli il tuo flusso di lavoro](workflows.md).

Usa MCP quando un agente o un editor deve chiamare Co-op Translator direttamente:

| Obiettivo dell'utente | Strumenti MCP |
| --- | --- |
| Tradurre un singolo documento Markdown, un notebook o un'immagine | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Tradurre contenuti Markdown o notebook con il modello host dell'agente | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Riscrivere i link tradotti di Markdown o notebook dopo aver scelto il percorso di output | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Tradurre un intero repository come la CLI | `run_translation`, `translate_project` |
| Rivedere l'output tradotto senza credenziali LLM | `run_review` |
| Verificare le funzionalità e lo stato dell'ambiente | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Il server MCP avvolge la stessa API Python pubblica documentata in [Python API](api.md). Gli strumenti basati su provider utilizzano gli stessi provider configurati della CLI e dell'API Python. Gli strumenti assistiti dall'agente preparano i chunk perché l'agente host MCP li traduca, quindi usano Co-op Translator per ricostruire il Markdown o il notebook finale.

## Passo 1: Installa e configura Co-op Translator

Installa Co-op Translator nell'ambiente Python che il tuo client MCP utilizzerà:

```bash
pip install co-op-translator
```

Per lo sviluppo locale da questo repository, installa il pacchetto in modalità editabile:

```bash
pip install -e .
```

Scegli la modalità di traduzione che il tuo client MCP utilizzerà:

| Modalità | Usalo per | Credenziali |
| --- | --- | --- |
| Basato su provider | Co-op Translator chiama `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, o `run_translation`. | La traduzione richiede Azure OpenAI, OpenAI o Anthropic. La traduzione delle immagini richiede inoltre Azure AI Vision. |
| Assistito dall'agente | L'agente host MCP traduce i chunk restituiti da `start_markdown_agent_translation` o `start_notebook_agent_translation`. | Non sono richieste credenziali provider LLM di Co-op Translator per chunk Markdown o notebook. La traduzione delle immagini non è ancora coperta dalla modalità assistita dall'agente. |

Se inizi con la traduzione di Markdown o notebook all'interno di un agente come Codex o Claude Code, inizia con la modalità assistita dall'agente. Usa la modalità basata su provider quando vuoi che sia Co-op Translator stesso a chiamare i provider configurati, quando stai traducendo immagini o quando esegui la traduzione a livello di repository come con la CLI.

Configura un provider per i flussi di lavoro basati su provider:

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

# O Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

La traduzione delle immagini basata su provider necessita inoltre di:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    La modalità assistita dall'agente copre attualmente Markdown e le celle Markdown dei notebook. La traduzione delle immagini utilizza ancora la pipeline per immagini basata su provider e richiede Azure AI Vision per OCR e rendering consapevole del layout.

## Passo 2: Configura il tuo client MCP

Per la normale configurazione locale `stdio`, aggiungi Co-op Translator alla configurazione del tuo client MCP. Il client avvierà e fermerà il processo automaticamente.

Configurazione del pacchetto installato:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

Configurazione per checkout da sorgente su Windows:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

Configurazione per checkout da sorgente su macOS o Linux:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

Dopo aver modificato la configurazione del client MCP, riavvia o ricarica il client in modo che possa scoprire il nuovo server.

## Passo 3: Verifica il server nel client

Chiedi al client MCP di elencare gli strumenti disponibili o chiama prima uno degli helper in sola lettura:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Controlli iniziali utili:

| Strumento | Cosa verificare |
| --- | --- |
| `get_api_overview` | Conferma che il server è raggiungibile e mostra i flussi di lavoro disponibili. |
| `list_supported_languages` | Conferma che i dati delle lingue inclusi possono essere caricati. |
| `get_configuration_status` | Conferma la disponibilità dei provider LLM e Vision senza esporre valori segreti. |

## Passo 4: Scegli un flusso di lavoro

### Tradurre file o documenti individuali

Usa gli strumenti per contenuti basati su provider quando il client MCP ha già il contenuto del documento o il percorso di un'immagine e Co-op Translator deve chiamare i provider di traduzione configurati.

Per Markdown:

1. Chiama `translate_markdown_content` con `document`, `language_code`, e opzionalmente `source_path`.
2. Se il risultato tradotto verrà scritto in un layout di output di Co-op Translator, chiama `rewrite_markdown_paths`.
3. Lascia che il client scriva o restituisca il `content` finale.

Per i notebook:

1. Chiama `translate_notebook_content` con il JSON del notebook e `language_code`.
2. Chiama `rewrite_notebook_paths` se i link del notebook tradotto devono essere regolati per un percorso di destinazione.
3. Scrivi o restituisci il JSON finale del notebook.

Per le immagini:

1. Chiama `translate_image_content` con `image_path`, `language_code` e opzionalmente `root_dir` o `fast_mode`.
2. Leggi il `data_base64` e il `mime_type` restituiti.
3. Se `output_path` è fornito, l'immagine tradotta viene anche salvata in quel percorso.

Gli strumenti per i contenuti non eseguono la scoperta del progetto, aggiornamenti dei metadati, disclaimer o riscrittura automatica dei percorsi. Se vuoi che l'agente host traduca i chunk di Markdown o notebook senza le credenziali provider LLM di Co-op Translator, usa il flusso di lavoro assistito dall'agente sotto.

### Tradurre con il modello agente host

Usa gli strumenti assistiti dall'agente quando vuoi che l'agente host MCP, come un assistente alla codifica, produca il testo tradotto invece di configurare un provider LLM per Co-op Translator.

In un client MCP basato su chat, normalmente non è necessario scrivere tu stesso il JSON degli strumenti. Chiedi all'agente di usare il flusso di lavoro assistito dall'agente:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Per i notebook, usa lo stesso schema:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Se il tuo client MCP supporta i server prompt, usa `agent_assisted_markdown_translation_prompt` per far caricare al client le stesse istruzioni del flusso di lavoro.

Per Markdown:

1. Chiama `start_markdown_agent_translation` con `document`, `language_code` e opzionalmente `source_path`.
2. Traduci ogni chunk restituito nell'agente host seguendo il `prompt` del chunk.
3. Chiama `finish_markdown_agent_translation` con il `job` originale e i chunk tradotti usando `chunk_id` e `translated_text`.
4. Se il contenuto verrà scritto in un percorso di destinazione tradotto, chiama `rewrite_markdown_paths`.

Per i notebook:

1. Chiama `start_notebook_agent_translation` con il JSON del notebook e `language_code`.
2. Traduci ogni chunk restituito nell'agente host.
3. Chiama `finish_notebook_agent_translation` con il `job` originale e i chunk tradotti.
4. Chiama `rewrite_notebook_paths` se i link del notebook tradotto necessitano di una regolazione del percorso di destinazione.

Gli strumenti assistiti dall'agente non chiamano il provider LLM configurato di Co-op Translator. L'agente host è responsabile della traduzione dei chunk restituiti. Co-op Translator gestisce il chunking del Markdown, la preservazione dei segnaposto, la ricostruzione del frontmatter, la sostituzione delle celle del notebook e la normalizzazione post-traduzione.

### Tradurre un intero repository

Usa `run_translation` quando l'utente vuole che Co-op Translator si comporti come la CLI `translate`.

La traduzione del repository predefinita è `dry_run=true` in modo che un agente possa ispezionare l'ambito prima delle modifiche ai file:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Il risultato di `run_translation` include un array `events` con eventi di avanzamento versionati
`co-op.translation.event.v1`. I client MCP dovrebbero usare campi come
come `type`, `stage_key`, `completed`, `total` e `current_path` invece di
analizzare il testo della console catturato. Passa `json_events_path` per scrivere anche quegli eventi
in un file NDJSON.

Per consentire le scritture, il chiamante deve impostare sia `dry_run=false` che `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` è esposto come alias di compatibilità per `run_translation`.

### Revisionare l'output tradotto

Usa `run_review` per controlli deterministici che non richiedono credenziali LLM o Vision:

!!! note "Beta"
    MCP espone l'API beta `run_review`. È sicura per flussi di lavoro di revisione in sola lettura, ma i controlli di revisione e gli schemi delle issue possono evolvere.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Il risultato include l'output di testo catturato e un sommario di revisione strutturato quando disponibile.

## Esecuzioni manuali del server

Le esecuzioni manuali sono principalmente per il debug o per trasporti che si comportano come server a lunga esecuzione.

Esegui il debug del server stdio predefinito:

```bash
co-op-translator-mcp
```

Esegui da un checkout della sorgente:

```bash
python -m co_op_translator.mcp.server
```

Esegui un server HTTP o SSE a lunga durata:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Per integrazioni locali con editor e agenti, preferisci la configurazione `stdio` gestita dal client nel Passo 2.

## Strumenti

| Strumento | Scopo | Scrive file |
| --- | --- | --- |
| `translate_markdown_content` | Traduci una stringa Markdown. | No |
| `translate_notebook_content` | Traduci le celle Markdown nel JSON del notebook. | No |
| `translate_image_content` | Traduce il testo in un'immagine e restituisce i dati immagine in base64. | Opzionale, solo quando `output_path` è fornito |
| `start_markdown_agent_translation` | Prepara i chunk Markdown affinché l'agente host li traduca senza credenziali LLM di Co-op Translator. | No |
| `finish_markdown_agent_translation` | Ricostruisce il Markdown dai chunk tradotti dall'agente host. | No |
| `start_notebook_agent_translation` | Prepara i chunk delle celle Markdown del notebook affinché l'agente host li traduca. | No |
| `finish_notebook_agent_translation` | Ricostruisce il JSON del notebook dai chunk tradotti dall'agente host. | No |
| `rewrite_markdown_paths` | Riscrive il corpo Markdown e i percorsi del frontmatter per un target tradotto. | No |
| `rewrite_notebook_paths` | Riscrive i percorsi all'interno delle celle Markdown del notebook. | No |
| `run_translation` | Esegue la traduzione a livello di progetto come la CLI. | Sì quando `dry_run=false` e `confirm_write=true` |
| `translate_project` | Alias di compatibilità per `run_translation`. | Sì quando `dry_run=false` e `confirm_write=true` |
| `run_review` | Esegue controlli di revisione deterministici. | No |
| `get_configuration_status` | Riporta i provider LLM e Vision configurati senza esporre segreti. | No |
| `list_supported_languages` | Elenca i codici delle lingue target supportate. | No |
| `get_api_overview` | Descrive i flussi di lavoro e gli strumenti MCP disponibili. | No |

## Risorse

| URI della risorsa | Scopo |
| --- | --- |
| `co-op://api` | Panoramica JSON dei flussi di lavoro e degli strumenti. |
| `co-op://supported-languages` | Elenco JSON dei codici lingua supportati. |
| `co-op://configuration` | Riepilogo JSON della disponibilità dei provider senza segreti. |

## Prompt

| Prompt | Scopo |
| --- | --- |
| `translate_markdown_document_prompt` | Guida un client MCP attraverso la traduzione dei contenuti e l'eventuale riscrittura dei percorsi. |
| `agent_assisted_markdown_translation_prompt` | Guida un client MCP attraverso la traduzione Markdown con agente host senza credenziali provider LLM di Co-op Translator. |
| `translate_repository_prompt` | Guida un client MCP attraverso la traduzione del repository con prima un dry-run. |

## Esempi da copiare e incollare

Traduci contenuto Markdown:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Riscrivi i link Markdown tradotti:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

Traduci Markdown con il modello agente host:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Dopo che l'agente host traduce ogni chunk restituito, termina il job con l'oggetto `job` completo restituito da `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Anteprima della traduzione del repository:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## Risoluzione dei problemi

| Problema | Cosa provare |
| --- | --- |
| Il client MCP non riesce a trovare `co-op-translator-mcp`. | Usa il percorso assoluto dell'eseguibile Python e la configurazione di checkout da sorgente `["-m", "co_op_translator.mcp.server"]`. |
| Il server è elencato ma la traduzione fallisce. | Chiama `get_configuration_status` e conferma che è disponibile un provider LLM. |
| Vuoi la traduzione di Markdown o notebook senza credenziali provider. | Usa `start_markdown_agent_translation` / `finish_markdown_agent_translation` o gli equivalenti per notebook in modo che l'agente host traduca i chunk. |
| La traduzione delle immagini fallisce. | Conferma che le variabili di Azure AI Vision siano impostate e chiama `get_configuration_status`. |
| La traduzione del repository non scrive file. | Imposta `dry_run=false` e `confirm_write=true` solo dopo l'approvazione esplicita dell'utente. |
| Le modifiche alla configurazione del client non appaiono. | Riavvia o ricarica il client MCP. |

## Note sulla sicurezza

- Le chiamate degli strumenti MCP sono controllate dal modello dell'applicazione host, quindi la traduzione del repository è in dry-run per impostazione predefinita.
- La traduzione completa del repository può creare, aggiornare o rimuovere molti file. Richiedi l'approvazione esplicita dell'utente prima di impostare `confirm_write=true`.
- Lo strumento di stato della configurazione non restituisce mai chiavi API, endpoint o altri valori segreti.
- La traduzione delle immagini restituisce dati immagine in base64. Immagini di grandi dimensioni possono produrre risposte dello strumento molto grandi.
- Gli strumenti assistiti dall'agente restituiscono chunk di origine e prompt all'agente host MCP. Usali solo con contenuti che l'utente è a suo agio a inviare a quel modello agente host.