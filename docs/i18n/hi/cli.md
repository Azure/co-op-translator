# CLI संदर्भ

Co-op Translator इन कमांड-लाइन एंट्री पॉइंट्स को इंस्टॉल करता है:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

कमांड `translate`, `evaluate`, `migrate-links`, और `co-op-review` को `co_op_translator.__main__` के माध्यम से डिस्पैच किया जाता है, जो बुलाए गए स्क्रिप्ट नाम के आधार पर कमांड के कार्यान्वयन का चयन करता है। MCP सर्वर सीधे `co_op_translator.mcp.server` का उपयोग करता है।

यदि आप CLI, Python API, और MCP के बीच निर्णय ले रहे हैं, तो [Choose Your Workflow](workflows.md) से शुरू करें।

## कंसोल आउटपुट

Interactive टर्मिनल कमांड हेडर, प्रोग्रेस, और सारांशों के लिए Rich फ़ॉर्मैटिंग का उपयोग करते हैं। CI और गैर-इंटरएक्टिव आउटपुट स्वतः ही सादा टेक्स्ट पर वापस लौटता है।

सादा आउटपुट के लिए `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` सेट करें, या Rich आउटपुट के लिए `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` सेट करें। लाइव प्रोग्रेस बार को दबाकर सारांश बनाए रखने के लिए `CO_OP_TRANSLATOR_NO_PROGRESS=1` सेट करें।

जब किसी अन्य सिस्टम को मशीन-पठनीय प्रगति की आवश्यकता हो तो `translate --json-events progress.ndjson` का उपयोग करें
CLI मानव-पठनीय आउटपुट को रेंडर करना जारी रखता है, जबकि
NDJSON फ़ाइल संस्करणीकृत `co-op.translation.event.v1` इवेंट्स प्राप्त करती है जिनमें
स्थिर फ़ील्ड जैसे `type`, `stage_key`, `completed`, `total`, और
`current_path` शामिल हैं।

## पहली बार CLI फ्लो

यदि आप टर्मिनल से Co-op Translator का उपयोग कर रहे हैं तो यहीं से शुरू करें:

1. [Configuration](configuration.md) में वर्णित अनुसार एक LLM प्रदाता कॉन्फ़िगर करें।
2. जिस सामग्री प्रकार का आप अनुवाद करना चाहते हैं, उसे चुनें।
3. पहले एक लक्षित कमांड चलाएँ, जैसे केवल Markdown अनुवाद।
4. बड़े रिपॉजिटरी परिवर्तन से पहले `--dry-run` का उपयोग करें।
5. संरचना और ताज़गी की जाँच के लिए अनुवाद के बाद `co-op-review` का उपयोग करें।

| लक्ष्य | शुरू करने के लिए कमांड |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | CLI कमांड सीधे चलाने की बजाय [MCP Server](mcp.md) को कॉन्फ़िगर करें। |

## translate

Markdown फ़ाइलों, नोटबुक्स, और इमेज टेक्स्ट को एक या अधिक लक्ष्य भाषाओं में अनुवाद करें।

```bash
translate -l "ko ja fr"
```

### सामान्य उदाहरण

केवल Markdown का अनुवाद करें:

```bash
translate -l "de" -md
```

केवल नोटबुक्स का अनुवाद करें:

```bash
translate -l "zh-CN" -nb
```

Markdown और इमेज का अनुवाद करें:

```bash
translate -l "pt-BR" -md -img
```

मौजूदा अनुवादों को हटाकर फिर से बनाकर अपडेट करें:

```bash
translate -l "ko" -u
```

इंटरएक्टिव प्रॉम्प्ट के बिना चलाएँ:

```bash
translate -l "ko ja" -md -y
```

लॉग्स सहेजें:

```bash
translate -l "ko" -s
```

संरचित प्रगति इवेंट लिखें:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### विकल्प

