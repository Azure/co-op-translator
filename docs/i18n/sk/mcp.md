# MCP Server

Co-op Translator obsahuje Model Context Protocol server pre agentov, editory a MCP-kompatibilných klientov.

Pre predvolené lokálne nastavenie používatelia ručne nespúšťajú samostatný server. Nakonfigurujú svoj MCP klient a klient automaticky spustí `co-op-translator-mcp` cez `stdio`, keď potrebuje nástroje Co-op Translator.

Ak sa rozhodujete medzi CLI, Python API a MCP, začnite s [Choose Your Workflow](workflows.md).

Použite MCP, keď by agent alebo editor mal volať Co-op Translator priamo:

| User goal | MCP tools |
| --- | --- |
| Preložte jeden Markdown dokument, poznámkový blok alebo obrázok | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Preložte obsah Markdownu alebo bunky Markdown v notebooku pomocou hostiteľského modelu agenta | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Prepíšte preložené odkazy v Markdowne alebo v notebooku po výbere výstupnej cesty | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Preložte celý repozitár pomocou CLI | `run_translation`, `translate_project` |
| Skontrolujte preložený výstup bez prihlasovacích údajov LLM | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP server obalí tú istú verejnú Python API, ktorá je dokumentovaná v [Python API](api.md). Nástroje využívajúce poskytovateľov používajú tie isté nakonfigurované providery ako CLI a Python API. Nástroje asistované agentom pripravia časti pre MCP hostiteľa, aby ich preložil, a potom použijú Co-op Translator na rekonštrukciu finálneho Markdownu alebo notebooku.

## Krok 1: Inštalácia a konfigurácia Co-op Translator

Nainštalujte Co-op Translator v Python prostredí, ktoré bude používať váš MCP klient:

```bash
pip install co-op-translator
```

Pre lokálny vývoj z tohto repozitára nainštalujte balíček v editable režime:

```bash
pip install -e .
```

Vyberte režim prekladu, ktorý bude váš MCP klient používať:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator volá `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` alebo `run_translation`. | Preklad vyžaduje Azure OpenAI, OpenAI alebo Anthropic. Pri preklade obrázkov je tiež potrebné Azure AI Vision. |
| Agent-assisted | MCP host agent preloží časti vrátené `start_markdown_agent_translation` alebo `start_notebook_agent_translation`. | Pre Markdown alebo notebook nie sú potrebné prihlasovacie údaje LLM providera pre Co-op Translator. Preklad obrázkov zatiaľ nie je pokrytý režimom asistovaným agentom. |

Ak začínate s prekladom Markdownu alebo notebooku v rámci agenta, ako je Codex alebo Claude Code, začnite režimom asistovaným agentom. Použite provider-backed režim, keď chcete, aby Co-op Translator sám volal vaše nakonfigurované providery, keď prekladáte obrázky, alebo keď spúšťate preklad na úrovni repozitára ako CLI.

Nakonfigurujte jedného providera pre provider-backed workflowy:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Alebo OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Alebo Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Provider-backed preklad obrázkov navyše potrebuje:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Režim asistovaný agentom momentálne pokrýva Markdown a bunky Markdown v notebookoch. Preklad obrázkov stále používa pipeline poskytovateľa a vyžaduje Azure AI Vision pre OCR a renderovanie so zachovaním rozloženia.

## Krok 2: Konfigurácia vášho MCP klienta

Pre bežné lokálne `stdio` nastavenie pridajte Co-op Translator do konfigurácie vášho MCP klienta. Klient automaticky spustí a zastaví proces.

Konfigurácia pre inštalovaný balíček:

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

Konfigurácia pre checkout zdrojov na Windows:

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

Konfigurácia pre checkout zdrojov na macOS alebo Linux:

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

Po zmene konfigurácie MCP klienta reštartujte alebo znova načítajte klienta, aby mohol objaviť nový server.

## Krok 3: Overenie servera v klientovi

Požiadajte MCP klienta, aby vymenoval dostupné nástroje, alebo najskôr zavolajte niektorý z read-only helperov:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Užitočné prvé kontroly:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Potvrdí, že je server dosiahnuteľný a ukáže dostupné workflowy. |
| `list_supported_languages` | Potvrdí, že zabalené dátové súbory jazykov sa dajú načítať. |
| `get_configuration_status` | Potvrdí dostupnosť LLM a Vision providerov bez toho, aby odhalil tajné hodnoty. |

## Krok 4: Vyberte pracovný postup

### Preklad jednotlivých súborov alebo dokumentov

Použite provider-backed content nástroje, keď MCP klient už má obsah dokumentu alebo cestu k obrázku a Co-op Translator by mal volať nakonfigurovaných providerov.

Pre Markdown:

