# Przewodnik dla opiekunów

Ta strona podsumowuje, jak API, CLI i serwis dokumentacji są połączone.

## Publiczna granica API

Stabilne API Pythona jest eksportowane z:

```python
co_op_translator.api
```

Publiczne API jest zorganizowane w pomocniki do tłumaczenia treści, pomocniki do przepisywania ścieżek, orkiestrację projektów oraz przegląd:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
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

Dodając nowe publiczne API, zaktualizuj:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- odpowiednie testy API w `tests/co_op_translator/`, takie jak `test_api.py` lub `test_review_api.py`

Unikaj dokumentowania modułów `core` niższego poziomu jako stabilnego API, chyba że projekt zamierza je wspierać bezpośrednio.

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

`src/co_op_translator/__main__.py` rozdziela według nazwy skryptu:

- `translate` wywołuje `co_op_translator.cli.translate.translate_command`
- `evaluate` wywołuje `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` wywołuje `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` wywołuje `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` omija `__main__.py` i wywołuje bezpośrednio `co_op_translator.mcp.server:main`.

Przy dodawaniu lub zmianie opcji CLI zaktualizuj:

- odpowiedni plik polecenia w `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- testy związane z CLI, jeśli zmienia się zachowanie

## Serwer MCP

Serwer MCP jest zaimplementowany w:

```python
co_op_translator.mcp.server
```

Serwer celowo owija publiczne API Pythona zamiast wywoływać moduły `core` niższego poziomu. Zachowaj tę granicę nienaruszoną, aby klienci MCP, wywołujący z Pythona oraz CLI, dzielili to samo zachowanie.

Przy dodawaniu lub zmianie narzędzi MCP zaktualizuj:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` jeśli powierzchnia publicznego API ulegnie zmianie

Narzędzia do tłumaczenia repozytorium są wywoływalne przez model za pośrednictwem MCP i mogą zapisywać wiele plików. Zachowaj `dry_run=True` jako wartość domyślną i wymagaj `confirm_write=True` przed tłumaczeniem projektu poza trybem dry run.

## Przepływ tłumaczenia

Wysokopoziomowy przepływ tłumaczenia projektu to:

1. Parsuj argumenty CLI lub parametry API.
2. Zweryfikuj konfigurację LLM przy użyciu `LLMConfig`.
3. Zweryfikuj Azure AI Vision, gdy wybrane jest tłumaczenie obrazów.
4. Normalizuj kody języków.
5. Wykryj przestarzałe aliasy folderów językowych.
6. Oszacuj objętość tłumaczenia.
7. Zaktualizuj sekcje README dotyczące języka/kursu, gdy ma to zastosowanie.
8. Deleguj tłumaczenie projektu do `ProjectTranslator`.
9. `ProjectTranslator` deleguje przetwarzanie plików do `TranslationManager`.

`TranslationManager` składa się z wyspecjalizowanych mixinów dla typów plików:

- `ProjectMarkdownTranslationMixin` obsługuje odczyty plików Markdown, tłumaczenie treści, przepisywanie ścieżek, metadane, zastrzeżenia i zapisy.
- `ProjectNotebookTranslationMixin` obsługuje odczyty plików notebooków, tłumaczenie komórek Markdown, przepisywanie ścieżek, metadane, zastrzeżenia i zapisy.
- `ProjectImageTranslationMixin` obsługuje wykrywanie obrazów, ekstrakcję/tłumaczenie tekstu, zapisy renderowanych obrazów oraz metadane.

Niższopoziomowe API treści pomijają przepływ pracy projektu:

1. `translate_markdown_content` i `translate_notebook_content` tłumaczą tylko zawartość w pamięci.
2. `translate_image_content` tłumaczy tekst w pojedynczym obrazie i zwraca wyrenderowany obiekt obrazu.
3. `rewrite_markdown_paths` i `rewrite_notebook_paths` są eksplicytnymi pomocnikami do post-processingu. Nie dokonują tłumaczenia ani zapisów w projekcie.

## Przepływ przeglądu

Deterministyczny przepływ przeglądu to:

1. Parsuj argumenty CLI lub parametry API.
2. Normalizuj żądane kody języków.
3. Zbuduj jeden lub więcej celów przeglądu z `root_dir`, `root_dirs` lub `groups`.
4. Opcjonalnie ogranicz pliki źródłowe za pomocą `--changed-from`.
5. Uruchom deterministyczne kontrole struktury, świeżości tłumaczeń, integralności Markdown i lokalnych ścieżek linków/obrazów.
6. Wypisz wyjście tekstowe lub Markdown w stylu GitHub.
7. Zakończ z błędem, gdy wykryto błędy przeglądu.

Przepływ przeglądu nie wymaga kluczy API i powinien pozostać odpowiedni dla CI pull requestów. Workflow pull requesta zapisuje podsumowanie kontroli przy każdym uruchomieniu i dodaje komentarz do PR tylko wtedy, gdy `co-op-review` zakończy się niepowodzeniem.

## Strona dokumentacji

Serwis dokumentacji jest konfigurowany przez:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Katalog `docs/` jest kanonicznym źródłem dokumentacji. Nie dodawaj nowych przewodników dla użytkowników końcowych poza tym katalogiem, chyba że projekt celowo wprowadza inną opublikowaną powierzchnię dokumentacji.

Build lokalnie:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Podgląd lokalny:

```bash
python -m mkdocs serve
```

Wygenerowana strona zapisywana jest do `site/`, który jest ignorowany przez git.

## Workflow GitHub Pages

.github/workflows/docs.yml buduje stronę na pull requesty i wdraża ją przy pushach do `main`.

Workflow instaluje:

```bash
pip install -r requirements-docs.txt
```

Workflow dokumentacji instaluje tylko toolchain dokumentacji. `mkdocs.yml` wskazuje `mkdocstrings` na `src/`, dzięki czemu strony publicznego API mogą być renderowane z drzewa źródłowego bez instalowania pełnego zestawu zależności w czasie wykonania. Jeśli przyszła dokumentacja API będzie wymagać importu opcjonalnych dostawców runtime podczas budowy, zaktualizuj zarówno `.github/workflows/docs.yml`, jak i ten przewodnik.

## Próg jakości dokumentacji

Przed scaleniem zmian w dokumentacji uruchom:

```bash
python -m mkdocs build --strict
git diff --check
```

Stosuj rygorystyczne buildy, aby złamane linki, nieprawidłowe wpisy nawigacji i problemy z renderowaniem API kończyły się niepowodzeniem na wczesnym etapie.