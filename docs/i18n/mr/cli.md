# CLI संदर्भ

Co-op Translator हे खालील कमांड-लाइन एंट्री प्वाइंट इंस्टॉल करते:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

`translate`, `evaluate`, `migrate-links`, आणि `co-op-review` कमांड्स `co_op_translator.__main__` द्वारे डिस्पॅच केल्या जातात, जे कॉल केलेल्या स्क्रिप्टच्या नावावर आधारित कमांड अंमलबजावणी निवडते. MCP सर्व्ह्हर थेट `co_op_translator.mcp.server` वापरते.

जर आपण CLI, Python API, आणि MCP यांपैकी निवड करत असाल, तर [आपला कार्यप्रवाह निवडा](workflows.md) पासून सुरुवात करा.

## प्रथमच CLI प्रवाह

टर्मिनलमधून Co-op Translator वापरत असाल तर येथे सुरुवात करा:

1. [कॉन्फिगरेशन](configuration.md) मध्ये वर्णन केलेल्या प्रमाणे LLM प्रदाता कॉन्फिगर करा.
2. आपण ज्या प्रकारचे कंटेंट अनुवादित करायचे आहे ते निवडा.
3. प्रथम एक लक्षित कमांड चालवा, जसे की फक्त Markdown अनुवाद.
4. मोठ्या रेपॉझिटरी बदलांपूर्वी `--dry-run` वापरा.
5. संरचना आणि ताजेपणा तपासण्यासाठी अनुवादानंतर `co-op-review` वापरा.

| Goal | Command to start with |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | Configure the [MCP Server](mcp.md) instead of running CLI commands directly. |

## translate

Markdown फाइल्स, नोटबुक, आणि इमेज मजकूर एक किंवा अधिक लक्ष्य भाषांमध्ये अनुवादित करा.

```bash
translate -l "ko ja fr"
```

### सामान्य उदाहरणे

फक्त Markdown अनुवाद करा:

```bash
translate -l "de" -md
```

फक्त नोटबुक अनुवाद करा:

```bash
translate -l "zh-CN" -nb
```

Markdown आणि इमेजेस अनुवाद करा:

```bash
translate -l "pt-BR" -md -img
```

अस्तित्वात असलेले अनुवाद हटवून पुन्हा तयार करून अपडेट करा:

```bash
translate -l "ko" -u
```

इंटरएक्टिव्ह प्रॉम्प्टशिवाय चालवा:

```bash
translate -l "ko ja" -md -y
```

लॉग सेव्ह करा:

```bash
translate -l "ko" -s
```

