<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T02:52:05+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ne"
}
-->
# Co-op Translator मा योगदान गर्ने

यो परियोजनाले योगदान र सुझावहरूलाई स्वागत गर्छ। अधिकांश योगदानहरूका लागि तपाईंले Contributor License Agreement (CLA) मा सहमति जनाउनु पर्ने हुन्छ, जसले तपाईंले आफ्नो योगदान प्रयोग गर्न अधिकार दिनु भएको छ भन्ने घोषणा गर्छ। थप जानकारीका लागि https://cla.opensource.microsoft.com मा जानुहोस्।

जब तपाईंले pull request पठाउनुहुन्छ, CLA bot ले स्वचालित रूपमा तपाईंलाई CLA चाहिन्छ कि छैन भनेर निर्धारण गर्छ र PR मा उपयुक्त रूपमा जानकारी देखाउँछ (जस्तै, status check, comment)। बोटले दिएको निर्देशनहरू पालना गर्नुहोस्। तपाईंले एकपटक CLA गर्नुभयो भने, सबै CLA प्रयोग गर्ने repos मा फेरि गर्न आवश्यक पर्दैन।

## विकास वातावरण सेटअप

यो परियोजनाको विकास वातावरण सेटअप गर्नका लागि, निर्भरता व्यवस्थापनका लागि Poetry प्रयोग गर्न सिफारिस गरिन्छ। हामी `pyproject.toml` प्रयोग गर्छौं, त्यसैले निर्भरता स्थापना गर्न Poetry प्रयोग गर्नुहोस्।

### भर्चुअल वातावरण बनाउने

#### pip प्रयोग गरेर

```bash
python -m venv .venv
```

#### Poetry प्रयोग गरेर

```bash
poetry init
```

### भर्चुअल वातावरण सक्रिय गर्ने

#### pip र Poetry दुवैका लागि

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry प्रयोग गरेर

```bash
poetry shell
```

### प्याकेज र आवश्यक प्याकेजहरू स्थापना गर्ने

#### Poetry प्रयोग गरेर (pyproject.toml बाट)

```bash
poetry install
```

### म्यानुअल परीक्षण

PR पठाउनु अघि, वास्तविक डक्युमेन्टेसनमा अनुवाद कार्यक्षमता परीक्षण गर्नु महत्त्वपूर्ण छ:

1. root directory मा test directory बनाउनुहोस्:
    ```bash
    mkdir test_docs
    ```

2. अनुवाद गर्न चाहेको markdown डक्युमेन्टेसन र images test directory मा राख्नुहोस्। उदाहरणका लागि:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. प्याकेज स्थानीय रूपमा स्थापना गर्नुहोस्:
    ```bash
    pip install -e .
    ```

