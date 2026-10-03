# API Pythona

Stabilne publiczne API Pythona jest eksportowane z `co_op_translator.api`. Większość integracji używa jednego z tych przepływów pracy:

| Scenariusz | Użyj, gdy | Główne API |
| --- | --- | --- |
| Przetłumacz pojedyncze pliki lub dokumenty | Twoja aplikacja odczytuje zawartość źródła, wywołuje Co-op Translator do tłumaczenia i decyduje, gdzie zapisać wynik. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Przygotuj zawartość do tłumaczenia przez host-agenta | Twój host MCP lub model aplikacji przetłumaczy fragmenty, podczas gdy Co-op Translator zajmie się dzieleniem na fragmenty i rekonstrukcją. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Tłumacz całe repozytorium | Chcesz, aby API Pythona zachowywało się jak CLI i obsługiwało wykrywanie, ścieżki wyjściowe, metadane, czyszczenie i zapisy. | `run_translation` |

Większość niższej warstwy modułów w `core`, `config`, `review` i `utils` to szczegóły implementacyjne używane przez te punkty wejścia API.

Klienci MCP używają tego samego publicznego API przez [Serwer MCP](mcp.md). Użyj tej strony, gdy wywołujesz Pythona bezpośrednio, a przewodnika MCP, gdy eksponujesz Co-op Translator dla agenta lub edytora. Jeśli zastanawiasz się między CLI, API Pythona i MCP, zacznij od [Wybierz swój przepływ pracy](workflows.md).

## Pierwsze użycie API

Zacznij tutaj, jeśli wywołujesz Co-op Translator z kodu Pythona:

1. Skonfiguruj dostawcę LLM zgodnie z opisem w [Konfiguracja](configuration.md), chyba że tylko przygotowujesz fragmenty Markdown lub notebooków do tłumaczenia przez host-agenta.
2. Zdecyduj, czy Twoja aplikacja jest odpowiedzialna za operacje wejścia/wyjścia na plikach.
3. Użyj API zawartości, gdy Twoja aplikacja odczytuje i zapisuje pojedyncze pliki.
4. Użyj `run_translation`, gdy Co-op Translator ma przetwarzać repozytorium jak CLI.
5. Użyj `run_review` po tłumaczeniu, jeśli potrzebujesz deterministycznych kontroli w automatyzacji.

| Cel | API do rozpoczęcia |
| --- | --- |
| Przetłumacz jeden łańcuch Markdown lub plik | `translate_markdown_content` |
| Przetłumacz jedną zawartość notebooka | `translate_notebook_content` |
| Przetłumacz jeden obraz | `translate_image_content` |
| Pozwól host-agentowi tłumaczyć fragmenty Markdown lub notebooków | `start_markdown_agent_translation` lub `start_notebook_agent_translation` |
| Przepisz przetłumaczone linki po wybraniu ścieżki wyjściowej | `rewrite_markdown_paths` lub `rewrite_notebook_paths` |
| Przetłumacz całe repozytorium | `run_translation` |
| Przejrzyj przetłumaczoną zawartość | `run_review` |

## Scenariusz 1: Tłumaczenie pojedynczych plików lub dokumentów

Użyj tego przepływu, gdy masz już plik, bufor edytora, zawartość notebooka, żądanie MCP lub niestandardowe wejście potoku. Twój kod zarządza operacjami wejścia/wyjścia na plikach:

1. Odczytaj zawartość źródła.
2. Wywołaj API tłumaczenia zawartości.
3. Opcjonalnie wywołaj API do przepisywania ścieżek, jeśli przetłumaczona zawartość będzie zapisywana w folderze tłumaczeń projektu.
4. Zapisz wynik lub zwróć go z aplikacji.

API tłumaczenia zawartości nie uruchamiają wykrywania projektu, nie zapisują metadanych, nie dodają zastrzeżeń ani automatycznie nie przepisują linków.

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

Jeśli przetłumaczony Markdown nie będzie znajdować się w układzie projektu Co-op Translator, pomiń `rewrite_markdown_paths` i zapisz przetłumaczony łańcuch bezpośrednio.

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

