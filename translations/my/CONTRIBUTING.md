<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T13:32:16+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "my"
}
-->
# Co-op Translator တွင် ပါဝင်ဆောင်ရွက်ခြင်း

ဒီပရောဂျက်မှာ ဝေမျှမှုများနဲ့ အကြံပြုချက်တွေကို ကြိုဆိုပါတယ်။ ဝေမျှမှုအများစုအတွက် သင်မှာ သင့်ရဲ့ ဝေမျှမှုကို အသုံးပြုခွင့်ရှိကြောင်းနှင့် လက်တွေ့အသုံးပြုခွင့်ပေးကြောင်း ကြေညာထားတဲ့ Contributor License Agreement (CLA) ကို သဘောတူရပါမယ်။ အသေးစိတ်အချက်အလက်များအတွက် https://cla.opensource.microsoft.com ကို သွားရောက်ကြည့်ရှုနိုင်ပါသည်။

သင် pull request တင်တဲ့အခါ CLA bot က သင့်မှာ CLA ပေးရန်လိုအပ်မရှိမရှိကို အလိုအလျောက်စစ်ဆေးပြီး PR ကို သင့်တော်စွာ ဖော်ပြပေးပါလိမ့်မယ် (ဥပမာ - status check, comment)။ bot ရဲ့ ညွှန်ကြားချက်တွေကို လိုက်နာရုံပါပဲ။ CLA သုံးသော repo အားလုံးအတွက် တစ်ကြိမ်တည်းပဲ ပြုလုပ်ရပါမယ်။

## ဖွံ့ဖြိုးရေးပတ်ဝန်းကျင် စတင်ပြင်ဆင်ခြင်း

ဒီပရောဂျက်အတွက် ဖွံ့ဖြိုးရေးပတ်ဝန်းကျင်ကို စတင်ဖို့ dependency များကို စီမံခန့်ခွဲရန် Poetry ကို အသုံးပြုဖို့ အကြံပြုပါတယ်။ `pyproject.toml` ကို project dependency များ စီမံရန် အသုံးပြုသဖြင့် dependency များကို install လုပ်ရန် Poetry ကို အသုံးပြုသင့်ပါသည်။

### Virtual environment တစ်ခု ဖန်တီးခြင်း

#### pip ဖြင့်

```bash
python -m venv .venv
```

#### Poetry ဖြင့်

```bash
poetry init
```

### Virtual environment ကို အက်တီဗိတ်လုပ်ခြင်း

#### pip နဲ့ Poetry နှစ်ခုလုံးအတွက်

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry ဖြင့်

```bash
poetry shell
```

### Package နှင့် လိုအပ်သော Packages များ တပ်ဆင်ခြင်း

#### Poetry ဖြင့် (pyproject.toml မှ)

```bash
poetry install
```

### လက်တွေ့ စမ်းသပ်ခြင်း

PR တင်ခွင့်မပြုမီ အမှန်တကယ်ရှိတဲ့ စာရွက်စာတမ်းတွေနဲ့ ဘာသာပြန်လုပ်ဆောင်မှုကို စမ်းသပ်ခြင်း အရေးကြီးပါတယ်။

1. root directory ထဲမှာ test directory တစ်ခု ဖန်တီးပါ။
    ```bash
    mkdir test_docs
    ```

2. ဘာသာပြန်လိုသော markdown စာရွက်စာတမ်းများနှင့် ပုံများကို test directory ထဲကို ကူးထည့်ပါ။ ဥပမာ -
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. package ကို ကိုယ်ပိုင်စက်ပေါ်တွင် တပ်ဆင်ပါ။
    ```bash
    pip install -e .
    ```

4. သင့် စမ်းသပ်စာရွက်စာတမ်းများတွင် Co-op Translator ကို အလုပ်လုပ်ပါ။
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. ဘာသာပြန်ပြီးသော ဖိုင်များကို `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` ဖိုင်ထဲမှာ စစ်ဆေးပါ။
1. environment variable များကို ညွှန်ကြားချက်အတိုင်း ဖြည့်စွက်ပါ။

> [!TIP]
>
> ### ဖွံ့ဖြိုးရေးပတ်ဝန်းကျင် အပိုရွေးချယ်စရာများ
>
> ပရောဂျက်ကို ကိုယ်ပိုင်စက်ပေါ်တွင်သာမက GitHub Codespaces သို့မဟုတ် VS Code Dev Containers ကိုလည်း အသုံးပြုနိုင်ပါတယ်။
>
> #### GitHub Codespaces
>
> GitHub Codespaces ကို အသုံးပြု၍ ဒီ sample များကို အွန်လိုင်းမှာ အလုပ်လုပ်စေလိုက်ပြီး ထပ်မံပြင်ဆင်ခြင်း သို့မဟုတ် စက်ပေါ်တွင် အဆင်ပြေစွာ မလိုအပ်ပါ။
>
> အောက်ပါ ခလုတ်က သင့် browser မှာ web-based VS Code ကို ဖွင့်ပေးပါလိမ့်မယ်။
>
> 1. Template ကို ဖွင့်ပါ (အချိန်အနည်းငယ်ယူနိုင်သည်) -
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### VS Code Dev Containers ဖြင့် ကိုယ်ပိုင်စက်ပေါ်တွင် အလုပ်လုပ်ခြင်း
>
> ⚠️ ဒီရွေးချယ်မှုကို အသုံးပြုရန် Docker Desktop သည် အနည်းဆုံး 16 GB RAM ကို ချမှတ်ထားရပါမည်။ RAM 16 GB ထက်နည်းပါက [GitHub Codespaces ရွေးချယ်မှု](../..) သို့မဟုတ် [ကိုယ်ပိုင်စက်တွင် စတင်ပြင်ဆင်ခြင်း](../..) ကို ကြိုးစားကြည့်ပါ။
>
> VS Code Dev Containers သည် Dev Containers extension ကို အသုံးပြု၍ ကိုယ်ပိုင် VS Code မှာ ပရောဂျက်ကို ဖွင့်ပေးပါသည်။
>
> 1. Docker Desktop ကို စတင်ပါ (မရှိသေးလျှင် install လုပ်ပါ)
> 2. ပရောဂျက်ကို ဖွင့်ပါ -
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Code စတိုင်

