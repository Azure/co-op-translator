# Wybierz swój przepływ pracy

Co-op Translator można używać na trzy sposoby: CLI, Python API i serwer MCP. Udostępniają te same możliwości tłumaczeniowe, ale każdy z nich pasuje do innego przepływu pracy.

Skorzystaj z tej strony, gdy decydujesz, od czego zacząć.

**Jeśli edytujesz tłumaczenia ręcznie:** domyślne workflowy CLI i Actions ponownie tłumaczą zmienione pliki źródłowe w całości, więc twoje sformułowania w tych plikach mogą zostać nadpisane. Przejrzyj diff przed zaakceptowaniem aktualizacji. Aby zachować blokową strukturę Markdown zaakceptowanych zmian, użyj opcjonalnego [dostawcy stanu tłumaczeń API Pythona](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Szybka decyzja

| Jeśli chcesz... | Użyj | Zacznij tutaj |
| --- | --- | --- |
| Przetłumaczyć lub przejrzeć repozytorium z terminala | CLI | [Dokumentacja CLI](cli.md) |
| Dodać tłumaczenie do skryptu Pythona, usługi, notatnika lub zadania CI | Python API | [Python API](api.md) |
| Pozwolić agentowi, edytorowi lub klientowi zgodnemu z MCP przetłumaczyć zawartość dla Ciebie | MCP Server | [MCP Server](mcp.md) |
| Przetłumaczyć pojedynczy dokument Markdown, notatnik lub obraz, który Twoja aplikacja już załadowała | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Przetłumaczyć całe repozytorium ze standardowymi folderami wyjściowymi i metadanymi | CLI or `run_translation` | [Dokumentacja CLI](cli.md) or [Python API](api.md) |

## Użyj CLI gdy

Wybierz CLI, gdy osoba lub zadanie CI uruchamia tłumaczenie repozytorium z powłoki.

CLI to najprostsza droga, gdy chcesz, aby Co-op Translator wykrył pliki projektu, utworzył przetłumaczone wyniki, zachował układ projektu, zaktualizował metadane i uruchomił polecenia przeglądu.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Ten przykład tłumaczy Markdown i notebooki. Dodaj `-img` dopiero po skonfigurowaniu [Azure AI Vision](configuration.md#azure-ai-vision). Jeśli chcesz najpierw uruchomić jedynie Markdown, postępuj zgodnie z [Twoim pierwszym tłumaczeniem](first-translation.md).

Dobrym wyborem, gdy:

- Tłumaczysz repozytorium z terminala.
- Chcesz powtarzalnego polecenia dla workflowów CI lub wydania.
- Chcesz wbudowanego wykrywania projektu, ścieżek wyjściowych, metadanych, sprzątania i przeglądu.
- Wolisz interfejs poleceń zamiast pisania kodu w Pythonie.

## Użyj Python API gdy

Wybierz Python API, gdy to Twój kod powinien kontrolować przepływ pracy.

API jest przydatne dla aplikacji, skryptów automatyzacyjnych, notatników, usług i niestandardowych potoków. Pozwala wywoływać niskopoziomowe API tłumaczenia treści dla pojedynczych plików albo uruchomić tę samą orkiestrację na poziomie repozytorium, której używa CLI.

Przetłumacz pojedynczy dokument Markdown i zdecyduj, gdzie go zapisać:

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

Uruchom tłumaczenie repozytorium z Pythona:

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

Dobrym wyborem, gdy:

- Twoja aplikacja już odczytuje pliki, bufory, notatniki lub bajty obrazów.
- Potrzebujesz niestandardowej walidacji, przechowywania, logowania, ponownych prób lub procesów zatwierdzania.
- Chcesz przetłumaczyć pojedynczy dokument, notatnik lub obraz bez przetwarzania całego repozytorium.
- Chcesz tłumaczenia repozytorium, ale z automatyzacji Pythona zamiast polecenia w powłoce.

## Użyj serwera MCP gdy

Wybierz serwer MCP, gdy agent, edytor lub klient zgodny z MCP powinien wywoływać narzędzia Co-op Translator.

W typowej konfiguracji lokalnej użytkownik nie utrzymuje serwera ręcznie. Klient MCP uruchamia `co-op-translator-mcp` przez `stdio`, gdy potrzebuje narzędzi.

Przykładowe żądania użytkownika, którymi agent mógłby się zająć:

- "Przetłumacz ten plik Markdown na koreański i zachowaj poprawność linków."
- "Przetłumacz ten plik Markdown na koreański za pomocą workflowu MCP z asystą agenta, używając własnego modelu dla tłumaczonych fragmentów."
- "Przetłumacz ten notatnik na koreański, zachowaj komórki kodu i użyj Co-op Translator MCP do rekonstrukcji notatnika."
- "Przetłumacz tekst na tym obrazie na japoński i zapisz wynik."
- "Wykonaj symulację tłumaczenia repozytorium na hiszpański i powiedz mi, co by się zmieniło."
- "Sprawdź, czy wyjście tłumaczenia na koreański jest aktualne."

Dla Markdown i notatników MCP może działać w dwóch trybach:

| Tryb | Użyj gdy | Główne narzędzia |
| --- | --- | --- |
| Z asystą agenta | Gdy hostujący agent MCP ma tłumaczyć fragmenty własnym modelem, bez poświadczeń dostawcy LLM Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Obsługiwany przez dostawcę | Co-op Translator powinien wywoływać Azure OpenAI, OpenAI, lub Anthropic bezpośrednio. | `translate_markdown_content`, `translate_notebook_content` |

Wywołanie narzędzia Markdown w trybie obsługiwanym przez dostawcę MCP:

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

Wywołanie narzędzia obrazów w MCP:

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

Domyślnie tłumaczenie repozytorium przez MCP jest wykonywane w trybie dry-run:

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

Dobrym wyborem, gdy:

- Chcesz przepływów tłumaczeń w naturalnym języku w agencie lub edytorze.
- Chcesz tłumaczeń Markdown lub notatników, w których hostujący agent tłumaczy przygotowane fragmenty własnym modelem.
- Chcesz, aby agent tłumaczył wybrane treści zamiast całego repozytorium.
- Chcesz kroku zatwierdzania przed zapisaniem zmian w całym repozytorium.
- Chcesz jednego interfejsu udostępniającego narzędzia do Markdown, notatników, obrazów, przeglądu i przepisywania ścieżek.

## Jak działają razem

CLI jest najlepszym domyślnym wyborem dla osób tłumaczących repozytoria. Python API jest najlepsze, gdy to Twój kod zarządza przepływem pracy. Serwer MCP jest najlepszy, gdy agent lub edytor zarządza przepływem pracy.

Wszystkie trzy ścieżki korzystają z tego samego publicznego API Co-op Translator, więc możesz zacząć od CLI, później zautomatyzować to w Pythonie i udostępnić te same możliwości klientom MCP, gdy potrzebujesz workflowów sterowanych przez agenta.