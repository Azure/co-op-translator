# ဆက်တင်များ

Co-op Translator သည် တစ်ခုသော ဘာသာစကား မော်ဒယ် ပရိုဗိုင်းဒါကိုလိုအပ်သည်။ ပုံ (image) ဘာသာပြန်ခြင်းအတွက် အပိုként Azure AI Vision လည်း လိုအပ်သည်။

Configuration သည် environment variables တွေမှ ဖတ်ယူထားသည်။ ဒေသတွင်း ပရောဂျက်များအတွက်၊ ပရောဂျက် root တွင် `.env` ဖိုင်ထည့်ထားပါ။

Azure အရင်းအမြစ် စီစဉ်ခြင်းအတွက် [Azure AI ပြင်ဆင်ခြင်း](azure-ai-setup.md) ကို ကြည့်ပါ။

## ဒေသခံ runtime တပ်ဆင်ခြင်း

CLI ကို ဒေသခံအနေဖြင့် run မပြုမီ virtual environment တစ်ခုကို အသုံးပြုပါ။ Co-op Translator သည် Python 3.10 မှ 3.12 အထိ တိုက်ဆိုင်ပါသည်။

ပုံမှန် CLI အသုံးပြုမှုအတွက်၊ ထုတ်ဝေထားသော package ကို virtual environment အတွင်း install လုပ်ပါ။

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

Repository အတွက် ဖွံ့ဖြိုးမှုလုပ်နေစဉ်တွင် သာမန်အားဖြင့် project root မှ dependency များကို install လုပ်ပါ။

```bash
poetry install
poetry run translate --help
```

CLI အသုံးချနိုင်သွားပါက `.env` တွင် တစ်ခုသော ဘာသာစကား မော်ဒယ် ပရိုဗိုင်းဒါကို ဖော်ပြ ရေးထည့်ပါ။

## ပရိုဗိုင်းဒါ ရွေးချယ်ခြင်း

ကိရိယာသည် အလျင်အမြန် အောက်ပါ အဆင့်စဉ်အတိုင်း ပရိုဗိုင်းဒါများကို auto-detect ပြုလုပ်သည်။

1. Azure OpenAI
2. OpenAI

နှစ်ခုလုံးမှ မရှိဘဲ ဖော်ပြချက် မစုံပါက `translate`, `evaluate`, `migrate-links`, နှင့် `run_translation` များသည် configuration စစ်ဆေးမှုများအတွင်း မအောင်မြင်ပါ။ `co-op-review` နှင့် `run_review` များမှာ သတ်မှတ်နိုင်သော ထိန်းသိမ်းမှု စစ်ဆေးမှုများဖြစ်၍ ပရိုဗိုင်းဒါ ချိတ်ဆက်ချက်များ မလိုအပ်ပါ။

## Azure OpenAI

သင့်မော်ဒယ်ကို Azure AI Foundry သို့မဟုတ် Azure OpenAI Service တွင် deploy လုပ်ထားပါက Azure OpenAI ကို သုံးပါ။

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

ချိတ်ဆက်မှု စစ်ဆေးမှုသည် endpoint၊ API key၊ API version၊ နှင့် deployment name များကို အဆိုပါ ဘာသာပြန်စတင်မည့်မီ စစ်ဆေးသည်။

## OpenAI

OpenAI API ကို တိုက်ရိုက် ခေါ်ယူသောအခါ OpenAI ကို သုံးပါ။

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # မလိုအပ်သော
OPENAI_BASE_URL="..."        # မလိုအပ်သော
```

`OPENAI_CHAT_MODEL_ID` သည် translator သည် API ခေါ်ယူမှုများအတွက် တိတိကျကျ chat model တစ်ခု လိုအပ်သောကြောင့် ပေးရပါမည်။

## Azure AI Vision

ပုံ ဘာသာပြန်ခြင်းအတွက် Azure AI Vision လိုအပ်ပါသည်၊ အကြောင်းမှာ ကိရိယာသည် ပုံထဲမှ စာသားများကို ပထမဦးစွာ ဖြုတ်ယူ၍ ထို့နောက် ဘာသာပြန်နိုင်ရန် ဖြစ်ပါသည်။

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`-img`, `images=True` သို့မဟုတ် content-type filter မရှိပါက ပုံ ဘာသာပြန်ခြင်း ရွေးချယ်ထားသလိုဖြစ်ပါက tool သည် ဘာသာပြန် စတင်မီ Vision configuration ကို စစ်ဆေးပါသည်။

## အတူတကွ credential စုံများ

configuration အလွှာသည် တူညီသော index ဖြင့် variables များကို suffix ထပ်ထည့်ခြင်းဖြင့် အများကြီးသော credential စုံများကို ထောက်ပံ့သည်။

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

စုံတိုင်းသည် ပြည့်စုံနေဖို့ လိုအပ်သည်။ health check သည် အလုပ်လုပ်နိုင်သည့် စုံတစ်ခုကို ရွေးချယ်ပြီး ပြန်လည် ရယူမှ ဘာသာပြန်ခြင်းကို ဆက်လက်လုပ်ဆောင်သည်။

## Command requirements

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | ရှိ | မရှိ | Markdown ဖိုင်များကိုပဲ ဘာသာပြန်သည်။ |
| `translate -nb` | ရှိ | မရှိ | notebook များကိုပဲ ဘာသာပြန်သည်။ |
| `translate -img` | ရှိ | ရှိ | ပုံများကိုပဲ ဘာသာပြန်သည်။ |
| `translate` with no type flags | ရှိ | ရှိ | ပုံမှန်မုဒ်တွင် Markdown၊ notebook များနှင့် ပုံများ ပါဝင်သည်။ |
| `evaluate` | ရှိ | မရှိ | `--fast` ကို ရွေးမထားပါက LLM အကဲဖြတ်ကို အသုံးပြုသည်။ |
| `migrate-links` | ရှိ | မရှိ | လင့်ခ်များကို မိုက်ဂရိတ် ပြုလုပ်သော်လည်း ပူးပေါင်း configuration စစ်ဆေးမှုများကိုလည်း ဆောင်ရွက်သည်။ |
| `co-op-review` | မလိုအပ် | မလိုအပ် | သတ်မှတ်နိုင်သော ဘာသာပြန် ဖွဲ့စည်းပုံ၊ အချက်အလက် အသစ်ဖြစ်မှု (freshness), Markdown, notebook နှင့် ဒေသဆိုင်ရာ လင့်ခ် စစ်ဆေးမှုများကို ပြုလုပ်သည်။ |
| `run_translation(markdown=True)` | ရှိ | မရှိ | ပရိုဂရမ်မှတစ်ဆင့် Markdown ဘာသာပြန်ခြင်း။ |
| `run_translation(images=True)` | ရှိ | ရှိ | ပရိုဂရမ်မှတစ်ဆင့် ပုံ ဘာသာပြန်ခြင်း။ |
| `run_review(...)` | မလိုအပ် | မလိုအပ် | ပရိုဂရမ်မှတစ်ဆင့် သတ်မှတ်ထားနိုင်သော ပြန်လည်သုံးသပ်ခြင်း။ |

## ထွက်ရှိသည့် ဖိုလ်ဒါများ

Default text translation output:

```text
translations/<language-code>/<source-relative-path>
```

Default translated image output:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API သည် `translations_dir` နှင့် `image_dir` ဖြင့် ဤဖိုလ်ဒါများကို အစားထိုး စိတ်ကြိုက် သတ်မှတ်နိုင်ပါသည်။