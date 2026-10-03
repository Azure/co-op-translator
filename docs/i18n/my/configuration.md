# ဖွဲ့စည်းမှု

Co-op Translator သည် တစ်ခုသော ဘာသာစကား မော်ဒယ် ပံ့ပိုးသူတစ်ဦးကို လိုအပ်သည်။ ဓာတ်ပုံ ဘာသာပြန်ရန် အပိုသဖြင့် Azure AI Vision လည်း လိုအပ်သည်။

ဖွဲ့စည်းမှုကို အခြားပတ်ဝန်းကျင် ဗေရဘယ်များ (environment variables) မှ ဖတ်ယူပါသည်။ ဒေသဆိုင်ရာ ပရောဂျက်များအတွက်၊ ၎င်းမ်ားကို ပရောဂျက်၏ root တွင် `.env` ဖိုင်ထဲထည့်ပါ။

Azure အရင်းအမြစ် ပြင်ဆင်ရန်အတွက်၊ [Azure AI တပ်ဆင်ခြင်း](azure-ai-setup.md) ကို ကြည့်ပါ။

## ဒေသခံ runtime ပြင်ဆင်ခြင်း

CLI ကို ဒေသခံအနေဖြင့် အလုပ်လုပ်စေချိန် မတိုင်မီ virtual environment တစ်ခု အသုံးပြုပါ။ Co-op Translator သည် Python 3.11 မှ 3.14 အထိ အထောက်အပံ့ ပြုသည်။

ရိုးရိုး CLI အသုံးပြုမှုအတွက်၊ ထုတ်ပြန်ထားသော package ကို virtual environment အတွင်း၌ တပ်ဆင်ပါ။

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### Repository ဖွံ့ဖြိုးရေး

Repository ဖွံ့ဖြိုးရေးအတွက်၊ ပရောဂျက် root မှ dependency များကို တပ်ဆင်ပါ။

```bash
poetry install
poetry run translate --help
```

CLI အသုံးပြုနိုင်သွားလျှင် `.env` ထဲတွင် ဘာသာစကား မော်ဒယ် ပံ့ပိုးသူ တစ်ဦးကို ဖော်ပြပါ။

## ပံ့ပိုးသူ ရွေးချယ်မှု

ကိရိယာသည် အောက်ပါ အစဉ်အတိုင်း ပံ့ပိုးသူများကို အလိုအလျောက် တွေ့ရှိသည်။

1. Azure OpenAI
2. OpenAI
3. Anthropic

ဘာသာပြန်ရန်အတွက် ပံ့ပိုးသူ၏ credentials လိုအပ်သည်၊ သို့သော် `translate -l "ko" -md --dry-run` ကဲ့သို့ ရှေ့ပြသချက်များအတွက် မလိုအပ်နိုင်ပါ။ `migrate-links`, `co-op-review`, နှင့် `run_review` များသည် သတ်မှတ်နိုင်သော ထိန်းသိမ်းရေး လုပ်ငန်းများဖြစ်ပြီး ပံ့ပိုးသူ credentials မလိုအပ်ပါ။

## မော်ဒယ် ဖောက်သည် (client) ဘက်အင်

Co-op Translator 0.22.0 မှ စ၍ Azure OpenAI, OpenAI, နှင့် Anthropic များသည် ပုံမှန်အားဖြင့် Microsoft Agent Framework ကို အသုံးပြုသည်။ ပုံမှန် အသုံးပြုမှုအတွက် backend သတ်မှတ်ခြင်း မလိုအပ်ပါ။

