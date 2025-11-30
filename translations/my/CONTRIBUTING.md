<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T04:11:12+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "my"
}
-->
# Co-op Translator ကို ပူးပေါင်းဆောင်ရွက်ခြင်း

ဒီ project မှာ ပူးပေါင်းဆောင်ရွက်မှုနဲ့ အကြံပြုချက်တွေကို ကြိုဆိုပါတယ်။ အများစုသော ပူးပေါင်းမှုတွေမှာ Contributor License Agreement (CLA) ကို သဘောတူဖို့ လိုအပ်ပါတယ်။ ဒါက သင့်ရဲ့ ပူးပေါင်းမှုကို အသုံးပြုခွင့်ကို ကျွန်တော်တို့ကို ပေးနိုင်ဖို့ သင့်မှာ အခွင့်အရေးရှိတယ်ဆိုတာ ကြေညာတာပါ။ အသေးစိတ်ကို https://cla.opensource.microsoft.com မှာ ကြည့်နိုင်ပါတယ်။

Pull request တင်တဲ့အခါ CLA bot က သင် CLA တင်ဖို့ လိုအပ်/မလိုအပ် စစ်ဆေးပြီး PR ကို သက်ဆိုင်ရာအတိုင်း ပြသပေးပါလိမ့်မယ် (ဥပမာ status check, comment စသည်ဖြင့်)။ Bot ရဲ့ ညွှန်ကြားချက်ကို လိုက်နာပေးပါ။ CLA ကို တစ်ကြိမ်တည်းပဲ တင်ရမှာဖြစ်ပြီး ကျွန်တော်တို့ CLA ကို သုံးတဲ့ repo တွေအားလုံးမှာ အသုံးဝင်ပါတယ်။

## Development environment ကို ပြင်ဆင်ခြင်း

ဒီ project အတွက် development environment ကို ပြင်ဆင်ဖို့ Poetry ကို အသုံးပြုဖို့ အကြံပြုပါတယ်။ Project dependencies တွေကို `pyproject.toml` မှာ စီမံထားတာမို့ Dependencies တွေကို တင်ဖို့ Poetry ကို သုံးပါ။

### Virtual environment တစ်ခု ဖန်တီးခြင်း

#### pip သုံးခြင်း

```bash
python -m venv .venv
```

#### Poetry သုံးခြင်း

```bash
poetry init
```

### Virtual environment ကို အသက်သွင်းခြင်း

#### pip နဲ့ Poetry နှစ်ခုလုံးအတွက်

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry သုံးခြင်း

```bash
poetry shell
```

### Package နဲ့ လိုအပ်တဲ့ Packages တွေ တင်ခြင်း

#### Poetry သုံးပြီး (pyproject.toml မှ)

```bash
poetry install
```

### Manual testing

PR တင်မတင်ခင်မှာ Translation လုပ်တဲ့ function ကို တကယ့် documentation နဲ့ စမ်းသပ်ကြည့်တာ အရေးကြီးပါတယ်။

1. Root directory မှာ test directory တစ်ခု ဖန်တီးပါ:
    ```bash
    mkdir test_docs
    ```

2. သင် translate လုပ်ချင်တဲ့ markdown documentation နဲ့ images တွေကို test directory ထဲကို ကူးထည့်ပါ။ ဥပမာ:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Package ကို local မှာ တင်ပါ:
    ```bash
    pip install -e .
    ```

