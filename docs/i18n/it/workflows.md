# Scegli il tuo flusso di lavoro

Co-op Translator può essere usato in tre modi: la CLI, l'API Python e il server MCP. Condividono le stesse capacità di traduzione, ma ciascuno si adatta a un flusso di lavoro diverso.

Usa questa pagina quando devi decidere da dove iniziare.

## Decisione rapida

| Se vuoi... | Usa | Inizia qui |
| --- | --- | --- |
| Tradurre o revisionare un repository da un terminale | CLI | [Riferimento CLI](cli.md) |
| Aggiungere la traduzione a uno script Python, a un servizio, a un notebook o a un lavoro CI | API Python | [API Python](api.md) |
| Lasciare che un agente, un editor o un client compatibile MCP traducano contenuti per te | Server MCP | [Server MCP](mcp.md) |
| Tradurre un singolo documento Markdown, notebook o immagine che la tua app ha già caricato | API Python o Server MCP | [API Python](api.md) o [Server MCP](mcp.md) |
| Tradurre un intero repository con cartelle di output standard e metadati | CLI o `run_translation` | [Riferimento CLI](cli.md) o [API Python](api.md) |

## Usa la CLI quando

Scegli la CLI quando una persona o un job CI esegue la traduzione del repository da una shell.

La CLI è il percorso più diretto quando vuoi che Co-op Translator scopra i file del progetto, crei output tradotti, preservi la struttura del progetto, aggiorni i metadati ed esegua comandi di revisione.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Situazioni adatte:

- Stai traducendo un repository dal tuo terminale.
- Vuoi un comando ripetibile per i flussi di lavoro CI o di rilascio.
- Vuoi funzionalità integrate per l'individuazione dei file del progetto, percorsi di output, metadati, pulizia e revisione.
- Preferisci un'interfaccia a comandi piuttosto che scrivere codice Python.

## Usa l'API Python quando

Scegli l'API Python quando il tuo codice deve controllare il flusso di lavoro.

L'API è utile per applicazioni, script di automazione, notebook, servizi e pipeline personalizzate. Ti permette di chiamare API di traduzione del contenuto di basso livello per singoli file, o eseguire la stessa orchestrazione a livello di repository usata dalla CLI.

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
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

Situazioni adatte:

- La tua applicazione già legge file, buffer, notebook o byte di immagini.
- Hai bisogno di validazione personalizzata, storage, logging, ritentativi o flussi di approvazione.
- Vuoi tradurre un singolo documento, notebook o immagine senza elaborare un intero repository.
- Vuoi la traduzione del repository, ma tramite automazione Python invece che tramite comando shell.

## Usa il server MCP quando

Scegli il server MCP quando un agente, un editor o un client compatibile MCP devono chiamare gli strumenti di Co-op Translator.

Nella configurazione locale normale, l'utente non mantiene manualmente un server in esecuzione. Il client MCP avvia `co-op-translator-mcp` su `stdio` quando ha bisogno degli strumenti.

Esempi di richieste utente che un agente potrebbe gestire:

- "Traduci questo file Markdown in coreano e mantieni i collegamenti corretti."
- "Traduci questo file Markdown in coreano con il flusso di lavoro MCP assistito da agente, usando il tuo modello per i blocchi tradotti."
- "Traduci questo notebook in coreano, preserva le celle di codice e usa Co-op Translator MCP per ricostruire il notebook."
- "Traduci il testo in questa immagine in giapponese e salva il risultato."
- "Esegui una simulazione (dry-run) della traduzione di un repository in spagnolo e dimmi cosa cambierebbe."
- "Verifica se l'output della traduzione in coreano è aggiornato."

Per Markdown e notebook, MCP può funzionare in due modalità:

| Modalità | Usalo quando | Strumenti principali |
| --- | --- | --- |
| Assistito dall'agente | L'agente host MCP dovrebbe tradurre i blocchi con il proprio modello, senza le credenziali del provider LLM di Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Basato su provider | Co-op Translator dovrebbe chiamare Azure OpenAI o OpenAI direttamente. | `translate_markdown_content`, `translate_notebook_content` |

Forma della chiamata dello strumento Markdown supportata dal provider MCP:

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

Forma della chiamata dello strumento immagine MCP:

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

La traduzione del repository viene eseguita in modalità simulazione (dry-run) per impostazione predefinita tramite MCP:

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

Situazioni adatte:

- Vuoi flussi di lavoro di traduzione in linguaggio naturale all'interno di un agente o di un editor.
- Vuoi la traduzione di Markdown o notebook in cui il modello dell'agente host traduce i blocchi preparati.
- Vuoi che l'agente traduca contenuti selezionati invece dell'intero repository.
- Vuoi un passaggio di approvazione prima delle scritture a livello di repository.
- Vuoi un'unica interfaccia che esponga strumenti per Markdown, notebook, immagini, revisione e riscrittura dei percorsi.

## Come si integrano

La CLI è la scelta predefinita migliore per le persone che traducono repository. L'API Python è la migliore quando il tuo codice controlla il flusso di lavoro. Il server MCP è la migliore quando un agente o un editor controllano il flusso di lavoro.

Tutti e tre i percorsi usano la stessa API pubblica di Co-op Translator, quindi puoi iniziare con la CLI, automatizzare con Python successivamente ed esporre le stesse funzionalità ai client MCP quando hai bisogno di flussi di lavoro guidati da agenti.