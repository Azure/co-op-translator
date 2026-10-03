# CLI संदर्भ

Co-op Translator हे खालील कमांड-लाइन एंट्री पॉइंट स्थापित करते:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

The `translate`, `evaluate`, `migrate-links`, आणि `co-op-review` कमांड `co_op_translator.__main__` मधून डिस्पॅच होतात, जे स्क्रिप्टच्या नावावर आधारित कमांड अंमलबजावणी निवडते. MCP सर्व्हर थेट `co_op_translator.mcp.server` वापरते.

CLI, Python API, आणि MCP यापैकी कोणता वापरायचा हे ठरवण्याचा विचार करत असाल तर [आपला कार्यप्रवाह निवडा](workflows.md) पासून सुरू करा.

## कन्सोल आउटपुट

इंटरेक्टिव्ह टर्मिनल्स कमांड हेडर, प्रगती आणि सारांशांसाठी Rich फॉरमॅटिंग वापरतात. CI आणि नॉन-इंटरेक्टिव्ह आउटपुट आपोआप साध्या मजकूराकडे परततात.

साधे आउटपुट मजबूर करण्यासाठी `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` सेट करा, किंवा Rich आउटपुट मजबूर करण्यासाठी `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` सेट करा. थेट प्रगती पट्टे लपवून सारांश ठेवण्यासाठी `CO_OP_TRANSLATOR_NO_PROGRESS=1` सेट करा.

इतर सिस्टमला मशीन-रीडेबल प्रगती हवी असल्यास `translate --json-events progress.ndjson` वापरा
मशीन-रीडेबल प्रगतीसाठी. CLI मानवी-उपयोगी आउटपुट दाखवत राहते, तर
NDJSON फाइलला versioned `co-op.translation.event.v1` इव्हेंट्स मिळतात ज्यात
स्थिर फील्ड्स जसे की `type`, `stage_key`, `completed`, `total`, आणि
`current_path`.

## प्रथम-वेळेचा CLI प्रवाह

जर आपण टर्मिनलमधून Co-op Translator वापरत असाल तर येथे सुरू करा:

1. [कॉन्फिगरेशन](configuration.md) मध्ये वर्णन केल्याप्रमाणे एक LLM प्रदाता कॉन्फिगर करा.
2. आपण अनुवादित करू इच्छित सामग्री प्रकार निवडा.
3. सुरुवातीला एक लक्षित कमांड चालवा, उदा. फक्त Markdown अनुवाद.
4. मोठ्या रेपॉजिटरी बदलांपूर्वी `--dry-run` वापरा.
5. अनुवादानंतर संरचना आणि ताजेपणा तपासण्यासाठी `co-op-review` वापरा.

| उद्दिष्ट | सुरू करण्यासाठी कमांड |
| --- | --- |
| Markdown दस्तऐवजांचे अनुवाद करा | `translate -l "ko" -md` |
| नोटबुक अनुवाद करा | `translate -l "ko" -nb` |
| प्रतिमेतील मजकूर अनुवाद करा | `translate -l "ko" -img` |
| फायली न लिहिता काम पूर्वावलोकन करा | `translate -l "ko" -md --dry-run` |
| विद्यमान अनुवाद पुनरावलोकन करा | `co-op-review -l "ko"` |
| नोटबुक आणि Markdown लिंक्स अद्यतनित करा | `migrate-links -l "ko" --dry-run` |
| उपकरणे MCP क्लायंटसाठी उपलब्ध करा | CLI कमांड थेट चालवण्याऐवजी [MCP सर्व्हर](mcp.md) कॉन्फिगर करा. |

## translate

Markdown फाइल्स, नोटबुक आणि प्रतिमेतील मजकूर एका किंवा अधिक लक्ष्य भाषांमध्ये अनुवादित करा.

```bash
translate -l "ko ja fr"
```

### सामान्य उदाहरणे

केवळ Markdown अनुवाद:

```bash
translate -l "de" -md
```

केवळ नोटबुक अनुवाद:

```bash
translate -l "zh-CN" -nb
```

Markdown आणि प्रतिमा अनुवाद:

```bash
translate -l "pt-BR" -md -img
```

आधीच्या अनुवादांना हटवून त्यांना पुन्हा तयार करून अद्यतनित करा:

