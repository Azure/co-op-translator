<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:31:28+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ne"
}
-->
# Co-op Translator मा योगदान गर्ने

यो प्रोजेक्ट योगदान र सुझावहरूलाई स्वागत गर्दछ। अधिकांश योगदानहरूका लागि तपाईंले Contributor License Agreement (CLA) मा सहमति जनाउन आवश्यक पर्छ, जसले तपाईंलाई अधिकार दिन्छ र तपाईंले साँच्चिकै हामीलाई तपाईंको योगदान प्रयोग गर्ने अधिकार दिनुभएको छ भनेर घोषणा गर्दछ। विवरणहरूका लागि https://cla.opensource.microsoft.com हेर्नुहोस्।

जब तपाईं pull request पेश गर्नुहुन्छ, CLA बोटले स्वचालित रूपमा निर्धारण गर्नेछ कि तपाईंले CLA प्रदान गर्न आवश्यक छ कि छैन र PR लाई उपयुक्त रूपमा चिन्ह लगाउनेछ (जस्तै, स्थिति जाँच, टिप्पणी)। बोटले दिएको निर्देशनहरू पालना गर्नुहोस्। तपाईंले यो सबै रिपोजिटोरीहरूमा एक पटक मात्र गर्नुपर्नेछ।

## विकास वातावरण सेटअप

यस प्रोजेक्टको विकास वातावरण सेटअप गर्न, हामी निर्भरता व्यवस्थापनका लागि Poetry प्रयोग गर्न सिफारिस गर्छौं। हामी परियोजना निर्भरता व्यवस्थापन गर्न `pyproject.toml` प्रयोग गर्छौं, त्यसैले निर्भरता स्थापना गर्न Poetry प्रयोग गर्नुपर्छ।

### भर्चुअल वातावरण सिर्जना गर्नुहोस्

#### pip प्रयोग गरेर

```bash
python -m venv .venv
```

#### Poetry प्रयोग गरेर

```bash
poetry init
```

### भर्चुअल वातावरण सक्रिय गर्नुहोस्

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

PR पेश गर्नु अघि, वास्तविक डकुमेन्टेसनसँग अनुवाद कार्यक्षमता परीक्षण गर्नु महत्त्वपूर्ण छ:

1. रुट डाइरेक्टरीमा test डाइरेक्टरी सिर्जना गर्नुहोस्:
    ```bash
    mkdir test_docs
    ```

2. अनुवाद गर्न चाहनुभएको केही markdown डकुमेन्टेसन र छविहरू test डाइरेक्टरीमा कपी गर्नुहोस्। उदाहरणका लागि:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. प्याकेज स्थानीय रूपमा स्थापना गर्नुहोस्:
    ```bash
    pip install -e .
    ```

4. तपाईंको test डकुमेन्टहरूमा Co-op Translator चलाउनुहोस्:
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

1. Create an `.env` file in the root directory by copying the provided `.env.template` फाइलमा अनुवादित फाइलहरू जाँच गर्नुहोस्।
1. वातावरण चरहरू निर्देशन अनुसार भर्नुहोस्।

> [!TIP]
>
> ### थप विकास वातावरण विकल्पहरू
>
> प्रोजेक्ट स्थानीय रूपमा चलाउने अतिरिक्त, तपाईं GitHub Codespaces वा VS Code Dev Containers प्रयोग गरेर वैकल्पिक विकास वातावरण सेटअप गर्न सक्नुहुन्छ।
>
> #### GitHub Codespaces
>
> तपाईं GitHub Codespaces प्रयोग गरेर यो नमूनाहरू भर्चुअल रूपमा चलाउन सक्नुहुन्छ र कुनै थप सेटिङ वा सेटअप आवश्यक पर्दैन।
>
> यो बटनले तपाईंको ब्राउजरमा वेब-आधारित VS Code उदाहरण खोल्नेछ:
>
> 1. टेम्प्लेट खोल्नुहोस् (यसले केही मिनेट लिन सक्छ):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### स्थानीय रूपमा VS Code Dev Containers प्रयोग गरेर चलाउने
>
> ⚠️ यो विकल्प तब मात्र काम गर्नेछ जब तपाईंको Docker Desktop मा कम्तिमा 16 GB RAM छुट्याइएको छ। यदि तपाईं सँग 16 GB भन्दा कम RAM छ भने, तपाईं [GitHub Codespaces विकल्प](../..) वा [स्थानीय रूपमा सेटअप गर्ने](../..) प्रयास गर्न सक्नुहुन्छ।
>
> सम्बन्धित विकल्प हो VS Code Dev Containers, जसले तपाईंको स्थानीय VS Code मा [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) प्रयोग गरेर प्रोजेक्ट खोल्नेछ:
>
> 1. Docker Desktop सुरु गर्नुहोस् (यदि छैन भने स्थापना गर्नुहोस्)
> 2. प्रोजेक्ट खोल्नुहोस्:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### कोड शैली

