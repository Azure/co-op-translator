<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "329abbc9354793ea422f7e7ebf66be2c",
  "translation_date": "2025-05-07T01:52:31+00:00",
  "source_file": "README.md",
  "language_code": "tw"
}
-->
![Logo](../../imgs/logo.png)

# Co-op Translator：輕鬆自動化教育文件的翻譯工作

_輕鬆將您的文件自動翻譯成多種語言，觸及全球讀者。_

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 由 Co-op Translator 提供技術支持的語言列表

[Korean](../ko/README.md) | [Japanese](../ja/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Taiwan)](./README.md) | [Spanish](../es/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Portuguese (Brazil)](../br/README.md) | [Hindi](../hi/README.md) | [Russian](../ru/README.md) | [Turkish](../tr/README.md) | [Arabic](../ar/README.md) | [Indonesian](../id/README.md) | [Vietnamese](../vi/README.md)

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
>
> **強大的自動化功能**：現在支援 GitHub Actions！當您的倉庫內容有變更時，自動翻譯您的文件，輕鬆保持所有內容最新。[了解更多](../..)。

## 支援的模型與服務

| 類型                  | 名稱                           |
|-----------------------|--------------------------------|
| 語言模型              | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| 電腦視覺              | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> 如果沒有可用的電腦視覺服務，co-op translator 會切換到 [Markdown-only mode](./getting_started/markdown-only-mode.md)。

## 概覽：簡化您的教育內容翻譯流程

語言障礙嚴重阻礙了全球學習者和開發者取得寶貴的教育資源與技術知識，限制了參與度並放緩全球創新與學習的速度。

**Co-op Translator** 是因應微軟自家大型教育系列（如「For Beginners」指南）中低效率的人工翻譯流程而誕生。它已發展成一款簡單好用且功能強大的工具，旨在打破語言障礙，讓所有人都能受益。透過 CLI 和 GitHub Actions 提供高品質的自動翻譯，Co-op Translator 讓全球的教育者、學生、研究人員與開發者無語言限制地分享與取得知識。

看看 Co-op Translator 如何組織已翻譯的教育內容：

![Example](../../imgs/translation-ex.png)

Markdown 檔案和圖片中的文字會自動翻譯，並整齊分類到各語言專屬的資料夾中。

**立即用 Co-op Translator 解鎖您的教育內容全球存取！**

## 支援微軟學習資源的全球存取

Co-op Translator 幫助縮短微軟主要教育計畫的語言差距，自動化翻譯流程，服務全球開發者社群。目前使用 Co-op Translator 的範例包括：

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## 主要特色

- **自動翻譯**：輕鬆將文字翻譯成多種語言。
- **GitHub Actions 整合**：將翻譯流程自動化，納入您的 CI/CD 管線。
- **Markdown 格式保留**：翻譯時保持正確的 Markdown 語法。
- **圖片文字翻譯**：擷取並翻譯圖片中的文字。
- **先進的 LLM 技術**：使用尖端語言模型，提供高品質翻譯。
- **輕鬆整合**：無縫接軌您現有的專案架構。
- **簡化在地化流程**：讓專案國際化更流暢。

## 運作方式

![Architecture](../../imgs/architecture_241019.png)

Co-op Translator 從您的專案資料夾擷取 Markdown 檔案和圖片，流程如下：

1. **文字擷取**：從 Markdown 檔案擷取文字，若有設定（例如 Azure Computer Vision），也會擷取圖片中的文字。
1. **AI 翻譯**：將擷取的文字送至設定的 LLM（Azure OpenAI、OpenAI 等）進行翻譯。
1. **結果儲存**：將翻譯後的 Markdown 檔案與圖片（含翻譯文字）存放到語言專屬資料夾，並保留原始格式。

## 快速開始

透過 CLI 快速上手，或設定 GitHub Actions 進行完整自動化。

### 快速啟動：命令列

使用命令列快速啟動：

1. 安裝套件：
    ```bash
    pip install co-op-translator
    ```
2. 設定憑證：
  - 建立 `.env` file in your project's root directory.
  - Copy the contents from the [.env.template](../../.env.template) file into your new `.env` file.
  - Fill in the required API keys and endpoint information in your `.env` file.
3. Run Translation:
  - Navigate to your project's root directory in your terminal.
  - Execute the translate command, specifying target languages with the `-l` 旗標：
    ```bash
    translate -l "ko ja fr"
    ```
    *(將 `"ko ja fr"` with your desired space-separated language codes)*

### Detailed Usage Guides

Choose the approach that best fits your workflow:

#### 1. Using the Command Line (CLI)

- Best for: One-time translations, manual control, or integration into custom scripts.
- Requires: Local installation of Python and the `co-op-translator` package.
- Guide: [Command Line Guide](./getting_started/command-line-guide/command-line-guide.md)

