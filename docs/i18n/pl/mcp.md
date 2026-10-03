# Serwer MCP

Co-op Translator zawiera serwer Model Context Protocol dla agentów, edytorów i klientów zgodnych z MCP.

W domyślnej konfiguracji lokalnej użytkownicy nie uruchamiają oddzielnego serwera ręcznie. Konfigurują swojego klienta MCP, a klient automatycznie uruchamia `co-op-translator-mcp` przez `stdio`, gdy potrzebuje narzędzi Co-op Translator.

Jeśli zastanawiasz się między CLI, Python API i MCP, zacznij od [Choose Your Workflow](workflows.md).

Użyj MCP, gdy agent lub edytor powinien wywoływać Co-op Translator bezpośrednio:

| Cel użytkownika | Narzędzia MCP |
| --- | --- |
| Przetłumaczyć jeden dokument Markdown, notebook lub obraz | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Przetłumaczyć zawartość Markdown lub notebooka używając modelu agenta hosta | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Przepisać przetłumaczone linki w Markdownie lub notebooku po wybraniu ścieżki wyjściowej | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Przetłumaczyć całe repozytorium jak CLI | `run_translation`, `translate_project` |
| Przejrzeć przetłumaczone wyniki bez poświadczeń LLM | `run_review` |
| Sprawdzić możliwości i status środowiska | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Serwer MCP udostępnia ten sam publiczny interfejs API Pythona udokumentowany w [Python API](api.md). Narzędzia korzystające z dostawców używają tych samych skonfigurowanych providerów co CLI i API Pythona. Narzędzia wspierane przez agenta przygotowują fragmenty do przetłumaczenia przez agenta hosta MCP, a następnie używają Co-op Translator do odbudowy końcowego Markdowna lub notebooka.

## Krok 1: Zainstaluj i skonfiguruj Co-op Translator

Zainstaluj Co-op Translator w środowisku Pythona, którego będzie używać Twój klient MCP:

```bash
pip install co-op-translator
```

Dla lokalnego rozwoju z tego repozytorium zainstaluj pakiet w trybie edytowalnym:

```bash
pip install -e .
```

Wybierz tryb tłumaczenia, którego będzie używał klient MCP:

| Tryb | Użyj tego do | Poświadczenia |
| --- | --- | --- |
| Provider-backed | Co-op Translator wywołuje `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` lub `run_translation`. | Do tłumaczenia wymagane są Azure OpenAI, OpenAI lub Anthropic. Tłumaczenie obrazów dodatkowo wymaga Azure AI Vision. |
| Agent-assisted | Agent hosta MCP tłumaczy fragmenty zwrócone przez `start_markdown_agent_translation` lub `start_notebook_agent_translation`. | Nie są wymagane poświadczenia dostawcy LLM Co-op Translator dla fragmentów Markdown lub notebooka. Tłumaczenie obrazów nie jest jeszcze objęte trybem agent-assisted. |

Jeśli zaczynasz od tłumaczenia Markdowna lub notebooka wewnątrz agenta takiego jak Codex lub Claude Code, zacznij od trybu agent-assisted. Użyj trybu provider-backed, gdy chcesz, aby Co-op Translator sam wywoływał skonfigurowanych dostawców, gdy tłumaczysz obrazy lub gdy uruchamiasz tłumaczenie na poziomie repozytorium podobne do CLI.

Skonfiguruj jednego dostawcę dla przepływów z obsługą dostawcy:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Lub OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Lub Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Tłumaczenie obrazów z obsługą dostawcy dodatkowo wymaga:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Tryb agent-assisted obecnie obejmuje Markdown i komórki Markdown w notebookach. Tłumaczenie obrazów nadal korzysta z pipeline'u dla obrazów z obsługą dostawcy i wymaga Azure AI Vision do OCR i renderowania uwzględniającego układ.

## Krok 2: Skonfiguruj swojego klienta MCP

Dla standardowej lokalnej konfiguracji `stdio` dodaj Co-op Translator do konfiguracji klienta MCP. Klient automatycznie uruchomi i zatrzyma proces.

