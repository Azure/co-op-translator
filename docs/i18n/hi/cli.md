# CLI संदर्भ

Co-op Translator ये कमांड-लाइन एंट्री पॉइंट्स इंस्टॉल करता है:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

The `translate`, `evaluate`, `migrate-links`, and `co-op-review` commands dispatch through `co_op_translator.__main__`, which selects the command implementation based on the invoked script name. The MCP server uses `co_op_translator.mcp.server` directly.

If you are deciding between CLI, Python API, and MCP, start with [अपना वर्कफ़्लो चुनें](workflows.md).

## पहली बार CLI प्रवाह

Start here if you are using Co-op Translator from a terminal:

1. एक LLM प्रदाता को कॉन्फ़िगर करें जैसा कि [कॉन्फ़िगरेशन](configuration.md) में वर्णित है।
2. वह सामग्री प्रकार चुनें जिसे आप अनुवादित करना चाहते हैं।
3. पहले एक लक्षित कमांड चलाएं, जैसे केवल Markdown का अनुवाद।
4. बड़े रिपॉजिटरी परिवर्तन से पहले `--dry-run` का उपयोग करें।
5. संरचना और ताजगी की जाँच करने के लिए अनुवाद के बाद `co-op-review` का उपयोग करें।

| लक्ष्य | प्रारंभ करने के लिए कमांड |
| --- | --- |
| Markdown दस्तावेज़ अनुवाद करें | `translate -l "ko" -md` |
| नोटबुक अनुवाद करें | `translate -l "ko" -nb` |
| छवि पाठ का अनुवाद करें | `translate -l "ko" -img` |
| फाइलें लिखे बिना काम का पूर्वावलोकन करें | `translate -l "ko" -md --dry-run` |
| मौजूदा अनुवादों की समीक्षा करें | `co-op-review -l "ko"` |
| नोटबुक और Markdown लिंक अपडेट करें | `migrate-links -l "ko" --dry-run` |
| MCP क्लाइंट को टूल्स उपलब्ध कराएँ | CLI कमांड सीधे चलाने के बजाय [MCP सर्वर](mcp.md) कॉन्फ़िगर करें। |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

```bash
translate -l "ko ja fr"
```

### सामान्य उदाहरण

केवल Markdown अनुवाद करें:

```bash
translate -l "de" -md
```

केवल नोटबुक अनुवाद करें:

```bash
translate -l "zh-CN" -nb
```

Markdown और छवियाँ अनुवाद करें:

```bash
translate -l "pt-BR" -md -img
```

मौजूदा अनुवादों को हटाकर और पुनः बनाकर अपडेट करें:

```bash
translate -l "ko" -u
```

इंटरएक्टिव प्रॉम्प्ट्स के बिना चलाएं:

```bash
translate -l "ko ja" -md -y
```

लॉग्स सहेजें:

```bash
translate -l "ko" -s
```

### विकल्प

| विकल्प | आवश्यक | विवरण |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | स्पेस-सेपरेटेड भाषा कोड, जैसे `"es fr de"`, या `"all"`। |
| `-r`, `--root-dir` | No | प्रोजेक्ट रूट। डिफ़ॉल्ट वर्तमान निर्देशिका। |
| `-u`, `--update` | No | चुनी हुई भाषाओं के लिए मौजूदा अनुवाद हटाएँ और उन्हें पुनः बनाएं। |
| `-img`, `--images` | No | केवल छवि फ़ाइलों का अनुवाद करें। |
| `-md`, `--markdown` | No | केवल Markdown फ़ाइलों का अनुवाद करें। |
| `-nb`, `--notebook` | No | केवल Jupyter नोटबुक फ़ाइलों का अनुवाद करें। |
| `-d`, `--debug` | No | कंसोल में डिबग लॉगिंग सक्षम करें। |
| `-s`, `--save-logs` | No | `<root-dir>/logs/` के तहत DEBUG-स्तर के लॉग सहेजें। |
| `-x`, `--fix` | No | पिछले मूल्यांकन परिणामों के आधार पर कम-विश्वास Markdown फ़ाइलों को पुनः अनुवाद करें। |
| `-c`, `--min-confidence` | No | `--fix` के लिए विश्वसनीयता सीमा। डिफ़ॉल्ट `0.7`। |
| `--add-disclaimer`, `--no-disclaimer` | No | मशीन अनुवाद अस्वीकरण जोड़ें या दबाएँ। CLI में डिफ़ॉल्ट रूप से सक्षम। |
| `-f`, `--fast` | No | अप्रचलित तेज़ इमेज मोड। |
| `-y`, `--yes` | No | प्रॉम्प्ट्स को स्वतः-पुष्टि करें, CI में उपयोगी। |
| `--repo-url` | No | README भाषाओं तालिका के sparse-checkout सलाह में उपयोग किया जाने वाला रिपॉजिटरी URL। |
| `--migrate-language-folders` | No | पुराने उपनाम फ़ोल्डरों को, जैसे `cn` या `tw`, canonical BCP 47 फ़ोल्डरों में नाम बदलें। |
| `--dry-run` | No | फाइलें लिखे बिना भाषा फ़ोल्डर माइग्रेशन और अनुवाद अनुमान का पूर्वावलोकन करें। |

