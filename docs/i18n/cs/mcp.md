# MCP server

Co-op Translator obsahuje server Model Context Protocol pro agenty, editory a klienty kompatibilní s MCP.

Pro výchozí lokální nastavení uživatelé nespouštějí samostatný server ručně. Nakonfigurují svůj MCP klient a klient automaticky spustí `co-op-translator-mcp` přes `stdio`, když potřebuje nástroje Co-op Translatoru.

Pokud se rozhodujete mezi CLI, Python API a MCP, začněte s [Vyberte svůj pracovní postup](workflows.md).

Použijte MCP, když by agent nebo editor měl přímo volat Co-op Translator:

| Cíl uživatele | Nástroje MCP |
| --- | --- |
| Přeložit jeden dokument Markdown, notebook nebo obrázek | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Přeložit obsah Markdownu nebo notebooku pomocí hostitelského agentního modelu | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Přepsat přeložené odkazy v Markdownu nebo notebooku po výběru výstupní cesty | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Přeložit celý repozitář podobně jako pomocí CLI | `run_translation`, `translate_project` |
| Zkontrolovat přeložený výstup bez přihlašovacích údajů LLM | `run_review` |
| Prohlédnout schopnosti a stav prostředí | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP server poskytuje rozhraní nad stejným veřejným Python API, které je popsáno v [Python API](api.md). Nástroje založené na poskytovateli používají stejné nakonfigurované poskytovatele jako CLI a Python API. Nástroje s asistencí agenta připraví části pro hostitelského agenta MCP k překladu a poté používají Co-op Translator k rekonstrukci finálního Markdownu nebo notebooku.

## Krok 1: Nainstalujte a nakonfigurujte Co-op Translator

Nainstalujte Co-op Translator do Python prostředí, které bude váš MCP klient používat:

```bash
pip install co-op-translator
```

Pro lokální vývoj z tohoto repozitáře nainstalujte balíček v editovatelném režimu:

```bash
pip install -e .
```

Zvolte režim překladu, který bude váš MCP klient používat:

| Režim | Použít pro | Přihlašovací údaje |
| --- | --- | --- |
| S podporou poskytovatele | Co-op Translator volá `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, nebo `run_translation`. | Překlad vyžaduje Azure OpenAI, OpenAI nebo Anthropic. Překlad obrázků navíc vyžaduje Azure AI Vision. |
| S asistencí agenta | Hostitelský agent MCP překládá části vrácené `start_markdown_agent_translation` nebo `start_notebook_agent_translation`. | Pro Markdown nebo části notebooku nejsou potřeba přihlašovací údaje poskytovatele LLM pro Co-op Translator. Překlad obrázků v agent-assisted režimu zatím není podporován. |

Pokud začínáte s překladem Markdownu nebo notebooku uvnitř agenta jako Codex nebo Claude Code, začněte v režimu s asistencí agenta. Režim s podporou poskytovatele použijte, když chcete, aby Co-op Translator sám volal vaše nakonfigurované poskytovatele, když překládáte obrázky, nebo když spouštíte překlad na úrovni repozitáře jako CLI.

Nakonfigurujte jednoho poskytovatele pro pracovní postupy s podporou poskytovatele:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Nebo OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Nebo Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Překlad obrázků s podporou poskytovatele navíc vyžaduje:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted režim v současnosti pokrývá Markdown a Markdown buňky v noteboocích. Překlad obrázků stále používá pipeline podporovanou poskytovatelem a vyžaduje Azure AI Vision pro OCR a renderování s ohledem na rozvržení.

## Krok 2: Nakonfigurujte svého MCP klienta

Pro běžné lokální nastavení přes `stdio` přidejte Co-op Translator do konfigurace vašeho MCP klienta. Klient proces automaticky spustí a zastaví.

Konfigurace pro nainstalovaný balíček:

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

Konfigurace pro zdrojový checkout na Windows:

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

Konfigurace pro zdrojový checkout na macOS nebo Linuxu:

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

Po změně konfigurace MCP klienta restartujte nebo znovu načtěte klienta, aby mohl objevit nový server.

## Krok 3: Ověřte server v klientovi

Požádejte MCP klienta, aby vypsal dostupné nástroje, nebo nejprve zavolejte některého z pomocných nástrojů pouze pro čtení:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Užitečné první kontroly:

| Nástroj | Co zkontrolovat |
| --- | --- |
| `get_api_overview` | Potvrzuje, že je server dosažitelný a zobrazuje dostupné pracovní postupy. |
| `list_supported_languages` | Potvrzuje, že lze načíst balíčkovaná data jazyků. |
| `get_configuration_status` | Potvrzuje dostupnost poskytovatelů LLM a Vision bez odhalení tajných údajů. |

## Krok 4: Vyberte pracovní postup

### Přeložit jednotlivé soubory nebo dokumenty

Použijte nástroje s podporou poskytovatele, když má MCP klient již obsah dokumentu nebo cestu k obrázku a Co-op Translator by měl volat nakonfigurované překladatelské poskytovatele.

Pro Markdown:

1. Zavolejte `translate_markdown_content` s `document`, `language_code` a volitelně `source_path`.
2. Pokud bude přeložený výsledek zapsán do výstupního rozvržení Co-op Translatoru, zavolejte `rewrite_markdown_paths`.
3. Nechte klienta zapsat nebo vrátit finální `content`.

Pro notebooky:

1. Zavolejte `translate_notebook_content` s JSON notebooku a `language_code`.
2. Zavolejte `rewrite_notebook_paths`, pokud je třeba upravit přeložené odkazy v notebooku pro cílovou cestu.
3. Zapište nebo vraťte finální JSON notebooku.

Pro obrázky:

1. Zavolejte `translate_image_content` s `image_path`, `language_code` a volitelně `root_dir` nebo `fast_mode`.
2. Přečtěte vrácené `data_base64` a `mime_type`.
3. Pokud je zadán `output_path`, přeložený obrázek je také uložen na tuto cestu.

Nástroje pro obsah neprovádějí objevování projektu, aktualizace metadat, prohlášení ani automatické přepisování cest. Pokud chcete, aby hostitelský agent překládal části Markdownu nebo notebooku bez pověření poskytovatele LLM pro Co-op Translator, použijte níže uvedený workflow s asistencí agenta.

### Překlad pomocí modelu hostitelského agenta

Použijte nástroje s asistencí agenta, když chcete, aby hostitelský agent MCP, například asistenti pro psaní kódu, vytvořil přeložený text místo konfigurace poskytovatele LLM pro Co-op Translator.

V chatovém MCP klientu obvykle nemusíte sami psát JSON nástrojů. Požádejte agenta, aby použil workflow s asistencí agenta:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Pro notebooky použijte stejný vzor:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Pokud váš MCP klient podporuje serverové prompt, použijte `agent_assisted_markdown_translation_prompt`, aby klient načetl stejné instrukce workflow.

Pro Markdown:

1. Zavolejte `start_markdown_agent_translation` s `document`, `language_code` a volitelně `source_path`.
2. V hostitelském agentovi přeložte každou vrácenou část podle jejího `prompt`.
3. Zavolejte `finish_markdown_agent_translation` s původním `job` a přeloženými částmi, používaje `chunk_id` a `translated_text`.
4. Pokud bude obsah zapsán do přeložené cílové cesty, zavolejte `rewrite_markdown_paths`.

Pro notebooky:

1. Zavolejte `start_notebook_agent_translation` s JSON notebooku a `language_code`.
2. Přeložte každou vrácenou část v hostitelském agentovi.
3. Zavolejte `finish_notebook_agent_translation` s původním `job` a přeloženými částmi.
4. Zavolejte `rewrite_notebook_paths`, pokud je třeba upravit cílové cesty přeložených odkazů v notebooku.

Nástroje s asistencí agenta nevolají nakonfigurovaného poskytovatele LLM z Co-op Translatoru. Za překlad vrácených částí je odpovědný hostitelský agent. Co-op Translator se stará o dělení Markdownu na části, zachování zástupných symbolů, rekonstrukci frontmatteru, nahrazování buněk v noteboocích a normalizaci po překladu.

### Přeložit celý repozitář

Použijte `run_translation`, když chce uživatel, aby se Co-op Translator choval jako CLI příkaz `translate`.

Překlad repozitáře má ve výchozím nastavení `dry_run=true`, aby si agent mohl před změnami souborů prohlédnout rozsah:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Výsledek `run_translation` zahrnuje pole `events` s verzovanými
progresovými událostmi `co-op.translation.event.v1`. MCP klienti by měli používat pole jako
`type`, `stage_key`, `completed`, `total` a `current_path` místo
parsování zachyceného textu z konzole. Předáte-li `json_events_path`, zapíšou se tyto události také
do NDJSON souboru.

Aby byly povoleny zápisy, volající musí nastavit jak `dry_run=false`, tak `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` je vystaven jako alias pro kompatibilitu k `run_translation`.

### Kontrola přeloženého výstupu

Použijte `run_review` pro deterministické kontroly, které nevyžadují pověření pro LLM nebo Vision:

!!! note "Beta"
    MCP zpřístupňuje beta API `run_review`. Je vhodné pro revizní pracovní toky pouze ke čtení, ale kontrolní testy a schémata problémů se mohou měnit.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Výsledek obsahuje zachycený textový výstup a strukturované shrnutí revize, pokud je dostupné.

## Ruční spuštění serveru

Ruční spuštění je určeno především pro debugování nebo pro transporty, které se chovají jako dlouho běžící servery.

Ladění výchozího stdio serveru:

```bash
co-op-translator-mcp
```

Spuštění ze zdrojového checkoutu:

```bash
python -m co_op_translator.mcp.server
```

Spusťte dlouho běžící HTTP nebo SSE server:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Pro integrace s lokálními editory a agenty upřednostněte konfiguraci `stdio` spravovanou klientem v Kroku 2.

## Nástroje

| Nástroj | Účel | Zapisuje soubory |
| --- | --- | --- |
| `translate_markdown_content` | Přeloží řetězec Markdownu. | Ne |
| `translate_notebook_content` | Přeloží Markdown buňky v JSONu notebooku. | Ne |
| `translate_image_content` | Přeloží text na jednom obrázku a vrátí base64 data obrázku. | Volitelné, pouze když je poskytnut `output_path` |
| `start_markdown_agent_translation` | Připraví části Markdownu pro hostitelského agenta, aby je přeložil bez pověření LLM Co-op Translatoru. | Ne |
| `finish_markdown_agent_translation` | Rekonstruuje Markdown z částí přeložených hostitelským agentem. | Ne |
| `start_notebook_agent_translation` | Připraví části Markdown buněk notebooku pro hostitelského agenta k překladu. | Ne |
| `finish_notebook_agent_translation` | Rekonstruuje JSON notebooku z částí přeložených hostitelským agentem. | Ne |
| `rewrite_markdown_paths` | Přepíše tělo Markdownu a cesty ve frontmatteru pro přeložený cíl. | Ne |
| `rewrite_notebook_paths` | Přepíše cesty uvnitř Markdown buněk v notebooku. | Ne |
| `run_translation` | Spustí překlad na úrovni projektu podobně jako CLI. | Ano, když `dry_run=false` a `confirm_write=true` |
| `translate_project` | Alias pro kompatibilitu k `run_translation`. | Ano, když `dry_run=false` a `confirm_write=true` |
| `run_review` | Spustí deterministické revizní kontroly. | Ne |
| `get_configuration_status` | Hlásí nakonfigurované poskytovatele LLM a Vision bez odhalení tajných údajů. | Ne |
| `list_supported_languages` | Vyjmenuje podporované cílové kódy jazyků. | Ne |
| `get_api_overview` | Popíše dostupné MCP pracovní postupy a nástroje. | Ne |

## Zdroje

| URI zdroje | Účel |
| --- | --- |
| `co-op://api` | JSON přehled pracovních postupů a nástrojů. |
| `co-op://supported-languages` | JSON seznam podporovaných kódů jazyků. |
| `co-op://configuration` | JSON souhrn dostupnosti poskytovatelů bez tajných údajů. |