| विकल्प | आवश्यक | विवरण |
| --- | --- | --- |
| `-l`, `--language-codes` | हाँ | स्पेस-से पृथक भाषा कोड, जैसे "es fr de", या "all". |
| `-r`, `--root-dir` | नहीं | प्रोजेक्ट रूट। डिफ़ॉल्ट वर्तमान निर्देशिका है। |
| `-u`, `--update` | नहीं | चुनी हुई भाषाओं के लिए मौजूदा अनुवाद हटाकर उन्हें पुनः बनाएं। |
| `-img`, `--images` | नहीं | केवल इमेज फ़ाइलों का अनुवाद करें। |
| `-md`, `--markdown` | नहीं | केवल Markdown फ़ाइलों का अनुवाद करें। |
| `-nb`, `--notebook` | नहीं | केवल Jupyter नोटबुक फ़ाइलों का अनुवाद करें। |
| `-d`, `--debug` | नहीं | कंसोल में डिबग लॉगिंग सक्षम करें। |
| `-s`, `--save-logs` | नहीं | DEBUG-स्तर के लॉग `<root-dir>/logs/` के तहत सहेजें। |
| `--json-events` | नहीं | मशीन-पठनीय अनुवाद प्रगति इवेंट्स को NDJSON के रूप में लिखें। |
| `-x`, `--fix` | नहीं | पिछले मूल्यांकन परिणामों के आधार पर कम-विश्वास Markdown फ़ाइलों को पुन:अनुवाद करें। |
| `-c`, `--min-confidence` | नहीं | `--fix` के लिए विश्वास सीमा। डिफ़ॉल्ट `0.7` है। |
| `--add-disclaimer`, `--no-disclaimer` | नहीं | मशीन अनुवाद अस्वीकरण जोड़ें या दबाएँ। CLI में डिफ़ॉल्ट रूप से सक्षम है। |
| `-f`, `--fast` | नहीं | अप्रचलित तेज़ इमेज मोड। |
| `-y`, `--yes` | नहीं | प्रॉम्प्टों को स्वचालित रूप से पुष्टि करें, CI में उपयोगी। |
| `--repo-url` | नहीं | README भाषाओं की तालिका sparse-checkout सलाह में उपयोग किया जाने वाला रिपॉजिटरी URL। |
| `--migrate-language-folders` | नहीं | पुराने उपनाम फ़ोल्डर्स, जैसे `cn` या `tw`, को मानक BCP 47 फ़ोल्डर्स में पुनर्नामित करें। |
| `--dry-run` | नहीं | फ़ाइलें लिखे बिना भाषा फ़ोल्डर माइग्रेशन और अनुवाद अनुमानों का पूर्वावलोकन। |

यदि कोई प्रकार फ़्लैग नहीं दिया गया है, तो `translate` Markdown, नोटबुक्स, और इमेजेज़ को प्रोसेस करता है। इमेज अनुवाद के लिए Azure AI Vision कॉन्फ़िगरेशन आवश्यक है।

## evaluate

एक भाषा के लिए अनुवादित Markdown की गुणवत्ता का मूल्यांकन करें।

!!! warning "प्रायोगिक"
    `evaluate` प्रायोगिक है। यह नियम-आधारित और LLM-आधारित गुणवत्ता जाँचों का उपयोग कर सकता है, मूल्यांकन परिणामों को अनुवाद मेटाडेटा में लिखता है, और इसका स्कोरिंग मॉडल तथा मेटाडेटा व्यवहार बदल सकते हैं।

```bash
evaluate -l "ko"
```

### सामान्य उदाहरण

कठोर कम-विश्वास सीमा का उपयोग करें:

```bash
evaluate -l "es" -c 0.8
```

केवल नियम-आधारित जाँच चलाएँ:

```bash
evaluate -l "fr" -f
```

केवल LLM-आधारित जाँच चलाएँ:

```bash
evaluate -l "ja" -D
```

### विकल्प

| विकल्प | आवश्यक | विवरण |
| --- | --- | --- |
| `-l`, `--language-code` | हाँ | मूल्यांकन के लिए एकल भाषा कोड। उपनाम कोड सामान्यीकृत किए जाते हैं। |
| `-r`, `--root-dir` | नहीं | प्रोजेक्ट रूट। डिफ़ॉल्ट वर्तमान निर्देशिका है। |
| `-c`, `--min-confidence` | नहीं | कम-विश्वास अनुवादों को सूचीबद्ध करते समय उपयोग की जाने वाली सीमा। डिफ़ॉल्ट `0.7` है। |
| `-d`, `--debug` | नहीं | डिबग लॉगिंग सक्षम करें। |
| `-s`, `--save-logs` | नहीं | DEBUG-स्तर के लॉग `<root-dir>/logs/` के तहत सहेजें। |
| `-f`, `--fast` | नहीं | केवल नियम-आधारित मूल्यांकन। |
| `-D`, `--deep` | नहीं | केवल LLM-आधारित मूल्यांकन। |

