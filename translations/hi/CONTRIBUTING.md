<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T02:42:38+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hi"
}
-->
# Co-op Translator में योगदान देना

यह प्रोजेक्ट योगदान और सुझावों का स्वागत करता है। अधिकांश योगदानों के लिए आपको एक Contributor License Agreement (CLA) से सहमत होना होता है, जिसमें आप यह घोषणा करते हैं कि आपके पास योगदान देने का अधिकार है और आप हमें अपने योगदान का उपयोग करने का अधिकार देते हैं। अधिक जानकारी के लिए https://cla.opensource.microsoft.com पर जाएं।

जब आप कोई pull request सबमिट करते हैं, तो एक CLA bot स्वचालित रूप से यह निर्धारित करेगा कि आपको CLA प्रदान करने की आवश्यकता है या नहीं और PR को उपयुक्त रूप से सजाएगा (जैसे, status check, comment)। बस bot द्वारा दिए गए निर्देशों का पालन करें। आपको यह प्रक्रिया सभी repos में केवल एक बार करनी होगी जो हमारे CLA का उपयोग करते हैं।

## डेवलपमेंट एनवायरनमेंट सेटअप

इस प्रोजेक्ट के लिए डेवलपमेंट एनवायरनमेंट सेटअप करने के लिए हम dependencies मैनेज करने के लिए Poetry का उपयोग करने की सलाह देते हैं। हम प्रोजेक्ट dependencies को मैनेज करने के लिए `pyproject.toml` का उपयोग करते हैं, इसलिए dependencies इंस्टॉल करने के लिए आपको Poetry का उपयोग करना चाहिए।

### वर्चुअल एनवायरनमेंट बनाएं

#### pip का उपयोग करके

```bash
python -m venv .venv
```

#### Poetry का उपयोग करके

```bash
poetry init
```

### वर्चुअल एनवायरनमेंट एक्टिवेट करें

#### pip और Poetry दोनों के लिए

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry का उपयोग करके

```bash
poetry shell
```

### पैकेज और आवश्यक पैकेज इंस्टॉल करना

#### Poetry का उपयोग करके (pyproject.toml से)

```bash
poetry install
```

### मैन्युअल टेस्टिंग

PR सबमिट करने से पहले, ट्रांसलेशन फंक्शनैलिटी को असली डॉक्युमेंटेशन के साथ टेस्ट करना जरूरी है:

1. रूट डायरेक्टरी में एक टेस्ट डायरेक्टरी बनाएं:
    ```bash
    mkdir test_docs
    ```

2. कुछ markdown डॉक्युमेंटेशन और इमेजेज, जिन्हें आप ट्रांसलेट करना चाहते हैं, टेस्ट डायरेक्टरी में कॉपी करें। उदाहरण के लिए:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. पैकेज को लोकली इंस्टॉल करें:
    ```bash
    pip install -e .
    ```