```bash
translate -l "ko" -u
```

इंटरएक्टिव्ह प्रॉम्प्टशिवाय चालवा:

```bash
translate -l "ko ja" -md -y
```

लॉग जतन करा:

```bash
translate -l "ko" -s
```

संरचित प्रगती इव्हेंट लिहा:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### पर्याय

| पर्याय | आवश्यक | वर्णन |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | स्पेस-वेगळे भाषा कोड, उदाहरणार्थ "es fr de", किंवा "all". |
| `-r`, `--root-dir` | No | प्रोजेक्ट रूट. डीफॉल्ट सध्याची निर्देशिका. |
| `-u`, `--update` | No | निवडलेल्या भाषांसाठी विद्यमान अनुवाद हटवून पुन्हा तयार करा. |
| `-img`, `--images` | No | फक्त प्रतिमा फाइल्स अनुवाद करा. |
| `-md`, `--markdown` | No | फक्त Markdown फाइल्स अनुवाद करा. |
| `-nb`, `--notebook` | No | फक्त Jupyter नोटबुक फाइल्स अनुवाद करा. |
| `-d`, `--debug` | No | कन्सोलमध्ये डीबग लॉगिंग सक्षम करा. |
| `-s`, `--save-logs` | No | DEBUG-स्तराचे लॉग `<root-dir>/logs/` खाली जतन करा. |
| `--json-events` | No | अनुवाद प्रगतीसाठी मशीन-पठनीय इव्हेंट NDJSON म्हणून लिहा. |
| `-x`, `--fix` | No | मागील मूल्यमापन निकालांवर आधारित कमी-विश्वास Markdown फाइल्स पुन्हा-अनुवाद करा. |
| `-c`, `--min-confidence` | No | `--fix` साठी आत्मविश्वास मर्यादा. डीफॉल्ट `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | मशीन अनुवाद अस्वीकरणे (disclaimers) जोडा किंवा लोप करा. CLI मध्ये डीफॉल्टने सक्षम आहे. |
| `-f`, `--fast` | No | Deprecated फास्ट इमेज मोड. |
| `-y`, `--yes` | No | प्रॉम्प्ट आपोआप पुष्टी करा, CI मध्ये उपयोगी. |
| `--repo-url` | No | README भाषांच्या टेबलच्या sparse-checkout सल्ल्यामध्ये वापरण्यात येणारा रेपॉजिटरी URL. |
| `--migrate-language-folders` | No | जुन्या उपनाम फोल्डरचे नाव बदलून canonical BCP 47 फोल्डर्समध्ये बदला, जसे `cn` किंवा `tw`. |
| `--dry-run` | No | फायली न लिहिता भाषा फोल्डर माइग्रेशन आणि अनुवाद अंदाजाचे पूर्वावलोकन दर्शवा. |

जर कोणताही type flag प्रदान केला गेला नाही, `translate` Markdown, नोटबुक्स आणि प्रतिमा प्रक्रिया करते. प्रतिमा अनुवादासाठी Azure AI Vision कॉन्फिगरेशन आवश्यक आहे.

## evaluate

एखाद्या भाषेसाठी अनुवाद केलेल्या Markdown ची गुणवत्ता मूल्यमापन करा.

!!! warning "प्रायोगिक"
    `evaluate` प्रायोगिक आहे. हे नियम-आधारित आणि LLM-आधारित गुणवत्ता तपासण्या वापरू शकते, अनुवाद मेटाडेटामध्ये मूल्यांकनाचे परिणाम लिहिते, आणि त्याचे स्कोअरिंग मॉडेल आणि मेटाडेटाच्या वर्तनात बदल होऊ शकतात.

```bash
evaluate -l "ko"
```

### सामान्य उदाहरणे

कठोर कमी-विश्वास मर्यादा वापरा:

```bash
evaluate -l "es" -c 0.8
```

फक्त नियम-आधारित तपास चालवा:

```bash
evaluate -l "fr" -f
```

फक्त LLM-आधारित तपास चालवा:

```bash
evaluate -l "ja" -D
```

### पर्याय

| पर्याय | आवश्यक | वर्णन |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | मूल्यमापन करण्यासाठी एकल भाषा कोड. उपनाम कोड सामान्यीकृत केले जातात. |
| `-r`, `--root-dir` | No | प्रोजेक्ट रूट. डीफॉल्ट सध्याची निर्देशिका. |
| `-c`, `--min-confidence` | No | कमी-विश्वास अनुवादांची यादी करताना वापरली जाणारी मर्यादा. डीफॉल्ट `0.7`. |
| `-d`, `--debug` | No | डीबग लॉगिंग सक्षम करा. |
| `-s`, `--save-logs` | No | DEBUG-स्तराचे लॉग `<root-dir>/logs/` खाली जतन करा. |
| `-f`, `--fast` | No | फक्त नियम-आधारित मूल्यमापन. |
| `-D`, `--deep` | No | फक्त LLM-आधारित मूल्यमापन. |

डीफॉल्टनुसार, `evaluate` हे नियम-आधारित आणि LLM-आधारित दोन्ही मूल्यमापन वापरते. निकाल अनुवाद मेटाडेटामध्ये लिहिले जातात आणि कन्सोलमध्ये सारांशित केले जातात.

## co-op-review

API क्रेडेन्शियलशिवाय निर्धारक अनुवाद देखभाल तपासण्या चालवा.

!!! note "बीटा"
    `co-op-review` हा बीटा ठराविक पुनरावलोकन आदेश आहे. हा मॉडेल पुरवठादारांना कॉल करत नाही किंवा फायली लिहीत नाही, परंतु त्याच्या तपासण्या आणि समस्या-आउटपुट स्कीम बदलू शकतात.

```bash
co-op-review -l "ko"
```

### सामान्य उदाहरणे

सध्याच्या निर्देशिकेतून कोरियन आणि जपानी अनुवाद पुनरावलोकन करा:

```bash
co-op-review -l "ko ja"
```

एखाद्या विशिष्ट प्रोजेक्ट रूटचे पुनरावलोकन करा:

```bash
co-op-review -l "fr" -r ./my-course
```

README-केवळ अनुवादनानंतर फक्त README चे पुनरावलोकन करा:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` इतर दस्तऐवज आणि नेस्टेड READMEs अनदेखा करते. हे अयशस्वी होते जर रूट
`README.md` गहाळ असेल. `--changed-from` सोबत वापरल्यास, ते फक्त README पुनरावलोकन करते
जेव्हा त्या स्रोत फाईलमध्ये बदल झाले असतील.
README-केवळ अनुवाद स्रोत README अपरिवर्तित ठेवते,

