# Co-op Translator

_Easily automate and maintain translations for your educational GitHub content across multiple languages as your project evolves._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**Start here:** [Choose your workflow](https://azure.github.io/co-op-translator/workflows/) | [Configuration](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Multi-Language Support

#### Supported by [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](./README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> This gives you everything you need to complete the course with a much faster download.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## ကြည့်မည့် အကျဥ်းချုပ်

**Co-op Translator** သည် သင့် ပညာရေးဆိုင်ရာ GitHub အကြောင်းအရာများကို ဘာသာစကားအများစွာသို့ မလွယ်ကူစွာ ပြန်လည် ပြောင်းလဲပေးနိုင်ရန် ကူညီပေးသည်။  
Markdown ဖိုင်များ၊ ပုံများ သို့မဟုတ် notebook များကို ပြင်ဆင်သောအခါ ဘာသာပြန်ထားသော အကြောင်းအရာများကို အလိုအလျောက် စုစည်းထားပေး၍ ကမ္ဘာတစ်ဝှမ်းရှိ သင်ယူလိုသူများအတွက် မှန်ကန်ပြီး ခေတ်မှီနေစေပါသည်။

ဒါကို CLI မှ အသုံးပြု၍ repository ကို ဘာသာပြန်နိုင်ပြီး၊ Python API ဖြင့် အလိုအလျောက်လုပ်ဆောင်နိုင်ပြီး၊ agent နှင့် editor workflow များအတွက် MCP server ကနေ အသုံးပြုနိုင်သည်။

ဘာသာပြန်ထားသော အကြောင်းအရာများ ဘယ်လို စုစည်းထားကြောင်း ဥပဒ်ပြ ဥပမာ:

![Example](../../imgs/translation-ex.png)

## အဘယ်ကြောင့် Co-op Translator ကို သုံးရမလဲ?

ဖိုင်တစ်ခုကို ဘာသာပြန်ခြင်းလက်တွေ့လုပ်ဆောင်ရတာ လွယ်ကူပေမယ့်
စာရွက်စာတမ်း repository တစ်ခုလုံးကို
ဘာသာပြန်ထား၊ link တွေနဲ့ချိတ်ဆက်ထားပြီး ခေတ်မီအောင် ထိန်းသိမ်းထားရတာက ခက်ခဲသည်။

| Problem | How Co-op Translator helps |
| --- | --- |
| Long docs are not one prompt | Large Markdown files are split into chunks, so a long README does not depend on one fragile model response. If a chunk fails, Co-op Translator can retry and re-chunk only the failed part. |
| Incomplete translations should not be marked current | A truncated translation should never be sealed as up to date. Co-op Translator checks translation integrity before saving and can detect structurally incomplete existing translations. |
| Links should match the translated repo structure | Manual translations often leave relative links pointing back to the source tree. Co-op Translator rewrites Markdown, notebook, image, and README links to match the `translations/<lang>/...` structure. |
| Translation should work across an entire repo | Co-op Translator handles README files, docs, notebooks, and image text as part of one repository workflow, instead of translating files one by one. |
| Maintaining translations matters more than creating them once | Source hashes and translation metadata let Co-op Translator find outdated files, skip unchanged files, and keep translated content synchronized as the source repo evolves. |

## ဘာသာပြန်ခြင်း အခြေအနေကို မည်ကဲ့သို့ စီမံငြိမ်သက်စေသနည်း

Co-op Translator သည် ဘာသာပြန်ထားသော အကြောင်းအရာများကို "ဗားရှင်းထားသော ဆော့ဖ်ဝဲ အရာဝတ္ထုများ" အဖြစ် စီမံသည်၊  
တည်ငြိမ်သော ဖိုင်များအဖြစ် မဟုတ်ပါ။

ဤကိရိယာသည် Markdown, ပုံနှင့် notebook များကို
ဘာသာစကားအလိုက် သတ်မှတ်ထားသော metadata များဖြင့် အခြေအနေကို စောင့်ကြည့်သည်။

ဒီဒီဇိုင်းကြောင့် Co-op Translator သည် အောက်ပါအရာများကို မြန်မြန်ဆန်ဆန် ပြုလုပ်နိုင်သည် -

- မထက်မြက်သေးသော ဘာသာပြန်ချက်များကို ယုံကြည်စွာ ရှာဖွေစစ်ဆေးနိုင်သည်
- Markdown, ပုံများနှင့် notebook များကို တစ်ရပ်တည်း သေချာစွာ ကိုင်တွယ်နိုင်သည်
- ကြီးမား၍ မြန်ဆန်သွားသော ဘာသာစကားစုံ repository များတွင်လည်း အန္တရာယ်ကင်းစွာ ဖော်ဆောင်နိုင်သည်

ဘာသာပြန်ချက်များကို စီမံချက်အဖြစ် မော်ဒယ်လုပ်ခြင်းဖြင့်
ဘာသာပြန် workflow များသည် ပစ္စည်းချိတ်ဆက်မှုနှင့် အရာဝတ္ထု စီမံခန့်ခွဲမှု ပုံစံများနှင့် သဘာဝကျစွာ ကိုက်ညီသွားသည်။

→ [How translation state is managed](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### ဆက်စပ် ပြင်းထန်ဆန်းစစ်ခြင်းများ

- [Fixing Broken Markdown in AI Translation: Hardening a Production Pipeline](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## စတင်အသုံးပြုရန်

Co-op Translator ကို CLI, Python API၊ MCP server မှ အသုံးပြုနိုင်သည်။ ဒါ့အပြင် နေ့စဉ် လုပ်ငန်းစဉ်၊ အလိုအလျောက်လုပ်ဆောင်ခြင်း၊ CI နှင့် agent/editor ပေါင်းစည်းမှုတို့အတွက် workflow ညွှန်ကြားမှုနှင့် စတင်ပါ။

- [Choose your workflow](../../docs/workflows.md)
- [Configure credentials](../../docs/configuration.md)
- [Translate from the CLI](../../docs/cli.md)
- [Automate with the Python API](../../docs/api.md)
- [Connect with the MCP Server](../../docs/mcp.md)
- [Run in GitHub Actions](../../docs/github-actions.md)

ဖွဲ့စည်းမှု ပြပြီးနောက် မျှဝေသုံးရန် CLI နမူနာ အနည်းဆုံး:

```bash
python -m venv .venv
# ဝင်းဒိုးစ်
.venv\Scripts\activate
# မက်အိုအက်စ်/လင်းနပ်စ်
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

ကြီးမားသော repository များပေါ်တွင် ပထမဆုံး run များအတွက် `--dry-run` ကို သုံးပြီး ဘာသာပြန်ထားသော ဖိုင်များကို ရေးသားရန်မပြုမီ စစ်ဆေးပြီး သုံးပါ။ အကြောင်းအရာ အမျိုးအစား flag များ၊ logs, review နှင့် link migration များအတွက် [CLI Reference](../../docs/cli.md) ကို ကြည့်ပါ။

Container အတွက် Bash/Zsh ဖြင့် အမြန် run:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

PowerShell ဖြင့် Container အမြန် run:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## အင်္ဂါရပ်များ

- Markdown, notebook, နှင့် ပုံများအတွက် အလိုအလျောက် ဘာသာပြန်ခြင်း
- မူရင်းပြောင်းလဲမှုများနှင့် အညီ ဘာသာပြန်ချက်များကို တစ်ပြိုင်နက် စနစ်တကျ ထိန်းသိမ်းထားသည်
- ဒေသခံ (CLI) သို့မဟုတ် CI (GitHub Actions) တွင် အလုပ်လုပ်နိုင်သည်
- MCP မှတဆင့် Markdown, notebook, image, review နှင့် project ဘာသာပြန် ကိရိယာများကို ဖော်ပြပေးသည်
- Azure OpenAI သို့မဟုတ် OpenAI ကို provider အဖြစ် အသုံးပြု၍ ဘာသာပြန်သည်
- MCP သည် agent များကို Co-op Translator LLM အောက်ခံ အထောက်အကူမရှိဘဲ Markdown နှင့် notebook chunk များကို ဘာသာပြန်စေရန် host လုပ်ခွင့်ပေးသည်
- ပုံထဲမှ စာသားထုတ်ယူခြင်းနှင့် ဘာသာပြန်ခြင်းအတွက် Azure AI Vision ကို အသုံးပြုသည်
- ဘာသာပြန်ဖွဲ့စည်းမှုနှင့် تازness ကို သေချာစစ်ဆေးခြင်းဖြင့် ပြန်လည်သုံးသပ်ပေးသည်
- Markdown ဖော်မတ်နှင့် ဖွဲ့စည်းမှုကို ထိန်းသိမ်းပေးသည်

## အကွက်စာတမ်းများ

- [Documentation site](https://azure.github.io/co-op-translator/)
- [Choose your workflow](../../docs/workflows.md)
- [Configuration](../../docs/configuration.md)
- [Azure AI Setup](../../docs/azure-ai-setup.md)
- [CLI Reference](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README languages template](../../docs/readme-languages-template.md)
- [Supported languages](../../docs/supported-languages.md)
- [Contributing](../../CONTRIBUTING.md)
- [Troubleshooting](../../docs/troubleshooting.md)

### Microsoft-specific guide
> [!NOTE]
> For maintainers of the Microsoft “For Beginners” repositories only.

- [Updating the “other courses” list (for MS Beginners repositories only)](../../docs/microsoft-beginners.md)

## ကျွန်တော်တို့အား ပံ့ပိုးပြီး ကမ္ဘာလုံးဆိုင်ရာ သင်ယူမှုကို ဖွံ့ဖြိုးစေပါ

ပညာရေးဆိုင်ရာ အကြောင်းအရာများကို ကမ္ဘာတစ်ဝှမ်း မျှဝေတင်ပြရာ၌ ပြောလေ့ရှိသည့် ဘာသာစကားအတားအဆီးများကို ဖျက်ဆီးရန် သင်၏ အရေးပါမှုနှင့် ဝေမျှမှုများသည် သာမန်မဟုတ်ပဲ အရေးကြီးပါသည်။ [Co-op Translator](https://github.com/azure/co-op-translator) ကို GitHub တွင် ⭐ ပေးကာ ကျွန်ုပ်တို့၏ မစ်ရှင်ကို ထောက်ပံ့ပါ။ ကိုဒ် ပံ့ပိုးမှုများနှင့် အင်္ဂါရပ် အကြံပြုချက်များကို အမြဲကြိုဆိုပါသည်။

### သင့်ဘာသာစကားဖြင့် Microsoft ပညာရေး အကြောင်းအရာများကို ရှာဖွေပါ
- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video presentations

👉 အောက်ပါပုံကို နှိပ်၍ YouTube မှာ ကြည့်ရှုနိုင်သည်။

- **Open at Microsoft**: Co-op Translator ကို ဘယ်လို အသုံးပြုရမလဲ ဆိုတာအကြောင်း အကျဉ်းချုပ် ၁၈ မိနစ်စာ မိတ်ဆက်နှင့် လမ်းညွှန်ချက်တိုကောက်။

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contributing

ဤပရောဂျက်သို့ မှာပါဝင်ဆောင်ရွက်ခြင်းနှင့် အကြံပြုချက်များကို ကြိုဆိုပါသည်။ Azure Co-op Translator တွင် ပါဝင်လိုပါသလား? Co-op Translator ကို ပို၍ လျင်မြန်ဝင်ရောက်နိုင်အောင် ကူညီနိုင်မည့်နည်းလမ်းများအတွက် ကျေးဇူးပြု၍ ကျွန်ုပ်တို့၏ [CONTRIBUTING.md](../../CONTRIBUTING.md) ကို ကြည့်ပါ။

## Contributors

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code of Conduct

ဤပရောဂျက်သည် [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ကို လက်ခံထားပါသည်။
နောက်ထပ်သိရှိလိုပါက [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ကို ကြည့်ရှုပါ သို့မဟုတ် any ထပ်ဆောင်းမေးခွန်းများအတွက် [opencode@microsoft.com](mailto:opencode@microsoft.com) သို့ ဆက်သွယ်ပါ။

## Responsible AI

Microsoft သည် ကျွန်ုပ်တို့၏ဖောက်သည်များအား AI ထုတ်ကုန်များကို တာဝန်ယူ၍ အသုံးပြုနိုင်ရန် ကူညီပေးခြင်း၊ သင်ယူချက်များကို မျှဝေရေးနှင့် Transparency Notes နှင့် Impact Assessments ကဲ့သို့သော ကိရိယာများမှတဆင့် ယုံကြည်စိတ်ချ ရင်းနှီးမြှုပ်နှံမှုများ တည်ဆောက်ပေးခြင်းကို အဓိကထားဆောင်ရွက်ပါသည်။ ဤရင်းမြစ်များ၏ အများအားဖြင့် ကိုးကားချက်များကို [https://aka.ms/RAI](https://aka.ms/RAI) တွင် တွေ့နိုင်ပါသည်။
Microsoft ၏ တာဝန်ရှိသော AI ကို မည်သို့ဆောင်ရွက်ရမည်ဆိုသည်မှာ တရားမျှတမှု၊ ယုံကြည်ရမှုနှင့် လုံခြုံရေး၊ ကိုယ်ရေးကိုယ်တာပိုင်ဆိုင်မှုနှင့်လုံခြုံမှု၊ ပါဝင်မှု၊ ထင်ရှားမြင်သာမှုနှင့် တာဝန်ယူမှု ဆိုသည့် AI 원칙များပေါ် မူတည်ထားပါသည်။

ဤနမူနာတွင် အသုံးပြုထားသော ကြီးမားသောဘာသာစကား၊ ပုံနှင့် အသံ မော်ဒယ်များသည် မျှတခြင်းမရှိသော၊ ယုံကြည်စိတ်မဖောက်နိုင်သော သို့မဟုတ် ရိုက်ခတ်စေမှုရှိသော ပုံစံများဖြစ်ပေါ်စေပြီး ထိုကြောင့် အန္တရာယ်များ ဖြစ်ပေါ်စေနိုင်ပါသည်။ အန္တရာယ်များနှင့် ကန့်သတ်ချက်များအကြောင်း အသိပညာရရှိရန် [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ကို ညွှန်ကြားစုံစမ်းပါ။

ဤအန္တရာယ်များကို လျော့နည်းစေရန် အကြံပြုချက်မှာ သင်၏ စနစ်ဒီဇိုင်းတွင် ထိခိုက်စေနိုင်သည့် ကုန်ရှိန်ကို တွေ့ရှိပြီး ကာကွယ်ပေးနိုင်မည့် safety system တပ်ဆင်ရန် ဖြစ်သည်။ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) သည် အသုံးပြုသူဖန်တီးသော နှင့် AI ဖန်တီးထားသည့် ဆိုးကျိုးရလဒ်များကို တွေ့ရှိနိုင်ရန် လွတ်လပ်သိမ်းဆည်းပေးသည့် ကာကွယ်မှုအလွှာတစ်ခု ဖြစ်သည်။ Azure AI Content Safety တွင် ဖော်ပြထားသည့် text နှင့် image API များဖြင့် ဆိုးကျိုးဖြစ်နိုင်သည့် အရာများကို တွေ့ရှိနိုင်ပါသည်။ ထို့အပြင် Content Safety Studio ဟူသော အပြန်အလှန် လေ့လာနိုင်သည့် စက်တင်လွယ်ကူသော ကိရိယာလည်းရှိကာ မတူကွဲပြားသည့် မိုဒယ်များအတွက် ဆိုးကျိုးဖြစ်စေနိုင်သည့် အကြောင်းအရာများကို တွေ့ခြင်း၊ စူးစမ်းခြင်းနှင့် နမူနာကုဒ်များကို စမ်းသပ်နိုင်ပါသည်။ ဝန်ဆောင်မှုသို့ တောင်းဆိုချက်များ ပို့ပေးခြင်းကို လမ်းညွှန်သည့် အောက်ပါ [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ကူညီပါမည်။

တခြားအချက်တစ်ခုမှာ စက်ရုပ်စနစ်တစ်ခု၏ စုစုပေါင်းလည်ပတ်မှုစွမ်းရည်ကိုလည်း မှတ်ထားရမည်ဖြစ်သည်။ မိုဒယ်စုံစုံပြောစပ်၍ မိုဒယ်အမျိုးမျိုးအသုံးပြုသော အက်ပလီကေးရှင်းများတွင် စနစ်သည် သင့်နှင့် သင့်အသုံးပြုသူများ မျှော်လင့်သလို လုပ်ဆောင်နိုင်ရမည်ဖြစ်ပြီး ထိုအတွင်း ဆိုးကျိုးထွက်ရှိခြင်း မဖြစ်ပေါ်စေရန်ပါရှိရမည်။ သင့် အက်ပလီကေးရှင်း၏ စုစုပေါင်း စွမ်းဆောင်ရည်ကို [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) များ အသုံးပြုပြီး သုံးသပ်ရန် လိုအပ်ပါသည်။

သင်သည် တိုးတက်ရေးပတ်ဝန်းကျင်တွင် သင့် AI အက်ပလီကေးရှင်းကို [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) အသုံးပြု၍ သုံးသပ်နိုင်ပါသည်။ စမ်းသပ်ဒေတာစုစစ်တစ်ခု သို့မဟုတ် ရည်မှန်းချက်တစ်ခု ရှိပါက သင့် generative AI အက်ပလီကေးရှင်း၏ ဖန်တီးမှုများကို တိုင်းတာရာတွင် built-in evaluator များ သို့မဟုတ် မိမိရွေးချယ်သည့် custom evaluator များဖြင့် အရေအတွက်ဆိုင်ရာ တိုင်းတာချက်များ ရရှိစေပါသည်။ သင့်စနစ်ကို သုံးသပ်ရန် prompt flow sdk ဖြင့် စတင်လိုပါက [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ကို လိုက်နာပါ။ သုံးသပ်ခြင်း run တစ်ခုကို အကောင်အထည်ဖော်ပြီးနောက် သင်သည် [Azure AI Studio တွင် ရလဒ်များကို မြင်ယောင်နိုင်ပါသည်](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)။

## Trademarks

ဤပရောဂျက်တွင် project၊ ထုတ်ကုန် သို့မဟုတ် ဝန်ဆောင်မှုများ၏ trademark သို့မဟုတ် logo များ ပါရှိနိုင်ပါသည်။ Microsoft trademark များနှင့် logo များကို ခွင့်ပြုထားသည့် အသုံးပြုမှုများသည် [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) အတိုင်း လိုက်နာရမည် ဖြစ်ပါသည်။
ဒီပရောဂျက်၏ ပြင်ဆင်ထားသော ဗားရှင်းများတွင် Microsoft trademark သို့မဟုတ် logo များကို အသုံးပြုခြင်းသည် မှားယွင်းစေခြင်း သို့မဟုတ် Microsoft ၏ အားပေးမှုကို ဆိုလိုမနေစေရန် ဂရုစိုက်ရပါမည်။
တတိယပါတီ trademark သို့မဟုတ် logo များအား အသုံးပြုခြင်းသည် ထိုတတိယပါတီ၏ မူဝါဒများအောက်မှ ဖြစ်ပါသည်။

## Getting Help

တခုခုတွင် အတားအဆီးကြုံသည် သို့မဟုတ် AI apps တည်ဆောက်ရာတွင် မေးခွန်းများရှိလျှင် ဝင်ပါ။

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

ထုတ်ကုန်အကြံပြုချက်များ သို့မဟုတ် တည်ဆောက်ရင်း အမှားများရှိပါက ဤနေရာသို့ သွားကြည့်ပါ။

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)