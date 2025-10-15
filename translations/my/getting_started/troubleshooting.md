<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T04:13:17+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "my"
}
-->
# Microsoft Co-op Translator ပြန်ဆိုရေးကိရိယာ ပြဿနာဖြေရှင်းနည်းလမ်းညွှန်

## အကျဉ်းချုပ်
Microsoft Co-Op Translator က Markdown စာရွက်စာတမ်းတွေကို အလွယ်တကူ ပြန်ဆိုနိုင်တဲ့ အင်္ဂါရပ်ရှိတဲ့ ကိရိယာတစ်ခုပါ။ ဒီလမ်းညွှန်မှာ သုံးစွဲသူတွေ မကြုံတွေ့နိုင်တဲ့ ပြဿနာတွေကို ဘယ်လို ဖြေရှင်းရမလဲ ဆိုတာကို ရှင်းပြပေးထားပါတယ်။

## မကြုံတွေ့နိုင်တဲ့ ပြဿနာများနှင့် ဖြေရှင်းနည်းများ

### 1. Markdown Tag ပြဿနာ
**ပြဿနာ:** ပြန်ဆိုပြီးတဲ့ Markdown စာရွက်မှာ `markdown` tag အပေါ်ဆုံးမှာ ပါလာတာကြောင့် ဖော်ပြမှုမှာ ပြဿနာဖြစ်တတ်ပါတယ်။

**ဖြေရှင်းနည်း:** ဒီပြဿနာကို ဖြေရှင်းဖို့ `markdown` tag ကို ဖိုင်အပေါ်ဆုံးကနေ ဖျက်လိုက်ပါ။ ဒါဆို Markdown ဖိုင်က မှန်ကန်စွာ ဖော်ပြနိုင်ပါလိမ့်မယ်။

**လုပ်ဆောင်ရန်အဆင့်များ:**
1. ပြန်ဆိုပြီးတဲ့ Markdown (`.md`) ဖိုင်ကို ဖွင့်ပါ။
2. စာရွက်အပေါ်ဆုံးမှာ `markdown` tag ကို ရှာပါ။
3. `markdown` tag ကို ဖျက်ပါ။
4. ဖိုင်ကို သိမ်းပါ။
5. ပြန်ဖွင့်ပြီး မှန်ကန်စွာ ဖော်ပြနိုင်သလား စစ်ပါ။

### 2. ပုံ URL မကိုက်ညီမှု ပြဿနာ
**ပြဿနာ:** ထည့်သွင်းထားတဲ့ ပုံတွေ URL များက ဘာသာစကား locale နဲ့ မကိုက်ညီလို့ ပုံတွေ မှားနေတတ်ပါတယ်၊ ပျောက်နေတတ်ပါတယ်။

**ဖြေရှင်းနည်း:** ပုံ URL တွေကို စစ်ကြည့်ပြီး ဘာသာစကား locale ကို ကိုက်ညီအောင် ပြင်ပါ။ ပုံအားလုံးကို `translated_images` folder ထဲမှာ သိမ်းထားပြီး ပုံနာမည်မှာ ဘာသာစကား locale tag ပါပါတယ်။

**လုပ်ဆောင်ရန်အဆင့်များ:**
1. ပြန်ဆိုပြီးတဲ့ Markdown စာရွက်ကို ဖွင့်ပါ။
2. ထည့်ထားတဲ့ ပုံတွေ URL ကို ရှာပါ။
3. ပုံနာမည်ထဲက ဘာသာစကား locale ကို စာရွက်ဘာသာစကားနဲ့ ကိုက်ညီစေပါ။
4. လိုအပ်ရင် URL ကို ပြင်ပါ။
5. သိမ်းပြီး ပြန်ဖွင့်ကြည့်ပါ။

### 3. ပြန်ဆိုမှုတိကျမှု
**ပြဿနာ:** ပြန်ဆိုထားတဲ့ အကြောင်းအရာက တိကျမှုမရှိဘူး၊ ပြင်ဆင်ဖို့ လိုအပ်တယ်။

**ဖြေရှင်းနည်း:** ပြန်ဆိုထားတဲ့ စာရွက်ကို ပြန်ကြည့်ပြီး တိကျမှု၊ ဖတ်ရလွယ်အောင် ပြင်ဆင်ပါ။

**လုပ်ဆောင်ရန်အဆင့်များ:**
1. ပြန်ဆိုထားတဲ့ စာရွက်ကို ဖွင့်ပါ။
2. အကြောင်းအရာကို ဂရုစိုက်စွာ ပြန်ကြည့်ပါ။
3. တိကျမှုအတွက် လိုအပ်တဲ့ ပြင်ဆင်မှုတွေ လုပ်ပါ။
4. သိမ်းပါ။

## 4. ခွင့်ပြုချက် Error Redacted သို့မဟုတ် 404