ပရောဂျက်တစ်ခုလုံးတွင် code စတိုင်ကို တူညီစေရန် Python code formatter အဖြစ် [Black](https://github.com/psf/black) ကို အသုံးပြုပါတယ်။ Black သည် Python code ကို အလိုအလျောက် ပြင်ဆင်ပေးပြီး Black စတိုင်အတိုင်း ပြောင်းလဲပေးသော code formatter ဖြစ်သည်။

#### ဖော်ပြချက်

Black ဖော်ပြချက်ကို `pyproject.toml` ထဲတွင် သတ်မှတ်ထားသည်။

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black ကို တပ်ဆင်ခြင်း

Poetry (အကြံပြု) သို့မဟုတ် pip ဖြင့် Black ကို တပ်ဆင်နိုင်ပါသည်။

##### Poetry ဖြင့်

ဖွံ့ဖြိုးရေးပတ်ဝန်းကျင် စတင်ပြင်ဆင်တဲ့အခါ Black ကို အလိုအလျောက် တပ်ဆင်ပေးပါသည်။
```bash
poetry install
```

##### pip ဖြင့်

pip အသုံးပြုပါက Black ကို တိုက်ရိုက် တပ်ဆင်နိုင်ပါသည်။
```bash
pip install black
```

#### Black ကို အသုံးပြုခြင်း

##### Poetry ဖြင့်

1. ပရောဂျက်အတွင်းရှိ Python ဖိုင်အားလုံးကို format လုပ်ရန် -
    ```bash
    poetry run black .
    ```

2. ဖိုင် သို့မဟုတ် directory တစ်ခုကို သီးသန့် format လုပ်ရန် -
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip ဖြင့်

1. ပရောဂျက်အတွင်းရှိ Python ဖိုင်အားလုံးကို format လုပ်ရန် -
    ```bash
    black .
    ```

2. ဖိုင် သို့မဟုတ် directory တစ်ခုကို သီးသန့် format လုပ်ရန် -
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> ကွန်ပျူတာတွင် Black ဖြင့် code ကို အလိုအလျောက် format လုပ်ဖို့ editor ကို ပြင်ဆင်ထားရန် အကြံပြုပါတယ်။ ယနေ့ခေတ် editor များမှာ extension သို့မဟုတ် plugin များဖြင့် ဒီလိုလုပ်နိုင်ပါသည်။

## Co-op Translator ကို အလုပ်လုပ်စေခြင်း

Poetry ကို အသုံးပြု၍ Co-op Translator ကို သင့်ပတ်ဝန်းကျင်တွင် အလုပ်လုပ်စေလိုပါက အောက်ပါအဆင့်များကို လိုက်နာပါ။

1. ဘာသာပြန်စမ်းသပ်မှုများ ပြုလုပ်လိုသော directory သို့ သို့မဟုတ် စမ်းသပ်ရန် အခမဲ့ folder တစ်ခု ဖန်တီးပါ။

2. အောက်ပါ command ကို အလုပ်လုပ်ပါ။ `-l ko` with the language code you wish to translate into. The `-d` flag သည် debug mode ကို ဆိုလိုသည်။

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Command လုပ်ဆောင်မည့်အခါ သင့် Poetry environment ကို အက်တီဗိတ်လုပ်ထားရန် (poetry shell) သေချာပါစေ။

## ထိန်းသိမ်းသူများ

### Commit message နှင့် Merge များလုပ်နည်း

ပရောဂျက် commit သမိုင်းမှာ တိကျရှင်းလင်းမှုရှိစေရန်အတွက် Squash and Merge များလုပ်တဲ့အခါ အဆုံး commit message အတွက် အထူး format ကိုလိုက်နာပါတယ်။

pull request (PR) တစ်ခု merge လုပ်သောအခါ၊ အခြား commit များအားလုံးကို single commit တစ်ခုအဖြစ် squash လုပ်မည်ဖြစ်ပြီး အဆုံး commit message ကို အောက်ပါ format အတိုင်း ရေးသားရပါမည်။

#### Commit message format (squash and merge အတွက်)

commit message များအတွက် အောက်ပါ format ကို အသုံးပြုပါသည် -

```bash
<type>: <description> (#<PR number>)
```

- **type**: commit အမျိုးအစားကို ဖော်ပြသည်။ အောက်ပါ အမျိုးအစားများကို အသုံးပြုသည် -
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

**တစ်ဖန်ကြေညာချက်**  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းပါသော်လည်း၊ စက်ရုပ်ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် အကြောင်းကြားအပ်ပါသည်။ မူရင်းစာရွက်စာတမ်းကို မိမိဘာသာစကားဖြင့် အတည်ပြုရမည့် အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်သူမှ လုပ်ဆောင်သည့် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှု အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်လာသော နားလည်မှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။