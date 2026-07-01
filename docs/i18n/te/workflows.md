# మీ వర్క్‌ఫ్లోను ఎంచుకోండి

Co-op Translator ని మూడు మార్గాల్లో ఉపయోగించవచ్చు: CLI, Python API, మరియు MCP server. వీటి అన్నీ ఒకسانమైన అనువాద సామర్ధ్యాలను కలిగి ఉంటాయి, కానీ ప్రతి ఒక్కటి వేరు వేరు వర్క్‌ఫ్లోలకు సరిపోతుంది.

ఎక్కడ ప్రారంభించాలో నిర్ణయించుకొంటున్నప్పుడు ఈ పేజీని ఉపయోగించండి.

## త్వరిత నిర్ణయం

| మీరు చేయదలచుకున్నది... | వాడండి | ఇక్కడ ప్రారంభించండి |
| --- | --- | --- |
| టర్మినల్ నుండి ఒక రిపాజిటరీని అనువదించండి లేదా సమీక్షించండి | CLI | [CLI సూచిక](cli.md) |
| Python స్క్రిప్ట్, సర్వీస్, నోట్‌బుక్ లేదా CI జాబ్‌కు అనువాదాన్ని జోడించండి | Python API | [Python API](api.md) |
| ఏజెంట్, ఎడిటర్, లేదా MCP-అనుకూల క్లయింట్ మీ కోసం కంటెంట్‌ను అనువదించనివ్వండి | MCP Server | [MCP Server](mcp.md) |
| మీ యాప్ ఇప్పటికే లోడ్ చేసిన ఒక Markdown డాక్యుమెంట్, నోట్‌బుక్, లేదా చిత్రం ఒకదానిని అనువదించండి | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| సాధారణ output ఫోల్డర్లు మరియు మెటాడేటాతో మొత్తం రిపాజిటరీని అనువదించండి | CLI or `run_translation` | [CLI సూచిక](cli.md) or [Python API](api.md) |

## CLI ని ఉపయోగించవలసినపుడు

ఒక వ్యక్తి లేదా CI జాబ్ షెల్ నుండి రిపాజిటరీ అనువాదాన్ని నడిపిస్తున్నప్పుడు CLI ని ఎంచుకోండి.

Co-op Translator ప్రాజెక్ట్ ఫైళ్లను కనుగొనడం, అనువదించిన అవుట్‌పుట్‌లను సృష్టించడం, ప్రాజెక్ట్ లేఅవుట్‌ను పరిరక్షించడం, మెటాడేటాను నవీకరించడం మరియు సమీక్ష కమాండ్లను నడపడం వంటి పని కోసం CLI అనేది ప్రత్యక్ష మార్గం.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

సరైన సందర్భాలు:

- మీరు టర్మినల్ నుండి ఒక రిపాజిటరీని అనువదిస్తున్నారు.
- మీరు CI లేదా రీలీజ్ వర్క్‌ఫ్లోల కోసం పునరావృతంగా నడిచే కమాండ్ కావాలనుకుంటున్నారు.
- మీరు బిల్ట్-ఇన్ ప్రాజెక్ట్ కనుగొనడం, అవుట్‌పుట్ మార్గాలు, మెటాడేటా, క్లీనప్ మరియు సమీక్ష కోరుకుంటున్నారు.
- మీరు Python కోడ్ వ్రాయడం కన్నా కమాండ్ ఇంటర్ఫేస్‌ను ఇష్టపడతారు.

## Python API ని ఉపయోగించవలసినపుడు

మీ స్వంత కోడ్ వర్క్‌ఫ్లోను నియంత్రించాలనేటప్పుడు Python APIను ఎంచుకోండి.

API అనువర్తనాలు, ఆటోమేషన్ స్క్రిప్టులు, నోట్‌బుక్స్, సర్వీసులు మరియు కస్టమ్ పైప్లైన్లకు ఉపయోగకరంగా ఉంటుంది. ఇది వ్యక్తిగత ఫైళ్ల కోసం లో-లెవల్ కంటెంట్ అనువాద APIలను పిలవడానికి లేదా CLI ఉపయోగించే అదే రిపాజిటరీ-స్థాయి ఆర్చెస్ట్రేషన్ నడపడానికి అనుమతిస్తుంది.

ఒక Markdown డాక్యుమెంట్‌ను అనువదించి దాన్ని ఎక్కడ సేవ్ చేయాలో నిర్ణయించండి:

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

Python నుండి రిపాజిటరీ అనువాదాన్ని నడపండి:

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

సరైన సందర్భాలు:

- మీ అనువర్తనం ఇప్పటికే ఫైళ్లు, బఫర్లు, నోట్‌బుక్స్ లేదా చిత్రం బైట్లను చదువుతోంది.
- మీరు కస్టమ్ వెరిఫికేషన్, స్టోరೇಜ్, లాగింగ్, రీట్రైలు లేదా ఆమోద ప్రవాహాలు అవసరమవుతాయి.
- మీరు మొత్తం రిపాజిటరీని ప్రాసెస్ చేయకుండా ఒక డాక్యుమెంట్, నోట్‌బుక్ లేదా చిత్రాన్ని అనువదించాలని కోరుకుంటారు.
- మీరు రిపాజిటరీ అనువాదం కావాలనుకుంటున్నారు, కానీ షెల్ కమాండ్ కాకుండా Python ఆటోమేషన్ ద్వారా కావాలి.

