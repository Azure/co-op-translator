# Przewodnik dla opiekunów

Ta strona podsumowuje, jak API, CLI i witryna dokumentacji są ze sobą powiązane.

## Granica publicznego API

Stabilne API Pythona jest eksportowane z:

```python
co_op_translator.api
```

Publiczne API jest zorganizowane w pomocniki do tłumaczenia treści, pomocniki do przepisywania ścieżek, orkiestrację projektu oraz przegląd:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

`TranslationStateProvider` jest warstwą trwałego przechowywania dla hostowanych integracji.
Musi utrzymywać wygenerowane kandydatury oddzielnie od zaakceptowanych baz odniesienia, tak aby
tłumaczenie, które nie zostało scalone, nie mogło stać się źródłem prawdy.

Przy dodawaniu nowych publicznych API zaktualizuj:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- odpowiednie testy API w katalogu `tests/co_op_translator/`, takie jak `test_api.py` lub `test_review_api.py`

Unikaj dokumentowania niższych poziomów modułów `core` jako stabilnego API, chyba że projekt zamierza je wspierać bezpośrednio.

## Punkty wejścia CLI

Pakiet definiuje te skrypty Poetry:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` rozpoznaje skrypt na podstawie jego nazwy:

- `translate` wywołuje `co_op_translator.cli.translate.translate_command`
- `evaluate` wywołuje `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` wywołuje `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` wywołuje `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` omija `__main__.py` i wywołuje bezpośrednio `co_op_translator.mcp.server:main`.

Przy dodawaniu lub zmianie opcji CLI zaktualizuj:

- odpowiednie polecenie w `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- testy związane z CLI, jeśli zachowanie ulega zmianie

## Serwer MCP

Serwer MCP jest zaimplementowany w:

```python
co_op_translator.mcp.server
```

Serwer celowo opakowuje publiczne API Pythona zamiast wywoływać moduły `core` niższego poziomu. Zachowaj tę granicę, aby klienci MCP, wywołujący z Pythona, i CLI dzielili to samo zachowanie.

Przy dodawaniu lub zmianie narzędzi MCP zaktualizuj:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` jeśli powierzchnia publicznego API ulegnie zmianie

Narzędzia tłumaczące repozytorium mogą być wywoływane przez modele za pośrednictwem MCP i mogą zapisać wiele plików. Utrzymuj `dry_run=True` jako domyślną wartość i wymagaj `confirm_write=True` przed tłumaczeniem projektu bez trybu suchego.

## Przebieg tłumaczenia

Ogólny przebieg tłumaczenia projektu:

1. Parsuj argumenty CLI lub parametry API.
2. Zweryfikuj konfigurację LLM za pomocą `LLMConfig`.
3. Zweryfikuj Azure AI Vision, gdy wybrano tłumaczenie obrazów.
4. Normalizuj kody języków.
5. Wykryj starsze aliasy folderów językowych.
6. Oszacuj wolumen tłumaczeń.
7. Zaktualizuj sekcje dotyczące języka/kursu w README, gdy ma to zastosowanie.
8. Deleguj tłumaczenie projektu do `ProjectTranslator`.
9. `ProjectTranslator` deleguje przetwarzanie plików do `TranslationManager`.

`TranslationManager` składa się z wyspecjalizowanych mixinów dla typów plików:

- `ProjectMarkdownTranslationMixin` obsługuje odczyty plików Markdown, tłumaczenie treści, przepisywanie ścieżek, metadane, zastrzeżenia i zapisy.
- `ProjectNotebookTranslationMixin` obsługuje odczyty plików notebook, tłumaczenie komórek Markdown, przepisywanie ścieżek, metadane, zastrzeżenia i zapisy.
- `ProjectImageTranslationMixin` obsługuje wykrywanie obrazów, ekstrakcję/tłumaczenie tekstu, zapisy renderowanych obrazów oraz metadane.

API treści na niższym poziomie pomijają przepływ pracy projektu:

1. `translate_markdown_content` i `translate_notebook_content` tłumaczą tylko zawartość w pamięci.
2. `translate_image_content` tłumaczy tekst w pojedynczym obrazie i zwraca obiekt renderowanego obrazu.
3. `rewrite_markdown_paths` i `rewrite_notebook_paths` są jawymi pomocnikami do postprocessingu. Nie wykonują tłumaczeń ani zapisów projektu.

## Przebieg przeglądu

Deterministyczny przebieg przeglądu to:

1. Parsuj argumenty CLI lub parametry API.
2. Normalizuj żądane kody języków.
3. Zbuduj jeden lub więcej celów przeglądu z `root_dir`, `root_dirs` lub `groups`.
4. Opcjonalnie ogranicz pliki źródłowe za pomocą `--changed-from`.
5. Uruchom deterministyczne kontrole struktury, świeżości tłumaczeń, integralności Markdown i lokalnych ścieżek linków/obrazów.
6. Wydrukuj wyjście w postaci tekstu lub Markdown w stylu GitHub.
7. Zakończ z błędem, gdy wykryte zostaną błędy przeglądu.

Przebieg przeglądu nie wymaga kluczy API i pozostaje dostępny do lokalnych kontroli lub dobrowolnego CI konsumenta. To repozytorium nie uruchamia automatycznie `co-op-review` przy każdym pull request.

## Witryna dokumentacji

Witryna dokumentacji jest konfigurowana przez:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Katalog `docs/` jest kanonicznym źródłem dokumentacji. Nie dodawaj nowych przewodników dla użytkownika końcowego poza tym katalogiem, chyba że projekt celowo wprowadza inny opublikowany obszar dokumentacji.

Buduj lokalnie:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Podglądaj lokalnie:

```bash
python -m mkdocs serve
```

Generowana witryna zapisywana jest do `site/`, który jest ignorowany przez git.

## Przepływ pracy GitHub Pages

`.github/workflows/docs.yml` buduje witrynę na pull requestach i wdraża ją przy pushach do `main`.

Przepływ pracy instaluje:

```bash
pip install -r requirements-docs.txt
```

Workflow dokumentacji instaluje tylko łańcuch narzędzi dokumentacyjnych. `mkdocs.yml` kieruje `mkdocstrings` do `src/`, dzięki czemu strony publicznego API mogą być renderowane z drzewa źródłowego bez instalowania pełnego zestawu zależności środowiska wykonawczego. Jeśli przyszłe dokumenty API będą wymagać importowania opcjonalnych dostawców środowiska wykonawczego podczas budowania, zaktualizuj zarówno `.github/workflows/docs.yml`, jak i ten przewodnik.

## Wymagania jakościowe dokumentacji

Przed scaleniem zmian w dokumentacji uruchom:

```bash
python -m mkdocs build --strict
git diff --check
```

Używaj rygorystycznych buildów, aby złamane linki, nieprawidłowe wpisy w nawigacji i problemy z renderowaniem API były wykrywane na wczesnym etapie.