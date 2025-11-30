<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T12:40:23+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "my"
}
-->
# Co-op Translator တွင် ပါဝင်ဆောင်ရွက်ခြင်း

ဤပရောဂျက်သည် အထောက်အပံ့များနှင့် အကြံပြုချက်များကို ကြိုဆိုပါသည်။ အများဆုံး အထောက်အပံ့များအတွက် သင်သည် Contributor License Agreement (CLA) တစ်ခုကို သဘောတူရမည်ဖြစ်ပြီး၊ သင်၏ အထောက်အပံ့ကို အသုံးပြုခွင့်ရှိကြောင်းနှင့် အမှန်တကယ်ပေးအပ်ကြောင်း ကြေညာရမည်ဖြစ်သည်။ အသေးစိတ်အချက်အလက်များအတွက် https://cla.opensource.microsoft.com ကို သွားရောက်ကြည့်ရှုနိုင်ပါသည်။

သင်သည် pull request တင်သည့်အခါ CLA bot သည် သင် CLA ပေးရန် လိုအပ်မလား၊ PR ကို မည်သို့ အလှဆင်ရမည်ကို (ဥပမာ - status check, comment) အလိုအလျောက် သတ်မှတ်ပေးပါလိမ့်မည်။ bot မှ ပေးသော ညွှန်ကြားချက်များကို လိုက်နာရုံဖြင့် ဖြစ်ပါသည်။ သင်သည် ကျွန်ုပ်တို့၏ CLA ကို အသုံးပြုသည့် repository များအားလုံးတွင် တစ်ကြိမ်တည်းသာ လုပ်ဆောင်ရမည်ဖြစ်သည်။

## ဖွံ့ဖြိုးတိုးတက်ရေး ပတ်ဝန်းကျင် စတင်ပြင်ဆင်ခြင်း

ဤပရောဂျက်အတွက် ဖွံ့ဖြိုးတိုးတက်ရေး ပတ်ဝန်းကျင်ကို စတင်ပြင်ဆင်ရာတွင် Poetry ကို dependency များ စီမံရန် အကြံပြုပါသည်။ ကျွန်ုပ်တို့သည် `pyproject.toml` ဖြင့် ပရောဂျက် dependency များကို စီမံထားပြီး၊ ထို့ကြောင့် dependency များကို ထည့်သွင်းရန် Poetry ကို အသုံးပြုသင့်ပါသည်။

### Virtual Environment တစ်ခု ဖန်တီးခြင်း

#### pip အသုံးပြုခြင်း

```bash
python -m venv .venv
```


#### Poetry အသုံးပြုခြင်း

```bash
poetry init
```


### Virtual Environment ကို ဖွင့်ခြင်း

#### pip နှင့် Poetry နှစ်ခုလုံးအတွက်

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```


- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```


#### Poetry အသုံးပြုခြင်း

```bash
poetry shell
```


### Package နှင့် လိုအပ်သော Package များ ထည့်သွင်းခြင်း

#### Poetry ဖြင့် (pyproject.toml မှ)

```bash
poetry install
```


### လက်တွေ့ စမ်းသပ်ခြင်း

PR တင်မည့်အရင်မှာ ဘာသာပြန်လုပ်ဆောင်ချက်ကို အမှန်တကယ် စာရွက်စာတမ်းများဖြင့် စမ်းသပ်ရန် အရေးကြီးပါသည်။

1. Root directory တွင် test directory တစ်ခု ဖန်တီးပါ။
    ```bash
    mkdir test_docs
    ```

2. ဘာသာပြန်လိုသော markdown စာရွက်စာတမ်းများနှင့် ပုံများကို test directory ထဲသို့ ကူးယူပါ။ ဥပမာ -
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Package ကို ဒေသခံတွင် ထည့်သွင်းပါ။
    ```bash
    pip install -e .
    ```