Konfiguracja dla zainstalowanego pakietu:

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

Konfiguracja checkoutu źródła w systemie Windows:

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

Konfiguracja checkoutu źródła na macOS lub Linuxie:

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

## Krok 3: Zweryfikuj serwer w kliencie

Poproś klienta MCP o wypisanie dostępnych narzędzi lub najpierw wywołaj jedno z pomocniczych narzędzi tylko do odczytu:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Przydatne pierwsze kontrole:

| Narzędzie | Co sprawdzić |
| --- | --- |
| `get_api_overview` | Potwierdza, że serwer jest osiągalny i pokazuje dostępne przepływy pracy. |
| `list_supported_languages` | Potwierdza, że pakowane dane językowe można załadować. |
| `get_configuration_status` | Potwierdza dostępność dostawców LLM i Vision bez ujawniania wartości sekretów. |

## Krok 4: Wybierz przepływ pracy

### Tłumaczenie pojedynczych plików lub dokumentów

Użyj narzędzi z obsługą dostawcy, gdy klient MCP ma już zawartość dokumentu lub ścieżkę obrazu i Co-op Translator powinien wywołać skonfigurowanych dostawców tłumaczeń.

Dla Markdowna:

1. Wywołaj `translate_markdown_content` z `document`, `language_code` i opcjonalnie `source_path`.
2. Jeśli przetłumaczony wynik będzie zapisany do layoutu wyjściowego Co-op Translator, wywołaj `rewrite_markdown_paths`.
3. Pozwól klientowi zapisać lub zwrócić ostateczną wartość `content`.

Dla notebooków:

1. Wywołaj `translate_notebook_content` z JSONem notebooka i `language_code`.
2. Wywołaj `rewrite_notebook_paths`, jeśli przetłumaczone linki w notebooku wymagają dostosowania do ścieżki docelowej.
3. Zapisz lub zwróć ostateczny JSON notebooka.

Dla obrazów:

1. Wywołaj `translate_image_content` z `image_path`, `language_code` oraz opcjonalnie `root_dir` lub `fast_mode`.
2. Odczytaj zwrócone `data_base64` i `mime_type`.
3. Jeśli podano `output_path`, przetłumaczony obraz zostanie również zapisany pod tą ścieżką.

Narzędzia do obsługi zawartości nie wykonują wykrywania projektów, aktualizacji metadanych, komunikatów ani automatycznego przepisywania ścieżek. Jeśli chcesz, aby agent hosta tłumaczył fragmenty Markdown lub notebooka bez poświadczeń dostawcy LLM Co-op Translator, użyj poniższego przepływu agent-assisted.

### Tłumaczenie z użyciem modelu agenta hosta

Użyj narzędzi agent-assisted, gdy chcesz, aby agent hosta MCP, na przykład asystent kodowania, wygenerował przetłumaczony tekst zamiast konfigurować dostawcę LLM dla Co-op Translator.

W kliencie MCP opartym na czacie zazwyczaj nie musisz samodzielnie pisać JSONa narzędzia. Poproś agenta o użycie przepływu agent-assisted:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Dla notebooków użyj tego samego wzorca:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Jeśli Twój klient MCP obsługuje server prompts, użyj `agent_assisted_markdown_translation_prompt`, aby klient załadował te same instrukcje przepływu pracy.

Dla Markdowna:

1. Wywołaj `start_markdown_agent_translation` z `document`, `language_code` i opcjonalnie `source_path`.
2. Przetłumacz każdy zwrócony fragment w agencie hosta, postępując zgodnie z `prompt` fragmentu.
3. Wywołaj `finish_markdown_agent_translation` z oryginalnym `job` i przetłumaczonymi fragmentami używając `chunk_id` i `translated_text`.
4. Jeśli zawartość będzie zapisana do przetłumaczonej ścieżki docelowej, wywołaj `rewrite_markdown_paths`.

Dla notebooków:

1. Wywołaj `start_notebook_agent_translation` z JSONem notebooka i `language_code`.
2. Przetłumacz każdy zwrócony fragment w agencie hosta.
3. Wywołaj `finish_notebook_agent_translation` z oryginalnym `job` i przetłumaczonymi fragmentami.
4. Wywołaj `rewrite_notebook_paths`, jeśli przetłumaczone linki w notebooku wymagają dostosowania ścieżki docelowej.

Narzędzia agent-assisted nie wywołują skonfigurowanego dostawcy LLM z poziomu Co-op Translator. Za tłumaczenie zwróconych fragmentów odpowiada agent hosta. Co-op Translator zajmuje się dzieleniem Markdowna na fragmenty, zachowaniem symboli zastępczych, odbudową frontmatter, zastępowaniem komórek w notebooku oraz normalizacją po tłumaczeniu.

### Tłumaczenie całego repozytorium

Użyj `run_translation`, gdy użytkownik chce, aby Co-op Translator zachowywał się jak CLI `translate`.

Tłumaczenie repozytorium ma domyślnie ustawione `dry_run=true`, aby agent mógł sprawdzić zakres przed zmianami plików:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Wynik `run_translation` zawiera tablicę `events` z wersjonowanymi
`co-op.translation.event.v1` zdarzeniami postępu. Klienci MCP powinni używać pól takich
jak `type`, `stage_key`, `completed`, `total` i `current_path` zamiast
parsowania przechwyconego tekstu z konsoli. Przekaż `json_events_path`, aby także zapisać te zdarzenia
do pliku NDJSON.

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

`translate_project` jest udostępnione jako alias zgodności dla `run_translation`.

### Przegląd przetłumaczonych wyników

Użyj `run_review` do deterministycznych kontroli, które nie wymagają poświadczeń LLM lub Vision:

!!! note "Beta"
    MCP udostępnia beta-API `run_review`. Jest bezpieczne dla przepływów przeglądania tylko do odczytu, ale kontrole przeglądu i schematy problemów mogą ewoluować.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Wynik zawiera przechwycony tekst wyjścia oraz ustrukturyzowane podsumowanie przeglądu, gdy jest dostępne.

## Ręczne uruchamianie serwera

Ręczne uruchomienia są przeznaczone głównie do debugowania lub dla transportów, które zachowują się jak długo działające serwery.

Debuguj domyślny serwer stdio:

```bash
co-op-translator-mcp
```

Uruchom z checkoutu źródła:

```bash
python -m co_op_translator.mcp.server
```

Uruchom długo działający serwer HTTP lub SSE:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Dla lokalnych integracji edytora i agenta preferuj zarządzaną przez klienta konfigurację `stdio` z Kroku 2.

## Narzędzia

| Narzędzie | Przeznaczenie | Zapisuje pliki |
| --- | --- | --- |
| `translate_markdown_content` | Tłumaczy tekst Markdown. | Nie |
| `translate_notebook_content` | Tłumaczy komórki Markdown w JSONie notebooka. | Nie |
| `translate_image_content` | Tłumaczy tekst na obrazie i zwraca dane obrazu w base64. | Opcjonalnie, tylko gdy podano `output_path` |
| `start_markdown_agent_translation` | Przygotowuje fragmenty Markdown dla agenta hosta do przetłumaczenia bez poświadczeń LLM Co-op Translator. | Nie |
| `finish_markdown_agent_translation` | Odbudowuje Markdown z fragmentów przetłumaczonych przez agenta hosta. | Nie |
| `start_notebook_agent_translation` | Przygotowuje fragmenty komórek Markdown notebooka dla agenta hosta do przetłumaczenia. | Nie |
| `finish_notebook_agent_translation` | Odbudowuje JSON notebooka z fragmentów przetłumaczonych przez agenta hosta. | Nie |
| `rewrite_markdown_paths` | Przepisuje ścieżki w treści Markdown i frontmatter dla przetłumaczonej ścieżki docelowej. | Nie |
| `rewrite_notebook_paths` | Przepisuje ścieżki wewnątrz komórek Markdown w notebooku. | Nie |
| `run_translation` | Uruchamia tłumaczenie na poziomie projektu jak CLI. | Tak, gdy `dry_run=false` i `confirm_write=true` |
| `translate_project` | Alias kompatybilnościowy dla `run_translation`. | Tak, gdy `dry_run=false` i `confirm_write=true` |
| `run_review` | Uruchamia deterministyczne kontrole przeglądu. | Nie |
| `get_configuration_status` | Raportuje skonfigurowanych dostawców LLM i Vision bez ujawniania sekretów. | Nie |
| `list_supported_languages` | Wypisuje obsługiwane kody języków docelowych. | Nie |
| `get_api_overview` | Opisuje dostępne przepływy pracy i narzędzia MCP. | Nie |

