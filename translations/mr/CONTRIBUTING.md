<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:30:56+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "mr"
}
-->
# Co-op Translator मध्ये योगदान देणे

हा प्रकल्प योगदान आणि सूचना स्वीकारतो. बहुतेक योगदानांसाठी तुम्हाला Contributor License Agreement (CLA) सहमत व्हावे लागते ज्यात तुम्ही सांगता की तुम्हाला तुमच्या योगदानाचा वापर करण्याचा अधिकार आहे आणि तुम्ही तो अधिकार आम्हाला देत आहात. तपशीलांसाठी, https://cla.opensource.microsoft.com वर भेट द्या.

जेव्हा तुम्ही pull request सबमिट करता, तेव्हा CLA bot आपोआप ठरवेल की तुम्हाला CLA प्रदान करायची आहे का आणि PR योग्यरित्या सजवेल (उदा., status check, comment). फक्त bot ने दिलेल्या सूचनांचे पालन करा. हा एकच वेळा सर्व repos मध्ये करणे आवश्यक आहे ज्यात आमचा CLA वापर होतो.

## विकास पर्यावरण सेटअप

या प्रकल्पासाठी विकास पर्यावरण सेट करण्यासाठी, आम्ही Poetry वापरण्याचा सल्ला देतो जे अवलंबन व्यवस्थापनासाठी उपयुक्त आहे. आम्ही प्रकल्पाच्या अवलंबनांचे व्यवस्थापन करण्यासाठी `pyproject.toml` वापरतो, त्यामुळे अवलंबने इन्स्टॉल करण्यासाठी तुम्ही Poetry वापरायला हवे.

### वर्चुअल एन्व्हायर्नमेंट तयार करा

#### pip वापरून

```bash
python -m venv .venv
```

#### Poetry वापरून

```bash
poetry init
```

### वर्चुअल एन्व्हायर्नमेंट सक्रिय करा

#### pip आणि Poetry दोन्हीसाठी

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry वापरून

```bash
poetry shell
```

### पॅकेज आणि आवश्यक पॅकेजेस इन्स्टॉल करणे

#### Poetry वापरून (pyproject.toml मधून)

```bash
poetry install
```

### मॅन्युअल चाचणी

PR सबमिट करण्यापूर्वी, वास्तविक दस्तऐवजांसह भाषांतर कार्यक्षमता तपासणे महत्त्वाचे आहे:

1. मूळ निर्देशिकेत test निर्देशिका तयार करा:
    ```bash
    mkdir test_docs
    ```

2. भाषांतरासाठी हवे असलेले markdown दस्तऐवज आणि प्रतिमा test निर्देशिकेत कॉपी करा. उदाहरणार्थ:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. पॅकेज स्थानिकरित्या इन्स्टॉल करा:
    ```bash
    pip install -e .
    ```

4. तुमच्या test दस्तऐवजांवर Co-op Translator चालवा:
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

1. Create an `.env` file in the root directory by copying the provided `.env.template` फाईलमधील भाषांतरित फाइल्स तपासा.
1. पर्यावरण चल भरण्याचे मार्गदर्शन करा.

> [!TIP]
>
> ### अतिरिक्त विकास पर्यावरण पर्याय
>
> प्रकल्प स्थानिकरित्या चालवण्याशिवाय, तुम्ही GitHub Codespaces किंवा VS Code Dev Containers वापरून पर्यायी विकास पर्यावरण देखील सेट करू शकता.
>
> #### GitHub Codespaces
>
> GitHub Codespaces वापरून तुम्ही हा नमुना आभासीपणे चालवू शकता आणि यासाठी कोणतीही अतिरिक्त सेटिंग्ज किंवा सेटअप आवश्यक नाही.
>
> बटण तुमच्या ब्राउझरमध्ये वेब-आधारित VS Code उदाहरण उघडेल:
>
> 1. टेम्प्लेट उघडा (हे काही मिनिटे लागू शकतात):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### VS Code Dev Containers वापरून स्थानिक चालवणे
>
> ⚠️ हा पर्याय फक्त तेव्हाच काम करेल जेव्हा तुमच्या Docker Desktop ला किमान 16 GB RAM वाटप केलेले असेल. जर तुमच्याकडे 16 GB पेक्षा कमी RAM असेल, तर तुम्ही [GitHub Codespaces पर्याय](../..) वापरू शकता किंवा [स्थानिक सेटअप](../..) करू शकता.
>
> संबंधित पर्याय म्हणजे VS Code Dev Containers, जे प्रकल्प तुमच्या स्थानिक VS Code मध्ये [Dev Containers विस्तार](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) वापरून उघडेल:
>
> 1. Docker Desktop सुरू करा (जर नसेल तर इन्स्टॉल करा)
> 2. प्रकल्प उघडा:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### कोड शैली

