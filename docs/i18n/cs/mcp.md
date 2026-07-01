# Server MCP

Co-op Translator obsahuje server Model Context Protocol pro agenty, editory a klienty kompatibilní s MCP.

Pro výchozí lokální nastavení uživatelé obvykle nespouští samostatný server ručně. Nakonfigurují svého MCP klienta a klient automaticky spustí `co-op-translator-mcp` přes `stdio`, když bude potřebovat nástroje Co-op Translatoru.

Pokud se rozhodujete mezi CLI, Python API a MCP, začněte s [Vyberte svůj pracovní postup](workflows.md).

Použijte MCP, když by agent nebo editor měl volat Co-op Translator přímo:

| Cíl uživatele | Nástroje MCP |
| --- | --- |
| Přeložit jeden Markdown dokument, notebook nebo obrázek | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Přeložit obsah Markdownu nebo notebooku pomocí hostitelského modelu agenta | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Přepsat přeložené odkazy v Markdownu nebo notebooku po volbě výstupní cesty | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Přeložit celé úložiště podobně jako CLI | `run_translation`, `translate_project` |
| Zkontrolovat přeložený výstup bez pověření LLM | `run_review` |
| Prohlédnout schopnosti a stav prostředí | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Server MCP obaluje stejné veřejné Python API dokumentované v [Python API](api.md). Nástroje závislé na poskytovateli používají stejné nakonfigurované poskytovatele jako CLI a Python API. Nástroje asistované agentem připraví části pro MCP hostitelského agenta k překladu a poté použijí Co-op Translator ke zrekonstruování finálního Markdownu nebo notebooku.

## Krok 1: Nainstalujte a nakonfigurujte Co-op Translator

Nainstalujte Co-op Translator do Python prostředí, které bude používat váš MCP klient:

```bash
pip install co-op-translator
```

Pro lokální vývoj z tohoto repozitáře nainstalujte balíček v režimu editable:

```bash
pip install -e .
```

Vyberte režim překladu, který bude váš MCP klient používat:

| Režim | Použít pro | Přihlašovací údaje |
| --- | --- | --- |
| S poskytovatelem | Co-op Translator volá `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` nebo `run_translation`. | Překlad Markdownu a notebooků vyžaduje Azure OpenAI nebo OpenAI. Překlad obrázků také vyžaduje Azure AI Vision. |
| Asistovaný agentem | MCP hostitelský agent překládá části vrácené `start_markdown_agent_translation` nebo `start_notebook_agent_translation`. | Pro části Markdownu nebo notebooku nejsou vyžadována pověření LLM poskytovatele Co-op Translatoru. Režim asistovaný agentem zatím nepokrývá překlad obrázků. |

Pokud začínáte s překladem Markdownu nebo notebooku uvnitř agenta, jako jsou Codex nebo Claude Code, začněte v režimu asistovaném agentem. Použijte režim s poskytovatelem, když chcete, aby Co-op Translator sám volal vaše nakonfigurované poskytovatele, když překládáte obrázky, nebo když provádíte překlad na úrovni repozitáře, jako u CLI.

Konfigurujte přihlašovací údaje poskytovatele pouze pro pracovní postupy závislé na poskytovateli:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Pro překlad obrázků závislý na poskytovateli je navíc potřeba:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Režim asistovaný agentem v současné době pokrývá Markdown a Markdown buňky v noteboocích. Překlad obrázků stále používá pipeline závislou na poskytovateli a vyžaduje Azure AI Vision pro OCR a vykreslování s ohledem na rozložení.

## Krok 2: Nakonfigurujte svého MCP klienta

Pro běžné lokální `stdio` nastavení přidejte Co-op Translator do konfigurace vašeho MCP klienta. Klient automaticky proces spustí a zastaví.

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

Konfigurace ze zdrojového checkoutu na Windows:

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

Konfigurace ze zdrojového checkoutu na macOS nebo Linuxu:

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

Požádejte MCP klienta, aby vypsal dostupné nástroje, nebo nejprve zavolejte jednoho z pomocných nástrojů pouze pro čtení:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Užitečné první kontroly:

| Nástroj | Co zkontrolovat |
| --- | --- |
| `get_api_overview` | Potvrzuje, že je server dostupný a zobrazuje dostupné pracovní postupy. |
| `list_supported_languages` | Potvrzuje, že lze načíst zabalená jazyková data. |
| `get_configuration_status` | Potvrzuje dostupnost LLM a Vision poskytovatelů, aniž by odhaloval tajné hodnoty. |

## Krok 4: Zvolte pracovní postup

### Přeložit jednotlivé soubory nebo dokumenty

Použijte nástroje závislé na poskytovateli, když má MCP klient již obsah dokumentu nebo cestu k obrázku a Co-op Translator má volat nakonfigurované překladové poskytovatele.

