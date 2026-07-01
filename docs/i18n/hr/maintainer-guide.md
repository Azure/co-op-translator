# Vodič za održavatelje

Ova stranica sažima kako su API, CLI i stranica dokumentacije povezani.

## Granica javnog API-ja

Stabilni Python API izvezen je iz:

```python
co_op_translator.api
```

Javni API organiziran je u pomoćnike za prevođenje sadržaja, pomoćnike za prepisivanje putanja, orkestraciju projekta i pregled:

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

Prilikom dodavanja novih javnih API-ja, ažurirajte:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevantne API testove pod `tests/co_op_translator/`, kao što su `test_api.py` ili `test_review_api.py`

Izbjegavajte dokumentirati niže razine `core` modula kao stabilni API osim ako projekt namjerava izravno podržavati te module.

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

`src/co_op_translator/__main__.py` prosljeđuje prema nazivu skripte:

- `translate` poziva `co_op_translator.cli.translate.translate_command`
- `evaluate` poziva `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` poziva `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` poziva `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` zaobilazi `__main__.py` i poziva `co_op_translator.mcp.server:main` izravno.

Prilikom dodavanja ili promjene CLI opcija, ažurirajte:

- relevantnu `src/co_op_translator/cli/*.py` naredbu
- `docs/cli.md`
- testove povezane s CLI-jem, ako se ponašanje promijeni

## MCP poslužitelj

MCP poslužitelj je implementiran u:

```python
co_op_translator.mcp.server
```

Poslužitelj namjerno koristi javni Python API umjesto pozivanja niže razine `core` modula. Održavajte ovu granicu netaknutom kako bi MCP klijenti, Python pozivači i CLI dijelili isto ponašanje.

Prilikom dodavanja ili promjene MCP alata, ažurirajte:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` ako se površina javnog API-ja promijeni

Alati za prevođenje repozitorija mogu se pozivati modelom preko MCP-a i mogu pisati mnogo datoteka. Ostavite `dry_run=True` kao zadano i zahtijevajte `confirm_write=True` prije prevođenja projekta koje nije suho pokretanje.

## Tijek prevođenja

Visokorazinski tijek prevođenja projekta je:

1. Parsiranje CLI argumenata ili API parametara.
2. Validacija LLM konfiguracije s `LLMConfig`.
3. Validacija Azure AI Vision kada je odabrano prevođenje slika.
4. Normaliziranje kodova jezika.
5. Otkrivanje zastarjelih aliasa mapa jezika.
6. Procjena opsega prevođenja.
7. Ažuriranje README odjeljaka za jezik/predmet kad je primjenjivo.
8. Delegiranje prevođenja projekta na `ProjectTranslator`.
9. `ProjectTranslator` delegira obradu datoteka na `TranslationManager`.

`TranslationManager` je sastavljen od mixinova fokusiranih na tipove datoteka:

- `ProjectMarkdownTranslationMixin` rukuje čitanjem Markdown datoteka, prevođenjem sadržaja, prepisivanjem putanja, metapodacima, izjavama o odricanju odgovornosti i zapisivanjem.
- `ProjectNotebookTranslationMixin` rukuje čitanjem datoteka bilježnice, prevođenjem Markdown-ćelija, prepisivanjem putanja, metapodacima, izjavama o odricanju odgovornosti i zapisivanjem.
- `ProjectImageTranslationMixin` rukuje otkrivanjem slika, ekstrakcijom/prevođenjem teksta, zapisivanjem renderiranih slika i metapodacima.

Niže razine API-ja za sadržaj preskaču tijek rada projekta:

1. `translate_markdown_content` i `translate_notebook_content` prevode samo sadržaj u memoriji.
2. `translate_image_content` prevodi tekst u jednoj slici i vraća renderirani objekt slike.
3. `rewrite_markdown_paths` i `rewrite_notebook_paths` su eksplicitni pomoćnici za postprocesiranje. Ne izvode prevođenje niti zapise projekta.

## Tijek pregleda

Deterministički tijek pregleda je:

1. Parsiranje CLI argumenata ili API parametara.
2. Normaliziranje traženih kodova jezika.
3. Sastavljanje jednog ili više ciljeva pregleda iz `root_dir`, `root_dirs` ili `groups`.
4. Opcionalno ograničavanje izvornih datoteka s `--changed-from`.
5. Pokretanje determinističkih provjera strukture, svježine prijevoda, integriteta Markdowna i lokalnih putanja linkova/slika.
6. Ispisivanje ili tekstualnog izlaza ili Markdowna u GitHub stilu.
7. Izlaz s neuspjehom kada se pronađu pogreške u pregledu.

Tijek pregleda ne zahtijeva API ključeve i trebao bi ostati prikladan za CI u pull requestovima. Radni tok za pull request zapisuje sažetak provjere pri svakom pokretanju i objavljuje komentar na PR samo kada `co-op-review` ne uspije.

## Stranica dokumentacije

Stranica s dokumentacijom konfigurirana je pomoću:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Direktorij `docs/` je kanonski izvor dokumentacije. Nemojte dodavati nove vodiče za krajnje korisnike izvan ovog direktorija osim ako projekt namjerno ne uvede drugo objavljeno mjesto dokumentacije.

Izgradite lokalno:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Pregledajte lokalno:

```bash
python -m mkdocs serve
```

Generirana stranica se zapisuje u `site/`, koji git ignorira.

## Radni tok GitHub Pages

`.github/workflows/docs.yml` gradi stranicu na pull requestovima i objavljuje je na push-evima na `main`.

Radni tok instalira:

```bash
pip install -r requirements-docs.txt
```

Radni tok za dokumentaciju instalira samo alatni lanac za dokumentaciju. `mkdocs.yml` usmjerava `mkdocstrings` na `src/` tako da se stranice javnog API-ja mogu prikazati iz izvornog stabla bez instaliranja kompletnog skupa runtime ovisnosti. Ako buduće API dokumentacije zahtijevaju uvoz opcionalnih runtime providera tijekom izgradnje, ažurirajte i `.github/workflows/docs.yml` i ovaj vodič zajedno.

## Standard kvalitete dokumentacije

Prije spajanja promjena dokumentacije, pokrenite:

```bash
python -m mkdocs build --strict
git diff --check
```

Koristite stroge buildove kako bi slomljeni linkovi, nevažeći unosi u navigaciji i problemi s prikazivanjem API-ja izazvali greške rano.