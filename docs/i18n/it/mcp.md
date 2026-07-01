# Server MCP

Co-op Translator include un server Model Context Protocol per agent, editor e client compatibili MCP.

Per la configurazione locale predefinita, gli utenti non devono mantenere un server separato in esecuzione manualmente. Configurano il loro client MCP e il client avvia automaticamente `co-op-translator-mcp` su `stdio` quando necessita degli strumenti di Co-op Translator.

Se stai decidendo tra CLI, Python API e MCP, inizia con [Scegli il flusso di lavoro](workflows.md).

Usa MCP quando un agente o un editor deve chiamare direttamente Co-op Translator:

| Obiettivo utente | Strumenti MCP |
| --- | --- |
| Tradurre un documento Markdown, un notebook o un'immagine | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Tradurre contenuto Markdown o di notebook con il modello host agente | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Riscrivere i link tradotti di Markdown o notebook dopo aver scelto il percorso di output | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Tradurre un intero repository come la CLI | `run_translation`, `translate_project` |
| Revisionare l'output tradotto senza credenziali LLM | `run_review` |
| Ispezionare capacità e stato dell'ambiente | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Il server MCP avvolge la stessa API Python pubblica documentata in [Python API](api.md). Gli strumenti supportati da provider utilizzano gli stessi provider configurati della CLI e della Python API. Gli strumenti assistiti dall'agente preparano i chunk per l'agente host MCP da tradurre, quindi usano Co-op Translator per ricostruire il Markdown o il notebook finale.

## Passo 1: Installa e configura Co-op Translator

Installa Co-op Translator nell'ambiente Python che il tuo client MCP utilizzerà:

```bash
pip install co-op-translator
```

Per lo sviluppo locale da questo repository, installa il pacchetto in modalità editable:

```bash
pip install -e .
```

Scegli la modalità di traduzione che il tuo client MCP utilizzerà:

| Modalità | Usalo per | Credenziali |
| --- | --- | --- |
| Basata su provider | Co-op Translator chiama `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, o `run_translation`. | La traduzione di Markdown e notebook richiede Azure OpenAI o OpenAI. La traduzione delle immagini richiede anche Azure AI Vision. |
| Assistita da agente | L'agente host MCP traduce i chunk restituiti da `start_markdown_agent_translation` o `start_notebook_agent_translation`. | Non sono richieste credenziali provider LLM di Co-op Translator per i chunk di Markdown o notebook. La traduzione delle immagini non è ancora coperta dalla modalità assistita da agente. |

Se inizi con la traduzione di Markdown o notebook all'interno di un agente come Codex o Claude Code, inizia con la modalità assistita da agente. Usa la modalità basata su provider quando vuoi che sia Co-op Translator a chiamare i provider configurati, quando stai traducendo immagini, o quando esegui una traduzione a livello di repository come la CLI.

Configura le credenziali del provider solo per i flussi di lavoro basati su provider:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

La traduzione di immagini basata su provider necessita inoltre di:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    La modalità assistita da agente copre attualmente Markdown e le celle Markdown dei notebook. La traduzione delle immagini utilizza ancora la pipeline di immagini basata su provider e richiede Azure AI Vision per OCR e rendering consapevole del layout.

## Passo 2: Configura il tuo client MCP

Per la normale configurazione `stdio` locale, aggiungi Co-op Translator alla configurazione del tuo client MCP. Il client avvierà e fermerà il processo automaticamente.

Configurazione pacchetto installato:

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

Configurazione del checkout sorgente su Windows:

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

Configurazione del checkout sorgente su macOS o Linux:

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

Dopo aver modificato la configurazione del client MCP, riavvia o ricarica il client in modo che possa rilevare il nuovo server.

## Passo 3: Verifica il server nel client

Chiedi al client MCP di elencare gli strumenti disponibili, oppure chiama prima uno degli helper in sola lettura:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Controlli utili iniziali:

| Strumento | Cosa verificare |
| --- | --- |
| `get_api_overview` | Conferma che il server è raggiungibile e mostra i flussi di lavoro disponibili. |
| `list_supported_languages` | Conferma che i dati linguistici inclusi possono essere caricati. |
| `get_configuration_status` | Conferma la disponibilità dei provider LLM e Vision senza esporre valori segreti. |

## Passo 4: Scegli un flusso di lavoro

### Traduci singoli file o documenti

Usa gli strumenti di contenuto basati su provider quando il client MCP ha già il contenuto del documento o un percorso immagine e Co-op Translator dovrebbe chiamare i provider di traduzione configurati.

Per Markdown:

1. Chiama `translate_markdown_content` con `document`, `language_code`, e opzionalmente `source_path`.
2. Se il risultato tradotto sarà scritto in un layout di output di Co-op Translator, chiama `rewrite_markdown_paths`.
3. Lascia che il client scriva o restituisca il `content` finale.

Per i notebook:

1. Chiama `translate_notebook_content` con il JSON del notebook e `language_code`.
2. Chiama `rewrite_notebook_paths` se i link del notebook tradotto devono essere adattati per un percorso di destinazione.
3. Scrivi o restituisci il JSON finale del notebook.

Per le immagini:

1. Chiama `translate_image_content` con `image_path`, `language_code`, e opzionali `root_dir` o `fast_mode`.
2. Leggi il `data_base64` e il `mime_type` restituiti.
3. Se `output_path` è fornito, l'immagine tradotta viene salvata anche in quel percorso.

Gli strumenti di contenuto non eseguono la scoperta del progetto, aggiornamenti dei metadati, disclaimer o riscrittura automatica dei percorsi. Se vuoi che l'agente host traduca i chunk di Markdown o notebook senza credenziali provider LLM di Co-op Translator, usa il flusso di lavoro assistito da agente qui sotto.

### Traduci con il modello host dell'agente

Usa gli strumenti assistiti da agente quando vuoi che l'agente host MCP, come un assistente di coding, produca il testo tradotto invece di configurare Azure OpenAI o OpenAI per Co-op Translator.

In un client MCP basato su chat, normalmente non è necessario scrivere tu stesso il JSON degli strumenti. Chiedi all'agente di usare il flusso di lavoro assistito da agente:

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

Se il tuo client MCP supporta prompt del server, usa `agent_assisted_markdown_translation_prompt` per far caricare al client le medesime istruzioni del flusso di lavoro.

Per Markdown:

1. Chiama `start_markdown_agent_translation` con `document`, `language_code`, e opzionalmente `source_path`.
2. Traduci ogni chunk restituito nell'agente host seguendo il `prompt` del chunk.
3. Chiama `finish_markdown_agent_translation` con il `job` originale e i chunk tradotti usando `chunk_id` e `translated_text`.
4. Se il contenuto sarà scritto in un percorso di destinazione tradotto, chiama `rewrite_markdown_paths`.

Per i notebook:

1. Chiama `start_notebook_agent_translation` con il JSON del notebook e `language_code`.
2. Traduci ogni chunk restituito nell'agente host.
3. Chiama `finish_notebook_agent_translation` con il `job` originale e i chunk tradotti.
4. Chiama `rewrite_notebook_paths` se i link dei notebook tradotti necessitano di adeguamento al percorso di destinazione.

Gli strumenti assistiti dall'agente non chiamano Azure OpenAI o OpenAI da Co-op Translator. L'agente host è responsabile della traduzione dei chunk restituiti. Co-op Translator gestisce il chunking del Markdown, la conservazione dei segnaposto, la ricostruzione del frontmatter, la sostituzione delle celle del notebook e la normalizzazione post-traduzione.

### Tradurre un intero repository

Usa `run_translation` quando l'utente vuole che Co-op Translator si comporti come la CLI `translate`.

La traduzione del repository è impostata di default su `dry_run=true` in modo che un agente possa ispezionare l'ambito prima delle modifiche ai file:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Per consentire le scritture, il chiamante deve impostare sia `dry_run=false` sia `confirm_write=true`:

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
    MCP espone l'API beta `run_review`. È sicura per flussi di lavoro di revisione in sola lettura, ma i controlli di revisione e gli schemi di issue potrebbero evolvere.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Il risultato include l'output di testo catturato e un riepilogo strutturato della revisione quando disponibile.

## Esecuzioni manuali del server

Le esecuzioni manuali servono principalmente per il debug o per trasporti che si comportano come server a lunga durata.

Debug del server stdio predefinito:

```bash
co-op-translator-mcp
```

Esegui da un checkout sorgente:

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
| `translate_markdown_content` | Tradurre una stringa Markdown. | No |
| `translate_notebook_content` | Tradurre le celle Markdown nel JSON del notebook. | No |
| `translate_image_content` | Tradurre il testo in un'immagine e restituire dati immagine base64. | Opzionale, solo quando `output_path` è fornito |
| `start_markdown_agent_translation` | Preparare chunk di Markdown affinché l'agente host li traduca senza credenziali LLM di Co-op Translator. | No |
| `finish_markdown_agent_translation` | Ricostruire il Markdown dai chunk tradotti dall'agente host. | No |
| `start_notebook_agent_translation` | Preparare chunk di celle Markdown del notebook affinché l'agente host li traduca. | No |
| `finish_notebook_agent_translation` | Ricostruire il JSON del notebook dai chunk tradotti dall'agente host. | No |
| `rewrite_markdown_paths` | Riscrivere i percorsi nel corpo Markdown e nel frontmatter per una destinazione tradotta. | No |
| `rewrite_notebook_paths` | Riscrivere i percorsi all'interno delle celle Markdown del notebook. | No |
| `run_translation` | Eseguire la traduzione a livello di progetto come la CLI. | Sì quando `dry_run=false` e `confirm_write=true` |
| `translate_project` | Alias di compatibilità per `run_translation`. | Sì quando `dry_run=false` e `confirm_write=true` |
| `run_review` | Eseguire controlli di revisione deterministici. | No |
| `get_configuration_status` | Segnalare i provider LLM e Vision configurati senza esporre segreti. | No |
| `list_supported_languages` | Elencare i codici lingua target supportati. | No |
| `get_api_overview` | Descrivere i flussi di lavoro e gli strumenti MCP disponibili. | No |

## Risorse

| Resource URI | Scopo |
| --- | --- |
| `co-op://api` | Panoramica JSON dei flussi di lavoro e degli strumenti. |
| `co-op://supported-languages` | Elenco JSON dei codici lingua supportati. |
| `co-op://configuration` | Riepilogo JSON della disponibilità dei provider senza segreti. |