Pro Markdown:

1. Zavolejte `translate_markdown_content` s `document`, `language_code` a volitelně `source_path`.
2. Pokud bude přeložený výsledek zapsán do výstupního rozvržení Co-op Translatoru, zavolejte `rewrite_markdown_paths`.
3. Nechte klienta zapsat nebo vrátit finální `content`.

Pro notebooky:

1. Zavolejte `translate_notebook_content` s JSONem notebooku a `language_code`.
2. Zavolejte `rewrite_notebook_paths`, pokud je třeba upravit přeložené odkazy notebooku pro cílovou cestu.
3. Zapište nebo vraťte finální JSON notebooku.

Pro obrázky:

1. Zavolejte `translate_image_content` s `image_path`, `language_code` a volitelně `root_dir` nebo `fast_mode`.
2. Přečtěte vrácené `data_base64` a `mime_type`.
3. Pokud je poskytnuta `output_path`, je přeložený obrázek také uložen na tuto cestu.

Nástroje pro obsah neprovádějí objevování projektu, aktualizace metadat, upozornění ani automatické přepisování cest. Pokud chcete, aby hostitelský agent překládal části Markdownu nebo notebooku bez pověření LLM poskytovatele Co-op Translatoru, použijte níže uvedený pracovní postup asistovaný agentem.

### Přeložit pomocí hostitelského modelu agenta

Použijte nástroje asistované agentem, když chcete, aby MCP hostitelský agent, jako je asistent pro kódování, vytvořil přeložený text místo konfigurace Azure OpenAI nebo OpenAI pro Co-op Translator.

V chatovém MCP klientu obvykle nemusíte psát JSON nástrojů sami. Požádejte agenta, aby použil pracovní postup asistovaný agentem:

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

Pokud váš MCP klient podporuje server prompts, použijte `agent_assisted_markdown_translation_prompt`, aby klient načetl stejné instrukce pracovního postupu.

Pro Markdown:

1. Zavolejte `start_markdown_agent_translation` s `document`, `language_code` a volitelně `source_path`.
2. Přeložte každou vrácenou část v hostitelském agentovi podle části `prompt`.
3. Zavolejte `finish_markdown_agent_translation` s původní `job` a přeloženými částmi použitím `chunk_id` a `translated_text`.
4. Pokud bude obsah zapsán do přeložené cílové cesty, zavolejte `rewrite_markdown_paths`.

Pro notebooky:

1. Zavolejte `start_notebook_agent_translation` s JSONem notebooku a `language_code`.
2. Přeložte každou vrácenou část v hostitelském agentovi.
3. Zavolejte `finish_notebook_agent_translation` s původní `job` a přeloženými částmi.
4. Zavolejte `rewrite_notebook_paths`, pokud je třeba upravit odkazy v přeloženém notebooku pro cílovou cestu.

Nástroje asistované agentem nevolají Azure OpenAI nebo OpenAI z Co-op Translatoru. Hostitelský agent je zodpovědný za překládání vrácených částí. Co-op Translator se stará o dělení Markdownu na části, zachování zástupných symbolů, rekonstrukci frontmatteru, nahrazení buněk notebooku a post-translation normalizaci.

### Přeložit celé úložiště

Použijte `run_translation`, když uživatel chce, aby se Co-op Translator choval jako CLI `translate`.

Překlad repozitáře má ve výchozím nastavení `dry_run=true`, aby si agent mohl prohlédnout rozsah před provedením změn souborů:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

K povolení zápisů musí volající nastavit současně `dry_run=false` a `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` je vystaveno jako kompatibilní alias pro `run_translation`.

### Zkontrolovat přeložený výstup

Použijte `run_review` pro deterministické kontroly, které nevyžadují pověření LLM nebo Vision:

!!! note "Beta"
    MCP vystavuje beta API `run_review`. Je bezpečné pro pracovní postupy pouze ke čtení, ale kontroly přezkumu a schémata problémů se mohou vyvíjet.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Výsledek obsahuje zachycený textový výstup a strukturované shrnutí přezkumu, pokud je k dispozici.

## Ruční spuštění serveru

Ruční spuštění se používá hlavně pro ladění nebo pro transporty, které se chovají jako dlouho běžící servery.

Ladění výchozího stdio serveru:

```bash
co-op-translator-mcp
```

Spuštění ze zdrojového checkoutu:

```bash
python -m co_op_translator.mcp.server
```

Spuštění dlouho běžícího HTTP nebo SSE serveru:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Pro lokální integrace editorů a agentů preferujte konfiguraci `stdio` spravovanou klientem v Kroku 2.

## Nástroje