If no type flag is provided, `translate` processes Markdown, notebooks, and images. Image translation requires Azure AI Vision configuration.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "प्रायोगिक"
    `evaluate` is experimental. It can use rule-based and LLM-based quality checks, writes evaluation results into translation metadata, and its scoring model and metadata behavior may change.

```bash
evaluate -l "ko"
```

### सामान्य उदाहरण

कठोर कम-विश्वास सीमा का उपयोग करें:

```bash
evaluate -l "es" -c 0.8
```

केवल नियम-आधारित जाँच चलाएं:

```bash
evaluate -l "fr" -f
```

केवल LLM-आधारित जाँच चलाएं:

```bash
evaluate -l "ja" -D
```

### विकल्प

| विकल्प | आवश्यक | विवरण |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | मूल्यांकन करने के लिए एकल भाषा कोड। उपनाम कोड सामान्यीकृत होते हैं। |
| `-r`, `--root-dir` | No | प्रोजेक्ट रूट। डिफ़ॉल्ट वर्तमान निर्देशिका। |
| `-c`, `--min-confidence` | No | उन कम-विश्वास अनुवादों को सूचीबद्ध करने के लिए प्रयुक्त सीमा। डिफ़ॉल्ट `0.7`। |
| `-d`, `--debug` | No | डिबग लॉगिंग सक्षम करें। |
| `-s`, `--save-logs` | No | `<root-dir>/logs/` के तहत DEBUG-स्तर के लॉग सहेजें। |
| `-f`, `--fast` | No | केवल नियम-आधारित मूल्यांकन। |
| `-D`, `--deep` | No | केवल LLM-आधारित मूल्यांकन। |

डिफ़ॉल्ट रूप से, `evaluate` दोनों नियम-आधारित और LLM-आधारित मूल्यांकन का उपयोग करता है। परिणाम अनुवाद मेटाडेटा में लिखे जाते हैं और कंसोल में सारांशित होते हैं।

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "बीटा"
    `co-op-review` is a beta deterministic review command. It does not call model providers or write files, but its checks and issue output schema may evolve.

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

केवल उन स्रोत फ़ाइलों की समीक्षा करें जो बेस रेफ के खिलाफ बदली गई हैं:

```bash
co-op-review -l "ko" --changed-from origin/main
```

CI सारांशों के लिए GitHub-उन्मुख Markdown आउटपुट प्रिंट करें:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### विकल्प

| विकल्प | आवश्यक | विवरण |
| --- | --- | --- |
| `-l`, `--language-code` | No | समीक्षा के लिए भाषा कोड। कई बार पास किया जा सकता है या स्पेस-सेपरेटेड मान के रूप में। डिफ़ॉल्ट सभी पाए गए अनुवादित भाषाएँ। |
| `-r`, `--root-dir` | No | प्रोजेक्ट रूट। डिफ़ॉल्ट वर्तमान निर्देशिका। |
| `--changed-from` | No | स्रोत फ़ाइलों को सीमित करने के लिए उपयोग किया जाने वाला Git रेफ। |
| `--format` | No | आउटपुट फ़ॉर्मेट: `text` या `github`। डिफ़ॉल्ट `text`। |

