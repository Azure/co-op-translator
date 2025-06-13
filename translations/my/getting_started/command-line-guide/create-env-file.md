<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:30:06+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "my"
}
-->
# အခြေခံ ဒါရိုက်ထရီမှာ *.env* ဖိုင် ဖန်တီးခြင်း

ဒီသင်ခန်းစာမှာ Azure ဝန်ဆောင်မှုများအတွက် သင့်ရဲ့ environment variables ကို *.env* ဖိုင်တစ်ခုဖြင့် ပြင်ဆင်နည်းကို လမ်းညွှန်ပေးပါမယ်။ Environment variables တွေက API key တွေလို sensitive credential တွေကို သင့်ကုဒ်အတွင်းမှာ မတိုက်ရိုက်ရေးသားဘဲ လုံခြုံစွာ စီမံခန့်ခွဲဖို့ အထောက်အကူပြုပါတယ်။

> [!IMPORTANT]
> - ဘာသာစကားမော်ဒယ် ဝန်ဆောင်မှုတစ်ခု (Azure OpenAI သို့မဟုတ် OpenAI) ကိုသာ ပြင်ဆင်ရပါမယ်။ သင့်နှစ်သက်ရာ ဝန်ဆောင်မှုအတွက် environment variables များဖြည့်ပါ။ ဘာသာစကားမော်ဒယ် အများအပြားအတွက် environment variables များထားရှိပါက co-op translator က ဦးစားပေးမှုအရ တစ်ခုကို ရွေးချယ်ပါလိမ့်မယ်။
> - Computer Vision environment variables မထားရှိပါက translator က အလိုအလျောက် [Markdown-only mode](./markdown-only-mode.md) သို့ ပြောင်းလဲသွားပါလိမ့်မယ်။

> [!NOTE]
> ဒီလမ်းညွှန်မှာ အဓိကအားဖြင့် Azure ဝန်ဆောင်မှုများကို ဦးတည်ထားပေမယ့် [supported models and services list](../README.md#-supported-models-and-services) မှ ထောက်ခံထားသော ဘာသာစကားမော်ဒယ် များကို မည်သည့်အချိန်မဆို ရွေးချယ်အသုံးပြုနိုင်ပါတယ်။

## *.env* ဖိုင် ဖန်တီးခြင်း

သင့်ပရောဂျက်ရဲ့ အခြေခံ ဒါရိုက်ထရီမှာ *.env* ဆိုတဲ့ ဖိုင်တစ်ခု ဖန်တီးပါ။ ဒီဖိုင်မှာ သင့် environment variables အားလုံးကို ရိုးရှင်းတဲ့ ဖော်မတ်နဲ့ သိမ်းဆည်းထားမှာ ဖြစ်ပါတယ်။

> [!WARNING]
> *.env* ဖိုင်ကို Git ကဲ့သို့သော version control system များထဲ သွင်းမထားပါနှင့်။ အမှားတစ်ခုဖြစ်၍ commit မဖြစ်အောင် *.env* ကို .gitignore ဖိုင်ထဲ ထည့်သွင်းပါ။

1. သင့်ပရောဂျက်ရဲ့ အခြေခံ ဒါရိုက်ထရီသို့ သွားပါ။

1. အခြေခံ ဒါရိုက်ထရီမှာ *.env* ဖိုင်တစ်ခု ဖန်တီးပါ။

1. *.env* ဖိုင်ကို ဖွင့်ပြီး အောက်ပါ အကြမ်းဖျင်းကို ကူးထည့်ပါ။

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"
    ```

> [!NOTE]
> သင့် API key များနှင့် endpoint များကို ရှာဖွေချင်ပါက [set-up-azure-ai.md](../set-up-azure-ai.md) ကို ကြည့်ရှုနိုင်ပါတယ်။

**ကန့်သတ်ချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ တိကျမှုအတွက် ကြိုးပမ်းထားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ အတည်ပြုရမည့် အရင်းအမြစ်အဖြစ် ယူဆရမည် ဖြစ်သည်။ အရေးကြီးသော သတင်းအချက်အလက်များအတွက်တော့ လူကြီးမင်းသည် ပညာရှင်လူသား ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုပြဿနာများ သို့မဟုတ် မှားယွင်းဖတ်ရှုမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မခံပါ။