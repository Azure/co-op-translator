# నిర్వహణ గైడ్

ఈ పేజీ API, CLI, మరియు డాక్యుమెన్టేషన్ సైట్ ఒకదానికొకటి ఎలా అనుసంధానించబడ్డాయో సారాంశం ఇస్తుంది.

## పబ్లిక్ API సరిహద్దు

స్థిరమైన Python API ఈ స్థలాల నుంచి ఎగుమతి చేయబడింది:

```python
co_op_translator.api
```

పబ్లిక్ API కంటెంట్ అనువాద సహాయకారులు, పాత్ పునఃరాయిటింగ్ సహాయకారులు, ప్రాజెక్ట్ నిర్వహణ, మరియు సమీక్షలుగా ఏర్పాటు చేయబడింది:

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

`TranslationStateProvider` హోస్టెడ్ ఇంటిగ్రేషన్ల కోసం పర్సిస్టెన్స్ సరిహద్దు.
ఇది ఉత్పత్తి చేయబడిన అభ్యర్థులను ఆమోదించిన బేస్‌లైన్ల నుండి వేరుగా ఉంచాలి కాబట్టి ఒక
అన్‌మార్జ్డ్ అనువాదం నిజమైన సత్య మూలం అవ్వకుండా ఉండాలి.

కొత్త పబ్లిక్ API లను జోడించినప్పుడు ఈ ఫైళ్లను నవీకరించండి:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- సంబంధిత API టెస్టులు `tests/co_op_translator/` కింద, ఉదాహరణకు `test_api.py` లేదా `test_review_api.py`

ప్రాజెక్ట్ నేరుగా వాటిని మద్దతు ఇవ్వాలని ఉద్దేశించకపోతే దిగువ స్థాయి `core` మాడ్యూల్‌లను స్థిర API గా డాక్యుమెంట్ చేయకండి.

## CLI ప్రవేశ బిందువులు

