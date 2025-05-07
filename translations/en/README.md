<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "329abbc9354793ea422f7e7ebf66be2c",
  "translation_date": "2025-05-07T01:50:04+00:00",
  "source_file": "README.md",
  "language_code": "en"
}
-->
![Logo](../../imgs/logo.png)

# Co-op Translator: Automate the Translation of Educational Documentation Effortlessly

_Easily automate the translation of your documentation into multiple languages to reach a global audience._

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### Language Support Powered by Co-op Translator

[Korean](../ko/README.md) | [Japanese](../ja/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Spanish](../es/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Portuguese (Brazil)](../br/README.md) | [Hindi](../hi/README.md) | [Russian](../ru/README.md) | [Turkish](../tr/README.md) | [Arabic](../ar/README.md) | [Indonesian](../id/README.md) | [Vietnamese](../vi/README.md)

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
>
> **Powerful Automation**: Now with GitHub Actions support! Automatically translate your documentation whenever changes are made to your repository, keeping everything up-to-date with ease. [Learn more](../..).

## Supported Models and Services

| Type                  | Name                           |
|-----------------------|--------------------------------|
| Language Model        | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| Computer Vision       | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> If a computer vision service is unavailable, co-op translator will switch to [Markdown-only mode](./getting_started/markdown-only-mode.md).

## Overview: Simplify Your Educational Content Translation

Language barriers significantly limit access to valuable educational materials and technical knowledge for learners and developers worldwide. This restricts participation and slows down global innovation and learning.

**Co-op Translator** was created to solve the inefficient manual translation process used for Microsoft’s large-scale educational series (such as the "For Beginners" guides). It has grown into a user-friendly, powerful tool designed to break down these barriers for everyone. By offering high-quality automated translations through CLI and GitHub Actions, Co-op Translator enables educators, students, researchers, and developers worldwide to share and access knowledge without language limits.

See how Co-op Translator organizes translated educational content:

![Example](../../imgs/translation-ex.png)

Markdown files and image text are automatically translated and neatly organized into language-specific folders.

**Unlock global access to your educational content with Co-op Translator today!**

## Supporting Global Access for Microsoft's Learning Resources

Co-op Translator helps close the language gap for key Microsoft educational initiatives by automating translations for repositories that serve a worldwide developer community. Examples currently using Co-op Translator include:

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## Key Features

- **Automated Translations**: Effortlessly translate text into multiple languages.
- **GitHub Actions Integration**: Automate translations as part of your CI/CD workflow.
- **Markdown Preservation**: Keep proper Markdown syntax intact during translation.
- **Image Text Translation**: Extract and translate text within images.
- **Advanced LLM Technology**: Utilize state-of-the-art language models for high-quality translations.
- **Easy Integration**: Smoothly fit into your existing project setup.
- **Simplify Localization**: Make localizing your project for international audiences straightforward.

## How It Works

![Architecture](../../imgs/architecture_241019.png)

Co-op Translator processes Markdown files and images from your project folder as follows:

1. **Text Extraction**: Extracts text from Markdown files and, if configured (e.g., with Azure Computer Vision), text embedded in images.
1. **AI Translation**: Sends the extracted text to the configured LLM (Azure OpenAI, OpenAI, etc.) for translation.
1. **Result Saving**: Saves the translated Markdown files and images (with translated text) into language-specific folders, preserving the original formatting.

## Getting Started

Get started quickly with the CLI or set up full automation using GitHub Actions.

### Quick Start: Command Line

For a quick start using the command line:

1. Install the package:
    ```bash
    pip install co-op-translator
    ```
2. Configure Credentials:
  - Create a `.env` file in your project's root directory.
  - Copy the contents from the [.env.template](../../.env.template) file into your new `.env` file.
  - Fill in the required API keys and endpoint information in your `.env` file.
3. Run Translation:
  - Navigate to your project's root directory in your terminal.
  - Execute the translate command, specifying target languages with the `-l` flag:
    ```bash
    translate -l "ko ja fr"
    ```
    *(Replace `"ko ja fr"` with your desired space-separated language codes)*

