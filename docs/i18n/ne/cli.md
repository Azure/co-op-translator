# CLI सन्दर्भ

Co-op Translator यी कमाण्ड–लाइन प्रवेश बिन्दुहरू स्थापना गर्छ:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

The `translate`, `evaluate`, `migrate-links`, र `co-op-review` कमाण्डहरूले `co_op_translator.__main__` मार्फत डिस्प्याच गर्दछन्, जसले आह्वान गरिएको स्क्रिप्ट नामको आधारमा कमाण्डको कार्यान्वयन चयन गर्दछ। MCP सर्भरले सिधै `co_op_translator.mcp.server` प्रयोग गर्छ।

CLI, Python API, र MCP बीच निर्णय गर्दै हुनुहुन्छ भने, [आफ्नो कार्यप्रवाह छान्नुहोस्](workflows.md) बाट सुरु गर्नुहोस्।

## कन्सोल आउटपुट

इन्टरएक्टिभ टर्मिनलहरूले कमाण्ड हेडर, प्रगति, र सारांसहरूका लागि Rich फर्म्याटिङ प्रयोग गर्छन्। CI र गैर-इन्टरएक्टिभ आउटपुटले स्वचालित रूपमा साधारण पाठमा फर्किन्छ।

`CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` लाई साधारण आउटपुट अनिवार्य बनाउन सेट गर्नुहोस्, वा `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` लाई Rich आउटपुट अनिवार्य बनाउन। `CO_OP_TRANSLATOR_NO_PROGRESS=1` सेट गर्दा सारांशहरू राखिन्छन् जबकि लाइभ प्रगति बारहरू दबाइन्छ।

`translate --json-events progress.ndjson` प्रयोग गर्नुहोस् जब अर्को प्रणालीलाई आवश्यक हुन्छ
मेसिन-पठनीय प्रगति। CLI मानव-उन्मुख आउटपुट रेंडर गर्न जारी राख्छ, जबकि
NDJSON फाइलले संस्करणयुक्त `co-op.translation.event.v1` इभेन्टहरू प्राप्त गर्छ जसमा
स्थिर फिल्डहरू जस्तै `type`, `stage_key`, `completed`, `total`, र
`current_path`.

## पहिलो पटक CLI प्रवाह

यदि तपाईं टर्मिनलबाट Co-op Translator प्रयोग गर्दै हुनुहुन्छ भने यहाँबाट सुरु गर्नुहोस्:

1. [Configuration](configuration.md) मा वर्णन गरिएको अनुसार LLM प्रदायक कन्फिगर गर्नुहोस्।
2. अनुवाद गर्न चाहनु भएको सामग्री प्रकार छान्नुहोस्।
3. पहिले केन्द्रित कमाण्ड चलाउनुहोस्, जस्तै Markdown मात्र अनुवाद।
4. ठूलो रिपोजिटरी परिवर्तन भन्दा पहिले `--dry-run` प्रयोग गर्नुहोस्।
5. संरचना र ताजापन जाँच गर्न अनुवादपछि `co-op-review` प्रयोग गर्नुहोस्।

| लक्ष्य | सुरु गर्ने कमाण्ड |
| --- | --- |
| Markdown दस्तावेजहरू अनुवाद गर्नुहोस् | `translate -l "ko" -md` |
| नोटबुकहरू अनुवाद गर्नुहोस् | `translate -l "ko" -nb` |
| चित्रको पाठ अनुवाद गर्नुहोस् | `translate -l "ko" -img` |
| फाइलहरू लेख्नु नपरी कामको पूर्वावलोकन गर्नुहोस् | `translate -l "ko" -md --dry-run` |
| अवस्थित अनुवादहरू समीक्षा गर्नुहोस् | `co-op-review -l "ko"` |
| नोटबुक र Markdown लिंकहरू अपडेट गर्नुहोस् | `migrate-links -l "ko" --dry-run` |
| उपकरणहरू MCP क्लाइन्टलाई उपलब्ध गराउनुहोस् | सिधै CLI कमाण्ड चलाउने सट्टा [MCP Server](mcp.md) कन्फिगर गर्नुहोस्। |

## translate

Markdown फाइलहरू, नोटबुकहरू, र छवि पाठहरूलाई एक वा एकभन्दा बढी लक्ष्य भाषाहरूमा अनुवाद गर्नुहोस्।

```bash
translate -l "ko ja fr"
```

### सामान्य उदाहरणहरू

Markdown मात्र अनुवाद गर्नुहोस्:

