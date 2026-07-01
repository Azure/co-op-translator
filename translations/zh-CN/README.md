# Co-op Translator

_轻松自动化并维护随项目发展而更新的教育类 GitHub 内容的多语言翻译。_

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python 包](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![许可证: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![下载量](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![下载量](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![容器: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![代码风格: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub 贡献者](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub 问题](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub 拉取请求](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![欢迎 PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**开始使用：** [选择你的工作流](https://azure.github.io/co-op-translator/workflows/) | [配置](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP 服务器](https://azure.github.io/co-op-translator/mcp/)

### 🌐 多语言支持

#### 由 [Co-op Translator](https://github.com/Azure/co-op-translator) 支持

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯语](../ar/README.md) | [孟加拉语](../bn/README.md) | [保加利亚语](../bg/README.md) | [缅甸语（缅甸）](../my/README.md) | [中文（简体）](./README.md) | [中文（繁体，香港）](../zh-HK/README.md) | [中文（繁体，澳门）](../zh-MO/README.md) | [中文（繁体，台湾）](../zh-TW/README.md) | [克罗地亚语](../hr/README.md) | [捷克语](../cs/README.md) | [丹麦语](../da/README.md) | [荷兰语](../nl/README.md) | [爱沙尼亚语](../et/README.md) | [芬兰语](../fi/README.md) | [法语](../fr/README.md) | [德语](../de/README.md) | [希腊语](../el/README.md) | [希伯来语](../he/README.md) | [印地语](../hi/README.md) | [匈牙利语](../hu/README.md) | [印尼语](../id/README.md) | [意大利语](../it/README.md) | [日语](../ja/README.md) | [卡纳达语](../kn/README.md) | [高棉语](../km/README.md) | [韩语](../ko/README.md) | [立陶宛语](../lt/README.md) | [马来语](../ms/README.md) | [马拉雅拉姆语](../ml/README.md) | [马拉地语](../mr/README.md) | [尼泊尔语](../ne/README.md) | [尼日利亚皮钦语](../pcm/README.md) | [挪威语](../no/README.md) | [波斯语（Farsi）](../fa/README.md) | [波兰语](../pl/README.md) | [葡萄牙语（巴西）](../pt-BR/README.md) | [葡萄牙语（葡萄牙）](../pt-PT/README.md) | [旁遮普语（Gurmukhi）](../pa/README.md) | [罗马尼亚语](../ro/README.md) | [俄语](../ru/README.md) | [塞尔维亚语（西里尔文）](../sr/README.md) | [斯洛伐克语](../sk/README.md) | [斯洛文尼亚语](../sl/README.md) | [西班牙语](../es/README.md) | [斯瓦希里语](../sw/README.md) | [瑞典语](../sv/README.md) | [他加禄语（菲律宾语）](../tl/README.md) | [泰米尔语](../ta/README.md) | [泰卢固语](../te/README.md) | [泰语](../th/README.md) | [土耳其语](../tr/README.md) | [乌克兰语](../uk/README.md) | [乌尔都语](../ur/README.md) | [越南语](../vi/README.md)

> **更喜欢本地克隆？**
>
> 该仓库包含 50+ 种语言的翻译，显著增加了下载大小。若要在不包含翻译的情况下克隆，请使用稀疏检出：
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
> 这会为您提供完成课程所需的一切，同时大幅加快下载速度。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub 关注者](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub 分叉](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub 星标](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![在 GitHub Codespaces 中打开](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 概述

**Co-op Translator** 帮助您将教育类 GitHub 内容轻松本地化为多种语言。当您更新 Markdown 文件、图像或笔记本时，翻译会自动保持同步，确保您的内容对全球的学习者而言准确且实时更新。

可以通过 CLI 在仓库层面进行翻译，通过 Python API 实现自动化，或通过 MCP 服务器用于代理和编辑器工作流。

翻译内容的组织示例：

![示例](../../imgs/translation-ex.png)

## 为什么选择 Co-op Translator？

翻译单个文件很容易。保持整个文档仓库被翻译、互相链接并保持最新才是难点。

| 问题 | Co-op Translator 如何帮助 |
| --- | --- |
| 长文档不能只用一个提示完成 | 大型 Markdown 文件会被拆分为多个片段，因此一个很长的 README 不依赖于一次脆弱的模型响应。如果某个片段失败，Co-op Translator 可以重试并仅对失败的部分重新分块。 |
| 不完整的翻译不应标记为当前 | 截断的翻译不应被封存为最新。Co-op Translator 在保存前会检查翻译完整性，并能检测结构上不完整的现有翻译。 |
| 链接应与翻译后的仓库结构匹配 | 手动翻译常常会留下指向源树的相对链接。Co-op Translator 会重写 Markdown、笔记本、图像和 README 的链接以匹配 `translations/<lang>/...` 结构。 |
| 翻译应适用于整个仓库 | Co-op Translator 将 README 文件、文档、笔记本和图像文本作为一个仓库工作流的一部分处理，而不是逐个文件地翻译。 |
| 比起一次性创建，维护翻译更重要 | 源哈希和翻译元数据让 Co-op Translator 能发现过期文件、跳过未更改的文件，并在源仓库演进时保持翻译内容的同步。 |

## 翻译状态如何管理

Co-op Translator 将翻译内容管理为 <strong>版本化的软件制品</strong>，  
而非静态文件。

该工具使用 <strong>按语言范围的元数据</strong> 跟踪已翻译的 Markdown、图像和笔记本的状态。

此设计允许 Co-op Translator：

- 可靠地检测过期翻译
- 一致地处理 Markdown、图像和笔记本
- 安全地扩展到大型、快速变化的多语言仓库

通过将翻译建模为受管理的制品，
翻译工作流自然而然地与现代的软件依赖和制品管理实践对齐。

→ [如何管理翻译状态](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### 相关深度文章

- [修复 AI 翻译中损坏的 Markdown：加强生产流水线](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## 开始使用

Co-op Translator 可以通过 CLI、Python API 或 MCP 服务器使用。如果您在本地翻译、自动化、CI 与代理/编辑器集成之间选择，请先阅读工作流指南。

- [选择你的工作流](../../docs/workflows.md)
- [配置凭据](../../docs/configuration.md)
- [从 CLI 翻译](../../docs/cli.md)
- [使用 Python API 自动化](../../docs/api.md)
- [连接到 MCP 服务器](../../docs/mcp.md)
- [在 GitHub Actions 中运行](../../docs/github-actions.md)

配置后的最小 CLI 示例：

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

对于大型仓库的首次运行，在写入翻译文件之前请使用 `--dry-run`。有关内容类型标志、日志、审查和链接迁移的信息，请参阅 [CLI 参考](../../docs/cli.md)。

使用 Bash/Zsh 的容器快速运行：

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

使用 PowerShell 的容器快速运行：

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## 功能

- 自动翻译 Markdown、笔记本和图像
- 使翻译与源更改保持同步
- 可在本地（CLI）或 CI（GitHub Actions）中运行
- 通过 MCP 提供 Markdown、笔记本、图像、审查和项目翻译工具
- 使用 Azure OpenAI 或 OpenAI 作为翻译提供方
- 允许 MCP 托管的代理在无需 Co-op Translator LLM 凭据的情况下翻译 Markdown 和笔记本片段
- 使用 Azure AI Vision 提取并翻译图像文本
- 使用确定性检查审查翻译结构和新鲜度
- 保留 Markdown 格式和结构

## 文档

- [文档站点](https://azure.github.io/co-op-translator/)
- [选择你的工作流](../../docs/workflows.md)
- [配置](../../docs/configuration.md)
- [Azure AI 设置](../../docs/azure-ai-setup.md)
- [CLI 参考](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP 服务器](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README 语言模板](../../docs/readme-languages-template.md)
- [支持的语言](../../docs/supported-languages.md)
- [贡献](../../CONTRIBUTING.md)
- [疑难解答](../../docs/troubleshooting.md)

### 面向微软的专门指南
> [!NOTE]
> 仅适用于 Microsoft “For Beginners” 仓库的维护者。

- [更新 “other courses” 列表（仅适用于 Microsoft For Beginners 仓库）](../../docs/microsoft-beginners.md)

## 支持我们并促进全球学习

加入我们，一起革新教育内容的全球分享方式！在 GitHub 上为 [Co-op Translator](https://github.com/azure/co-op-translator) 点 ⭐，支持我们打破学习与科技中的语言障碍的使命。您的关注和贡献具有重要影响！代码贡献和功能建议随时欢迎。

### 以你的语言探索微软教育内容
- [LangChain4j 入门](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD 入门](https://github.com/microsoft/AZD-for-beginners)
- [边缘 AI 入门](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) 入门](https://github.com/microsoft/mcp-for-beginners)
- [AI 代理 入门](https://github.com/microsoft/ai-agents-for-beginners)
- [使用 .NET 的生成式 AI 入门](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [生成式 AI 入门](https://github.com/microsoft/generative-ai-for-beginners)
- [使用 Java 的生成式 AI 入门](https://github.com/microsoft/generative-ai-for-beginners-java)
- [机器学习 入门](https://aka.ms/ml-beginners)
- [数据科学 入门](https://aka.ms/datascience-beginners)
- [人工智能 入门](https://aka.ms/ai-beginners)
- [网络安全 入门](https://github.com/microsoft/Security-101)
- [Web 开发 入门](https://aka.ms/webdev-beginners)
- [物联网 入门](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## 视频演示

👉 点击下方图片在 YouTube 上观看。

- **Open at Microsoft**：一个简短的 18 分钟介绍，快速指南教您如何使用 Co-op Translator。

  [![在微软公开演示](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 贡献

本项目欢迎贡献与建议。想为 Azure Co-op Translator 作出贡献吗？请参阅我们的 [CONTRIBUTING.md](../../CONTRIBUTING.md) 了解如何帮助使 Co-op Translator 更易于使用的指南。

## 贡献者

[![co-op-translator 贡献者](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行为守则

本项目已采纳 [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)。
欲了解更多信息，请参阅 [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ，或将任何其他问题或意见发送至 [opencode@microsoft.com](mailto:opencode@microsoft.com)。

## 负责任的 AI

Microsoft 致力于帮助我们的客户负责任地使用我们的 AI 产品，分享我们的经验，并通过 Transparency Notes 和 Impact Assessments 等工具建立基于信任的合作关系。许多这些资源可在 [https://aka.ms/RAI](https://aka.ms/RAI) 找到。
Microsoft 的负责任 AI 方法基于我们的 AI 原则：公平、可靠与安全、隐私与安全、包容性、透明性和问责制。

大规模的自然语言、图像和语音模型（例如本示例中使用的模型）可能会表现出不公平、不可靠或冒犯性的行为，从而造成伤害。请参阅 [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) 以了解相关风险和限制。

缓解这些风险的推荐方法是在您的架构中包含一个安全系统，能够检测并阻止有害行为。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供了一个独立的保护层，能够检测应用和服务中的用户生成和 AI 生成的有害内容。Azure AI Content Safety 包含文本和图像 API，允许您检测有害材料。我们还有一个交互式的 Content Safety Studio，允许您查看、探索并尝试用于不同模态检测有害内容的示例代码。下面的 [快速入门文档](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) 将引导您如何向该服务发出请求。

另一个需要考虑的方面是整体应用的性能。对于多模态和多模型的应用，我们将性能视为系统能够按照您和用户的期望运行，包括不会生成有害输出。使用 [生成质量与风险安全指标](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) 评估您整体应用的性能非常重要。

您可以使用 [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) 在开发环境中评估您的 AI 应用。无论是使用测试数据集还是目标，您的生成式 AI 应用的生成结果都可以用内置评估器或您选择的自定义评估器进行量化测量。要开始使用 prompt flow SDK 来评估系统，您可以遵循[快速入门指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。执行评估运行后，您可以[在 Azure AI Studio 中可视化结果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商标

本项目可能包含项目、产品或服务的商标或徽标。对 Microsoft 商标或徽标的授权使用须遵循并受限于 [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。
在本项目的修改版本中使用 Microsoft 商标或徽标不得引起混淆或暗示 Microsoft 的赞助。
任何第三方商标或徽标的使用须遵守该第三方的政策。

## 获取帮助

如果在构建 AI 应用时遇到困难或有任何问题，请加入：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如果在构建过程中有产品反馈或遇到错误，请访问：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)