`translate_notebook_content` tłumaczy komórki Markdown i zachowuje komórki niebędące Markdown. Przepisywanie ścieżek jest stosowane tylko do komórek Markdown.

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

`translate_image_content` odczytuje obraz źródłowy i zwraca wyrenderowany `PIL.Image.Image`. Nie zapisuje przetłumaczonych metadanych obrazu.

## Scenariusz 2: Tłumaczenie całego repozytorium

Użyj tego przepływu, gdy chcesz, aby API Pythona zachowywało się jak polecenie CLI `translate`. `run_translation` odkrywa obsługiwane pliki, tłumaczy wybrane typy zawartości, przepisuje ścieżki, zapisuje pliki wyjściowe, aktualizuje metadane i wykonuje zadania konserwacyjne tłumaczeń, takie jak czyszczenie.

`run_translation` jest preferowanym punktem wejścia do orkiestracji projektów. `translate_project` jest eksportowany jako alias zgodności z tym samym zachowaniem.

Przetłumacz pliki Markdown w bieżącym repozytorium na koreański i japoński:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Tłumacz tylko notebooki z określonego katalogu projektu:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Wyświetl podgląd objętości tłumaczenia bez zapisu plików:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Zarejestruj ustrukturyzowane zdarzenia postępu dla integracji:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Przechowaj dane w tabeli zdarzeń zadań lub przesyłaj je strumieniowo do interfejsu użytkownika.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Zdarzenia używają wersjonowanego schematu `co-op.translation.event.v1`. Integracje powinny
opierać się na stabilnych polach, takich jak `type` i `stage_key`, a nie na tekście
dla użytkownika w konsoli lub `stage_label`.

Tłumacz wiele źródeł zawartości w jednym wywołaniu:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Zapisz tłumaczenia w wyraźnych grupach wyjściowych:

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

Użyj symbolu zastępczego na język, gdy każdy język powinien mieć zagnieżdżony podkatalog:

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

Jeśli żadne z `markdown`, `notebook` ani `images` nie są ustawione, API tłumaczy wszystkie obsługiwane typy: Markdown, notebooki i obrazy.

### Zachowaj zaakceptowane ręczne edycje za pomocą dostawcy stanu tłumaczenia

Domyślnie Co-op Translator utrzymuje swoje istniejące zachowanie na poziomie pliku: gdy
źródło Markdown jest nieaktualne, cały przetłumaczony plik jest regenerowany. Hostowane
integracje mogą opcjonalnie przekazać `TranslationStateProvider`, aby zachować ręczne
edycje w blokach źródłowych, które się nie zmieniły.

Dostawca dostarcza ostatnią zaakceptowaną parę źródło/cel i rejestruje każdą nową
kandydaturę. Akceptacja pozostaje odpowiedzialnością integracji — na przykład,
po scaleniu pull requesta z tłumaczeniami:

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

Dla plików Markdown z prawidłową zaakceptowaną bazą, Co-op Translator wyrównuje
bloków Markdown najwyższego poziomu. Nie zmienione bloki źródłowe ponownie wykorzystują aktualne przetłumaczone
bloki, łącznie z edycjami wprowadzonymi przez ludzi; zmienione lub dodane bloki źródłowe są wysyłane
do tłumaczenia; usunięte bloki źródłowe są usuwane. Jeśli wyrównanie jest niejednoznaczne,
struktura docelowa uległa zmianie, tłumaczenie bloku jest nieprawidłowe lub brak jest bazy odniesienia,
Co-op Translator bezpiecznie wraca do istniejącej pełnej
ścieżki tłumaczenia pliku.

To API przechowuje stan tłumaczenia dokumentu, a nie międzydokumentową pamięć fraz czy
segmentów tłumaczeniowych. Obecnie dotyczy tłumaczeń projektów Markdown.
Zachowanie dla notebooków i obrazów pozostaje bez zmian. Przekazanie `update=True`
wciąż żąda pełnej regeneracji.

Jeśli jeden lub więcej plików nie może zostać przetłumaczonych, `run_translation` zgłasza
`RuntimeError` po zakończeniu przepływu projektu zamiast raportować
pomyślne uruchomienie z brakującym wyjściem. Integracje powinny traktować to jako nieudane
zadanie i zachować poprzedni zaakceptowany stan tłumaczenia.