## MCP Server ను ఉపయోగించవలసినపుడు

ఏజెంట్, ఎడిటర్, లేదా MCP-అనుకూల క్లయింట్ Co-op Translator టూల్స్‌ను పిలవాలనేటప్పుడు MCP serverని ఎంచుకోండి.

సాధారణ స్థానిక సెటప్‌లో, వినియోగదారుడు నిల్వగా సర్వర్ ను చేతితో నడుపరు. MCP క్లయింట్ అవసరం ఉన్నప్పుడు `co-op-translator-mcp` ని `stdio` ద్వారా స్టార్ట్ చేస్తుంది.

ఏజెంట్ అధ్వర్యంలో యూజర్ అభ్యర్థనలు ఉదాహరణలు:

- "ఈ Markdown ఫైల్‌ను కొరియన్‌కు అనువదించండి మరియు లింకులు సరిగ్గా ఉంచండి."
- "ఏజెంట్-సహాయ MCP వర్క్‌ఫ్లోతో ఈ Markdown ఫైల్‌ను కొరియన్‌కు అనువదించండి, అనువదించిన చంక్‌ల కోసం మీ స్వంత మోడల్‌ని ఉపయోగించి."
- "ఈ నోట్‌బుక్‌ని కొరియన్‌కు అనువదించి, కోడ్ సెల్‌లను పరిరక్షించి, నోట్‌బుక్‌ను పునఃనిర్మించడానికి Co-op Translator MCPని ఉపయోగించండి."
- "ఈ చిత్రంలోని టెక్స్ట్‌ను జపనీస్‌కు అనువదించి ఫలితాన్ని సేవ్ చేయండి."
- "రిపాజిటరీ అనువాదాన్ని స్పానిష్‌కు డ్రై-రన్ చేసి ఏమి మారుతుందో చెప్పండి."
- "కొరియన్ అనువాద అవుట్‌పుట్ నవీకరించబడిందో లేదో సమీక్షించండి."

Markdown మరియు నోట్‌బుక్స్ కోసం, MCP రెండు మోడ్‌లలో పని చేయగలదు:

| మోడ్ | ఎప్పుడు ఉపయోగించాలి | ప్రధాన టూల్స్ |
| --- | --- | --- |
| Agent-assisted | MCP హోస్ట్ ఏజెంట్ అతని సొంత మోడల్‌తో చంక్‌లను అనువదించాలి, Co-op Translator LLM ప్రొవైడర్ క్రెడెన్షియల్స్ లేకుండా. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator నేరుగా Azure OpenAI లేదా OpenAIను పిలవాలి. | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-backed Markdown టూల్ కాల్ ఆకారం:

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

MCP ఇమేజ్ టూల్ కాల్ ఆకారం:

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

MCP ద్వారా రిపాజిటరీ అనువాదం డిఫాల్ట్‌గా డ్రై-రన్‌గా ఉంటుంది:

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

సరైన సందర్భాలు:

- మీరు ఏజెంట్ లేదా ఎడిటర్ లో సహజ-భాష అనువాద వర్క్‌ఫ్లోలను కావాలనుకుంటున్నారు.
- హోస్ట్ ఏజెంట్ మోడల్ సిద్ధంగా ఉన్న చంక్‌లను అనువదించే Markdown లేదా నోట్‌బుక్ అనువాదం కావాలి.
- మొత్తం రిపాజిటరీ కాకుండా ఏజెంట్ ఎంపిక చేసిన కంటెంట్‌ని అనువదించాలని మీకు కావాలి.
- రిపాజిటరీ-ప్రమాణమైన రాయింపులకు ముందే ఒక ఆమోద దశ కావాలి.
- మీరు Markdown, నోట్‌బుక్, ఇమేజ్, రివ్యూ మరియు పాత్-రిరైట్ టూల్స్ అన్నింటినీ వెతికే ఒకే ఒక ఇంటర్ఫేస్ కావాలి.

## ఇవి ఒకరికొకరు ఎలా సరిపోతాయి

CLI అనేది రిపాజిటరీలు అనువదించు మనుషుల కోసం ఉత్తమ డిఫాల్ట్. Python API మీ కోడ్ వర్క్‌ఫ్లోని నియంత్రించినప్పుడు ఉత్తమం. MCP server ఏజెంట్ లేదా ఎడిటర్ వర్క్‌ఫ్లోని యజమాని అయినప్పుడు ఉత్తమం.

మూడు మార్గాలన్నీ ఒకటే పబ్లిక్ Co-op Translator APIను ఉపయోగిస్తాయి, కాబట్టి మీరు CLIతో మొదలుపెట్టి, తరువాత Pythonతో ఆటోమేట్ చేసి, అవసరమైతే ఏజెంట్-నడిపే వర్క్‌ఫ్లోల కోసం అదే సామర్థ్యాలను MCP క్లయింట్లకు అందించవచ్చు.