| Nástroj | Účel | Zapisuje soubory |
| --- | --- | --- |
| `translate_markdown_content` | Přeložit řetězec Markdown. | Ne |
| `translate_notebook_content` | Přeložit Markdown buňky v JSONu notebooku. | Ne |
| `translate_image_content` | Přeložit text v jednom obrázku a vrátit base64 obrazová data. | Volitelně, pouze když je poskytnuta `output_path` |
| `start_markdown_agent_translation` | Připravit části Markdownu pro hostitelského agenta k překladu bez pověření LLM Co-op Translatoru. | Ne |
| `finish_markdown_agent_translation` | Zrekonstruovat Markdown z přeložených částí hostitelského agenta. | Ne |
| `start_notebook_agent_translation` | Připravit části Markdown buněk notebooku pro hostitelského agenta k překladu. | Ne |
| `finish_notebook_agent_translation` | Zrekonstruovat JSON notebooku z přeložených částí hostitelského agenta. | Ne |
| `rewrite_markdown_paths` | Přepsat cesty v těle Markdownu a frontmatteru pro přeložený cíl. | Ne |
| `rewrite_notebook_paths` | Přepsat cesty uvnitř Markdown buněk v notebooku. | Ne |
| `run_translation` | Spustit překlad projektu jako CLI. | Ano, když `dry_run=false` a `confirm_write=true` |
| `translate_project` | Kompatibilní alias pro `run_translation`. | Ano, když `dry_run=false` a `confirm_write=true` |
| `run_review` | Spustit deterministické kontroly přezkumu. | Ne |
| `get_configuration_status` | Nahlásit nakonfigurované LLM a Vision poskytovatele bez odhalení tajných údajů. | Ne |
| `list_supported_languages` | Vypsat podporované cílové kódy jazyků. | Ne |
| `get_api_overview` | Popsat dostupné MCP pracovní postupy a nástroje. | Ne |

## Zdroje

| URI zdroje | Účel |
| --- | --- |
| `co-op://api` | JSON přehled pracovních postupů a nástrojů. |
| `co-op://supported-languages` | JSON seznam podporovaných kódů jazyků. |
| `co-op://configuration` | JSON souhrn dostupnosti poskytovatelů bez tajných údajů. |

## Prompty

| Prompt | Účel |
| --- | --- |
| `translate_markdown_document_prompt` | Navigovat MCP klienta přes překlad obsahu a volitelné přepisování cest. |
| `agent_assisted_markdown_translation_prompt` | Navigovat MCP klienta přes překládání Markdownu hostitelským agentem bez pověření LLM Co-op Translatoru. |
| `translate_repository_prompt` | Navigovat MCP klienta přes překlad repozitáře s nejprve suchým během (dry-run). |

## Ukázky pro kopírování a vložení

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

Přeložit Markdown s hostitelským modelem agenta:

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

Poté, co hostitelský agent přeloží každou vrácenou část, dokončete úlohu s kompletním objektem `job` vráceným `start_markdown_agent_translation`:

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

## Řešení problémů

| Problém | Co zkusit |
| --- | --- |
| MCP klient nemůže najít `co-op-translator-mcp`. | Použijte absolutní cestu k Pythonu a konfiguraci zdrojového checkoutu `["-m", "co_op_translator.mcp.server"]`. |
| Server je vypsán, ale překlad selže. | Zavolejte `get_configuration_status` a potvrďte, že je dostupný poskytovatel LLM. |
| Chcete překlad Markdownu nebo notebooku bez klíčů Azure OpenAI/OpenAI. | Použijte `start_markdown_agent_translation` / `finish_markdown_agent_translation` nebo ekvivalenty pro notebook, aby části přeložil hostitelský agent. |
| Překlad obrázků selže. | Potvrďte, že jsou nastaveny proměnné Azure AI Vision a zavolejte `get_configuration_status`. |
| Překlad repozitáře nezapisuje soubory. | Nastavte `dry_run=false` a `confirm_write=true` pouze po výslovném schválení uživatelem. |
| Změny konfigurace klienta se neprojeví. | Restartujte nebo znovu načtěte MCP klienta. |

## Bezpečnostní poznámky

- Volání nástrojů MCP jsou řízena modelem hostitelské aplikace, takže překlad repozitáře je ve výchozím nastavení suchý běh.
- Plný překlad repozitáře může vytvořit, aktualizovat nebo odstranit mnoho souborů. Požadujte výslovné schválení uživatele před nastavením `confirm_write=true`.
- Nástroj stavu konfigurace nikdy nevrací API klíče, koncové body ani jiné tajné hodnoty.
- Překlad obrázků vrací base64 obrazová data. Velké obrázky mohou vytvořit rozsáhlé odpovědi nástrojů.
- Nástroje asistované agentem vracejí zdrojové části a promptů hostiteli MCP. Používejte je pouze s obsahem, který je uživatel ochoten odeslat tomuto hostitelskému agentnímu modelu.