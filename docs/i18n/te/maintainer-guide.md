# నిర్వహణ గైడ్

This page summarizes how the API, CLI, and documentation site are wired together.

## పబ్లిక్ API సరిహద్దు

The stable Python API is exported from:

```python
co_op_translator.api
```

The public API is organized into content translation helpers, path rewriting helpers, project orchestration, and review:

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

When adding new public APIs, update:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

క్రొత్త పబ్లిక్ APIలు జోడిస్తున్నప్పుడు, దిగువదాన్ని అప్డేట్ చేయండి. తక్కువ-స్థాయి `core` మాడ్యూల్స్‌ను స్థిరమైన APIగా డాక్యుమెంట్ చేయకుండా ఉండండి, వారు ప్రాజెక్ట్ ద్వారా నేరుగా మద్దతు ఇవ్వాలని ఉద్దేశించకపోతే.

## CLI ఎంట్రీ పాయింట్లు

The package defines these Poetry scripts:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` స్క్రిప్ట్ పేరు ఆధారంగా డిస్పాచ్ చేస్తుంది:

- `translate` పిలుస్తుంది `co_op_translator.cli.translate.translate_command`
- `evaluate` పిలుస్తుంది `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` పిలుస్తుంది `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` పిలుస్తుంది `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` `__main__.py` ను దాటి నేరుగా `co_op_translator.mcp.server:main` ను పిలుస్తుంది.

CLI ఆప్షన్లను జోడించినప్పుడు లేదా మార్చినప్పుడు, అప్డేట్ చేయండి:

- సంబంధిత `src/co_op_translator/cli/*.py` కమాండ్
- `docs/cli.md`
- CLI-సంబంధిత టెస్టులు, ప్రవర్తన మారితే

## MCP సర్వర్

The MCP server is implemented in:

```python
co_op_translator.mcp.server
```

సర్వర్ ఉద్దేశపూర్వకంగా పబ్లిక్ Python APIని ర్యాప్ చేస్తుంది, తక్కువ-స్థాయి `core` మాడ్యూల్స్‌ను నేరుగా పిలవడం కాకుండా. ఈ సరిహద్దును intact గా ఉంచండి ताकि MCP క్లయింట్లు, Python కాల్‌ర్స్, మరియు CLI అందరు ఒకే ప్రవర్తనను పంచుకోవచ్చు.

MCP టూల్స్‌ను జోడించినప్పుడు లేదా మార్చినప్పుడు, అప్డేట్ చేయండి:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- పబ్లిక్ API ఉపరితలంలో మార్పు ఉంటే `docs/api.md`

రికపాజిటరీ అనువాద టూల్స్ MCP ద్వారా మోడల్-కాలబుల్‌గా ఉంటాయి మరియు అనేక ఫైళ్లను రాయగలవు. డిఫాల్ట్‌గా `dry_run=True` ఉంచండి మరియు నాన్-డ్రై-రన్ ప్రాజెక్ట్ అనువాదానికి ముందు `confirm_write=True` అవసరం చేయండి.

## అనువాద ప్రవాహం

The high-level project translation flow is:

1. CLI ఆర్గుమెంట్లు లేదా API పరామితులను పార్స్ చేయండి.
2. `LLMConfig` తో LLM కాన్ఫిగరేషన్‌ను ధృవీకరించండి.
3. చిత్రం అనువాదం ఎంపిక చేయబడినప్పుడు Azure AI Vision ను ధృవీకరించండి.
4. భాషా కోడ్లను సాధారణీకరించండి.
5. పాత భాషా ఫోల్డర్ అలియాస్‌లను గుర్తించండి.
6. అనువాద పరిమాణాన్ని అంచనా వేయండి.
7. అనువర్తింపుల సందర్భాల్లో README భాష/కోర్సు విభాగాలను నవీకరించండి.
8. ప్రాజెక్ట్ అనువాదాన్ని `ProjectTranslator` కు అప్పగించండి.
9. `ProjectTranslator` ఫైల్ ప్రాసెసింగ్‌ను `TranslationManager` కి అప్పగిస్తుంది.

`TranslationManager` ప్రత్యేక ఫైల్-రకం మిక్సిన్ల నుండి రూపొందించబడుతుంది:

- `ProjectMarkdownTranslationMixin` Markdown ఫైళ్లను చదవడం, కంటెంట్ అనువాదం, పాథ్‌లను తిరిగి రాయడం, మెటాడేటా, నిరాకరణలు మరియు రాయడాన్ని నిర్వహిస్తుంది.
- `ProjectNotebookTranslationMixin` నోట్‌బుక్ ఫైళ్లను చదవడం, Markdown-సెల్ అనువాదం, పాథ్‌లను తిరిగి రాయడం, మెటాడేటా, నిరాకరణలు మరియు రాయడాన్ని నిర్వహిస్తుంది.
- `ProjectImageTranslationMixin` చిత్రాల కనుగొనడం, టెక్స్ట్ ఉపసంహరణ/అనువాదం, రెండరింగ్ చేసిన చిత్రం రాయడం, మరియు మెటాడేటాను నిర్వహిస్తుంది.

తక్కువ-స్థాయి కంటెంట్ APIలు ప్రాజెక్ట్ వర్క్‌ఫ్లోని స్కిప్ చేస్తాయి:

1. `translate_markdown_content` మరియు `translate_notebook_content` కేవలం ఇన్-మెమరీ కంటెంట్‌ను మాత్రమే అనువదిస్తాయి.
2. `translate_image_content` ఒకే చిత్రంలోని టెక్స్ట్‌ను అనువదించి ఒక రెండరింగ్ చేసిన చిత్రం ఆబ్జెక్ట్‌ను తిరిగి ఇస్తుంది.
3. `rewrite_markdown_paths` మరియు `rewrite_notebook_paths` స్పష్టమైన పోస్ట్-ప్రాసెసింగ్ సహాయకులు. ఇవి అనువాదం చేయవు మరియు ప్రాజెక్ట్ రాయడాలు చేయవు.

## సమీక్ష ప్రవాహం

The deterministic review flow is:

1. CLI ఆర్గుమెంట్లు లేదా API పరామితుల్ని పార్స్ చేయండి.
2. అభ్యర్థించిన భాషా కోడ్లను సాధారణీకరించండి.
3. `root_dir`, `root_dirs`, లేదా `groups` నుండి ఒకటి లేదా ఎక్కువ సమీక్ష లక్ష్యాలను తయారుచేయండి.
4. ఐచ్ఛికంగా `--changed-from` తో సోర్స్ ఫైళ్లను పరిమితం చేయండి.
5. సంరచన, అనువాద తాజాదనం, Markdown సమగ్రత, మరియు లోకల్ లింక్/ఇమేజ్ మార్గాల కోసం నిర్ధారిత తనిఖీ పరిగణనలు నడపండి.
6. లేదా పాఠ్య అవుట్‌పుట్ లేదా GitHub-ఫ్లేవర్డ్ Markdown ముద్రించండి.
7. సమీక్ష లోపాలు కనబడితే వైఫల్యంగా నిష్క్రమించండి.

సమీక్ష ప్రవాహం API కీస్ అవసరం లేకుండా ఉంటుంది మరియు పుల్ రిక్వెస్ట్ CIకు సరిపడేది గా ఉండాలి. పుల్ రిక్వెస్ట్ వర్క్‌ఫ్లో ప్రతి నడుస్తున్న సారి ఒక చెక్ సమ్మరీను రాస్తుంది మరియు `co-op-review` అప్రమత్తమైతే మాత్రమే PR కామెంట్‌ను పోస్ట్ చేస్తుంది.

## డాక్యుమెంటేషన్ సైట్

The docs site is configured by:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` డైరెక్టరీ అధికారం కలిగిన డాక్యుమెంటేషన్ మూలం. ప్రాజెక్ట్ ఉద్దేశపూర్వకంగా మరో ప్రచురించబడిన డాక్యుమెంటేషన్ ఉపరితలాన్ని పరిచయం చేయకపోతే, ఈ డైరెక్టరీకి బయట కొత్త end-user గైడ్‌లను చేర్చవద్దు.

Build locally:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview locally:

```bash
python -m mkdocs serve
```

జనరేట్ చేసిన సైట్ `site/`లో రాయబడుతుంది, ఇది git ద్వారా నిర్లక్ష్యం చేయబడింది.

## GitHub Pages వర్క్‌ఫ్లో

.github/workflows/docs.yml పుల్ రిక్వెస్ట్‌లపై సైట్‌ను బిల్డ్ చేస్తుంది మరియు `main` కి పుష్ చేయబడినప్పుడు డిప్లాయ్ చేస్తుంది.

The workflow installs:

```bash
pip install -r requirements-docs.txt
```

డాక్స్ వర్క్‌ఫ్లో కేవలం డాక్యుమెంటేషన్ టూల్‌చెయిన్‌ను మాత్రమే ఇన్స్టాల్ చేస్తుంది. `mkdocs.yml` `mkdocstrings` ను `src/` వైపు సూచిస్తుంది అందునా పబ్లిక్ API పేజీలను పూర్తి రన్‌టైమ్ డిపెండెన్సీలు ఇన్స్టాల్ చేయకుండా సోర్స్ ట్రీ నుండి రేండర్ చేయచ్చు. భవిష్యత్తులో API డాక్స్ బిల్డ్ సమయంలో ఐచ్చిక రన్‌టైమ్ ప్రొవైడర్లు దిగుమతి కావాలనుకుంటే, `.github/workflows/docs.yml` మరియు ఈ గైడ్ రెండింటినీ అప్డేట్ చేయండి.

## డాక్స్ నాణ్యత ప్రమాణం

Before merging documentation changes, run:

```bash
python -m mkdocs build --strict
git diff --check
```

బలమైన బిల్డులను ఉపయోగించండి zodat (Note: keep original language?) కాబట్టినా...