1. Zavolajte `translate_markdown_content` s `document`, `language_code` a voliteľne `source_path`.
2. Ak bude preložený výsledok zapísaný do výstupného layoutu Co-op Translator, zavolajte `rewrite_markdown_paths`.
3. Nechajte klienta zapísať alebo vrátiť finálny `content`.

Pre notebooky:

1. Zavolajte `translate_notebook_content` s notebookovým JSONom a `language_code`.
2. Zavolajte `rewrite_notebook_paths`, ak potrebujete upraviť preložené odkazy v notebooku pre cieľovú cestu.
3. Zapíšte alebo vráťte finálny notebookový JSON.

Pre obrázky:

1. Zavolajte `translate_image_content` s `image_path`, `language_code` a voliteľne `root_dir` alebo `fast_mode`.
2. Prečítajte vrátené `data_base64` a `mime_type`.
3. Ak je poskytnutý `output_path`, preložený obrázok sa tiež uloží na túto cestu.

Content nástroje nevykonávajú discovery projektu, aktualizácie metadát, disclaimery ani automatické prepísanie ciest. Ak chcete, aby host agent preložil časti Markdownu alebo notebooku bez prihlasovacích údajov LLM providera pre Co-op Translator, použite nižšie agent-assisted workflow.

### Preklad pomocou hostiteľského modelu agenta

Použite agent-assisted nástroje, keď chcete, aby MCP host agent, napríklad kódovací asistent, vytvoril preložený text namiesto konfigurácie LLM providera pre Co-op Translator.

V chatovom MCP klientovi zvyčajne nemusíte písať JSON nástrojov sami. Požiadajte agenta, aby použil agent-assisted workflow:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Pre notebooky použite rovnaký vzor:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Ak váš MCP klient podporuje server prompts, použite `agent_assisted_markdown_translation_prompt`, aby si klient načítal rovnaké inštrukcie workflowu.

Pre Markdown:

1. Zavolajte `start_markdown_agent_translation` s `document`, `language_code` a voliteľne `source_path`.
2. Preložte každú vrátenú časť v host agentovi podľa `prompt` časti.
3. Zavolajte `finish_markdown_agent_translation` s pôvodným `job` a preloženými časťami pomocou `chunk_id` a `translated_text`.
4. Ak bude obsah zapísaný do preloženej cieľovej cesty, zavolajte `rewrite_markdown_paths`.

Pre notebooky:

1. Zavolajte `start_notebook_agent_translation` s notebookovým JSONom a `language_code`.
2. Preložte každú vrátenú časť v host agentovi.
3. Zavolajte `finish_notebook_agent_translation` s pôvodným `job` a preloženými časťami.
4. Zavolajte `rewrite_notebook_paths`, ak potrebujú preložené odkazy v notebooku úpravu pre cieľovú cestu.

Agent-assisted nástroje nevolajú nakonfigurovaného LLM providera z Co-op Translator. Host agent je zodpovedný za preklad vrátených častí. Co-op Translator sa postará o delenie Markdownu na časti, zachovanie zástupných symbolov, rekonštrukciu frontmatteru, nahradenie buniek v notebooku a post-prekladovú normalizáciu.

### Preložiť celé úložisko

Použite `run_translation`, keď chce používateľ, aby sa Co-op Translator správal ako CLI `translate`.

Preklad repozitára má predvolene `dry_run=true`, aby si agent mohol pred zmenami súborov skontrolovať rozsah:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Výsledok `run_translation` obsahuje pole `events` s verzovanými
`co-op.translation.event.v1` progresnými udalosťami. MCP klienti by mali používať polia ako
`type`, `stage_key`, `completed`, `total` a `current_path` namiesto
parsovania zachyteného textu v konzole. Predajte `json_events_path`, ak chcete tieto udalosti
zapísať aj do NDJSON súboru.

Aby boli povolené zápisy, volajúci musí nastaviť zároveň `dry_run=false` a `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` je vystavený ako kompatibilný alias pre `run_translation`.

### Skontrolovať preložený výstup

Použite `run_review` pre deterministické kontroly, ktoré nevyžadujú LLM alebo Vision poverenia:

!!! note "Beta"
    MCP sprístupňuje beta API `run_review`. Je bezpečné pre revízne pracovné toky len na čítanie, ale kontroly pri revízii a schémy problémov sa môžu vyvíjať.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Výsledok obsahuje zachytený textový výstup a štruktúrované zhrnutie kontroly, keď je k dispozícii.

## Ručné spustenia servera

Manuálne spustenia sú hlavne na ladenie alebo pre transporty, ktoré sa správajú ako dlho-bežiace servery.

Ladenie predvoleného stdio servera:

```bash
co-op-translator-mcp
```

Spustenie z checkoutu zdrojov:

```bash
python -m co_op_translator.mcp.server
```