## Zasoby

| URI zasobu | Przeznaczenie |
| --- | --- |
| `co-op://api` | JSON-owy przegląd przepływów pracy i narzędzi. |
| `co-op://supported-languages` | JSON-owa lista obsługiwanych kodów języków. |
| `co-op://configuration` | JSON-owe podsumowanie dostępności dostawców bez sekretów. |

## Prompty

| Prompt | Przeznaczenie |
| --- | --- |
| `translate_markdown_document_prompt` | Przeprowadza klienta MCP przez tłumaczenie zawartości oraz opcjonalne przepisywanie ścieżek. |
| `agent_assisted_markdown_translation_prompt` | Przeprowadza klienta MCP przez tłumaczenie Markdown przez agenta hosta bez poświadczeń dostawcy LLM Co-op Translator. |
| `translate_repository_prompt` | Przeprowadza klienta MCP przez tłumaczenie repozytorium rozpoczynające się od dry-run. |

## Przykłady do kopiuj-wklej

Przetłumacz zawartość Markdown:

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

Przepisz przetłumaczone linki Markdown:

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

Tłumacz Markdown przy użyciu modelu agenta hosta:

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

Po tym, jak agent hosta przetłumaczy każdy zwrócony fragment, zakończ zadanie używając kompletnego obiektu `job` zwróconego przez `start_markdown_agent_translation`:

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

## Rozwiązywanie problemów

| Problem | Co spróbować |
| --- | --- |
| Klient MCP nie może znaleźć `co-op-translator-mcp`. | Użyj absolutnej ścieżki do interpretera Pythona oraz konfiguracji checkoutu źródła `["-m", "co_op_translator.mcp.server"]`. |
| Serwer jest wymieniony, ale tłumaczenie nie powiodło się. | Wywołaj `get_configuration_status` i potwierdź, że dostawca LLM jest dostępny. |
| Chcesz tłumaczyć Markdown lub notebook bez poświadczeń dostawcy. | Użyj `start_markdown_agent_translation` / `finish_markdown_agent_translation` lub odpowiedników dla notebooków, aby agent hosta tłumaczył fragmenty. |
| Tłumaczenie obrazu nie powiodło się. | Potwierdź, że zmienne Azure AI Vision są ustawione i wywołaj `get_configuration_status`. |
| Tłumaczenie repozytorium nie zapisuje plików. | Ustaw `dry_run=false` i `confirm_write=true` tylko po wyraźnej zgodzie użytkownika. |
| Zmiany w konfiguracji klienta nie pojawiają się. | Zrestartuj lub przeładuj klienta MCP. |

## Uwagi dotyczące bezpieczeństwa

- Wywołania narzędzi MCP są sterowane przez model w aplikacji hosta, dlatego tłumaczenie repozytorium domyślnie działa w trybie podglądu (dry-run).
- Pełne tłumaczenie repozytorium może tworzyć, aktualizować lub usuwać wiele plików. Wymagaj wyraźnej zgody użytkownika przed ustawieniem `confirm_write=true`.
- Narzędzie statusu konfiguracji nigdy nie zwraca kluczy API, endpointów ani innych wartości sekretów.
- Tłumaczenie obrazów zwraca dane obrazu w base64. Duże obrazy mogą generować obszerne odpowiedzi narzędzi.
- Narzędzia agent-assisted zwracają fragmenty źródłowe i prompt do agenta hosta MCP. Używaj ich tylko z zawartością, którą użytkownik zgadza się wysłać do modelu agenta hosta.