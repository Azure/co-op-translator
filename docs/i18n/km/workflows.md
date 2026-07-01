# ជ្រើសរបៀបធ្វើការ

Co-op Translator អាចប្រើបានជារបៀបបី៖ CLI, Python API, និង MCP server. ពួកវាមានសមត្ថភាពបកប្រែដូចគ្នា ប៉ុន្តែម្ដងៗនីមួយសមស្របសម្រាប់របៀបធ្វើការ ខុសៗគ្នា។

ប្រើទំព័រនេះនៅពេលអ្នកកំពុងសម្រេចចិត្តថាចង់ចាប់ផ្តើមពីណា។

## ការសម្រេចចិត្តរហ័ស

| បើអ្នកចង់... | ប្រើ | ចាប់ផ្ដើមពីទីនេះ |
| --- | --- | --- |
| បកប្រែ ឬ ពិនិត្យមើល ឃ្លាំងកូដ (repository) ពី terminal | CLI | [ឯកសារ CLI](cli.md) |
| បន្ថែមការបកប្រែទៅក្នុង script Python, service, notebook ឬ ការងារ CI | Python API | [Python API](api.md) |
| អនុញ្ញាតឱ្យភ្នាក់ងារ, កម្មវិធីកែសម្រួល ឬ client ដែលសមស្របជាមួយ MCP បកប្រែមាតិកាដល់អ្នក | MCP Server | [ម៉ាស៊ីនមេ MCP](mcp.md) |
| បកប្រែឯកសារ Markdown មួយ, notebook, ឬ រូបភាព ដែលកម្មវិធីរបស់អ្នកបានផ្ទុករួច | Python API ឬ MCP Server | [Python API](api.md) ឬ [ម៉ាស៊ីនមេ MCP](mcp.md) |
| បកប្រែឃ្លាំងកូដទាំងមូលជាមួយថតចេញ និងមេតាដាតា​ស្តង់ដារ | CLI ឬ `run_translation` | [ឯកសារ CLI](cli.md) ឬ [Python API](api.md) |

## ប្រើ CLI នៅពេល

ជ្រើស CLI នៅពេលមនុស្ស ឬ ការងារ CI កំពុងបញ្ជាដំណើរការបកប្រែឃ្លាំងកូដពី shell។

CLI គឺជាវិធីត្រង់បំផុត ពេលអ្នកចង់ឱ្យ Co-op Translator ស្វែងរកឯកសារគម្រោង, បង្កើតច្រកចេញដែលបានបកប្រែ, រក្សាទ្រង់ទ្រាយគម្រោង, កែប្រែមេតាដាតា, និងដំណើរការការត្រួតពិនិត្យ។

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

សមសម្រាប់:

- អ្នកកំពុងបកប្រែឃ្លាំងកូដពី terminal របស់អ្នក។
- អ្នកចង់មានពាក្យបញ្ជាដែលអាចប្រើឡើងវិញសម្រាប់ CI ឬ ដំណើរការចេញផ្សាយ។
- អ្នកចង់បានការស្វែងរកគម្រោង, ផ្លូវចេញ, មេតាដាតា, ការសម្អាត និងការត្រួតពិនិត្យដែលមានរួចក្នុងកម្មវិធី។
- អ្នកចូលចិត្តរបៀបបញ្ជារម៉ាស៊ីនជាងការសរសេរកូដ Python។

## ប្រើ Python API នៅពេល

ជ្រើស Python API នៅពេលកូដរបស់អ្នកគួរតែគ្រប់គ្រងដំណើរការ។

API មានប្រយោជន៍សម្រាប់កម្មវិធី, ស្គ្រីបស្វ័យប្រវត្តិការ, notebooks, សេវាកម្ម, និងបណ្តាញដំណើរការផ្សេងៗ។ វាអនុញ្ញាតឱ្យអ្នកហៅ API បកប្រែមាតិកាកម្រិតទាបសម្រាប់ឯកសារឯកតា, ឬដំណើរការអូកស្ដ្រាតជាថ្នាក់ repository ដូចដែល CLI ប្រើ។

បកប្រែឯកសារ Markdown មួយ ហើយសម្រេចចិត្តថาจะរក្សាទុកនៅណា:

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

ដំណើរការបកប្រែឃ្លាំងកូដពី Python:

```python
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

សមសម្រាប់:

- កម្មវិធីរបស់អ្នកបានអានឯកសារ, ប៊ុហ្វឺរ, notebook ឬ បៃទរូបភាពរួចហើយ។
- អ្នកត្រូវការការត្រួតពិនិត្យ, ស្តុក, ការចុះបញ្ជី, ការព្យាយាមឡើងវិញ, ឬ ដំណើរការអនុម័តដែលអាចប្ដូរបាន។
- អ្នកចង់បកប្រែឯកសារ, notebook ឬ រូបភាព មួយ ដោយមិនដំណើរការទាំងឃ្លាំងកូដទាំងមូល។
- អ្នកចង់បកប្រែឃ្លាំងកូដ ប៉ុន្តែពីស្វ័យប្រវត្តិ Python ជំនួសពាក្យបញ្ជា shell។

## ប្រើម៉ាស៊ីនមេ MCP នៅពេល

ជ្រើសម៉ាស៊ីនមេ MCP នៅពេលភ្នាក់ងារ, កម្មវិធីកែសម្រួល ឬ client ដែលសមស្របជាមួយ MCP គួរតែហៅឧបករណ៍ Co-op Translator។

នៅក្នុងការតំឡើងក្នុងតំបន់ធម្មតា អ្នកប្រើមិនត្រូវដាក់ម៉ាស៊ីនមេឲ្យដំណើរការដោយដៃទេ។ MCP client ចាប់ផ្តើម `co-op-translator-mcp` តាម `stdio` ពេលវាត្រូវការឧបករណ៍។

ឧទាហរណ៍សំណើរដែលអ្នកប្រើអាចស្នើឱ្យភ្នាក់ងារបំពេញ:

- "បកប្រែឯកសារ Markdown នេះទៅជាភាសាកូរ៉េ ហើយរក្សាតំណភ្ជាប់ឲ្យត្រឹមត្រូវ។"
- "បកប្រែឯកសារ Markdown នេះទៅភាសាកូរ៉េ ដោយប្រើដំណើរការ MCP ជួយដោយភ្នាក់ងារ ហើយប្រើម៉ូដែលរបស់អ្នកសម្រាប់ចំណុចដែលបានបកប្រែ។"
- "បកប្រែ notebook នេះទៅភាសាកូរ៉េ រក្សា code cells ហើយប្រើ Co-op Translator MCP ដើម្បីស្តារឡើងវិញ notebook។"
- "បកប្រែអត្ថបទក្នុងរូបភាពនេះទៅជាភាសាជប៉ុន ហើយរក្សាលទ្ធផល។"
- "ធ្វើ dry-run នៃការបកប្រែឃ្លាំងកូដទៅជាភាសាស្ប៉ាញ ហើយប្រាប់ខ្ញុំថាតើអ្វីៗនឹងផ្លាស់ប្តូរ។"
- "ពិនិត្យថាតើលទ្ធផលបកប្រែទៅភាសាកូរ៉េមានទាន់ពេលឬទេ។"

សម្រាប់ Markdown និង notebooks, MCP អាចដំណើរការបានក្នុងរបៀបពីរប្រភេទ៖

| ម៉ូដ | ប្រើនៅពេល | ឧបករណ៍សំខាន់ |
| --- | --- | --- |
| ជំនួយដោយភ្នាក់ងារ | ភ្នាក់ងារ MCP នៃម៉ាស៊ីនផ្ទុកគួរតែបកប្រែចំណុចដែលបានបែងចែកដោយប្រើម៉ូដែលរបស់ខ្លួន ដោយមិនចាំបាច់មានសិទ្ធិលើអ្នកផ្តល់ LLM របស់ Co-op Translator។ | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| គាំទ្រដោយអ្នកផ្គត់ផ្គង់ | Co-op Translator គួរតែហៅ Azure OpenAI ឬ OpenAI ដោយផ្ទាល់។ | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-backed Markdown tool call shape:

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

Repository translation is dry-run by default through MCP:

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

សមសម្រាប់:

- អ្នកចង់បានដំណើរការបកប្រែដោយភាសាធម្មជាតិ នៅក្នុងភ្នាក់ងារ ឬ កម្មវិធីកែសម្រួល។
- អ្នកចង់បកប្រែ Markdown ឬ notebook ដែលម៉ូដែលភ្នាក់ងារផ្លាស់បកប្រែចំណែកដែលបានរៀបចំ។
- អ្នកចង់ឲ្យភ្នាក់ងារបកប្រែមាតិកាដែលបានជ្រើស ជំនួសការបកប្រែឃ្លាំងកូដទាំងមូល។
- អ្នកចង់មានជំហានអនុម័តមួយ មុនពេលសរសេរទៅលើឃ្លាំងកូដទាំងមូល។
- អ្នកចង់បានចំណុចប្រទាក់មួយ ដែលផ្តល់ឱ្យនូវឧបករណ៍សម្រាប់ Markdown, notebook, រូបភាព, ការពិនិត្យ, និងឧបករណ៍សម្រាប់កែប្រែទីតាំងផ្លូវ។

## របៀបដែលពួកវាសម្របសម្រួលគ្នា

CLI គឺជាចំណុចលំនាំដើមល្អបំផុតសម្រាប់មនុស្សដែលកំពុងបកប្រែឃ្លាំងកូដ។ Python API ល្អបំផុតនៅពេលកូដរបស់អ្នកគ្រប់គ្រងដំណើរការ។ ម៉ាស៊ីនមេ MCP ល្អបំផុតនៅពេលភ្នាក់ងារ ឬ កម្មវិធីកែសម្រួលគ្រប់គ្រងដំណើរការ។

វិធីទាំងបីនេះប្រើ Co-op Translator API សាធារណៈដូចគ្នា ដូច្នេះអ្នកអាចចាប់ផ្តើមជាមួយ CLI, បន្ទាប់មកស្វ័យប្រវត្តិដោយ Python, ហើយបង្ហាញសមត្ថភាពដូចគ្នាទៅឱ្យអតិថិជន MCP នៅពេលអ្នកត្រូវការដំណើរការដឹកដោយភ្នាក់ងារ។