बेस रेफ विरुद्ध बदल केलेल्या फक्त स्रोत फाइल्सचे पुनरावलोकन करा:

```bash
co-op-review -l "ko" --changed-from origin/main
```

CI सारांशांसाठी GitHub-फ्लेवर्ड Markdown आउटपुट छापा:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### पर्याय

| पर्याय | आवश्यक | वर्णन |
| --- | --- | --- |
| `-l`, `--language-code` | No | पुनरावलोकन करण्यासाठी भाषा कोड. अनेक वेळा पास करू शकता किंवा स्पेसने विभाजित मूल्य म्हणून देऊ शकता. डीफॉल्ट सर्व शोधलेल्या अनुवाद भाषांसाठी. |
| `-r`, `--root-dir` | No | प्रोजेक्ट रूट. डीफॉल्ट सध्याची निर्देशिका. |
| `--changed-from` | No | Git ref जो बदललेल्या स्रोत फाइल्सपुरते पुनरावलोकन मर्यादित करण्यासाठी वापरला जातो. |
| `--readme-only` | No | फक्त रूट `README.md` अनुवादाचे पुनरावलोकन करा. |
| `--format` | No | आउटपुट फॉरमॅट: `text` किंवा `github`. डीफॉल्ट `text`. |

`co-op-review` सध्या गहाळ अनुवादित फाइल्स, गहाळ किंवा कालबाह्य अनुवाद मेटाडेटा, Markdown फ्रंटमॅटर आणि कोड फेन्सची अखंडता, अमान्य अनुवादित नोटबुक JSON, आणि गहाळ लोकल Markdown किंवा प्रतिमा लिंक लक्ष्ये तपासते. गहाळ लिंक्स पूर्वनिर्धारितपणे चेतावण्या असतात; संरचनात्मक आणि ताजेपणाच्या समस्या कमांड अयशस्वी करतात.

## co-op-translator-mcp

