# Vodnik za vzdrževalce

Ta stran povzema, kako so API, CLI in dokumentacijsko mesto med seboj povezani.

## Meja javnega API-ja

Stabilni Python API je izpostavljen iz:

```python
co_op_translator.api
```

Javni API je organiziran v pomočnike za prevajanje vsebine, pomočnike za prepis poti, orkestracijo projektov in pregled:

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

`TranslationStateProvider` je meja za trajno shranjevanje za gostovane integracije.
Mora hraniti generirane kandidate ločeno od sprejetih osnovnih različic, tako da
nezdružen prevod ne sme postati zanesljiv vir.

Ko dodajate nove javne API-je, posodobite:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- ustrezni API testi v `tests/co_op_translator/`, na primer `test_api.py` ali `test_review_api.py`

Izogibajte se dokumentiranju nižjenivojskih `core` modulov kot stabilnega API-ja, razen če projekt namerava neposredno podpirati te module.

## Vstopne točke CLI

Paket definira naslednje Poetry skripte:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` preusmerja po imenu skripte:

- `translate` kliče `co_op_translator.cli.translate.translate_command`
- `evaluate` kliče `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` kliče `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` kliče `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` zaobide `__main__.py` in neposredno pokliče `co_op_translator.mcp.server:main`.

Ko dodajate ali spreminjate CLI možnosti, posodobite:

- ustrezen ukaz v `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- teste povezane s CLI, če se vedenje spremeni

## MCP strežnik

MCP strežnik je implementiran v:

```python
co_op_translator.mcp.server
```

Strežnik namenoma ovije javni Python API namesto klicanja nižjenivojskih `core` modulov. Ohranite to mejo nedotaknjeno, da bodo MCP klienti, Python klicatelji in CLI imeli enako vedenje.

Ko dodajate ali spreminjate MCP orodja, posodobite:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` če se površina javnega API-ja spremeni

Orodja za prevajanje repozitorija so klicljiva preko MCP in lahko zapišejo veliko datotek. Ohranite `dry_run=True` kot privzeto in zahtevajte `confirm_write=True` pred prevajanjem projekta brez `dry_run`.

## Potek prevajanja

Visokonivojski potek prevajanja projekta je:

1. Analizirajte CLI argumente ali API parametre.
2. Preverite konfiguracijo LLM z `LLMConfig`.
3. Preverite Azure AI Vision, ko je izbrano prevajanje slik.
4. Normalizirajte kode jezikov.
5. Zaznajte zastarele alias-e map jezikov.
6. Ocenite obseg prevajanja.
7. Posodobite odseke README o jeziku/tečaju, kadar je to primerno.
8. Delegirajte prevajanje projekta na `ProjectTranslator`.
9. `ProjectTranslator` delegira obdelavo datotek na `TranslationManager`.

`TranslationManager` je sestavljen iz mixinov, osredotočenih na vrste datotek:

- `ProjectMarkdownTranslationMixin` obravnava branje Markdown datotek, prevajanje vsebine, prepisovanje poti, metapodatke, omejitve odgovornosti in zapise.
- `ProjectNotebookTranslationMixin` obravnava branje datotek zvezkov, prevajanje Markdown celic, prepisovanje poti, metapodatke, omejitve odgovornosti in zapise.
- `ProjectImageTranslationMixin` obravnava iskanje slik, izvleček/prevod besedila, zapis renderiranih slik in metapodatke.

Nižjenivojski API-ji za vsebino preskočijo delovni tok projekta:

1. `translate_markdown_content` in `translate_notebook_content` prevajata samo vsebino v pomnilniku.
2. `translate_image_content` prevede besedilo v eni sliki in vrne upodobljen objekt slike.
3. `rewrite_markdown_paths` in `rewrite_notebook_paths` so eksplicitni pripomočki za post-obdelavo. Ne izvajajo prevajanja in ne zapisujejo v projekt.

## Potek pregleda

Deterministični potek pregleda je:

1. Analizirajte CLI argumente ali API parametre.
2. Normalizirajte zahtevane kode jezikov.
3. Sestavite eno ali več ciljev pregleda iz `root_dir`, `root_dirs` ali `groups`.
4. Po potrebi omejite izvorne datoteke z `--changed-from`.
5. Zaženite deterministične preverbe strukture, svežine prevodov, integritete Markdowna in lokalnih poti povezav in slik.
6. Izpišite bodisi besedilni izhod ali Markdown v GitHub različici.
7. Izhodite z napako, kadar so najdene napake pri pregledu.

Potek pregleda ne zahteva API ključev in ostaja na voljo za lokalne preglede ali CI, v katerega se uporabnik vključi. Ta repozitorij ne zažene `co-op-review` samodejno pri vsakem pull requestu.

## Spletno mesto dokumentacije

Spletno mesto z dokumentacijo je konfigurirano z:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Map a `docs/` je kanoničen vir dokumentacije. Ne dodajajte novih uporabniških vodičev izven tega imenika, razen če projekt namerno uvede drugo objavljeno dokumentacijsko površino.

Zgradite lokalno:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Predogled lokalno:

```bash
python -m mkdocs serve
```

Ustvarjeno spletno mesto se zapiše v `site/`, ki ga git ignorira.

## Potek dela GitHub Pages

`.github/workflows/docs.yml` zgradi spletno mesto ob pull requestih in ga namesti ob pushih v `main`.

Potek dela namesti:

```bash
pip install -r requirements-docs.txt
```

Potek dokumentacije namesti le orodja za dokumentacijo. `mkdocs.yml` usmeri `mkdocstrings` na `src/`, tako da se strani javnega API-ja lahko upodobijo iz izvornega drevesa brez nameščanja celotnega nabora runtime odvisnosti. Če bodo prihodnje API dokumentacije zahtevale uvoz neobveznih runtime providerjev med gradnjo, posodobite tako `.github/workflows/docs.yml` kot ta vodnik.

## Standard kakovosti dokumentacije

Pred združitvijo sprememb v dokumentaciji zaženite:

```bash
python -m mkdocs build --strict
git diff --check
```

Uporabljajte stroge gradnje, da napačne povezave, neveljavni vnosi v navigaciji in težave pri upodabljanju API-ja odpovejo zgodaj.