हामीले हाम्रो Python कोड शैलीलाई एकरूप राख्न [Black](https://github.com/psf/black) प्रयोग गर्छौं। Black एक कडाइपूर्वक कोड फर्म्याटर हो जसले Python कोडलाई Black कोड शैलीअनुसार स्वचालित रूपमा पुन: स्वरूपित गर्छ।

#### कन्फिगरेसन

Black कन्फिगरेसन हाम्रो `pyproject.toml` मा निर्दिष्ट गरिएको छ:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black स्थापना गर्ने

तपाईं Black लाई Poetry (सिफारिस गरिएको) वा pip प्रयोग गरेर स्थापना गर्न सक्नुहुन्छ:

##### Poetry प्रयोग गरेर

विकास वातावरण सेटअप गर्दा Black स्वचालित रूपमा स्थापना हुन्छ:
```bash
poetry install
```

##### pip प्रयोग गरेर

pip प्रयोग गर्दै हुनुहुन्छ भने, तपाईंले सिधै Black स्थापना गर्न सक्नुहुन्छ:
```bash
pip install black
```

#### Black प्रयोग गर्ने

##### Poetry सँग

1. प्रोजेक्टका सबै Python फाइलहरू फर्म्याट गर्नुहोस्:
    ```bash
    poetry run black .
    ```

2. विशेष फाइल वा डाइरेक्टरी फर्म्याट गर्नुहोस्:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip सँग

1. प्रोजेक्टका सबै Python फाइलहरू फर्म्याट गर्नुहोस्:
    ```bash
    black .
    ```

2. विशेष फाइल वा डाइरेक्टरी फर्म्याट गर्नुहोस्:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> हामी सिफारिस गर्छौं कि तपाईंको सम्पादकलाई Black सँग कोडलाई बचत गर्दा स्वचालित रूपमा फर्म्याट गर्न सेटअप गर्नुहोस्। अधिकांश आधुनिक सम्पादकहरूले यो विस्तार वा प्लगइनमार्फत समर्थन गर्छन्।

## Co-op Translator चलाउने

तपाईंको वातावरणमा Poetry प्रयोग गरेर Co-op Translator चलाउनका लागि, यी चरणहरू पालना गर्नुहोस्:

1. अनुवाद परीक्षण गर्न चाहनुभएको डाइरेक्टरीमा जानुहोस् वा परीक्षणका लागि अस्थायी फोल्डर सिर्जना गर्नुहोस्।

2. तलको कमाण्ड चलाउनुहोस्। `-l ko` with the language code you wish to translate into. The `-d` झण्डाले डिबग मोड जनाउँछ।

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> कमाण्ड चलाउनुअघि तपाईंको Poetry वातावरण सक्रिय (poetry shell) गरिएको छ भनेर सुनिश्चित गर्नुहोस्।

## मर्मतकर्ताहरू

### कमिट सन्देश र मर्ज रणनीति

हाम्रो प्रोजेक्टको कमिट इतिहासलाई एकरूप र स्पष्ट राख्न, हामी **Squash and Merge** रणनीति प्रयोग गर्दा अन्तिम कमिट सन्देशका लागि विशेष ढाँचा अनुसरण गर्छौं।

जब pull request (PR) मर्ज हुन्छ, व्यक्तिगत कमिटहरू एकल कमिटमा सँगालिनेछन्। अन्तिम कमिट सन्देश तलको ढाँचामा हुनु पर्छ जसले सफा र एकरूप इतिहास सुनिश्चित गर्छ।

#### कमिट सन्देश ढाँचा (squash and merge का लागि)

हामी कमिट सन्देशका लागि तलको ढाँचा प्रयोग गर्छौं:

```bash
<type>: <description> (#<PR number>)
```

- **type**: कमिटको वर्गीकरण जनाउँछ। हामीले निम्न प्रकारहरू प्रयोग गर्छौं:
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
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुनसक्छ। मूल दस्तावेज यसको स्वदेशी भाषामा नै प्रामाणिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीको लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा गलत व्याख्याको लागि हामी जिम्मेवार छैनौं।