4. သင်၏ စမ်းသပ်စာရွက်စာတမ်းများတွင် Co-op Translator ကို လည်ပတ်ပါ။
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` နှင့် `test_docs/translated_images` တွင် ဘာသာပြန်ထားသော ဖိုင်များကို စစ်ဆေးပါ -
   - ဘာသာပြန်အရည်အသွေး
   - metadata မှတ်ချက်များမှန်ကန်မှု
   - မူရင်း markdown ဖွဲ့စည်းမှု ထိန်းသိမ်းမှု
   - လင့်ခ်များနှင့် ပုံများ လုပ်ဆောင်မှုမှန်ကန်မှု

ဤလက်တွေ့ စမ်းသပ်မှုသည် သင်၏ ပြင်ဆင်မှုများကို လက်တွေ့ အသုံးပြုမှုတွင် ကောင်းမွန်စွာ လည်ပတ်နိုင်စေရန် အထောက်အကူဖြစ်ပါသည်။

### ပတ်ဝန်းကျင် အပြောင်းအလဲများ

1. Root directory တွင် `.env.template` ကို ကူးယူ၍ `.env` ဖိုင်တစ်ခု ဖန်တီးပါ။
2. ပတ်ဝန်းကျင် အပြောင်းအလဲများကို ညွှန်ကြားချက်အတိုင်း ဖြည့်စွက်ပါ။

> [!TIP]
>
> ### ဖွံ့ဖြိုးတိုးတက်ရေး ပတ်ဝန်းကျင် အခြားရွေးချယ်စရာများ
>
> ပရောဂျက်ကို ဒေသခံတွင် လည်ပတ်ခြင်းအပြင် GitHub Codespaces သို့မဟုတ် VS Code Dev Containers ကိုလည်း အသုံးပြုနိုင်ပါသည်။
>
> #### GitHub Codespaces
>
> GitHub Codespaces ကို အသုံးပြု၍ ဤနမူနာများကို အွန်လိုင်းတွင် လည်ပတ်နိုင်ပြီး ထပ်မံ ပြင်ဆင်ရန် သို့မဟုတ် စီမံခန့်ခွဲရန် မလိုအပ်ပါ။
>
> ခလုတ်ကို နှိပ်လျှင် သင်၏ browser တွင် web-based VS Code instance တစ်ခု ဖွင့်ပေးပါလိမ့်မည်။
>
> 1. Template ကို ဖွင့်ပါ (အချိန်အနည်းငယ် ကြာနိုင်သည်) -
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### VS Code Dev Containers ဖြင့် ဒေသခံတွင် လည်ပတ်ခြင်း
>
> ⚠️ ဤရွေးချယ်စရာသည် သင်၏ Docker Desktop တွင် အနည်းဆုံး 16 GB RAM ခန့်သတ်ထားမှသာ လည်ပတ်နိုင်ပါသည်။ RAM 16 GB ထက်နည်းပါက [GitHub Codespaces ရွေးချယ်စရာ](../..) သို့မဟုတ် [ဒေသခံတွင် ပြင်ဆင်ခြင်း](../..) ကို စမ်းသပ်နိုင်ပါသည်။
>
> VS Code Dev Containers သည် [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) ကို အသုံးပြု၍ ဒေသခံ VS Code တွင် ပရောဂျက်ကို ဖွင့်ပေးပါသည်။
>
> 1. Docker Desktop ကို စတင်ပါ (မရှိသေးပါက ထည့်သွင်းပါ)
> 2. ပရောဂျက်ကို ဖွင့်ပါ -
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

### ကုဒ်ပုံစံ

ကျွန်ုပ်တို့သည် ပရောဂျက်အတွင်း Python ကုဒ်ပုံစံကို တစ်သွေ့တစ်ပြား ထိန်းသိမ်းရန် [Black](https://github.com/psf/black) ကို အသုံးပြုပါသည်။ Black သည် Python ကုဒ်ကို အလိုအလျောက် ပြန်လည်ဖော်ပြပေးသော အတင်းအကျပ် code formatter ဖြစ်သည်။

#### ဖွဲ့စည်းမှု

Black ဖွဲ့စည်းမှုကို ကျွန်ုပ်တို့၏ `pyproject.toml` တွင် သတ်မှတ်ထားပါသည်။

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```


