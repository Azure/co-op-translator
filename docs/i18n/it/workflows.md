# Scegli il tuo flusso di lavoro

Co-op Translator può essere usato in tre modi: la CLI, l'API Python e il server MCP. Condividono le stesse capacità di traduzione, ma ciascuno si adatta a un flusso di lavoro diverso.

Usa questa pagina quando devi decidere da dove iniziare.

**Se modifichi le traduzioni a mano:** i flussi di lavoro predefiniti CLI e Actions ritradurranno completamente i file sorgente modificati, quindi la tua formulazione in quei file potrebbe essere sovrascritta. Controlla il diff prima di accettare una modifica. Per la preservazione a livello di blocco Markdown delle modifiche accettate, usa l'opzionale [fornitore di stato di traduzione per l'API Python](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Decisione rapida

| Se vuoi... | Usa | Inizia qui |
| --- | --- | --- |
| Tradurre o revisionare un repository da un terminale | CLI | [Riferimento CLI](cli.md) |
| Aggiungere la traduzione a uno script Python, servizio, notebook o lavoro CI | API Python | [API Python](api.md) |
| Permetti a un agente, editor o client compatibile MCP di tradurre contenuti per te | MCP Server | [Server MCP](mcp.md) |
| Tradurre un documento Markdown, notebook o immagine che la tua app ha già caricato | API Python o MCP Server | [API Python](api.md) o [Server MCP](mcp.md) |
| Tradurre un intero repository con cartelle di output standard e metadata | CLI o `run_translation` | [Riferimento CLI](cli.md) o [API Python](api.md) |

## Usa la CLI quando

Scegli la CLI quando una persona o un lavoro CI avvia la traduzione del repository da una shell.

La CLI è il percorso più diretto quando vuoi che Co-op Translator scopra i file del progetto, crei output tradotti, preservi la struttura del progetto, aggiorni i metadata ed esegua comandi di revisione.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Questo esempio traduce Markdown e notebook. Aggiungi `-img` solo dopo aver configurato [Azure AI Vision](configuration.md#azure-ai-vision). Per una prima esecuzione solo Markdown, segui [La tua prima traduzione](first-translation.md).

Adatti:

- Stai traducendo un repository dal tuo terminale.
- Vuoi un comando ripetibile per i flussi di lavoro CI o di rilascio.
- Vuoi scoperta del progetto integrata, percorsi di output, metadata, pulizia e revisione.
- Preferisci un'interfaccia a comandi piuttosto che scrivere codice Python.

## Usa l'API Python quando

Scegli l'API Python quando il tuo codice deve controllare il flusso di lavoro.

L'API è utile per applicazioni, script di automazione, notebook, servizi e pipeline personalizzate. Ti permette di chiamare API di traduzione dei contenuti a basso livello per file individuali, o eseguire la stessa orchestrazione a livello di repository usata dalla CLI.

Traduci un documento Markdown e decidi dove salvarlo:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Esegui la traduzione di un repository da Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

Adatti:

- La tua applicazione già legge file, buffer, notebook o byte di immagini.
- Hai bisogno di validazione personalizzata, archiviazione, logging, retry o flussi di approvazione.
- Vuoi tradurre un documento, notebook o immagine senza processare un intero repository.
- Vuoi la traduzione del repository, ma tramite automazione Python invece che con un comando shell.

## Usa il Server MCP quando

Scegli il server MCP quando un agente, un editor o un client compatibile MCP dovrebbe chiamare gli strumenti di Co-op Translator.

Nella normale configurazione locale, l'utente non mantiene manualmente un server in esecuzione. Il client MCP avvia `co-op-translator-mcp` su `stdio` quando ha bisogno degli strumenti.

Esempi di richieste utente che un agente potrebbe gestire:

- "Traduci questo file Markdown in coreano e mantieni i link corretti."
- "Traduci questo file Markdown in coreano con il flusso di lavoro MCP assistito dall'agente, usando il tuo modello per i blocchi tradotti."
- "Traduci questo notebook in coreano, preserva le celle di codice e usa Co-op Translator MCP per ricostruire il notebook."
- "Traduci il testo in questa immagine in giapponese e salva il risultato."
- "Esegui una simulazione (dry-run) di una traduzione del repository in spagnolo e dimmi cosa cambierebbe."
- "Verifica se l'output della traduzione in coreano è aggiornato."

Per Markdown e notebook, MCP può lavorare in due modalità:

| Modalità | Usa quando | Principali strumenti |
| --- | --- | --- |
| Assistito dall'agente | L'agente host MCP dovrebbe tradurre i frammenti con il proprio modello, senza le credenziali del provider LLM di Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Supportato dal provider | Co-op Translator dovrebbe chiamare direttamente Azure OpenAI, OpenAI o Anthropic. | `translate_markdown_content`, `translate_notebook_content` |

Forma della chiamata dello strumento Markdown supportato dal provider MCP:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

MCP image tool call shape:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

La traduzione del repository è per impostazione predefinita in dry-run tramite MCP:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

Adatti:

- Vuoi flussi di lavoro di traduzione in linguaggio naturale all'interno di un agente o editor.
- Vuoi la traduzione di Markdown o notebook in cui il modello agente host traduce i frammenti preparati.
- Vuoi che l'agente traduca contenuti selezionati invece di un intero repository.
- Vuoi un passaggio di approvazione prima delle scritture a livello di repository.
- Vuoi un'unica interfaccia che esponga strumenti per Markdown, notebook, immagini, revisione e riscrittura dei percorsi.

## Come si integrano

La CLI è l'opzione predefinita migliore per gli esseri umani che traducono repository. L'API Python è la migliore quando il tuo codice gestisce il flusso di lavoro. Il server MCP è il migliore quando un agente o un editor gestisce il flusso di lavoro.

Tutti e tre i percorsi utilizzano la stessa API pubblica di Co-op Translator, quindi puoi iniziare con la CLI, automatizzare con Python in seguito e esporre le stesse capacità ai client MCP quando hai bisogno di flussi di lavoro guidati da agenti.