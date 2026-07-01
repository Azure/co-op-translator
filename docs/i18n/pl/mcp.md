# Serwer MCP

Co-op Translator zawiera serwer Model Context Protocol dla agentów, edytorów i klientów zgodnych z MCP.

W domyślnej lokalnej konfiguracji użytkownicy nie uruchamiają osobnego serwera ręcznie. Konfigurują klienta MCP, a klient automatycznie uruchamia `co-op-translator-mcp` przez `stdio`, gdy potrzebuje narzędzi Co-op Translator.

Jeżeli zastanawiasz się między CLI, Python API i MCP, zacznij od [Wybierz swój przepływ pracy](workflows.md).

Używaj MCP, gdy agent lub edytor powinien wywołać Co-op Translator bezpośrednio:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Serwer MCP owija tę samą publiczną Python API udokumentowaną w [Python API](api.md). Narzędzia korzystające z dostawców używają tych samych skonfigurowanych dostawców co CLI i Python API. Narzędzia wspomagane przez agenta przygotowują fragmenty dla agenta-hostującego MCP do przetłumaczenia, a następnie używają Co-op Translator do odtworzenia końcowego Markdown lub notatnika.

## Step 1: Install and Configure Co-op Translator

Zainstaluj Co-op Translator w środowisku Pythona, którego będzie używać twój klient MCP:

```bash
pip install co-op-translator
```

Dla lokalnego rozwoju z tego repozytorium, zainstaluj pakiet w trybie edytowalnym:

```bash
pip install -e .
```