#### Black ထည့်သွင်းခြင်း

Poetry (အကြံပြု) သို့မဟုတ် pip ဖြင့် Black ကို ထည့်သွင်းနိုင်ပါသည်။

##### Poetry အသုံးပြုခြင်း

ဖွံ့ဖြိုးတိုးတက်ရေး ပတ်ဝန်းကျင် စတင်ပြင်ဆင်သည့်အခါ Black ကို အလိုအလျောက် ထည့်သွင်းပါသည်။

```bash
poetry install
```


##### pip အသုံးပြုခြင်း

pip အသုံးပြုပါက Black ကို တိုက်ရိုက် ထည့်သွင်းနိုင်ပါသည်။

```bash
pip install black
```


#### Black အသုံးပြုခြင်း

##### Poetry ဖြင့်

1. ပရောဂျက်ရှိ Python ဖိုင်အားလုံးကို ဖော်မတ်လုပ်ပါ။

    ```bash
    poetry run black .
    ```


2. ဖိုင် သို့မဟုတ် directory တစ်ခုကို ဖော်မတ်လုပ်ပါ။

    ```bash
    poetry run black path/to/file_or_directory
    ```


##### pip ဖြင့်

1. ပရောဂျက်ရှိ Python ဖိုင်အားလုံးကို ဖော်မတ်လုပ်ပါ။

    ```bash
    black .
    ```


2. ဖိုင် သို့မဟုတ် directory တစ်ခုကို ဖော်မတ်လုပ်ပါ။

    ```bash
    black path/to/file_or_directory
    ```


> [!TIP]
> သင်၏ editor ကို Black ဖြင့် ကုဒ်ကို သိမ်းဆည်းသည့်အချိန် အလိုအလျောက် ဖော်မတ်လုပ်ရန် ပြင်ဆင်ရန် အကြံပြုပါသည်။ မော်ဒန် editor များအများစုသည် extension သို့မဟုတ် plugin များဖြင့် ထောက်ပံ့ပါသည်။

## Co-op Translator ကို လည်ပတ်ခြင်း

သင်၏ ပတ်ဝန်းကျင်တွင် Poetry ဖြင့် Co-op Translator ကို လည်ပတ်ရန် အောက်ပါအဆင့်များကို လိုက်နာပါ။

1. ဘာသာပြန် စမ်းသပ်လိုသော directory သို့ သွားပါ၊ သို့မဟုတ် စမ်းသပ်ရန် အချိန်ပိုင်း folder တစ်ခု ဖန်တီးပါ။

