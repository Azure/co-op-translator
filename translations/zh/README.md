<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T10:08:16+00:00",
  "source_file": "README.md",
  "language_code": "zh"
}
-->
# Co-op 翻译器

_轻松自动将您的教育类 GitHub 内容翻译成多种语言，触达全球受众。_

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

### 🌐 多语言支持

#### 由 [Co-op Translator](https://github.com/Azure/Co-op-Translator) 提供支持

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯语](../ar/README.md) | [孟加拉语](../bn/README.md) | [保加利亚语](../bg/README.md) | [缅甸语](../my/README.md) | [中文（简体）](./README.md) | [中文（繁体，香港）](../hk/README.md) | [中文（繁体，澳门）](../mo/README.md) | [中文（繁体，台湾）](../tw/README.md) | [克罗地亚语](../hr/README.md) | [捷克语](../cs/README.md) | [丹麦语](../da/README.md) | [荷兰语](../nl/README.md) | [爱沙尼亚语](../et/README.md) | [芬兰语](../fi/README.md) | [法语](../fr/README.md) | [德语](../de/README.md) | [希腊语](../el/README.md) | [希伯来语](../he/README.md) | [印地语](../hi/README.md) | [匈牙利语](../hu/README.md) | [印尼语](../id/README.md) | [意大利语](../it/README.md) | [日语](../ja/README.md) | [卡纳达语](../kn/README.md) | [韩语](../ko/README.md) | [立陶宛语](../lt/README.md) | [马来语](../ms/README.md) | [马拉雅拉姆语](../ml/README.md) | [马拉地语](../mr/README.md) | [尼泊尔语](../ne/README.md) | [尼日利亚皮钦语](../pcm/README.md) | [挪威语](../no/README.md) | [波斯语（法尔西语）](../fa/README.md) | [波兰语](../pl/README.md) | [葡萄牙语（巴西）](../br/README.md) | [葡萄牙语（葡萄牙）](../pt/README.md) | [旁遮普语（古鲁姆奇）](../pa/README.md) | [罗马尼亚语](../ro/README.md) | [俄语](../ru/README.md) | [塞尔维亚语（西里尔字母）](../sr/README.md) | [斯洛伐克语](../sk/README.md) | [斯洛文尼亚语](../sl/README.md) | [西班牙语](../es/README.md) | [斯瓦希里语](../sw/README.md) | [瑞典语](../sv/README.md) | [他加禄语（菲律宾语）](../tl/README.md) | [泰米尔语](../ta/README.md) | [泰卢固语](../te/README.md) | [泰语](../th/README.md) | [土耳其语](../tr/README.md) | [乌克兰语](../uk/README.md) | [乌尔都语](../ur/README.md) | [越南语](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=关注)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=分叉)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=收藏)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![在 GitHub Codespaces 中打开](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=打开&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 概览

**Co-op 翻译器** 帮助您轻松将教育类 GitHub 内容本地化为多种语言。
当您更新 Markdown 文件、图片或笔记本时，翻译内容会自动同步，确保您的内容对全球学习者始终准确且最新。

翻译内容的组织示例：

![示例](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.zh.png)

## 快速开始

```bash
# 创建并激活虚拟环境（推荐）
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# 安装软件包
pip install co-op-translator
# 翻译
translate -l "ko ja fr" -md
```

Docker：

```bash
# 从 GHCR 拉取公共镜像
docker pull ghcr.io/azure/co-op-translator:latest
# 运行时挂载当前文件夹并提供 .env（Bash/Zsh）
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## 最简配置

1. 使用模板创建 `.env` 文件：[.env.template](../../.env.template)
2. 配置一个 LLM 提供商（Azure OpenAI 或 OpenAI）
3. （可选）若需图片翻译（`-img`），配置 Azure AI Vision
4. （推荐）清理之前的翻译内容以避免冲突（例如 `translations/`）
5. （推荐）在 README 中添加翻译语言部分，使用 [README 语言模板](./getting_started/README_languages_template.md)
6. 参见：[设置 Azure AI](./getting_started/set-up-azure-ai.md)

## 使用方法

翻译所有支持的类型：

```bash
translate -l "ko ja"
```

仅翻译 Markdown：

```bash
translate -l "de" -md
```

Markdown + 图片：

```bash
translate -l "pt" -md -img
```

仅翻译笔记本：

```bash
translate -l "zh" -nb
```

更多参数：[命令参考](./getting_started/command-reference.md)

## 功能

- 自动翻译 Markdown、笔记本和图片
- 保持翻译与源内容同步更新
- 支持本地（CLI）和 CI（GitHub Actions）环境
- 使用 Azure OpenAI 或 OpenAI；图片翻译可选 Azure AI Vision
- 保留 Markdown 格式和结构

## 文档

- [命令行指南](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions 指南（公共仓库 & 标准密钥）](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions 指南（微软组织仓库 & 组织级设置）](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README 语言模板](./getting_started/README_languages_template.md)
- [支持的语言](./getting_started/supported-languages.md)
- [贡献指南](./CONTRIBUTING.md)
- [故障排除](./getting_started/troubleshooting.md)

### 微软专用指南
> [!NOTE]
> 仅适用于微软“初学者”仓库的维护者。

- [更新“其他课程”列表（仅限微软初学者仓库）](./getting_started/update-other-courses.md)

## 支持我们，促进全球学习

加入我们，一起革新教育内容的全球分享方式！请在 GitHub 上为 [Co-op Translator](https://github.com/azure/co-op-translator) 点⭐，支持我们打破学习和技术中的语言障碍。您的关注和贡献意义重大！欢迎代码贡献和功能建议。

### 用您的语言探索微软教育内容

- [AZD 初学者](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI 初学者](https://github.com/microsoft/edgeai-for-beginners)
- [模型上下文协议 (MCP) 初学者](https://github.com/microsoft/mcp-for-beginners)
- [AI 代理初学者](https://github.com/microsoft/ai-agents-for-beginners)
- [.NET 生成式 AI 初学者](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [生成式 AI 初学者](https://github.com/microsoft/generative-ai-for-beginners)
- [Java 生成式 AI 初学者](https://github.com/microsoft/generative-ai-for-beginners-java)
- [机器学习初学者](https://aka.ms/ml-beginners)
- [数据科学初学者](https://aka.ms/datascience-beginners)
- [AI 初学者](https://aka.ms/ai-beginners)
- [网络安全初学者](https://github.com/microsoft/Security-101)
- [Web 开发初学者](https://aka.ms/webdev-beginners)
- [物联网初学者](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## 视频介绍

👉 点击下方图片，在 YouTube 上观看。

- **Open at Microsoft**：简短的 18 分钟介绍及快速使用 Co-op Translator 指南。

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.zh.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 贡献

欢迎贡献和建议。想为 Azure Co-op Translator 贡献代码？请查看我们的 [CONTRIBUTING.md](./CONTRIBUTING.md)，了解如何帮助让 Co-op Translator 更加易用。

## 贡献者

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行为准则

本项目采用了 [微软开源行为准则](https://opensource.microsoft.com/codeofconduct/)。
更多信息请参见 [行为准则常见问题](https://opensource.microsoft.com/codeofconduct/faq/) 或
通过邮件联系 [opencode@microsoft.com](mailto:opencode@microsoft.com) 以获取更多问题或反馈。

## 负责任的 AI

微软致力于帮助客户负责任地使用我们的 AI 产品，分享经验，并通过透明度说明和影响评估等工具建立基于信任的合作关系。许多相关资源可在 [https://aka.ms/RAI](https://aka.ms/RAI) 找到。
微软的负责任 AI 方法基于公平性、可靠性与安全性、隐私与安全、包容性、透明度和问责制等 AI 原则。

大规模自然语言、图像和语音模型——如本示例中使用的模型——可能会表现出不公平、不可靠或冒犯性的行为，从而造成伤害。请查阅 [Azure OpenAI 服务透明度说明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)，了解相关风险和限制。
推荐的风险缓解方法是在架构中包含一个安全系统，能够检测并防止有害行为。[Azure AI 内容安全](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供了一个独立的保护层，能够检测应用和服务中的有害用户生成内容和 AI 生成内容。Azure AI 内容安全包括文本和图像 API，允许您检测有害材料。我们还提供了一个交互式内容安全工作室，您可以在其中查看、探索并试用用于检测不同模态有害内容的示例代码。以下[快速入门文档](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)将指导您如何向该服务发出请求。

另一个需要考虑的方面是整体应用性能。对于多模态和多模型应用，我们认为性能意味着系统能够按您和用户的预期运行，包括不生成有害输出。评估整体应用性能时，重要的是使用[生成质量和风险与安全指标](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)。

您可以使用[prompt flow SDK](https://microsoft.github.io/promptflow/index.html)在开发环境中评估您的 AI 应用。无论是测试数据集还是目标，您的生成式 AI 应用生成结果都可以通过内置评估器或您选择的自定义评估器进行定量测量。要开始使用 prompt flow SDK 评估您的系统，可以参考[快速入门指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。执行评估运行后，您可以在[Azure AI Studio 中可视化结果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商标

本项目可能包含项目、产品或服务的商标或标识。微软商标或标识的授权使用须遵守并遵循[微软商标和品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。在本项目的修改版本中使用微软商标或标识不得引起混淆或暗示微软的赞助。任何第三方商标或标识的使用均须遵守相应第三方的政策。

## 获取帮助

如果遇到困难或对构建 AI 应用有任何疑问，请加入：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如果您在构建过程中有产品反馈或遇到错误，请访问：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->