Wybierz tryb tłumaczenia, którego będzie używać twój klient MCP:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator wywołuje `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, lub `run_translation`. | Tłumaczenie Markdown i notatników wymaga Azure OpenAI lub OpenAI. Tłumaczenie obrazów wymaga także Azure AI Vision. |
| Agent-assisted | Agent-host MCP tłumaczy fragmenty zwrócone przez `start_markdown_agent_translation` lub `start_notebook_agent_translation`. | Dla fragmentów Markdown lub notatników nie są wymagane dane uwierzytelniające dostawcy LLM Co-op Translatora. Tłumaczenie obrazów nie jest jeszcze objęte trybem wspomaganym przez agenta. |

Jeśli zaczynasz od tłumaczenia Markdown lub notatnika wewnątrz agenta takiego jak Codex lub Claude Code, zacznij od trybu wspomaganego przez agenta. Użyj trybu z obsługą dostawcy, gdy chcesz, aby sam Co-op Translator wywoływał skonfigurowanych dostawców, gdy tłumaczysz obrazy, lub gdy uruchamiasz tłumaczenie na poziomie repozytorium jak w CLI.

Skonfiguruj dane uwierzytelniające dostawcy tylko dla przepływów opartych na dostawcy:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Dodatkowo tłumaczenie obrazów oparte na dostawcy wymaga:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## Step 2: Configure Your MCP Client

Dla normalnej lokalnej konfiguracji `stdio`, dodaj Co-op Translator do konfiguracji klienta MCP. Klient automatycznie uruchomi i zatrzyma proces.

Konfiguracja z zainstalowanego pakietu:

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

Konfiguracja z wypakowanego źródła na Windows:

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

Konfiguracja z wypakowanego źródła na macOS lub Linux:

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

Po zmianie konfiguracji klienta MCP, zrestartuj lub przeładuj klienta, aby mógł wykryć nowy serwer.

## Step 3: Verify the Server in the Client

Poproś klienta MCP o wypisanie dostępnych narzędzi lub wywołaj najpierw jeden z tylko do odczytu helperów:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Przydatne pierwsze kontrole:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Potwierdza, że serwer jest osiągalny i pokazuje dostępne przepływy pracy. |
| `list_supported_languages` | Potwierdza, że pakowane dane językowe można załadować. |
| `get_configuration_status` | Potwierdza dostępność dostawcy LLM i Vision bez ujawniania wartości tajnych. |

## Step 4: Choose a Workflow

### Translate Individual Files or Documents

Używaj narzędzi opartych na dostawcy, gdy klient MCP już posiada zawartość dokumentu lub ścieżkę do obrazu, a Co-op Translator ma wywołać skonfigurowanych dostawców.

Dla Markdown:

1. Wywołaj `translate_markdown_content` z `document`, `language_code` i opcjonalnie `source_path`.
2. Jeżeli przetłumaczony wynik będzie zapisany w układzie wyjściowym Co-op Translator, wywołaj `rewrite_markdown_paths`.
3. Pozwól klientowi zapisać lub zwrócić końcową `content`.

Dla notatników:

1. Wywołaj `translate_notebook_content` z JSON notatnika i `language_code`.
2. Wywołaj `rewrite_notebook_paths`, jeśli przetłumaczone linki w notatniku wymagają dostosowania do docelowej ścieżki.
3. Zapisz lub zwróć końcowy JSON notatnika.

Dla obrazów:

1. Wywołaj `translate_image_content` z `image_path`, `language_code` i opcjonalnym `root_dir` lub `fast_mode`.
2. Odczytaj zwrócone `data_base64` i `mime_type`.
3. Jeśli podano `output_path`, przetłumaczony obraz zostanie również zapisany pod tą ścieżką.

Narzędzia treści nie wykonują odkrywania projektu, aktualizacji metadanych, dodawania zastrzeżeń ani automatycznego przepisywania ścieżek. Jeśli chcesz, aby agent-host tłumaczył fragmenty Markdown lub notatnika bez danych uwierzytelniających dostawcy LLM Co-op Translator, użyj poniższego przepływu wspomaganego przez agenta.

### Translate with the Host Agent Model

Użyj narzędzi wspomaganych przez agenta, gdy chcesz, aby model agenta-hostującego, taki jak asystent kodowania, wygenerował przetłumaczony tekst zamiast konfigurować Azure OpenAI lub OpenAI dla Co-op Translator.

W kliencie MCP opartym na czacie zazwyczaj nie musisz pisać JSON narzędzia samodzielnie. Poproś agenta o użycie przepływu wspomaganego przez agenta:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Dla notatników użyj tego samego wzorca:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Jeśli twój klient MCP obsługuje server prompts, użyj `agent_assisted_markdown_translation_prompt`, aby klient załadował te same instrukcje przepływu pracy.

Dla Markdown:

1. Wywołaj `start_markdown_agent_translation` z `document`, `language_code` i opcjonalnie `source_path`.
2. Przetłumacz każdy zwrócony fragment w agencie-host, stosując się do `prompt` fragmentu.
3. Wywołaj `finish_markdown_agent_translation` z oryginalnym `job` i przetłumaczonymi fragmentami używając `chunk_id` i `translated_text`.
4. Jeśli zawartość zostanie zapisana do przetłumaczonej ścieżki docelowej, wywołaj `rewrite_markdown_paths`.

Dla notatników:

1. Wywołaj `start_notebook_agent_translation` z JSON notatnika i `language_code`.
2. Przetłumacz każdy zwrócony fragment w agencie-host.
3. Wywołaj `finish_notebook_agent_translation` z oryginalnym `job` i przetłumaczonymi fragmentami.
4. Wywołaj `rewrite_notebook_paths`, jeśli przetłumaczone linki w notatniku wymagają dostosowania do ścieżki docelowej.

Narzędzia wspomagane przez agenta nie wywołują Azure OpenAI ani OpenAI z poziomu Co-op Translator. Za przetłumaczenie zwróconych fragmentów odpowiada agent-host. Co-op Translator zajmuje się dzieleniem Markdown na fragmenty, zachowaniem zastępników, rekonstrukcją frontmatter, zastępowaniem komórek notatnika oraz normalizacją po tłumaczeniu.

### Translate an Entire Repository

Użyj `run_translation`, gdy użytkownik chce, aby Co-op Translator zachowywał się jak CLI `translate`.

Tłumaczenie repozytorium domyślnie ustawione jest na `dry_run=true`, aby agent mógł sprawdzić zakres przed wprowadzeniem zmian w plikach:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Aby zezwolić na zapisy, wywołujący musi ustawić zarówno `dry_run=false`, jak i `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` jest udostępnione jako alias kompatybilności dla `run_translation`.

### Review Translated Output

Użyj `run_review` dla deterministycznych kontroli, które nie wymagają danych uwierzytelniających LLM ani Vision:

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

Wynik zawiera przechwycony tekst wyjściowy oraz ustrukturyzowane podsumowanie przeglądu, jeśli jest dostępne.

## Manual Server Runs

Ręczne uruchomienia są głównie do debugowania lub dla transportów, które zachowują się jak długotrwałe serwery.

Debuguj domyślny serwer stdio:

```bash
co-op-translator-mcp
```

Uruchom z wypakowanego źródła:

```bash
python -m co_op_translator.mcp.server
```

Uruchom długotrwały serwer HTTP lub SSE:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Dla lokalnych integracji edytora i agenta, preferuj konfigurację `stdio` zarządzaną przez klienta opisaną w Kroku 2.

## Tools

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Tłumaczy ciąg Markdown. | No |
| `translate_notebook_content` | Tłumaczy komórki Markdown w JSON notatnika. | No |
| `translate_image_content` | Tłumaczy tekst na jednym obrazie i zwraca dane obrazu w base64. | Optional, only when `output_path` is provided |
| `start_markdown_agent_translation` | Przygotowuje fragmenty Markdown dla agenta-host, aby tłumaczył bez danych uwierzytelniających LLM Co-op Translator. | No |
| `finish_markdown_agent_translation` | Odtwarza Markdown z przetłumaczonych fragmentów agenta-host. | No |
| `start_notebook_agent_translation` | Przygotowuje fragmenty komórek Markdown notatnika dla agenta-host. | No |
| `finish_notebook_agent_translation` | Odtwarza JSON notatnika z przetłumaczonych fragmentów agenta-host. | No |
| `rewrite_markdown_paths` | Przepisuje ścieżki w treści Markdown i frontmatter dla przetłumaczonego celu. | No |
| `rewrite_notebook_paths` | Przepisuje ścieżki wewnątrz komórek Markdown notatnika. | No |
| `run_translation` | Uruchamia tłumaczenie na poziomie projektu jak CLI. | Yes when `dry_run=false` and `confirm_write=true` |
| `translate_project` | Alias kompatybilności dla `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | Uruchamia deterministyczne kontrole przeglądu. | No |
| `get_configuration_status` | Raportuje skonfigurowanych dostawców LLM i Vision bez ujawniania sekretów. | No |
| `list_supported_languages` | Wypisuje obsługiwane kody języków docelowych. | No |
| `get_api_overview` | Opisuje dostępne przepływy MCP i narzędzia. | No |

