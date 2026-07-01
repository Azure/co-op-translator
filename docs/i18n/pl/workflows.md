# Wybierz swój przepływ pracy

Co-op Translator można używać na trzy sposoby: przez CLI, Python API i serwer MCP. Udostępniają te same możliwości tłumaczeniowe, ale każdy z nich pasuje do innego przepływu pracy.

Skorzystaj z tej strony, gdy zastanawiasz się, od czego zacząć.

## Szybka decyzja

| Jeśli chcesz... | Użyj | Zacznij tutaj |
| --- | --- | --- |
| Przetłumaczyć lub przejrzeć repozytorium z terminala | CLI | [Dokumentacja CLI](cli.md) |
| Dodać tłumaczenie do skryptu Pythona, usługi, notatnika lub zadania CI | Python API | [Python API](api.md) |
| Pozwolić agentowi, edytorowi lub klientowi zgodnemu z MCP tłumaczyć treść dla Ciebie | MCP Server | [Serwer MCP](mcp.md) |
| Przetłumaczyć pojedynczy dokument Markdown, notatnik lub obraz, które Twoja aplikacja już załadowała | Python API lub Serwer MCP | [Python API](api.md) lub [MCP Server](mcp.md) |
| Przetłumaczyć całe repozytorium z standardowymi folderami wyjściowymi i metadanymi | CLI lub `run_translation` | [Dokumentacja CLI](cli.md) lub [Python API](api.md) |

## Użyj CLI, gdy

Wybierz CLI, gdy osoba lub zadanie CI uruchamia tłumaczenie repozytorium z powłoki.

CLI to najprostsza ścieżka, gdy chcesz, aby Co-op Translator wykrywał pliki projektu, tworzył tłumaczenia wyjściowe, zachowywał strukturę projektu, aktualizował metadane i uruchamiał polecenia przeglądu.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Pasuje, gdy:

- Tłumaczysz repozytorium z terminala.
- Chcesz powtarzalnego polecenia dla procesów CI lub wydawniczych.
- Chcesz wbudowanego wykrywania projektu, ścieżek wyjściowych, metadanych, sprzątania i przeglądu.
- Wolisz interfejs poleceń zamiast pisania kodu Pythona.

## Użyj Python API, gdy

Wybierz Python API, gdy to Twój kod ma kontrolować przepływ pracy.

API jest przydatne dla aplikacji, skryptów automatyzujących, notatników, usług i niestandardowych potoków. Pozwala wywoływać niskopoziomowe API tłumaczenia treści dla poszczególnych plików lub uruchamiać tę samą orkiestrację na poziomie repozytorium, której używa CLI.

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
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

Pasuje, gdy:

- Twoja aplikacja już odczytuje pliki, buffory, notatniki lub bajty obrazów.
- Potrzebujesz niestandardowej walidacji, przechowywania, logowania, ponowień lub procesów zatwierdzania.
- Chcesz przetłumaczyć pojedynczy dokument, notatnik lub obraz bez przetwarzania całego repozytorium.
- Chcesz tłumaczenia repozytorium, ale z automatyzacji w Pythonie zamiast polecenia powłoki.

## Użyj serwera MCP, gdy

Wybierz serwer MCP, gdy agent, edytor lub klient zgodny z MCP powinien wywoływać narzędzia Co-op Translator.

W normalnej lokalnej konfiguracji użytkownik nie utrzymuje ręcznie uruchomionego serwera. Klient MCP uruchamia `co-op-translator-mcp` przez `stdio`, gdy potrzebuje narzędzi.

Przykładowe żądania użytkownika, które agent mógłby obsłużyć:

- "Przetłumacz ten plik Markdown na koreański i zachowaj poprawność linków."
- "Przetłumacz ten plik Markdown na koreański za pomocą przepływu pracy MCP wspomaganego przez agenta, używając własnego modelu do tłumaczonych fragmentów."
- "Przetłumacz ten notatnik na koreański, zachowaj komórki z kodem i użyj Co-op Translator MCP do odtworzenia notatnika."
- "Przetłumacz tekst na tym obrazie na japoński i zapisz wynik."
- "Wykonaj próbne tłumaczenie repozytorium na hiszpański i powiedz mi, co by się zmieniło."
- "Sprawdź, czy wynik tłumaczenia na koreański jest aktualny."

Dla Markdown i notatników, MCP może działać w dwóch trybach:

| Tryb | Użyj, gdy | Główne narzędzia |
| --- | --- | --- |
| Agent-assisted | Hostujący agent MCP powinien tłumaczyć fragmenty swoim własnym modelem, bez poświadczeń dostawcy LLM Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator powinien wywołać Azure OpenAI lub OpenAI bezpośrednio. | `translate_markdown_content`, `translate_notebook_content` |

Kształt wywołania narzędzia Markdown wspieranego przez dostawcę w MCP:

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

Kształt wywołania narzędzia obrazu MCP:

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

Tłumaczenie repozytorium jest domyślnie wykonywane próbnie przez MCP:

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

Pasuje, gdy:

- Chcesz przepływów tłumaczenia w języku naturalnym wewnątrz agenta lub edytora.
- Chcesz tłumaczenia Markdown lub notatników, gdzie hostujący model agenta tłumaczy przygotowane fragmenty.
- Chcesz, aby agent tłumaczył wybraną zawartość zamiast całego repozytorium.
- Chcesz kroku zatwierdzenia przed zapisem w całym repozytorium.
- Chcesz jednego interfejsu, który udostępnia narzędzia do Markdown, notatników, obrazów, przeglądu i przepisywania ścieżek.

## Jak ze sobą współgrają

CLI jest najlepszym domyślnym wyborem dla osób tłumaczących repozytoria. Python API jest najlepsze, gdy to Twój kod zarządza przepływem pracy. Serwer MCP jest najlepszy, gdy agent lub edytor zarządza przepływem pracy.

Wszystkie trzy ścieżki używają tego samego publicznego API Co-op Translator, więc możesz zacząć od CLI, zautomatyzować później w Pythonie i udostępnić te same możliwości klientom MCP, gdy potrzebujesz przepływów pracy sterowanych przez agenta.