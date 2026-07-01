# Alegeți fluxul de lucru

Co-op Translator poate fi folosit în trei moduri: CLI, API-ul Python și serverul MCP. Împărtășesc aceleași capabilități de traducere, dar fiecare se potrivește unui flux de lucru diferit.

Folosiți această pagină când decideți de unde să începeți.

## Decizie rapidă

| Dacă doriți să... | Folosiți | Începeți aici |
| --- | --- | --- |
| Traduceți sau revizuiți un depozit dintr-un terminal | CLI | [Referință CLI](cli.md) |
| Adăugați traducere într-un script Python, serviciu, notebook sau job CI | API Python | [API Python](api.md) |
| Permiteți unui agent, editor sau client compatibil MCP să traducă conținutul pentru dvs. | Server MCP | [Server MCP](mcp.md) |
| Traduceți un singur document Markdown, notebook sau o imagine pe care aplicația dvs. deja le-a încărcat | API Python sau Server MCP | [API Python](api.md) or [Server MCP](mcp.md) |
| Traduceți un întreg depozit cu foldere de ieșire standard și metadate | CLI or `run_translation` | [Referință CLI](cli.md) or [API Python](api.md) |

## Folosiți CLI când

Alegeți CLI atunci când o persoană sau un job CI inițiază traducerea unui depozit dintr-un shell.

CLI este calea cea mai directă când doriți ca Co-op Translator să descopere fișierele proiectului, să creeze ieșiri traduse, să păstreze structura proiectului, să actualizeze metadatele și să ruleze comenzi de revizuire.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Se potrivește bine:

- Traduceți un depozit din terminalul dvs.
- Doriți o comandă repetabilă pentru fluxuri CI sau de lansare.
- Doriți descoperire încorporată a proiectului, căi de ieșire, metadate, curățare și revizuire.
- Preferiți o interfață de comandă în loc să scrieți cod Python.

## Folosiți API-ul Python când

Alegeți API-ul Python când propriul dvs. cod ar trebui să controleze fluxul de lucru.

API-ul este util pentru aplicații, scripturi de automatizare, notebook-uri, servicii și pipeline-uri personalizate. Vă permite să apelați API-uri de traducere a conținutului la nivel scăzut pentru fișiere individuale sau să rulați aceeași organizare la nivel de depozit folosită de CLI.

Traduceți un singur document Markdown și decideți unde să îl salvați:

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

Rulați o traducere de depozit din Python:

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

Se potrivește bine:

- Aplicația dvs. deja citește fișiere, buffere, notebook-uri sau octeți de imagine.
- Aveți nevoie de validare personalizată, stocare, jurnalizare, reîncercări sau fluxuri de aprobare.
- Doriți să traduceți un singur document, notebook sau o imagine fără a procesa întregul depozit.
- Doriți traducerea unui depozit, dar din automatizarea Python în locul unei comenzi shell.

## Folosiți serverul MCP când

Alegeți serverul MCP atunci când un agent, editor sau un client compatibil MCP ar trebui să apeleze uneltele Co-op Translator.

În configurația locală normală, utilizatorul nu menține manual un server pornit. Clientul MCP pornește `co-op-translator-mcp` peste `stdio` când are nevoie de unelte.

Exemple de solicitări ale utilizatorului pe care le-ar putea gestiona un agent:

- "Traduceți acest fișier Markdown în coreeană și păstrați linkurile corecte."
- "Traduceți acest fișier Markdown în coreeană cu fluxul de lucru MCP asistat de agent, folosind modelul dvs. pentru fragmentele traduse."
- "Traduceți acest notebook în coreeană, păstrați celulele de cod și folosiți Co-op Translator MCP pentru a reconstrui notebook-ul."
- "Traduceți textul din această imagine în japoneză și salvați rezultatul."
- "Efectuați o simulare a traducerii unui depozit în spaniolă și spuneți-mi ce s-ar schimba."
- "Revizuiți dacă ieșirea traducerii în coreeană este actualizată."

Pentru Markdown și notebook-uri, MCP poate funcționa în două moduri:

| Mod | Folosiți când | Unelte principale |
| --- | --- | --- |
| Asistat de agent | Agentul gazdă MCP ar trebui să traducă fragmentele cu propriul model, fără acreditările providerului LLM ale Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Susținut de provider | Co-op Translator ar trebui să apeleze direct Azure OpenAI sau OpenAI. | `translate_markdown_content`, `translate_notebook_content` |

Forma apelului uneltei Markdown susținută de provider MCP:

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

Forma apelului uneltei pentru imagini MCP:

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

Traducerea depozitului este executată în modul simulare implicit prin MCP:

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

Se potrivește bine:

- Doriți fluxuri de lucru de traducere în limbaj natural în interiorul unui agent sau editor.
- Doriți traducere Markdown sau notebook în care modelul agentului gazdă traduce fragmente pregătite.
- Doriți ca agentul să traducă conținut selectat în locul întregului depozit.
- Doriți un pas de aprobare înainte de scrierile la nivelul întregului depozit.
- Doriți o singură interfață care expune unelte pentru Markdown, notebook, imagini, revizuire și rescrierea căilor.

## Cum se potrivesc împreună

CLI este cea mai bună alegere implicită pentru persoanele care traduc depozite. API-ul Python este cel mai bun când codul dvs. deține fluxul de lucru. Serverul MCP este cel mai bun când un agent sau editor deține fluxul de lucru.

Toate cele trei căi folosesc același API public Co-op Translator, astfel încât puteți începe cu CLI, automatiza mai târziu cu Python și expune aceleași capabilități către clienții MCP când aveți nevoie de fluxuri de lucru conduse de agenți.