# មគ្គុទេសក៍អ្នកថែទាំ

ទំព័រនេះសង្ខេបពីរបៀបដែល API, CLI, និងតំបន់ឯកសារត្រូវបានភ្ជាប់គ្នា។

## ខ្សែស៊ីមាសាធារណៈ API

API Python ដែលមានស្ថេរភាពត្រូវបាននាំចេញពី:

```python
co_op_translator.api
```

API សាធារណៈត្រូវបានរៀបចំជា ជំនួយក្រមហត្ថបកប្រែមាតិកា, ជំនួយកែផ្លូវ, ការរៀបចំព្រឹត្តិការណ៍គម្រោង, និងការពិនិត្យ:

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

ពេលបន្ថែម API សាធារណៈថ្មី សូមធ្វើបច្ចុប្បន្នភាព:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- ករណីតេស្ត API សមរម្យនៅក្រោម `tests/co_op_translator/`, ដូចជា `test_api.py` ឬ `test_review_api.py`

ជៀសវាងការឲ្យឯកសារ module `core` កម្រិតទាបជាកម្មវិធី API ដែលមានស្ថេរភាព លុះត្រាតែគម្រោងមានគំនិតគាំទ្រពួកវាដោយផ្ទាល់។

## ច្រកចូល CLI

កញ្ចប់នេះកំណត់ script ទាំងនេះនៅក្នុង Poetry:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` ដាក់ចេញតាមឈ្មោះ script៖

- `translate` ហៅ `co_op_translator.cli.translate.translate_command`
- `evaluate` ហៅ `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` ហៅ `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` ហៅ `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` រំលង `__main__.py` និង ហៅ `co_op_translator.mcp.server:main` ដោយផ្ទាល់។

ពេលបន្ថែម ឬផ្លាស់ប្តូរជម្រើស CLI សូមធ្វើបច្ចុប្បន្នភាព:

- ការបញ្ជា `src/co_op_translator/cli/*.py` សមរម្យ
- `docs/cli.md`
- តេស្តដែលពាក់ព័ន្ធ CLI ប្រសិនបើអាកប្បកិរិយាបានផ្លាស់ប្តូរ

## ម៉ាស៊ីន MCP

ម៉ាស៊ីន MCP ត្រូវបានអនុវត្តនៅក្នុង:

```python
co_op_translator.mcp.server
```

ម៉ាស៊ីននេះបំណងចិត្ដដាក់សូម្បី API Python សាធារណៈជាស្រទាប់ក្រោមវិធីផ្ទាល់ជំនួសការហៅ module `core` កម្រិតទាប។ រក្សា​ព្រំដែននេះឲ្យមានសុពលភាព ដូច្នេះ client MCP, អ្នកហៅ Python, និង CLI នឹងមានអាកប្បកិរិយាដូចគ្នា។

ពេលបន្ថែម ឬផ្លាស់ប្តូរសូមធ្វើបច្ចុប្បន្នភាព:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` ប្រសិនបើផ្ទៃ API សាធារណៈមានការផ្លាស់ប្តូរ

ឧបករណ៍បកប្រែក្នុងរ៉េប៉ូស៊ីតរីអាចត្រូវបានហៅដោយម៉ូដែលតាមរយៈ MCP និងអាចសរសេរឯកសារជាច្រើន។ រក្សា `dry_run=True` ជាប្លែកលំនាំដើម ហើយទាមទារ `confirm_write=True` មុនការបកប្រែគម្រោងដែលមិនមែន dry-run ។

## ដំណើរការ​បកប្រែ

ដំណើរការបកប្រែគម្រោងជាកម្រិតខ្ពស់មានដូចជា៖

1. បំបែកអាគុយម៉ង់ CLI ឬប៉ារ៉ាម៉ែត្រ API។
2. ផ្ទៀងផ្ទាត់ការកំណត់ LLM ជាមួយ `LLMConfig`.
3. ផ្ទៀងផ្ទាត់ Azure AI Vision នៅពេលជ្រើសបកប្រែរូបភាព។
4. បញ្ចូលកូដភាសាឲ្យស្ដង់ដារ។
5. រកឃើញអាសយដ្ឋានថតភាសាបុរាណ។
6. គណនា​បរិមាណប៉ាន់ស្មាននៃការបកប្រែ។
7. បច្ចុប្បន្នភាពផ្នែក README ភាសា/វគ្គប្រសិនបើអាចប្រើបាន។
8. ផ្តល់ភារៈការបកប្រែគម្រោងទៅ `ProjectTranslator`.
9. `ProjectTranslator` ផ្តល់ភារៈសម្រាប់ដំណើរការឯកសារទៅ `TranslationManager`.

`TranslationManager` ត្រូវបានផ្សំឡើងពី mixin ប្រភេទឯកសារយោងផ្តោតចិត្ត៖

- `ProjectMarkdownTranslationMixin` ទទួលខុសត្រូវសម្រាប់ការអានឯកសារ Markdown, ការបកប្រែមាតិកា, ការកែផ្លូវ, មេតាឌាតា, សេចក្តីបដិសេធ, និងការសរសេរ។
- `ProjectNotebookTranslationMixin` ទទួលខុសត្រូវសម្រាប់ការអានឯកសារបញ្ចុះសុក្រឹត (notebook), ការបកប្រែខCells Markdown, ការកែផ្លូវ, មេតាឌាតា, សេចក្តីបដិសេធ, និងការសរសេរ۔
- `ProjectImageTranslationMixin` ទទួលខុសត្រូវសម្រាប់ការស្វែងរករូបភាព, យកអត្ថបទ/បកប្រែអត្ថបទ, ការសរសេររូបភាពដែលបានបង្ហាញឡើងវិញ, និងមេតាឌาตា។

API មាតិកាកម្រិតទាប ធ្វើការរំលង workflow គម្រោង៖

1. `translate_markdown_content` និង `translate_notebook_content` បកប្រែតែមាតិកានៅក្នុងម៉ោងចិត្តប៉ុណ្ណោះ។
2. `translate_image_content` បកប្រែអត្ថបទនៅក្នុងរូបភាពតែមួយ ហើយត្រឡប់ធាតុរូបភាពដែលបានបង្ហាញឡើងវិញ។
3. `rewrite_markdown_paths` និង `rewrite_notebook_paths` ជាជំនួយការក្រោយដាក់ដំណើរការ បញ្ជាក់ជាច្បាស់។ វា​មិនអនុវត្តការបកប្រែ និងមិនមានការសរសេរគម្រោងណាមួយទេ។

## ដំណើរការ​ពិនិត្យ

ដំណើរការ​ពិនិត្យដែលមានលទ្ធផលកំណត់មានដូចជា៖

1. បំបែកអាគុយម៉ង់ CLI ឬប៉ារ៉ាម៉ែត្រ API।
2. បញ្ចូលកូដភាសាដែលបានស្នើសុំឲ្យស្ដង់ដារ។
3. បង្កើតគោលដៅពិនិត្យមួយឬច្រើនពី `root_dir`, `root_dirs`, និង `groups`.
4. ជាជម្រើស សងកំណត់ឯកសារដើមដោយ `--changed-from`.
5. រត់តេស្តកំណត់សម្រាប់រចនាសម្ព័ន្ធ, ស្រស់ភាពបកប្រែ, សុពលភាព Markdown, និងផ្លូវតំណ/រូបភាពក្នុងស្រុក។
6. បោះពុម្ពចេញជាអក្សរ ឬ Markdown តាមរបៀប GitHub។
7. បញ្ចប់ជាមួយការបរាជ័យនៅពេលមានកំហុសពិនិត្យ។

ដំណើរការពិនិត្យមិនទាមទារកូនសោ API និងគួរជាប់សមស្របសម្រាប់ CI ក្នុង pull request។ វិធានការជាចលនាការងារ pull request សរសេរឮសេចក្តីសង្ខេបតេស្តនៅលើគ្រប់ការប្រត្តិបត្តិ ហើយតែបង្ហោះមតិ PR នៅពេល `co-op-review` បរាជ័យប៉ុណ្ណោះ។

## តំបន់ឯកសារ

តំបន់ឯកសារត្រូវបានកំណត់រចនាសម្ព័ន្ធដោយ:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

ថត `docs/` គឺជាធនធានឯកសារចម្បង។ សូមកុំបន្ថែមមគ្គុទេសក៍ចុងអ្នកប្រើក្រៅថតនេះ លុះត្រាតែ​គម្រោងមានបង្ហាញផ្ទៃឯកសារបោះពុម្ពផ្សាយផ្សេងទៀត។

សង់នៅក្នុងម៉ាស៊ីនមូលដ្ឋាន:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

មើល 미ុនក្នុងម៉ាស៊ីនមូលដ្ឋាន:

```bash
python -m mkdocs serve
```

តំបន់ដែលបានបង្កើតត្រូវបានសរសេរទៅ `site/`, ដែលត្រូវបានលែងពិនិត្យដោយ git។

## វិធីសាស្ត្រ GitHub Pages

`.github/workflows/docs.yml` សង់តំបន់នៅលើ pull requests និងដាក់ចេញនៅពេលមាន pushes ទៅ `main`។

វិធីសាស្ត្រនេះតម្លើង:

```bash
pip install -r requirements-docs.txt
```

Workflow ឯកសារតម្លើងតែឧបករណ៍ឯកសារប៉ុណ្ណោះ។ `mkdocs.yml` បញ្ជិសម្រាប់ `mkdocstrings` ទៅកាន់ `src/` ដូច្នេះទំព័រ API សាធារណៈអាចត្រូវបានបញ្ចាំងពីរពTree ឯកសារដើមដោយគ្មានការតំឡើង dependency កាលចRuntime ពេញលេញ។ ប្រសិនបើឯកសារ API នៅអនាគតត្រូវការនាំចូលអ្នកផ្គត់ផ្គង់ runtime ជាជម្រើស ក្នុងអំឡុងពេលសាងសង់ សូមធ្វើបច្ចុប្បន្នភាពទាំង `.github/workflows/docs.yml` និងមគ្គុទេសក៍នេះរួមគ្នា។

## កម្រិតគុណភាពឯកសារ

មុនពេលបញ្ចូលការផ្លាស់ប្តូរឯកសារ សូមរត់:

```bash
python -m mkdocs build --strict
git diff --check
```

ប្រើការសាងសង់ទទឹងដើម្បីឲ្យតំណខូច, វាតម្លើងការនាវីហ្គេសិន មិនត្រឹមត្រូវ, និងបញ្ហាការរៀបចំ API បរាជ័យជាមុន។