एजंट्स, एडिटर्स आणि MCP-योग्य क्लायंटसाठी Co-op Translator MCP सर्व्हर चालवा.

```bash
co-op-translator-mcp
```

डीफॉल्ट ट्रान्सपोर्ट `stdio` आहे. क्लायंट कॉन्फिगरेशन, साधने, संसाधने आणि सुरक्षा टीपांसाठी [MCP सर्व्हर](mcp.md) मार्गदर्शक पहा.

### पर्याय

| पर्याय | आवश्यक | वर्णन |
| --- | --- | --- |
| `--transport` | No | MCP ट्रान्सपोर्ट: `stdio`, `streamable-http`, किंवा `sse`. डीफॉल्ट `stdio`. |

## migrate-links

अनुवादित Markdown फाइल्स रीप्रोसेस करा आणि नोटबुक लिंक अद्यतनित करा जेणे करून उपलब्ध असतील तेव्हा त्या अनुवादित नोटबुककडे निर्देश करतील.

```bash
migrate-links -l "ko ja"
```

### सामान्य उदाहरणे

लिंक अद्यतने पूर्वावलोकन करा:

```bash
migrate-links -l "ko" --dry-run
```

पुष्टीशिवाय सर्व समर्थित भाषा प्रक्रिया करा:

```bash
migrate-links -l "all" -y
```

फक्त तेव्हा लिंक पुनर्लेखन करा जेव्हा अनुवादित नोटबुक अस्तित्वात असतील:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### पर्याय

| पर्याय | आवश्यक | वर्णन |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | स्पेस-वेगळे भाषा कोड, किंवा "all". |
| `-r`, `--root-dir` | No | प्रोजेक्ट रूट. डीफॉल्ट सध्याची निर्देशिका. |
| `--image-dir` | No | रूटच्या सापेक्ष अनुवादित प्रतिमा निर्देशिका. डीफॉल्ट `translated_images`. |
| `--dry-run` | No | अपडेट लिहिण्याशिवाय ज्या फायली बदलल्या जातील त्या दाखवा. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | अनुवादित नोटबुक अनुपस्थित असताना मूळ नोटबुक लिंक वापरा. डीफॉल्टनुसार सक्षम आहे. |
| `-d`, `--debug` | No | डीबग लॉगिंग सक्षम करा. |
| `-s`, `--save-logs` | No | DEBUG-स्तराचे लॉग `<root-dir>/logs/` खाली जतन करा. |
| `-y`, `--yes` | No | सर्व भाषा प्रक्रिया करताना प्रॉम्प्ट आपोआप पुष्टी करा. |

## पर्यावरण

जेव्हा एखाद्या कमांडला प्रदाता क्रेडेन्शियल्सची गरज असते, तेव्हा खालीलपैकी एखादा प्रदाता सेट कॉन्फिगर करा. `translate --dry-run` आणि `co-op-review` ना प्रदाता क्रेडेन्शियल्सची आवश्यकता नाही:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# किंवा OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# किंवा Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

प्रतिमा अनुवादासाठी अतिरिक्तपणे Azure AI Vision आवश्यक आहे:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## आउटपुट रचना

मजकूर अनुवाद खालील ठिकाणी लिहिले जातात:

```text
translations/<language-code>/<original-path>
```

अनुवादित प्रतिमा आउटपुट खाली लिहिले जाते:

```text
translated_images/<language-code>/<original-path>
```

उदाहरणार्थ, `README.md` आणि `docs/setup.md` चे कोरियनमध्ये अनुवाद केल्यास हे तयार होते:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## कॉपी-पेस्ट CLI उदाहरणे

Markdown तीन भाषांमध्ये अनुवाद करा:

```bash
translate -l "ko ja fr" -md
```

केवळ नोटबुक अनुवाद करा:

```bash
translate -l "zh-CN" -nb
```

केवळ प्रतिमा अनुवाद करा:

```bash
translate -l "pt-BR" -img
```

फायली न लिहिता Markdown अनुवादाचे पूर्वावलोकन करा:

```bash
translate -l "de es" -md --dry-run
```

कमी-विश्वास Markdown अनुवाद दुरुस्त करा:

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

लिंक माइग्रेशनचे पूर्वावलोकन करा:

```bash
migrate-links -l "ko" --dry-run
```