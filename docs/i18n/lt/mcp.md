# MCP serveris

Co-op Translator įtraukia Model Context Protocol serverį agentams, redaktoriams ir MCP suderinamiems klientams.

Dėl numatyto vietinio nustatymo vartotojams nereikia rankiniu būdu paleisti atskiro serverio. Jie sukonfigūruoja savo MCP klientą, ir klientas automatiškai paleidžia `co-op-translator-mcp` per `stdio`, kai jam reikalingi Co-op Translator įrankiai.

Jei renkatės tarp CLI, Python API ir MCP, pradėkite nuo [Pasirinkite savo darbo eigą](workflows.md).

Naudokite MCP, kai agentas arba redaktorius turėtų tiesiogiai kviesti Co-op Translator:

| Vartotojo tikslas | MCP įrankiai |
| --- | --- |
| Išversti vieną Markdown dokumentą, užrašų knygelę arba vaizdą | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Išversti Markdown arba užrašų knygelės turinį naudojant pagrindinio agento modelį | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Perrašyti išverstus Markdown arba užrašų knygelės nuorodas po išvesties kelio pasirinkimo | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Išversti visą saugyklą kaip CLI | `run_translation`, `translate_project` |
| Peržiūrėti išverstą išvestį be LLM kredencialų | `run_review` |
| Patikrinti galimybes ir aplinkos būseną | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP serveris apgaubia tą pačią viešą Python API, aprašytą [Python API](api.md). Teikėjo palaikomi įrankiai naudoja tuos pačius sukonfigūruotus teikėjus kaip CLI ir Python API. Agentų palaikomi įrankiai paruošia fragmentus, kuriuos MCP host agentas išverčia, o tada Co-op Translator rekonstruoja galutinį Markdown arba notebook.

## Žingsnis 1: Įdiekite ir sukonfigūruokite Co-op Translator

Įdiekite Co-op Translator į Python aplinką, kurios naudos jūsų MCP klientas:

```bash
pip install co-op-translator
```

Vietiniam kūrimui iš šios saugyklos įdiekite paketą redaguojamu režimu:

```bash
pip install -e .
```

Pasirinkite vertimo režimą, kurį naudos jūsų MCP klientas:

| Režimas | Naudojamas | Kredencialai |
| --- | --- | --- |
| Teikėjo pagrįstas | Co-op Translator kviečia `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, arba `run_translation`. | Vertimui reikalingas Azure OpenAI, OpenAI arba Anthropic. Vaizdo vertimui taip pat reikalingas Azure AI Vision. |
| Agentų palaikomas | MCP host agentas išverčia fragmentus, grąžintus `start_markdown_agent_translation` arba `start_notebook_agent_translation`. | Markdown arba notebook fragmentams Co-op Translator LLM teikėjo kredencialai nereikalingi. Vaizdų vertimas kol kas neapima agentų palaikymo režimo. |

Jei pradedate vertimą iš Markdown arba notebook viduje agento, pvz., Codex arba Claude Code, pradėkite nuo agentų palaikymo režimo. Naudokite teikėjo palaikomą režimą, kai norite, kad pats Co-op Translator kreiptųsi į sukonfigūruotus teikėjus, kai verčiate vaizdus, arba kai vykdote saugyklos lygio vertimą kaip CLI.

Sukonfigūruokite vieną teikėją teikėjo palaikomiems darbo eigoms:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Arba OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Arba Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Teikėjo palaikomam vaizdų vertimui papildomai reikalinga:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agentų palaikomas režimas šiuo metu apima Markdown ir notebook Markdown ląsteles. Vaizdų vertimas vis dar naudoja teikėjo palaikomą vaizdų srautą ir reikalauja Azure AI Vision OCR ir išdėstymo palaikančio atvaizdavimo.

## Žingsnis 2: Sukonfigūruokite savo MCP klientą

Dėl įprasto vietinio `stdio` nustatymo pridėkite Co-op Translator į savo MCP kliento konfigūraciją. Klientas automatiškai paleis ir sustabdys procesą.

Įdiegto paketo konfigūracija:

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

Šaltinio kodo konfigūracija Windows:

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

Šaltinio kodo konfigūracija macOS arba Linux:

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

Pakeitus MCP kliento konfigūraciją, paleiskite iš naujo arba perkraukite klientą, kad jis galėtų aptikti naują serverį.

## Žingsnis 3: Patikrinkite serverį kliente

Paprašykite MCP kliento išvardinti galimus įrankius arba pirmiausia iškvieskite vieną iš tik skaitymui skirtų pagalbinių funkcijų:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Naudingi pirmieji patikrinimai:

| Įrankis | Ką patikrinti |
| --- | --- |
| `get_api_overview` | Patvirtina, kad serveris pasiekiamas ir parodo galimas darbo eigas. |
| `list_supported_languages` | Patvirtina, kad supakuoti kalbų duomenys gali būti įkelti. |
| `get_configuration_status` | Patvirtina LLM ir Vision teikėjų prieinamumą neatskleidžiant slaptų reikšmių. |

## Žingsnis 4: Pasirinkite darbo eigą

### Išversti atskirus failus ar dokumentus

Naudokite teikėjo palaikomus turinio įrankius, kai MCP klientas jau turi dokumento turinį arba vaizdo kelią ir Co-op Translator turėtų kreiptis į sukonfigūruotus vertimo teikėjus.

Markdown atveju:

1. Iškvieskite `translate_markdown_content` su `document`, `language_code` ir neprivalomu `source_path`.
2. Jei išverstas rezultatas bus įrašytas į Co-op Translator išvesties išdėstymą, iškvieskite `rewrite_markdown_paths`.
3. Leiskite klientui įrašyti arba grąžinti galutinį `content`.

Užrašų knygelėms:

1. Iškvieskite `translate_notebook_content` su notebook JSON ir `language_code`.
2. Iškvieskite `rewrite_notebook_paths`, jei išverstų notebook nuorodų reikia pakeisti pagal tikslinį kelią.
3. Įrašykite arba grąžinkite galutinį notebook JSON.

Vaizdams:

1. Iškvieskite `translate_image_content` su `image_path`, `language_code` ir neprivalomu `root_dir` arba `fast_mode`.
2. Perskaitykite grąžintus `data_base64` ir `mime_type`.
3. Jei pateiktas `output_path`, išverstas vaizdas taip pat bus išsaugotas tame kelyje.

Turinio įrankiai neatlieka projekto aptikimo, metaduomenų atnaujinimų, atsakomybės apribojimų ar automatinio kelių perrašymo. Jei norite, kad host agentas išverstų Markdown arba notebook fragmentus be Co-op Translator LLM teikėjo kredencialų, naudokite žemiau pateiktą agentų palaikomą darbo eigą.

### Vertimas su host agent modeliu

Naudokite agentų palaikomus įrankius, kai norite, kad MCP host agentas, pvz., kodo asistentas, sukurtų išverstą tekstą vietoje to, kad sukonfigūruotumėte LLM teikėją Co-op Translator.

Pokalbių pagrindu veikiančiame MCP kliente paprastai nereikia rašyti įrankio JSON patiems. Paprašykite agento naudoti agentų palaikomą darbo eigą:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Užrašų knygelėms naudokite tą patį modelį:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Jei jūsų MCP klientas palaiko serverio užklausas, naudokite `agent_assisted_markdown_translation_prompt`, kad klientas įkeltų tą pačią darbo eigos instrukciją.

Markdown atveju:

1. Iškvieskite `start_markdown_agent_translation` su `document`, `language_code` ir neprivalomu `source_path`.
2. Išverskite kiekvieną grąžintą fragmentą host agente, sekdami fragmento `prompt`.
3. Iškvieskite `finish_markdown_agent_translation` su originaliu `job` ir išverstais fragmentais, nurodydami `chunk_id` ir `translated_text`.
4. Jei turinys bus įrašytas į išverstą tikslinį kelią, iškvieskite `rewrite_markdown_paths`.

Užrašų knygelėms:

1. Iškvieskite `start_notebook_agent_translation` su notebook JSON ir `language_code`.
2. Išverskite kiekvieną grąžintą fragmentą host agente.
3. Iškvieskite `finish_notebook_agent_translation` su originaliu `job` ir išvertais fragmentais.
4. Iškvieskite `rewrite_notebook_paths`, jei išverstų notebook nuorodų reikia pritaikyti tiksliniam keliui.

Agentų palaikomi įrankiai nekviečia sukonfigūruoto LLM teikėjo per Co-op Translator. Host agentas yra atsakingas už grąžintų fragmentų vertimą. Co-op Translator rūpinasi Markdown suskaidymu į fragmentus, vietos rezervavimo ženklų išsaugojimu, frontmatter atkūrimu, notebook ląstelių pakeitimu ir vertimo po apdorojimo normalizavimu.

### Išversti visą saugyklą

Naudokite `run_translation`, kai vartotojas nori, kad Co-op Translator elgtųsi kaip `translate` CLI.

Saugyklos vertimas pagal nutylėjimą naudoja `dry_run=true`, kad agentas galėtų peržiūrėti apimtį prieš failų pakeitimus:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

`run_translation` rezultatas apima `events` masyvą su verzijuotais
`co-op.translation.event.v1` progreso įvykiais. MCP klientai turėtų naudoti laukus tokius
kaip `type`, `stage_key`, `completed`, `total`, ir `current_path` vietoj
nagrinėjimo užfiksuoto konsolės teksto. Nurodykite `json_events_path`, kad taip pat įrašytumėte tuos įvykius
į NDJSON failą.

Norint leisti įrašymus, kvietėjas turi nustatyti tiek `dry_run=false`, tiek `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` yra pateiktas kaip suderinamumo aliasas `run_translation`.

### Peržiūrėti išverstą išvestį

Naudokite `run_review` deterministiniams patikrinimams, kuriems nereikia LLM ar Vision kredencialų:

!!! note "Beta"
    MCP pateikia beta `run_review` API. Jis saugus tik skaitymui skirtoms peržiūros darbo eigoms, tačiau peržiūros patikrinimai ir problemų schemos gali keistis.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Rezultatas apima užfiksuotą tekstinę išvestį ir struktūrizuotą peržiūros santrauką, kai ji prieinama.

## Rankiniai serverio paleidimai

Rankiniai paleidimai dažniausiai skirti derinimui arba transportams, kurie elgiasi kaip ilgai veikiantys serveriai.

Derinkite numatytąjį stdio serverį:

```bash
co-op-translator-mcp
```

Paleisti iš šaltinio kopijos:

```bash
python -m co_op_translator.mcp.server
```

Paleisti ilgai veikiančią HTTP arba SSE serverį:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Vietinėms redaktoriaus ir agento integracijoms pirmenybę teikite kliento valdomai `stdio` konfigūracijai Žingsnyje 2.

## Įrankiai

| Įrankis | Paskirtis | Rašo failus |
| --- | --- | --- |
| `translate_markdown_content` | Išversti Markdown eilutę. | Ne |
| `translate_notebook_content` | Išversti Markdown ląsteles notebook JSON. | Ne |
| `translate_image_content` | Išversti tekstą viename vaizde ir grąžinti base64 vaizdo duomenis. | Pasirenkama, tik kai pateiktas `output_path` |
| `start_markdown_agent_translation` | Paruošti Markdown fragmentus, kad host agentas galėtų juos išversti be Co-op Translator LLM kredencialų. | Ne |
| `finish_markdown_agent_translation` | Rekonstruoti Markdown iš host agente išverstų fragmentų. | Ne |
| `start_notebook_agent_translation` | Paruošti notebook Markdown ląstelių fragmentus, kuriuos host agentas išvers. | Ne |
| `finish_notebook_agent_translation` | Rekonstruoti notebook JSON iš host agente išverstų fragmentų. | Ne |
| `rewrite_markdown_paths` | Perrašyti Markdown turinį ir frontmatter kelius skirtam išvesties keliui. | Ne |
| `rewrite_notebook_paths` | Perrašyti kelius notebook Markdown ląstelėse. | Ne |
| `run_translation` | Vykdyti projekto lygio vertimą kaip CLI. | Taip, kai `dry_run=false` ir `confirm_write=true` |
| `translate_project` | Suderinamumo aliasas `run_translation`. | Taip, kai `dry_run=false` ir `confirm_write=true` |
| `run_review` | Vykdyti deterministinius peržiūros patikrinimus. | Ne |
| `get_configuration_status` | Pranešti apie sukonfigūruotus LLM ir Vision teikėjus neatskleidžiant slaptų duomenų. | Ne |
| `list_supported_languages` | Išvardinti palaikomų tikslinių kalbų kodus. | Ne |
| `get_api_overview` | Apibūdinti galimas MCP darbo eigas ir įrankius. | Ne |

## Resursai

| Resurso URI | Paskirtis |
| --- | --- |
| `co-op://api` | JSON apžvalga apie darbo eigas ir įrankius. |
| `co-op://supported-languages` | JSON sąrašas palaikomų kalbų kodų. |
| `co-op://configuration` | JSON teikėjų prieinamumo santrauka be slaptų duomenų. |

