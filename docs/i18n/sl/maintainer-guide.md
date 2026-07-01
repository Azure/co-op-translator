# Vodnik za vzdrževalce

Ta stran povzema, kako sta API, CLI in spletno mesto dokumentacije medsebojno povezana.

## Meja javnega API-ja

Stabilni Python API je izpostavljen iz:

```python
co_op_translator.api
```

Javni API je organiziran v pomočnike za prevajanje vsebine, pomočnike za prepisovanje poti, orkestracijo projektov in pregled:

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

Ko dodajate nove javne API-je, posodobite:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- ustrezne teste API pod `tests/co_op_translator/`, kot so `test_api.py` ali `test_review_api.py`

Izogibajte se dokumentiranju nižjenivojskih modulov `core` kot stabilnega API-ja, razen če projekt namerno podpira njihovo neposredno uporabo.

## Vhodne točke za CLI

Paket definira te Poetry skripte:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` napotuje po imenu skripte:

- `translate` pokliče `co_op_translator.cli.translate.translate_command`
- `evaluate` pokliče `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` pokliče `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` pokliče `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` zaobide `__main__.py` in neposredno pokliče `co_op_translator.mcp.server:main`.

Ko dodajate ali spreminjate možnosti CLI, posodobite:

- ustrezen ukaz v `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- teste povezane s CLI, če se vedenje spremeni

## MCP strežnik

MCP strežnik je implementiran v:

```python
co_op_translator.mcp.server
```

Strežnik namerno ovije javni Python API namesto neposrednega klica nižjenivojskih `core` modulov. Ohranjajte to mejo nedotaknjeno, da bodo MCP odjemalci, klicatelji v Pythonu in CLI delili enako vedenje.

Ko dodajate ali spreminjate orodja MCP, posodobite:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` če se spremeni površina javnega API-ja

Orodja za prevajanje repozitorija so priklicna z modelom preko MCP in lahko pišejo veliko datotek. Ohranjajte `dry_run=True` kot privzeto in zahtevajte `confirm_write=True` pred ne-dry-run prevajanjem projekta.

## Potek prevajanja

Visokonivojski potek prevajanja projekta je:

1. Analiziraj argumente CLI ali parametre API-ja.
2. Preveri konfiguracijo LLM z `LLMConfig`.
3. Preveri Azure AI Vision, kadar je izbrano prevajanje slik.
4. Normaliziraj kode jezikov.
5. Zaznaj zastarele nadomestne mape jezikov.
6. Oceni obseg prevajanja.
7. Posodobi razdelke README o jeziku/tečaju, kadar je primerno.
8. Prenesi prevajanje projekta na `ProjectTranslator`.
9. `ProjectTranslator` prenese obdelavo datotek na `TranslationManager`.

`TranslationManager` je sestavljen iz mixinov za posamezne tipe datotek:

- `ProjectMarkdownTranslationMixin` obravnava branje Markdown datotek, prevajanje vsebine, prepisovanje poti, metapodatke, opozorila in zapisovanje.
- `ProjectNotebookTranslationMixin` obravnava branje datotek beležnic, prevajanje Markdown celic, prepisovanje poti, metapodatke, opozorila in zapisovanje.
- `ProjectImageTranslationMixin` obravnava odkrivanje slik, izvleček besedila/prevajanje, zapisovanje upodobljenih slik in metapodatke.

Nižjenivojski vsebinski API-ji preskočijo potek projekta:

1. `translate_markdown_content` in `translate_notebook_content` prevajata samo vsebino v pomnilniku.
2. `translate_image_content` prevede besedilo v eni sliki in vrne upodobljen objekt slike.
3. `rewrite_markdown_paths` in `rewrite_notebook_paths` so eksplicitni pomočniki za post-procesiranje. Ne izvajajo prevajanja in ne pišejo v projekt.

## Potek pregleda

Deterministični potek pregleda je:

1. Analiziraj argumente CLI ali parametre API-ja.
2. Normaliziraj zahtevane kode jezikov.
3. Sestavi enega ali več ciljev pregleda iz `root_dir`, `root_dirs` ali `groups`.
4. Po želji omeji izvorne datoteke z `--changed-from`.
5. Zaženi deterministične preglede za strukturo, svežino prevodov, celovitost Markdowna in poti lokalnih povezav/slik.
6. Izpiši bodisi besedilni izhod ali Markdown v GitHub slogu.
7. Izhod z napako, če so najdene napake pregleda.

Potek pregleda ne zahteva API ključev in naj ostane primeren za CI v pull requestih. Delovni tok pull requesta zapiše povzetek preverjanja pri vsakem zagonu in objavi komentar na PR le, ko `co-op-review` ne uspe.

## Spletna stran dokumentacije

Spletna stran z dokumentacijo je konfigurirana z:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Mapa `docs/` je kanoničen vir dokumentacije. Ne dodaj novih uporabniških vodnikov zunaj tega imenika, razen če projekt namerno uvede drugo objavljeno dokumentacijsko površino.

Zgradi lokalno:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Predogled lokalno:

```bash
python -m mkdocs serve
```

Generirana stran je zapisana v `site/`, ki ga git ignorira.

## Delovni tok GitHub Pages

`.github/workflows/docs.yml` zgradi stran ob pull requestih in jo objavi ob pushih v `main`.

Delovni tok namesti:

```bash
pip install -r requirements-docs.txt
```

Delovni tok za dokumentacijo namesti samo verigo orodij za dokumentacijo. `mkdocs.yml` usmeri `mkdocstrings` na `src/`, tako da je mogoče strani javnega API-ja upodobiti iz vira brez namestitve celotnega nabora odvisnosti za runtime. Če bodo prihodnje API dokumentacije zahtevale uvoz izbirnih izvajalcev med gradnjo, posodobi hkrati `.github/workflows/docs.yml` in ta vodič.

## Standard kakovosti dokumentacije

Pred združitvijo sprememb dokumentacije zaženi:

```bash
python -m mkdocs build --strict
git diff --check
```

Uporabi stroge gradnje, da se pokvarjene povezave, neveljavni vnosi v navigaciji in težave pri upodabljanju API-ja zaznajo zgodaj.