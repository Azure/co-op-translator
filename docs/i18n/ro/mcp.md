# Server MCP

Co-op Translator include un server Model Context Protocol pentru agenți, editori și clienți compatibili MCP.

Pentru configurația locală implicită, utilizatorii nu mențin un server separat pornit manual. Ei configurează clientul MCP, iar clientul pornește automat `co-op-translator-mcp` peste `stdio` atunci când are nevoie de instrumentele Co-op Translator.

Dacă decideți între CLI, API Python și MCP, începeți cu [Alegeți fluxul de lucru](workflows.md).

Folosiți MCP când un agent sau editor ar trebui să apeleze Co-op Translator direct:

| Scopul utilizatorului | Instrumente MCP |
| --- | --- |
| Traduceți un document Markdown, un notebook sau o imagine | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Traduceți conținut Markdown sau notebook cu modelul agentului gazdă | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rescrieți linkurile traduse din Markdown sau notebook după alegerea căii de ieșire | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Traduceți un întreg depozit precum CLI-ul | `run_translation`, `translate_project` |
| Revizuiți ieșirea tradusă fără credențiale LLM | `run_review` |
| Inspectați capabilitățile și starea mediului | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Serverul MCP înfășoară aceeași API publică Python documentată în [API Python](api.md). Instrumentele bazate pe provider folosesc aceiași provideri configurați ca și CLI-ul și API-ul Python. Instrumentele asistate de agent pregătesc fragmente pentru ca agentul gazdă MCP să le traducă, apoi folosesc Co-op Translator pentru a reconstrui Markdown-ul sau notebook-ul final.

## Pasul 1: Instalați și configurați Co-op Translator

Instalați Co-op Translator în mediul Python pe care îl va folosi clientul MCP:

```bash
pip install co-op-translator
```

Pentru dezvoltare locală din acest repository, instalați pachetul în modul editabil:

```bash
pip install -e .
```

Alegeți modul de traducere pe care îl va folosi clientul MCP:

| Mod | Folosiți pentru | Credențiale |
| --- | --- | --- |
| Bazat pe provider | Co-op Translator apelează `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, sau `run_translation`. | Traducerea necesită Azure OpenAI, OpenAI sau Anthropic. Traducerea imaginilor necesită și Azure AI Vision. |
| Asistat de agent | Agentul gazdă MCP traduce fragmente returnate de `start_markdown_agent_translation` sau `start_notebook_agent_translation`. | Nu sunt necesare credențiale ale providerului LLM pentru Co-op Translator pentru fragmente Markdown sau notebook. Traducerea imaginilor nu este încă acoperită de modul asistat de agent. |

Dacă începeți cu traducerea Markdown sau a notebook-urilor în interiorul unui agent precum Codex sau Claude Code, începeți cu modul asistat de agent. Folosiți modul bazat pe provider când doriți ca Co-op Translator să apeleze direct providerii configurați, când traduceți imagini sau când executați traducerea la nivel de repository, precum CLI-ul.

Configurați un provider pentru fluxurile de lucru bazate pe provider:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Sau OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Sau Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Traducerea imaginilor bazată pe provider necesită, în plus:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Modul asistat de agent acoperă în prezent Markdown-ul și celulele Markdown din notebook. Traducerea imaginilor folosește în continuare pipeline-ul de imagini bazat pe provider și necesită Azure AI Vision pentru OCR și redare care păstrează aspectul.

## Pasul 2: Configurați clientul MCP

Pentru configurația locală normală `stdio`, adăugați Co-op Translator la configurația clientului MCP. Clientul va porni și opri procesul automat.

Configurația pentru pachet instalat:

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

Configurația pentru checkout-ul sursei pe Windows:

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

Configurația pentru checkout-ul sursei pe macOS sau Linux:

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

După ce schimbați configurația clientului MCP, reporniți sau reîncărcați clientul pentru a descoperi noul server.

## Pasul 3: Verificați serverul în client

Rugați clientul MCP să listeze instrumentele disponibile sau apelați mai întâi unul dintre ajutoarele doar pentru citire:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Verificări utile inițiale:

| Instrument | Ce să verificați |
| --- | --- |
| `get_api_overview` | Confirmă că serverul este accesibil și afișează fluxurile de lucru disponibile. |
| `list_supported_languages` | Confirmă că datele de limbă incluse pot fi încărcate. |
| `get_configuration_status` | Confirmă disponibilitatea providerului LLM și Vision fără a expune valori secrete. |

## Pasul 4: Alegeți un flux de lucru

### Traduceți fișiere sau documente individuale

Folosiți instrumentele de conținut bazate pe provider când clientul MCP are deja conținutul documentului sau calea imaginii și Co-op Translator ar trebui să apeleze providerii de traducere configurați.

Pentru Markdown:

1. Apelați `translate_markdown_content` cu `document`, `language_code` și opțional `source_path`.
2. Dacă rezultatul tradus va fi scris într-un layout de ieșire Co-op Translator, apelați `rewrite_markdown_paths`.
3. Lăsați clientul să scrie sau să returneze `content` final.

Pentru notebook-uri:

1. Apelați `translate_notebook_content` cu JSON-ul notebook-ului și `language_code`.
2. Apelați `rewrite_notebook_paths` dacă linkurile din notebook tradus trebuie ajustate pentru o cale țintă.
3. Scrieți sau returnați JSON-ul final al notebook-ului.

Pentru imagini:

1. Apelați `translate_image_content` cu `image_path`, `language_code` și opțional `root_dir` sau `fast_mode`.
2. Citiți `data_base64` și `mime_type` returnate.
3. Dacă se furnizează `output_path`, imaginea tradusă este salvată și la acea cale.

Instrumentele de conținut nu efectuează descoperirea proiectului, actualizări de metadata, declarații sau rescriere automată a căilor. Dacă doriți ca agentul gazdă să traducă fragmente Markdown sau notebook fără credențiale ale providerului LLM pentru Co-op Translator, folosiți fluxul asistat de agent de mai jos.

### Traduceți cu modelul agentului gazdă

Folosiți instrumentele asistate de agent când doriți ca agentul gazdă MCP, de exemplu un asistent de programare, să producă textul tradus în loc să configurați un provider LLM pentru Co-op Translator.

Într-un client MCP bazat pe chat, de obicei nu trebuie să scrieți voi înșivă JSON-ul instrumentului. Rugați agentul să folosească fluxul de lucru asistat de agent:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Pentru notebook-uri, folosiți același tipar:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Dacă clientul MCP acceptă prompturi de server, folosiți `agent_assisted_markdown_translation_prompt` pentru ca clientul să încarce aceleași instrucțiuni de flux de lucru.

Pentru Markdown:

1. Apelați `start_markdown_agent_translation` cu `document`, `language_code` și opțional `source_path`.
2. Traduceți fiecare fragment returnat în agentul gazdă urmând `prompt`-ul fragmentului.
3. Apelați `finish_markdown_agent_translation` cu `job` original și fragmentele traduse folosind `chunk_id` și `translated_text`.
4. Dacă conținutul va fi scris într-o cale țintă tradusă, apelați `rewrite_markdown_paths`.

Pentru notebook-uri:

1. Apelați `start_notebook_agent_translation` cu JSON-ul notebook-ului și `language_code`.
2. Traduceți fiecare fragment returnat în agentul gazdă.
3. Apelați `finish_notebook_agent_translation` cu `job` original și fragmentele traduse.
4. Apelați `rewrite_notebook_paths` dacă linkurile din notebook tradus necesită ajustare pentru calea țintă.

Instrumentele asistate de agent nu apelează providerul LLM configurat în numele Co-op Translator. Agentul gazdă este responsabil pentru traducerea fragmentelor returnate. Co-op Translator se ocupă de împărțirea în fragmente a Markdown-ului, păstrarea placeholder-elor, reconstrucția frontmatter-ului, înlocuirea celulelor din notebook și normalizarea post-traducere.

### Traduceți întregul depozit

Folosiți `run_translation` când utilizatorul dorește ca Co-op Translator să se comporte ca CLI-ul `translate`.

Traducerea depozitului are implicit `dry_run=true` astfel încât un agent să poată inspecta scopul înainte de modificările de fișiere:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Rezultatul lui `run_translation` include un array `events` cu evenimente progres versionate
`co-op.translation.event.v1`. Clienții MCP ar trebui să folosească câmpuri precum `type`, `stage_key`, `completed`, `total`, și `current_path` în loc să parseze textul capturat din consolă. Specificați `json_events_path` pentru a scrie de asemenea acele evenimente într-un fișier NDJSON.




Pentru a permite scrierile, apelantul trebuie să seteze atât `dry_run=false`, cât și `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` este expus ca un alias de compatibilitate pentru `run_translation`.

### Revizuirea ieșirii traduse

Folosiți `run_review` pentru verificări deterministe care nu necesită credențiale LLM sau Vision:

!!! note "Beta"
    MCP expune API-ul beta `run_review`. Este sigur pentru fluxuri de revizuire doar pentru citire, dar verificările de revizuire și schemele de issue pot evolua.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Rezultatul include textul capturat al output-ului și un sumar structurat al revizuirii când este disponibil.

## Execuții manuale ale serverului

Execuțiile manuale sunt în principal pentru depanare sau pentru transporturi care se comportă ca servere de lungă durată.

Depanați serverul stdio implicit:

```bash
co-op-translator-mcp
```

Rulați dintr-un checkout al sursei:

```bash
python -m co_op_translator.mcp.server
```

Rulați un server HTTP sau SSE de durată lungă:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Pentru integrările locale cu editorul și agentul, preferați configurația `stdio` gestionată de client din Pasul 2.

## Instrumente

| Instrument | Scop | Scrie fișiere |
| --- | --- | --- |
| `translate_markdown_content` | Traduce un text Markdown. | Nu |
| `translate_notebook_content` | Traduce celulele Markdown din JSON-ul notebook-ului. | Nu |
| `translate_image_content` | Traduce textul dintr-o imagine și returnează datele imaginii în base64. | Opțional, doar când `output_path` este furnizat |
| `start_markdown_agent_translation` | Pregătește fragmente Markdown pentru ca agentul gazdă să le traducă fără credențiale LLM pentru Co-op Translator. | Nu |
| `finish_markdown_agent_translation` | Reconstruiește Markdown-ul din fragmentele traduse de agentul gazdă. | Nu |
| `start_notebook_agent_translation` | Pregătește fragmente de celule Markdown din notebook pentru ca agentul gazdă să le traducă. | Nu |
| `finish_notebook_agent_translation` | Reconstruiește JSON-ul notebook-ului din fragmentele traduse de agentul gazdă. | Nu |
| `rewrite_markdown_paths` | Rescrie căile din corpul Markdown și din frontmatter pentru o țintă tradusă. | Nu |
| `rewrite_notebook_paths` | Rescrie căile din celulele Markdown ale notebook-ului. | Nu |
| `run_translation` | Rulează traducerea la nivel de proiect precum CLI-ul. | Da când `dry_run=false` și `confirm_write=true` |
| `translate_project` | Alias de compatibilitate pentru `run_translation`. | Da când `dry_run=false` și `confirm_write=true` |
| `run_review` | Rulează verificări deterministe de revizuire. | Nu |
| `get_configuration_status` | Raportează provideri LLM și Vision configurați fără a expune secrete. | Nu |
| `list_supported_languages` | Listează codurile limbilor țintă suportate. | Nu |
| `get_api_overview` | Descrie fluxurile de lucru și instrumentele MCP disponibile. | Nu |

## Resurse

| URI resursă | Scop |
| --- | --- |
| `co-op://api` | Prezentare JSON a fluxurilor de lucru și instrumentelor. |
| `co-op://supported-languages` | Listă JSON a codurilor limbilor suportate. |
| `co-op://configuration` | Sumar JSON al disponibilității providerilor fără secrete. |