आम्ही प्रकल्पात सुसंगत कोड शैली राखण्यासाठी Python कोड फॉर्मॅटर म्हणून [Black](https://github.com/psf/black) वापरतो. Black हा एक कडक कोड फॉर्मॅटर आहे जो Python कोड आपोआप Black च्या कोड शैलीनुसार पुनर्रूपित करतो.

#### कॉन्फिगरेशन

Black ची कॉन्फिगरेशन आमच्या `pyproject.toml` मध्ये निर्दिष्ट केलेली आहे:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black इन्स्टॉल करणे

तुम्ही Black Poetry (शिफारस केलेले) किंवा pip वापरून इन्स्टॉल करू शकता:

##### Poetry वापरून

विकास पर्यावरण सेट करताना Black आपोआप इन्स्टॉल होतो:
```bash
poetry install
```

##### pip वापरून

जर तुम्ही pip वापरत असाल, तर Black थेट इन्स्टॉल करू शकता:
```bash
pip install black
```

#### Black वापरणे

##### Poetry सह

1. प्रकल्पातील सर्व Python फाइल्स फॉर्मॅट करा:
    ```bash
    poetry run black .
    ```

2. विशिष्ट फाइल किंवा निर्देशिका फॉर्मॅट करा:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip सह

1. प्रकल्पातील सर्व Python फाइल्स फॉर्मॅट करा:
    ```bash
    black .
    ```

2. विशिष्ट फाइल किंवा निर्देशिका फॉर्मॅट करा:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> आम्ही शिफारस करतो की तुम्ही तुमच्या संपादकात Black वापरून कोड सेव्ह करताना आपोआप फॉर्मॅट होईल असे सेटअप करा. बहुतेक आधुनिक संपादक हे विस्तार किंवा प्लगइनद्वारे समर्थित करतात.

## Co-op Translator चालवणे

तुमच्या पर्यावरणात Poetry वापरून Co-op Translator चालवण्यासाठी, खालील चरणांचे पालन करा:

1. त्या निर्देशिकेत जा जिथे तुम्हाला भाषांतर चाचण्या करायच्या आहेत किंवा चाचणीसाठी तात्पुरते फोल्डर तयार करा.

2. खालील कमांड चालवा. `-l ko` with the language code you wish to translate into. The `-d` फलकडे डिबग मोड सूचित करतो.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> कमांड चालवण्यापूर्वी तुमचे Poetry पर्यावरण सक्रिय (poetry shell) आहे याची खात्री करा.

## देखभाल करणारे

### कमिट संदेश आणि मर्ज धोरण

आमच्या प्रकल्पाच्या कमिट इतिहासात सुसंगतता आणि स्पष्टता सुनिश्चित करण्यासाठी, आम्ही **Squash and Merge** धोरण वापरताना **अंतिम कमिट संदेशासाठी** विशिष्ट कमिट संदेश फॉरमॅट अनुसरतो.

जेव्हा pull request (PR) मर्ज होते, तेव्हा वेगवेगळे कमिट्स एका कमिटमध्ये एकत्र केले जातात. अंतिम कमिट संदेश खालील फॉरमॅटमध्ये असावा जेणेकरून स्वच्छ आणि सुसंगत इतिहास राखता येईल.

#### कमिट संदेश फॉरमॅट (squash and merge साठी)

आम्ही कमिट संदेशांसाठी खालील फॉरमॅट वापरतो:

```bash
<type>: <description> (#<PR number>)
```

- **type**: कमिटच्या प्रकाराचे स्पष्टीकरण. आम्ही खालील प्रकार वापरतो:
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
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीकरिता व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाचा वापर करून उद्भवणाऱ्या कोणत्याही गैरसमजुतीसाठी किंवा चुकीच्या अर्थलागीसाठी आम्ही जबाबदार नाही.