```bash
translate -l "de" -md
```

Translate only notebooks:

```bash
translate -l "zh-CN" -nb
```

Translate Markdown and images:

```bash
translate -l "pt-BR" -md -img
```

अघिल्ला अनुवादहरू मेटेर र पुनः सिर्जना गरेर अद्यावधिक गर्नुहोस्:

```bash
translate -l "ko" -u
```

Run without interactive prompts:

```bash
translate -l "ko ja" -md -y
```

Save logs:

```bash
translate -l "ko" -s
```

Write structured progress events:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### विकल्पहरू

| विकल्प | आवश्यक | विवरण |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | स्पेसले छुट्याइएका भाषा कोडहरू, जस्तै `"es fr de"`, वा `"all"`। |
| `-r`, `--root-dir` | No | प्रोजेक्ट रुट। डिफल्टले हालको निर्देशिका हो। |
| `-u`, `--update` | No | चयन गरिएका भाषाहरूका लागि अवस्थित अनुवादहरू मेटेर पुनः सिर्जना गर्नुहोस्। |
| `-img`, `--images` | No | केवल इमेज फाइलहरू अनुवाद गर्नुहोस्। |
| `-md`, `--markdown` | No | केवल Markdown फाइलहरू अनुवाद गर्नुहोस्। |
| `-nb`, `--notebook` | No | केवल Jupyter नोटबुक फाइलहरू अनुवाद गर्नुहोस्। |
| `-d`, `--debug` | No | कन्सोलमा डिबग लगिङ सक्षम गर्नुहोस्। |
| `-s`, `--save-logs` | No | DEBUG-स्तरका लगहरू `<root-dir>/logs/` भित्र सुरक्षित गर्नुहोस्। |
| `--json-events` | No | अनुवाद प्रगतिको मेसिन-पठनीय घटनाहरू NDJSON रूपमा लेख्नुहोस्। |
| `-x`, `--fix` | No | अघिल्लो मूल्यांकन परिणामहरूका आधारमा कम-विश्वासका Markdown फाइलहरू पुन: अनुवाद गर्नुहोस्। |
| `-c`, `--min-confidence` | No | `--fix` का लागि विश्वसनीयता थ्रेसहोल्ड। डिफल्ट `0.7`। |
| `--add-disclaimer`, `--no-disclaimer` | No | मेसिन अनुवाद अस्वीकरणहरू थप्ने वा दबाउने। CLI मा डिफल्टले सक्षम छ। |
| `-f`, `--fast` | No | अप्रचलित फास्ट इमेज मोड। |
| `-y`, `--yes` | No | प्रम्प्टहरू स्वचालित रूपमा पुष्टि गर्ने, CI मा उपयोगी। |
| `--repo-url` | No | README भाषा तालिकामा sparse-checkout सल्लाहका लागि प्रयोग हुने रिपोजिटरी URL। |
| `--migrate-language-folders` | No | पुराना उपनाम फोल्डरहरू, जस्तै `cn` वा `tw`, लाई मान्य BCP 47 फोल्डर नाममा परिवर्तन गर्नुहोस्। |
| `--dry-run` | No | फाइल लेख्नु नपरी भाषा फोल्डर माइग्रेशन र अनुवाद अनुमानहरूको पूर्वावलोकन गर्नुहोस्। |

यदि कुनै प्रकार फ्ल्याग प्रदान गरिएको छैन भने, `translate` ले Markdown, नोटबुकहरू, र छविहरू प्रोसेस गर्छ। छवि अनुवादका लागि Azure AI Vision कन्फिगरेसन आवश्यक छ।

## evaluate

एक भाषाको लागि अनुवादित Markdown को गुणस्तर मूल्याङ्कन गर्नुहोस्।

!!! warning "प्रयोगात्मक"
    `evaluate` प्रयोगात्मक छ। यसले नियम-आधारित र LLM-आधारित गुणस्तर जाँचहरू प्रयोग गर्न सक्छ, मूल्याङ्कन परिणामहरू अनुवाद मेटाडेटामा लेख्छ, र यसको स्कोरिङ मोडेल तथा मेटाडेटा व्यवहार परिवर्तन हुन सक्छ।

```bash
evaluate -l "ko"
```

### सामान्य उदाहरणहरू

कम आत्मविश्वासको थ्रेसहोल्ड कडा राख्नुहोस्:

```bash
evaluate -l "es" -c 0.8
```

Run rule-based checks only:

```bash
evaluate -l "fr" -f
```

Run LLM-based checks only:

```bash
evaluate -l "ja" -D
```

### विकल्पहरू

| विकल्प | आवश्यक | विवरण |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | मूल्याङ्कनका लागि एकल भाषा कोड। उपनाम कोडहरू सामान्यीकृत गरिन्छ। |
| `-r`, `--root-dir` | No | प्रोजेक्ट रुट। डिफल्टले हालको निर्देशिका हो। |
| `-c`, `--min-confidence` | No | कम-विश्वास अनुवादहरू सूची गर्दा प्रयोग हुने थ्रेसहोल्ड। डिफल्ट `0.7`। |
| `-d`, `--debug` | No | डिबग लगिङ सक्षम गर्नुहोस्। |
| `-s`, `--save-logs` | No | DEBUG-स्तरका लगहरू `<root-dir>/logs/` भित्र सुरक्षित गर्नुहोस्। |
| `-f`, `--fast` | No | नियम-आधारित मूल्याङ्कन मात्र। |
| `-D`, `--deep` | No | LLM-आधारित मूल्याङ्कन मात्र। |

डिफल्ट रूपमा, `evaluate` ले नियम-आधारित र LLM-आधारित दुवै मूल्याङ्कन प्रयोग गर्छ। परिणामहरू अनुवाद मेटाडाटा मा लेखिन्छन् र कन्सोलमा सारांश गरिन्छ।

## co-op-review

API प्रमाण-पत्रहरू बिना निर्धारक अनुवाद मर्मत जाँचहरू चलाउनुहोस्।

!!! note "बीटा"
    `co-op-review` एक बीटा निर्धारक समीक्षा कमाण्ड हो। यसले मोडेल प्रदायकहरूलाई कल गर्दैन वा फाइलहरू लेख्दैन, तर यसको जाँचहरू र मुद्दा आउटपुट स्किमा विकास हुन सक्छ।

```bash
co-op-review -l "ko"
```

### सामान्य उदाहरणहरू

हालको डाइरेक्टरीबाट कोरियन र जापानी अनुवादहरू समीक्षा गर्नुहोस्:

```bash
co-op-review -l "ko ja"
```

Review a specific project root:

```bash
co-op-review -l "fr" -r ./my-course
```

