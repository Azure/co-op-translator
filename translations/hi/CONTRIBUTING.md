<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-05-06T17:22:06+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hi"
}
-->
# Co-op Translator में योगदान देना

यह प्रोजेक्ट योगदान और सुझावों का स्वागत करता है। अधिकांश योगदानों के लिए आपको एक Contributor License Agreement (CLA) से सहमति देनी होती है, जिसमें आप यह घोषणा करते हैं कि आपके पास अपने योगदान का उपयोग करने के अधिकार हैं। विवरण के लिए, https://cla.opensource.microsoft.com देखें।

जब आप एक पुल रिक्वेस्ट सबमिट करते हैं, तो CLA बॉट स्वचालित रूप से निर्धारित करेगा कि आपको CLA प्रदान करना है या नहीं और PR को उपयुक्त रूप से चिह्नित करेगा (जैसे, स्थिति जांच, टिप्पणी)। बस बॉट द्वारा दिए गए निर्देशों का पालन करें। आपको यह केवल एक बार सभी रिपोज़ में करना होगा जो हमारे CLA का उपयोग करते हैं।

## विकास पर्यावरण सेटअप

इस प्रोजेक्ट के विकास पर्यावरण को सेटअप करने के लिए, हम Poetry का उपयोग करने की सलाह देते हैं जो निर्भरताओं को प्रबंधित करता है। हम परियोजना निर्भरताओं को प्रबंधित करने के लिए `pyproject.toml` का उपयोग करते हैं, इसलिए निर्भरताएँ स्थापित करने के लिए आपको Poetry का उपयोग करना चाहिए।

### वर्चुअल एनवायरनमेंट बनाना

#### pip का उपयोग करते हुए

```bash
python -m venv .venv
```

#### Poetry का उपयोग करते हुए

```bash
poetry init
```

### वर्चुअल एनवायरनमेंट सक्रिय करना

#### pip और Poetry दोनों के लिए

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry का उपयोग करते हुए

```bash
poetry shell
```

### पैकेज और आवश्यक पैकेज स्थापित करना

#### Poetry का उपयोग करते हुए (pyproject.toml से)

```bash
poetry install
```

### मैनुअल परीक्षण

PR सबमिट करने से पहले, वास्तविक डाक्यूमेंटेशन के साथ अनुवाद कार्यक्षमता का परीक्षण करना महत्वपूर्ण है:

1. रूट डायरेक्टरी में एक टेस्ट डायरेक्टरी बनाएं:
    ```bash
    mkdir test_docs
    ```

2. कुछ मार्कडाउन डाक्यूमेंटेशन और इमेजेज़ जिन्हें आप अनुवाद करना चाहते हैं, उन्हें टेस्ट डायरेक्टरी में कॉपी करें। उदाहरण के लिए:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. पैकेज को लोकली इंस्टॉल करें:
    ```bash
    pip install -e .
    ```