Semantic Kernel ကို ကိုက်ညီမှုအတွက် ယာယီ ရရှိနိုင်ဆဲ ဖြစ်သည်။ ထိုကို ထုတ်ဖော်ရွေးချယ်လိုပါက အောက်ပါအတိုင်း သတ်မှတ်ပါ။

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Semantic Kernel အသုံးပြုခြင်းသည် deprecation သတိပေးချက် ထုတ်ပေးမည်။ package သည် Semantic Kernel ကို 0.23.0 တွင် optional dependency အဖြစ် ပြောင်းရွှေ့ရန် နှင့် 0.24.0 တွင် အင်တဂရေးရှင်းကို ဖယ်ရှားရန် စီစဉ်ထားသည်၊ ၎င်းသည် ကိုက်ညီမှုရလဒ်များနှင့် အသုံးပြုသူ သဘောထားပေါ် မူတည်ပါသည်။ Anthropic သည် `agent-framework` ကို လိုအပ်သည်；Anthropic နှင့် အတူ `semantic-kernel` ကို ထူးခြားရွေးချယ်ပါက configuration error ဖြစ်ပေါ်ပါမည်။ မမှန်ကန်သော တန်ဖိုးများသည် provider-backed translator initialization အတွင်းတွင် မအောင်မြင်ဘဲ ရပ်တန့်ကြောင်းဖြစ်သည်။ rollout ကို လိုက်နာပြီး အတားအဆီးများကို [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543) တွင် အစီရင်ခံပါ။

## Azure OpenAI

မော်ဒယ်ကို Azure AI Foundry သို့မဟုတ် Azure OpenAI Service တွင် တပ်ဆင်ထားပါက Azure OpenAI ကို အသုံးပြုပါ။

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

ဘာသာပြန်မှု စတင်မီ ဆက်သွယ်နိုင်မှု စစ်ဆေးမှုသည် endpoint, API key, API version, နှင့် deployment name များကို အသုံးပြုသည်။

## OpenAI

OpenAI API ကို တိုက်ရိုက် ခေါ်ယူသောအခါ OpenAI ကို အသုံးပြုပါ။

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` လိုအပ်ပါသည်၊ အကြောင်းမှာ translator သည် API ခေါ်ဆိုမှုများအတွက် ထူးခြားသတ်မှတ်ထားသည့် chat model တစ်ခုကို လိုအပ်သောကြောင့် ဖြစ်သည်။

ပုံမှန် စနစ်အတွက် `OPENAI_ORG_ID` နှင့် `OPENAI_BASE_URL` ကို မသတ်မှတ်ထားရ။ သင့်အကောင့်အတွက် organization ID လိုအပ်ပါကသာ ထည့်ပါ၊ custom endpoint အသုံးပြုနေပါကသာ base URL ကို သတ်မှတ်ပါ။ ရွေးချယ်နိုင်သည့် settings များအတွက် placeholder တန်ဖိုးများကို မကူးယူပါနှင့်။

## Anthropic Claude

Claude API ကို တိုက်ရိုက် ခေါ်ယူချိန် Anthropic ကို အသုံးပြုပါ။ [Anthropic API key](https://platform.claude.com/docs/en/get-started) တစ်ခု ဖန်တီးပြီး သင့်ကိုက်ညီသော [Claude model ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) ကို ရွေးချယ်ပါ။

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` နှင့် `ANTHROPIC_MODEL` လိုအပ်ပါသည်။ `CO_OP_TRANSLATOR_MODEL_CLIENT` ကို သတ်မှတ်ရန် မလိုအပ်ပါ။ Agent Framework သည် ပုံမှန် backend ဖြစ်သည်။

Anthropic API အတွက် `ANTHROPIC_BASE_URL` ကို မသတ်မှတ်ထားပါ။ custom endpoint အသုံးပြုနေပါကသာ သတ်မှတ်ပါ။

`ANTHROPIC_MAX_TOKENS` သည် ပုံမှန်အားဖြင့် `8192` ဖြစ်ပြီး Meitei Mayek ကဲ့သည့် token များထူသော စာလုံးစနစ်များအတွက် အနေအထား ထားပါသည်။ သင့်မော်ဒယ် သို့မဟုတ် Anthropic-ကိုက်ညီသည့် endpoint က ထုတ်လွှင့်မည့် output ကို ထိုအောက်သို့ ကန့်သတ်ထားပါက ဤတန်ဖိုးကို လျှော့ချပါ။

## Azure AI Vision

ပုံ ဘာသာပြန်ခြင်းအတွက် Azure AI Vision လိုအပ်သည်၊ ကိရိယာသည် မော်ဒယ်ဖြင့် ဘာသာပြန်မလုပ်မီ ပုံများမှ စာသားကို ဆွဲယူနိုင်ရန် အလိုအလျောက် အလုပ်လုပ်သည်။ Anthropic သည် ဆွဲယူထားသော စာသားကို Azure OpenAI သို့ OpenAI ကဲ့သို့ တူညီစွာ ဘာသာပြန်နိုင်သည်။

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

