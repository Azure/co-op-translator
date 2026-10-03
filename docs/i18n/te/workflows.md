# మీ వర్క్‌ఫ్లోని ఎంచుకోండి

Co-op Translator ను మూడు విధాలుగా ఉపయోగించవచ్చు: CLI, Python API, మరియు MCP సర్వర్. అవి అదే అనువాద సామర్ధ్యాలను పంచుకుంటాయి, కానీ ప్రతి ఒక్కటి వేరే వర్క్‌ఫ్లోకి సరిపోతుంది.

ఎక్కడినుండి మొదలెట్టాలో నిర్ణయిస్తోన్నప్పుడు ఈ పేజీని ఉపయోగించండి.

**మీరు అనువాదాలను చేతితో సవరిస్తే:** డిఫాల్ట్ CLI మరియు Actions వర్క్‌ఫ్లోలు మారిన మూల్ ఫైళ్లను పూర్తిగా మళ్ళీ అనువదిస్తాయి, కాబట్టి ఆ ఫైళ్లలో మీ వాక్యం మార్చబడవచ్చు. అప్డేట్‌ను అంగీకరించేముందు diff ని సమీక్షించండి. ఒప్పుకోబడిన సవరింపుల Markdown బ్లాక్-స్థాయి పరిరక్షణ కోసం, ఐచ్ఛిక [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) ను ఉపయోగించండి.

## త్వరిత నిర్ణయం

| If you want to... | Use | Start here |
| --- | --- | --- |
| టెర్మినల్ నుండి ఒక రిపాజిటరీని అనువదించండి లేదా సమీక్షించండి | CLI | [CLI సూచిక](cli.md) |
| Python స్క్రిప్ట్, సర్వీస్, నోట్బుక్, లేదా CI జాబ్‌లో అనువాదం జోడించండి | Python API | [Python API](api.md) |
| ఏజెంట్, ఎడిటర్ లేదా MCP-సమర్ధ క్లయింట్ మీ కోసం కంటెంట్‌ను అనువదించనివ్వండి | MCP Server | [MCP సర్వర్](mcp.md) |
| మీ యాప్ ఇప్పటికే లోడ్ చేసిన ఒక Markdown డాక్యుమెంట్, నోట్బుక్, లేదా ఇమేజ్‌ను అనువదించండి | Python API or MCP Server | [Python API](api.md) or [MCP సర్వర్](mcp.md) |
| సాధారణ అవుట్పుట్ ఫోల్డర్స్ మరియు మెటాడేటాతో మొత్తం రిపాజిటరీని అనువదించండి | CLI or `run_translation` | [CLI సూచిక](cli.md) or [Python API](api.md) |

## CLI ని ఉపయోగించవలసినప్పుడు

వ్యక్తి లేదా CI పని షెల్ నుండి రిపాజిటరీ అనువాదాన్ని నడిపిస్తుంటే CLI ఎంచుకోండి.

Co-op Translator ప్రాజెక్ట్ ఫైళ్లను కనుగొనడం, అనువదించిన అవుట్పుట్‌లను సృష్టించడం, ప్రాజెక్ట్ లేఅవుట్‌ను పరిరక్షించడం, మెటాడేటాను నవీకరించడం మరియు సమీక్ష కమాండ్లను అమలు చేయడం వంటి వాటికి CLI నేరుగా సరిపడే మార్గం.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

