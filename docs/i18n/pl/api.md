# API Pythona

Stabilne publiczne API Pythona jest eksportowane z `co_op_translator.api`. Większość integracji używa jednego z następujących przepływów:

| Scenariusz | Użyj gdy | Główne API |
| --- | --- | --- |
| Translate individual files or documents | Twoja aplikacja odczytuje zawartość źródła, wywołuje Co-op Translator, aby wykonać tłumaczenie, i decyduje, gdzie zapisać wynik. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Twój host MCP lub model aplikacji przetłumaczy fragmenty, podczas gdy Co-op Translator zajmie się dzieleniem na fragmenty i rekonstrukcją. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | Chcesz, aby API Pythona zachowywało się jak CLI i obsługiwało wykrywanie, ścieżki wyjścia, metadane, sprzątanie i zapisy. | `run_translation` |

Większość modułów niższego poziomu w `core`, `config`, `review` i `utils` to szczegóły implementacyjne używane przez te punkty wejścia API.

Klienci MCP używają tego samego publicznego API przez [Serwer MCP](mcp.md). Użyj tej strony, gdy wywołujesz Pythona bezpośrednio, a przewodnika MCP, gdy udostępniasz Co-op Translator agentowi lub edytorowi. Jeśli zastanawiasz się między CLI, API Pythona i MCP, zacznij od [Wybierz swój przepływ pracy](workflows.md).

## Pierwszy przepływ użycia API

Zacznij tutaj, jeśli wywołujesz Co-op Translator z kodu Pythona:

1. Skonfiguruj dostawcę LLM zgodnie z opisem w [Configuration](configuration.md), chyba że tylko przygotowujesz fragmenty Markdown lub notebooków dla tłumaczenia przez host-agenta.
2. Zdecyduj, czy Twoja aplikacja obsługuje operacje wejścia/wyjścia plików.
3. Używaj API zawartości, gdy Twoja aplikacja odczytuje i zapisuje poszczególne pliki.
4. Użyj `run_translation`, gdy Co-op Translator powinien przetworzyć repozytorium podobnie jak CLI.
5. Użyj `run_review` po tłumaczeniu, jeśli potrzebujesz deterministycznych kontroli w automatyzacji.

| Cel | API do rozpoczęcia |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Scenariusz 1: Tłumaczenie pojedynczych plików lub dokumentów

Użyj tego przepływu, gdy masz już plik, bufor edytora, payload notebooka, żądanie MCP lub niestandardowe wejście potoku. To Twój kod odpowiada za operacje wejścia/wyjścia plików:

1. Odczytaj zawartość źródła.
2. Wywołaj API tłumaczenia zawartości.
3. Opcjonalnie wywołaj API przepisywania ścieżek, jeśli przetłumaczona zawartość zostanie zapisana w folderze tłumaczeń projektu.
4. Zapisz lub zwróć wynik z aplikacji.

API tłumaczenia zawartości nie uruchamia odkrywania projektu, nie zapisuje metadanych, nie dołącza zastrzeżeń i nie przepisuje linków automatycznie.

### Plik Markdown

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


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
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Jeśli przetłumaczony Markdown nie będzie częścią struktury projektu Co-op Translator, pominij `rewrite_markdown_paths` i zapisz przetłumaczony ciąg bezpośrednio.

### Plik notebooka

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

`translate_notebook_content` tłumaczy komórki Markdown i zachowuje komórki inne niż Markdown. Przepisywanie ścieżek stosowane jest tylko do komórek Markdown.

### Plik obrazu

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

`translate_image_content` odczytuje źródłowy obraz i zwraca renderowany `PIL.Image.Image`. Nie zapisuje przetłumaczonych metadanych obrazu.

## Scenariusz 2: Tłumaczenie całego repozytorium

Użyj tego przepływu, gdy chcesz, aby API Pythona zachowywało się jak polecenie `translate` w CLI. `run_translation` wykrywa obsługiwane pliki, tłumaczy wybrane typy zawartości, przepisuje ścieżki, zapisuje pliki wyjściowe, aktualizuje metadane i wykonuje zadania konserwacyjne tłumaczenia, takie jak sprzątanie.

`run_translation` jest preferowanym punktem wejścia do orkiestracji projektu. `translate_project` jest eksportowany jako alias kompatybilności o tym samym zachowaniu.

Przetłumacz pliki Markdown w bieżącym repozytorium na koreański i japoński:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Przetłumacz tylko notebooki z określonego katalogu głównego projektu:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Podejrzyj wolumen tłumaczenia bez zapisywania plików:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Przetłumacz wiele katalogów źródłowych w jednym wywołaniu:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Zapisz tłumaczenia do jawnych grup wyjściowych:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

Użyj zastępczego katalogu na język, gdy każdy język powinien zawierać zagnieżdżony podkatalog:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

