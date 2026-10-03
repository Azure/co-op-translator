# ជ្រើសរើសលំហូរការងាររបស់អ្នក

Co-op Translator អាចប្រើបានតាមរយៈវិធីបីប្រភេទ៖ CLI, Python API និង MCP server។ ពួកវាមានសមត្ថភាពបកប្រែដូចគ្នា ប៉ុន្តែមួយៗសមរម្យនឹងលំហូរការងារផ្សេងគ្នា។

ប្រើទំព័រនេះពេលអ្នកកំពុងសម្រេចចិត្តថា តើត្រូវចាប់ផ្តើមពីណា។

**បើអ្នកកែសម្រួលការបកប្រែដោយដៃ:** workflow ដើមរបស់ CLI និង Actions នឹងបកប្រែឡើងវិញឯកសារដើមដែលផ្លាស់ប្ដូរទាំងមូល ដូច្នេះពាក្យដែលអ្នកបានកំណត់ក្នុងឯកសារទាំងនោះអាចត្រូវបានលើសសរសេរ។ សូមពិនិត្យ diff មុនពេលទទួលយកការអាប់ដេត។ សម្រាប់ការការពារ​កម្រិតប្លុក Markdown នៃកែប្រែដែលទទួលយក សូមប្រើជម្រើស [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider)។

## ការសម្រេចចិត្តរហ័ស

| ប្រសិនបើអ្នកចង់... | ប្រើ | ចាប់ផ្តើមនៅទីនេះ |
| --- | --- | --- |
| បកប្រែ ឬ ពិនិត្យមើល repository ពី terminal | CLI | [ឯកសារយោង CLI](cli.md) |
| បន្ថែមការបកប្រែទៅក្នុងស្គ្រីប Python, សេវា, notebook, ឬ កិច្ចការ CI | Python API | [Python API](api.md) |
| អនុញ្ញាតឲ្យ agent, editor, ឬ MCP-compatible client បកប្រែមាតិកាសម្រាប់អ្នក | MCP Server | [MCP Server](mcp.md) |
| បកប្រែឯកសារ Markdown មួយ, notebook, ឬ រូបភាព ដែលកម្មវិធីរបស់អ្នកបានបើករួច | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| បកប្រែ repository ទាំងមូល ជាមួយថតលទ្ធផលស្តង់ដារ និង metadata | CLI or `run_translation` | [ឯកសារយោង CLI](cli.md) or [Python API](api.md) |

## ប្រើ CLI នៅពេល

ជ្រើស CLI នៅពេលមនុស្ស ឬ កិច្ចការ CI កំពុងបញ្ជាដំណើរការការបកប្រែ repository ពី shell។

CLI គឺជាវិធីត្រង់បំផុតពេលអ្នកចង់ឲ្យ Co-op Translator ស្វែងរកឯកសារគម្រោង, បង្កើតលទ្ធផលដែលបានបកប្រែ, រក្សាទុកលំនាំរចនាសម្ព័ន្ធគម្រោង, ធ្វើបច្ចុប្បន្នភាព metadata, និងរត់ពាក្យបញ្ជាផ្ទៀងផ្ទាត់។

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