ပုံတွေ သို့မဟုတ် စာသားတွေကို မှန်ကန်တဲ့ ဘာသာစကားနဲ့ မပြန်ဆိုနိုင်ဘူး၊ -d debug mode နဲ့ run လုပ်တဲ့အခါ 401 error တွေ့ရင် authentication fail ဖြစ်တာပါ။ သော့ချက်က မမှန်ဘူး၊ သက်တမ်းကုန်သွားပြီ သို့မဟုတ် endpoint region နဲ့ မချိတ်ထားဘူး ဖြစ်နိုင်ပါတယ်။

[-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) နဲ့ co-op translator ကို run လုပ်ပြီး root cause ကို နားလည်နိုင်ပါတယ်။

- **Error Message**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **ဖြစ်နိုင်တဲ့ အကြောင်းရင်းများ**:
  - Subscription key ကို request မှာ မှားရေးထားတယ်၊ redact လုပ်ထားတယ်။
  - AI Services Key သို့မဟုတ် Subscription Key က Azure AI Vision resource မဟုတ်ဘဲ Translator သို့မဟုတ် OpenAI resource ဖြစ်နိုင်တယ်။

 **Resource Type**
  - [Azure Portal](https://portal.azure.com) သို့မဟုတ် [Azure AI Foundry](https://ai.azure.com) ကို သွားပြီး resource type ကို `Azure AI services` → `Vision` ဖြစ်ကြောင်း စစ်ပါ။
  - သော့ချက်တွေ မှန်ကန်စွာ သုံးထားကြောင်း အတည်ပြုပါ။

## 5. Configuration Errors (Error Handling အသစ်)

Selective translation system အသစ်မှာ Co-op Translator က လိုအပ်တဲ့ service မရှိရင် error message တွေကို တိကျစွာ ပြပေးပါတယ်။

### 5.1. Azure AI Service မရှိသေးလို့ Image Translation မလုပ်နိုင်

**ပြဿနာ:** Image translation (`-img` flag) တောင်းဆိုထားပေမယ့် Azure AI Service ကို configure မလုပ်ထားပါ။

**Error Message:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**ဖြေရှင်းနည်း:**
1. **Option 1**: Azure AI Service ကို configure လုပ်ပါ
   - `.env` ဖိုင်ထဲ `AZURE_AI_SERVICE_API_KEY` ထည့်ပါ
   - `.env` ဖိုင်ထဲ `AZURE_AI_SERVICE_ENDPOINT` ထည့်ပါ
   - Service ကို အသုံးပြုနိုင်ကြောင်း စစ်ပါ

2. **Option 2**: Image translation request ကို ဖယ်ရှားပါ
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. လိုအပ်တဲ့ Configuration မရှိ

**ပြဿနာ:** LLM configuration အရေးကြီးတာ မရှိပါ။

**Error Message:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**ဖြေရှင်းနည်း:**
1. `.env` ဖိုင်ထဲမှာ အနည်းဆုံး LLM configuration တစ်ခုတော့ ပါစေကြောင်း စစ်ပါ:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` နဲ့ `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Azure OpenAI သို့မဟုတ် OpenAI တစ်ခုခု configure လုပ်ထားရပါမယ်၊ နှစ်ခုလုံး မလိုအပ်ပါ။

### 5.3. Selective Translation မှားယွင်းမှု

**ပြဿနာ:** Command အောင်မြင်သွားပေမယ့် ဖိုင်မပြန်ဆိုဘူး။

**ဖြစ်နိုင်တဲ့ အကြောင်းရင်းများ:**
- File type flags (`-md`, `-img`, `-nb`) မှားသုံးထားတယ်
- Project ထဲမှာ ကိုက်ညီတဲ့ ဖိုင်မရှိဘူး
- Directory structure မှားနေတယ်

**ဖြေရှင်းနည်း:**
1. **Debug mode သုံးပါ**:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Project ထဲက file types ကို စစ်ပါ**:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Flag တွေကို ကိုက်ညီစေပါ**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. System အဟောင်းကနေ ပြောင်းရွှေ့ခြင်း

### 6.1. Markdown-Only Mode ပယ်ဖျက်သွားပြီ

**ပြဿနာ:** Markdown-only fallback ကို အလိုအလျောက် သုံးတဲ့ command တွေ အလုပ်မလုပ်တော့ဘူး။

**အဟောင်းမှာ:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**အသစ်မှာ:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**ဖြေရှင်းနည်း:**
- **တိကျစွာ သတ်မှတ်ပါ**: ဘာကို ပြန်ဆိုချင်သလဲ ရှင်းရှင်းလင်းလင်း သတ်မှတ်ပါ
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Link များ မမျှော်လင့်တဲ့နေရာကို ဦးတည်ခြင်း

**ပြဿနာ:** ပြန်ဆိုထားတဲ့ ဖိုင်ထဲက link တွေ မမျှော်လင့်တဲ့နေရာကို ဦးတည်နေတတ်တယ်။

**အကြောင်းရင်း:** File type ရွေးချယ်မှုအပေါ် မူတည်ပြီး link တွေ dynamic ပြောင်းလဲတတ်တယ်။

**ဖြေရှင်းနည်း:**
1. **Link အသစ်အနေနဲ့ ဘယ်လို အလုပ်လုပ်သလဲ နားလည်ပါ**:
   - `-nb` ပါဝင်ရင်: Notebook link တွေ ပြန်ဆိုထားတဲ့ version ကို ဦးတည်တယ်
   - `-nb` မပါဝင်ရင်: Notebook link တွေ မူရင်းဖိုင်ကို ဦးတည်တယ်
   - `-img` ပါဝင်ရင်: Image link တွေ ပြန်ဆိုထားတဲ့ version ကို ဦးတည်တယ်
   - `-img` မပါဝင်ရင်: Image link တွေ မူရင်းဖိုင်ကို ဦးတည်တယ်

2. **သင့်လိုအပ်ချက်အတွက် combination မှန်ကန်စွာ ရွေးပါ**:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action run ပြီး PR မဖန်တီးဘူး

**လက္ခဏာ:** `peter-evans/create-pull-request` workflow logs မှာ:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**ဖြစ်နိုင်တဲ့ အကြောင်းရင်းများ:**
- **မပြောင်းလဲမှုရှိ**: Translation လုပ်ပြီး repo မှာ diff မရှိတော့ (repo up to date ဖြစ်နေတယ်)
- **Ignored outputs**: `.gitignore` မှာ commit လုပ်ချင်တဲ့ ဖိုင်တွေ (ဥပမာ `*.ipynb`, `translations/`, `translated_images/`) ကို exclude လုပ်ထားတယ်
- **add-paths မကိုက်ညီမှု**: Action ကို paths ပေးတဲ့အခါ output location နဲ့ မကိုက်ညီဘူး
- **Workflow logic/conditions**: Translation step က စောစောထွက်သွားတယ် သို့မဟုတ် မမျှော်လင့်တဲ့ directory မှာ ဖိုင်ရေးထားတယ်

**ဘယ်လို ပြင်/စစ်ရမလဲ:**
1. **Output ရှိ/မရှိ စစ်ပါ**: Translation ပြီးရင် workspace ထဲမှာ `translations/` နဲ့/သို့မဟုတ် `translated_images/` ထဲမှာ ဖိုင်အသစ်/ပြောင်းလဲမှု ရှိ/မရှိ စစ်ပါ။
   - Notebook ပြန်ဆိုရင် `.ipynb` ဖိုင်တွေ `translations/<lang>/...` ထဲမှာ ရေးထားကြောင်း စစ်ပါ။
2. **`.gitignore` ကို ပြန်ကြည့်ပါ**: Generated outputs တွေကို ignore မလုပ်ပါနဲ့။ အောက်ပါအရာတွေကို မထည့်ပါနဲ့:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (Notebook ပြန်ဆိုရင်)
3. **add-paths ကို output နဲ့ ကိုက်ညီစေပါ**: Multiline value သုံးပြီး folder နှစ်ခုလုံး ထည့်ပါ:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Debug အတွက် PR ကို အတင်းလုပ်ပါ**: Empty commit ကို ခွင့်ပြုထားပြီး wiring မှန်မမှန် စစ်ပါ:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Debug mode နဲ့ run လုပ်ပါ**: translate command မှာ `-d` ထည့်ပြီး ဘယ်ဖိုင်တွေ ရှာတွေ့/ရေးထားသလဲ print ထုတ်ပါ။
6. **Permissions (GITHUB_TOKEN)**: Workflow မှာ commit/PR ဖန်တီးခွင့်ရှိကြောင်း စစ်ပါ:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Quick Debugging Checklist

ပြန်ဆိုရေး ပြဿနာဖြေရှင်းတဲ့အခါ:

1. **Debug mode သုံးပါ**: `-d` flag ထည့်ပြီး log အသေးစိတ်ကြည့်ပါ
2. **Flag တွေကို စစ်ပါ**: `-md`, `-img`, `-nb` သုံးမှု သင့်ရည်ရွယ်ချက်နဲ့ ကိုက်ညီစေပါ
3. **Configuration ကို စစ်ပါ**: `.env` ဖိုင်ထဲမှာ လိုအပ်တဲ့ key တွေ ပါ/မပါ စစ်ပါ
4. **တဖြည်းဖြည်း စမ်းပါ**: `-md` တစ်ခုတည်းနဲ့ စပြီး နောက်ထပ် type တွေ ထပ်ထည့်ပါ
5. **File structure ကို စစ်ပါ**: Source ဖိုင်တွေ ရှိ/မရှိ၊ အသုံးပြုနိုင်/မနိုင် စစ်ပါ

Command တွေ၊ flag တွေ အသေးစိတ်ကို [Command Reference](./command-reference.md) မှာ ကြည့်နိုင်ပါတယ်။

---

**သတိပေးချက်**:
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူလစာရွက်စာတမ်း၏ မူရင်းဘာသာစကားကို အာဏာပိုင်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသောအချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာသော နားလည်မှုမှားခြင်း သို့မဟုတ် အနားလည်မှုမှားခြင်းများအတွက် ကျွန်ုပ်တို့သည် တာဝန်ယူမည်မဟုတ်ပါ။