2. အောက်ပါ command ကို အကောင်အထည်ဖော်ပါ။ `-l ko` ကို သင်ဘာသာပြန်လိုသော ဘာသာစကားကုဒ်ဖြင့် အစားထိုးပါ။ `-d` flag သည် debug mode ကို ဆိုလိုသည်။

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```


> [!NOTE]
> command ကို လည်ပတ်မည့်အခါ သင်၏ Poetry ပတ်ဝန်းကျင် (poetry shell) ဖွင့်ထားရန် သေချာပါစေ။

## ဘာသာစကားအသစ် တစ်ခု ထည့်သွင်းရန်

ဘာသာစကားအသစ်များ ထည့်သွင်းရန် အထောက်အပံ့များကို ကြိုဆိုပါသည်။ PR တင်မည့်အရင် အောက်ပါအဆင့်များကို ပြီးမြောက်စေရန် လိုအပ်ပါသည်။

1. Font mapping တွင် ဘာသာစကားကို ထည့်ပါ
   - `src/co_op_translator/fonts/font_language_mappings.yml` ကို ပြင်ဆင်ပါ
   - အောက်ပါအချက်များဖြင့် entry တစ်ခု ထည့်ပါ -
     - `code`: ISO-ပုံစံ ဘာသာစကားကုဒ် (ဥပမာ - `vi`)
     - `name`: လူသိများသော ပြသမည့်အမည်
     - `font`: `src/co_op_translator/fonts/` တွင် ပါဝင်ပြီး စာလုံးပုံစံကို ထောက်ပံ့သော font
     - `rtl`: ညာမှ ဘယ်သို့ဖတ်သည်ဆိုပါက `true`၊ မဟုတ်ပါက `false`

2. လိုအပ်ပါက font ဖိုင်များ ထည့်သွင်းပါ
   - အသစ်သော font လိုအပ်ပါက open source ဖြန့်ဝေမှုအတွက် လိုင်စင်ကို စစ်ဆေးပါ
   - font ဖိုင်ကို `src/co_op_translator/fonts/` ထဲသို့ ထည့်ပါ

3. ဒေသခံ စစ်ဆေးခြင်း
   - နမူနာအသေးစားများ (Markdown, ပုံများ၊ notebook များ) အတွက် ဘာသာပြန်မှုများ လည်ပတ်ပါ
   - output မှန်ကန်စွာ ပြသနေမှု၊ font များနှင့် RTL layout (လိုအပ်ပါက) စစ်ဆေးပါ

4. စာရွက်စာတမ်းများ ပြင်ဆင်ခြင်း
   - ဘာသာစကားသည် `getting_started/supported-languages.md` တွင် ပါဝင်ရန် သေချာစေပါ
   - `getting_started/README_languages_template.md` တွင် မပြောင်းလဲရပါ၊ ၎င်းသည် supported list မှ အလိုအလျောက် ဖန်တီးသည်

5. PR တင်ပါ
   - ထည့်သွင်းသော ဘာသာစကားနှင့် font/လိုင်စင်ဆိုင်ရာ အချက်အလက်များ ဖော်ပြပါ
   - ရနိုင်ပါက output screenshot များကို ပူးတွဲပါ

ဥပမာ YAML entry:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


### ဘာသာစကားအသစ် စမ်းသပ်ခြင်း

အောက်ပါ command ဖြင့် ဘာသာစကားအသစ်ကို စမ်းသပ်နိုင်ပါသည်။

```bash
# အတုပတ်ဝန်းကျင်တစ်ခု ဖန်တီးပြီး ဖွင့်ပါ
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# ဖွံ့ဖြိုးရေး ပက်ကေ့ချ်ကို ထည့်သွင်းပါ
pip install -e .
# ဘာသာပြန်ချက်ကို အလုပ်လုပ်ပါ
translate -l "new_lang"
```


## ထိန်းသိမ်းသူများ

### Commit message နှင့် Merge များဆောင်ရွက်မှု မျိုးစုံ

ပရောဂျက်၏ commit သမိုင်းကို တိကျသေချာစေရန်နှင့် ရှင်းလင်းမှုရှိစေရန်၊ **Squash and Merge** မျိုးစုံကို အသုံးပြုသောအခါ **နောက်ဆုံး commit message** အတွက် အောက်ပါပုံစံကို လိုက်နာပါသည်။

PR တစ်ခု merge လုပ်သောအခါ၊ အထူး commit များကို တစ်ခုတည်း commit အဖြစ် squash လုပ်မည်ဖြစ်ပြီး၊ နောက်ဆုံး commit message သည် အောက်ပါပုံစံအတိုင်း ဖြစ်ရမည်။

#### Commit message ပုံစံ (squash and merge အတွက်)

commit message များအတွက် အောက်ပါပုံစံကို အသုံးပြုပါသည်။

```bash
<type>: <description> (#<PR နံပါတ်>)
```


- **type**: commit အမျိုးအစားကို ဖော်ပြသည်။ အောက်ပါအမျိုးအစားများကို အသုံးပြုပါသည် -
  - `Docs`: စာရွက်စာတမ်း ပြင်ဆင်မှုများအတွက်။
  - `Build`: build system သို့မဟုတ် dependency များနှင့် ဆက်စပ်သော ပြောင်းလဲမှုများ၊ configuration ဖိုင်များ၊ CI workflow များ သို့မဟုတ် Dockerfile ပြင်ဆင်မှုများအပါအဝင်။
  - `Core`: ပရောဂျက်၏ အဓိက လုပ်ဆောင်ချက်များ သို့မဟုတ် features များ ပြင်ဆင်မှုများ၊ အထူးသဖြင့် `src/co_op_translator/core` directory တွင်ပါဝင်သော ဖိုင်များ။

- **description**: ပြောင်းလဲမှု အကျဉ်းချုပ် တိုတောင်းစွာ။
- **PR number**: commit နှင့် ဆက်စပ်သော pull request နံပါတ်။

**ဥပမာများ**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> လက်ရှိတွင် **`Docs`**, **`Core`**, နှင့် **`Build`** prefix များကို ပြင်ဆင်ထားသော source code အပေါ် label များအရ PR ခေါင်းစဉ်တွင် အလိုအလျောက် ထည့်သွင်းပေးပါသည်။ မှန်ကန်သော label များ ထည့်သွင်းထားပါက PR ခေါင်းစဉ်ကို ကိုယ်တိုင် ပြင်ဆင်ရန် မလိုအပ်ပါ။ သင်သည် အားလုံးမှန်ကန်ကြောင်းနှင့် prefix များ ထည့်သွင်းထားကြောင်းသာ စစ်ဆေးရုံဖြစ်သည်။

#### Merge မျိုးစုံ

ကျွန်ုပ်တို့သည် pull request များအတွက် **Squash and Merge** ကို ပုံမှန် မျိုးစုံအဖြစ် အသုံးပြုပါသည်။ ဤမော်ဒယ်သည် commit message များကို ကျွန်ုပ်တို့၏ ပုံစံနှင့် ကိုက်ညီစေပါသည်၊ သို့သော် အထူး commit များ မလိုအပ်ပါ။

**အကြောင်းပြချက်များ**:

- သန့်ရှင်းပြီး တန်းတူသော ပရောဂျက် သမိုင်းကြောင်း။
- commit message များတွင် တစ်ညီတစ်မျှ ဖြစ်စေရန်။
- အနည်းငယ်သော commit များ (ဥပမာ - "fix typo") မှ ဖြစ်သော ဆူညံသံ လျော့နည်းစေရန်။

merge လုပ်သောအခါ နောက်ဆုံး commit message သည် အထက်ဖော်ပြထားသည့် commit message ပုံစံနှင့် ကိုက်ညီစေရန် သေချာစေပါ။

**Squash and Merge ၏ ဥပမာ**

PR တစ်ခုတွင် အောက်ပါ commit များပါရှိပါက -

- `fix typo`
- `update README`
- `adjust formatting`

၎င်းတို့ကို squash လုပ်ပြီး -

`Docs: Improve documentation clarity and formatting (#65)`

အဖြစ် ပြောင်းလဲသင့်သည်။

### ထုတ်ပြန်မှု လုပ်ငန်းစဉ်

ဤအပိုင်းတွင် Co-op Translator ၏ ထုတ်ပြန်မှု အသစ်ကို ထုတ်ပြန်ရန် အလွယ်တကူနည်းလမ်းကို ဖော်ပြပါသည်။

#### 1. `pyproject.toml` တွင် ဗားရှင်းကို မြှင့်တင်ခြင်း

1. နောက်ထပ် ဗားရှင်းနံပါတ်ကို ဆုံးဖြတ်ပါ (semantic versioning ကို လိုက်နာသည် - `MAJOR.MINOR.PATCH`)။
2. `pyproject.toml` ကို ပြင်ဆင်ပြီး `[tool.poetry]` အောက်ရှိ `version` ကို ပြောင်းပါ။
3. ဗားရှင်းသာ ပြောင်းလဲထားသော dedicated pull request တစ်ခု ဖွင့်ပါ (lock/metadata ဖိုင်များကို အလိုအလျောက် ပြောင်းလဲပါကပါဝင်နိုင်သည်

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->