## Resources

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON z przeglądem przepływów pracy i narzędzi. |
| `co-op://supported-languages` | JSON z listą obsługiwanych kodów języków. |
| `co-op://configuration` | JSON z podsumowaniem dostępności dostawców bez sekretów. |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Prowadzi klienta MCP przez tłumaczenie treści oraz opcjonalne przepisywanie ścieżek. |
| `agent_assisted_markdown_translation_prompt` | Prowadzi klienta MCP przez tłumaczenie Markdown przez agenta-host bez danych uwierzytelniających dostawcy LLM Co-op Translator. |
| `translate_repository_prompt` | Prowadzi klienta MCP przez tłumaczenie repozytorium zaczynające się od dry-run. |

## Copy-Paste Examples

Tłumaczenie zawartości Markdown:

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

Przepisanie przetłumaczonych linków Markdown:

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

Tłumaczenie Markdown z użyciem modelu agenta-host:

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

Po tym jak agent-host przetłumaczy każdy zwrócony fragment, zakończ zadanie z pełnym obiektem `job` zwróconym przez `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Podgląd tłumaczenia repozytorium:

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
| The MCP client cannot find `co-op-translator-mcp`. | Use the absolute Python executable path and `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| The server is listed but translation fails. | Call `get_configuration_status` and confirm an LLM provider is available. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` or the notebook equivalents so the host agent translates the chunks. |
| Image translation fails. | Confirm Azure AI Vision variables are set and call `get_configuration_status`. |
| Repository translation does not write files. | Set `dry_run=false` and `confirm_write=true` only after explicit user approval. |
| Changes to client config do not appear. | Restart or reload the MCP client. |

## Safety Notes

- Wywołania narzędzi MCP są kontrolowane przez model w aplikacji hostującej, więc tłumaczenie repozytorium domyślnie wykonywane jest w trybie dry-run.
- Pełne tłumaczenie repozytorium może stworzyć, zaktualizować lub usunąć wiele plików. Wymagaj wyraźnej zgody użytkownika przed ustawieniem `confirm_write=true`.
- Narzędzie statusu konfiguracji nigdy nie zwraca kluczy API, punktów końcowych ani innych wartości tajnych.
- Tłumaczenie obrazów zwraca dane obrazu w base64. Duże obrazy mogą generować duże odpowiedzi narzędzi.
- Narzędzia wspomagane przez agenta zwracają źródłowe fragmenty i podpowiedzi do agenta-host MCP. Używaj ich tylko z zawartością, którą użytkownik zgadza się wysłać do tego modelu agenta-host.