## Przegląd przetłumaczonej zawartości

`run_review` uruchamia deterministyczne kontrole tłumaczeń bez poświadczeń LLM lub Vision.

!!! note "Beta"
    `run_review` to beta wersja deterministycznego API przeglądu. Nie wywołuje dostawców modeli ani nie zapisuje plików, ale schematy kontroli i zgłoszeń mogą się zmieniać.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Po tłumaczeniu tylko README, użyj tego samego zakresu do przeglądu:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` przegląda tylko `README.md` w każdym skonfigurowanym katalogu źródłowym,
w tym niestandardowe `groups` i katalogi wyjściowe. Inne dokumenty i zagnieżdżone
READMEs są wyłączone. Brakujący plik README źródła powoduje `ValueError`; nieudane
sprawdzenia tłumaczenia powodują `RuntimeError`.

Przeglądaj tylko pliki zmienione względem refa bazowego i wypisz wynik w formacie GitHub-flavored:

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

## Przykłady API do kopiuj-wklej

Tłumacz zawartość Markdown bez zapisu plików:

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

Tłumacz i przepisuj linki w Markdown:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
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

Tłumacz repozytorium za pomocą Pythona:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Tłumacz wiele katalogów źródłowych:

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

Zachowaj terminy glosariusza:

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

## Punkty wejścia publiczne

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
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

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## API tłumaczenia treści

API tłumaczenia treści są przeznaczone dla integracji, które już mają zawartość w pamięci, takich jak rozszerzenie edytora, narzędzie MCP, procesor notebooków lub niestandardowy pipeline.

| Funkcja | Wejście | Wyjście | I/O plików | Uwagi |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Nie | Asynchronicznie. Tłumaczy tylko zawartość Markdown. Nie przepisuje linków, nie zapisuje metadanych ani nie dołącza zastrzeżeń. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | Nie | Asynchronicznie. Tłumaczy komórki Markdown i zachowuje komórki niebędące Markdown. Nie przepisuje linków, nie zapisuje metadanych ani nie dołącza zastrzeżeń. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Odczytuje tylko obraz źródłowy | Synchronicznie. Wyodrębnia i tłumaczy tekst z obrazu, następnie zwraca wyrenderowany obraz. Nie zapisuje metadanych przetłumaczonego obrazu. |

`translate_markdown_content` i `translate_notebook_content` akceptują opcjonalny `source_path` przez ich opcje. Ścieżka jest przekazywana jako kontekst do tłumacza; wywołujący pozostają odpowiedzialni za wszelkie specyficzne dla projektu przepisywanie ścieżek po tłumaczeniu.

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

## API tłumaczeń wspomaganych przez agenta

API wspomagane przez agenta nie wywołują skonfigurowanego dostawcy LLM z Co-op Translator. Przygotowują fragmenty Markdown lub notebooka dla agenta gospodarza do przetłumaczenia, a następnie rekonstruują końcową zawartość z przetłumaczonych fragmentów.

| Funkcja | Cel |
| --- | --- |
| `start_markdown_agent_translation` | Zwraca samodzielne zadanie Markdown z fragmentami, promptami i stanem rekonstrukcji. |
| `finish_markdown_agent_translation` | Rekonstruuje Markdown z zadania i przetłumaczonych przez agenta gospodarza fragmentów. |
| `start_notebook_agent_translation` | Zwraca zadanie notebooka z fragmentami komórek Markdown do przetłumaczenia przez agenta gospodarza. |
| `finish_notebook_agent_translation` | Rekonstruuje JSON notebooka przy zachowaniu komórek kodu, wyników i metadanych. |

Ten przepływ pracy jest głównie przeznaczony dla hostów MCP. Jeśli potrzebujesz produkcyjnego tłumaczenia repozytorium z Co-op Translator zarządzającym wywołaniami dostawcy, użyj `translate_markdown_content`, `translate_notebook_content` lub `run_translation`.

## API przepisywania ścieżek

API przepisywania ścieżek nie wykonują tłumaczenia. Aktualizują linki i ścieżki we frontmatter po tym, jak wywołujący znają ścieżkę źródłową, przetłumaczoną ścieżkę docelową i układ projektu.

| Funkcja | Zakres | Uwagi |
| --- | --- | --- |
| `rewrite_markdown_paths` | Treść Markdown i frontmatter | Przepisuje linki Markdown i obsługiwane pola ścieżek we frontmatter dla przetłumaczonego celu. |
| `rewrite_notebook_paths` | Komórki Markdown w JSON notebooka | Stosuje przepisywanie ścieżek Markdown do każdej komórki Markdown i pozostawia komórki niebędące Markdown bez zmian. |

Argument `policy` może być słownikiem z następującymi polami:

| Pole | Wymagane | Cel |
| --- | --- | --- |
| `language_code` | Tak | Kod docelowego języka, taki jak `"ko"` lub `"pt-BR"`. |
| `root_dir` | Nie | Katalog główny projektu źródłowego. Domyślnie `"."`. |
| `translations_dir` | Nie | Katalog wyjściowy tłumaczeń tekstu. Domyślnie `translations` w `root_dir`. |
| `translated_images_dir` | Nie | Katalog wyjściowy przetłumaczonych obrazów. Domyślnie `translated_images` w `root_dir`. |
| `translation_types` | Nie | Włączone typy tłumaczeń. Domyślnie Markdown, notebooki i obrazy. |
| `lang_subdir` | Nie | Opcjonalny podkatalog pod każdym folderem języka. |

## Parametry tłumaczenia projektu

| Parametr | Typ | Domyślnie | Cel |
| --- | --- | --- | --- |
| `language_codes` | `str` | Wymagane | Kody docelowych języków oddzielone spacją, takie jak `"ko ja fr"` lub `"all"`. Aliasowe kody są normalizowane do kanonicznych wartości BCP 47. |
| `root_dir` | `str` | `"."` | Katalog główny projektu dla pojedynczego celu tłumaczenia. Ignorowane jeśli podano `root_dirs` lub `groups`. |
| `update` | `bool` | `False` | Usuwa i tworzy ponownie istniejące tłumaczenia dla wybranych języków. |
| `images` | `bool` | `False` | Dołącz tłumaczenie obrazów. Wymaga konfiguracji Azure AI Vision. |
| `markdown` | `bool` | `False` | Dołącz tłumaczenie Markdown. |
| `notebook` | `bool` | `False` | Dołącz tłumaczenie notatników Jupyter. |
| `debug` | `bool` | `False` | Włącz logowanie debugowe. |
| `save_logs` | `bool` | `False` | Zapisuj pliki logów poziomu DEBUG w katalogu `logs/` w katalogu głównym. |
| `yes` | `bool` | `True` | Automatycznie potwierdzaj monity dla zastosowań programowych i CI. |
| `add_disclaimer` | `bool` | `False` | Dodaj zastrzeżenia dotyczące tłumaczenia maszynowego do tłumaczonych plików Markdown i notatników. |
| `translations_dir` | `str \| None` | `None` | Niestandardowy katalog wyjściowy tłumaczeń tekstu. Ścieżki względne są rozwiązywane względem każdego katalogu głównego. |
| `image_dir` | `str \| None` | `None` | Niestandardowy katalog wyjściowy przetłumaczonych obrazów. Ścieżki względne są rozwiązywane względem każdego katalogu głównego. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Wiele katalogów głównych dzielących te same ustawienia wyjścia. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Jawne `(root_dir, translations_dir)` pary. Ma pierwszeństwo przed `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL repozytorium używany podczas renderowania tabeli języków w README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Terminy słownikowe do zachowania podczas tłumaczenia. Duplikaty i puste terminy są normalizowane. |
| `dry_run` | `bool` | `False` | Oszacuj wolumen tłumaczenia i podejrzyj zachowanie migracji bez zapisu plików. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Opcjonalny adapter trwałości dla zaakceptowanej bazy i kandydata do przyrostowych aktualizacji Markdown. Pominięcie go zachowuje istniejące zachowanie pełnych plików. |

