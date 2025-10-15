<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T02:48:52+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "mr"
}
-->
# Co-op Translator मध्ये योगदान देणे

या प्रकल्पात योगदान आणि सूचना स्वागतार्ह आहेत. बहुतेक योगदानांसाठी तुम्हाला Contributor License Agreement (CLA) वर सहमती द्यावी लागते, ज्यामध्ये तुम्ही आम्हाला तुमचे योगदान वापरण्याचा अधिकार देत आहात, हे जाहीर करता. अधिक माहितीसाठी https://cla.opensource.microsoft.com या लिंकला भेट द्या.

जेव्हा तुम्ही pull request सबमिट करता, तेव्हा CLA bot आपोआप तपासेल की तुम्हाला CLA द्यायची गरज आहे का आणि PR ला योग्यरित्या सजवेल (उदा., status check, comment). फक्त bot ने दिलेल्या सूचनांचे पालन करा. तुम्हाला हे सर्व CLA वापरणाऱ्या सर्व रेपोजसाठी फक्त एकदाच करावे लागेल.

## विकासासाठी वातावरणाची सेटअप

या प्रकल्पासाठी विकासाचे वातावरण सेट करण्यासाठी, dependency व्यवस्थापनासाठी Poetry वापरण्याची शिफारस केली जाते. आम्ही प्रकल्पाच्या dependency साठी `pyproject.toml` वापरतो, त्यामुळे dependency install करण्यासाठी Poetry वापरा.

### virtual environment तयार करा

#### pip वापरून

```bash
python -m venv .venv
```

#### Poetry वापरून

```bash
poetry init
```

### virtual environment सक्रिय करा

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

### पॅकेज आणि आवश्यक पॅकेजेस install करणे

#### Poetry वापरून (pyproject.toml मधून)

```bash
poetry install
```

### मॅन्युअल चाचणी

PR सबमिट करण्यापूर्वी, प्रत्यक्ष दस्तऐवजांसह भाषांतर कार्यक्षमता तपासणे महत्त्वाचे आहे:

1. मुख्य directory मध्ये एक test directory तयार करा:
    ```bash
    mkdir test_docs
    ```

2. तुम्हाला भाषांतर करायचे markdown दस्तऐवज आणि प्रतिमा test directory मध्ये कॉपी करा. उदाहरणार्थ:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. पॅकेज स्थानिकरित्या install करा:
    ```bash
    pip install -e .
    ```

