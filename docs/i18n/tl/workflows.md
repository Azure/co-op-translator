# Piliin ang Iyong Daloy ng Trabaho

Maaaring gamitin ang Co-op Translator sa tatlong paraan: ang CLI, ang Python API, at ang MCP server. Pareho ang kakayahan nila sa pagsasalin, ngunit bawat isa ay nababagay sa ibang daloy ng trabaho.

Gamitin ang pahinang ito kapag nagtatakda ka kung saan magsisimula.

## Mabilis na Desisyon

| Kung gusto mong... | Gamitin | Magsimula dito |
| --- | --- | --- |
| Isalin o suriin ang isang repository mula sa terminal | CLI | [CLI Reference](cli.md) |
| Magdagdag ng pagsasalin sa isang Python script, service, notebook, o CI job | Python API | [Python API](api.md) |
| Hayaan ang isang agent, editor, o MCP-compatible na kliyente na isalin ang nilalaman para sa iyo | MCP Server | [MCP Server](mcp.md) |
| Isalin ang isang Markdown na dokumento, notebook, o imahe na na-load na ng iyong app | Python API o MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Isalin ang buong repository na may mga karaniwang output folder at metadata | CLI o `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## Gamitin ang CLI kapag

Piliin ang CLI kapag ang isang tao o CI job ang nagpapatakbo ng pagsasalin ng repository mula sa shell.

Ang CLI ang pinakamadaling daan kapag gusto mong ang Co-op Translator ang mag-diskubre ng mga file ng proyekto, gumawa ng mga isinaling output, panatilihin ang layout ng proyekto, i-update ang metadata, at magpatakbo ng mga review na command.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Mainam para sa:

- Isinasalin mo ang isang repository mula sa iyong terminal.
- Nais mo ng isang paulit-ulit na command para sa CI o mga release workflow.
- Nais mo ng built-in na pag-diskubre ng proyekto, mga output path, metadata, cleanup, at review.
- Mas gusto mo ang command interface kaysa sa pagsulat ng Python code.

## Gamitin ang Python API kapag

Piliin ang Python API kapag ang sarili mong code ang dapat kumontrol sa daloy ng trabaho.

Kapaki-pakinabang ang API para sa mga aplikasyon, automation scripts, notebook, serbisyo, at custom na pipeline. Pinapayagan ka nitong tumawag ng low-level content translation APIs para sa indibidwal na mga file, o patakbuhin ang parehong repository-level orchestration na ginagamit ng CLI.

Isalin ang isang Markdown na dokumento at magpasya kung saan ito ise-save:

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

Patakbuhin ang pagsasalin ng repository mula sa Python:

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

Mainam para sa:

- Binabasa na ng iyong aplikasyon ang mga file, buffer, notebook, o mga byte ng imahe.
- Kailangan mo ng custom na validation, storage, logging, retries, o approval flows.
- Gusto mong isalin ang isang dokumento, notebook, o imahe nang hindi pinoproseso ang buong repository.
- Gusto mo ng repository translation, ngunit mula sa Python automation sa halip na isang shell command.

## Gamitin ang MCP Server kapag

Piliin ang MCP server kapag ang isang agent, editor, o MCP-compatible na kliyente ang dapat tumawag sa mga tool ng Co-op Translator.

Sa normal na lokal na setup, hindi manu-manong pinananatiling tumatakbo ng user ang isang server. Sinisimulan ng MCP client ang `co-op-translator-mcp` sa ibabaw ng `stdio` kapag kailangan nito ng mga tool.

Mga halimbawa ng kahilingan ng gumagamit na maaaring asikasuhin ng isang agent:

- "Isalin ang Markdown na file na ito sa Koreano at panatilihing tama ang mga link."
- "Isalin ang Markdown na file na ito sa Koreano gamit ang agent-assisted MCP workflow, na gumagamit ng sarili mong modelo para sa mga isinaling bahagi."
- "Isalin ang notebook na ito sa Koreano, panatilihin ang mga code cell, at gamitin ang Co-op Translator MCP para muling buuin ang notebook."
- "Isalin ang teksto sa larawang ito sa Hapon at i-save ang resulta."
- "Gumawa ng dry-run ng pagsasalin ng repository sa Espanyol at sabihin sa akin kung ano ang magbabago."
- "Suriin kung napapanahon ang output ng pagsasalin sa Koreano."

Para sa Markdown at mga notebook, maaaring gumana ang MCP sa dalawang mode:

| Mode | Gamitin kapag | Pangunahing tools |
| --- | --- | --- |
| Agent-assisted | Dapat isalin ng MCP host agent ang mga chunk gamit ang sarili nitong modelo, nang hindi gumagamit ng Co-op Translator LLM provider credentials. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Dapat tawagan ng Co-op Translator ang Azure OpenAI o OpenAI nang direkta. | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-backed Markdown tool call shape:

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

Ang pagsasalin ng repository ay dry-run bilang default sa pamamagitan ng MCP:

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

Mainam para sa:

- Nais mo ng mga workflow ng pagsasalin sa natural na wika sa loob ng isang agent o editor.
- Nais mo ng pagsasalin ng Markdown o notebook kung saan isinasalin ng host agent model ang mga inihandang bahagi.
- Nais mong isalin ng agent ang napiling nilalaman sa halip na ang buong repository.
- Nais mo ng hakbang ng pag-apruba bago ang mga pagsulat sa buong repository.
- Nais mo ng isang interface na nagpapakita ng mga tool para sa Markdown, notebook, imahe, pagsusuri, at pag-rewrite ng path.

## Paano Sila Nagkakaugnay

Ang CLI ang pinakamahusay na default para sa mga taong nagsasalin ng mga repository. Ang Python API ang pinakamahusay kapag ang iyong code ang may kontrol sa daloy ng trabaho. Ang MCP server ang pinakamahusay kapag ang isang agent o editor ang may kontrol sa daloy ng trabaho.

Lahat ng tatlong landas ay gumagamit ng parehong pampublikong Co-op Translator API, kaya maaari kang magsimula sa CLI, mag-automate gamit ang Python mamaya, at ilantad ang parehong mga kakayahan sa MCP clients kapag kailangan mo ng agent-driven workflows.