4. अपने टेस्ट डॉक्यूमेंट्स पर Co-op Translator चलाएं:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` फाइल में अनुवादित फाइलों की जांच करें।
1. पर्यावरण वेरिएबल्स को निर्देशानुसार भरें।

> [!TIP]
>
> ### अतिरिक्त विकास पर्यावरण विकल्प
>
> प्रोजेक्ट को लोकली चलाने के अलावा, आप GitHub Codespaces या VS Code Dev Containers का उपयोग करके वैकल्पिक विकास पर्यावरण सेटअप कर सकते हैं।
>
> #### GitHub Codespaces
>
> आप GitHub Codespaces का उपयोग करके इस सैंपल को वर्चुअली चला सकते हैं और इसके लिए कोई अतिरिक्त सेटिंग या सेटअप आवश्यक नहीं है।
>
> यह बटन आपके ब्राउज़र में वेब-आधारित VS Code इंस्टेंस खोलेगा:
>
> 1. टेम्पलेट खोलें (यह कुछ मिनट ले सकता है):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### VS Code Dev Containers का उपयोग करके लोकली चलाना
>
> ⚠️ यह विकल्प तभी काम करेगा जब आपके Docker Desktop को कम से कम 16 GB RAM आवंटित हो। यदि आपके पास 16 GB से कम RAM है, तो आप [GitHub Codespaces विकल्प](../..) या [लोकली सेटअप](../..) आजमा सकते हैं।
>
> एक संबंधित विकल्प VS Code Dev Containers है, जो प्रोजेक्ट को आपके लोकल VS Code में [Dev Containers एक्सटेंशन](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) का उपयोग करके खोलेगा:
>
> 1. Docker Desktop शुरू करें (यदि पहले से इंस्टॉल नहीं है तो इंस्टॉल करें)
> 2. प्रोजेक्ट खोलें:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### कोड स्टाइल

हम परियोजना में एक समान कोड स्टाइल बनाए रखने के लिए Python कोड फॉर्मैटर के रूप में [Black](https://github.com/psf/black) का उपयोग करते हैं। Black एक सख्त कोड फॉर्मैटर है जो Python कोड को स्वचालित रूप से Black कोड स्टाइल के अनुरूप पुनः स्वरूपित करता है।

#### कॉन्फ़िगरेशन

Black कॉन्फ़िगरेशन हमारे `pyproject.toml` में निर्दिष्ट है:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black स्थापित करना

आप Black को Poetry (सिफारिश की गई) या pip के जरिए इंस्टॉल कर सकते हैं:

##### Poetry का उपयोग करते हुए

डेवलपमेंट एनवायरनमेंट सेटअप करते समय Black स्वचालित रूप से इंस्टॉल हो जाता है:
```bash
poetry install
```

##### pip का उपयोग करते हुए

यदि आप pip का उपयोग कर रहे हैं, तो आप सीधे Black इंस्टॉल कर सकते हैं:
```bash
pip install black
```

#### Black का उपयोग करना

##### Poetry के साथ

1. प्रोजेक्ट में सभी Python फाइलों को फॉर्मेट करें:
    ```bash
    poetry run black .
    ```

2. किसी विशेष फाइल या डायरेक्टरी को फॉर्मेट करें:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip के साथ

1. प्रोजेक्ट में सभी Python फाइलों को फॉर्मेट करें:
    ```bash
    black .
    ```

2. किसी विशेष फाइल या डायरेक्टरी को फॉर्मेट करें:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> हम सुझाव देते हैं कि आप अपने एडिटर को इस तरह सेट करें कि Black के साथ कोड सेव करते समय स्वचालित रूप से फॉर्मेट हो जाए। अधिकांश आधुनिक एडिटर एक्सटेंशन या प्लगइन्स के माध्यम से इसका समर्थन करते हैं।

## Co-op Translator चलाना

अपने पर्यावरण में Poetry का उपयोग करके Co-op Translator चलाने के लिए, निम्न चरणों का पालन करें:

1. उस डायरेक्टरी में जाएं जहाँ आप अनुवाद परीक्षण करना चाहते हैं या परीक्षण के लिए एक अस्थायी फोल्डर बनाएं।

2. निम्न कमांड चलाएं। `-l ko` with the language code you wish to translate into. The `-d` फ़्लैग डिबग मोड को दर्शाता है।

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> कमांड चलाने से पहले सुनिश्चित करें कि आपका Poetry पर्यावरण सक्रिय है (poetry shell)।

## मेंटेनर्स

### कमिट संदेश और मर्ज रणनीति

हमारे प्रोजेक्ट के कमिट इतिहास में एकरूपता और स्पष्टता सुनिश्चित करने के लिए, हम **Squash and Merge** रणनीति के तहत **अंतिम कमिट संदेश** के लिए एक विशिष्ट कमिट संदेश प्रारूप का पालन करते हैं।

जब कोई पुल रिक्वेस्ट (PR) मर्ज होता है, तो व्यक्तिगत कमिट्स को एकल कमिट में स्क्वैश किया जाएगा। अंतिम कमिट संदेश को नीचे दिए गए प्रारूप के अनुसार होना चाहिए ताकि इतिहास साफ और एकरूप रहे।

#### कमिट संदेश प्रारूप (squash and merge के लिए)

हम कमिट संदेशों के लिए निम्नलिखित प्रारूप का उपयोग करते हैं:

```bash
<type>: <description> (#<PR number>)
```

- **type**: कमिट की श्रेणी निर्दिष्ट करता है। हम निम्नलिखित प्रकारों का उपयोग करते हैं:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `fix typo`
- `update README`
- `adjust formatting`

They should be squashed into:
`Docs: Improve documentation clarity and formatting (#65)`

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।