डिफ़ॉल्ट रूप से, `evaluate` दोनों नियम-आधारित और LLM-आधारित मूल्यांकन का उपयोग करता है। परिणाम अनुवाद मेटाडेटा में लिखे जाते हैं और कंसोल में सारांशित होते हैं।

## co-op-review

API क्रेडेंशियल्स के बिना निर्धारक अनुवाद रखरखाव जाँच चलाएँ।

!!! note "बीटा"
    `co-op-review` एक बीटा निर्धारक समीक्षा कमांड है। यह मॉडल प्रदाताओं को कॉल नहीं करता और फ़ाइलें नहीं लिखता, लेकिन इसके चेक और इश्यू आउटपुट स्कीमा बदल सकते हैं।

```bash
co-op-review -l "ko"
```

### सामान्य उदाहरण

वर्तमान निर्देशिका से कोरियाई और जापानी अनुवादों की समीक्षा करें:

```bash
co-op-review -l "ko ja"
```

किसी विशिष्ट प्रोजेक्ट रूट की समीक्षा करें:

```bash
co-op-review -l "fr" -r ./my-course
```

README-केवल अनुवाद के बाद सिर्फ README की समीक्षा करें:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` अन्य दस्तावेज़ों और नेस्टेड README को अनदेखा करता है। यदि रूट
`README.md` गायब है तो यह विफल हो जाता है। `--changed-from` के साथ संयोजन में, यह केवल तभी README की समीक्षा करता है
जब वह सोर्स फ़ाइल बदली हो। README-केवल अनुवाद स्रोत README को अपरिवर्तित छोड़ता है,
जिसमें कोई भी साझा-सेक्शन मार्कर शामिल हैं।

केवल उन सोर्स फ़ाइलों की समीक्षा करें जो बेस रेफ़ के खिलाफ बदली गई हों:

```bash
co-op-review -l "ko" --changed-from origin/main
```

CI सारांशों के लिए GitHub-फ्लेवर्ड Markdown आउटपुट प्रिंट करें:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### विकल्प

| विकल्प | आवश्यक | विवरण |
| --- | --- | --- |
| `-l`, `--language-code` | नहीं | समीक्षा के लिए भाषा कोड। इसे कई बार पास किया जा सकता है या स्पेस-से पृथक मान के रूप में। डिफ़ॉल्ट सभी खोजी गई अनुवाद भाषाएँ हैं। |
| `-r`, `--root-dir` | नहीं | प्रोजेक्ट रूट। डिफ़ॉल्ट वर्तमान निर्देशिका है। |
| `--changed-from` | नहीं | बदली हुई सोर्स फ़ाइलों तक समीक्षा को सीमित करने के लिए उपयोग किया गया Git रेफ़। |
| `--readme-only` | नहीं | केवल रूट `README.md` अनुवाद की समीक्षा करें। |
| `--format` | नहीं | आउटपुट प्रारूप: `text` या `github`. डिफ़ॉल्ट `text` है। |

`co-op-review` वर्तमान में अनुपस्थित अनूदित फ़ाइलों, अनुपस्थित या पुराना अनुवाद मेटाडेटा, Markdown frontmatter और कोड फ़ेन्स की अखंडता, अमान्य अनूदित नोटबुक JSON, और स्थानीय Markdown या इमेज लिंक लक्ष्यों की अनुपस्थिति की जाँच करता है। लिंक की कमी डिफ़ॉल्ट रूप से चेतावनियाँ हैं; संरचनात्मक और ताजगी समस्याएँ कमांड को विफल करती हैं।

## co-op-translator-mcp

एजेंट्स, एडिटर्स, और MCP-अनुकूल क्लाइंट्स के लिए Co-op Translator MCP सर्वर चलाएँ।

```bash
co-op-translator-mcp
```

डिफ़ॉल्ट ट्रांसपोर्ट `stdio` है। क्लाइंट कॉन्फ़िगरेशन, टूल्स, संसाधन, और सुरक्षा नोट्स के लिए [MCP Server](mcp.md) गाइड देखें।

### विकल्प

| विकल्प | आवश्यक | विवरण |
| --- | --- | --- |
| `--transport` | नहीं | MCP ट्रांसपोर्ट: `stdio`, `streamable-http`, या `sse`. डिफ़ॉल्ट `stdio` है। |

## migrate-links

अनुवादित Markdown फ़ाइलों को पुनःप्रोसेस करें और नोटबुक लिंक अपडेट करें ताकि वे उपलब्ध होने पर अनूदित नोटबुक की ओर इशारा करें।

```bash
migrate-links -l "ko ja"
```

### सामान्य उदाहरण

लिंक अपडेट का पूर्वावलोकन करें:

```bash
migrate-links -l "ko" --dry-run
```

सभी समर्थित भाषाओं को बिना पुष्टि के प्रोसेस करें:

```bash
migrate-links -l "all" -y
```

केवल तब लिंक पुनर्लेखन करें जब अनूदित नोटबुक मौजूद हों:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### विकल्प

| विकल्प | आवश्यक | विवरण |
| --- | --- | --- |
| `-l`, `--language-codes` | हाँ | स्पेस-से पृथक भाषा कोड, या "all". |
| `-r`, `--root-dir` | नहीं | प्रोजेक्ट रूट। डिफ़ॉल्ट वर्तमान निर्देशिका है। |
| `--image-dir` | नहीं | रूट के सापेक्ष अनूदित इमेज निर्देशिका। डिफ़ॉल्ट `translated_images` है। |
| `--dry-run` | नहीं | वे फ़ाइलें दिखाएँ जो बदलेंगी, बिना अपडेट लिखे। |
| `--fallback-to-original`, `--no-fallback-to-original` | नहीं | अनूदित नोटबुक मौजूद नहीं होने पर मूल नोटबुक लिंक का उपयोग करें। डिफ़ॉल्ट रूप से सक्षम। |
| `-d`, `--debug` | नहीं | डिबग लॉगिंग सक्षम करें। |
| `-s`, `--save-logs` | नहीं | DEBUG-स्तर के लॉग `<root-dir>/logs/` के तहत सहेजें। |
| `-y`, `--yes` | नहीं | सभी भाषाओं को प्रोसेस करते समय प्रॉम्प्ट्स को स्वचालित रूप से कन्फर्म करें। |

## वातावरण

जब किसी कमांड को प्रदाता क्रेडेंशियल की आवश्यकता हो, तो इन प्रदाता सेट्स में से एक कॉन्फ़िगर करें। `translate --dry-run` और `co-op-review` को प्रदाता क्रेडेंशियल की आवश्यकता नहीं है:

```bash
# एज़्योर ओपनएआई
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# या ओपनएआई
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# या एंथ्रोपिक
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

