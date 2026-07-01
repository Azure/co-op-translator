# MCP server

Co-op Translator obsahuje server Model Context Protocol pre agentov, editory a klientov kompatibilných s MCP.

Pre predvolené lokálne nastavenie používatelia nespúšťajú samostatný server ručne. Nakonfigurujú svoj MCP klient a klient automaticky spustí `co-op-translator-mcp` cez `stdio`, keď bude potrebovať nástroje Co-op Translator.

Ak sa rozhodujete medzi CLI, Python API a MCP, začnite s [Choose Your Workflow](workflows.md).

Použite MCP, keď má agent alebo editor volať Co-op Translator priamo:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP server obalí to isté verejné Python API zdokumentované v [Python API](api.md). Nástroje závislé od poskytovateľov používajú rovnakých nakonfigurovaných poskytovateľov ako CLI a Python API. Nástroje asistované agentom pripravia úseky pre MCP hostiteľa na preklad a potom použijú Co-op Translator na rekonštrukciu konečného Markdownu alebo notebooku.

## Krok 1: Inštalácia a konfigurácia Co-op Translator

Nainštalujte Co-op Translator do Python prostredia, ktoré bude používať váš MCP klient:

```bash
pip install co-op-translator
```

Pre lokálny vývoj z tohto repozitára nainštalujte balík v editable režime:

```bash
pip install -e .
```