ឧទាហរណ៍នេះបកប្រែ Markdown និង notebooks. បន្ថែម `-img` តែបន្ទាប់ពីបានកំណត់រចនាសម្ព័ន្ធ [Azure AI Vision](configuration.md#azure-ai-vision). សម្រាប់ការរត់ដំបូងដែលមានតែ Markdown, អនុវត្តតាម [ការបកប្រែដំបូងរបស់អ្នក](first-translation.md).

សមរម្យសម្រាប់:

- អ្នកកំពុងបកប្រែ repository ពី terminal របស់អ្នក។
- អ្នកចង់បានពាក្យបញ្ជាដដែលសម្រាប់ workflow CI ឬ ការចេញផ្សាយ។
- អ្នកចង់បានការស្វែងរកឯកសារគម្រោង built-in, ផ្លូវលទ្ធផល, metadata, ការសម្អាត និងការពិនិត្យ។
- អ្នកចូលចិត្តចំណុចប្រទាក់តាមបញ្ជា ជាងការសរសេរកូដ Python។

## ប្រើ Python API នៅពេល

ជ្រើស Python API ពេលកូដរបស់អ្នកត្រូវគ្រប់គ្រងលំហូរការងារ។

API មានប្រយោជន៍សម្រាប់កម្មវិធី, ស្គ្រីបស្វ័យប្រវត្តិ, notebooks, សេវាកម្ម និងបណ្តាញផ្លូវប្ដូរផ្ទាល់ខ្លួន។ វាអនុញ្ញាតឲ្យអ្នកហៅ API បកប្រែមាតិកាថ្នាក់ទាបសម្រាប់ឯកសារតែមួយៗ ឬរត់ orchestration កម្រិត repository ដដែលដែល CLI ប្រើ។

បកប្រែឯកសារ Markdown មួយ ហើយសម្រេចចិត្តថានឹងរក្សាទុកវានៅណា៖

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

រត់ការបកប្រែ repository ពី Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

សមរម្យសម្រាប់:

- កម្មវិធីរបស់អ្នកបានអានឯកសារ, buffers, notebooks, ឬ bytes រូបភាពរួចហើយ។
- អ្នកត្រូវការការផ្ទៀងផ្ទាត់ផ្ទាល់ខ្លួន, ការផ្ទុក, ការចុះកំណត់ហេតុ (logging), ការសាកល្បងឡើងវិញ, ឬលំហូរសម្រាប់ការអនុម័ត។
- អ្នកចង់បកប្រែឯកសារតែមួយ, notebook, ឬ រូបភាព ដោយមិនដំណើរការទាំង repository ទាំងមូល។
- អ្នកចង់បានការបកប្រែ repository តែពីស្វ័យប្រវត្តិ Python មិនមែនពីពាក្យបញ្ជា shell។

## ប្រើ MCP Server នៅពេល

ជ្រើស MCP server ពេល agent, editor, ឬ client ដែលមានភាពឆបគ្នាជាមួយ MCP គួរតែហៅឧបករណ៍ Co-op Translator។

ក្នុងការកំណត់ក្នុងស្រុកធម្មតា អ្នកប្រើប្រាស់មិនត្រូវបើក server ដោយដៃទុកដំណើរការ។ MCP client ចាប់ផ្តើម `co-op-translator-mcp` លើ `stdio` ពេលវាចាំបាច់ប្រើឧបករណ៍។

ឧទាហរណ៍សំណើរបស់អ្នកប្រើដែល agent អាចដោះស្រាយបាន៖

- "បកប្រែឯកសារ Markdown នេះទៅជាភាសាកូរ៉េ ហើយរក្សាឲ្យតំណភ្ជាប់ត្រឹមត្រូវ។"
- "បកប្រែឯកសារ Markdown នេះទៅជាភាសាកូរ៉េ ជាមួយលំហូរ MCP ជួយដោយភ្នាក់ងារ ដោយប្រើម៉ូដែលរបស់អ្នកសម្រាប់ចំណែកដែលបានបកប្រែ។"
- "បកប្រែ notebook នេះទៅជាភាសាកូរ៉េ រក្សាឲ្យ code cells នៅដដែល ហើយប្រើ Co-op Translator MCP ដើម្បីស្ដារឡើងវិញ notebook។"
- "បកប្រែអត្ថបទក្នុងរូបភាពនេះទៅជាភាសាជប៉ុន ហើយរក្សាទុកលទ្ធផល។"
- "ធ្វើ dry-run ការបកប្រែ repository ទៅជាភាសាអេស្បាញ ហើយប្រាប់ខ្ញុំពីអ្វីដែលនឹងប្ដូរ។"
- "ពិនិត្យមើលថាតើលទ្ធផលបកប្រែភាសាកូរ៉េមានភាពទាន់សម័យឬទេ។"

សម្រាប់ Markdown និង notebooks, MCP អាចដំណើរការបានក្នុងពីររបៀប៖

| របៀប | ប្រើពេល | ឧបករណ៍សំខាន់ |
| --- | --- | --- |
| Agent-assisted | ភ្នាក់ងារ MCP លើម៉ាស៊ីនផ្ទះគួរបកប្រែចំណែកដោយប្រើម៉ូឌែលផ្ទាល់ខ្លួន ដោយគ្មានសញ្ញាប័ណ្ណអ្នកផ្តល់ LLM របស់ Co-op Translator។ | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator គួរហៅ Azure OpenAI, OpenAI, ឬ Anthropic ដោយផ្ទាល់។ | `translate_markdown_content`, `translate_notebook_content` |

ទ្រង់ទ្រាយនៃការហៅឧបករណ៍ Markdown ដែលគាំទ្រដោយអ្នកផ្គត់ផ្គង់ MCP:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

MCP image tool call shape:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

ការបកប្រែឃុំផ្ទុកត្រូវបានធ្វើជាការសាកល្បង (dry-run) ដោយលំនាំដើម តាមរយៈ MCP:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

សមរម្យសម្រាប់:

- អ្នកចង់បានលំហូរការបកប្រែជាភាសាធម្មជាតិ នៅក្នុង agent ឬ editor។
- អ្នកចង់បានការបកប្រែ Markdown ឬ notebook ដែលម៉ូឌែលភ្នាក់ងារ host បកប្រែចំណែកដែលបានរៀបចំ។
- អ្នកចង់ឲ្យភ្នាក់ងារ បកប្រែមាតិកាដែលបានជ្រើស ជំនួសការបកប្រែ repository ទាំងមូល។
- អ្នកចង់មានជំហានសម្រាប់អនុម័ត មុននឹងសរសេរទៅលើ repository ទាំងមូល។
- អ្នកចង់មានចំណុចប្រទាក់តែមួយដែលផ្ដល់ឧបករណ៍សម្រាប់ Markdown, notebook, រូបភាព, ការពិនិត្យ និងការកែសម្រួលផ្លូវ (path-rewriting)។

## តើពួកវាអៀងគ្នាទៅដូចម្តេច

CLI គឺជាជម្រើសលំនាំល្អបំផុតសម្រាប់មនុស្សដែលបកប្រែ repositories។ Python API ល្អបើកូដរបស់អ្នកជាម្ចាស់លំហូរការងារ។ MCP server ល្អបើ agent ឬ editor ជាម្ចាស់លំហូរការងារ។

ទាំងបីខ្សែនេះប្រើ Co-op Translator API សាធារណៈដូចគ្នា ដូច្នេះអ្នកអាចចាប់ផ្តើមជាមួយ CLI, ស្វ័យប្រវត្តិជាមួយ Python បន្ទាប់មក, ហើយបង្ហាញសមត្ថភាពដដែលទៅកាន់ MCP clients ពេលអ្នកត្រូវការលំហូរដឹកដោយ agent។