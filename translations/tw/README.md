<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "18318279bb851dc2c709bfc6a26f6e1d",
  "translation_date": "2025-05-07T14:01:20+00:00",
  "source_file": "README.md",
  "language_code": "tw"
}
-->
![Logo](../../imgs/logo.png)

# Co-op Translator：輕鬆自動化教育文件的翻譯工作

_輕鬆自動化將您的文件翻譯成多種語言，觸及全球讀者。_

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 語言支援由 Co-op Translator 提供

[Korean](../ko/README.md) | [Japanese](../ja/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Taiwan)](./README.md) | [Spanish](../es/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Portuguese (Brazil)](../br/README.md) | [Hindi](../hi/README.md) | [Russian](../ru/README.md) | [Turkish](../tr/README.md) | [Arabic](../ar/README.md) | [Indonesian](../id/README.md) | [Vietnamese](../vi/README.md)

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
> **強大的自動化功能**：現在支援 GitHub Actions！當您的儲存庫有變更時，自動翻譯您的文件，輕鬆保持內容最新。[了解更多](../..)。

## 支援的模型與服務

| 類型                  | 名稱                           |
|-----------------------|--------------------------------|
| 語言模型              | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| 電腦視覺              | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> 如果沒有可用的電腦視覺服務，co-op translator 將切換到[僅限 Markdown 模式](./getting_started/markdown-only-mode.md)。

## 概覽：簡化您的教育內容翻譯流程

語言障礙嚴重阻礙了全球學習者與開發者取得寶貴的教育資源與技術知識，限制了參與度，也放緩了全球創新與學習的速度。

**Co-op Translator** 是為了解決微軟自家大型教育系列（如「For Beginners」指南）中低效率的手動翻譯流程而誕生。它已發展成一個易用且強大的工具，旨在打破語言障礙，讓所有人都能受益。透過 CLI 與 GitHub Actions 提供高品質的自動翻譯，Co-op Translator 讓全球的教育者、學生、研究人員與開發者無語言限制地分享與取得知識。

看看 Co-op Translator 如何組織翻譯後的教育內容：

![Example](../../imgs/translation-ex.png)

Markdown 檔案與圖片中的文字會自動翻譯，並整齊地分類到不同語言的資料夾中。

**立即使用 Co-op Translator，解鎖您的教育內容全球存取！**

## 支援微軟學習資源的全球存取

Co-op Translator 協助彌補語言鴻溝，自動翻譯服務於全球開發者社群的微軟重要教育計畫。現有使用 Co-op Translator 的範例包括：

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## 主要功能

- **自動翻譯**：輕鬆將文字翻譯成多種語言。
- **GitHub Actions 整合**：將翻譯自動化納入您的 CI/CD 流程。
- **保留 Markdown 格式**：翻譯時保持正確的 Markdown 語法。
- **圖片文字翻譯**：擷取並翻譯圖片中的文字。
- **先進 LLM 技術**：使用最尖端的語言模型，提供高品質翻譯。
- **輕鬆整合**：無縫接入您現有的專案架構。
- **簡化在地化**：讓專案國際化流程更簡單流暢。

## 運作方式

![Architecture](../../imgs/architecture_241019.png)

Co-op Translator 從您的專案資料夾中擷取 Markdown 檔案和圖片，並進行以下處理：

1. **文字擷取**：從 Markdown 檔案抽取文字，並在設定（例如使用 Azure Computer Vision）下，擷取圖片內嵌文字。
1. **AI 翻譯**：將擷取的文字送至設定好的 LLM（Azure OpenAI、OpenAI 等）進行翻譯。
1. **結果儲存**：將翻譯後的 Markdown 檔案和帶翻譯文字的圖片存入語言專屬資料夾，並保留原始格式。

## 快速開始

> [!NOTE]
> 本教學以 Azure 資源為主，但您也可以使用[支援的模型與服務](../..)列表中的任何語言模型。

您可以快速透過 CLI 開始，或設定 GitHub Actions 進行完整自動化。

### 初始設定

- [設定 Azure AI](./getting_started/set-up-azure-ai.md)

### 快速上手：命令列

快速使用命令列啟動：

1. 安裝套件：
    ```bash
    pip install co-op-translator
    ```
2. 設定認證：
  - 建立 `.env` file in your project's root directory.
  - Copy the contents from the [.env.template](../../.env.template) file into your new `.env` file.
  - Fill in the required API keys and endpoint information in your `.env` file.
3. Run Translation:
  - Navigate to your project's root directory in your terminal.
  - Execute the translate command, specifying target languages with the `-l` 旗標：
    ```bash
    translate -l "ko ja fr"
    ```
    *(替換 `"ko ja fr"` with your desired space-separated language codes)*

### Detailed Usage Guides

Choose the approach that best fits your workflow:

#### 1. Using the Command Line (CLI)

- Best for: One-time translations, manual control, or integration into custom scripts.
- Requires: Local installation of Python and the `co-op-translator` package.
- Guide: [Command Line Guide](./getting_started/command-line-guide/command-line-guide.md)