Vyberte režim prekladu, ktorý bude používať váš MCP klient:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator volá `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, alebo `run_translation`. | Preklad Markdownu a notebookov vyžaduje Azure OpenAI alebo OpenAI. Preklad obrázkov tiež vyžaduje Azure AI Vision. |
| Agent-assisted | MCP hostiteľský agent prekladá úseky vrátené `start_markdown_agent_translation` alebo `start_notebook_agent_translation`. | Pre úseky Markdownu alebo notebooku nie sú potrebné žiadne prihlasovacie údaje LLM poskytovateľa pre Co-op Translator. Režim asistovaný agentom ešte nepokrýva preklad obrázkov. |

Ak začínate s prekladom Markdownu alebo notebooku v rámci agenta, ako sú Codex alebo Claude Code, začnite v režime asistovanom agentom. Použite režim podporovaný poskytovateľom, keď chcete, aby Co-op Translator sám volal vašich nakonfigurovaných poskytovateľov, keď prekladáte obrázky, alebo keď vykonávate preklad na úrovni repozitára ako CLI.

Nakonfigurujte prihlasovacie údaje poskytovateľa len pre workflowy závislé od poskytovateľa:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Preklad obrázkov závislý od poskytovateľa ďalej potrebuje:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## Krok 2: Konfigurujte svoj MCP klient

Pre bežné lokálne `stdio` nastavenie pridajte Co-op Translator do konfigurácie vášho MCP klienta. Klient automaticky spustí a zastaví proces.

Konfigurácia nainštalovaného balíka:

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

Konfigurácia zo zdrojového checkoutu na Windows:

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

Konfigurácia zo zdrojového checkoutu na macOS alebo Linuxe:

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

Po zmene konfigurácie MCP klienta reštartujte alebo znovu načítajte klienta, aby mohol objaviť nový server.

## Krok 3: Overte server v klientovi

Požiadajte MCP klienta, aby vypísal dostupné nástroje, alebo zavolajte najprv jeden z čítacích pomocníkov:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Užitočné prvé kontroly:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Potvrdí, že server je dostupný a ukáže dostupné workflowy. |
| `list_supported_languages` | Potvrdí, že balené jazykové dáta sa dajú načítať. |
| `get_configuration_status` | Potvrdí dostupnosť LLM a Vision poskytovateľov bez odhalenia tajných hodnôt. |

## Krok 4: Vyberte pracovný postup

### Preložte jednotlivé súbory alebo dokumenty

Použite nástroje závislé od poskytovateľa, keď má MCP klient už obsah dokumentu alebo cestu k obrázku a Co-op Translator má volať nakonfigurovaných poskytovateľov prekladu.

Pre Markdown:

1. Zavolajte `translate_markdown_content` s `document`, `language_code` a voliteľne `source_path`.
2. Ak bude preložený výsledok zapísaný do výstupného layoutu Co-op Translator, zavolajte `rewrite_markdown_paths`.
3. Nechajte klienta zapísať alebo vrátiť konečný `content`.

Pre notebooky:

1. Zavolajte `translate_notebook_content` s notebookovým JSONom a `language_code`.
2. Zavolajte `rewrite_notebook_paths`, ak je potrebné upraviť preložené odkazy v notebooku pre cieľovú cestu.
3. Zapíšte alebo vráťte konečný notebookový JSON.

Pre obrázky:

1. Zavolajte `translate_image_content` s `image_path`, `language_code` a voliteľne `root_dir` alebo `fast_mode`.
2. Prečítajte vrátené `data_base64` a `mime_type`.
3. Ak je uvedený `output_path`, preložený obrázok sa uloží aj na túto cestu.

Nástroje na obsah nevykonávajú objavovanie projektu, aktualizácie metadát, upozornenia ani automatické prepísanie ciest. Ak chcete, aby hostiteľský agent preložil úseky Markdownu alebo notebooku bez prihlasovacích údajov LLM poskytovateľa Co-op Translator, použite nižšie uvedený workflow asistovaný agentom.

### Preložte pomocou modelu hostiteľského agenta

Použite nástroje asistované agentom, keď chcete, aby MCP hostiteľský agent, napríklad kódovací asistent, vygeneroval preložený text namiesto toho, aby ste konfigurovali Azure OpenAI alebo OpenAI pre Co-op Translator.

V chatovom MCP klientovi zvyčajne nemusíte sami písať JSON nástrojov. Požiadajte agenta, aby použil workflow asistovaný agentom:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Pre notebooky použite rovnaký postup:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Ak váš MCP klient podporuje server prompt, použite `agent_assisted_markdown_translation_prompt`, aby si klient načítal rovnaké inštrukcie workflowu.

Pre Markdown:

1. Zavolajte `start_markdown_agent_translation` s `document`, `language_code` a voliteľne `source_path`.
2. Preložte každý vrátený úsek v hostiteľskom agentovi podľa `prompt` úseku.
3. Zavolajte `finish_markdown_agent_translation` s pôvodnou `job` a preloženými úsekmi pomocou `chunk_id` a `translated_text`.
4. Ak bude obsah zapísaný do preloženej cieľovej cesty, zavolajte `rewrite_markdown_paths`.

Pre notebooky:

1. Zavolajte `start_notebook_agent_translation` s notebookovým JSONom a `language_code`.
2. Preložte každý vrátený úsek v hostiteľskom agentovi.
3. Zavolajte `finish_notebook_agent_translation` s pôvodnou `job` a preloženými úsekmi.
4. Zavolajte `rewrite_notebook_paths`, ak je potrebné upraviť odkazy v preložených notebookových bunkách pre cieľovú cestu.

Nástroje asistované agentom nevolajú Azure OpenAI ani OpenAI z Co-op Translator. Hostiteľský agent je zodpovedný za preklad vrátených úsekov. Co-op Translator sa stará o delenie Markdownu na úseky, zachovanie zástupných znakov, rekonštrukciu frontmatteru, nahradenie buniek v notebooku a normalizáciu po preklade.

### Preložte celý repozitár

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

`translate_project` je vystavený ako alias kompatibility pre `run_translation`.

### Skontrolujte preložený výstup

Použite `run_review` pre deterministické kontroly, ktoré nevyžadujú prihlasovacie údaje LLM alebo Vision:

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

Výsledok obsahuje zachytený textový výstup a štruktúrované zhrnutie kontroly, keď je k dispozícii.

## Manuálne spustenia servera

Manuálne spustenia sú hlavne na ladenie alebo pre transporty, ktoré sa správajú ako dlho bežiace servery.

Ladite predvolený stdio server:

```bash
co-op-translator-mcp
```

Spustenie z checkoutu zdrojov:

```bash
python -m co_op_translator.mcp.server
```

Spustenie dlho bežiaceho HTTP alebo SSE servera:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Pre lokálne integrácie editorov a agentov uprednostnite konfiguráciu `stdio` spravovanú klientom v Kroku 2.

## Nástroje

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Preložiť reťazec Markdownu. | Nie |
| `translate_notebook_content` | Preložiť Markdown bunky v notebookovom JSONe. | Nie |
| `translate_image_content` | Preložiť text na jednom obrázku a vrátiť base64 obrázkové dáta. | Voliteľné, iba keď je uvedený `output_path` |
| `start_markdown_agent_translation` | Pripraviť úseky Markdownu pre hostiteľského agenta na preklad bez prihlasovacích údajov LLM Co-op Translator. | Nie |
| `finish_markdown_agent_translation` | Rekonštruovať Markdown z preložených úsekov hostiteľského agenta. | Nie |
| `start_notebook_agent_translation` | Pripraviť úseky Markdown buniek notebooku pre hostiteľského agenta na preklad. | Nie |
| `finish_notebook_agent_translation` | Rekonštruovať notebookový JSON z preložených úsekov hostiteľského agenta. | Nie |
| `rewrite_markdown_paths` | Prepísať cesty v tele Markdownu a frontmattere pre preložený cieľ. | Nie |
| `rewrite_notebook_paths` | Prepísať cesty v Markdown bunkách notebooku. | Nie |
| `run_translation` | Spustiť preklad projektu ako CLI. | Áno, keď `dry_run=false` a `confirm_write=true` |
| `translate_project` | Alias kompatibility pre `run_translation`. | Áno, keď `dry_run=false` a `confirm_write=true` |
| `run_review` | Spustiť deterministické kontrolné prehliadky. | Nie |
| `get_configuration_status` | Nahlásiť nakonfigurovaných LLM a Vision poskytovateľov bez odhalenia tajomstiev. | Nie |
| `list_supported_languages` | Zoznam podporovaných cieľových jazykových kódov. | Nie |
| `get_api_overview` | Popísať dostupné MCP workflowy a nástroje. | Nie |

## Zdroje

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON prehľad workflowov a nástrojov. |
| `co-op://supported-languages` | JSON zoznam podporovaných jazykových kódov. |
| `co-op://configuration` | JSON súhrn dostupnosti poskytovateľov bez tajných hodnôt. |

