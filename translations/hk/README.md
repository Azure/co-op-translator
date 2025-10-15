<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T02:31:42+00:00",
  "source_file": "README.md",
  "language_code": "hk"
}
-->
# Co-op Translator

_輕鬆自動化翻譯你的 GitHub 教育內容，支援多種語言，助你觸及全球用戶。_

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

### 🌐 多語言支援

#### 由 [Co-op Translator](https://github.com/Azure/Co-op-Translator) 提供

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](./README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 簡介

**Co-op Translator** 讓你可以快速將 GitHub 教育內容翻譯成多種語言，輕鬆觸及全球用戶。當你更新 Markdown 檔案、圖片或 Jupyter 筆記本時，翻譯會自動同步，確保你的教育內容對國際用戶保持最新和相關。

以下是 Co-op Translator 如何組織翻譯後的 GitHub 教育內容：

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.hk.png)

## 快速開始

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

Docker：

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## 最簡設置

- 用 [.env.template](../../.env.template) 建立 `.env`
- 設定一個 LLM 供應商（Azure OpenAI 或 OpenAI）
- 如需翻譯圖片（`-img`），同時設定 Azure AI Vision
- 建議：如果你有其他工具產生的翻譯，先清理（例如：`translations/`），避免衝突
- 建議：在 README 加入翻譯語言區段，參考 [README languages template](./README_languages_template.md)
- 詳情請參考：[Set up Azure AI](./getting_started/set-up-azure-ai.md)

## 使用方法

翻譯所有支援類型：

```bash
translate -l "ko ja"
```

只翻譯 Markdown：

```bash
translate -l "de" -md
```

Markdown + 圖片：

```bash
translate -l "pt" -md -img
```

只翻譯筆記本：

```bash
translate -l "zh" -nb
```

更多參數：[Command reference](./getting_started/command-reference.md)

## 功能特色

- 自動翻譯 Markdown、筆記本及圖片
- 翻譯內容會隨原文更新自動同步
- 可本地（CLI）或 CI（GitHub Actions）運行
- 支援 Azure OpenAI 或 OpenAI，圖片可選用 Azure AI Vision
- 保持 Markdown 格式及結構不變

## 文件

- [命令列指南](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions 指南（公開倉庫及標準密鑰）](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions 指南（Microsoft 組織倉庫及組織級設置）](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [支援語言列表](./getting_started/supported-languages.md)
- [疑難排解](./getting_started/troubleshooting.md)

## 支持我們，推動全球學習

歡迎加入我們，一起革新全球教育內容分享方式！在 GitHub 為 [Co-op Translator](https://github.com/azure/co-op-translator) 點個 ⭐，支持我們打破學習和科技的語言障礙。你的關注和貢獻非常重要！歡迎提交程式碼和功能建議。

### 探索 Microsoft 教育內容（多語言）

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

## 影片簡介

想了解 Co-op Translator？歡迎觀看我們的簡報影片（點擊下圖到 YouTube）：

- **Open at Microsoft**：18 分鐘簡介及快速教學，帶你認識 Co-op Translator。

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.hk.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 貢獻方式

本項目歡迎各方貢獻及建議。有興趣參與 Azure Co-op Translator？請參閱 [CONTRIBUTING.md](./CONTRIBUTING.md)，了解如何協助 Co-op Translator 變得更易用。

## 貢獻者

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行為守則

本項目採用 [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)。
詳情請參閱 [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) 或
如有疑問，請電郵 [opencode@microsoft.com](mailto:opencode@microsoft.com)。

## 負責任的 AI

Microsoft 致力協助客戶負責任地使用 AI 產品，分享我們的經驗，並透過透明度說明和影響評估等工具建立信任。相關資源可於 [https://aka.ms/RAI](https://aka.ms/RAI) 查閱。
Microsoft 的負責任 AI 原則包括公平、可靠及安全、私隱及保安、共融、透明及問責。

大規模自然語言、圖像及語音模型（如本範例所用）有機會出現不公平、不可靠或冒犯性行為，可能造成傷害。請參閱 [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) 了解相關風險及限制。

建議的風險緩解方法，是在你的架構中加入安全系統，偵測及防止有害行為。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供獨立保護層，可偵測應用程式及服務中的有害用戶或 AI 內容。Azure AI Content Safety 包括文字及圖像 API，助你偵測有害資料。我們亦有互動式 Content Safety Studio，讓你試用偵測不同類型有害內容的範例程式碼。以下 [快速入門文件](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) 可指導你如何向服務發送請求。
另一個需要考慮的層面是整體應用程式的效能。對於多模態和多模型的應用程式來說，效能指的是系統能夠如你和用戶所期望般運作，包括不產生有害的輸出。評估整體應用程式的效能時，建議參考[生成品質及風險與安全性指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)。

你可以在開發環境中利用 [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) 來評估你的 AI 應用程式。無論是使用測試數據集或目標，你的生成式 AI 應用程式的輸出都可以透過內建或自訂的評估器進行量化評分。想要開始使用 prompt flow sdk 來評估你的系統，可以參考[快速入門指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。當你執行評估後，可以[在 Azure AI Studio 視覺化結果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商標

本專案可能包含某些專案、產品或服務的商標或標誌。經授權使用 Microsoft
商標或標誌時，必須遵守
[Microsoft 的商標及品牌指引](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。
在本專案的修改版本中使用 Microsoft 商標或標誌時，不得造成混淆或暗示 Microsoft 贊助。
任何第三方商標或標誌的使用，則需遵守該第三方的相關政策。

## 尋求協助

如果你在開發 AI 應用程式時遇到困難或有疑問，歡迎加入：

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

如果你有產品意見或在開發過程中遇到錯誤，請前往：

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**免責聲明**：
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。我們致力於確保翻譯的準確性，但請注意，自動翻譯可能會包含錯誤或不準確之處。原始語言的文件應被視為具權威性的來源。對於重要資訊，建議使用專業人工翻譯。因使用本翻譯而引起的任何誤解或錯誤，我們概不負責。