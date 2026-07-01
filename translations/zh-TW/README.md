# Co-op 翻譯器

_Easily automate and maintain translations for your educational GitHub content across multiple languages as your project evolves._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
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

**開始使用：** [Choose your workflow](https://azure.github.io/co-op-translator/workflows/) | [Configuration](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 多語言支援

#### 由 [Co-op Translator](https://github.com/Azure/co-op-translator) 支援

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯語](../ar/README.md) | [孟加拉語](../bn/README.md) | [保加利亞語](../bg/README.md) | [緬甸語（緬甸）](../my/README.md) | [中文（簡體）](../zh-CN/README.md) | [中文（繁體，香港）](../zh-HK/README.md) | [中文（繁體，澳門）](../zh-MO/README.md) | [中文（繁體，台灣）](./README.md) | [克羅埃西亞語](../hr/README.md) | [捷克語](../cs/README.md) | [丹麥語](../da/README.md) | [荷蘭語](../nl/README.md) | [愛沙尼亞語](../et/README.md) | [芬蘭語](../fi/README.md) | [法語](../fr/README.md) | [德語](../de/README.md) | [希臘語](../el/README.md) | [希伯來語](../he/README.md) | [印地語](../hi/README.md) | [匈牙利語](../hu/README.md) | [印尼語](../id/README.md) | [義大利語](../it/README.md) | [日語](../ja/README.md) | [卡納達語](../kn/README.md) | [高棉語](../km/README.md) | [韓語](../ko/README.md) | [立陶宛語](../lt/README.md) | [馬來語](../ms/README.md) | [馬拉雅拉姆語](../ml/README.md) | [馬拉地語](../mr/README.md) | [尼泊爾語](../ne/README.md) | [奈及利亞皮欽語](../pcm/README.md) | [挪威語](../no/README.md) | [波斯語（Farsi）](../fa/README.md) | [波蘭語](../pl/README.md) | [葡萄牙語（巴西）](../pt-BR/README.md) | [葡萄牙語（葡萄牙）](../pt-PT/README.md) | [旁遮普語（Gurmukhi）](../pa/README.md) | [羅馬尼亞語](../ro/README.md) | [俄語](../ru/README.md) | [塞爾維亞語（西里爾字母）](../sr/README.md) | [斯洛伐克語](../sk/README.md) | [斯洛維尼亞語](../sl/README.md) | [西班牙語](../es/README.md) | [史瓦希里語](../sw/README.md) | [瑞典語](../sv/README.md) | [他加祿語（菲律賓）](../tl/README.md) | [泰米爾語](../ta/README.md) | [泰盧固語](../te/README.md) | [泰語](../th/README.md) | [土耳其語](../tr/README.md) | [烏克蘭語](../uk/README.md) | [烏爾都語](../ur/README.md) | [越南語](../vi/README.md)

> **偏好本機複製？**
>
> 本存放庫包含超過 50 種語言的翻譯，會顯著增加下載大小。若要在不包含翻譯的情況下複製，請使用 Sparse Checkout：
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
> 這樣可以讓你以更快的下載速度取得完成課程所需的一切。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 概覽

**Co-op Translator** 幫助你將教育類的 GitHub 內容輕鬆在多種語言中在地化。
當你更新 Markdown 檔案、圖片或筆記本時，翻譯會自動保持同步，確保你的內容對全球學習者來說保持正確且最新。

從 CLI 進行存放庫翻譯，或使用 Python API 進行自動化，或透過 MCP 伺服器進行代理與編輯者工作流程。

Example of how translated content is organized:

![Example](../../imgs/translation-ex.png)

## 為什麼選擇 Co-op Translator？

翻譯一個檔案很容易。讓整個文件存放庫
保持翻譯、連結且最新才是困難的部分。

