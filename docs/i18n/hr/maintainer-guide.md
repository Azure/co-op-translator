# Vodič za održavatelje

Ova stranica sažima kako su API, CLI i stranica s dokumentacijom međusobno povezani.

## Granica javnog API-ja

Stabilni Python API izvezen je iz:

```python
co_op_translator.api
```

Javni API organiziran je u pomoćnike za prevođenje sadržaja, pomoćnike za prepisivanje putanja, orkestraciju projekata i pregled:

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

`TranslationStateProvider` je granica za trajnu pohranu za hostirane integracije.
Mora držati generirane kandidate odvojeno od prihvaćenih osnovnih verzija tako da
ne-spojeni prijevod ne postane izvor istine.

Prilikom dodavanja novih javnih API-ja, ažurirajte:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- odgovarajući API testovi u `tests/co_op_translator/`, kao što su `test_api.py` ili `test_review_api.py`

Izbjegavajte dokumentiranje niže razine `core` modula kao stabilnog API-ja, osim ako projekt ne namjerava izravno podržavati te module.

## Ulazne točke CLI-ja

Paket definira ove Poetry skripte:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` preusmjerava prema nazivu skripte:

- `translate` poziva `co_op_translator.cli.translate.translate_command`
- `evaluate` poziva `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` poziva `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` poziva `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` zaobilazi `__main__.py` i izravno poziva `co_op_translator.mcp.server:main`.

Prilikom dodavanja ili mijenjanja CLI opcija, ažurirajte:

- odgovarajuću naredbu u `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- testovi vezani uz CLI, ako se ponašanje promijeni

## MCP poslužitelj

MCP poslužitelj je implementiran u:

```python
co_op_translator.mcp.server
```

Poslužitelj namjerno obuhvaća javni Python API umjesto da poziva niže razine `core` module. Ostavite ovu granicu netaknutom tako da MCP klijenti, Python pozivatelji i CLI dijele isto ponašanje.

Prilikom dodavanja ili mijenjanja MCP alata, ažurirajte:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` ako se javna površina API-ja promijeni

Alati za prevođenje u repozitoriju mogu se pozivati putem modela kroz MCP i mogu zapisati mnogo datoteka. Ostavite `dry_run=True` kao zadanu vrijednost i zahtijevajte `confirm_write=True` prije izvođenja prevođenja projekta bez suhog pokusa.

## Tijek prevođenja

Opći tijek prevođenja projekta je:

1. Parsirajte CLI argumente ili API parametre.
2. Provjerite konfiguraciju LLM-a s `LLMConfig`.
3. Provjerite Azure AI Vision kada je odabrano prevođenje slika.
4. Normalizirajte kodove jezika.
5. Otkrivanje zastarjelih aliasa za mape jezika.
6. Procijenite opseg prevođenja.
7. Ažurirajte odjeljke jezika/tečaja u README-u kad je primjenjivo.
8. Delegirajte prevođenje projekta na `ProjectTranslator`.
9. `ProjectTranslator` delegira obradu datoteka na `TranslationManager`.

`TranslationManager` sastoji se od fokusiranih mixina za vrste datoteka:

- `ProjectMarkdownTranslationMixin` upravlja čitanjem Markdown datoteka, prevođenjem sadržaja, prepisivanjem putanja, metapodacima, izjavama o odricanju odgovornosti i zapisivanjem.
- `ProjectNotebookTranslationMixin` upravlja čitanjem notebook datoteka, prevođenjem Markdown ćelija, prepisivanjem putanja, metapodacima, izjavama o odricanju odgovornosti i zapisivanjem.
- `ProjectImageTranslationMixin` upravlja pronalaženjem slika, izdvajanje i prevođenjem teksta, zapisivanjem renderiranih slika i metapodacima.

Niže razine API-ja za sadržaj preskaču projektni tijek rada:

1. `translate_markdown_content` i `translate_notebook_content` prevode samo sadržaj u memoriji.
2. `translate_image_content` prevodi tekst na pojedinačnoj slici i vraća renderirani objekt slike.
3. `rewrite_markdown_paths` i `rewrite_notebook_paths` su eksplicitni pomoćnici za naknadnu obradu. Ne obavljaju prevođenje niti zapisuju u projekt.

## Tijek pregleda

Deterministički tijek pregleda je:

1. Parsirajte CLI argumente ili API parametre.
2. Normalizirajte tražene kodove jezika.
3. Izgradite jedan ili više ciljeva pregleda iz `root_dir`, `root_dirs` ili `groups`.
4. Opcionalno ograničite izvorne datoteke pomoću `--changed-from`.
5. Pokrenite determinističke provjere za strukturu, svježinu prijevoda, integritet Markdowna i lokalne putanje poveznica/slika.
6. Ispišite ili tekstualni izlaz ili Markdown u GitHub stilu.
7. Izađite s greškom ako se pronađu pogreške pri pregledu.

Tijek pregleda ne zahtijeva API ključeve i dostupan je za lokalne provjere ili za CI koji korisnik uključi (opt-in). Ovaj repozitorij ne pokreće `co-op-review` automatski za svaki pull request.

## Stranica dokumentacije

Stranica s dokumentacijom konfigurirana je pomoću:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Direktorij `docs/` je kanonski izvor dokumentacije. Ne dodajte nove vodiče za krajnjeg korisnika izvan ovog direktorija osim ako projekt namjerno ne uvodi drugo javno dostupno mjesto dokumentacije.

Izgradite lokalno:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview lokalno:

```bash
python -m mkdocs serve
```

Generirana stranica zapisuje se u `site/`, koja je ignorirana od strane gita.

## GitHub Pages radni tijek

`.github/workflows/docs.yml` izgrađuje stranicu za pull requestove i postavlja je pri pushu na `main`.

Radni tijek instalira:

```bash
pip install -r requirements-docs.txt
```

Radni tijek za dokumentaciju instalira samo alatni lanac za dokumentaciju. `mkdocs.yml` usmjerava `mkdocstrings` na `src/` tako da se stranice javnog API-ja mogu renderirati iz izvornog stabla bez instaliranja kompletnog skupa runtime ovisnosti. Ako buduće API dokumentacije zahtijevaju uvoz opcionalnih runtime providera tijekom izgradnje, ažurirajte `.github/workflows/docs.yml` i ovaj vodič zajedno.

## Kriteriji kvalitete dokumentacije

Prije spajanja promjena dokumentacije, pokrenite:

```bash
python -m mkdocs build --strict
git diff --check
```

Koristite strogu izgradnju kako bi slomljene poveznice, neispravni unosi u navigaciji i problemi pri prikazu API-ja bili otkriveni na vrijeme.