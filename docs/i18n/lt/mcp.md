# MCP serveris

Co-op Translator turi Model Context Protocol serverį agentams, redaktoriams ir MCP suderinamiems klientams.

Numatytam vietiniam nustatymui vartotojams nereikia atskirai ranka paleisti serverio. Jie sukonfigūruoja savo MCP klientą, ir klientas automatiškai paleidžia `co-op-translator-mcp` per `stdio`, kai reikia Co-op Translator įrankių.

Jei renkatės tarp CLI, Python API ir MCP, pradėkite nuo [Pasirinkite savo darbo eigą](workflows.md).

Naudokite MCP, kai agentas arba redaktorius turėtų tiesiogiai kviesti Co-op Translator:

| Vartotojo tikslas | MCP įrankiai |
| --- | --- |
| Išversti vieną Markdown dokumentą, užrašų knygelę (notebook) arba vaizdą | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Išversti Markdown arba notebook turinį naudojant pagrindinio agento modelį | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Perrašyti išverstų Markdown ar notebook nuorodas pasirinkus išvesties kelią | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Išversti visą saugyklą (repository) panašiai kaip CLI | `run_translation`, `translate_project` |
| Peržiūrėti išverstą turinį be LLM kredencialų | `run_review` |
| Patikrinti galimybes ir aplinkos būseną | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP serveris apgaubia tą pačią viešą Python API, aprašytą [Python API](api.md). Priemonių funkcijos, palaikomos tiekėjo, naudoja tuos pačius sukonfigūruotus tiekėjus kaip ir CLI bei Python API. Agento pagalbos įrankiai paruošia gabalus, kuriuos MCP pagrindinis agentas išverčia, o tada Co-op Translator rekonstruoja galutinį Markdown arba notebook.

## 1 žingsnis: Įdiekite ir sukonfigūruokite Co-op Translator

Įdiekite Co-op Translator į Python aplinką, kurią naudos jūsų MCP klientas:

```bash
pip install co-op-translator
```

Vietiniam vystymui iš šios saugyklos įdiekite paketą redaguojamu režimu:

```bash
pip install -e .
```

Pasirinkite vertimo režimą, kurį naudos jūsų MCP klientas:

| Režimas | Naudoti šiam tikslui | Kredencialai |
| --- | --- | --- |
| Tiekėjo palaikomas | Co-op Translator iškviečia `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` arba `run_translation`. | Markdown ir notebook vertimams reikalingi Azure OpenAI arba OpenAI. Vaizdų vertimui taip pat reikalingas Azure AI Vision. |
| Agento pagalba | MCP pagrindinis agentas išverčia gabalus, kuriuos grąžina `start_markdown_agent_translation` arba `start_notebook_agent_translation`. | Norint versti Markdown arba notebook gabalus, Co-op Translator LLM tiekėjo kredencialai nėra reikalingi. Vaizdų vertimas dar nepalaikomas agento pagalbos režimu. |

Jei pradedate nuo Markdown arba notebook vertimo agento aplinkoje, pavyzdžiui Codex ar Claude Code, pradėkite nuo agento pagalbos režimo. Naudokite tiekėjo palaikomą režimą, kai norite, kad pats Co-op Translator kviestų jūsų sukonfigūruotus tiekėjus, kai verčiate vaizdus arba kai vykdote saugyklos lygio vertimą, panašų į CLI.

Tiekėjo kredencialus konfigūruokite tik tiekėjo palaikymui skirtoms darbo eigoms:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Tiekėjo palaikomam vaizdų vertimui papildomai reikalinga:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## 2 žingsnis: Sukonfigūruokite savo MCP klientą

Paprastam vietiniam `stdio` nustatymui pridėkite Co-op Translator į savo MCP kliento konfigūraciją. Klientas automatiškai paleis ir sustabdys procesą.

Installed package configuration:

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

Source checkout configuration on Windows:

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

Source checkout configuration on macOS or Linux:

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

Po MCP kliento konfigūracijos pakeitimo paleiskite arba įkraukite klientą iš naujo, kad jis galėtų aptikti naują serverį.

## 3 žingsnis: Patikrinkite serverį kliente

Paprašykite MCP kliento išvardinti prieinamus įrankius arba pirmiausia iškvieskite vieną iš tik skaitymui skirtų pagalbininkų:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Naudingi pirmieji patikrinimai:

| Įrankis | Ką patikrinti |
| --- | --- |
| `get_api_overview` | Patvirtina, kad serveris pasiekiamas ir rodo prieinamas darbo eigas. |
| `list_supported_languages` | Patvirtina, kad galima įkelti įtrauktus kalbų duomenis. |
| `get_configuration_status` | Patvirtina LLM ir Vision tiekėjų prieinamumą neatskleidžiant slaptų reikšmių. |

## 4 žingsnis: Pasirinkite darbo eigą

### Išversti atskirus failus ar dokumentus

Naudokite tiekėjo palaikomus turinio įrankius, kai MCP klientas jau turi dokumento turinį arba vaizdo kelią ir Co-op Translator turėtų kviesti sukonfigūruotus vertimo tiekėjus.

Markdown atveju:

1. Iškvieskite `translate_markdown_content` su `document`, `language_code` ir, jei reikia, `source_path`.
2. Jei išverstas rezultatas bus įrašytas į Co-op Translator išvesties maketą, iškvieskite `rewrite_markdown_paths`.
3. Leiskite klientui įrašyti arba grąžinti galutinį `content`.

Notebook atveju:

1. Iškvieskite `translate_notebook_content` su notebook JSON ir `language_code`.
2. Iškvieskite `rewrite_notebook_paths`, jei reikia pakoreguoti išverstų notebook nuorodas pagal tikslinį kelią.
3. Įrašykite arba grąžinkite galutinį notebook JSON.

Vaizdų atveju:

1. Iškvieskite `translate_image_content` su `image_path`, `language_code` ir neprivalomu `root_dir` arba `fast_mode`.
2. Perskaitykite grąžintus `data_base64` ir `mime_type`.
3. Jei pateiktas `output_path`, išverstas vaizdas taip pat įrašomas į tą kelią.

Turinio įrankiai neatlieka projekto aptikimo, metaduomenų atnaujinimų, įspėjimų ar automatinio kelių perrašymo. Jei norite, kad pagrindinis agentas išversti Markdown ar notebook gabalus be Co-op Translator LLM tiekėjo kredencialų, naudokite žemiau pateiktą agento pagalbos darbo eigą.

### Vertimas naudojant pagrindinio agento modelį

Naudokite agento pagalbos įrankius, kai norite, kad MCP pagrindinis agentas, pavyzdžiui, kodo asistentas, sugeneruotų išverstą tekstą vietoje to, kad sukonfigūruotumėte Azure OpenAI arba OpenAI Co-op Translator.

Chat pagrindu veikiančiame MCP kliente paprastai nereikia rašyti įrankio JSON ranka. Paprašykite agento naudoti agento pagalbos darbo eigą:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Notebook atveju naudokite tą pačią schemą:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Jei jūsų MCP klientas palaiko serverio užklausas, naudokite `agent_assisted_markdown_translation_prompt`, kad klientas užkrautų tas pačias darbo eigos instrukcijas.

Markdown atveju:

1. Iškvieskite `start_markdown_agent_translation` su `document`, `language_code` ir, jei reikia, `source_path`.
2. Išverskite kiekvieną grąžintą gabalą pagrindiniame agentui sekdami gabalo `prompt`.
3. Iškvieskite `finish_markdown_agent_translation` su originaliu `job` ir išvertais gabalais, naudojant `chunk_id` ir `translated_text`.
4. Jei turinys bus įrašytas į išverstą tikslinį kelią, iškvieskite `rewrite_markdown_paths`.

Notebook atveju:

1. Iškvieskite `start_notebook_agent_translation` su notebook JSON ir `language_code`.
2. Išversti kiekvieną grąžintą gabalą pagrindiniame agentui.
3. Iškvieskite `finish_notebook_agent_translation` su originaliu `job` ir išvertais gabalais.
4. Iškvieskite `rewrite_notebook_paths`, jei reikia pakoreguoti išverstų notebook nuorodas pagal tikslinį kelią.

Agent-assisted įrankiai nekviečia Azure OpenAI arba OpenAI iš Co-op Translator. Pagrindinis agentas yra atsakingas už grąžintų gabalų vertimą. Co-op Translator tvarko Markdown gabalavimą, vietos rezervavimo ženklų išsaugojimą, frontmatter rekonstrukciją, notebook langelių pakeitimą ir povertiminę normalizaciją.

### Išversti visą saugyklą

Naudokite `run_translation`, kai vartotojas nori, kad Co-op Translator elgtųsi kaip `translate` CLI.

Saugyklos vertimas pagal nutylėjimą naudoja `dry_run=true`, kad agentas galėtų patikrinti apimtį prieš keičiant failus:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Kad leisti įrašymus, kvietėjas turi nustatyti tiek `dry_run=false`, tiek `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` pateikiamas kaip suderinamumo aliasas `run_translation`.

### Peržiūrėti išverstą turinį

Naudokite `run_review` determinizuotoms patikroms, kurios nereikalauja LLM ar Vision kredencialų:

!!! note "Beta"
    MCP exposes the beta `run_review` API. It is safe for read-only review workflows, but review checks and issue schemas may evolve.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Rezultatas apima užfiksuotą teksto išvestį ir, kai prieinama, struktūruotą peržiūros santrauką.

## Rankiniai serverio paleidimai

Rankiniai paleidimai skirti labiau derinimui arba transportams, kurie elgiasi kaip ilgai veikiantys serveriai.

Derinkite numatytąjį stdio serverį:

```bash
co-op-translator-mcp
```

Paleisti iš source checkout:

```bash
python -m co_op_translator.mcp.server
```

Paleisti ilgai veikiančią HTTP arba SSE serverį:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Vietinėms redaktoriaus ir agente integracijoms pirmenybę teikite kliento valdomam `stdio` nustatymui 2 žingsnyje.

## Įrankiai