#### 2. Using GitHub Actions (Automation)

- Best for: Automatically translating content whenever changes are pushed to your repository. Keeps translations consistently up-to-date.
- Requires: Setting up a workflow file (`.github/workflows`) 放入您的倉庫。無需本地安裝。
- 指南：
  - [GitHub Actions 指南（公開倉庫與標準密鑰）](./getting_started/github-actions-guide/github-actions-guide-public.md) - 適用於大多數公開或個人倉庫，使用標準的倉庫密鑰。
  - [GitHub Actions 指南（微軟組織倉庫與組織級設定）](./getting_started/github-actions-guide/github-actions-guide-org.md) - 如果您在微軟 GitHub 組織內工作，或需要使用組織層級的密鑰或 runner，請使用此指南。

> [!NOTE]
> 本教學以 Azure 資源為主，但您也可以使用 [supported models and services](../..) 清單中的任何支援語言模型。

### 疑難排解與技巧

- [疑難排解指南](./getting_started/troubleshooting.md)

### 其他資源

- [命令參考](./getting_started/command-reference.md)：所有命令與選項的詳細指南。
- [多語言支援設定](./getting_started/multi-language-support.md)：如何在 README 中加入連結至翻譯版本的表格。
- [支援語言](./getting_started/supported-languages.md)：檢視支援語言清單及新增語言說明。
- [Markdown-only 模式](./getting_started/markdown-only-mode.md)：如何只翻譯文字，不翻譯圖片。

## 影片介紹

透過我們的簡報更深入了解 Co-op Translator _(點擊下方圖片前往 YouTube 觀看)_：

- **Open at Microsoft**：18 分鐘的簡短介紹與快速使用指南。

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**：一小時的詳細逐步教學，涵蓋 Co-op Translator 是什麼、如何設定及有效使用，並有現場示範其強大功能。

  [![Microsoft Reactor](../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## 支持我們，促進全球學習

加入我們，一起改變教育內容的全球分享方式！在 GitHub 為 [Co-op Translator](https://github.com/azure/co-op-translator) 點⭐，支持我們打破學習與技術的語言障礙。您的關注與貢獻將帶來重大影響！我們歡迎程式碼貢獻與功能建議。

## 貢獻指南

本專案歡迎各種貢獻與建議。想參與 Azure Co-op Translator 的開發？請參閱我們的 [CONTRIBUTING.md](./CONTRIBUTING.md)，了解如何協助讓 Co-op Translator 更加普及。

## 貢獻者

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行為準則

本專案採用 [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)。
更多資訊請參考 [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) 或
聯絡 [opencode@microsoft.com](mailto:opencode@microsoft.com) 以獲得進一步協助。

## 負責任的 AI

微軟致力協助客戶負責任地使用 AI 產品，分享我們的學習成果，並透過透明度說明與影響評估等工具建立信任夥伴關係。許多相關資源可於 [https://aka.ms/RAI](https://aka.ms/RAI) 找到。
微軟的負責任 AI 方法基於公平性、可靠性與安全性、隱私與安全、包容性、透明度與問責制等 AI 原則。

大型自然語言、影像與語音模型（如本範例中使用的）可能會出現不公平、不可靠或冒犯性的行為，進而造成傷害。請參考 [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) 以了解相關風險與限制。
建議的風險緩解方法是在您的架構中加入一個安全系統，能夠偵測並防止有害行為。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供獨立的保護層，能偵測應用程式和服務中用戶產生及 AI 產生的有害內容。Azure AI Content Safety 包含文字與影像 API，讓您能偵測有害素材。我們也有一個互動式的 Content Safety Studio，讓您可以查看、探索並試用偵測不同模態有害內容的範例程式碼。以下的[快速入門文件](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)會引導您如何向服務發出請求。

另一個需要考慮的面向是整體應用程式效能。對於多模態和多模型的應用，我們認為效能是指系統能如您和使用者預期般運作，包括不產生有害輸出。使用[生成品質與風險及安全指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)來評估您整體應用程式的效能是很重要的。

您可以在開發環境中使用[prompt flow SDK](https://microsoft.github.io/promptflow/index.html)評估您的 AI 應用。無論是測試資料集或目標，您的生成式 AI 應用產出都能透過內建評估器或您選擇的自訂評估器做量化測量。若要開始使用 prompt flow SDK 評估您的系統，您可以參考[快速入門指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。執行評估後，您可以在[Azure AI Studio 中視覺化結果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## Trademarks

本專案可能包含專案、產品或服務的商標或標誌。Microsoft 商標或標誌的授權使用須遵守並遵循[Microsoft 的商標與品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。在本專案的修改版本中使用 Microsoft 商標或標誌，不得造成混淆或暗示 Microsoft 的贊助。任何第三方商標或標誌的使用均須遵守該第三方的政策。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生之任何誤解或誤譯負責。