## Prompt-y

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Navigovať MCP klienta cez preklad obsahu s voliteľným prepísaním ciest. |
| `agent_assisted_markdown_translation_prompt` | Navigovať MCP klienta cez preklad Markdownu hostiteľským agentom bez prihlasovacích údajov LLM poskytovateľa Co-op Translator. |
| `translate_repository_prompt` | Navigovať MCP klienta cez preklad repozitára s najprv suchým behom (dry-run). |

## Príklady na kopírovanie a prilepenie

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

Preložte Markdown pomocou modelu hostiteľského agenta:

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

Keď hostiteľský agent preloží každý vrátený úsek, dokončite úlohu s kompletným `job` objektom vráteným `start_markdown_agent_translation`:

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

## Riešenie problémov

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Použite absolútnu cestu k Python vykonávaciemu súboru a konfiguráciu zo zdrojového checkoutu `["-m", "co_op_translator.mcp.server"]`. |
| The server is listed but translation fails. | Zavolajte `get_configuration_status` a potvrďte, že je dostupný poskytovateľ LLM. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Použite `start_markdown_agent_translation` / `finish_markdown_agent_translation` alebo ekvivalenty pre notebook, aby hostiteľský agent preložil úseky. |
| Image translation fails. | Potvrďte, že sú nastavené premenné Azure AI Vision a zavolajte `get_configuration_status`. |
| Repository translation does not write files. | Nastavte `dry_run=false` a `confirm_write=true` len po explicitnom schválení používateľom. |
| Changes to client config do not appear. | Reštartujte alebo znovu načítajte MCP klienta. |

## Bezpečnostné poznámky

- Volania MCP nástrojov sú riadené modelom hostiteľskej aplikácie, preto je preklad repozitára predvolene suchý beh (dry-run).
- Plný preklad repozitára môže vytvoriť, aktualizovať alebo odstrániť veľa súborov. Vyžadujte explicitné schválenie používateľa pred nastavením `confirm_write=true`.
- Nástroj stav konfigurácie nikdy nevráti API kľúče, koncové body ani iné tajné hodnoty.
- Preklad obrázkov vracia base64 obrázkové dáta. Veľké obrázky môžu spôsobiť veľké odpovede nástrojov.
- Nástroje asistované agentom vracajú zdrojové úseky a výzvy (prompts) hostiteľskému agentovi MCP. Používajte ich len s obsahom, ktorý je používateľ pohodlný poslať tomuto hostiteľskému agentovi modelu.