| 問題 | Co-op Translator 如何協助 |
| --- | --- |
| Long docs are not one prompt | 大型 Markdown 檔案會被拆分成多個區塊，因此一份冗長的 README 不會依賴於單一脆弱的模型回應。如果某個區塊失敗，Co-op Translator 可以重試並僅重新分割失敗的部分。 |
| Incomplete translations should not be marked current | 截斷的翻譯絕不應標記為最新。Co-op Translator 在儲存前會檢查翻譯完整性，並能偵測結構上不完整的既有翻譯。 |
| Links should match the translated repo structure | 手動翻譯常常會讓相對連結指回原始樹。Co-op Translator 會重寫 Markdown、筆記本、圖片與 README 的連結，以符合 `translations/<lang>/...` 結構。 |
| Translation should work across an entire repo | Co-op Translator 將 README 檔案、文件、筆記本與圖片文字視為單一存放庫工作流程的一部分，而不是逐一翻譯檔案。 |
| Maintaining translations matters more than creating them once | 來源雜湊與翻譯的 metadata 讓 Co-op Translator 能找出過期的檔案、跳過未更動的檔案，並在來源存放庫演進時維持翻譯內容的同步。 |

## 翻譯狀態如何管理

Co-op Translator 將翻譯內容視為「版本化的軟體工件」，  
而不是靜態檔案。

該工具使用「語言範圍的 metadata」來追蹤已翻譯的 Markdown、圖片和筆記本的狀態。

此設計允許 Co-op Translator：

- 可靠地偵測過期的翻譯
- 一致地處理 Markdown、圖片與筆記本
- 在大型、快速變動的多語言存放庫中安全擴充

透過將翻譯建模為受管理的工件，
翻譯工作流程自然地與現代
軟體相依性與工件管理實務一致。