## Parametry przeglądu

`run_review` celowo odzwierciedla sygnaturę `run_translation`, gdzie to możliwe, aby automatyzacja mogła przełączać się między przepływami pracy tłumaczenia i przeglądu przy minimalnym rozgałęzieniu.

| Parametr | Typ | Domyślne | Przeznaczenie |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Docelowe foldery językowe do przeglądu. Akceptowane są łańcuchy rozdzielone spacją oraz iterowalne. `"all"` przegląda wszystkie wykryte języki tłumaczeń. |
| `root_dir` | `str` | `"."` | Katalog główny projektu dla pojedynczego celu przeglądu. Ignorowane, gdy podano `root_dirs` lub `groups`. |
| `markdown` | `bool` | `False` | Uwzględnij pliki źródłowe Markdown i MDX. |
| `notebook` | `bool` | `False` | Uwzględnij pliki źródłowe notatników Jupyter. |
| `images` | `bool` | `False` | Zarezerwowane dla zgodności z opcjami tłumaczenia. Odwołania do obrazów są sprawdzane z poziomu Markdown. |
| `translations_dir` | `str \| None` | `None` | Niestandardowy katalog wyjściowy tłumaczeń tekstu. Ścieżki względne są rozwiązywane względem każdego katalogu głównego. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Wiele katalogów głównych dzielących te same ustawienia wyjścia. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Jawne `(root_dir, translations_dir)` pary. Ma pierwszeństwo przed `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Ref Git używany do ograniczenia przeglądu do zmienionych plików źródłowych. |
| `readme_only` | `bool` | `False` | Przeglądaj tylko `README.md` w każdym katalogu źródłowym. Brakujący README źródła powoduje `ValueError`. |
| `output_format` | `str` | `"text"` | Format wyjścia przeglądu. Obsługiwane wartości to `"text"` i `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Traktuj ostrzeżenia jako niepowodzenia oprócz błędów. |
| `debug` | `bool` | `False` | Włącz logowanie debugowe. |
| `save_logs` | `bool` | `False` | Zapisz pliki dziennika na poziomie DEBUG w katalogu głównym `logs/`. |