#### 2. Using GitHub Actions (Automation)

- Best for: Automatically translating content whenever changes are pushed to your repository. Keeps translations consistently up-to-date.
- Requires: Setting up a workflow file (`.github/workflows`) 在您的儲存庫中。無需本機安裝。
- 指南：
  - [GitHub Actions 指南（公開儲存庫與標準密鑰）](./getting_started/github-actions-guide/github-actions-guide-public.md) - 適用於大多數公開或個人儲存庫，使用標準儲存庫密鑰。
  - [GitHub Actions 指南（微軟組織儲存庫與組織層級設定）](./getting_started/github-actions-guide/github-actions-guide-org.md) - 若您在微軟 GitHub 組織內工作，或需使用組織層級密鑰或執行器，請參考此指南。

### 疑難排解與技巧

- [疑難排解指南](./getting_started/troubleshooting.md)

### 其他資源

- [指令參考](./getting_started/command-reference.md)：所有可用指令與選項的詳細說明。
- [多語言支援設定](./getting_started/multi-language-support.md)：如何在 README 中新增連結到翻譯版本的表格。
- [支援語言](./getting_started/supported-languages.md)：查看支援語言列表與新增語言的說明。
- [僅限 Markdown 模式](./getting_started/markdown-only-mode.md)：僅翻譯文字，不包含圖片翻譯。

## 影片介紹

透過以下簡報更深入了解 Co-op Translator _(點擊下方圖片可在 YouTube 觀看)_：

- **Open at Microsoft**：18 分鐘簡短介紹與快速教學，教您如何使用 Co-op Translator。

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**：一小時詳細步驟教學，涵蓋 Co-op Translator 的概念、工具設定與實際操作示範。

  [![Microsoft Reactor](../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## 支持我們並促進全球學習

加入我們，一起革新教育內容的全球分享方式！在 GitHub 上為 [Co-op Translator](https://github.com/azure/co-op-translator) 點 ⭐，支持我們打破學習與技術的語言障礙。您的關注與貢獻帶來重大影響！歡迎隨時提供程式碼貢獻與功能建議。

## 參與貢獻

本專案歡迎貢獻與建議。想參與 Azure Co-op Translator 的開發嗎？請參考我們的 [CONTRIBUTING.md](./CONTRIBUTING.md)，了解如何幫助 Co-op Translator 更加普及。

## 貢獻者

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行為準則

本專案採用 [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)。
更多資訊請見 [行為準則常見問題](https://opensource.microsoft.com/codeofconduct/faq/) 或
聯絡 [opencode@microsoft.com](mailto:opencode@microsoft.com) 提出問題或建議。

## 負責任的 AI

微軟致力於協助客戶負責任地使用 AI 產品，分享學習經驗，並透過透明度說明與影響評估等工具建立信任夥伴關係。許多相關資源可在 [https://aka.ms/RAI](https://aka.ms/RAI) 找到。
微軟的負責任 AI 策略建立在公平性、可靠性與安全性、隱私與安全、包容性、透明度與問責制等 AI 原則上。
大型自然語言、影像與語音模型——像這個範例中使用的模型——可能會有不公平、不可靠或冒犯性的行為，進而造成傷害。請參考[Azure OpenAI 服務透明度說明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)以了解相關風險與限制。

減輕這些風險的建議做法是在架構中加入能偵測並防止有害行為的安全系統。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供獨立的保護層，能在應用程式和服務中偵測使用者生成及 AI 生成的有害內容。Azure AI Content Safety 包含文字與影像 API，可協助你偵測有害素材。我們也提供互動式的 Content Safety Studio，讓你能檢視、探索並試用用於偵測不同模態有害內容的範例程式碼。以下的[快速入門文件](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)會引導你如何向服務發出請求。

另一個需要考慮的面向是整體應用程式效能。對於多模態與多模型的應用程式來說，我們認為效能代表系統如你與使用者預期般運作，包括不產生有害輸出。評估整體應用程式效能時，重要的是使用[生成品質與風險及安全指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)。

你可以在開發環境中使用[prompt flow SDK](https://microsoft.github.io/promptflow/index.html)來評估你的 AI 應用程式。無論是使用測試資料集或目標，你的生成式 AI 應用程式產出都會透過內建評估器或你選擇的自訂評估器進行量化測量。若要開始使用 prompt flow sdk 評估系統，可以參考[快速入門指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。執行評估後，你可以在[Azure AI Studio 中視覺化結果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商標

本專案可能包含專案、產品或服務的商標或標誌。Microsoft 商標或標誌的授權使用需遵守並依循[Microsoft 商標與品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。
在本專案的修改版本中使用 Microsoft 商標或標誌，不得造成混淆或暗示 Microsoft 贊助。
任何第三方商標或標誌的使用，均需遵守該第三方的相關政策。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於翻譯準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生之任何誤解或誤譯負責。