इमेज अनुवाद के लिए अतिरिक्त रूप से Azure AI Vision आवश्यक है:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## आउटपुट लेआउट

टेक्स्ट अनुवाद निम्न स्थानों पर लिखे जाते हैं:

```text
translations/<language-code>/<original-path>
```

अनूदित इमेज आउटपुट निम्न स्थान पर लिखा जाता है:

```text
translated_images/<language-code>/<original-path>
```

उदाहरण के लिए, `README.md` और `docs/setup.md` को कोरियाई में अनुवाद करने से यह बनता है:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## कॉपी-पेस्ट CLI उदाहरण

Markdown को तीन भाषाओं में अनुवाद करें:

```bash
translate -l "ko ja fr" -md
```

केवल नोटबुक्स का अनुवाद करें:

```bash
translate -l "zh-CN" -nb
```

केवल इमेज का अनुवाद करें:

```bash
translate -l "pt-BR" -img
```

फ़ाइलें लिखे बिना Markdown अनुवाद का पूर्वावलोकन करें:

```bash
translate -l "de es" -md --dry-run
```

कम-विश्वास Markdown अनुवाद ठीक करें:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

CI-फ्रेंडली Markdown अनुवाद चलाएँ:

```bash
translate -l "ko ja" -md -y -s
```

अनूदित आउटपुट की समीक्षा करें:

```bash
co-op-review -l "ko ja"
```

लिंक माइग्रेशन का पूर्वावलोकन करें:

```bash
migrate-links -l "ko" --dry-run
```