→ [翻譯狀態如何管理](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### 延伸深入閱讀

- [Fixing Broken Markdown in AI Translation: Hardening a Production Pipeline](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## 開始使用

Co-op Translator 可從 CLI、Python API 或 MCP 伺服器使用。若在本機翻譯、自動化、CI 與代理/編輯者整合間做選擇，請先閱讀工作流程指南。

- [Choose your workflow](../../docs/workflows.md)
- [Configure credentials](../../docs/configuration.md)
- [Translate from the CLI](../../docs/cli.md)
- [Automate with the Python API](../../docs/api.md)
- [Connect with the MCP Server](../../docs/mcp.md)
- [Run in GitHub Actions](../../docs/github-actions.md)

Minimal CLI example after configuration:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS／Linux
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

For first runs on large repositories, use `--dry-run` before writing translated files. See the [CLI Reference](../../docs/cli.md) for content type flags, logs, review, and link migration.

Container quick run with Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Container quick run with PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## 功能

- 自動翻譯 Markdown、筆記本與圖片
- 將翻譯與來源變更保持同步
- 可在本機 (CLI) 或 CI (GitHub Actions) 運行
- 透過 MCP 提供 Markdown、筆記本、圖片、審閱與專案翻譯工具
- 使用 Azure OpenAI 或 OpenAI 作為有提供者支援的翻譯
- 允許 MCP 代管代理在未提供 Co-op Translator LLM 憑證下翻譯 Markdown 與筆記本區塊
- 使用 Azure AI Vision 提取圖片文字並翻譯
- 以確定性檢查審閱翻譯的結構與新鮮度
- 保留 Markdown 格式與結構

## 文件

- [Documentation site](https://azure.github.io/co-op-translator/)
- [Choose your workflow](../../docs/workflows.md)
- [Configuration](../../docs/configuration.md)
- [Azure AI Setup](../../docs/azure-ai-setup.md)
- [CLI Reference](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README languages template](../../docs/readme-languages-template.md)
- [Supported languages](../../docs/supported-languages.md)
- [Contributing](../../CONTRIBUTING.md)
- [Troubleshooting](../../docs/troubleshooting.md)

### 微軟專屬指南
> [!NOTE]
> 僅供 Microsoft「For Beginners」資源庫的維護者使用。

- [Updating the “other courses” list (for MS Beginners repositories only)](../../docs/microsoft-beginners.md)

## 支持我們並促進全球學習

加入我們，一起革新教育內容的全球分享方式！在 GitHub 為 [Co-op Translator](https://github.com/azure/co-op-translator) 點一顆 ⭐，支持我們打破學習與科技的語言障礙的使命。你的關注與貢獻有重大影響！歡迎提供程式碼貢獻與功能建議。

### 以你的語言探索 Microsoft 的教育內容
- [LangChain4j 入門](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD 入門](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI 入門](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) 入門](https://github.com/microsoft/mcp-for-beginners)
- [AI 代理人入門](https://github.com/microsoft/ai-agents-for-beginners)
- [使用 .NET 的生成式 AI 入門](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [生成式 AI 入門](https://github.com/microsoft/generative-ai-for-beginners)
- [使用 Java 的生成式 AI 入門](https://github.com/microsoft/generative-ai-for-beginners-java)
- [機器學習入門](https://aka.ms/ml-beginners)
- [資料科學入門](https://aka.ms/datascience-beginners)
- [AI 入門](https://aka.ms/ai-beginners)
- [資安入門](https://github.com/microsoft/Security-101)
- [網頁開發入門](https://aka.ms/webdev-beginners)
- [物聯網入門](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## 影片簡報

👉 點擊下方影像，在 YouTube 觀看。

- **Open at Microsoft**: 簡短 18 分鐘的介紹以及如何使用 Co-op Translator 的快速指南。

  [![在微軟：Open](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 貢獻

本專案歡迎貢獻與建議。想為 Azure Co-op Translator 貢獻嗎？請參閱我們的 [CONTRIBUTING.md](../../CONTRIBUTING.md) 以了解如何協助讓 Co-op Translator 更易取得的指引。

## 貢獻者

[![co-op-translator 貢獻者](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行為準則

本專案已採用 [Microsoft 開放原始碼行為準則](https://opensource.microsoft.com/codeofconduct/)。
欲知更多資訊，請參閱 [行為準則 常見問答](https://opensource.microsoft.com/codeofconduct/faq/) 或寄信至 [opencode@microsoft.com](mailto:opencode@microsoft.com) 詢問或提供意見。

## 負責任的 AI

Microsoft 致力於協助客戶負責任地使用我們的 AI 產品、分享我們的經驗，並透過例如 Transparency Notes 與 Impact Assessments 的工具建立基於信任的合作關係。許多這些資源可在 [https://aka.ms/RAI](https://aka.ms/RAI) 找到。
Microsoft 對負責任 AI 的作法建立在我們的 AI 原則上：公平性、可靠性與安全、隱私與安全、包容性、透明性與問責制。

大型的自然語言、影像與語音模型（如本範例中使用的模型）可能會表現出不公平、不可靠或冒犯性的行為，進而造成傷害。請參閱 [Azure OpenAI 服務透明度說明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) 以了解相關風險與限制。

建議的風險緩解方法是在您的架構中納入一個能偵測並防止有害行為的安全系統。 [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供一個獨立的保護層，能在應用程式與服務中偵測使用者產生與 AI 產生之有害內容。Azure AI Content Safety 包含可偵測有害內容的文字與影像 API。我們也提供互動式的 Content Safety Studio，讓您檢視、探索並試用跨模態偵測有害內容的範例程式碼。下列 [快速入門文件](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) 將引導您如何向該服務發出請求。

另一個需要考量的面向是整體應用程式的效能。在多模態與多模型的應用中，我們將效能視為系統表現符合您與使用者的預期，包括不產生有害輸出。使用 [生成品質與風險及安全性指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) 評估整體應用程式的表現是很重要的。

您可以在開發環境中使用 [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) 評估 AI 應用程式。無論是測試資料集或目標，生成式 AI 的產出都可以使用內建評估器或您選擇的自訂評估器進行量化衡量。要開始使用 prompt flow SDK 評估系統，您可以參照 [快速入門指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。執行評估後，您可以[在 Azure AI Studio 中視覺化結果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商標

本專案可能包含專案、產品或服務的商標或商標圖示。經授權使用 Microsoft 商標或圖示時，必須遵守並服從 [Microsoft 的商標與品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。
在本專案的修改版本中使用 Microsoft 商標或圖示，必須避免造成混淆或暗示 Microsoft 贊助。本專案中使用之任何第三方商標或圖示，皆須遵守該第三方的使用政策。

## 尋求協助

如果您在建立 AI 應用時遇到困難或有任何問題，歡迎加入：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如果您在開發過程中有產品回饋或遇到錯誤，請造訪：

[![Microsoft Foundry 開發者論壇](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)