<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:38:26+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "my"
}
-->
# Co-op translator package ကို တပ်ဆင်ခြင်း

**Co-op Translator** သည် command-line interface (CLI) ကိရိယာတစ်ခုဖြစ်ပြီး သင်၏ project ထဲရှိ markdown ဖိုင်များနှင့် ပုံများအားလုံးကို မျိုးစုံဘာသာစကားများသို့ ဘာသာပြန်ရာတွင် ကူညီပေးရန် ရည်ရွယ်ထားသည်။ ဤသင်ခန်းစာတွင် translator ကို စီမံကိန်းပြုလုပ်ခြင်းနှင့် အမျိုးမျိုးသော အသုံးပြုမှုအတွက် ပြေးဆွဲခြင်းကို လမ်းညွှန်ပေးပါမည်။

### virtual environment တစ်ခု ဖန်တီးခြင်း

virtual environment ကို `pip` သို့မဟုတ် `Poetry` ဖြင့် ဖန်တီးနိုင်သည်။ Terminal အတွင်း အောက်ပါ command များထဲမှ တစ်ခုကို ရိုက်ထည့်ပါ။

#### pip အသုံးပြုခြင်း

```bash
python -m venv .venv
```

#### Poetry အသုံးပြုခြင်း

```bash
poetry init
```

### virtual environment ကို ဖွင့်ခြင်း

virtual environment ဖန်တီးပြီးပါက၊ အဲဒါကို ဖွင့်ရပါမည်။ သင်၏ operating system အလိုက် လုပ်ဆောင်ရမည့် နည်းလမ်းကွာခြားသည်။ Terminal အတွင်း အောက်ပါ command ကို ရိုက်ထည့်ပါ။

#### pip နှင့် Poetry နှစ်ခုလုံးအတွက်

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry အသုံးပြုခြင်း

1. Poetry ဖြင့် environment ဖန်တီးထားပါက၊ Terminal အတွင်း အောက်ပါ command ကို ရိုက်ထည့်၍ ဖွင့်ပါ။

    ```bash
    poetry shell
    ```

### Package နှင့် လိုအပ်သော Packages များ တပ်ဆင်ခြင်း

virtual environment ကို စတင်ဖန်တီးပြီး ဖွင့်ပြီးပါက လိုအပ်သော dependencies များကို တပ်ဆင်ရန် နောက်တစ်ဆင့်ဖြစ်သည်။

### အမြန်တပ်ဆင်ခြင်း

Co-Op Translator ကို pip ဖြင့် တပ်ဆင်ပါ

```
pip install co-op-translator
```
သို့မဟုတ်

poetry ဖြင့် တပ်ဆင်ပါ
```
poetry add co-op-translator
```

#### pip အသုံးပြုခြင်း (requirements.txt မှ) ဤ repo ကို clone လုပ်ပါက

![NOTE] quick install ဖြင့် co-op translator ကို တပ်ဆင်ပါက ဤနည်းကို မသုံးပါနှင့်။

1. pip အသုံးပြုပါက Terminal အတွင်း အောက်ပါ command ကို ရိုက်ထည့်ပါ။ `requirements.txt` ဖိုင်တွင် ဖော်ပြထားသော လိုအပ်သော package များကို အလိုအလျောက် တပ်ဆင်ပေးပါလိမ့်မည်။

    ```bash
    pip install -r requirements.txt
    ```

#### Poetry အသုံးပြုခြင်း (pyproject.toml မှ)

1. Poetry အသုံးပြုပါက Terminal အတွင်း အောက်ပါ command ကို ရိုက်ထည့်ပါ။ `pyproject.toml` ဖိုင်တွင် ဖော်ပြထားသော လိုအပ်သော package များကို အလိုအလျောက် တပ်ဆင်ပေးပါလိမ့်မည်။

    ```bash
    poetry install
    ```

**တာဝန်မခံချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် တောင်းဆိုအပ်ပါသည်။ မူလစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင် အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော သတင်းအချက်အလက်များအတွက်တော့ လူမှု့အရည်အချင်းရှိ ဘာသာပြန်သူများမှ ဘာသာပြန်ပေးခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် မမှန်မကန် နားလည်မှုများ သို့မဟုတ် မှားယွင်းချက်များအတွက် ကျွန်ုပ်တို့တာဝန်မခံပါ။