4. သင့် test documents တွေမှာ Co-op Translator ကို run ပါ:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` နဲ့ `test_docs/translated_images` ထဲက translated files တွေကို စစ်ဆေးပါ:
   - ဘာသာပြန်ရတဲ့ အရည်အသွေး
   - Metadata comments တွေ မှန်ကန်မှု
   - မူလ markdown structure ကို ထိန်းသိမ်းထားမှု
   - Links နဲ့ images တွေ မှန်ကန်စွာ အလုပ်လုပ်မှု

ဒီလို manual testing လုပ်ခြင်းက သင့်ပြင်ဆင်မှုတွေဟာ တကယ့်အသုံးပြုမှုမှာ အလုပ်လုပ်သလား စစ်ဆေးနိုင်ပါတယ်။

### Environment variables

1. Root directory မှာ `.env` ဖိုင်ကို `.env.template` ဖိုင်ကို ကူးယူပြီး ဖန်တီးပါ။
1. Environment variables တွေကို ညွှန်ကြားချက်အတိုင်း ဖြည့်ပါ။

> [!TIP]
>
> ### Development environment အတွက် အခြားရွေးချယ်စရာများ
>
> Project ကို local မှာ run လုပ်ခြင်းအပြင် GitHub Codespaces သို့မဟုတ် VS Code Dev Containers ကိုလည်း အသုံးပြုနိုင်ပါတယ်။
>
> #### GitHub Codespaces
>
> GitHub Codespaces ကို သုံးပြီး ဒီ sample တွေကို virtual မှာ run လုပ်နိုင်ပါတယ်။ ထပ်ဆင့်ပြင်ဆင်စရာမလိုပါ။
>
> ဒီ button ကိုနှိပ်ရင် browser မှာ web-based VS Code instance တစ်ခု ဖွင့်ပေးပါလိမ့်မယ်:
>
> 1. Template ကို ဖွင့်ပါ (အချိန်အနည်းငယ် ကြာနိုင်ပါတယ်):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### Local မှာ VS Code Dev Containers သုံးပြီး run လုပ်ခြင်း
>
> ⚠️ ဒီ option ကို သုံးဖို့အတွက် သင့် Docker Desktop မှာ အနည်းဆုံး 16 GB RAM ရှိဖို့ လိုအပ်ပါတယ်။ RAM နည်းနေရင် [GitHub Codespaces option](../..) သို့မဟုတ် [local မှာ ပြင်ဆင်ခြင်း](../..) ကို စမ်းကြည့်နိုင်ပါတယ်။
>
> ဆက်စပ်ရွေးချယ်စရာတစ်ခုက VS Code Dev Containers ဖြစ်ပြီး [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) ကို သုံးပြီး local VS Code မှာ project ကို ဖွင့်နိုင်ပါတယ်။
>
> 1. Docker Desktop ကို start လုပ်ပါ (မရှိသေးရင် install လုပ်ပါ)
> 2. Project ကို ဖွင့်ပါ:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>

### Code Style

Project တစ်ခုလုံးမှာ code style ကို တစ်သမတ်တည်း ထိန်းသိမ်းဖို့ [Black](https://github.com/psf/black) Python code formatter ကို သုံးပါတယ်။ Black က Python code ကို Black style အတိုင်း အလိုအလျောက် ပြန်စီပေးပါတယ်။

#### Configuration

Black configuration ကို `pyproject.toml` မှာ သတ်မှတ်ထားပါတယ်။

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black ကို တင်ခြင်း

Black ကို Poetry (အကြံပြု) သို့မဟုတ် pip နဲ့ တင်နိုင်ပါတယ်။

##### Poetry သုံးခြင်း

Development environment ပြင်ဆင်တဲ့အခါ Black ကို အလိုအလျောက် တင်ပေးပါလိမ့်မယ်:
```bash
poetry install
```

##### pip သုံးခြင်း

pip သုံးရင် Black ကို တိုက်ရိုက် တင်နိုင်ပါတယ်:
```bash
pip install black
```

#### Black ကို အသုံးပြုခြင်း

##### Poetry နဲ့

1. Project ထဲက Python files အားလုံးကို format လုပ်ပါ:
    ```bash
    poetry run black .
    ```

2. File တစ်ခု သို့မဟုတ် directory တစ်ခုကို format လုပ်ပါ:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip နဲ့

1. Project ထဲက Python files အားလုံးကို format လုပ်ပါ:
    ```bash
    black .
    ```

2. File တစ်ခု သို့မဟုတ် directory တစ်ခုကို format လုပ်ပါ:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Code ကို Black နဲ့ save လုပ်တိုင်း အလိုအလျောက် format လုပ်ဖို့ editor ကို ပြင်ဆင်ထားဖို့ အကြံပြုပါတယ်။ Editor များစုစုပေါင်းမှာ extension သို့မဟုတ် plugin တွေနဲ့ ဒီအလုပ်ကို လုပ်နိုင်ပါတယ်။

## Co-op Translator ကို run လုပ်ခြင်း

Poetry ကို သုံးပြီး Co-op Translator ကို run လုပ်ဖို့ အောက်ပါအဆင့်တွေကို လိုက်နာပါ။

1. Translation test လုပ်ချင်တဲ့ directory ကို သွားပါ သို့မဟုတ် စမ်းသပ်ဖို့အတွက် temporary folder တစ်ခု ဖန်တီးပါ။

2. အောက်ပါ command ကို run ပါ။ `-l ko` ကို သင် translate လုပ်ချင်တဲ့ ဘာသာစကား code နဲ့ အစားထိုးပါ။ `-d` flag က debug mode ကို ဆိုလိုပါတယ်။

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Command ကို run လုပ်ခင် Poetry environment ကို activate (poetry shell) လုပ်ထားဖို့ သေချာပါစေ။

## ဘာသာစကားအသစ် တစ်ခု ထည့်သွင်းရန်

ဘာသာစကားအသစ်တွေကို ထပ်မံထည့်သွင်းဖို့ ကြိုဆိုပါတယ်။ PR တင်ခင် အောက်ပါအဆင့်တွေကို ပြီးစီးထားဖို့ လိုအပ်ပါတယ်။

1. Font mapping မှာ ဘာသာစကားကို ထည့်ပါ
   - `src/co_op_translator/fonts/font_language_mappings.yml` ကို ပြင်ပါ
   - အောက်ပါအတိုင်း entry တစ်ခု ထည့်ပါ:
     - `code`: ISO နဲ့ ဆင်တူ language code (ဥပမာ `vi`)
     - `name`: လူသုံး display name
     - `font`: `src/co_op_translator/fonts/` ထဲမှာရှိတဲ့ script ကို support လုပ်တဲ့ font
     - `rtl`: ဘယ်မှညာသို့ (right-to-left) ဆိုရင် `true`, မဟုတ်ရင် `false`

2. လိုအပ်လျှင် font files တွေ ထည့်ပါ
   - Font အသစ်လိုအပ်ရင် open source ဖြန့်ဝေခွင့်ရှိ/မရှိ စစ်ဆေးပါ
   - Font file ကို `src/co_op_translator/fonts/` ထဲထည့်ပါ

3. Local မှာ စစ်ဆေးပါ
   - Markdown, images, notebooks စသည့် sample နည်းနည်းနဲ့ translate လုပ်ပါ
   - Output မှာ font တွေ၊ RTL layout (လိုအပ်လျှင်) မှန်ကန်စွာ ပြသနိုင်မှု စစ်ဆေးပါ

4. Documentation ကို update လုပ်ပါ
   - ဘာသာစကားအသစ်ကို `getting_started/supported-languages.md` မှာ ထည့်ပါ
   - `README_languages_template.md` ကို ပြင်စရာမလိုပါဘူး။ supported list မှ auto generate ဖြစ်ပါတယ်

5. PR တင်ပါ
   - ထည့်သွင်းတဲ့ ဘာသာစကားနဲ့ font/licensing အကြောင်းအရာကို ရှင်းပြပါ
   - Screenshot တွေပါထည့်နိုင်ရင် ပိုကောင်းပါတယ်

ตัวอย่าง YAML entry:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Maintainers

### Commit message နဲ့ Merge strategy

Project ရဲ့ commit history ကို တစ်သမတ်တည်း၊ ရှင်းလင်းစွာ ထိန်းသိမ်းဖို့ **Squash and Merge** strategy ကို သုံးတဲ့အခါ **နောက်ဆုံး commit message** format ကို လိုက်နာပါတယ်။

Pull request (PR) တစ်ခု merge လုပ်တဲ့အခါ commits တွေကို တစ်ခုတည်း commit အဖြစ် squash လုပ်ပါလိမ့်မယ်။ နောက်ဆုံး commit message ကို အောက်ပါ format နဲ့ ရေးသင့်ပါတယ်။

#### Commit message format (squash and merge အတွက်)

Commit message တွေကို အောက်ပါ format နဲ့ သုံးပါတယ်။

```bash
<type>: <description> (#<PR number>)
```

- **type**: Commit ရဲ့ category ကို ဖော်ပြပါတယ်။ အောက်ပါ type တွေကို သုံးပါတယ်။
  - `Docs`: Documentation update အတွက်။
  - `Build`: Build system သို့မဟုတ် dependencies, configuration files, CI workflows, Dockerfile စသည့် ပြင်ဆင်မှုအတွက်။
  - `Core`: Project ရဲ့ core functionality သို့မဟုတ် features တွေ၊ အထူးသဖြင့် `src/co_op_translator/core` directory ထဲက files တွေပြင်ဆင်မှုအတွက်။

- **description**: ပြင်ဆင်မှုအကြောင်း အကျဉ်းချုပ်။
- **PR number**: Pull request နံပါတ်။

**ဥပမာများ**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> လက်ရှိမှာ **`Docs`**, **`Core`**, **`Build`** prefix တွေကို PR title မှာ labels အပေါ်မူတည်ပြီး အလိုအလျောက် ထည့်ပေးပါတယ်။ မှန်ကန်တဲ့ label ကို apply လုပ်ထားရင် PR title ကို ကိုယ်တိုင် ပြင်စရာမလိုပါဘူး။ Prefix မှန်/မမှန် စစ်ဆေးပေးရုံပါ။

#### Merge strategy

Pull requests အတွက် **Squash and Merge** ကို default strategy အနေနဲ့ သုံးပါတယ်။ ဒီ strategy က commit messages တွေ format ကို တစ်သမတ်တည်း ထိန်းသိမ်းနိုင်ပါတယ်။

**အကြောင်းပြချက်များ**:

- Project history ကို ရှင်းလင်း၊ တစ်ကြောင်းတည်း ထိန်းသိမ်းနိုင်ခြင်း
- Commit messages တွေ တစ်သမတ်တည်း ဖြစ်ခြင်း
- အရေးမကြီးတဲ့ commits (ဥပမာ "fix typo") တွေကို လျှော့ချနိုင်ခြင်း

Merge လုပ်တဲ့အခါ နောက်ဆုံး commit message ကို အထက်ပါ format နဲ့ ရေးထားဖို့ သေချာပါစေ။

**Squash and Merge ဥပမာ**
PR တစ်ခုမှာ အောက်ပါ commits တွေပါဝင်ရင်:

- `fix typo`
- `update README`
- `adjust formatting`

Squash လုပ်ပြီးနောက်:
`Docs: Improve documentation clarity and formatting (#65)`

---

**သတိပေးချက်**:
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို မူလဘာသာဖြင့်သာ အာဏာရှိသောရင်းမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသောအချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များ၏ ဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာသော နားလည်မှုမှားခြင်း သို့မဟုတ် အနားလည်မှုမှားခြင်းများအတွက် ကျွန်ုပ်တို့သည် တာဝန်ယူမည်မဟုတ်ပါ။