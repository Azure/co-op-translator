<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "329abbc9354793ea422f7e7ebf66be2c",
  "translation_date": "2025-05-07T01:51:49+00:00",
  "source_file": "README.md",
  "language_code": "zh"
}
-->
![Logo](../../imgs/logo.png)

# Co-op Translator：轻松实现教育文档的自动翻译

_轻松将您的文档自动翻译成多种语言，触达全球受众。_

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 由 Co-op Translator 支持的语言

[Korean](../ko/README.md) | [Japanese](../ja/README.md) | [Chinese (Simplified)](./README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Spanish](../es/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Portuguese (Brazil)](../br/README.md) | [Hindi](../hi/README.md) | [Russian](../ru/README.md) | [Turkish](../tr/README.md) | [Arabic](../ar/README.md) | [Indonesian](../id/README.md) | [Vietnamese](../vi/README.md)

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
>
> **强大自动化**：现已支持 GitHub Actions！当仓库内容发生更改时，自动翻译您的文档，轻松保持内容最新。[了解更多](../..)。

## 支持的模型和服务

| 类型                   | 名称                            |
|-----------------------|--------------------------------|
| 语言模型              | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| 计算机视觉            | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> 如果计算机视觉服务不可用，co-op translator 将切换到 [仅 Markdown 模式](./getting_started/markdown-only-mode.md)。

## 概览：简化您的教育内容翻译

语言障碍严重阻碍了全球学习者和开发者获取宝贵的教育资源和技术知识，限制了参与度，减缓了全球创新和学习的步伐。

**Co-op Translator** 诞生于解决微软自身大型教育系列（如“入门指南”）手动翻译效率低下的问题。它已发展成为一个易用且强大的工具，旨在为所有人打破语言壁垒。通过命令行界面和 GitHub Actions 提供高质量的自动翻译，Co-op Translator 赋能全球的教育者、学生、研究人员和开发者，无语言限制地分享和获取知识。

看看 Co-op Translator 如何组织翻译后的教育内容：

![示例](../../imgs/translation-ex.png)

Markdown 文件和图片中的文本会被自动翻译，并整齐地归档到按语言划分的文件夹中。

**立即使用 Co-op Translator，解锁您的教育内容全球访问！**

## 支持微软学习资源的全球访问

Co-op Translator 帮助弥合微软关键教育项目的语言鸿沟，自动化翻译服务全球开发者社区的仓库。目前使用 Co-op Translator 的示例包括：

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## 主要功能

- **自动翻译**：轻松将文本翻译成多种语言。
- **GitHub Actions 集成**：将翻译自动化纳入您的 CI/CD 流程。
- **保留 Markdown 格式**：翻译过程中保持正确的 Markdown 语法。
- **图片文本翻译**：提取并翻译图片中的文本。
- **先进的 LLM 技术**：使用最前沿的语言模型，确保高质量翻译。
- **轻松集成**：无缝结合您现有的项目配置。
- **简化本地化**：优化项目面向国际市场的本地化流程。

## 工作原理

![架构](../../imgs/architecture_241019.png)

Co-op Translator 从您的项目文件夹中获取 Markdown 文件和图片，按以下步骤处理：

1. **文本提取**：从 Markdown 文件中提取文本，若配置了（如 Azure 计算机视觉），还会提取图片中的嵌入文本。
1. **AI 翻译**：将提取的文本发送到配置的 LLM（Azure OpenAI、OpenAI 等）进行翻译。
1. **结果保存**：将翻译后的 Markdown 文件和图片（含翻译文本）保存到按语言划分的文件夹，保持原有格式。

## 快速入门

快速通过命令行开始，或通过 GitHub Actions 设置完整自动化。

### 快速开始：命令行

通过命令行快速启动：

1. 安装包：
    ```bash
    pip install co-op-translator
    ```
2. 配置凭据：
  - 创建 `.env` file in your project's root directory.
  - Copy the contents from the [.env.template](../../.env.template) file into your new `.env` file.
  - Fill in the required API keys and endpoint information in your `.env` file.
3. Run Translation:
  - Navigate to your project's root directory in your terminal.
  - Execute the translate command, specifying target languages with the `-l` 标志：
    ```bash
    translate -l "ko ja fr"
    ```
    *(替换 `"ko ja fr"` with your desired space-separated language codes)*

### Detailed Usage Guides

Choose the approach that best fits your workflow:

#### 1. Using the Command Line (CLI)

- Best for: One-time translations, manual control, or integration into custom scripts.
- Requires: Local installation of Python and the `co-op-translator` package.
- Guide: [Command Line Guide](./getting_started/command-line-guide/command-line-guide.md)

#### 2. Using GitHub Actions (Automation)

