# Co-op Translator

_Make e easy to automate an maintain translations for your educational GitHub content for plenty languages as your project dey change._

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

### 🌐 Support for plenty languages

#### Na [Co-op Translator](https://github.com/Azure/co-op-translator) dey support

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](./README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **You wan clone am for your machine?**
>
> This repository get 50+ language translations wey go make the download size big well well. If you wan clone without translations, use sparse checkout:
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
> This one go give you everything wey you need to complete the course with much faster download.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Overview

**Co-op Translator** dey help you localize your educational GitHub content into plenty languages without wahala.
When you update your Markdown files, images, or notebooks, translations go dey automatically synced, so your content go remain correct an up-to-date for learners all over the world.

You fit use am from the CLI for repository translation, from the Python API for automation, or through the MCP server for agent an editor workflows.

Example of how translated content dey organized:

![Example](../../imgs/translation-ex.png)

## Why Co-op Translator?

Translating one file easy. To keep whole documentation repository translated, linked, an up to date na the gbege.

| Problem | How Co-op Translator helps |
| --- | --- |
| Long docs are not one prompt | Large Markdown files dem dey split into chunks, so long README no dey depend on one fragile model response. If one chunk fail, Co-op Translator fit retry an only re-chunk the part wey fail. |
| Incomplete translations should not be marked current | If translation cut short e no suppose seal as up to date. Co-op Translator dey check translation integrity before e save, an fit detect translations wey no complete structurally. |
| Links should match the translated repo structure | Manual translations dey often leave relative links wey still point back to the source tree. Co-op Translator go rewrite Markdown, notebook, image, an README links to match the `translations/<lang>/...` structure. |
| Translation should work across an entire repo | Co-op Translator dey handle README files, docs, notebooks, an image text as one repository workflow, no be translate files one-by-one. |
| Maintaining translations matters more than creating them once | Source hashes an translation metadata make Co-op Translator fit find outdated files, skip files wey never change, an keep translated content synchronized as the source repo dey evolve. |

## How translation state is managed

Co-op Translator dey manage translated content as **versioned software artifacts**,  
no be as static files.

The tool dey track the state of translated Markdown, images, and notebooks
using **language-scoped metadata**.

This design make Co-op Translator fit:

- Reliably detect outdated translations
- Treat Markdown, images, and notebooks the same way
- Scale safely across big, fast-moving, multi-language repositories

By modeling translations as managed artifacts,
translation workflows go align naturally with modern
software dependency an artifact management practices.

→ [How dem dey manage translation state](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Related deep dives

- [Fixing Broken Markdown in AI Translation: Hardening a Production Pipeline](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Get Started

You fit use Co-op Translator from the CLI, the Python API, or the MCP server. Start with the workflow guide if you dey choose between local translation, automation, CI, and agent/editor integration.

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

For first runs on big repositories, use `--dry-run` before you write translated files. See the [CLI Reference](../../docs/cli.md) for content type flags, logs, review, and link migration.

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

Make join us change how educational content dey shared for the world! Give [Co-op Translator](https://github.com/azure/co-op-translator) one ⭐ for GitHub an support our mission to break language barrier for learning an technology. Your interest an contributions dey make big difference! Code contributions an feature suggestions dey welcome anytime.

### Explore Microsoft educational content in your language
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

👉 Make you click di image wey dey under to watch for YouTube.

- **Open at Microsoft**: Small 18-minute intro and quick guide wey show how you go take use Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contributing

Dis project dey welcome contributions and suggestions. You dey interested to contribute to Azure Co-op Translator? Abeg check our [CONTRIBUTING.md](../../CONTRIBUTING.md) for di guidelines wey go show how you fit help make Co-op Translator easier for people to use.

## Contributors

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code of Conduct

Dis project don adopt di [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information, check di [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or hala [opencode@microsoft.com](mailto:opencode@microsoft.com) if you get any extra questions or comments.

## Responsible AI

Microsoft dey committed to help customers use our AI products responsibly, to share wetin we learn, and to build trust through tools like Transparency Notes and Impact Assessments. Plenti of dem resources dey available for [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoft approach to responsible AI base for our AI principles: fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability.

Big natural language, image, and speech models — like di ones wey dey used for dis sample — fit behave in ways wey no fair, wey no reliable, or wey fit offend people, and fit cause harm. Abeg read di [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) make you sabi di risks and limits.

Di recommended way to reduce dis kain risks na to put safety system for your architecture wey fit detect and stop harmful behaviour. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) dey provide independent level of protection wey fit detect harmful user-generated and AI-generated content for apps and services. Azure AI Content Safety get text and image APIs wey allow you to detect materials wey harmful. We still get interactive Content Safety Studio wey allow you view, explore and try sample code for detecting harmful content across different modalities. Dis [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) go guide you on how to make requests to the service.

Another thing to consider na overall application performance. For multi-modal and multi-model applications, performance mean say di system go do wetin you and your users dey expect, including make e no produce harmful outputs. E important make you assess the performance of your whole application using [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

You fit evaluate your AI app for your development environment using di [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). If you get test dataset or target, your generative AI application generations go dey measured quantitatively with built-in evaluators or custom evaluators wey you choose. To start with prompt flow sdk to evaluate your system, follow di [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). After you run evaluation, you fit [visualize di results for Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Trademarks

Dis project fit get trademarks or logos for different projects, products, or services. Authorized use of Microsoft trademarks or logos must follow [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
If you modify dis project and use Microsoft trademarks or logos, make sure e no go cause confusion or make people think Microsoft dey sponsor am. Any use of third-party trademarks or logos dey subject to di policies of those third parties.

## Getting Help

If you jam problem or get question about building AI apps, join:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

If you get product feedback or errors while you dey build, visit:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)