Spustenie dlho-bežiaceho HTTP alebo SSE servera:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Pre lokálne integrácie editorov a agentov preferujte klientom-spravovanú `stdio` konfiguráciu v Kroku 2.

## Tools

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Preloží reťazec Markdown. | Nie |
| `translate_notebook_content` | Preloží Markdown bunky v notebookovom JSONe. | Nie |
| `translate_image_content` | Preloží text v jednom obrázku a vráti base64 obrazové dáta. | Voliteľné, len keď je poskytnutý `output_path` |
| `start_markdown_agent_translation` | Pripraví Markdown časti, aby ich host agent preložil bez prihlasovacích údajov LLM Co-op Translator. | Nie |
| `finish_markdown_agent_translation` | Rekonštruuje Markdown z host-agentom preložených častí. | Nie |
| `start_notebook_agent_translation` | Pripraví Markdown-bunkové časti notebooku, aby ich host agent preložil. | Nie |
| `finish_notebook_agent_translation` | Rekonštruuje notebookový JSON z host-agentom preložených častí. | Nie |
| `rewrite_markdown_paths` | Prepíše cesty v tele Markdownu a frontmatter pre preložený cieľ. | Nie |
| `rewrite_notebook_paths` | Prepíše cesty v Markdown bunkách notebooku. | Nie |
| `run_translation` | Spustí preklad projektu ako CLI. | Áno, keď `dry_run=false` a `confirm_write=true` |
| `translate_project` | Kompatibilný alias pre `run_translation`. | Áno, keď `dry_run=false` a `confirm_write=true` |
| `run_review` | Spustí deterministické kontroly prehliadky. | Nie |
| `get_configuration_status` | Nahlási nakonfigurovaných LLM a Vision providerov bez odhalenia tajomstiev. | Nie |
| `list_supported_languages` | Vypíše podporované cieľové jazykové kódy. | Nie |
| `get_api_overview` | Popíše dostupné MCP workflowy a nástroje. | Nie |

## Resources

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON prehľad workflowov a nástrojov. |
| `co-op://supported-languages` | JSON zoznam podporovaných jazykových kódov. |
| `co-op://configuration` | JSON súhrn dostupnosti providerov bez tajomstiev. |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Viesť MCP klienta cez preklad obsahu plus voliteľné prepísanie ciest. |
| `agent_assisted_markdown_translation_prompt` | Viesť MCP klienta cez preklad Markdownu host-agentom bez prihlasovacích údajov LLM providera Co-op Translator. |
| `translate_repository_prompt` | Viesť MCP klienta cez preklad repozitára, ktorý najprv vykoná suchý beh. |

## Príklady kopírovania a vkladania

Preložte obsah Markdownu:

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

Prepíšte preložené odkazy v Markdown:

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

Preložte Markdown s modelom host agenta:

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

Po tom, ako host agent preloží každú vrátenú časť, dokončite úlohu s kompletným `job` objektom vráteným `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Náhľad prekladu repozitára:

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

## Troubleshooting

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Použite absolútnu cestu k Python vykonávateľnému súboru a `["-m", "co_op_translator.mcp.server"]` konfiguráciu pre source checkout. |
| Server je uvedený, ale preklad zlyháva. | Zavolajte `get_configuration_status` a potvrďte, že je dostupný LLM provider. |
| Chcete preklad Markdownu alebo notebooku bez prihlasovacích údajov poskytovateľa. | Použite `start_markdown_agent_translation` / `finish_markdown_agent_translation` alebo ekvivalenty pre notebook, aby host agent preložil časti. |
| Image translation fails. | Potvrďte, že sú nastavené premenné Azure AI Vision a zavolajte `get_configuration_status`. |
| Preklad repozitára nezapisuje súbory. | Nastavte `dry_run=false` a `confirm_write=true` až po explicitnom súhlase používateľa. |
| Zmeny v konfigurácii klienta sa nezobrazujú. | Reštartujte alebo znova načítajte MCP klienta. |

## Bezpečnostné poznámky

- Volania nástrojov MCP sú riadené modelom hostiteľskej aplikácie, takže preklad repozitára je predvolene v režime dry-run.
- Plný preklad repozitára môže vytvoriť, aktualizovať alebo odstrániť mnoho súborov. Vyžadujte explicitné schválenie používateľa pred nastavením `confirm_write=true`.
- Nástroj stavu konfigurácie nikdy nevracia API kľúče, koncové body ani iné tajné hodnoty.
- Preklad obrázka vracia base64 obrazové údaje. Veľké obrázky môžu viesť k veľkým odpovediam nástroja.
- Nástroje asistované agentom vracajú zdrojové úryvky a výzvy hostiteľovi MCP. Používajte ich iba s obsahom, ktorý je pre používateľa pohodlné odoslať tomuto modelu hostiteľského agenta.