4. अपने टेस्ट डॉक्युमेंट्स पर Co-op Translator चलाएं:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` और `test_docs/translated_images` में ट्रांसलेटेड फाइल्स चेक करें और सुनिश्चित करें:
   - ट्रांसलेशन की गुणवत्ता
   - मेटाडेटा कमेंट्स सही हैं
   - ओरिजिनल markdown स्ट्रक्चर बना हुआ है
   - लिंक और इमेजेज सही काम कर रहे हैं

यह मैन्युअल टेस्टिंग यह सुनिश्चित करने में मदद करती है कि आपके बदलाव असली परिस्थितियों में अच्छे से काम करते हैं।

### एनवायरनमेंट वेरिएबल्स

1. रूट डायरेक्टरी में `.env.template` फाइल को कॉपी करके `.env` फाइल बनाएं।
1. दिए गए निर्देशों के अनुसार एनवायरनमेंट वेरिएबल्स भरें।

> ### अतिरिक्त डेवलपमेंट एनवायरनमेंट विकल्प
>
> प्रोजेक्ट को लोकली चलाने के अलावा, आप GitHub Codespaces या VS Code Dev Containers का भी उपयोग कर सकते हैं।
>
> #### GitHub Codespaces
>
> आप इस सैंपल को virtually GitHub Codespaces का उपयोग करके चला सकते हैं, इसमें कोई अतिरिक्त सेटिंग या सेटअप की आवश्यकता नहीं है।
>
> बटन आपके ब्राउज़र में वेब-बेस्ड VS Code इंस्टेंस खोलेगा:
>
> 1. टेम्पलेट खोलें (इसमें कुछ मिनट लग सकते हैं):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### लोकली VS Code Dev Containers का उपयोग करके चलाना
>
> ⚠️ यह विकल्प तभी काम करेगा जब आपके Docker Desktop को कम से कम 16 GB RAM अलॉट किया गया हो। अगर आपके पास 16 GB से कम RAM है, तो आप [GitHub Codespaces विकल्प](../..) या [लोकली सेटअप](../..) आज़मा सकते हैं।
>
> एक संबंधित विकल्प VS Code Dev Containers है, जो प्रोजेक्ट को आपके लोकल VS Code में [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) के साथ खोलेगा:
>
> 1. Docker Desktop शुरू करें (अगर इंस्टॉल नहीं है तो इंस्टॉल करें)
> 2. प्रोजेक्ट खोलें:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### कोड स्टाइल

हम प्रोजेक्ट में कोड स्टाइल को एक जैसा बनाए रखने के लिए [Black](https://github.com/psf/black) Python कोड फॉर्मेटर का उपयोग करते हैं। Black एक uncompromising कोड फॉर्मेटर है जो Python कोड को Black कोड स्टाइल के अनुसार ऑटोमेटिकली रीफॉर्मेट करता है।

#### कॉन्फ़िगरेशन

Black की कॉन्फ़िगरेशन हमारे `pyproject.toml` में दी गई है:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black इंस्टॉल करना

आप Black को Poetry (अनुशंसित) या pip से इंस्टॉल कर सकते हैं:

##### Poetry का उपयोग करके

Black ऑटोमेटिकली इंस्टॉल हो जाता है जब आप डेवलपमेंट एनवायरनमेंट सेटअप करते हैं:
```bash
poetry install
```

##### pip का उपयोग करके

अगर आप pip का उपयोग कर रहे हैं, तो आप Black को डायरेक्टली इंस्टॉल कर सकते हैं:
```bash
pip install black
```

#### Black का उपयोग करना

##### Poetry के साथ

1. प्रोजेक्ट की सभी Python फाइल्स को फॉर्मेट करें:
    ```bash
    poetry run black .
    ```

2. किसी खास फाइल या डायरेक्टरी को फॉर्मेट करें:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip के साथ

1. प्रोजेक्ट की सभी Python फाइल्स को फॉर्मेट करें:
    ```bash
    black .
    ```

2. किसी खास फाइल या डायरेक्टरी को फॉर्मेट करें:
    ```bash
    black path/to/file_or_directory
    ```

> हम सलाह देते हैं कि आप अपने एडिटर को Black के साथ ऑटोमेटिक फॉर्मेटिंग के लिए सेट करें। ज्यादातर मॉडर्न एडिटर्स में यह एक्सटेंशन या प्लगइन के जरिए संभव है।

## Co-op Translator चलाना

अपने एनवायरनमेंट में Poetry का उपयोग करके Co-op Translator चलाने के लिए ये स्टेप्स फॉलो करें:

1. उस डायरेक्टरी में जाएं जहां आप ट्रांसलेशन टेस्ट करना चाहते हैं या टेस्टिंग के लिए एक टेम्पररी फोल्डर बनाएं।

2. नीचे दिया गया कमांड चलाएं। `-l ko` को उस भाषा कोड से बदलें जिसमें आप ट्रांसलेट करना चाहते हैं। `-d` फ्लैग debug मोड के लिए है।

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> सुनिश्चित करें कि आपका Poetry एनवायरनमेंट एक्टिवेटेड है (poetry shell) इससे पहले कि आप कमांड चलाएं।

## नई भाषा का योगदान दें

हम नई भाषाओं के लिए सपोर्ट जोड़ने वाले योगदानों का स्वागत करते हैं। PR खोलने से पहले, कृपया नीचे दिए गए स्टेप्स पूरे करें ताकि रिव्यू आसानी से हो सके।

1. भाषा को font mapping में जोड़ें
   - `src/co_op_translator/fonts/font_language_mappings.yml` एडिट करें
   - एक एंट्री जोड़ें जिसमें:
     - `code`: ISO-जैसा भाषा कोड (जैसे, `vi`)
     - `name`: इंसान के लिए समझने योग्य नाम
     - `font`: `src/co_op_translator/fonts/` में उपलब्ध कोई font जो उस स्क्रिप्ट को सपोर्ट करता हो
     - `rtl`: अगर right-to-left है तो `true`, अन्यथा `false`

2. आवश्यक font फाइल्स शामिल करें (अगर जरूरत हो)
   - अगर नया font चाहिए, तो ओपन सोर्स डिस्ट्रीब्यूशन के लिए लाइसेंस कम्पैटिबिलिटी जांचें
   - font फाइल को `src/co_op_translator/fonts/` में जोड़ें

3. लोकल वेरिफिकेशन
   - छोटे सैंपल (Markdown, images, और notebooks) के लिए ट्रांसलेशन चलाएं
   - आउटपुट सही रेंडर हो रहा है, font और RTL लेआउट (अगर लागू हो) सही है, यह जांचें

4. डॉक्युमेंटेशन अपडेट करें
   - सुनिश्चित करें कि भाषा `getting_started/supported-languages.md` में दिख रही है
   - `README_languages_template.md` में कोई बदलाव जरूरी नहीं है; यह सपोर्टेड लिस्ट से जेनरेट होती है

5. PR खोलें
   - जोड़ी गई भाषा और font/licensing से संबंधित बातें बताएं
   - संभव हो तो रेंडर किए गए आउटपुट के स्क्रीनशॉट अटैच करें

YAML एंट्री का उदाहरण:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## मेंटेनर्स

### कमिट मैसेज और मर्ज स्ट्रैटेजी

हमारे प्रोजेक्ट के कमिट हिस्ट्री में एकरूपता और स्पष्टता बनाए रखने के लिए हम **Squash and Merge** स्ट्रैटेजी के तहत अंतिम कमिट मैसेज के लिए एक खास फॉर्मेट का पालन करते हैं।

जब कोई pull request (PR) मर्ज किया जाता है, तो व्यक्तिगत कमिट्स एक ही कमिट में squash हो जाते हैं। अंतिम कमिट मैसेज नीचे दिए गए फॉर्मेट का होना चाहिए ताकि हिस्ट्री साफ और एक जैसी रहे।

#### कमिट मैसेज फॉर्मेट (squash and merge के लिए)

हम कमिट मैसेज के लिए यह फॉर्मेट उपयोग करते हैं:

```bash
<type>: <description> (#<PR number>)
```

- **type**: कमिट की श्रेणी बताता है। हम ये types उपयोग करते हैं:
  - `Docs`: डॉक्युमेंटेशन अपडेट्स के लिए।
  - `Build`: बिल्ड सिस्टम या dependencies से संबंधित बदलावों के लिए, जैसे configuration files, CI workflows, या Dockerfile।
  - `Core`: प्रोजेक्ट की मुख्य फंक्शनैलिटी या फीचर्स में बदलाव के लिए, खासकर `src/co_op_translator/core` डायरेक्टरी में।

- **description**: बदलाव का संक्षिप्त सारांश।
- **PR number**: उस कमिट से संबंधित pull request का नंबर।

**उदाहरण**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> अभी, **`Docs`**, **`Core`**, और **`Build`** prefixes ऑटोमेटिकली PR titles में जोड़ दिए जाते हैं, modified source code पर लगाए गए labels के आधार पर। जब तक सही label लगा है, आपको आमतौर पर PR title मैन्युअली अपडेट करने की जरूरत नहीं होती। बस यह जांच लें कि सब सही है और prefix सही तरीके से जेनरेट हुआ है।

#### मर्ज स्ट्रैटेजी

हम pull requests के लिए **Squash and Merge** को डिफॉल्ट स्ट्रैटेजी के रूप में उपयोग करते हैं। यह स्ट्रैटेजी सुनिश्चित करती है कि कमिट मैसेज हमारे फॉर्मेट का पालन करें, भले ही व्यक्तिगत कमिट्स न करें।

**कारण**:

- साफ, linear प्रोजेक्ट हिस्ट्री।
- कमिट मैसेज में एकरूपता।
- छोटे-मोटे कमिट्स (जैसे, "fix typo") से बचाव।

मर्ज करते समय, सुनिश्चित करें कि अंतिम कमिट मैसेज ऊपर बताए गए फॉर्मेट का पालन करता है।

**Squash and Merge का उदाहरण**
अगर किसी PR में ये कमिट्स हैं:

- `fix typo`
- `update README`
- `adjust formatting`

तो इन्हें squash करके बनाना चाहिए:
`Docs: Improve documentation clarity and formatting (#65)`

---

**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद एआई अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।