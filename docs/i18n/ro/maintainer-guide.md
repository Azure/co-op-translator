# Ghid pentru întreținători

Această pagină rezumă cum sunt legate împreună API-ul, CLI-ul și site-ul de documentație.

## Limita API-ului public

API-ul Python stabil este exportat din:

```python
co_op_translator.api
```

API-ul public este organizat în ajutoare pentru traducerea conținutului, ajutoare pentru rescrierea căilor, orchestrarea proiectului și revizuire:

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

Când adăugați noi API-uri publice, actualizați:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

Evitați documentarea modulelor `core` de nivel inferior ca API stabil decât dacă proiectul intenționează să le suporte direct.

## Punctele de intrare CLI

Pachetul definește aceste scripturi Poetry:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` redirecționează în funcție de numele scriptului:

- `translate` apelează `co_op_translator.cli.translate.translate_command`
- `evaluate` apelează `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` apelează `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` apelează `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` ocolește `__main__.py` și apelează direct `co_op_translator.mcp.server:main`.

Când adăugați sau modificați opțiuni CLI, actualizați:

- comanda relevantă `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- teste legate de CLI, dacă comportamentul se schimbă

## Server MCP

Serverul MCP este implementat în:

```python
co_op_translator.mcp.server
```

Serverul înfășoară intenționat API-ul Python public în loc să apeleze modulele `core` de nivel inferior. Păstrați această delimitare intactă astfel încât clienții MCP, apelanții Python și CLI-ul să partajeze același comportament.

Când adăugați sau modificați unelte MCP, actualizați:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

Uneltele de traducere din repository pot fi apelate de modele prin MCP și pot scrie multe fișiere. Păstrați `dry_run=True` ca implicit și cereți `confirm_write=True` înainte de traducerea proiectului care nu este în modul dry-run.

## Fluxul de traducere

Fluxul de traducere la nivel înalt al proiectului este:

1. Parseați argumentele CLI sau parametrii API.
2. Validați configurația LLM cu `LLMConfig`.
3. Validați Azure AI Vision când este selectată traducerea imaginilor.
4. Normalizați codurile de limbă.
5. Detectați aliasurile folderelor de limbă vechi.
6. Estimați volumul traducerii.
7. Actualizați secțiunile de limbă/curs din README când este cazul.
8. Delegați traducerea proiectului către `ProjectTranslator`.
9. `ProjectTranslator` delegă procesarea fișierelor către `TranslationManager`.

`TranslationManager` este compus din mixin-uri focalizate pe tipuri de fișiere:

- `ProjectMarkdownTranslationMixin` se ocupă de citirea fișierelor Markdown, traducerea conținutului, rescrierea căilor, metadate, avertismente și scrierea fișierelor.
- `ProjectNotebookTranslationMixin` se ocupă de citirea fișierelor notebook, traducerea celulelor Markdown, rescrierea căilor, metadate, avertismente și scrierea fișierelor.
- `ProjectImageTranslationMixin` se ocupă de descoperirea imaginilor, extragerea/traducerea textului, scrierea imaginilor generate și metadate.

API-urile de conținut la nivel inferior ocolesc fluxul de lucru al proiectului:

1. `translate_markdown_content` și `translate_notebook_content` traduc doar conținutul din memorie.
2. `translate_image_content` traduce textul dintr-o singură imagine și returnează un obiect imagine randat.
3. `rewrite_markdown_paths` și `rewrite_notebook_paths` sunt ajutoare explicite de post-procesare. Ele nu realizează nicio traducere și nici scrieri în proiect.

## Fluxul de revizuire

Fluxul de revizuire determinist este:

1. Parseați argumentele CLI sau parametrii API.
2. Normalizați codurile de limbă solicitate.
3. Construiți unul sau mai multe ținte de revizuire din `root_dir`, `root_dirs` sau `groups`.
4. Opțional limitați fișierele sursă cu `--changed-from`.
5. Rulați verificări deterministe pentru structură, prospețimea traducerilor, integritatea Markdown și căile locale pentru linkuri/imagini.
6. Afișați fie ieșare text, fie Markdown în stil GitHub.
7. Ieșiți cu o eroare când se găsesc erori de revizuire.

Fluxul de revizuire nu necesită chei API și ar trebui să rămână potrivit pentru CI-ul pull request-urilor. Fluxul de lucru pentru pull request scrie un rezumat al verificării la fiecare rulare și postează un comentariu pe PR doar când `co-op-review` eșuează.

## Site-ul de documentație

Site-ul de documentație este configurat de:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Directorul `docs/` este sursa canonică de documentație. Nu adăugați ghiduri noi pentru utilizatori finali în afara acestui director decât dacă proiectul introduce în mod intenționat o altă suprafață de documentație publicată.

Build locally:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Previzualizați local:

```bash
python -m mkdocs serve
```

Site-ul generat este scris în `site/`, care este ignorat de git.

## Fluxul de lucru GitHub Pages

`.github/workflows/docs.yml` construiește site-ul pe pull request-uri și îl distribuie la push-urile către `main`.

Fluxul de lucru instalează:

```bash
pip install -r requirements-docs.txt
```

Fluxul de lucru pentru documentație instalează doar lanțul de unelte pentru documentare. `mkdocs.yml` indică `mkdocstrings` către `src/` astfel încât paginile API publice pot fi generate din arborele sursă fără a instala setul complet de dependențe runtime. Dacă documentația API viitoare necesită importarea providerilor opționali de runtime în timpul compilării, actualizați atât `.github/workflows/docs.yml`, cât și acest ghid împreună.

## Standardul de calitate al documentației

Înainte de a îmbina modificările din documentație, rulați:

```bash
python -m mkdocs build --strict
git diff --check
```

Folosiți build-uri stricte astfel încât link-urile rupte, intrările invalide din navigație și problemele de redare a API-ului să eșueze devreme.