`co-op-review` वर्तमान में ग़ायब अनुवादित फ़ाइलों, ग़ायब या पुराने अनुवाद मेटाडेटा, Markdown frontmatter और कोड फेंस अखंडता, अवैध अनुवादित नोटबुक JSON, और ग़ायब स्थानीय Markdown या इमेज लिंक लक्ष्यों के लिए जाँच करता है। ग़ायब लिंक डिफ़ॉल्ट रूप से चेतावनियाँ होती हैं; संरचनात्मक और ताजगी संबंधित समस्याएँ कमांड को असफल कर देती हैं।

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [MCP सर्वर](mcp.md) guide for client configuration, tools, resources, and safety notes.

### विकल्प

| विकल्प | आवश्यक | विवरण |
| --- | --- | --- |
| `--transport` | No | MCP ट्रांसपोर्ट: `stdio`, `streamable-http`, या `sse`। डिफ़ॉल्ट `stdio`। |

## migrate-links

Reprocess translated Markdown files and update notebook links so they point to translated notebooks when available.

```bash
migrate-links -l "ko ja"
```

### सामान्य उदाहरण

लिंक अपडेट्स का पूर्वावलोकन करें:

```bash
migrate-links -l "ko" --dry-run
```

पुष्टिकरण के बिना सभी समर्थित भाषाओं को प्रोसेस करें:

```bash
migrate-links -l "all" -y
```

केवल तब लिंक रीराइट करें जब अनुवादित नोटबुक उपलब्ध हों:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### विकल्प

| विकल्प | आवश्यक | विवरण |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | स्पेस-सेपरेटेड भाषा कोड, या `"all"`। |
| `-r`, `--root-dir` | No | प्रोजेक्ट रूट। डिफ़ॉल्ट वर्तमान निर्देशिका। |
| `--image-dir` | No | रूट के सापेक्ष अनुवादित इमेज निर्देशिका। डिफ़ॉल्ट `translated_images`। |
| `--dry-run` | No | अपडेट लिखे बिना जिन फ़ाइलों में बदलाव होंगे उन्हें दिखाएँ। |
| `--fallback-to-original`, `--no-fallback-to-original` | No | जब अनुवादित नोटबुक गायब हों तो मूल नोटबुक लिंक का उपयोग करें। डिफ़ॉल्ट सक्षम। |
| `-d`, `--debug` | No | डिबग लॉगिंग सक्षम करें। |
| `-s`, `--save-logs` | No | `<root-dir>/logs/` के तहत DEBUG-स्तर के लॉग सहेजें। |
| `-y`, `--yes` | No | सभी भाषाओं को प्रोसेस करते समय प्रॉम्प्ट्स को स्वतः-पुष्टि करें। |

## पर्यावरण

All commands require one configured LLM provider:

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
```

Image translation additionally requires Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## आउटपुट लेआउट

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

Translated image output is written under:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## कॉपी-पेस्ट CLI उदाहरण

Markdown को तीन भाषाओं में अनुवाद करें:

```bash
translate -l "ko ja fr" -md
```

केवल नोटबुक अनुवाद करें:

```bash
translate -l "zh-CN" -nb
```

केवल छवियाँ अनुवाद करें:

```bash
translate -l "pt-BR" -img
```

फाइलें लिखे बिना Markdown अनुवाद का पूर्वावलोकन करें:

```bash
translate -l "de es" -md --dry-run
```

कम-विश्वास Markdown अनुवादों की मरम्मत करें:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

CI-अनुकूल Markdown अनुवाद चलाएँ:

```bash
translate -l "ko ja" -md -y -s
```

अनुवादित आउटपुट की समीक्षा करें:

```bash
co-op-review -l "ko ja"
```

लिंक माइग्रेशन का पूर्वावलोकन करें:

```bash
migrate-links -l "ko" --dry-run
```