# Co-op Translator

_Easily automate multilingual translations for your projects with co-op-translator, powered by advanced LLM technology and Azure AI Services._

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

## Overview

**Co-op Translator** is a Python package designed to automate multilingual translations for your projects using advanced Large Language Model (LLM) technology and Azure AI Services. This project aims to simplify the process of translating content into multiple languages, making it accessible and efficient for developers.

By integrating Co-op Translator into your workflow, you can effortlessly manage multilingual support while focusing on core functionalities.

Here is an example of how Co-op Translator can be used to translate text in images and markdown files in your project:

![Example](/imgs/ex.png)

### Key features

- **Automated translations**: Easily translate text in your project files into multiple languages.
- **Comprehensive coverage**: Translate all markdown files and text within images in your project directories.
- **Advanced LLM technology**: Utilize cutting-edge language models for high-quality translations.
- **Simplify localization**: Streamline the process of localizing your project for international markets.
- **Easy integration**: Seamlessly integrate with your existing project setup.

### How it works

![Architecture](/imgs/Architecture.png)

The process begins with markdown and image files from your project folder, which are processed by **Azure AI Services**:

- **Azure OpenAI**: Translates text from markdown files.
- **Azure Computer Vision**: Extracts text from images, which are then translated by Azure OpenAI.

The final translated markdown and image files are saved in the designated translation folder, ready to be used in multiple languages.

## Getting started with Co-op Translator

### Prerequisites

- Azure Computer vision resource
- Azure OpenAI resource
- Python 3.10 or higher

### Quick install

#### Install Co-op Translator via pip

```bash
pip install co-op-translator
```

#### Install Co-op Translator via poetry

```bash
poetry add co-op-translator
```

### How to use Co-op Translator

1. [Set up Azure resources before starting](./getting_started/set-up-azure-resources.md)
1. [Create an '.env' file in the root directory](./getting_started/create-env-file.md)
1. [Install the Co-op translator package](./getting_started/install-package.md)
1. [Translate your project using Co-op Translator](./getting_started/translator-your-project.md)

### Case Studies: Applying Co-op Translator in real projects

These case studies show how Co-op Translator was applied to translate a real-world project. It highlights the translation process, the challenges encountered, and the results achieved, providing a useful reference for applying the tool to similar projects.

1. [Phi-3 Cookbook translation: A case study](./getting_started/Phi-3Cookbook-translation-case.md)

## Supported languages

The table below lists the languages currently supported by **Co-op Translator**. It includes language codes, language names, and any known issues associated with each language. If you would like to add support for a new language, please add the corresponding language code, name, and appropriate font in the `font_language_mappings.yml` file located at `src/co_op_translator/fonts/` and submit a pull request after testing.

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | English              | NotoSans-Medium.ttf               | No          | No           |
| fr            | French               | NotoSans-Medium.ttf               | No          | No           |
| es            | Spanish              | NotoSans-Medium.ttf               | No          | No           |
| de            | German               | NotoSans-Medium.ttf               | No          | No           |
| ru            | Russian              | NotoSans-Medium.ttf               | No          | No           |
| ar            | Arabic               | NotoSansArabic-Medium.ttf         | Yes         | Yes          |
| fa            | Persian (Farsi)      | NotoSansArabic-Medium.ttf         | Yes         | Yes          |
| ur            | Urdu                 | NotoSansArabic-Medium.ttf         | Yes         | Yes          |
| zh            | Chinese (Simplified) | NotoSansCJK-Medium.ttc            | No          | No           |
| mo            | Chinese (Traditional) | NotoSansCJK-Medium.ttc           | No          | No           |
| hk            | Chinese (Traditional) | NotoSansCJK-Medium.ttc           | No          | No           |
| tw            | Chinese (Traditional) | NotoSansCJK-Medium.ttc           | No          | No           |
| ja            | Japanese             | NotoSansCJK-Medium.ttc            | No          | No           |
| ko            | Korean               | NotoSansCJK-Medium.ttc            | No          | No           |
| hi            | Hindi                | NotoSansDevanagari-Medium.ttf     | No          | No           |
| bn            | Bengali              | NotoSansBengali-Medium.ttf        | No          | No           |
| mr            | Marathi              | NotoSansDevanagari-Medium.ttf     | No          | No           |
| ne            | Nepali               | NotoSansDevanagari-Medium.ttf     | No          | No           |
| pa            | Punjabi (Gurmukhi)   | NotoSansGurmukhi-Medium.ttf       | No          | No           |
| pt            | Portuguese           | NotoSans-Medium.ttf               | No          | No           |
| it            | Italian              | NotoSans-Medium.ttf               | No          | No           |
| pl            | Polish               | NotoSans-Medium.ttf               | No          | No           |
| tr            | Turkish              | NotoSans-Medium.ttf               | No          | No           |
| el            | Greek                | NotoSans-Medium.ttf               | No          | No           |
| th            | Thai                 | NotoSansThai-Medium.ttf           | No          | No           |
| sv            | Swedish              | NotoSans-Medium.ttf               | No          | No           |
| da            | Danish               | NotoSans-Medium.ttf               | No          | No           |
| no            | Norwegian            | NotoSans-Medium.ttf               | No          | No           |
| fi            | Finnish              | NotoSans-Medium.ttf               | No          | No           |
| nl            | Dutch                | NotoSans-Medium.ttf               | No          | No           |
| he            | Hebrew               | NotoSansHebrew-Medium.ttf         | Yes         | No           |
| vi            | Vietnamese           | NotoSans-Medium.ttf               | No          | No           |
| id            | Indonesian           | NotoSans-Medium.ttf               | No          | No           |
| ms            | Malay                | NotoSans-Medium.ttf               | No          | No           |
| tl            | Tagalog (Filipino)   | NotoSans-Medium.ttf               | No          | No           |
| sw            | Swahili              | NotoSans-Medium.ttf               | No          | No           |
| hu            | Hungarian            | NotoSans-Medium.ttf               | No          | No           |
| cs            | Czech                | NotoSans-Medium.ttf               | No          | No           |
| sk            | Slovak               | NotoSans-Medium.ttf               | No          | No           |
| ro            | Romanian             | NotoSans-Medium.ttf               | No          | No           |
| bg            | Bulgarian            | NotoSans-Medium.ttf               | No          | No           |
| sr            | Serbian (Cyrillic)   | NotoSans-Medium.ttf               | No          | No           |
| hr            | Croatian             | NotoSans-Medium.ttf               | No          | No           |
| sl            | Slovenian            | NotoSans-Medium.ttf               | No          | No           |

### Adding a new language

To add support for a new language:

1. Go to [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml).
2. Add the language code, name, and appropriate font file name. Make sure to include the `rtl` attribute if the language is right-to-left.
3. If you need to use a new font, ensure that the font is free to use in open-source projects by checking its licensing and copyright terms. After verifying, add the font file to the `src/co_op_translator/fonts/` directory.
4. Test your changes locally to ensure that the new language is properly supported.
5. Submit a Pull Request with your changes and indicate the addition of the new language in the PR description.

Example:

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

## Repository Structure

- **src/co_op_translator/**: Source code for the translator.
- **getting_started/**: Guides and tutorials to get started.
- **imgs/**: Images used in documentation.
- **tests/**: Test cases for the project.
- **data/**: Contains data files.

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