- Best for: Automatically translating content whenever changes are pushed to your repository. Keeps translations consistently up-to-date.
- Requires: Setting up a workflow file (`.github/workflows`)，无需本地安装。
- 指南：
  - [GitHub Actions 指南（公共仓库和标准密钥）](./getting_started/github-actions-guide/github-actions-guide-public.md) - 适用于大多数公共或个人仓库，使用标准仓库密钥。
  - [GitHub Actions 指南（微软组织仓库及组织级设置）](./getting_started/github-actions-guide/github-actions-guide-org.md) - 适用于微软 GitHub 组织内，或需要使用组织级密钥或运行器的场景。

> [!NOTE]
> 本教程以 Azure 资源为例，但您也可以使用[支持的模型和服务](../..)列表中的任何语言模型。

### 故障排除与技巧

- [故障排除指南](./getting_started/troubleshooting.md)

### 其他资源

- [命令参考](./getting_started/command-reference.md)：详细介绍所有可用命令和选项。
- [多语言支持设置](./getting_started/multi-language-support.md)：如何在 README 中添加链接到翻译版本的表格。
- [支持的语言](./getting_started/supported-languages.md)：查看支持的语言列表及添加新语言的说明。
- [仅 Markdown 模式](./getting_started/markdown-only-mode.md)：仅翻译文本，不进行图片翻译的方法。

## 视频介绍

通过我们的演示视频了解更多关于 Co-op Translator 的信息 _(点击下方图片在 YouTube 观看)_：

- **Open at Microsoft**：简短的18分钟介绍和快速使用指南。

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**：一小时详细分步教程，涵盖 Co-op Translator 的概念介绍、工具设置、有效使用及现场演示。

  [![Microsoft Reactor](../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## 支持我们，促进全球学习

加入我们，革新教育内容的全球分享方式！在 GitHub 上为 [Co-op Translator](https://github.com/azure/co-op-translator) 点⭐，支持我们打破学习和技术中的语言障碍。您的关注和贡献意义重大！欢迎代码贡献和功能建议。

## 贡献指南

本项目欢迎贡献和建议。想为 Azure Co-op Translator 贡献力量？请参阅我们的 [CONTRIBUTING.md](./CONTRIBUTING.md)，了解如何帮助提升 Co-op Translator 的可用性。

## 贡献者

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行为准则

本项目采用了 [Microsoft 开源行为准则](https://opensource.microsoft.com/codeofconduct/)。
更多信息请参见 [行为准则常见问题](https://opensource.microsoft.com/codeofconduct/faq/) 或
联系 [opencode@microsoft.com](mailto:opencode@microsoft.com) 反馈问题或建议。

## 负责任的人工智能

微软致力于帮助客户负责任地使用我们的 AI 产品，分享我们的经验，并通过透明度说明和影响评估等工具建立基于信任的合作关系。许多相关资源可在 [https://aka.ms/RAI](https://aka.ms/RAI) 找到。
微软的负责任 AI 方法基于我们的 AI 原则：公平性、可靠性与安全性、隐私与安全、包容性、透明度和问责制。

大规模的自然语言、图像和语音模型——如本示例中使用的模型——可能会出现不公平、不可靠或冒犯性的行为，从而造成伤害。请查阅 [Azure OpenAI 服务透明度说明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)，了解相关风险和限制。
减轻这些风险的推荐方法是在您的架构中包含一个安全系统，能够检测并防止有害行为。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供了一个独立的保护层，能够检测应用程序和服务中的用户生成和 AI 生成的有害内容。Azure AI Content Safety 包含文本和图像 API，允许您检测有害材料。我们还提供了一个交互式的 Content Safety Studio，您可以在其中查看、探索并试用针对不同模态检测有害内容的示例代码。以下[快速入门文档](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)将引导您完成向该服务发送请求的流程。

另一个需要考虑的方面是整体应用性能。对于多模态和多模型应用，我们认为性能意味着系统能够按您和用户的预期运行，包括不生成有害输出。评估整体应用的性能时，重要的是使用[生成质量以及风险和安全指标](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)。

您可以使用[prompt flow SDK](https://microsoft.github.io/promptflow/index.html)在开发环境中评估您的 AI 应用。无论是测试数据集还是目标，您的生成式 AI 应用的生成结果都可以通过内置评估器或您选择的自定义评估器进行量化测量。要开始使用 prompt flow sdk 评估系统，可以参考[快速入门指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。执行评估运行后，您可以在[Azure AI Studio 中可视化结果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商标

本项目可能包含项目、产品或服务的商标或标识。微软商标或标识的授权使用须遵守并遵循[微软商标和品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。在本项目的修改版本中使用微软商标或标识不得引起混淆或暗示微软的赞助。任何第三方商标或标识的使用均须遵守相关第三方的政策。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们努力保证准确性，但请注意自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。