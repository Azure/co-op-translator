<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T04:13:49+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "my"
}
-->
# Co-op Translator package ကို တပ်ဆင်ခြင်း

**Co-op Translator** ဆိုတာက command-line interface (CLI) tool တစ်ခုဖြစ်ပြီး၊ သင့် project ထဲမှာရှိတဲ့ markdown ဖိုင်တွေနဲ့ image တွေကို ဘာသာစကားအမျိုးမျိုးသို့ ဘာသာပြန်နိုင်အောင် အထောက်အပံ့ပေးပါတယ်။ ဒီသင်ခန်းစာမှာ Translator ကို စနစ်တကျ ပြင်ဆင်သုံးစွဲနည်းနဲ့ အသုံးပြုနည်းတွေကို လမ်းညွှန်ပေးပါမယ်။

### Virtual environment တစ်ခု ဖန်တီးပါ

`pip` သို့မဟုတ် `Poetry` ကို အသုံးပြုပြီး virtual environment တစ်ခု ဖန်တီးနိုင်ပါတယ်။ Terminal ထဲမှာ အောက်ပါ command များထဲမှ တစ်ခုကို ရိုက်ထည့်ပါ။

#### pip အသုံးပြုခြင်း

```bash
python -m venv .venv
```

#### Poetry အသုံးပြုခြင်း

```bash
poetry init
```

### Virtual environment ကို အသက်သွင်းပါ

Virtual environment ကို ဖန်တီးပြီးနောက်မှာ အသက်သွင်းဖို့ လိုအပ်ပါတယ်။ Operating system ပေါ်မူတည်ပြီး လုပ်ဆောင်နည်းက မတူနိုင်ပါတယ်။ Terminal ထဲမှာ အောက်ပါ command ကို ရိုက်ထည့်ပါ။

#### pip နဲ့ Poetry နှစ်ခုလုံးအတွက်

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry အသုံးပြုခြင်း

1. Poetry နဲ့ environment ကို ဖန်တီးထားလျှင်၊ Terminal ထဲမှာ အောက်ပါ command ကို ရိုက်ထည့်ပြီး အသက်သွင်းပါ။

    ```bash
    poetry shell
    ```

### Package နဲ့ လိုအပ်တဲ့ Packages များ တပ်ဆင်ခြင်း

Virtual environment ကို ပြင်ဆင်ပြီး အသက်သွင်းပြီးနောက်မှာ လိုအပ်တဲ့ dependencies များကို တပ်ဆင်ရပါမယ်။

### အလွယ်တကူ တပ်ဆင်ခြင်း

Co-Op Translator ကို pip နဲ့ တပ်ဆင်ပါ

```
pip install co-op-translator
```
သို့မဟုတ် 

Poetry နဲ့ တပ်ဆင်ပါ
```
poetry add co-op-translator
```

#### pip (requirements.txt မှတစ်ဆင့်) အသုံးပြုခြင်း - ဒီ repo ကို clone လုပ်ထားလျှင်

> [!NOTE]
> Co-op translator ကို quick install နဲ့ တပ်ဆင်ထားလျှင် ဒီအဆင့်ကို မလုပ်ပါနဲ့။

1. pip ကို အသုံးပြုလျှင် Terminal ထဲမှာ အောက်ပါ command ကို ရိုက်ထည့်ပါ။ `requirements.txt` ဖိုင်ထဲမှာ ဖော်ပြထားတဲ့ လိုအပ်တဲ့ packages များကို အလိုအလျောက် တပ်ဆင်ပေးပါမယ်။

    ```bash
    pip install -r requirements.txt
    ```

#### Poetry (pyproject.toml မှတစ်ဆင့်) အသုံးပြုခြင်း

1. Poetry ကို အသုံးပြုလျှင် Terminal ထဲမှာ အောက်ပါ command ကို ရိုက်ထည့်ပါ။ `pyproject.toml` ဖိုင်ထဲမှာ ဖော်ပြထားတဲ့ လိုအပ်တဲ့ packages များကို အလိုအလျောက် တပ်ဆင်ပေးပါမယ်။

    ```bash
    poetry install
    ```

---

**ဝေဖန်ချက်**:
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းသည် မူလဘာသာစကားဖြင့် အာဏာရှိသောရင်းမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသောအချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားခြင်း သို့မဟုတ် အဓိပ္ပါယ်မှားခြင်းများအတွက် ကျွန်ုပ်တို့သည် တာဝန်ယူမည်မဟုတ်ပါ။