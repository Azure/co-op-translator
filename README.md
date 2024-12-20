![Logo](/imgs/logo.png)

# Co-op Translator: Localize Your Project with a Single Command

_Easily generate multilingual translations for your project with a single command, powered by Azure AI Services._

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

## 🤖 Supported models and services

| Type                  | Name                           |
|-----------------------|--------------------------------|
| Language Model        | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| Computer Vision       | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> If a computer vision service is not available, the co-op translator will switch to [Markdown-only mode](./getting_started/markdown-only-mode.md).

## 🌐 Overview

**Co-op Translator** is a Python package designed to automate multilingual translations for your projects using advanced Large Language Model (LLM) technology and Azure AI Services. This project aims to simplify the process of translating content into multiple languages, making it accessible and efficient for developers.

By integrating Co-op Translator into your workflow, you can automatically generate organized translation folders for different languages, and translate both Markdown files and images effortlessly.

Here is an example of how Co-op Translator structures the translations and translates both Markdown files and text within images in your project:

![Example](/imgs/translation-ex.png)

**Ready to unlock multilingual accessibility? Get started with Co-op Translator today!**

## ✨ Key features

- **Automated Translations**: Translate text into multiple languages effortlessly.
- **Markdown Preservation**: Maintain correct Markdown syntax during translation.
- **Image Text Translation**: Extract and translate text within images.
- **Advanced LLM Technology**: Utilize cutting-edge language models for high-quality translations.
- **Easy Integration**: Seamlessly integrate with your existing project setup.
- **Simplify Localization**: Streamline the process of localizing your project for international markets.

## 🌉 Bridging the language gap in tech

English is often considered the universal language of technology, but many developers worldwide are non-native English speakers. This can create barriers in accessing and contributing to technical projects.

**Co-op Translator** aims to break down these language barriers by providing an easy-to-use tool for automating translations. By making technical documentation accessible in multiple languages, we empower developers, students, and researchers globally.

## ⭐ Support us

Join us in revolutionizing global communication! Give a ⭐ to [Co-op Translator](https://github.com/azure/co-op-translator) on GitHub and help us break down language barriers together. Your support makes a difference!

## ⚙️ How it works

![Architecture](/imgs/architecture_241019.png)

The process begins with Markdown and image files from your project folder, which are processed by various AI services:

- **Language Models**: 
  - **Azure OpenAI** and other supported LLMs translate text from Markdown files. See the [supported models and services](#-supported-models-and-services) for more information.
- **Computer Vision Services** (optional): 
  - **Azure Computer Vision** extracts text from images, which are then translated by the selected language model. If a computer vision service is not available, the process defaults to [Markdown-only mode](./getting_started/markdown-only-mode.md).

The final translated Markdown and image files are saved in the designated translation folder, ready to be used in multiple languages.

## 🚀 Getting started with Co-op Translator

### Prerequisites

- **Python 3.10 or higher**: Required for running the Co-op Translator.
- **Language Model Resource**: 
  - **Azure OpenAI** or other LLMs. Details can be found in the [supported models and services](#-supported-models-and-services).
- **Computer Vision Resource** (optional):
  - For image translation. If unavailable, the translator defaults to [Markdown-only mode](./getting_started/markdown-only-mode.md).
  - **Azure Computer Vision**

### Quick install

#### Install via pip

```bash
pip install co-op-translator
```

#### Install via poetry

```bash
poetry add co-op-translator
```

### How to use Co-op Translator

> [!NOTE]
> While this tutorial focuses on Azure resources, you can use any supported language model from the [supported models and services](#-supported-models-and-services) list.

1. Set up resources
   - [Set up Azure OpenAI](./getting_started/set-up-resources/set-up-azure-openai.md)
   - [Set up Azure Computer Vision](./getting_started/set-up-resources/set-up-azure-computer-vision.md) (optional)

2. [Create an '.env' file in the root directory](./getting_started/create-env-file.md)
   - Include necessary keys for the chosen language model service.
   - If Azure Computer Vision keys are omitted or `-md` is specified, the translator will operate in Markdown-only mode.
3. [Install the Co-op translator package](./getting_started/install-package.md)
4. [Translate your project using Co-op Translator](./getting_started/translator-your-project.md)

### Additional resources

- [Command reference](./getting_started/command-reference.md): Learn about all available commands and their options in detail.
- [Multi-language support setup](./getting_started/multi-language-support.md): Before starting the translation process, you can add a table in the README that links to the translated versions of your document.
- [Supported Languages](./getting_started/supported-languages.md): Check the list of supported languages and instructions to add new languages.
- [Markdown-Only Mode](./getting_started/markdown-only-mode.md): Learn how to use Co-op Translator in Markdown-only mode.

## 📚 Case Studies: Applying Co-op Translator in real projects

These case studies show how Co-op Translator was applied to translate a real-world project. It highlights the translation process, the challenges encountered, and the results achieved, providing a useful reference for applying the tool to similar projects.

1. [Phi-3 Cookbook translation: A case study](./getting_started/Phi-3Cookbook-translation-case.md)

## 🎥 Video presentations

Learn more about Co-op Translator through our presentations _(Click the image below to watch on YouTube.)_:

- **Open at Microsoft**: A brief 18-minute introduction and quick guide on how to use Co-op Translator.

  [![Open at Microsoft](/imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**: A one-hour detailed step-by-step guide covering everything from understanding what Co-op Translator is, setting up the tool, and using it effectively, to a live demo showcasing its capabilities in action.

  [![Microsoft Reactor](/imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## Contributing

This project welcomes contributions and suggestions. Interested in contributing to Azure Co-op Translator? Please see our [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on how you can help make Co-op Translator more accessible.

## Contributors

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Responsible AI

Microsoft is committed to helping our customers use our AI products responsibly, sharing our learnings, and building trust-based partnerships through tools like Transparency Notes and Impact Assessments. Many of these resources can be found at [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoft’s approach to responsible AI is grounded in our AI principles of fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability.

Large-scale natural language, image, and speech models - like the ones used in this sample - can potentially behave in ways that are unfair, unreliable, or offensive, in turn causing harms. Please consult the [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) to be informed about risks and limitations.

The recommended approach to mitigating these risks is to include a safety system in your architecture that can detect and prevent harmful behavior. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) provides an independent layer of protection, able to detect harmful user-generated and AI-generated content in applications and services. Azure AI Content Safety includes text and image APIs that allow you to detect material that is harmful. We also have an interactive Content Safety Studio that allows you to view, explore and try out sample code for detecting harmful content across different modalities. The following [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) guides you through making requests to the service.

Another aspect to take into account is the overall application performance. With multi-modal and multi-models applications, we consider performance to mean that the system performs as you and your users expect, including not generating harmful outputs. It's important to assess the performance of your overall application using [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

You can evaluate your AI application in your development environment using the [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Given either a test dataset or a target, your generative AI application generations are quantitatively measured with built-in evaluators or custom evaluators of your choice. To get started with the prompt flow sdk to evaluate your system, you can follow the [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Once you execute an evaluation run, you can [visualize the results in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