4. आफ्नो test डक्युमेन्टहरूमा Co-op Translator चलाउनुहोस्:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` र `test_docs/translated_images` मा अनुवादित फाइलहरू जाँच गर्नुहोस्:
   - अनुवादको गुणस्तर
   - metadata टिप्पणीहरू सही छन् कि छैनन्
   - मूल markdown संरचना जस्ताको तस्तै छ कि छैन
   - लिंक र images ठीकसँग काम गर्छन् कि छैनन्

यो म्यानुअल परीक्षणले तपाईंको परिवर्तनहरू वास्तविक प्रयोगमा राम्रोसँग काम गर्छन् भन्ने सुनिश्चित गर्छ।

### Environment variables

1. root directory मा `.env.template` फाइलको प्रतिलिपि गरेर `.env` फाइल बनाउनुहोस्।
1. निर्देशन अनुसार environment variables भर्नुहोस्।

> [!TIP]
>
> ### थप विकास वातावरण विकल्पहरू
>
> परियोजना स्थानीय रूपमा चलाउनुका साथै, GitHub Codespaces वा VS Code Dev Containers पनि प्रयोग गर्न सक्नुहुन्छ।
>
> #### GitHub Codespaces
>
> तपाईंले GitHub Codespaces प्रयोग गरेर virtually samples चलाउन सक्नुहुन्छ, कुनै अतिरिक्त सेटअप आवश्यक छैन।
>
> यो बटनले तपाईंको ब्राउजरमा web-based VS Code खोल्छ:
>
> 1. template खोल्नुहोस् (केही मिनेट लाग्न सक्छ):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### स्थानीय रूपमा VS Code Dev Containers प्रयोग गरेर चलाउने
>
> ⚠️ यो विकल्प तभी काम गर्छ जब तपाईंको Docker Desktop मा कम्तिमा १६ GB RAM छ। यदि तपाईंको RAM १६ GB भन्दा कम छ भने, [GitHub Codespaces विकल्प](../..) वा [स्थानीय रूपमा सेटअप](../..) प्रयास गर्न सक्नुहुन्छ।
>
> अर्को विकल्प VS Code Dev Containers हो, जसले तपाईंको स्थानीय VS Code मा [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) प्रयोग गरेर परियोजना खोल्छ:
>
> 1. Docker Desktop सुरु गर्नुहोस् (स्थापना नभएको भए पहिले स्थापना गर्नुहोस्)
> 2. परियोजना खोल्नुहोस्:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### कोड शैली

हामी [Black](https://github.com/psf/black) लाई Python कोड formatter को रूपमा प्रयोग गर्छौं, जसले परियोजनामा कोड शैली एकरूप राख्न मद्दत गर्छ। Black ले Python कोडलाई स्वचालित रूपमा Black कोड शैलीमा पुनःफर्म्याट गर्छ।

#### कन्फिगरेसन

Black को कन्फिगरेसन हाम्रो `pyproject.toml` मा छ:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black स्थापना गर्ने

Poetry (सिफारिस गरिएको) वा pip प्रयोग गरेर Black स्थापना गर्न सकिन्छ:

##### Poetry प्रयोग गरेर

विकास वातावरण सेटअप गर्दा Black स्वचालित रूपमा स्थापना हुन्छ:
```bash
poetry install
```

##### pip प्रयोग गरेर

यदि तपाईं pip प्रयोग गर्दै हुनुहुन्छ भने, Black सिधै स्थापना गर्न सक्नुहुन्छ:
```bash
pip install black
```

#### Black प्रयोग गर्ने

##### Poetry सँग

1. परियोजनाका सबै Python फाइलहरू फर्म्याट गर्नुहोस्:
    ```bash
    poetry run black .
    ```

2. कुनै विशेष फाइल वा directory फर्म्याट गर्नुहोस्:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip सँग

1. परियोजनाका सबै Python फाइलहरू फर्म्याट गर्नुहोस्:
    ```bash
    black .
    ```

2. कुनै विशेष फाइल वा directory फर्म्याट गर्नुहोस्:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> तपाईंको editor लाई Black सँग कोड save गर्दा स्वचालित रूपमा फर्म्याट गर्न सेटअप गर्न सिफारिस गरिन्छ। अधिकांश आधुनिक editor हरूमा extension वा plugin मार्फत यो सुविधा उपलब्ध छ।

## Co-op Translator चलाउने

Poetry प्रयोग गरेर Co-op Translator चलाउनका लागि तलका चरणहरू पालना गर्नुहोस्:

1. अनुवाद परीक्षण गर्न चाहेको directory मा जानुहोस् वा परीक्षणका लागि temporary folder बनाउनुहोस्।

2. तलको आदेश चलाउनुहोस्। `-l ko` लाई तपाईं अनुवाद गर्न चाहेको भाषा कोडमा परिवर्तन गर्नुहोस्। `-d` flag ले debug mode जनाउँछ।

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> आदेश चलाउनु अघि Poetry वातावरण सक्रिय भएको छ (poetry shell) भन्ने सुनिश्चित गर्नुहोस्।

## नयाँ भाषा योगदान गर्नुहोस्

नयाँ भाषा समर्थन थप्नका लागि योगदानलाई स्वागत छ। PR खोल्नु अघि, समीक्षा सहज बनाउन तलका चरणहरू पूरा गर्नुहोस्।

1. भाषा font mapping मा थप्नुहोस्
   - `src/co_op_translator/fonts/font_language_mappings.yml` सम्पादन गर्नुहोस्
   - निम्न विवरण थप्नुहोस्:
     - `code`: ISO-जस्तो भाषा कोड (जस्तै, `vi`)
     - `name`: देखिने नाम
     - `font`: `src/co_op_translator/fonts/` मा उपलब्ध script समर्थन गर्ने font
     - `rtl`: दायाँबाट-बायाँ भए `true`, अन्यथा `false`

2. आवश्यक font फाइलहरू समावेश गर्नुहोस् (आवश्यक भएमा)
   - नयाँ font आवश्यक भए, open source वितरणका लागि license मिल्छ कि जाँच गर्नुहोस्
   - font फाइल `src/co_op_translator/fonts/` मा थप्नुहोस्

3. स्थानीय परीक्षण
   - सानो sample (Markdown, images, notebooks) मा अनुवाद चलाउनुहोस्
   - output सही देखिन्छ कि जाँच गर्नुहोस्, font र RTL layout समेत

4. डक्युमेन्टेसन अपडेट गर्नुहोस्
   - भाषा `getting_started/supported-languages.md` मा देखिन्छ कि सुनिश्चित गर्नुहोस्
   - `README_languages_template.md` मा परिवर्तन आवश्यक छैन; यो supported list बाट स्वतः बनाइन्छ

5. PR खोल्नुहोस्
   - थपिएको भाषा र font/license सम्बन्धी कुरा उल्लेख गर्नुहोस्
   - सकेसम्म output को screenshot संलग्न गर्नुहोस्

Example YAML entry:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Maintainers

### Commit message र Merge रणनीति

परियोजनाको commit इतिहासमा एकरूपता र स्पष्टता सुनिश्चित गर्न, हामी **Squash and Merge** रणनीति प्रयोग गर्दा अन्तिम commit message को लागि विशेष ढाँचा पालना गर्छौं।

Pull request (PR) merge गर्दा, individual commits एक commit मा squash गरिन्छ। अन्तिम commit message तलको ढाँचामा हुनुपर्छ।

#### Commit message ढाँचा (squash and merge का लागि)

हामी commit messages का लागि निम्न ढाँचा प्रयोग गर्छौं:

```bash
<type>: <description> (#<PR number>)
```

- **type**: commit को category जनाउँछ। हामी निम्न प्रकार प्रयोग गर्छौं:
  - `Docs`: डक्युमेन्टेसन अपडेटका लागि।
  - `Build`: build system वा निर्भरता सम्बन्धी परिवर्तनका लागि, जस्तै configuration files, CI workflows, Dockerfile।
  - `Core`: परियोजनाको मुख्य कार्यक्षमता वा features मा परिवर्तनका लागि, विशेष गरी `src/co_op_translator/core` directory मा।

- **description**: परिवर्तनको संक्षिप्त सारांश।
- **PR number**: commit सँग सम्बन्धित pull request नम्बर।

**उदाहरणहरू**:

- `Docs: स्पष्टता लागि स्थापना निर्देशन अपडेट (#50)`
- `Core: image translation को ह्यान्डलिंग सुधार (#60)`

> [!NOTE]
> हाल, **`Docs`**, **`Core`**, र **`Build`** prefixes PR title मा स्वतः थपिन्छ, source code मा लागू गरिएको label अनुसार। सही label लागू भएमा, PR title manually अपडेट गर्न आवश्यक छैन। तपाईंले सबै कुरा सही छ कि छैन र prefix ठीकसँग आएको छ कि जाँच गर्नुपर्छ।

#### Merge रणनीति

हामी pull requests का लागि default रूपमा **Squash and Merge** रणनीति प्रयोग गर्छौं। यसले commit messages हाम्रो ढाँचामा राख्न मद्दत गर्छ, individual commits जस्तो भए पनि।

**कारणहरू**:

- परियोजनाको इतिहास सफा र linear हुन्छ।
- commit messages मा एकरूपता।
- साना commits (जस्तै, "fix typo") बाट उत्पन्न हुने अनावश्यक कुरा कम हुन्छ।

Merge गर्दा, अन्तिम commit message माथि उल्लेखित ढाँचामा राख्नुहोस्।

**Squash and Merge को उदाहरण**
यदि PR मा निम्न commits छन्:

- `fix typo`
- `update README`
- `adjust formatting`

यी squash गरेर यस्तो हुनुपर्छ:
`Docs: Improve documentation clarity and formatting (#65)`

---

**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल भाषामा रहेको दस्तावेज़लाई नै अधिकारिक स्रोत मान्नुपर्छ। महत्वपूर्ण जानकारीको लागि, पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलत बुझाइ वा व्याख्याका लागि हामी जिम्मेवार हुने छैनौं।