## Prompty

| Prompt | Účel |
| --- | --- |
| `translate_markdown_document_prompt` | Provede MCP klienta procesem překladu obsahu plus volitelným přepisováním cest. |
| `agent_assisted_markdown_translation_prompt` | Provede MCP klienta procesem překladu Markdownu hostitelským agentem bez pověření poskytovatele LLM pro Co-op Translator. |
| `translate_repository_prompt` | Provede MCP klienta procesem překladu repozitáře, který začíná dry-runem. |

## Příklady pro kopírování a vložení

Přeložit obsah Markdownu:

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

Přepsat přeložené odkazy v Markdownu:

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

Přeložit Markdown pomocí modelu hostitelského agenta:

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

Poté, co hostitelský agent přeloží každou vrácenou část, dokončete úlohu s úplným objektem `job`, který vrací `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Náhled překladu repozitáře:

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

## Odstraňování problémů

| Problém | Co zkusit |
| --- | --- |
| MCP klient nemůže najít `co-op-translator-mcp`. | Použijte absolutní cestu k Python spustitelnému souboru a konfiguraci source checkout `["-m", "co_op_translator.mcp.server"]`. |
| Server je vypsán, ale překlad selže. | Zavolejte `get_configuration_status` a potvrďte, že je k dispozici poskytovatel LLM. |
| Chcete překlad Markdownu nebo notebooku bez pověření poskytovatele. | Použijte `start_markdown_agent_translation` / `finish_markdown_agent_translation` nebo ekvivalenty pro notebooky, aby hostitelský agent přeložil části. |
| Překlad obrázků selže. | Potvrďte, že jsou nastaveny proměnné Azure AI Vision a zavolejte `get_configuration_status`. |
| Překlad repozitáře nezapisuje soubory. | Nastavte `dry_run=false` a `confirm_write=true` pouze po výslovném schválení uživatele. |
| Změny v konfiguraci klienta se neprojeví. | Restartujte nebo znovu načtěte MCP klienta. |

## Bezpečnostní poznámky

- Volání nástrojů MCP jsou řízena modelem hostitelské aplikace, proto je překlad repozitáře ve výchozím nastavení v režimu dry-run.
- Kompletní překlad repozitáře může vytvořit, aktualizovat nebo odstranit mnoho souborů. Požadujte výslovné schválení uživatele před nastavením `confirm_write=true`.
- Nástroj pro stav konfigurace nikdy nevrací API klíče, endpointy ani jiné tajné hodnoty.
- Překlad obrázků vrací base64 data obrázku. Velké obrázky mohou produkovat velké odpovědi nástrojů.
- Nástroje s asistencí agenta vracejí zdrojové části a prompty hostiteli MCP. Používejte je pouze s obsahem, který je uživatel ochoten poslat tomuto hostitelskému agentnímu modelu.