Jeśli żadne z `markdown`, `notebook` lub `images` nie jest ustawione, API przegląda Markdown, notatniki oraz odwołania do obrazów tam, gdzie ma to zastosowanie. Przegląd nie wywołuje dostawcy LLM i nie wymaga kluczy API.

## Wymagania konfiguracji

Interfejsy API tłumaczeń zależne od dostawcy wymagają konfiguracji dostawcy przed tłumaczeniem:

- Tłumaczenie Markdown i notatników wymaga dostawcy LLM. Skonfiguruj Azure OpenAI, OpenAI lub Anthropic.
- Tłumaczenie obrazów wymaga Azure AI Vision oprócz dostawcy LLM.
- `run_translation` uruchamia lekkie kontrole łączności przed rozpoczęciem tłumaczenia projektu.
- Wspomagane przez agenta interfejsy API `start_*_agent_translation` i `finish_*_agent_translation` nie wywołują dostawców LLM Co-op Translator. Aplikacja hostująca lub agent MCP tłumaczy przygotowane fragmenty.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` i `run_review` są deterministyczne i nie wymagają poświadczeń dostawcy.

Wymagane zmienne Azure OpenAI:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Wymagane zmienne OpenAI:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Wymagane zmienne Anthropic:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` i `ANTHROPIC_MAX_TOKENS` są opcjonalne. Microsoft Agent Framework jest domyślnym klientem modelu dla wszystkich dostawców począwszy od Co-op Translator 0.22.0. Semantic Kernel można nadal tymczasowo wybrać za pomocą `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, ale spowoduje to wygenerowanie ostrzeżenia o przestarzałości; zobacz [konfiguracja](configuration.md#model-client-backend) w celu zapoznania się z planem stopniowego usuwania.

Wymagane zmienne Azure AI Vision dla tłumaczenia obrazów:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` jest deterministyczny i nie wymaga konfiguracji LLM ani Azure AI Vision.

## Uwagi dotyczące zachowania

