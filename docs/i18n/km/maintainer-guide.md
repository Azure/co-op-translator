# មគ្គុទេសក៍សម្រាប់អ្នកថែទាំ

ទំព័រនេះសង្ខេបពីរបៀបដែល API, CLI និងគេហទំព័រឯកសារត្រូវបានភ្ជាប់គ្នា។

## ព្រំដែន API សាធារណៈ

API Python ដែលមានស្ថេរភាព ត្រូវបាននាំចេញពី៖

```python
co_op_translator.api
```

API សាធារណៈ ត្រូវបានរៀបចំបែកជា ជំនួយកសាងបកប្រែមាតិកា ជំនួយកែផ្លូវ ការរៀបចំគម្រោង និងការពិនិត្យ៖

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

`TranslationStateProvider` គឺជាព្រំដែននៃការរក្សាទុកសម្រាប់ការរួមបញ្ចូលដែលបានផ្តល់សេវា។
វាត្រូវតែរក្សាបេក្ខភាពដែលបានបង្កើតឱ្យដាច់ពីមូលដ្ឋានដែលទទួលយក ដូច្នេះ
ការបកប្រែដែលមិនទាន់បញ្ចូលមិនអាចក្លាយជាប្រភពនៃការពិត។

ពេលបន្ថែម API សាធារណៈថ្មី, ធ្វើការអាប់ដេត៖

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

ចៀសវិញពីការឯកសារមុខងារ `core` កម្រិតទាបជាផ្នែក API ស្ថេរ លុះត្រាតែគម្រោងមានបំណងគាំទ្រពួកវាដោយផ្ទាល់។

## ចំណុចចូល CLI