ప్యాకేజ్ ఈ Poetry స్క్రిప్ట్‌లను నిర్వచిస్తుంది:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` స్క్రిప్ట్ పేరుతో డిస్పాచ్ చేస్తుంది:

- `translate` `co_op_translator.cli.translate.translate_command` ను పిలుస్తుంది
- `evaluate` `co_op_translator.cli.evaluate.evaluate_command` ను పిలుస్తుంది
- `migrate-links` `co_op_translator.cli.migrate_links.migrate_links_command` ను పిలుస్తుంది
- `co-op-review` `co_op_translator.cli.review.review_command` ను పిలుస్తుంది

`co-op-translator-mcp` `__main__.py` ను బైపాస్ చేస్తుంది మరియు నేరుగా `co_op_translator.mcp.server:main` ను పిలుస్తుంది.

CLI ఎంపికలు జోడించినప్పుడు లేదా మార్చినప్పుడు, నవీకరించండి:

- సంబంధిత `src/co_op_translator/cli/*.py` కమాండ్
- `docs/cli.md`
- ప్రవర్తన మారితే CLI సంబంధిత పరీక్షలు

## MCP server

MCP సర్వర్ ఈ ఫైల్లో అమలు చేయబడింది:

```python
co_op_translator.mcp.server
```

సర్వర్ ను ఉద్దేశపూర్వకವಾಗಿ పబ్లిక్ Python API ను ర్యాప్ చేస్తుంది, దిగువస్థాయి `core` మాడ్యూల్‌లను నేరుగా పిలవకుండా. ఈ సరిహద్దును అలాగే ఉంచండి, తద్వారా MCP క్లయింట్లు, Python కాలర్లు మరియు CLI ఒకే ప్రవర్తనను పంచుకుంటాయి.

MCP టూల్‌లను జోడించినప్పుడు లేదా మార్చినప్పుడు, నవీకరించండి:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` పబ్లిక్ API ఉపరితలం మారితే

రిపోజిటరీ అనువాద టూల్‌లు MCP ద్వారా మోడల్-కాల్ చేయదగినవి మరియు బహు ఫైళ్లను రాయగలవు. `dry_run=True` ని డిఫాల్ట్‌గా ఉంచండి మరియు non-dry-run ప్రాజెక్ట్ అనువాదానికి ముందు `confirm_write=True` అవసరం చేయండి.

## అనువాద ప్రవాహం

హై-లెవల్ ప్రాజెక్ట్ అనువాద ప్రవాహం ఇలా ఉంటుంది:

1. CLI ఆర్గ్యుమెంట్లు లేదా API పరామితులను పార్స్ చేయండి.
2. `LLMConfig` తో LLM కాన్ఫిగరేషన్ ని సరిచూడండి.
3. ఇమేజ్ అనువాదం ఎంపిక చేయబడినప్పుడు Azure AI Vision ని ధృవీకరించండి.
4. భాష కోడ్లను సాధారణీకరించండి.
5. పూర్వపు భాష ఫోల్డర్ అలియాసులను కనుగొనండి.
6. అనువాద పరిమాణాన్ని అంచనా వేయండి.
7. అవసరమైతే README భాష/కోర్సు విభాగాలను నవీకరించండి.
8. ప్రాజెక్ట్ అనువాదాన్ని `ProjectTranslator` కు అప్పగించండి.
9. `ProjectTranslator` ఫైల్ ప్రాసెసింగ్‌ను `TranslationManager` కి అప్పగిస్తుంది.

`TranslationManager` ప్రత్యేక ఫైల్-రకం మిక్సిన్లతో రూపొందించబడింది:

- `ProjectMarkdownTranslationMixin` మార్క్డౌన్ ఫైల్ చదివే పనులు, కంటెంట్ అనువాదం, పాత్ పునఃరాయిటింగ్, మెటాడేటా, డిస్క్లెయిమర్లు, మరియు రాయడం నిర్వహిస్తుంది.
- `ProjectNotebookTranslationMixin` నోటుబుక్ ఫైల్ చదివే పనులు, Markdown-సెల్ అనువాదం, పాత్ పునఃరాయిటింగ్, మెటాడేటా, డిస్క్లెయిమర్లు మరియు రాయడం నిర్వహిస్తుంది.
- `ProjectImageTranslationMixin` చిత్రం కనుగొనటం, టెక్స్ట్ ఎక్స్‌ట్రాక్షన్/అనువాదం, రెండర్డ్ చిత్రం రాయడం మరియు మెటాడేటాను నిర్వహిస్తుంది.

తక్కువ స్థాయి కంటెంట్ APIలు ప్రాజెక్ట్ వర్క్‍ఫ్లోను స్కిప్ చేస్తాయి:

1. `translate_markdown_content` మరియు `translate_notebook_content` కేవలం మెమోరీలో ఉన్న కంటెంట్ ను అనువదిస్తాయి.
2. `translate_image_content` ఒకే చిత్రంలోని టెక్స్ట్ ను అనువదించి రెండర్డ్ ఇమేజ్ ఆబ్జెక్టును 반환 చేస్తుంది.
3. `rewrite_markdown_paths` మరియు `rewrite_notebook_paths` స్పష్టమైన పోస్ట్-ప్రాసెసింగ్ సహాయకులు. అవి ఎటువంటి అనువాదం చేయవు మరియు ప్రాజెక్ట్ రాయింపులు చేయవు.

## సమీక్ష ప్రవాహం

నిర్దిష్ట సమీక్ష ప్రవాహం:

1. CLI ఆర్గ్యుమెంట్లు లేదా API పరామితులను పార్స్ చేయండి.
2. అభ్యర్థించబడిన భాష కోడ్లను సాధారణీకరించండి.
3. `root_dir`, `root_dirs`, లేదా `groups` నుంచి ఒకటి లేదా ఎక్కువ సమీక్ష టార్గెట్లను నిర్మించండి.
4. ఐచ్ఛికంగా మూల ఫైల్స్‌ను `--changed-from` తో పరిమితం చేయండి.
5. నిర్మాణం, అనువాద తాజాదనం, Markdown సమగ్రత, మరియు స్థానిక లింక్/చిత్ర మార్గాల కోసం డిటర్మినిస్టిక్ చెక్‌లను అమలు చేయండి.
6. టెక్స్ట్ అవుట్పుట్ లేదా GitHub-ఫ్లేవర్డ్ Markdown ను ప్రింట్ చేయండి.
7. సమీక్ష లోపాలు కనుగొనబడితే ఫెయిల్యూర్ తో ఎగ్జిట్ అవండి.

సమీక్ష ప్రవాహానికి API కీలు అవసరం ఉండవు మరియు ఇది స్థానిక చెక్స్ లేదా ఆప్ట్-ఇన్ వినియోగదారుని CI కోసం అందుబాటులో ఉంటుంది. ఈ రిపోజిటరీ ప్రతి pull request పై ఆటోమేటిక్గా `co-op-review` ను 실행ే చేయదు.

## డాక్యుమెంటేషన్ సైట్

డాక్స్ సైట్ ఈ ప్రకారంగా కాన్ఫిగర్ చేయబడింది:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` డైరెక్టరీ అనేది ప్రధాన డాక్యుమెంటేషన్ మూలం. ప్రాజెక్ట్ ఉద్దేశపూర్వకంగా మరో ప్రచురిత డాక్యుమెంటేషన్ ఉపరితలాన్ని పరిచయం చేసే సందర్భం కాకుండా ఈ డైరెక్టరీ బయట కొత్త end-user గైడ్‌లను జోడించకండి.

Build locally:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview locally:

```bash
python -m mkdocs serve
```

సృష్టించబడిన సైట్ `site/` ఫోల్డర్‌కి రాయబడుతుంది, అది git ద్వారా ignore చేయబడింది.

## GitHub Pages పని ప్రవాహం

`.github/workflows/docs.yml` పుల్ రిక్వెస్టులపై సైట్‌ను బిల్డ్ చేస్తుంది మరియు `main` కు పుష్ చేసినప్పుడు డిప్లాయ్ చేస్తుంది.

వర్క్‌ఫ్లో క్రింది ప్యాకేజీలను ఇన్‌స్టాల్ చేస్తుంది:

```bash
pip install -r requirements-docs.txt
```

డాక్స్ వర్క్‌ఫ్లో కేవలం డాక్యుమెంటేషన్ టూల్‌చెయిన్‌ను మాత్రమే ఇన్‌స్టాల్ చేస్తుంది. `mkdocs.yml` లో `mkdocstrings` ను `src/` వైపు సూచిస్తారు కాబట్టి పబ్లిక్ API పేజీలు పూర్తి రన్‌టైమ్ డిపెండెన్సీ సెట్ను ఇన్‌స్టాల్ చేయకుండానే సోర్స్ ట్రీ నుండి రెండర్ చేయబడవచ్చు. భవిష్యత్తులో API డాక్స్ బిల్డ్ సమయంలో ఐచ్ఛిక రన్‌టైమ్ ప్రొవైడర్స్ ను ఇంపోర్ట్ చేయాల్సిన అవసరం వస్తే, `.github/workflows/docs.yml` మరియు ఈ గైడ్‌ను రెండింటినీ నవీకరించండి.

## డాక్యుమెంటేషన్ నాణ్యత ప్రమాణం

డాక్యుమెంటేషన్ మార్పులను మర్జ్ చేయకముందు, రన్ చేయండి:

```bash
python -m mkdocs build --strict
git diff --check
```

కఠిన బిల్డులను ఉపయోగించండి, తద్వారా బ్రోకెన్ లింకులు, చెల్లని నావిగేషన్ ఎంట్రీలు మరియు API రెండరింగ్ సమస్యలు తొందరగా ఫెయిల్ అవుతాయి.