### Detailed Usage Guides

Choose the approach that best fits your workflow:

#### 1. Using the Command Line (CLI)

- Best for: One-time translations, manual control, or integration into custom scripts.
- Requires: Local installation of Python and the `co-op-translator` package.
- Guide: [Command Line Guide](./getting_started/command-line-guide/command-line-guide.md)

#### 2. Using GitHub Actions (Automation)

- Best for: Automatically translating content whenever changes are pushed to your repository. Keeps translations consistently up-to-date.
- Requires: Setting up a workflow file (`.github/workflows`) in your repository. No local installation needed.
- Guides:
  - [GitHub Actions Guide (Public Repositories & Standard Secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md) - Use this for most public or personal repositories that rely on standard repository secrets.
  - [GitHub Actions Guide (Microsoft Organization Repos & Org-Level Setups)](./getting_started/github-actions-guide/github-actions-guide-org.md) - Use this if you work within the Microsoft GitHub organization or need to use organization-level secrets or runners.

> [!NOTE]
> While this tutorial focuses on Azure resources, you can use any supported language model from the [supported models and services](../..) list.

### Troubleshooting and Tips

- [Troubleshooting Guide](./getting_started/troubleshooting.md)

### Additional Resources

- [Command Reference](./getting_started/command-reference.md): Detailed guide to all commands and options.
- [Multi-language Support Setup](./getting_started/multi-language-support.md): How to add a table linking to translated versions in your README.
- [Supported Languages](./getting_started/supported-languages.md): List of supported languages and instructions for adding new ones.
- [Markdown-Only Mode](./getting_started/markdown-only-mode.md): How to translate text only, without translating images.

## Video Presentations

Learn more about Co-op Translator through our presentations _(Click the image below to watch on YouTube.)_:

- **Open at Microsoft**: A concise 18-minute introduction and quick guide on how to use Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**: A detailed one-hour step-by-step walkthrough covering everything from understanding what Co-op Translator is, setting up the tool, and using it effectively, to a live demo showcasing its capabilities.

  [![Microsoft Reactor](../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## Support Us and Promote Global Learning

Join us in transforming how educational content is shared worldwide! Give [Co-op Translator](https://github.com/azure/co-op-translator) a ⭐ on GitHub and support our mission to remove language barriers in learning and technology. Your interest and contributions make a big difference! Contributions and feature suggestions are always welcome.

## Contributing

This project welcomes contributions and ideas. Interested in contributing to Azure Co-op Translator? Please see our [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on how you can help make Co-op Translator more accessible.

## Contributors

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information, see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any questions or comments.

## Responsible AI

Microsoft is committed to helping customers use our AI products responsibly, sharing our insights, and building trust-based partnerships through tools like Transparency Notes and Impact Assessments. Many of these resources are available at [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoft’s approach to responsible AI is based on our AI principles of fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability.

Large-scale natural language, image, and speech models—like those used in this sample—can sometimes behave in ways that are unfair, unreliable, or offensive, potentially causing harm. Please refer to the [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) to understand the risks and limitations.
The recommended approach to mitigating these risks is to include a safety system in your architecture that can detect and prevent harmful behavior. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) provides an independent layer of protection, capable of detecting harmful user-generated and AI-generated content in applications and services. Azure AI Content Safety includes text and image APIs that enable you to identify harmful material. We also offer an interactive Content Safety Studio that lets you view, explore, and try out sample code for detecting harmful content across different modalities. The following [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) guides you through making requests to the service.

Another factor to consider is the overall application performance. With multi-modal and multi-model applications, performance means that the system behaves as you and your users expect, including not producing harmful outputs. It's important to evaluate your application's overall performance using [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

You can assess your AI application in your development environment using the [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Whether you have a test dataset or a specific target, your generative AI application's outputs are quantitatively measured with built-in or custom evaluators of your choice. To get started with the prompt flow SDK for evaluating your system, follow the [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). After running an evaluation, you can [visualize the results in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos is subject to those third parties' policies.

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.