កញ្ចប់កំណត់ស្គ្រីប Poetry ទាំងនេះ៖

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` បញ្ជូនតាមឈ្មោះស្គ្រីប៖

- `translate` ហៅ `co_op_translator.cli.translate.translate_command`
- `evaluate` ហៅ `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` ហៅ `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` ហៅ `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` រកជៀស `__main__.py` និងហៅ `co_op_translator.mcp.server:main` ដោយផ្ទាល់។

ពេលបន្ថែមឬប្ដូរជម្រើស CLI, អាប់ដេត៖

- the relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- ការធ្វើតេស្តដែលពាក់ព័ន្ធនឹង CLI ប្រសិនបើអាកប្បកិរិយាប្រែប្រួល

## ម៉ាស៊ីនមេ MCP

ម៉ាស៊ីនមេ MCP ត្រូវបានអនុវត្តនៅក្នុង៖

```python
co_op_translator.mcp.server
```

ម៉ាស៊ីនមេបានទិក្កាដឹកដៃដើម្បីបញ្ចូល API Python សាធារណៈ ជាងហៅម៉ូឌុល `core` កម្រិតទាប។ រក្សាព្រំដែននេះឲ្យអស់ ដូច្នេះ អតិថិជន MCP អ្នកហៅ Python និង CLI មានអាកប្បកិរិយាតែមួយ។

ពេលបន្ថែមឬប្ដូរឧបករណ៍ MCP, អាប់ដេត៖

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

ឧបករណ៍បកប្រែកម្មវិធីក្នុងរ៉ែបូស៊ីតរីអាចត្រូវហៅម៉ូដែលតាមរយៈ MCP និងអាចសរសេរឯកសារច្រើន។ រក្សា `dry_run=True` ជាលំនាំដើម ហើយទាមទារ `confirm_write=True` មុនពេលធ្វើការបកប្រែគម្រោងដែលមិនមែន dry-run។

## ដំណើរការបកប្រែ

ដំណើរការបកប្រែគម្រោងលំដាប់ខ្ពស់មាន៖

1. វិភាគអាគុយម៉ង់ CLI ឬប៉ារ៉ាម៉ែត្រ API។
2. ផ្ទៀងផ្ទាត់ ការកំណត់រចនាសម្ព័ន្ធ LLM ជាមួយ `LLMConfig`។
3. ផ្ទៀងផ្ទាត់ Azure AI Vision នៅពេលដែលបានជ្រើសបកប្រែរូបភាព។
4. ធ្វើឲ្យកូដភាសាមានទម្រង់គ្នា។
5. រកឃើញឈ្មោះជំនួសសម្រាប់ថតភាសាចាស់។
6. ប៉ាន់ស្មានបរិមាណការបកប្រែ។
7. អាប់ដេតផ្នែក README ស្តីពីភាសា/វគ្គ បើអាចអនុវត្ត។
8. ចែកភារកិច្ចការបកប្រែគម្រោងទៅកាន់ `ProjectTranslator`។
9. `ProjectTranslator` ចែកបន្ទុកដំណើរការឯកសារទៅ `TranslationManager`។

`TranslationManager` ត្រូវបានបង្កើតពី mixins ដែលផ្តោតលើប្រភេទឯកសារ៖

- `ProjectMarkdownTranslationMixin` គ្រប់គ្រងការទាញអានឯកសារ Markdown, ការបកប្រែមាតិកា, ការកែសម្រួលផ្លូវ, មេតាដាតា, ការបដិសេធ និងការសរសេរ។
- `ProjectNotebookTranslationMixin` គ្រប់គ្រងការទាញអានឯកសារ notebook, ការបកប្រែផ្នែក Markdown ក្នុងកោសិកា, ការកែផ្លូវ, មេតាដាតា, ការបដិសេធ និងការសរសេរ។
- `ProjectImageTranslationMixin` គ្រប់គ្រងការស្វែងរករូបភាព, ការដកអត្ថបទ/បកប្រែ, ការសរសេររូបភាពដែលបានបញ្ចាំង, និងមេតាដាតា។

API មាតិកាកម្រិតទាបជៀសវាងដំណើរការ​គម្រោង៖

1. `translate_markdown_content` និង `translate_notebook_content` បកប្រែមាតិកាផ្ទុកក្នុងចងចាំតែប៉ុណ្ណោះ។
2. `translate_image_content` បកប្រែអត្ថបទក្នុងរូបភាពមួយ ហើយត្រឡប់មកជាវត្ថុរូបភាពដែលបានបញ្ចាំង។
3. `rewrite_markdown_paths` និង `rewrite_notebook_paths` ជាជំនួយការដំណើរការក្រោយយ៉ាងច្បាស់។ ពួកវា​មិនអនុវត្តការបកប្រែ និងមិនសរសេរកិច្ចការគម្រោងឡើយ។

## ដំណើរការពិនិត្យ

ដំណើរការពិនិត្យដែលប្រាកដលទ្ធផលមាន៖

1. វិភាគអាគុយម៉ង់ CLI ឬប៉ារ៉ាម៉ែត្រ API។
2. ធ្វើឲ្យកូដភាសាដែលបានស្នើសុំមានទម្រង់គ្នា។
3. កសាងគោលដៅពិនិត្យមួយឬច្រើន ពី `root_dir`, `root_dirs`, ឬ `groups`។
4. ជាជម្រើស កំណត់ឯកសារប្រភពដោយប្រើ `--changed-from`។
5. ដំណើរការតេស្តប្រាកដសម្រាប់រចនា ភាពទាន់សម័យនៃការបកប្រែ សុពលភាព Markdown និងផ្លូវតំណ/រូបភាពក្នុងតំបន់។
6. បោះពុម្ពលទ្ធផលជា អត្ថបទ ឬ Markdown ដែលមានរចនាប័ទ្ម GitHub។
7. បញ្ចប់ដោយបរាជ័យនៅពេលរកឃើញកំហុសពិនិត្យ។

ដំណើរការពិនិត្យមិនទាមទារកូនសម្រាប់ API និងនៅតែអាចប្រើសម្រាប់តេស្តក្នុងតំបន់ ឬ CI ដែលអ្នកប្រើជ្រើសរើស។ ឃ្លាំងកូដនេះមិនរត់ `co-op-review` ដោយស្វ័យប្រវត្តិលើរបៀប pull request ទាំងអស់ទេ។

## គេហទំព័រឯកសារ

គេហទំព័រឯកសារត្រូវបានកំណត់រចនាតាម៖

```text
mkdocs.yml
requirements-docs.txt
docs/
```

ថត `docs/` គឺជាដើមប្រភពឯកសារដែលមានស្តង់ដារ។ កុំបន្ថែមមគ្គុទេសក៌អ្នកប្រើថ្មីៗខាងក្រៅថតនេះ លុះត្រាតែក្នុងករណីគម្រោងមានបំណងណែនាំផ្ទាំងឯកសារចេញផ្សាយផ្សេងទៀត។

សាងសង់ក្នុងតំបន់៖

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

មើលជាមុនក្នុងតំបន់៖

```bash
python -m mkdocs serve
```

គេហទំព័រដែលបានបង្កើតត្រូវបានសរសេរទៅ `site/` ដែល git មិនរាប់បញ្ចូល។

## ដំណើរការពិធីសាស្រ្ត GitHub Pages

`.github/workflows/docs.yml` សាងសង់គេហទំព័រនៅពេល pull requests ហើយប្រតិបត្តិការ deploy នៅពេល push ទៅ `main`។

ដំណើរការនេះតំឡើង៖

```bash
pip install -r requirements-docs.txt
```

ដំណើរការ docs តំឡើងតែឧបករណ៍សម្រាប់ឯកសារ តែប៉ុណ្ណោះ។ `mkdocs.yml` បង្ហាញ `mkdocstrings` ទៅកាន់ `src/` ដូច្នេះ ទំព័រ API សាធារណៈអាចត្រូវបានបង្ហាញពីដើមប្រភព (source tree) ដោយគ្មានការតំឡើងឧបករណ៍ runtime ទាំងមូល។ ប្រសិនបើឯកសារ API អនាគតត្រូវការនាំចូលផ្តល់ runtime ជាជម្រើសនៅពេលសាងសង់ សូមអាប់ដេតទាំង `.github/workflows/docs.yml` និងមគ្គុទេសក៍នេះរួមគ្នា។

## ស្តង់ដារគុណភាពឯកសារ

មុនបញ្ចូលការផ្លាស់ប្ដូរឯកសារ, រត់៖

```bash
python -m mkdocs build --strict
git diff --check
```

ប្រើការសាងសង់តឹងរ៉ឹង ដើម្បីឲ្យតំណខូច, បញ្ចូលរុករកមិនត្រឹមត្រូវ និងបញ្ហាការបង្ហាញ API បរាជ័យនៅដំណាក់កាលដំបូង។