<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T13:06:12+00:00",
  "source_file": "README.md",
  "language_code": "pcm"
}
-->
# Co-op Translator

_Ezly automate di translation of your educational GitHub content into plenti languages to reach people all over di world._

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

### 🌐 Multi-Language Support

#### Supported by [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](./README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Overview

**Co-op Translator** dey help you localize your educational GitHub content into many languages without wahala.
When you update your Markdown files, images, or notebooks, di translations go dey automatically synchronized, so your content go always dey correct and fresh for learners everywhere.

Example of how translated content dey arranged:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.pcm.png)

## Quick start

```bash
# Make and start one virtual environment (na wetin dem recommend)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install di package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

Docker:

```bash
# Comot di public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run wit di current folder mount and .env provide (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimal setup

1. Make one `.env` file using di template: [.env.template](../../.env.template)
2. Setup one LLM provider (Azure OpenAI or OpenAI)
3. (Optional) For image translation (`-img`), setup Azure AI Vision
4. (Recommended) Clear any old translations to avoid gbege (e.g., `translations/`)
5. (Recommended) Add translation section for your README using di [README languages template](./getting_started/README_languages_template.md)
6. Check: [Set up Azure AI](./getting_started/set-up-azure-ai.md)

## Usage

Translate all di supported types:

```bash
translate -l "ko ja"
```

Only Markdown:

```bash
translate -l "de" -md
```

Markdown + images:

```bash
translate -l "pt" -md -img
```

Only notebooks:

```bash
translate -l "zh" -nb
```

More flags: [Command reference](./getting_started/command-reference.md)

## Features

- Automatic translation for Markdown, notebooks, and images
- Keep translations dey synchronized with source changes
- Fit work locally (CLI) or for CI (GitHub Actions)
- Use Azure OpenAI or OpenAI; optional Azure AI Vision for images
- Preserve Markdown formatting and structure

## Docs

- [Command-line guide](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions guide (Public repositories & standard secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions guide (Microsoft organization repositories & org-level setups)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README languages template](./getting_started/README_languages_template.md)
- [Supported languages](./getting_started/supported-languages.md)
- [Contributing](./CONTRIBUTING.md)
- [Troubleshooting](./getting_started/troubleshooting.md)

### Microsoft-specific guide
> [!NOTE]
> For people wey dey maintain Microsoft “For Beginners” repositories only.

- [Updating the “other courses” list (for MS Beginners repositories only)](./getting_started/update-other-courses.md)

## Support us and foster global learning

Make you join us to change how educational content dey shared worldwide! Give [Co-op Translator](https://github.com/azure/co-op-translator) one ⭐ for GitHub and support our mission to break language barrier for learning and technology. Your interest and contributions dey make big difference! Code contributions and feature ideas always dey welcome.

### Explore Microsoft educational content in your language

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

👉 Click di image below to watch for YouTube.

- **Open at Microsoft**: Short 18-minute introduction and quick guide on how to use Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.pcm.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contributing

Dis project dey welcome contributions and suggestions. If you wan contribute to Azure Co-op Translator, abeg check our [CONTRIBUTING.md](./CONTRIBUTING.md) for how you fit help make Co-op Translator easier for everybody.

## Contributors

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code of Conduct

Dis project don adopt di [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more info check di [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) if you get any questions or comments.

## Responsible AI

Microsoft dey committed to help our customers use our AI products responsibly, share wetin we learn, and build trust-based partnerships through tools like Transparency Notes and Impact Assessments. Plenty of these resources dey for [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoft approach to responsible AI dey based on our AI principles of fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability.

Big natural language, image, and speech models - like di ones wey dem use for dis sample - fit sometimes behave in ways wey no fair, no reliable, or fit offend people, and dis fit cause wahala. Abeg check di [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) to sabi di risks and limits.
Di beta way to reduce dis kain risk na to put one safety system for your architecture wey fit detect and stop bad behavior. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) dey provide one independent protection layer wey fit detect bad user-generated and AI-generated content for apps and services. Azure AI Content Safety get text and image APIs wey fit help you detect bad material. We still get one interactive Content Safety Studio wey make you fit see, explore, and try sample code to detect bad content for different types. Dis [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) go guide you how to make requests to di service.

Another thing wey you suppose consider na di overall app performance. For multi-modal and multi-model apps, we mean say di system go perform as you and your users expect, including no to generate bad outputs. E important to check how your whole app dey perform using [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

You fit test your AI app for your development environment using di [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Whether you get test dataset or target, your generative AI app generations go get quantitative measurement with built-in evaluators or custom evaluators wey you choose. To start to use prompt flow sdk to evaluate your system, you fit follow di [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). After you run evaluation, you fit [see di results for Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Trademarks

Dis project fit get trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos dey follow [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos for modified versions of dis project no suppose cause confusion or make people think say Microsoft dey sponsor am. Any use of third-party trademarks or logos dey follow di policies of those third parties.

## Getting Help

If you jam wahala or get any question about how to build AI apps, join:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

If you get product feedback or errors while you dey build, visit:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document na AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) wey translate am. Even though we dey try make am correct, abeg sabi say automated translation fit get some mistakes or no too correct. Di original document wey dem write for im own language na di correct one. If na serious matter, e better make person wey sabi human translation do am. We no go responsible for any wahala or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->