README-मै गरिएको अनुवादपछि केवल README समीक्षा गर्नुहोस्:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` अरू कागजातहरू र नेस्टेड READMEहरूलाई बेवास्ता गर्दछ। यो असफल हुन्छ यदि मूल
`README.md` अनुपस्थित छ। `--changed-from` सँग संयुक्त गर्दा, यसले केवल README मात्र समीक्षा गर्छ
जब त्यो स्रोत फाइल परिवर्तन भएको छ। README-मात्र अनुवादले स्रोत README लाई
अपरिवर्तित राख्छ, जसमा कुनै पनि साझा-सेक्शन मार्करहरू समावेश छन्।

एक base ref विरुद्ध परिवर्तन भएका मात्र स्रोत फाइलहरू समीक्षा गर्नुहोस्:

```bash
co-op-review -l "ko" --changed-from origin/main
```

CI सारांशहरूको लागि GitHub-flavored Markdown आउटपुट प्रिन्ट गर्नुहोस्:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### विकल्पहरू

| विकल्प | आवश्यक | विवरण |
| --- | --- | --- |
| `-l`, `--language-code` | No | समीक्षा गर्नको लागि भाषा कोड। एकै पटक धेरै पटक वा स्पेस-सेपरेटेड मानका रूपमा पास गर्न सकिन्छ। डिफल्टले पत्ता लागेका सबै अनुवाद भाषाहरू। |
| `-r`, `--root-dir` | No | प्रोजेक्ट रुट। डिफल्टले हालको निर्देशिका हो। |
| `--changed-from` | No | समीक्षा परिवर्तन भएका स्रोत फाइलहरूमा सीमित गर्न प्रयोग गरिने Git रेफ। |
| `--readme-only` | No | केवल रुट `README.md` अनुवाद मात्र समीक्षा गर्नुहोस्। |
| `--format` | No | आउटपुट ढाँचा: `text` वा `github`। डिफल्ट `text`। |

`co-op-review` हाल अनुवादित फाइलहरू हराइरहेका छन् कि छैनन्, हराएको वा पुरानो अनुवाद मेटाडाटा, Markdown frontmatter र code fence को अखण्डता, अमान्य अनुवादित नोटबुक JSON, र स्थानीय Markdown वा छवि लिंक लक्ष्य हराइरहेका छन् कि छैनन् जाँच गर्छ। हराइरहेका लिङ्कहरू डिफल्ट रूपमा चेतावनी हुन्; संरचनात्मक र ताजगी सम्बन्धी समस्याहरूले कमाण्ड असफल बनाउँछन्।

## co-op-translator-mcp

एजेन्टहरू, सम्पादकहरू, र MCP-समर्थित क्लाइन्टहरूको लागि Co-op Translator MCP सर्भर चलाउनुहोस्।

```bash
co-op-translator-mcp
```

डिफल्ट ट्रान्सपोर्ट `stdio` हो। क्लाइन्ट कन्फिगरेसन, उपकरणहरू, स्रोतहरू, र सुरक्षा नोटहरूको लागि [MCP सर्भर](mcp.md) मार्गदर्शन हेर्नुहोस्।

### Options

| विकल्प | आवश्यक | विवरण |
| --- | --- | --- |
| `--transport` | No | MCP ट्रान्सपोर्ट: `stdio`, `streamable-http`, या `sse`। डिफल्ट `stdio`। |

## migrate-links

अनुवादित Markdown फाइलहरू पुन:प्रोसेस गर्नुहोस् र नोटबुक लिंकहरू अद्यावधिक गर्नुहोस् ताकि उपलब्ध हुँदा तिनीहरू अनुवादित नोटबुकहरूतर्फ संकेत गरोस्।

```bash
migrate-links -l "ko ja"
```

### सामान्य उदाहरणहरू

Preview link updates:

```bash
migrate-links -l "ko" --dry-run
```

पुष्टिकरण बिना सबै समर्थित भाषाहरू प्रक्रिया गर्नुहोस्:

```bash
migrate-links -l "all" -y
```

अनुवादित नोटबुकहरू उपलब्ध हुँदा मात्र लिङ्कहरू पुन:लेख्नुहोस्:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### विकल्पहरू

| विकल्प | आवश्यक | विवरण |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | स्पेसले छुट्याइएका भाषा कोडहरू, वा `"all"`। |
| `-r`, `--root-dir` | No | प्रोजेक्ट रुट। डिफल्टले हालको निर्देशिका हो। |
| `--image-dir` | No | रुट सापेक्ष अनुवादित इमेज निर्देशिका। डिफल्ट `translated_images`। |
| `--dry-run` | No | अपडेट लेख्नु नपरी कुन फाइलहरू परिवर्तन हुने थिए देखाउनुहोस्। |
| `--fallback-to-original`, `--no-fallback-to-original` | No | अनुवादित नोटबुकहरू हराएको अवस्थामा मूल नोटबुक लिंक प्रयोग गर्ने। डिफल्टले सक्षम छ। |
| `-d`, `--debug` | No | डिबग लगिङ सक्षम गर्नुहोस्। |
| `-s`, `--save-logs` | No | DEBUG-स्तरका लगहरू `<root-dir>/logs/` भित्र सुरक्षित गर्नुहोस्। |
| `-y`, `--yes` | No | सबै भाषाहरू प्रक्रिया गर्दा प्रम्प्टहरू स्वचालित रूपले पुष्टि गर्नुहोस्। |

## वातावरण

जब कुनै कमाण्डले प्रदायक प्रमाणपत्रहरू आवश्यक पार्दछ, यी प्रदायक सेटहरूमध्ये एक कन्फिगर गर्नुहोस्। `translate --dry-run` र `co-op-review` लाई प्रदायक प्रमाणपत्रहरू आवश्यक पर्दैन:

```bash
# एज्योर OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# वा OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# वा Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

छवि अनुवादका लागि थप रूपमा Azure AI Vision आवश्यक छ:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## आउटपुट लेआउट

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

अनुवाद गरिएको छवि आउटपुट निम्न स्थानमा लेखिन्छ:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## कपी-पेस्ट CLI उदाहरणहरू

Translate Markdown into three languages:

```bash
translate -l "ko ja fr" -md
```

Translate notebooks only:

```bash
translate -l "zh-CN" -nb
```

Translate images only:

```bash
translate -l "pt-BR" -img
```

फाइलहरू लेख्ने बिना मार्कडाउन अनुवाद पूर्वावलोकन:

```bash
translate -l "de es" -md --dry-run
```

Repair low-confidence Markdown translations:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Run CI-friendly Markdown translation:

```bash
translate -l "ko ja" -md -y -s
```

Review translated output:

```bash
co-op-review -l "ko ja"
```

Preview link migration:

```bash
migrate-links -l "ko" --dry-run
```