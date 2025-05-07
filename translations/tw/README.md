<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbc19abb46abfba90855f2b7bd01767",
  "translation_date": "2025-05-06T17:26:06+00:00",
  "source_file": "README.md",
  "language_code": "tw"
}
-->
![Logo](../../../../../../imgs/logo.png)

# Co-op Translator：輕鬆自動化教育文件的翻譯

_輕鬆自動化將你的文件翻譯成多種語言，觸及全球讀者。_

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 由 Co-op Translator 提供的語言支援

[Korean](../ko/README.md) | [Japanese](../ja/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Taiwan)](./README.md) | [Spanish](../es/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Portuguese (Brazil)](../br/README.md) | [Hindi](../hi/README.md) | [Russian](../ru/README.md) | [Turkish](../tr/README.md) | [Arabic](../ar/README.md) | [Indonesian](../id/README.md) | [Vietnamese](../vi/README.md)


[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
> **強大的自動化功能**：現在支援 GitHub Actions！當您的儲存庫有變更時，會自動翻譯您的文件，輕鬆保持內容最新。[了解更多](../..)。

## 支援的模型與服務

| 類型                  | 名稱                           |
|-----------------------|--------------------------------|
| 語言模型              | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| 電腦視覺              | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> 若無法使用電腦視覺服務，co-op translator 將會切換至[僅 Markdown 模式](./getting_started/markdown-only-mode.md)。

## 概覽：簡化您的教育內容翻譯流程

語言障礙嚴重阻礙全球學習者和開發者取得寶貴的教育資源與技術知識，限制了參與度並放慢全球創新與學習的腳步。

**Co-op Translator** 是因應微軟大型教育系列（例如「For Beginners」指南）繁瑣的人工翻譯流程而誕生，現已發展成一款簡單好用且強大的工具，旨在打破語言障礙。透過 CLI 和 GitHub Actions 提供高品質自動翻譯，Co-op Translator 讓教育者、學生、研究人員和開發者能夠跨越語言限制，共享並存取知識。

看看 Co-op Translator 如何組織翻譯後的教育內容：

![範例](../../../../../../imgs/translation-ex.png)

Markdown 檔案與圖片中的文字會自動翻譯，並整齊分類到各語言專屬資料夾。

**立即用 Co-op Translator 解鎖您的教育內容全球存取！**

## 支援微軟學習資源的全球存取

Co-op Translator 協助彌合微軟重要教育專案的語言隔閡，自動翻譯服務全球開發者社群使用的儲存庫。目前使用 Co-op Translator 的範例包括：

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## 主要功能

- **自動翻譯**：輕鬆將文字翻譯成多種語言。
- **GitHub Actions 整合**：將翻譯自動化納入您的 CI/CD 流程。
- **保留 Markdown 格式**：翻譯過程中維持正確的 Markdown 語法。
- **圖片文字翻譯**：擷取並翻譯圖片中的文字。
- **先進的 LLM 技術**：使用尖端語言模型提供高品質翻譯。
- **輕鬆整合**：無縫接軌您現有的專案架構。
- **簡化在地化流程**：加速您的專案國際化步驟。

## 運作原理

![架構圖](../../../../../../imgs/architecture_241019.png)

Co-op Translator 會從您的專案資料夾中取得 Markdown 檔案與圖片，並進行以下處理：

1. **文字擷取**：從 Markdown 檔案擷取文字，若有設定（例如 Azure Computer Vision），也會擷取圖片內的文字。
1. **AI 翻譯**：將擷取的文字送到設定的 LLM（Azure OpenAI、OpenAI 等）進行翻譯。
1. **結果存檔**：將翻譯後的 Markdown 檔案與圖片（含翻譯文字）存入各語言專屬資料夾，同時保留原始格式。

## 快速上手

使用 CLI 快速開始，或透過 GitHub Actions 設定完整自動化。

### 快速啟動：命令列

快速透過命令列開始：

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
  - Execute the translate command, specifying target languages with the `-l` 參數：
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
- Requires: Setting up a workflow file (`.github/workflows` 替換為您的儲存庫路徑。無需本地安裝。
- 指南：
  - [GitHub Actions 指南（公開儲存庫與標準祕密）](./getting_started/github-actions-guide/github-actions-guide-public.md) - 適用於大多數公開或個人儲存庫，使用標準儲存庫祕密。
  - [GitHub Actions 指南（微軟組織儲存庫與組織層級設定）](./getting_started/github-actions-guide/github-actions-guide-org.md) - 若您在微軟 GitHub 組織內工作，或需使用組織層級的祕密或執行器，請參考此指南。

> [!NOTE]
> 本教學聚焦 Azure 資源，但您也可以使用[支援的模型與服務](../..)列表中的任何語言模型。

### 疑難排解與技巧

- [疑難排解指南](./getting_started/troubleshooting.md)

### 額外資源

- [命令參考](./getting_started/command-reference.md)：所有可用命令與選項的詳細指南。
- [多語言支援設定](./getting_started/multi-language-support.md)：如何在 README 中加入連結至翻譯版本的表格。
- [支援語言](./getting_started/supported-languages.md)：查看支援語言清單與新增語言的說明。
- [僅 Markdown 模式](./getting_started/markdown-only-mode.md)：如何只翻譯文字，不包含圖片翻譯。

## 影片介紹

透過以下影片更了解 Co-op Translator _(點擊圖片可在 YouTube 觀看)_：

- **Open at Microsoft**：18 分鐘簡短介紹與快速上手指南。

  [![Open at Microsoft](../../../../../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**：一小時詳盡步驟說明，涵蓋 Co-op Translator 是什麼、如何設定與使用，以及實際演示。

  [![Microsoft Reactor](../../../../../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## 支持我們，促進全球學習

加入我們，一起革新全球教育內容的分享方式！在 GitHub 為 [Co-op Translator](https://github.com/azure/co-op-translator) 按⭐，支持我們打破學習與技術上的語言障礙。您的關注與貢獻將帶來重大影響！我們歡迎程式碼貢獻與功能建議。

## 貢獻指南

本專案歡迎貢獻與建議。想為 Azure Co-op Translator 貢獻？請參閱我們的 [CONTRIBUTING.md](./CONTRIBUTING.md) 了解如何協助讓 Co-op Translator 更易取得。

## 貢獻者

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行為準則

本專案已採用 [Microsoft 開源行為準則](https://opensource.microsoft.com/codeofconduct/)。
更多資訊請參考 [行為準則常見問題](https://opensource.microsoft.com/codeofconduct/faq/)，或聯絡 [opencode@microsoft.com](mailto:opencode@microsoft.com) 提問或反饋。

## 負責任的 AI

微軟致力協助客戶負責任地使用 AI 產品，分享我們的經驗，並透過透明度說明與影響評估建立信任夥伴關係。許多相關資源可在 [https://aka.ms/RAI](https://aka.ms/RAI) 找到。
微軟負責任 AI 的理念基於公平性、可靠性與安全性、隱私與安全、包容性、透明度及問責制等 AI 原則。

大型自然語言、影像與語音模型——如本範例所用——可能會有不公平、不可靠或冒犯性的行為，進而造成傷害。請參閱 [Azure OpenAI 服務透明度說明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)，以了解相關風險與限制。
建議的風險緩解方法是在您的架構中加入一個安全系統，能夠偵測並防止有害行為。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供獨立的保護層，能偵測應用程式和服務中使用者產生及 AI 產生的有害內容。Azure AI Content Safety 包含文字與影像 API，讓您能偵測有害的素材。我們也提供互動式 Content Safety Studio，讓您可以查看、探索並試用不同模態中偵測有害內容的範例程式碼。以下的[快速入門文件](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)會指導您如何向服務發送請求。

另一個需要考慮的面向是整體應用程式的效能。對於多模態與多模型的應用，我們認為效能是指系統能符合您和使用者的預期，包括不產生有害輸出。評估整體應用程式的效能時，建議使用[生成品質與風險及安全指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)。

您可以使用[prompt flow SDK](https://microsoft.github.io/promptflow/index.html)在開發環境中評估您的 AI 應用程式。無論是測試資料集或目標，您的生成式 AI 應用程式的產出都會透過內建評估器或您選擇的自訂評估器進行量化測量。若要開始使用 prompt flow sdk 評估系統，您可以參考[快速入門指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。執行評估後，您可以在[Azure AI Studio 中視覺化結果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商標

本專案可能包含專案、產品或服務的商標或標誌。授權使用 Microsoft 商標或標誌需遵守並依據[Microsoft 的商標與品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。在本專案的修改版本中使用 Microsoft 商標或標誌，不得造成混淆或暗示 Microsoft 贊助。任何第三方商標或標誌的使用皆須遵守該第三方的相關政策。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生之任何誤解或誤釋負責。