## Promptai

| Prompt | Paskirtis |
| --- | --- |
| `translate_markdown_document_prompt` | Nurodo MCP klientui turinio vertimo eigą bei neprivalomą kelių perrašymą. |
| `agent_assisted_markdown_translation_prompt` | Nurodo MCP klientui host-agento Markdown vertimo eigą be Co-op Translator LLM teikėjo kredencialų. |
| `translate_repository_prompt` | Nurodo MCP klientui saugyklos vertimą, pradedant peržiūra (dry-run). |

## Kopijuoti-ir-įklijuoti pavyzdžiai

Išversti Markdown turinį:

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

Perrašyti išverstų Markdown nuorodas:

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

Išversti Markdown su host agent modeliu:

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

Kai host agentas išvers kiekvieną grąžintą fragmentą, užbaikite darbą naudodami pilną `job` objektą, kurį grąžino `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Peržiūrėti saugyklos vertimą:

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

## Trikčių šalinimas

| Problema | Ką išbandyti |
| --- | --- |
| MCP klientas negali rasti `co-op-translator-mcp`. | Naudokite absoliutų Python vykdomojo failo kelią ir `["-m", "co_op_translator.mcp.server"]` šaltinio checkout konfigūraciją. |
| Serveris yra išvardintas, bet vertimas nepavyksta. | Iškvieskite `get_configuration_status` ir patikrinkite, ar yra prieinamas LLM teikėjas. |
| Norite Markdown arba notebook vertimo be teikėjo kredencialų. | Naudokite `start_markdown_agent_translation` / `finish_markdown_agent_translation` arba atitinkamus notebook įrankius, kad host agentas išverstų fragmentus. |
| Vaizdų vertimas nepavyksta. | Patikrinkite, ar nustatyti Azure AI Vision kintamieji ir iškvieskite `get_configuration_status`. |
| Saugyklos vertimas neįrašo failų. | Nustatykite `dry_run=false` ir `confirm_write=true` tik gavus aiškų vartotojo patvirtinimą. |
| Kliento konfigūracijos pakeitimai neatsiranda. | Paleiskite arba perkraukite MCP klientą. |

## Saugumo pastabos

- MCP įrankių kvietimai yra valdomi host programos modelio, todėl saugyklos vertimas pagal nutylėjimą yra dry-run.
- Visas saugyklos vertimas gali sukurti, atnaujinti arba pašalinti daug failų. Reikalaukite aiškaus vartotojo patvirtinimo prieš nustatant `confirm_write=true`.
- Konfigūracijos būsenos įrankis niekada negrąžina API raktų, galinių taškų ar kitų slaptų reikšmių.
- Vaizdų vertimas grąžina base64 vaizdo duomenis. Dideli vaizdai gali sukurti didelius įrankių atsakymus.
- Agentų palaikomi įrankiai grąžina šaltinio fragmentus ir prompt'us MCP hostui. Naudokite juos tik su turiniu, kurį vartotojas yra pasirengęs siųsti tam host agent modeliui.