ပုံ ဘာသာပြန်ခြင်းကို `-img`, `images=True`, သို့မဟုတ် content-type filter မရှိသည့် အခြေအနေဖြင့် ရွေးချယ်ပါက tool သည် ဘာသာပြန်မှု စတင်မီ Vision ဖွဲ့စည်းမှုကို သေချာစစ်ဆေးပါသည်။

## များစွာသော credential စုံများ

ဖွဲ့စည်းမှု အလွှာသည် တူညီသည့် index ဖြင့် variable များကို suffix ချ၍ credential စုံများကို ထောက်ပံ့သည်။

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

အစုတိုင်းသည် ပြည့်စုံရမည်။ health check သည် ဘာသာပြန်ရေး စတင်မီ အလုပ်လုပ်နိုင်သည့် အစုတစ်ခုကို ရွေးချယ်ပါသည်။

OpenAI နှင့် Anthropic များသည် တူညီသော suffix စည်းမျဉ်းကို ထောက်ခံသည်။ credential အစုတစ်စုရှိ variable အားလုံးကို တူညီသော suffix ပေါ်တွင် ထားပါ၊ `OPENAI_BASE_URL_1` သို့မဟုတ် `ANTHROPIC_BASE_URL_1` ကဲ့သို့ ရွေးချယ်နိုင်သည့် တန်ဖိုးများကိုပါ ထားပါ။

## ကမန်ဒ် လိုအပ်ချက်များ

| Command သို့ API | LLM လိုအပ်သလား | Vision လိုအပ်သလား | မှတ်ချက်များ |
| --- | --- | --- | --- |
| `translate -md` | ဟုတ် | မဟုတ် | Markdown ကိုသာ ဘာသာပြန်သည်။ |
| `translate -nb` | ဟုတ် | မဟုတ် | Notebooks များကိုသာ ဘာသာပြန်သည်။ |
| `translate -img` | ဟုတ် | ဟုတ် | ပုံများကိုသာ ဘာသာပြန်သည်။ |
| `translate` with no type flags | ဟုတ် | ဟုတ် | ပုံမှန် mode သည် Markdown, notebooks, နှင့် images များကို ပါဝင်စေသည်။ |
| `evaluate` | ဟုတ် | မဟုတ် | `--fast` ရွေးချယ်ထားခြင်းမရှိပါက LLM အခြေခံ အကဲဖြတ်မှုကို အသုံးပြုသည်။ |
| `migrate-links` | မဟုတ် | မဟုတ် | provider ခေါ်ဆိုမှု မရှိဘဲ ဒေသန္တရ link ပြောင်းရွှေ့မှုကို ဆောင်ရွက်သည်။ |
| `co-op-review` | မဟုတ် | မဟုတ် | သတ်မှတ်နိုင်သော ဘာသာပြန် ဖွဲ့စည်းမှု၊ အသစ်ရှိမှု စစ်ဆေးမှု၊ Markdown၊ notebook နှင့် ဒေသန္တရ link စစ်ဆေးမှုများကို ဆောင်ရွက်သည်။ |
| `run_translation(markdown=True)` | ဟုတ် | မဟုတ် | ပရိုဂရမ်တစ်ဆင့် Markdown ဘာသာပြန်ခြင်း။ |
| `run_translation(images=True)` | ဟုတ် | ဟုတ် | ပရိုဂရမ်တစ်ဆင့် ပုံ ဘာသာပြန်ခြင်း။ |
| `run_review(...)` | မဟုတ် | မဟုတ် | ပရိုဂရမ်တစ်ဆင့် သတ်မှတ်နိုင်သော ပြန်လည်သုံးသပ်မှု။ |

## ထွက်ဖိုလ်ဒါများ

ပုံမှန် စာသား ဘာသာပြန် ထုတ်လွှင့်ချက်:

```text
translations/<language-code>/<source-relative-path>
```

ပုံမှန် ဘာသာပြန်ပြီး ပုံ ထွက်ရှိမှု:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API သည် `translations_dir` နှင့် `image_dir` များဖြင့် ဤ ဖိုလ်ဒါများကို override လုပ်နိုင်သည်။