| Įrankis | Paskirtis | Rašo failus |
| --- | --- | --- |
| `translate_markdown_content` | Išversti Markdown eilutę. | Ne |
| `translate_notebook_content` | Išversti Markdown langelius notebook JSON. | Ne |
| `translate_image_content` | Išversti tekstą viename vaizde ir grąžinti base64 vaizdo duomenis. | Pasirinktina, tik kai pateiktas `output_path` |
| `start_markdown_agent_translation` | Paruošti Markdown gabalus pagrindiniam agentui versti be Co-op Translator LLM kredencialų. | Ne |
| `finish_markdown_agent_translation` | Atkurti Markdown iš pagrindinio agento išverstų gabalų. | Ne |
| `start_notebook_agent_translation` | Paruošti notebook Markdown-langelių gabalus pagrindiniam agentui versti. | Ne |
| `finish_notebook_agent_translation` | Atkurti notebook JSON iš pagrindinio agento išverstų gabalų. | Ne |
| `rewrite_markdown_paths` | Perrašyti Markdown kūną ir frontmatter keliams tinkamiems išverstam tikslui. | Ne |
| `rewrite_notebook_paths` | Perrašyti kelius notebook Markdown langeliuose. | Ne |
| `run_translation` | Vykdyti projekto lygio vertimą kaip CLI. | Taip, kai `dry_run=false` ir `confirm_write=true` |
| `translate_project` | Suderinamumo aliasas `run_translation`. | Taip, kai `dry_run=false` ir `confirm_write=true` |
| `run_review` | Vykdyti determinizuotas peržiūros patikras. | Ne |
| `get_configuration_status` | Pranešti apie sukonfigūruotus LLM ir Vision tiekėjus neatskleidžiant slaptažodžių. | Ne |
| `list_supported_languages` | Išvardinti palaikomų tikslinių kalbų kodus. | Ne |
| `get_api_overview` | Apibūdinti prieinamas MCP darbo eigas ir įrankius. | Ne |

## Ištekliai

| Resource URI | Paskirtis |
| --- | --- |
| `co-op://api` | JSON apžvalga apie darbo eigas ir įrankius. |
| `co-op://supported-languages` | JSON sąrašas palaikomų kalbų kodų. |
| `co-op://configuration` | JSON tiekėjų prieinamumo santrauka be slaptų reikšmių. |

## Užklausos

| Užklausa | Paskirtis |
| --- | --- |
| `translate_markdown_document_prompt` | Nurodyti MCP klientui turinio vertimą ir neprivalomą kelių perrašymą. |
| `agent_assisted_markdown_translation_prompt` | Nurodyti MCP klientui, kaip atlikti pagrindinio agento Markdown vertimą be Co-op Translator LLM tiekėjo kredencialų. |
| `translate_repository_prompt` | Nurodyti MCP klientui saugyklos vertimą, kai pradedama nuo dry-run. |

## Kopijuoti ir įklijuoti pavyzdžiai

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

Išversti Markdown naudojant pagrindinio agento modelį:

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

Po to, kai pagrindinis agentas išverčia kiekvieną grąžintą gabalą, užbaikite darbą su pilnu `job` objektu, kurį grąžino `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Peržiūra saugyklos vertimo:

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
| MCP klientas neranda `co-op-translator-mcp`. | Naudokite absoliutų Python vykdomąjį failą ir `["-m", "co_op_translator.mcp.server"]` source checkout konfigūraciją. |
| Serveris nurodytas, bet vertimas nepavyksta. | Iškvieskite `get_configuration_status` ir patikrinkite, ar yra prieinamas LLM tiekėjas. |
| Norite Markdown ar notebook vertimo be Azure OpenAI/OpenAI raktų. | Naudokite `start_markdown_agent_translation` / `finish_markdown_agent_translation` arba atitinkamus notebook įrankius, kad pagrindinis agentas išverstų gabalus. |
| Vaizdų vertimas nepavyksta. | Patikrinkite, ar nustatyti Azure AI Vision kintamieji ir iškvieskite `get_configuration_status`. |
| Saugyklos vertimas neįrašo failų. | Nustatykite `dry_run=false` ir `confirm_write=true` tik gavus aiškų vartotojo patvirtinimą. |
| Kliento konfigūracijos pakeitimai neatsispindi. | Paleiskite arba įkraukite MCP klientą iš naujo. |

## Saugumo pastabos

- MCP įrankių kvietimai yra valdomi modelio per pagrindinę programą, todėl saugyklos vertimas pagal nutylėjimą yra dry-run.
- Pilnas saugyklos vertimas gali sukurti, atnaujinti arba pašalinti daug failų. Prieš nustatant `confirm_write=true` reikalaukite aiškaus vartotojo patvirtinimo.
- Konfigūracijos būsenos įrankis niekada negrąžina API raktų, galinių taškų ar kitų slaptų reikšmių.
- Vaizdų vertimas grąžina base64 vaizdo duomenis. Dideli vaizdai gali sukurti didelius įrankio atsakymus.
- Agento pagalbos įrankiai grąžina šaltinio gabalus ir užklausas MCP pagrindiniam agentui. Naudokite juos tik su turiniu, kurį vartotojas sutinka siųsti tam pagrindinio agento modeliui.