ఈ ఉదాహరణ Markdown మరియు నోట్బుక్స్‌ని అనువదిస్తుంది. [Azure AI Vision](configuration.md#azure-ai-vision) ను కాన్ఫిగర్ చేసిన తర్వాతే `-img`ను జోడించండి. Markdown మాత్రమే మొదటి రన్ కోసం, [మీ మొదటి అనువాదం](first-translation.md) ను అనుసరించండి.

బాగా సరిపోతాయి:

- మీరు టెర్మినల్ నుండి ఒక రిపాజిటరీని అనువదిస్తున్నారు.
- CI లేదా విడుదల వర్క్‌ఫ్లోలకు పునరావృతంగా పని చేసే కమాండ్ కావాలి.
- బిల్ట్-ఇన్ ప్రాజెక్ట్ కనుగొనడం, అవుట్‌పుట్ పథాలు, మెటాడేటా, క్లీన్‌అప్, మరియు సమీక్ష కావాలి.
- Python కోడ్ రాయడంపై కాకుండా కమాండ్ ఇన్టర్ఫేస్‌ను ప్రాధాన్యం ఇస్తారు.

## Python API ని ఉపయోగించవలసినప్పుడు

మీ స్వంత కోడ్ వర్క్‌ఫ్లోని నియంత్రించాలి అనిపిస్తే Python API ఎంచుకోండి.

API అనువర్తనాలు, ఆటోమేషన్ స్క్రిప్టులు, నోట్బుక్స్, సర్వీసులు మరియు కస్టమ్ పైప్‌లైన్ల కోసం ఉపయోగకరం. ఇది వ్యక్తిగత ఫైళ్ల కోసం లో-లెవెల్ కంటెంట్ అనువాద APIలను కాల్ చేయడానికి లేదా CLI ఉపయోగించే అదే రిపాజిటరీ-స్థాయి ఆర్కెస్ట్రేషన్‌ను నడిపేందుకు అనుమతిస్తుంది.

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

Python నుండి ఒక రిపాజిటరీ అనువాదాన్ని నడపండి:

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

బాగా సరిపోతాయి:

- మీ అప్లికేషన్ ఇప్పటికే ఫైళ్లు, బఫర్స్, నోట్బుక్స్ లేదా ఇమేజ్ బైట్స్ చదివే ఉంటే.
- మీరు కస్టమ్ వాలిడేషన్, స్టోరేజ్, లాగింగ్, రీట్రైలు లేదా ఆమోద ప్రవాహాలు అవసరమైతే.
- మొత్తం రిపాజిటరీని ప్రాసెస్ చేయకుండా ఒక డాక్యుమెంట్, నోట్బుక్ లేదా ఇమేజ్‌ను అనువదించాలనుకుంటే.
- రిపాజిటరీ అనువాదం కావాలి, కానీ షెల్ కమాండ్ కాకుండా Python ఆటోమేషన్ ద్వారా.

## MCP సర్వర్‌ను ఉపయోగించవలసినప్పుడు

ఏజెంట్, ఎడిటర్ లేదా MCP-అనుకూల క్లయింట్ Co-op Translator టూల్స్‌ను కాల్ చేయాల్సిన పరిస్థితుల్లో MCP సర్వర్ ఎంచుకోండి.

సాధారణ లోకల్ సెటప్‌లో, వినియోగదారు స్వయంగా సర్వర్‌ను నడిపించరాదు. టూల్స్ అవసరమైనప్పుడు MCP క్లయింట్ `stdio` మీద `co-op-translator-mcp` ను ప్రారంభిస్తుంది.

ఏజెంట్ నిర్వహించగల ఉదాహరణ యూజర్ అభ్యర్థనలు:

- "ఈ Markdown ఫైల్‌ను కొరియన్‌కు అనువదించి లింకులు సరకుగా ఉంచండి."
- "ఏజెంట్-సహాయ MCP వర్క్‌ఫ్లోతో ఈ Markdown ఫైల్‌ను కొరియన్‌కు అనువదించి, అనువదించబడిన చంక్‌ల కోసం మీ స్వంత మోడల్ ఉపయోగించండి."
- "ఈ నోట్బుక్‌ను కొరియన్‌కు అనువదించండి, కోడ్ క셀్స్‌ను పరిరక్షించండి, మరియు నోట్బుక్‌ను తిరిగి కన్‌స్ట్రక్ట్ చేయడానికి Co-op Translator MCP ను ఉపయోగించండి."
- "ఈ ఇమేజ్‌లో ఉన్న టెక్స్ట్ను జపనీస్‌కు అనువదించి ఫలితాన్ని సేవ్ చేయండి."
- "రిపాజిటరీని స్పానిష్‌కు డ్రై-రన్ చేసి ఏమి మారుతుందో నాకు చెప్పండి."
- "కొరియన్ అనువాద అవుట్పుట్ అప్డేట్ అయిందా అని సమీక్షించండి."

Markdown మరియు నోట్బుక్స్ కోసం, MCP రెండు మోడ్స్‌లో పని చేయవచ్చు:

| మోడ్ | ఎప్పుడు ఉపయోగించాలి | ప్రధాన టూల్స్ |
| --- | --- | --- |
| ఏజెంట్-సహాయంతో | MCP హోస్ట్ ఏజెంట్ తన స్వంత మోడల్ ఉపయోగించి చంక్‌లను అనువదించాలి, Co-op Translator LLM ప్రొవైడర్ క్రెడెన్షియల్స్ లేకుండా. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| ప్రొవైడర్-బ్యాక్డ్ | Co-op Translator సూటిగా Azure OpenAI, OpenAI, లేదా Anthropic ను కాల్ చేయాలి. | `translate_markdown_content`, `translate_notebook_content` |

MCP ప్రొవైడర్-బ్యాక్డ్ Markdown టూల్ కాల్ ఆకారం:

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

రిపాజిటరీ అనువాదం MCP ద్వారా డిఫాల్ట్‌గా డ్రై-రన్ అవుతుంది:

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

బాగా సరిపోతాయి:

- ఏజెంట్ లేదా ఎడిటర్‌లో సహజ-భাষ అనువాద వర్క్‌ఫ్లోలు కావాలి.
- హోస్ట్ ఏజెంట్ మోడల్ తయారైన చంక్‌లను అనువదించే Markdown లేదా నోట్బుక్ అనువాదం కావాలి.
- మొత్తం రిపాజిటరీకి బదులుగా ఎంపిక చేసిన కంటెంట్‌ను ఏజెంట్ అనువదించాలి.
- రిపాజిటరీ-స్థాయి రాయకాలకి ముందు ఒక ఆమోద దశ కావాలి.
- Markdown, నోట్బుక్, ఇమేజ్, సమీక్ష, మరియు మార్గ-రిరైటింగ్ టూల్స్‌ను ప్రదర్శించే ఒకే ఇంటర్‌ఫేస్ కావాలి.

## అవి ఎలా పరస్పరంగా సరిపోతాయి

CLI మనుష్యులు రిపాజిటరీలను అనువదించే సందర్భాల్లో అత్యుత్తమ డిఫాల్ట్. మీ కోడ్ వర్క్‌ఫ్లోను ఆధిపత్యం చేసుకుంటే Python API ఉత్తమం. ఏజెంట్ లేదా ఎడిటర్ వర్క్‌ఫ్లోను అధిపత్యం చేసుకుంటే MCP సర్వర్ ఉత్తమం.

మూడు మార్గాలన్నీ ఒకే పబ్లిక్ Co-op Translator APIని ఉపయోగిస్తాయి, కాబట్టి మీరు CLI తో మొదలు పెట్టి, తర్వాత Python తో ఆటోమెట్ చేయవచ్చు, మరియు ఏజెంట్-నిర్వహిత వర్క్‌ఫ్లోలు అవసరమయ్యాక అదే సామర్ధ్యాలను MCP క్లయింట్లకు ఎక్స్‌పోజ్ చేయవచ్చు.