## Prompturi

| Prompt | Scop |
| --- | --- |
| `translate_markdown_document_prompt` | Ghidează un client MCP prin traducerea conținutului plus rescrierea opțională a căilor. |
| `agent_assisted_markdown_translation_prompt` | Ghidează un client MCP prin traducerea Markdown de către agentul gazdă fără credențiale ale providerului LLM pentru Co-op Translator. |
| `translate_repository_prompt` | Ghidează un client MCP prin traducerea depozitului cu dry-run inițial. |

## Exemple copy-paste

Traduceți conținut Markdown:

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

Rescrieți linkurile Markdown traduse:

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

Traduceți Markdown cu modelul agentului gazdă:

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

După ce agentul gazdă traduce fiecare fragment returnat, finalizați jobul cu obiectul complet `job` returnat de `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Previzualizați traducerea depozitului:

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

## Depanare

| Problemă | Ce să încercați |
| --- | --- |
| Clientul MCP nu găsește `co-op-translator-mcp`. | Folosiți calea absolută a executabilului Python și configurația source checkout `["-m", "co_op_translator.mcp.server"]`. |
| Serverul este listat dar traducerea eșuează. | Apelați `get_configuration_status` și confirmați că un provider LLM este disponibil. |
| Doriți traducerea Markdown sau a notebook-ului fără credențiale de provider. | Folosiți `start_markdown_agent_translation` / `finish_markdown_agent_translation` sau echivalentele pentru notebook astfel încât agentul gazdă să traducă fragmentele. |
| Traducerea imaginilor eșuează. | Confirmați că variabilele Azure AI Vision sunt setate și apelați `get_configuration_status`. |
| Traducerea depozitului nu scrie fișiere. | Setați `dry_run=false` și `confirm_write=true` doar după aprobarea explicită a utilizatorului. |
| Schimbările în configurația clientului nu apar. | Reporniți sau reîncărcați clientul MCP. |

## Note de securitate

- Apelurile instrumentelor MCP sunt controlate de model de aplicația gazdă, așadar traducerea depozitului este implicit în dry-run.
- Traducerea completă a depozitului poate crea, actualiza sau șterge multe fișiere. Cereți aprobarea explicită a utilizatorului înainte de a seta `confirm_write=true`.
- Instrumentul de stare a configurației nu returnează niciodată chei API, endpoint-uri sau alte valori secrete.
- Traducerea imaginilor returnează date imagine în base64. Imaginile mari pot produce răspunsuri mari ale instrumentelor.
- Instrumentele asistate de agent returnează fragmentele sursă și prompturi către gazda MCP. Folosiți-le doar cu conținut pe care utilizatorul este confortabil să îl trimită modelului agent gazdă.