# Piliin ang Iyong Daloy ng Trabaho

Maaaring gamitin ang Co-op Translator sa tatlong paraan: ang CLI, ang Python API, at ang MCP server. Pareho ang kanilang kakayahan sa pagsasalin, ngunit ang bawat isa ay angkop sa magkakaibang daloy ng trabaho.

Gamitin ang pahinang ito kapag nagpasiya ka kung saan magsisimula.

**Kung mano-manong ina-edit mo ang mga pagsasalin:** ang default na CLI at Actions workflows ay muling isinasalin nang buo ang mga binagong source file, kaya maaaring mapalitan ang iyong pagkakabuo ng salita sa mga file na iyon. Suriin ang diff bago tanggapin ang update. Para sa pagpapanatili ng Markdown block-level ng mga tinanggap na mga pag-edit, gamitin ang opsyonal na [tagabigay ng estado ng pagsasalin ng Python API](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Mabilis na Desisyon

| Kung nais mong... | Gamitin | Magsimula dito |
| --- | --- | --- |
| Isalin o suriin ang repository mula sa terminal | CLI | [Sanggunian ng CLI](cli.md) |
| Magdagdag ng pagsasalin sa isang Python script, serbisyo, notebook, o CI job | Python API | [Python API](api.md) |
| Hayaan ang isang agent, editor, o MCP-compatible na kliyente na isalin ang nilalaman para sa iyo | MCP Server | [MCP Server](mcp.md) |
| Isalin ang isang Markdown na dokumento, notebook, o imahe na na-load na ng iyong app | Python API o MCP Server | [Python API](api.md) o [MCP Server](mcp.md) |
| Isalin ang buong repository na may karaniwang mga output folder at metadata | CLI o `run_translation` | [CLI Reference](cli.md) o [Python API](api.md) |

## Gamitin ang CLI kapag

Piliin ang CLI kapag isang tao o CI job ang nagpapatakbo ng pagsasalin ng repository mula sa shell.

Ang CLI ang pinaka-direktang paraan kapag nais mong tuklasin ng Co-op Translator ang mga file ng proyekto, lumikha ng mga isinaling output, panatilihin ang layout ng proyekto, i-update ang metadata, at patakbuhin ang mga review na utos.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Isinasalin ng halimbawang ito ang Markdown at mga notebook. Idagdag ang `-img` lamang pagkatapos i-configure ang [Azure AI Vision](configuration.md#azure-ai-vision). Para sa unang pagtakbo na Markdown lamang, sundin ang [Ang iyong unang pagsasalin](first-translation.md).

Mainam para sa:

- Isinasalin mo ang isang repository mula sa iyong terminal.
- Nais mo ng isang ulit-ulit na utos para sa mga workflow ng CI o release.
- Nais mo ng built-in na pagtuklas ng proyekto, mga output path, metadata, paglilinis, at review.
- Mas gusto mo ang isang command interface kaysa pagsusulat ng Python code.

## Gamitin ang Python API kapag

Piliin ang Python API kapag ang iyong sariling code ang dapat kumontrol sa daloy ng trabaho.

Ang API ay kapaki-pakinabang para sa mga aplikasyon, automation script, mga notebook, serbisyo, at pasadyang pipeline. Pinahihintulutan ka nitong tumawag ng mababang-level na content translation APIs para sa indibidwal na mga file, o patakbuhin ang parehong repository-level orchestration na ginagamit ng CLI.

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
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

Mainam para sa:

- Binabasa na ng iyong aplikasyon ang mga file, buffer, notebook, o mga byte ng imahe.
- Kailangan mo ng pasadyang validation, storage, logging, retries, o approval flows.
- Nais mong isalin ang isang dokumento, notebook, o imahe nang hindi pinoproseso ang buong repository.
- Nais mo ng pagsasalin ng repository, ngunit mula sa Python automation sa halip na isang shell command.

## Gamitin ang MCP Server kapag

Piliin ang MCP server kapag isang agent, editor, o MCP-compatible na kliyente ang dapat tumawag sa mga tool ng Co-op Translator.

Sa normal na lokal na setup, hindi mano-manong pinananatiling tumatakbo ng user ang isang server. Sinisimulan ng MCP client ang `co-op-translator-mcp` sa pamamagitan ng `stdio` kapag kailangan nito ang mga tool.

Mga halimbawa ng kahilingan ng user na maaaring hawakan ng agent:

- "Isalin ang Markdown na file na ito sa Koreano at panatilihing tama ang mga link."
- "Isalin ang Markdown na file na ito sa Koreano gamit ang agent-assisted na MCP workflow, gamit ang sarili mong modelo para sa mga isinaling chunks."
- "Isalin ang notebook na ito sa Koreano, panatilihin ang mga code cell, at gamitin ang Co-op Translator MCP para muling buuin ang notebook."
- "Isalin ang teksto sa larawang ito sa Hapones at i-save ang resulta."
- "Gawin ang dry-run ng pagsasalin ng repository sa Espanyol at sabihin sa akin kung ano ang magbabago."
- "Suriin kung napapanahon ang output ng pagsasalin sa Koreano."

Para sa Markdown at mga notebook, maaaring gumana ang MCP sa dalawang mode:

| Mode | Gamitin kapag | Pangunahing mga tool |
| --- | --- | --- |
| May tulong ng agent | Dapat isalin ng host agent ng MCP ang mga chunk gamit ang sarili nitong modelo, nang walang kredensyal ng provider ng LLM ng Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Sinusuportahan ng provider | Dapat tawagan ng Co-op Translator ang Azure OpenAI, OpenAI, o Anthropic nang direkta. | `translate_markdown_content`, `translate_notebook_content` |

Hugis ng tawag ng MCP provider-backed na tool para sa Markdown:

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
- Nais mo ng pagsasalin ng Markdown o notebook kung saan isinasalin ng host agent model ang mga inihandang chunk.
- Nais mong isalin ng agent ang napiling nilalaman sa halip na ang buong repository.
- Nais mo ng hakbang ng pag-apruba bago magsulat sa buong repository.
- Nais mo ng isang interface na naglalantad ng mga tool para sa Markdown, notebook, imahe, pagsusuri, at pag-rewrite ng mga path.

## Paano Sila Nagkakatugma

Ang CLI ang pinakamainam na default para sa mga tao na nagsasalin ng mga repository. Ang Python API ang pinakamainam kapag ang iyong code ang may kontrol sa daloy ng trabaho. Ang MCP server ang pinakamainam kapag ang isang agent o editor ang may kontrol sa daloy ng trabaho.

Nagpapagamit ng parehong pampublikong Co-op Translator API ang tatlong landas, kaya maaari kang magsimula sa CLI, i-automate gamit ang Python sa kalaunan, at ilantad ang parehong mga kakayahan sa mga kliyenteng MCP kapag kailangan mo ng agent-driven na mga workflow.