## Prompt

| Prompt | Scopo |
| --- | --- |
| `translate_markdown_document_prompt` | Guidare un client MCP attraverso la traduzione del contenuto più la riscrittura opzionale dei percorsi. |
| `agent_assisted_markdown_translation_prompt` | Guidare un client MCP attraverso la traduzione Markdown con agente host senza credenziali provider LLM di Co-op Translator. |
| `translate_repository_prompt` | Guidare un client MCP attraverso la traduzione del repository iniziando con dry-run. |

## Esempi copia-incolla

Tradurre contenuto Markdown:

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

Riscrivere i link del Markdown tradotto:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

Tradurre Markdown con il modello host dell'agente:

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

Dopo che l'agente host ha tradotto ogni chunk restituito, completa il job con l'oggetto `job` completo restituito da `start_markdown_agent_translation`:

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
| Il client MCP non riesce a trovare `co-op-translator-mcp`. | Usa il percorso assoluto dell'eseguibile Python e la configurazione di checkout sorgente `["-m", "co_op_translator.mcp.server"]`. |
| Il server è elencato ma la traduzione fallisce. | Chiama `get_configuration_status` e conferma che è disponibile un provider LLM. |
| Vuoi la traduzione di Markdown o notebook senza chiavi Azure OpenAI/OpenAI. | Usa `start_markdown_agent_translation` / `finish_markdown_agent_translation` o gli equivalenti per notebook in modo che l'agente host traduca i chunk. |
| La traduzione delle immagini fallisce. | Conferma che le variabili Azure AI Vision sono impostate e chiama `get_configuration_status`. |
| La traduzione del repository non scrive i file. | Imposta `dry_run=false` e `confirm_write=true` solo dopo l'approvazione esplicita dell'utente. |
| Le modifiche alla configurazione del client non appaiono. | Riavvia o ricarica il client MCP. |

## Note di sicurezza

- Le chiamate agli strumenti MCP sono controllate dal modello dall'applicazione host, quindi la traduzione del repository è di default in dry-run.
- La traduzione completa del repository può creare, aggiornare o rimuovere molti file. Richiedi l'approvazione esplicita dell'utente prima di impostare `confirm_write=true`.
- Lo strumento di stato della configurazione non restituisce mai API key, endpoint o altri valori segreti.
- La traduzione delle immagini restituisce dati immagine base64. Immagini di grandi dimensioni possono produrre risposte strumento di grandi dimensioni.
- Gli strumenti assistiti dall'agente restituiscono chunk di origine e prompt all'agente host MCP. Usali solo con contenuti che l'utente è a suo agio a inviare a quel modello agente host.