4. Co-op Translator तुमच्या test documents वर चालवा:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` आणि `test_docs/translated_images` मधील भाषांतरित फाइल्स तपासा आणि खात्री करा:
   - भाषांतराची गुणवत्ता
   - metadata comments योग्य आहेत का
   - मूळ markdown रचना जशीच्या तशी आहे का
   - लिंक आणि प्रतिमा व्यवस्थित काम करत आहेत का

ही मॅन्युअल चाचणी तुमचे बदल प्रत्यक्ष वापरात योग्यरित्या काम करतात याची खात्री करते.

### Environment variables

1. मुख्य directory मध्ये `.env.template` फाइल कॉपी करून `.env` फाइल तयार करा.
1. दिलेल्या सूचनांप्रमाणे environment variables भरा.

> [!TIP]
>
> ### अतिरिक्त विकास वातावरणाचे पर्याय
>
> प्रकल्प स्थानिकरित्या चालवण्याव्यतिरिक्त, GitHub Codespaces किंवा VS Code Dev Containers वापरूनही विकासाचे वातावरण सेट करू शकता.
>
> #### GitHub Codespaces
>
> GitHub Codespaces वापरून हे samples virtually चालवू शकता आणि कोणतीही अतिरिक्त सेटिंग किंवा सेटअप आवश्यक नाही.
>
> हा बटण तुमच्या ब्राउझरमध्ये web-based VS Code instance उघडेल:
>
> 1. template उघडा (याला काही मिनिटे लागू शकतात):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### स्थानिकरित्या VS Code Dev Containers वापरून चालवणे
>
> ⚠️ हा पर्याय फक्त तेव्हाच काम करेल जेव्हा तुमच्या Docker Desktop ला किमान 16 GB RAM दिलेले असेल. जर तुमच्याकडे 16 GB पेक्षा कमी RAM असेल, तर [GitHub Codespaces पर्याय](../..) वापरू शकता किंवा [स्थानिकरित्या सेटअप करा](../..).
>
> संबंधित पर्याय म्हणजे VS Code Dev Containers, जे प्रकल्प तुमच्या स्थानिक VS Code मध्ये [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) वापरून उघडेल:
>
> 1. Docker Desktop सुरू करा (install केले नसेल तर आधी install करा)
> 2. प्रकल्प उघडा:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### कोड शैली

आम्ही [Black](https://github.com/psf/black) हा Python code formatter वापरतो, जेणेकरून प्रकल्पात कोड शैली सुसंगत राहील. Black हा एक कठोर formatter आहे जो Python कोड आपोआप Black code style नुसार सुधारतो.

#### संरचना

Black ची संरचना आमच्या `pyproject.toml` मध्ये दिली आहे:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black install करणे

Poetry (शिफारसीय) किंवा pip वापरून Black install करू शकता:

##### Poetry वापरून

विकासाचे वातावरण सेट करताना Black आपोआप install होते:
```bash
poetry install
```

##### pip वापरून

pip वापरत असाल, तर Black थेट install करा:
```bash
pip install black
```

#### Black वापरणे

##### Poetry सह

1. प्रकल्पातील सर्व Python फाइल्स format करा:
    ```bash
    poetry run black .
    ```

2. विशिष्ट फाइल किंवा directory format करा:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip सह

1. प्रकल्पातील सर्व Python फाइल्स format करा:
    ```bash
    black .
    ```

2. विशिष्ट फाइल किंवा directory format करा:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Black सह कोड save करताच आपोआप format होईल असे editor सेटअप करण्याची शिफारस करतो. बहुतेक आधुनिक editors मध्ये हे extension किंवा plugin द्वारे शक्य आहे.

## Co-op Translator चालवणे

Poetry वापरून Co-op Translator चालवण्यासाठी खालील पावले पाळा:

1. ज्या directory मध्ये भाषांतर चाचण्या करायच्या आहेत किंवा चाचणीसाठी तात्पुरती फोल्डर तयार करायची आहे, तिथे जा.

2. खालील कमांड चालवा. `-l ko` ऐवजी तुम्हाला हवी असलेली भाषा कोड वापरा. `-d` flag म्हणजे debug mode.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> कमांड चालवण्यापूर्वी तुमचे Poetry environment सक्रिय (poetry shell) आहे याची खात्री करा.

## नवीन भाषा जोडण्यासाठी योगदान द्या

नवीन भाषांसाठी समर्थन जोडणारे योगदान स्वागतार्ह आहे. PR उघडण्यापूर्वी, खालील पावले पूर्ण करा, जेणेकरून review सुलभ होईल.

1. भाषा font mapping मध्ये जोडा
   - `src/co_op_translator/fonts/font_language_mappings.yml` संपादित करा
   - खालील entry जोडा:
     - `code`: ISO सारखा भाषा कोड (उदा., `vi`)
     - `name`: वाचायला सोपे नाव
     - `font`: `src/co_op_translator/fonts/` मध्ये असलेला script ला support करणारा font
     - `rtl`: script right-to-left असल्यास `true`, अन्यथा `false`

2. आवश्यक font फाइल्स समाविष्ट करा (आवश्यक असल्यास)
   - नवीन font लागल्यास, open source वितरणासाठी license compatible आहे का ते तपासा
   - font फाइल `src/co_op_translator/fonts/` मध्ये जोडा

3. स्थानिक तपासणी
   - लहान sample साठी (Markdown, images, notebooks) भाषांतर चालवा
   - output योग्यरित्या render होते का, font आणि RTL layout (लागल्यास) तपासा

4. दस्तऐवज अपडेट करा
   - भाषा `getting_started/supported-languages.md` मध्ये दिसते आहे याची खात्री करा
   - `README_languages_template.md` मध्ये बदल करण्याची गरज नाही; हे supported list वरून तयार होते

5. PR उघडा
   - कोणती भाषा जोडली आणि font/license बाबत काही विचार आहेत का ते सांगा
   - शक्य असल्यास rendered output चे screenshots जोडा

YAML entry चे उदाहरण:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## देखभाल करणारे

### Commit message आणि Merge strategy

आमच्या प्रकल्पाच्या commit history मध्ये सुसंगतता आणि स्पष्टता राखण्यासाठी, **Squash and Merge** strategy वापरताना **अंतिम commit message** साठी खास format वापरतो.

Pull request (PR) merge केल्यावर, वेगवेगळे commits एकाच commit मध्ये squash केले जातात. अंतिम commit message खालील format नुसार असावा, जेणेकरून history स्वच्छ आणि सुसंगत राहील.

#### Commit message format (squash and merge साठी)

आम्ही commit messages साठी खालील format वापरतो:

```bash
<type>: <description> (#<PR number>)
```

- **type**: commit चा प्रकार दर्शवतो. आम्ही हे प्रकार वापरतो:
  - `Docs`: दस्तऐवज अपडेटसाठी.
  - `Build`: build system किंवा dependency संबंधित बदलांसाठी, configuration files, CI workflows, किंवा Dockerfile updates.
  - `Core`: प्रकल्पाच्या मुख्य कार्यक्षमता किंवा वैशिष्ट्यांमध्ये बदल, विशेषतः `src/co_op_translator/core` directory मधील फाइल्ससाठी.

- **description**: बदलाचा संक्षिप्त सारांश.
- **PR number**: commit शी संबंधित pull request चा क्रमांक.

**उदाहरणे**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> सध्या, **`Docs`**, **`Core`**, आणि **`Build`** हे prefixes PR titles मध्ये आपोआप जोडले जातात, modified source code वर लागू केलेल्या labels नुसार. योग्य label लागू केला असेल, तर तुम्हाला manually PR title बदलण्याची गरज नाही. फक्त सर्व काही योग्य आहे आणि prefix योग्यरित्या तयार झाला आहे याची खात्री करा.

#### Merge strategy

आम्ही pull requests साठी **Squash and Merge** हा default strategy वापरतो. या strategy मुळे commit messages आमच्या format नुसार राहतात, जरी individual commits तसे नसले तरी.

**कारणे**:

- स्वच्छ, linear project history.
- commit messages मध्ये सुसंगतता.
- किरकोळ commits (उदा., "fix typo") मुळे होणारा गोंधळ कमी.

Merge करताना, अंतिम commit message वरील format नुसार आहे याची खात्री करा.

**Squash and Merge चे उदाहरण**
जर PR मध्ये खालील commits असतील:

- `fix typo`
- `update README`
- `adjust formatting`

तर ते squash करून असे असावे:
`Docs: Improve documentation clarity and formatting (#65)`

---

**अस्वीकरण**:
हे दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये चुका किंवा अपूर्णता असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानावा. अत्यावश्यक माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून झालेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.