Jeśli żadna z opcji `markdown`, `notebook` lub `images` nie jest ustawiona, API tłumaczy wszystkie obsługiwane typy: Markdown, notebooki i obrazy.

## Przegląd przetłumionej zawartości

`run_review` uruchamia deterministyczne kontrole tłumaczeń bez poświadczeń LLM lub Vision.

!!! note "Beta"
    `run_review` is a beta deterministic review API. It does not call model providers or write files, but checks and issue schemas may evolve.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Sprawdź tylko pliki zmienione względem bazowego refa i wydrukuj wynik w formacie GitHub:

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## Przykłady API - kopiuj/wklej

Przetłumacz zawartość Markdown bez zapisywania plików:

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

Przetłumacz i przepisz linki Markdown:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

Przetłumacz repozytorium z Pythona:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Przetłumacz wiele katalogów źródłowych:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

Zachowaj terminy ze słownika:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## Publiczne punkty wejścia

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## API tłumaczenia zawartości

API tłumaczenia zawartości są przeznaczone do integracji, które już mają zawartość w pamięci, takich jak rozszerzenie edytora, narzędzie MCP, przetwarzacz notebooków lub niestandardowy potok.

| Funkcja | Wejście | Wyjście | Operacje na plikach | Uwagi |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Nie | Asynchroniczne. Tłumaczy tylko zawartość Markdown. Nie przepisuje linków, nie zapisuje metadanych ani nie dołącza zastrzeżeń. |
| `translate_notebook_content` | Notebook JSON `str` lub `dict` | Notebook JSON `str` | Nie | Asynchroniczne. Tłumaczy komórki Markdown i zachowuje komórki inne niż Markdown. Nie przepisuje linków, nie zapisuje metadanych ani nie dołącza zastrzeżeń. |
| `translate_image_content` | Ścieżka do obrazu | `PIL.Image.Image` | Odczytuje tylko źródłowy obraz | Synchroniczne. Ekstrahuje i tłumaczy tekst z obrazu, a następnie zwraca renderowany obraz. Nie zapisuje przetłumaczonych metadanych obrazu. |

`translate_markdown_content` i `translate_notebook_content` akceptują opcjonalny `source_path` poprzez swoje opcje. Ścieżka jest przekazywana jako kontekst do tłumacza; wywołujący pozostają odpowiedzialni za wszelkie specyficzne dla projektu przepisywanie ścieżek po tłumaczeniu.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Te same opcje można przekazać jako słowniki:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API tłumaczenia z pomocą agenta

API wspomagane przez agenta nie wywołują Azure OpenAI ani OpenAI z poziomu Co-op Translator. Przygotowują fragmenty Markdown lub notebooka do przetłumaczenia przez host-agenta, a następnie rekonstruują końcową zawartość z przetłumaczonych fragmentów.

| Funkcja | Cel |
| --- | --- |
| `start_markdown_agent_translation` | Zwróć samodzielne zadanie Markdown z fragmentami, promptami i stanem rekonstrukcji. |
| `finish_markdown_agent_translation` | Zrekonstruuj Markdown z zadania i przetłumaczonych przez host-agenta fragmentów. |
| `start_notebook_agent_translation` | Zwróć zadanie notebooka z fragmentami komórek Markdown do przetłumaczenia przez host-agenta. |
| `finish_notebook_agent_translation` | Zrekonstruuj JSON notebooka zachowując komórki kodu, outputy i metadane. |

Ten przepływ jest przeznaczony głównie dla hostów MCP. Jeśli potrzebujesz produkcyjnego tłumaczenia repozytorium, gdzie Co-op Translator zarządza wywołaniami dostawców, użyj `translate_markdown_content`, `translate_notebook_content` lub `run_translation`.

## API przepisywania ścieżek

API przepisywania ścieżek nie wykonują tłumaczenia. Aktualizują linki i pola frontmatter po tym, jak wywołujący zna ścieżkę źródłową, przetłumaczoną ścieżkę docelową i strukturę projektu.

| Funkcja | Zakres | Uwagi |
| --- | --- | --- |
| `rewrite_markdown_paths` | Treść Markdown i frontmatter | Przepisuje linki Markdown i obsługiwane pola frontmatter dotyczące ścieżek dla przetłumaczonego celu. |
| `rewrite_notebook_paths` | Komórki Markdown w JSON notebooka | Stosuje przepisywanie ścieżek Markdown do każdej komórki Markdown i pozostawia nie-Markdownowe komórki bez zmian. |

Argument `policy` może być słownikiem z następującymi polami:

| Pole | Wymagane | Cel |
| --- | --- | --- |
| `language_code` | Yes | Docelowy kod języka, np. `"ko"` lub `"pt-BR"`. |
| `root_dir` | No | Katalog główny projektu. Domyślnie `"."`. |
| `translations_dir` | No | Katalog wyjściowy tłumaczeń tekstu. Domyślnie `translations` w `root_dir`. |
| `translated_images_dir` | No | Katalog wyjściowy przetłumaczonych obrazów. Domyślnie `translated_images` w `root_dir`. |
| `translation_types` | No | Włączone typy tłumaczeń. Domyślnie Markdown, notebooki i obrazy. |
| `lang_subdir` | No | Opcjonalny podkatalog pod każdym folderem języka. |

## Parametry tłumaczenia projektu

| Parametr | Typ | Domyślnie | Cel |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Kody docelowych języków oddzielone spacjami, np. `"ko ja fr"`, lub `"all"`. Kody aliasów są normalizowane do kanonicznych wartości BCP 47. |
| `root_dir` | `str` | `"."` | Katalog główny projektu dla jednego celu tłumaczenia. Ignorowany, gdy podano `root_dirs` lub `groups`. |
| `update` | `bool` | `False` | Usuń i odtwórz istniejące tłumaczenia dla wybranych języków. |
| `images` | `bool` | `False` | Uwzględnij tłumaczenie obrazów. Wymaga konfiguracji Azure AI Vision. |
| `markdown` | `bool` | `False` | Uwzględnij tłumaczenie Markdown. |
| `notebook` | `bool` | `False` | Uwzględnij tłumaczenie notebooków Jupyter. |
| `debug` | `bool` | `False` | Włącz logowanie debugowania. |
| `save_logs` | `bool` | `False` | Zapisz pliki logów poziomu DEBUG w katalogu `logs/` pod katalogiem głównym. |
| `yes` | `bool` | `True` | Automatycznie potwierdź monity dla użycia programowego i CI. |
| `add_disclaimer` | `bool` | `False` | Dodaj zastrzeżenia dotyczące tłumaczenia maszynowego do przetłumaczonych Markdown i notebooków. |
| `translations_dir` | `str \| None` | `None` | Niestandardowy katalog wyjściowy tłumaczeń tekstu. Ścieżki względne rozwiązywane są względem każdego katalogu głównego. |
| `image_dir` | `str \| None` | `None` | Niestandardowy katalog wyjściowy przetłumaczonych obrazów. Ścieżki względne rozwiązywane są względem każdego katalogu głównego. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Wiele katalogów głównych, które dzielą te same ustawienia wyjściowe. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Jawne pary `(root_dir, translations_dir)`. Ma pierwszeństwo przed `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL repozytorium używany przy renderowaniu tabeli języków w README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Terminy słownikowe do zachowania podczas tłumaczenia. Duplikaty i puste terminy są normalizowane. |
| `dry_run` | `bool` | `False` | Oszacuj wolumen tłumaczeń i podejrzyj zachowanie migracji bez zapisywania plików. |

## Parametry przeglądu

`run_review` celowo odzwierciedla sygnaturę `run_translation` tam, gdzie to możliwe, aby automatyzacja mogła przełączać się między przepływami tłumaczenia i przeglądu przy minimalnym rozgałęzieniu.

| Parametr | Typ | Domyślnie | Cel |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Foldery językowe do przeglądu. Akceptowane są łańcuchy oddzielone spacjami i iterowalne. `"all"` przegląda każdy wykryty język tłumaczenia. |
| `root_dir` | `str` | `"."` | Katalog główny projektu dla jednego celu przeglądu. Ignorowany, gdy podano `root_dirs` lub `groups`. |
| `markdown` | `bool` | `False` | Uwzględnij pliki źródłowe Markdown i MDX. |
| `notebook` | `bool` | `False` | Uwzględnij pliki źródłowe notebooków Jupyter. |
| `images` | `bool` | `False` | Zarezerwowane dla zgodności z opcjami tłumaczenia. Odwołania do obrazów są sprawdzane z Markdown. |
| `translations_dir` | `str \| None` | `None` | Niestandardowy katalog wyjściowy dla przetłumaczonego tekstu. Ścieżki względne są rozwiązywane względem każdego katalogu głównego. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Wiele katalogów głównych, które mają wspólne ustawienia wyjściowe. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Jawne (root_dir, translations_dir) pary. Ma pierwszeństwo przed `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref używane do ograniczenia przeglądu do zmienionych plików źródłowych. |
| `output_format` | `str` | `"text"` | Format wyjścia przeglądu. Obsługiwane wartości to `"text"` i `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Traktuj ostrzeżenia jako niepowodzenia, oprócz błędów. |
| `debug` | `bool` | `False` | Włącz logowanie debugowe. |
| `save_logs` | `bool` | `False` | Zapisuj pliki dziennika poziomu DEBUG w katalogu głównym `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Wymagania konfiguracji

Provider-backed translation APIs require provider configuration before translating:

- Tłumaczenie Markdown i notatników wymaga dostawcy LLM. Skonfiguruj albo Azure OpenAI, albo OpenAI.
- Tłumaczenie obrazów wymaga Azure AI Vision oprócz dostawcy LLM.
- `run_translation` uruchamia lekkie testy łączności przed rozpoczęciem tłumaczenia projektu.
- Interfejsy API wspomagane przez agenta `start_*_agent_translation` i `finish_*_agent_translation` nie wywołują dostawców LLM Co-op Translator. Aplikacja hosta lub agent MCP tłumaczy przygotowane fragmenty.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` i `run_review` są deterministyczne i nie wymagają poświadczeń dostawcy.

Required Azure OpenAI variables:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Required OpenAI variables:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Required Azure AI Vision variables for image translation:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` is deterministic and does not require Azure OpenAI, OpenAI, or Azure AI Vision configuration.

## Uwagi dotyczące zachowania

- Interfejsy API tłumaczenia treści oddzielają tłumaczenie od przepisania ścieżek projektu. Wywołaj explicite `rewrite_markdown_paths` lub `rewrite_notebook_paths`, gdy przetłumaczona zawartość wymaga dostosowania linków względem projektu dla docelowej lokalizacji.
- Interfejsy API orkiestracji projektu dodają zachowania projektowe wokół tłumaczenia treści, w tym wykrywanie plików, zapisy, przepisywanie ścieżek, metadane, sprzątanie i opcjonalne zastrzeżenia.
- `run_translation` wypisuje podsumowania postępu i szacunków za pomocą Click, odpowiadając doświadczeniu użytkownika CLI.
- `dry_run=True` oblicza szacunki używając wirtualnych aktualizacji README, ale nie zapisuje README ani plików tłumaczeń.
- `groups` są przetwarzane sekwencyjnie. Jeden zbiorczy szacunek jest wypisany przed rozpoczęciem pracy.
- Gdy wybrane jest tłumaczenie obrazów, brak konfiguracji Vision powoduje zgłoszenie błędu przed rozpoczęciem tłumaczenia.
- Istniejące foldery językowe oparte na aliasach są wykrywane i mogą zostać przeniesione do kanonicznych nazw folderów językowych w ramach uruchomienia.
- `run_review` kończy się niepowodzeniem w przypadku brakujących przetłumaczonych plików, brakujących lub przestarzałych metadanych tłumaczeń, nieprawidłowego frontmatteru lub ogrodzeń kodu w Markdown oraz nieprawidłowego przetłumaczonego JSON notatnika.
- `run_review` domyślnie zgłasza brakujące lokalne cele linków Markdown i obrazów jako ostrzeżenia.

## Wewnętrzna ścieżka wywołań

The API delegates to the same core implementation used by the CLI:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Focused project translation mixins for Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators under `co_op_translator.core`.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| Klasa | Moduł | Odpowiedzialność |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordynuje tłumaczenie na poziomie projektu, zarządzanie katalogami, normalizację metadanych per-język oraz delegowanie do tłumaczy Markdown, notatników i obrazów. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Wykonuje asynchroniczne przetwarzanie plików dla Markdown, notatników, obrazów, wykrywania przestarzałości i aktualizacji metadanych tłumaczeń. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Koordynuje odczyty plików Markdown, tłumaczenie treści, przepisywanie ścieżek, metadane, zastrzeżenia i zapisy. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Koordynuje odczyty plików notatników, tłumaczenie komórek Markdown, przepisywanie ścieżek, metadane, zastrzeżenia i zapisy. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Koordynuje wykrywanie źródłowych obrazów, tłumaczenie obrazów, ścieżki wyjściowe, metadane i zapisy. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Znajduje pary przetłumaczonych plików Markdown, ocenia jakość tłumaczeń i odczytuje metadane dotyczące pewności w celu obsługi workflow naprawczych o niskim poziomie pewności. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordynuje deterministyczne kontrole przeglądu w zakresie plików źródłowych, języków docelowych i skonfigurowanych katalogów tłumaczeń. |
| `ReviewTarget` | `co_op_translator.review.targets` | Opisuje źródłowy katalog główny i katalog wyjściowy tłumaczeń sprawdzany dla tego katalogu. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Wykrywa przestarzałe aliasowe foldery językowe i przygotowuje plany migracji do kanonicznych nazw folderów BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Ładuje `.env` pliki i sprawdza, czy wymagani dostawcy LLM oraz opcjonalny Vision są skonfigurowani. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Automatycznie wykrywa Azure OpenAI lub OpenAI, weryfikuje wymagane zmienne środowiskowe i uruchamia testy łączności dostawcy. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Wykrywa konfigurację Azure AI Vision i uruchamia testy łączności dla tłumaczenia obrazów. |