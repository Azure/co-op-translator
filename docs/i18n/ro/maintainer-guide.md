# Ghid pentru menținători

Această pagină rezumă modul în care API-ul, CLI-ul și site-ul de documentație sunt conectate.

## Frontiera API-ului public

API-ul Python stabil este exportat din:

```python
co_op_translator.api
```

API-ul public este organizat în ajutoare pentru traducerea conținutului, ajutoare pentru rescrierea căilor, orchestrarea proiectelor și revizuire:

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

`TranslationStateProvider` este limita de persistență pentru integrările găzduite.
Trebuie să păstreze candidații generați separați de bazele acceptate astfel încât o
traducere necombinată să nu devină sursa adevărului.

Atunci când adăugați noi API-uri publice, actualizați:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- teste relevante ale API-ului din `tests/co_op_translator/`, cum ar fi `test_api.py` sau `test_review_api.py`

Evitați documentarea modulelor `core` de nivel inferior ca API-uri stabile, cu excepția cazului în care proiectul intenționează să le susțină direct.

## Puncte de intrare CLI

Pachetul definește aceste scripturi Poetry:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` direcționează în funcție de numele scriptului:

- `translate` calls `co_op_translator.cli.translate.translate_command`
- `evaluate` calls `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` calls `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` calls `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` ocolește `__main__.py` și apelează direct `co_op_translator.mcp.server:main`.

Când adăugați sau modificați opțiuni CLI, actualizați:

- comanda relevantă din `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- teste legate de CLI, dacă comportamentul se schimbă

## Server MCP

Serverul MCP este implementat în:

```python
co_op_translator.mcp.server
```

Serverul în mod intenționat înfășoară API-ul Python public în loc să apeleze module `core` de nivel inferior. Păstrați această limită intactă astfel încât clienții MCP, apelanții Python și CLI-ul să împărtășească același comportament.

Când adăugați sau modificați instrumente MCP, actualizați:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` dacă suprafața API-ului public se modifică

Uneltele de traducere ale depozitului pot fi apelate de model prin MCP și pot scrie multe fișiere. Păstrați `dry_run=True` ca implicit și cereți `confirm_write=True` înainte de traducerea proiectului care nu este în modul dry_run.

## Fluxul de traducere

Fluxul general de traducere al proiectului este:

1. Parseați argumentele CLI sau parametrii API.
2. Validați configurația LLM cu `LLMConfig`.
3. Validați Azure AI Vision atunci când este selectată traducerea imaginilor.
4. Normalizați codurile limbilor.
5. Detectați aliasurile folderelor de limbă vechi.
6. Estimați volumul traducerii.
7. Actualizați secțiunile de limbă/curs din README când este cazul.
8. Delegați traducerea proiectului către `ProjectTranslator`.
9. `ProjectTranslator` delegă procesarea fișierelor către `TranslationManager`.

`TranslationManager` este compus din mixin-uri pentru tipuri de fișiere specializate:

- `ProjectMarkdownTranslationMixin` se ocupă de citirea fișierelor Markdown, traducerea conținutului, rescrierea căilor, gestionarea metadatelor, avertismente și scrieri.
- `ProjectNotebookTranslationMixin` se ocupă de citirea fișierelor notebook, traducerea celulelor Markdown, rescrierea căilor, gestionarea metadatelor, avertismente și scrieri.
- `ProjectImageTranslationMixin` se ocupă de descoperirea imaginilor, extragerea/traducerea textului, scrierea imaginilor procesate și metadatele.

API-urile de conținut de nivel inferior sar peste fluxul de lucru al proiectului:

1. `translate_markdown_content` și `translate_notebook_content` traduc doar conținut din memorie.
2. `translate_image_content` traduce textul dintr-o singură imagine și returnează un obiect imagine redat.
3. `rewrite_markdown_paths` și `rewrite_notebook_paths` sunt ajutoare explicite de post-procesare. Ele nu efectuează nicio traducere și nu scriu fișiere în proiect.

## Fluxul de revizuire

Fluxul determinist de revizuire este:

1. Parseați argumentele CLI sau parametrii API.
2. Normalizați codurile de limbă solicitate.
3. Construiți unul sau mai multe ținte de revizuire din `root_dir`, `root_dirs` sau `groups`.
4. Opțional limitați fișierele sursă cu `--changed-from`.
5. Rulați verificări deterministe pentru structură, prospețimea traducerii, integritatea Markdown și căile locale ale link-urilor/imaginilor.
6. Afișați fie ieșire text, fie Markdown în stil GitHub.
7. Ieșiți cu eșec când se găsesc erori de revizuire.

Fluxul de revizuire nu necesită chei API și rămâne disponibil pentru verificări locale sau CI opțional pentru consumatori. Acest depozit nu rulează `co-op-review` automat la fiecare pull request.

## Site-ul de documentație

Site-ul de documentație este configurat de:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Directorul `docs/` este sursa canonică a documentației. Nu adăugați noi ghiduri pentru utilizatorii finali în afara acestui director decât dacă proiectul introduce în mod intenționat o altă suprafață de documentație publicată.

Build locally:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview locally:

```bash
python -m mkdocs serve
```

Site-ul generat este scris în `site/`, care este ignorat de git.

## Flux de lucru GitHub Pages

`.github/workflows/docs.yml` construiește site-ul pentru pull request-uri și îl publică la push-uri pe `main`.

Fluxul de lucru instalează:

```bash
pip install -r requirements-docs.txt
```

Fluxul de lucru pentru documentație instalează doar lanțul de instrumente pentru documentație. `mkdocs.yml` directionează `mkdocstrings` către `src/` astfel încât paginile API publice pot fi generate din arborele sursă fără a instala întregul set de dependențe de runtime. Dacă documentația API viitoare necesită importarea provider-ilor opționali de runtime în timpul build-ului, actualizați atât `.github/workflows/docs.yml`, cât și acest ghid împreună.

## Standardul de calitate al documentației

Înainte de a îmbina modificările de documentație, rulați:

```bash
python -m mkdocs build --strict
git diff --check
```

Folosiți build-uri stricte astfel încât link-urile rupte, intrările de navigație invalide și problemele de redare a API-ului să eșueze devreme.