- Interfejsy API tłumaczeń treści utrzymują tłumaczenie oddzielnie od przepisywania ścieżek projektu. Wywołaj jawnie `rewrite_markdown_paths` lub `rewrite_notebook_paths`, gdy przetłumaczona zawartość wymaga dostosowania linków względnych względem projektu dla docelowej lokalizacji.
- Interfejsy API orkiestracji projektu dodają zachowania projektowe wokół tłumaczenia treści, w tym odkrywanie plików, zapisy, przepisywanie ścieżek, metadane, czyszczenie oraz opcjonalne zastrzeżenia.
- `run_translation` drukuje podsumowania postępu i oszacowań poprzez tego samego reportera opartego na Rich używanego przez CLI. Wyjście nieinteraktywne wraca do prostego tekstu.
- `dry_run=True` oblicza oszacowania przy użyciu wirtualnych aktualizacji README, ale nie zapisuje README ani plików tłumaczeń.
- `groups` są przetwarzane sekwencyjnie. Jedno zbiorcze oszacowanie jest drukowane przed rozpoczęciem pracy.
- Gdy wybrane jest tłumaczenie obrazów, brak konfiguracji Vision powoduje błąd przed rozpoczęciem tłumaczenia.
- Istniejące foldery językowe oparte na aliasach są wykrywane i mogą zostać przeniesione do kanonicznych nazw folderów językowych w ramach uruchomienia.
- `run_review` kończy się niepowodzeniem w przypadku brakujących przetłumaczonych plików, brakujących lub nieaktualnych metadanych tłumaczenia, niepoprawnego frontmatteru / bloków kodu Markdown oraz nieprawidłowego przetłumaczonego JSON notatnika.
- `run_review` domyślnie zgłasza brakujące lokalne cele linków Markdown i obrazów jako ostrzeżenia.

## Wewnętrzna ścieżka wywołań

API deleguje do tej samej podstawowej implementacji używanej przez CLI:

Tłumaczenie:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Skoncentrowane mixiny do tłumaczenia projektów dla Markdown, notebooków i obrazów.
8. Tłumacze Markdown, notebooków, tekstu i obrazów w `co_op_translator.core`.

Przegląd:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministyczne kontrole w `co_op_translator.review.checks`

Poniższe klasy są przydatne dla opiekunów projektu, ale nie są eksportowane jako stabilne API na poziomie pakietu.

| Klasa | Moduł | Odpowiedzialność |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordynuje tłumaczenie na poziomie projektu, zarządzanie katalogami, normalizację metadanych dla każdego języka oraz delegowanie do tłumaczy Markdown, notatników i obrazów. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Wykonuje asynchroniczne przetwarzanie plików dla Markdown, notatników, obrazów, wykrywania nieaktualności oraz aktualizacji metadanych tłumaczeń. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orkiestruje odczyty plików Markdown, tłumaczenie zawartości, przepisywanie ścieżek, metadane, zastrzeżenia i zapisy. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orkiestruje odczyty plików notatników, tłumaczenie komórek Markdown, przepisywanie ścieżek, metadane, zastrzeżenia i zapisy. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orkiestruje wykrywanie źródłowych obrazów, tłumaczenie obrazów, ścieżki wyjściowe, metadane i zapisy. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Znajduje pary przetłumaczonych Markdown, ocenia jakość tłumaczenia i odczytuje metadane zaufania dla przepływów naprawczych o niskim zaufaniu. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordynuje deterministyczne kontrole przeglądu wśród plików źródłowych, docelowych języków i skonfigurowanych katalogów tłumaczeń. |
| `ReviewTarget` | `co_op_translator.review.targets` | Opisuje katalog źródłowy i katalog wyjściowy tłumaczeń przeglądany dla tego katalogu. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Wykrywa stare aliasy folderów językowych i przygotowuje plany migracji do kanonicznych folderów BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Ładuje pliki `.env` i sprawdza, czy wymagani dostawcy LLM oraz opcjonalny Vision są skonfigurowani. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Automatycznie wykrywa Azure OpenAI, OpenAI lub Anthropic, waliduje wymagane zmienne środowiskowe i uruchamia kontrole łączności dostawcy. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Wykrywa konfigurację Azure AI Vision i uruchamia kontrole łączności dla tłumaczenia obrazów. |