### पर्याय

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Space-separated language codes, such as `"es fr de"`, or `"all"`. |
| `-r`, `--root-dir` | No | प्रोजेक्ट रूट. डिफॉल्ट सध्याच्या निर्देशिकेवर आहे. |
| `-u`, `--update` | No | निवडलेल्या भाषांसाठी विद्यमान अनुवाद हटवून पुन्हा तयार करा. |
| `-img`, `--images` | No | फक्त इमेज फाइल्स अनुवादित करा. |
| `-md`, `--markdown` | No | फक्त Markdown फाइल्स अनुवादित करा. |
| `-nb`, `--notebook` | No | फक्त Jupyter नोटबुक फाइल्स अनुवादित करा. |
| `-d`, `--debug` | No | कन्सोलमध्ये डिबग लॉगिंग सक्षम करा. |
| `-s`, `--save-logs` | No | `<root-dir>/logs/` अंतर्गत DEBUG-स्तरीय लॉग जतन करा. |
| `-x`, `--fix` | No | मागील मूल्यमापन परिणामांच्या आधारे कमी-कॉनफिडन्स Markdown फाइल्स पुनःअनुवाद करा. |
| `-c`, `--min-confidence` | No | `--fix` साठी कॉन्फिडन्स थ्रेशहोल्ड. डिफॉल्ट `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | मशीन ट्रान्सलेशन डिस्क्लेमर जोडा किंवा दडवा. CLI मध्ये डिफॉल्टने सक्षम आहे. |
| `-f`, `--fast` | No | डिप्रिकेटेड फास्ट इमेज मोड. |
| `-y`, `--yes` | No | प्रॉम्प्ट्स ऑटो-कन्फर्म करा, CI मध्ये उपयुक्त. |
| `--repo-url` | No | README भाषासारणी सल्ल्यांमध्ये वापरले जाणारे रेपॉझिटरी URL. |
| `--migrate-language-folders` | No | जुने उपनाम फोल्डर्स, जसे `cn` किंवा `tw`, मुख्य BCP 47 फोल्डर्समध्ये नाव बदला. |
| `--dry-run` | No | भाषा फोल्डर माइग्रेशन आणि अनुवाद अंदाज फाइल्स न लिहिता प्रीव्ह्यू करा. |

जर कोणताही प्रकार फ्लॅग प्रदान केला नसेल, तर `translate` Markdown, नोटबुक्स आणि इमेजेस प्रक्रिया करते. इमेज अनुवादासाठी Azure AI Vision कॉन्फिगरेशन आवश्यक आहे.

## evaluate

एका भाषेसाठी अनुवादित Markdown ची गुणवत्ता मूल्यमापन करा.

!!! warning "Experimental"
    `evaluate` is experimental. It can use rule-based and LLM-based quality checks, writes evaluation results into translation metadata, and its scoring model and metadata behavior may change.

```bash
evaluate -l "ko"
```

### सामान्य उदाहरणे

कठोर कमी-कॉनफिडन्स थ्रेशहोल्ड वापरा:

```bash
evaluate -l "es" -c 0.8
```

फक्त नियम-आधारित तपासण्या चालवा:

```bash
evaluate -l "fr" -f
```

फक्त LLM-आधारित तपासण्या चालवा:

```bash
evaluate -l "ja" -D
```

### पर्याय

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | मूल्यमापन करण्यासाठी एकल भाषा कोड. अॅलियस कोड सामान्यीकृत केले जातात. |
| `-r`, `--root-dir` | No | प्रोजेक्ट रूट. डिफॉल्ट सध्याच्या निर्देशिकेवर आहे. |
| `-c`, `--min-confidence` | No | कमी-कॉनफिडन्स अनुवादांची यादी करताना वापरले जाणारे थ्रेशहोल्ड. डिफॉल्ट `0.7`. |
| `-d`, `--debug` | No | डिबग लॉगिंग सक्षम करा. |
| `-s`, `--save-logs` | No | `<root-dir>/logs/` अंतर्गत DEBUG-स्तरीय लॉग जतन करा. |
| `-f`, `--fast` | No | फक्त नियम-आधारित मूल्यमापन. |
| `-D`, `--deep` | No | फक्त LLM-आधारित मूल्यमापन. |

डिफॉल्टनुसार, `evaluate` नियम-आधारित आणि LLM-आधारित दोन्ही मूल्यमापन वापरते. परिणाम अनुवाद मेटाडेटामध्ये लिहिले जातात आणि कन्सोलमध्ये सारांशित केले जातात.

## co-op-review

API क्रेडेन्शियल्स न वापरता निर्धारक अनुवाद देखभाल तपासण्या चालवा.

!!! note "Beta"
    `co-op-review` is a beta deterministic review command. It does not call model providers or write files, but its checks and issue output schema may evolve.

```bash
co-op-review -l "ko"
```

### सामान्य उदाहरणे

सध्याच्या निर्देशिकेमधून कोरियन आणि जपानी अनुवाद पुनरावलोकन करा:

```bash
co-op-review -l "ko ja"
```

विशिष्ट प्रोजेक्ट रूट पुनरावलोकन करा:

```bash
co-op-review -l "fr" -r ./my-course
```

फक्त बेस रेफच्या विरुद्ध बदललेल्या स्रोत फाइल्स पुनरावलोकन करा:

```bash
co-op-review -l "ko" --changed-from origin/main
```

CI सारांशांसाठी GitHub-फ्लेवर्ड Markdown आउटपुट प्रिंट करा:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### पर्याय

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | No | पुनरावलोकनासाठी भाषा कोड. एकापेक्षा जास्त वेळा किंवा स्पेस-वेगळ्या किमतींसह पास केला जाऊ शकतो. डिफॉल्ट सर्व शोधलेल्या अनुवाद भाषांसाठी. |
| `-r`, `--root-dir` | No | प्रोजेक्ट रूट. डिफॉल्ट सध्याच्या निर्देशिकेवर आहे. |
| `--changed-from` | No | बदललेल्या स्रोत फाइल्सवर पुनरावलोकन मर्यादित करण्यासाठी वापरले जाणारे Git रेफ. |
| `--format` | No | आउटपुट फॉरमॅट: `text` किंवा `github`. डिफॉल्ट `text`. |

`co-op-review` सध्या गहाळ अनुवादित फाइल्स, गहाळ किंवा जुनी अनुवाद मेटाडेटा, Markdown फ्रंटमॅटर आणि कोड फेन्सची अखंडता, अमान्य अनुवादित नोटबुक JSON, आणि गहाळ स्थानिक Markdown किंवा इमेज लिंक लक्ष्यांसाठी तपासणी करते. गहाळ लिंक सामान्यतः चेतावणी असतात; संरचनात्मक आणि ताजेपणाशी संबंधित समस्या कमांड अयशस्वी करतात.

## co-op-translator-mcp

एजंट, एडिटर्स, आणि MCP-अनुकूल क्लायंटसाठी Co-op Translator MCP सर्व्ह्हर चालवा.

```bash
co-op-translator-mcp
```

Default ट्रान्सपोर्ट `stdio` आहे. क्लायंट कॉन्फिगरेशन, टूल्स, रिसोर्सेस, आणि सुरक्षा नोंदींसाठी [MCP Server](mcp.md) मार्गदर्शक पहा.

### पर्याय

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP ट्रान्सपोर्ट: `stdio`, `streamable-http`, किंवा `sse`. डिफॉल्ट `stdio`. |

## migrate-links

अनुवादित Markdown फाइल्स पुन्हा प्रक्रिया करा आणि नोटबुक लिंक अद्ययावत करा ज्यामुळे उपलब्ध असलेल्या अनुवादित नोटबुककडे त्या निर्देशित करतील.

```bash
migrate-links -l "ko ja"
```

### सामान्य उदाहरणे

लिंक अपडेट्सचे प्रीव्ह्यू करा:

```bash
migrate-links -l "ko" --dry-run
```

कोणत्याही पुष्टीशिवाय सर्व समर्थित भाषांमध्ये प्रक्रिया करा:

```bash
migrate-links -l "all" -y
```

केवळ अनुवादित नोटबुक्स असतील तेव्हाच लिंक री-राइट करा:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### पर्याय

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | स्पेस-वेगळे भाषा कोड, किंवा `"all"`. |
| `-r`, `--root-dir` | No | प्रोजेक्ट रूट. डिफॉल्ट सध्याच्या निर्देशिकेवर आहे. |
| `--image-dir` | No | रुटच्या सापेक्ष अनुवादित इमेज डिरेक्टरी. डिफॉल्ट `translated_images`. |
| `--dry-run` | No | फाइल्स ज्या बदलल्या असत्या त्या दाखवा परंतु अपडेट्स न लिहिता. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | अनुवादित नोटबुक नसल्यास मूळ नोटबुक लिंकचा वापर करा. डिफॉल्टने सक्षम आहे. |
| `-d`, `--debug` | No | डिबग लॉगिंग सक्षम करा. |
| `-s`, `--save-logs` | No | `<root-dir>/logs/` अंतर्गत DEBUG-स्तरीय लॉग जतन करा. |
| `-y`, `--yes` | No | सर्व भाषांवर प्रक्रिया करताना प्रॉम्प्ट्स ऑटो-कन्फर्म करा. |

## Environment

सर्व कमांड्ससाठी एक कॉन्फिगर केलेला LLM प्रदाता आवश्यक आहे:

```bash
# एझ्युअर ओपनएआय
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# किंवा ओपनएआय
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

