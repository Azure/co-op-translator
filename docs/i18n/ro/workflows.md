# Alegeți fluxul de lucru

Co-op Translator poate fi folosit în trei moduri: CLI, API-ul Python și serverul MCP. Ele împărtășesc aceleași capacități de traducere, dar fiecare se potrivește unui flux de lucru diferit.

Folosiți această pagină când decideți de unde să începeți.

**Dacă editați traducerile manual:** fluxurile implicite CLI și Actions retraduce fișierele sursă modificate în întregime, astfel încât formularea dvs. din acele fișiere poate fi suprascrisă. Revizuiți diff-ul înainte de a accepta o actualizare. Pentru păstrarea la nivel de bloc Markdown a editărilor acceptate, folosiți opționalul [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Decizie rapidă

| Dacă doriți să... | Folosiți | Începeți aici |
| --- | --- | --- |
| Traduceți sau revizuiți un depozit dintr-un terminal | CLI | [Referință CLI](cli.md) |
| Adăugați traducere într-un script Python, serviciu, notebook sau job CI | Python API | [Python API](api.md) |
| Permiteți unui agent, unui editor sau unui client compatibil MCP să traducă conținut pentru dvs. | MCP Server | [MCP Server](mcp.md) |
| Traduceți un document Markdown, un notebook sau o imagine pe care aplicația dvs. le-a încărcat deja | Python API sau MCP Server | [Python API](api.md) sau [MCP Server](mcp.md) |
| Traduceți întregul repository cu foldere standard de ieșire și metadate | CLI sau `run_translation` | [CLI Reference](cli.md) sau [Python API](api.md) |

## Folosiți CLI când

Alegeți CLI atunci când o persoană sau un job CI inițiază traducerea depozitului dintr-un shell.

CLI este calea cea mai directă atunci când doriți ca Co-op Translator să descopere fișierele proiectului, să creeze ieșiri traduse, să păstreze structura proiectului, să actualizeze metadatele și să ruleze comenzi de revizuire.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Acest exemplu traduce Markdown și notebook-uri. Adăugați `-img` doar după ce configurați [Azure AI Vision](configuration.md#azure-ai-vision). Pentru o primă rulare doar cu Markdown, urmați [Prima dvs. traducere](first-translation.md).

Potrivit pentru:

- Traduceți un depozit din terminalul dvs.
- Vreți o comandă repetabilă pentru fluxuri de lucru CI sau lansări.
- Vreți descoperire încorporată a proiectului, căi de ieșire, metadate, curățare și revizuire.
- Preferiți o interfață de comandă în loc să scrieți cod Python.

## Folosiți API-ul Python când

Alegeți API-ul Python atunci când codul dvs. ar trebui să controleze fluxul de lucru.

API-ul este util pentru aplicații, scripturi de automatizare, notebook-uri, servicii și pipeline-uri personalizate. Vă permite să apelați API-uri de traducere a conținutului la nivel scăzut pentru fișiere individuale sau să rulați aceeași orchestrare la nivel de depozit folosită de CLI.

Traduceți un document Markdown și decideți unde să îl salvați:

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

Rulați o traducere a depozitului din Python:

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

Potrivit pentru:

- Aplicația dvs. citește deja fișiere, buffere, notebook-uri sau octeți de imagine.
- Aveți nevoie de validare personalizată, stocare, jurnalizare, reîncercări sau fluxuri de aprobare.
- Doriți să traduceți un document, un notebook sau o imagine fără a procesa întregul depozit.
- Vreți traducerea depozitului, dar din automatizare Python în loc de o comandă shell.

## Folosiți serverul MCP când

Alegeți serverul MCP atunci când un agent, editor sau client compatibil MCP ar trebui să apeleze instrumentele Co-op Translator.

În configurarea locală normală, utilizatorul nu menține manual un server în execuție. Clientul MCP pornește `co-op-translator-mcp` peste `stdio` când are nevoie de instrumente.

Exemple de cereri ale utilizatorului pe care le-ar putea gestiona un agent:

- "Traduceți acest fișier Markdown în coreeană și păstrați linkurile corecte."
- "Traduceți acest fișier Markdown în coreeană cu fluxul de lucru MCP asistat de agent, folosind propriul vostru model pentru segmentele traduse."
- "Traduceți acest notebook în coreeană, păstrați celulele de cod și folosiți Co-op Translator MCP pentru a reconstrui notebook-ul."
- "Traduceți textul din această imagine în japoneză și salvați rezultatul."
- "Efectuați o simulare (dry-run) a unei traduceri de depozit în spaniolă și spuneți-mi ce s-ar schimba."
- "Revizuiți dacă rezultatul traducerii în coreeană este la zi."

Pentru Markdown și notebook-uri, MCP poate funcționa în două moduri:

| Mod | Folosiți când | Principalele instrumente |
| --- | --- | --- |
| Agent-assisted | Agentul gazdă MCP ar trebui să traducă segmentele cu propriul model, fără acreditări ale furnizorului LLM Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator ar trebui să apeleze direct Azure OpenAI, OpenAI, sau Anthropic. | `translate_markdown_content`, `translate_notebook_content` |

Apelul instrumentului Markdown susținut de furnizor MCP:

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

Apelul instrumentului imagine MCP:

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

Traducerea depozitului este în modul de simulare (dry-run) implicit prin MCP:

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

Potrivit pentru:

- Doriți fluxuri de lucru de traducere în limbaj natural în interiorul unui agent sau editor.
- Doriți traducerea Markdown sau a notebook-urilor unde agentul gazdă traduce segmentele pregătite.
- Doriți ca agentul să traducă conținut selectat în locul întregului depozit.
- Doriți un pas de aprobare înainte de scrierile la scară de întreg depozitul.
- Vreți o singură interfață care expune instrumente pentru Markdown, notebook, imagine, revizuire și rescrierea căilor.

## Cum se potrivesc între ele

CLI este cel mai bun implicit pentru persoane care traduc depozite. API-ul Python este cel mai bun când codul dvs. deține fluxul de lucru. Serverul MCP este cel mai bun când un agent sau editor deține fluxul de lucru.

Toate cele trei căi folosesc aceeași API publică Co-op Translator, astfel încât puteți începe cu CLI, automatiza mai târziu cu Python și expune aceleași capacități clienților MCP atunci când aveți nevoie de fluxuri de lucru conduse de agenți.