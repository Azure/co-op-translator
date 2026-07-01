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

**Anza hapa:** [Chagua mtiririko wako wa kazi](https://azure.github.io/co-op-translator/workflows/) | [Utekelezaji wa mipangilio](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [API ya Python](https://azure.github.io/co-op-translator/api/) | [Seva ya MCP](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Multi-Language Support

#### Supported by [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](./README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

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

## Overview

**Co-op Translator** inakusaidia kutafsiri yaliyomo yako ya elimu kwenye GitHub kwa lugha nyingi kwa urahisi.
Unapo-update faili zako za Markdown, picha, au majarida (notebooks), tafsiri zinabaki zikasawazishwa kiotomatiki, zikihakikisha maudhui yako yanabaki sahihi na ya kisasa kwa wanafunzi duniani kote.

Tumia kutoka kwa CLI kwa tafsiri za rejesta, kutoka kwa API ya Python kwa uendeshaji wa kazi, au kupitia seva ya MCP kwa mtiririko wa mawakala na wahariri.

Mfano wa jinsi yaliyotafsiriwa yanavyopangwa:

![Example](../../imgs/translation-ex.png)

## Why Co-op Translator?

Kutafsiri faili moja ni rahisi. Kuendelea na kutunza rejesta nzima ya nyaraka
iliyotafsiriwa, iliyounganishwa, na iliyosasishwa ni sehemu ngumu zaidi.

| Problem | How Co-op Translator helps |
| --- | --- |
| Long docs are not one prompt | Large Markdown files are split into chunks, so a long README does not depend on one fragile model response. If a chunk fails, Co-op Translator can retry and re-chunk only the failed part. |
| Incomplete translations should not be marked current | A truncated translation should never be sealed as up to date. Co-op Translator checks translation integrity before saving and can detect structurally incomplete existing translations. |
| Links should match the translated repo structure | Manual translations often leave relative links pointing back to the source tree. Co-op Translator rewrites Markdown, notebook, image, and README links to match the `translations/<lang>/...` structure. |
| Translation should work across an entire repo | Co-op Translator handles README files, docs, notebooks, and image text as part of one repository workflow, instead of translating files one by one. |
| Maintaining translations matters more than creating them once | Source hashes and translation metadata let Co-op Translator find outdated files, skip unchanged files, and keep translated content synchronized as the source repo evolves. |

## How translation state is managed

Co-op Translator manages translated content as **versioned software artifacts**,  
not as static files.

The tool tracks the state of translated Markdown, images, and notebooks
using **language-scoped metadata**.

This design allows Co-op Translator to:

- Reliably detect outdated translations
- Treat Markdown, images, and notebooks consistently
- Scale safely across large, fast-moving, multi-language repositories

By modeling translations as managed artifacts,
translation workflows align naturally with modern
software dependency and artifact management practices.

→ [How translation state is managed](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Related deep dives

- [Fixing Broken Markdown in AI Translation: Hardening a Production Pipeline](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Get Started

Co-op Translator can be used from the CLI, the Python API, or the MCP server. Start with the workflow guide if you are choosing between local translation, automation, CI, and agent/editor integration.

- [Choose your workflow](../../docs/workflows.md)
- [Configure credentials](../../docs/configuration.md)
- [Translate from the CLI](../../docs/cli.md)
- [Automate with the Python API](../../docs/api.md)
- [Connect with the MCP Server](../../docs/mcp.md)
- [Run in GitHub Actions](../../docs/github-actions.md)

Minimal CLI example after configuration:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

For first runs on large repositories, use `--dry-run` before writing translated files. See the [CLI Reference](../../docs/cli.md) for content type flags, logs, review, and link migration.

Container quick run with Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Container quick run with PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Features

- Automated translation for Markdown, notebooks, and images
- Keeps translations in sync with source changes
- Works locally (CLI) or in CI (GitHub Actions)
- Exposes Markdown, notebook, image, review, and project translation tools through MCP
- Uses Azure OpenAI or OpenAI for provider-backed translation
- Lets MCP host agents translate Markdown and notebook chunks without Co-op Translator LLM credentials
- Uses Azure AI Vision for image text extraction and translation
- Reviews translation structure and freshness with deterministic checks
- Preserves Markdown formatting and structure

## Docs

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

## Support us and foster global learning

Join us in revolutionizing how educational content is shared globally! Give [Co-op Translator](https://github.com/azure/co-op-translator) a ⭐ on GitHub and support our mission to break down language barriers in learning and technology. Your interest and contributions make a significant impact! Code contributions and feature suggestions are always welcome.

### Explore Microsoft educational content in your language
- [LangChain4j kwa Waanzilishi](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD kwa Waanzilishi](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI kwa Waanzilishi](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) kwa Waanzilishi](https://github.com/microsoft/mcp-for-beginners)
- [Maajenti za AI kwa Waanzilishi](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI kwa Waanzilishi ukitumia .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI kwa Waanzilishi](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI kwa Waanzilishi ukitumia Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML kwa Waanzilishi](https://aka.ms/ml-beginners)
- [Sayansi ya Data kwa Waanzilishi](https://aka.ms/datascience-beginners)
- [AI kwa Waanzilishi](https://aka.ms/ai-beginners)
- [Usalama wa Mtandao kwa Waanzilishi](https://github.com/microsoft/Security-101)
- [Uendelezaji wa Wavuti kwa Waanzilishi](https://aka.ms/webdev-beginners)
- [IoT kwa Waanzilishi](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video presentations

👉 Bofya picha iliyo hapa chini kutazama kwenye YouTube.

- **Open at Microsoft**: Maelezo mafupi ya dakika 18 na mwongozo wa haraka juu ya jinsi ya kutumia Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contributing

Mradi huu unakaribisha michango na mapendekezo. Unavutiwa kuchangia Azure Co-op Translator? Tafadhali tazama [CONTRIBUTING.md](../../CONTRIBUTING.md) kwa miongozo juu ya jinsi unavyoweza kusaidia kufanya Co-op Translator iwe rahisi kupatikana.

## Contributors

[![wachangiaji wa co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code of Conduct

Mradi huu umepitisha [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Kwa habari zaidi angalia [FAQ ya Kanuni za Tabia](https://opensource.microsoft.com/codeofconduct/faq/) au wasiliana na [opencode@microsoft.com](mailto:opencode@microsoft.com) kwa maswali au maoni zaidi.

## Responsible AI

Microsoft imejizatiti kuwasaidia wateja wetu kutumia bidhaa zetu za AI kwa uwajibikaji, kushirikisha yale tunayojifunza, na kujenga ushirikiano wa kuaminiana kupitia zana kama Transparency Notes na Impact Assessments. Rasilimali nyingi kati ya hizi zinaweza kupatikana kwenye [https://aka.ms/RAI](https://aka.ms/RAI).
Njia ya Microsoft kwa AI yenye uwajibikaji imetegemea kanuni zetu za AI za usawa, uthabiti na usalama, faragha na ulinzi, ujumuishaji, uwazi, na uwajibikaji.

Mifano kubwa ya lugha asilia, picha, na sauti - kama ile zinazotumika katika sampuli hii - inaweza kutoa tabia ambazo sio za haki, zisizokuwa za kuaminika, au za kuudhi, na hivyo kusababisha madhara. Tafadhali wasiliana na [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ili ujue kuhusu hatari na mipaka.

Njia inayopendekezwa kupunguza hatari hizi ni kujumuisha mfumo wa usalama katika usanifu wako ambao unaweza kugundua na kuzuia tabia hatari. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) inatoa safu huru ya ulinzi, inayoweza kugundua maudhui hatari yaliyozalishwa na watumiaji na yale yaliyozalishwa na AI katika programu na huduma. Azure AI Content Safety inajumuisha API za maandishi na picha ambazo zinakuwezesha kugundua nyenzo hatari. Pia tunayo Content Safety Studio itakayokuwezesha kuona, kuchunguza na kujaribu mifano ya msimbo wa ku detects maudhui hatari kwa aina mbalimbali. Nyaraka za [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) zitaongoza jinsi ya kutuma maombi kwa huduma.

Sehemu nyingine ya kuzingatia ni utendaji wa jumla wa programu. Kwa programu zenye modal na modeli nyingi, tunachukulia utendaji kama kuwa mfumo unafanya kazi kama unavyotarajia wewe na watumiaji wako, ikijumuisha kutozalisha matokeo hatari. Ni muhimu kutathmini utendaji wa programu yako kwa ujumla kwa kutumia [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Unaweza kutathmini programu yako ya AI katika mazingira yako ya maendeleo ukitumia [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Ukiwa na seti ya data ya mtihani au lengo, uzazi wa programu yako ya generative AI hupimwa kwa kiasi kwa kutumia wenye tathmini waliyojengwa au wenye tathmini maalum unayochagua. Ili kuanza na prompt flow sdk kutathmini mfumo wako, unaweza kufuata [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Ukimaliza utekelezaji wa uteuzi wa tathmini, unaweza [kuonyesha matokeo katika Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Trademarks

Mradi huu unaweza kuwa na nembo za biashara au nembo za miradi, bidhaa, au huduma. Matumizi yaliyoruhusiwa ya nembo za biashara au nembo za Microsoft yanayofuata na lazima yafuate [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Matumizi ya nembo za Microsoft katika matoleo yaliyorekebishwa ya mradi huu yasifanye kuchanganya au kuonyesha udhamini wa Microsoft.
Matumizi yoyote ya nembo za upande wa tatu au nembo unatazwa na sera za upande wa tatu husika.

## Getting Help

Ikiwa umekwama au una maswali kuhusu kujenga programu za AI, jiunge na:

[![Discord ya Microsoft Foundry](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ikiwa una maoni kuhusu bidhaa au makosa wakati wa kujenga tembelea:

[![Jukwaa la Waendelezaji Microsoft Foundry](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)