इमेज अनुवादासाठी अतिरिक्तपणे Azure AI Vision आवश्यक आहे:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Output layout

टेक्स्ट अनुवाद पुढील अंतर्गत लिहिले जातात:

```text
translations/<language-code>/<original-path>
```

अनुवादित इमेज आउटपुट पुढील अंतर्गत लिहिले जाते:

```text
translated_images/<language-code>/<original-path>
```

उदाहरणार्थ, `README.md` आणि `docs/setup.md` चे कोरियनमध्ये अनुवाद केल्यास:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## कॉपी-पेस्ट CLI उदाहरणे

Markdown तीन भाषांमध्ये अनुवाद करा:

```bash
translate -l "ko ja fr" -md
```

फक्त नोटबुक्स अनुवाद करा:

```bash
translate -l "zh-CN" -nb
```

फक्त इमेजेस अनुवाद करा:

```bash
translate -l "pt-BR" -img
```

Markdown अनुवादाचे प्रीव्ह्यू फाइल्स लिहित न देता:

```bash
translate -l "de es" -md --dry-run
```

कमी-कॉनफिडन्स Markdown अनुवाद दुरुस्त करा:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

CI-फ्रेंडली Markdown अनुवाद चालवा:

```bash
translate -l "ko ja" -md -y -s
```

अनुवादित आउटपुट पुनरावलोकन करा:

```bash
co-op-review -l "ko ja"
```

लिंक माइग्रेशनचे प्रीव्ह्यू करा:

```bash
migrate-links -l "ko" --dry-run
```