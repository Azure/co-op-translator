# Co-op Translator

_輕鬆自動化並維護您在多種語言上的教育性 GitHub 內容翻譯，隨著專案演進保持同步。_

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python 套件](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![授權：MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![下載次數](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![下載次數](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![容器：GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![程式碼風格：black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub 貢獻者](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub 問題](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub 拉取請求](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![歡迎 PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**從這裡開始：** [選擇您的工作流程](https://azure.github.io/co-op-translator/workflows/) | [設定](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP 伺服器](https://azure.github.io/co-op-translator/mcp/)

### 🌐 多語言支援

#### 由 [Co-op Translator](https://github.com/Azure/co-op-translator) 支援

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯語](../ar/README.md) | [孟加拉語](../bn/README.md) | [保加利亞語](../bg/README.md) | [緬甸語（緬甸）](../my/README.md) | [中文（簡體）](../zh-CN/README.md) | [中文（繁體，香港）](../zh-HK/README.md) | [中文（繁體，澳門）](./README.md) | [中文（繁體，台灣）](../zh-TW/README.md) | [克羅地亞語](../hr/README.md) | [捷克語](../cs/README.md) | [丹麥語](../da/README.md) | [荷蘭語](../nl/README.md) | [愛沙尼亞語](../et/README.md) | [芬蘭語](../fi/README.md) | [法語](../fr/README.md) | [德語](../de/README.md) | [希臘語](../el/README.md) | [希伯來語](../he/README.md) | [印地語](../hi/README.md) | [匈牙利語](../hu/README.md) | [印尼語](../id/README.md) | [意大利語](../it/README.md) | [日語](../ja/README.md) | [卡納達語](../kn/README.md) | [高棉語](../km/README.md) | [韓語](../ko/README.md) | [立陶宛語](../lt/README.md) | [馬來語](../ms/README.md) | [馬拉雅拉姆語](../ml/README.md) | [馬拉地語](../mr/README.md) | [尼泊爾語](../ne/README.md) | [奈及利亞皮欽語](../pcm/README.md) | [挪威語](../no/README.md) | [波斯語（法爾西）](../fa/README.md) | [波蘭語](../pl/README.md) | [葡萄牙語（巴西）](../pt-BR/README.md) | [葡萄牙語（葡萄牙）](../pt-PT/README.md) | [旁遮普語（Gurmukhi）](../pa/README.md) | [羅馬尼亞語](../ro/README.md) | [俄語](../ru/README.md) | [塞爾維亞語（西里爾字母）](../sr/README.md) | [斯洛伐克語](../sk/README.md) | [斯洛維尼亞語](../sl/README.md) | [西班牙語](../es/README.md) | [史瓦西里語](../sw/README.md) | [瑞典語](../sv/README.md) | [他加祿語（菲律賓）](../tl/README.md) | [泰米爾語](../ta/README.md) | [泰盧固語](../te/README.md) | [泰語](../th/README.md) | [土耳其語](../tr/README.md) | [烏克蘭語](../uk/README.md) | [烏爾都語](../ur/README.md) | [越南語](../vi/README.md)

> **想在本機複製？**
>
> 本儲存庫包含 50+ 種語言的翻譯，會顯著增加下載大小。若要在不下載翻譯的情況下複製，請使用稀疏檢出：
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
> 這能為您提供完成課程所需的所有內容，同時大幅減少下載時間。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub 觀察者](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub 分叉](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub 星標](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![在 GitHub Codespaces 開啟](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 概述

**Co-op Translator** 幫助您輕鬆地將教育性 GitHub 內容在多種語言間在地化。
當您更新 Markdown 檔案、圖片或筆記本時，翻譯會自動同步，確保您的內容對全球學習者保持準確且最新。

可從 CLI 用於儲存庫翻譯，從 Python API 用於自動化，或透過 MCP 伺服器用於代理與編輯器工作流程。

Example of how translated content is organized:

![範例](../../imgs/translation-ex.png)

## 為什麼使用 Co-op Translator？

翻譯單一檔案很簡單。要維持整個文件庫
的翻譯、連結與更新才是困難的部分。

| 問題 | Co-op Translator 的解決方式 |
| --- | --- |
| Long docs are not one prompt | 大型 Markdown 檔會被切成區塊，因而一個冗長的 README 不會依賴單一脆弱的模型回應。如果某個區塊失敗，Co-op Translator 可以重試並僅重新切分失敗的部分。 |
| Incomplete translations should not be marked current | 不完整的翻譯不應被標示為最新。Co-op Translator 在儲存前會檢查翻譯完整性，並能偵測結構上不完整的既有翻譯。 |
| Links should match the translated repo structure | 手動翻譯常會讓相對連結指回來源樹。Co-op Translator 會重寫 Markdown、筆記本、圖片與 README 的連結，以符合 `translations/<lang>/...` 結構。 |
| Translation should work across an entire repo | Co-op Translator 將 README 檔、文件、筆記本與圖片文字視為一個儲存庫工作流程的一部分，而不是逐一翻譯檔案。 |
| Maintaining translations matters more than creating them once | 來源雜湊與翻譯的 metadata 讓 Co-op Translator 找出過時的檔案、跳過未變更的檔案，並在來源儲存庫演進時保持翻譯內容同步。 |

## 如何管理翻譯狀態

Co-op Translator 將翻譯內容視為「版本化的軟體工件」來管理，  
而非靜態檔案。

此工具使用「語言範圍的 metadata」來追蹤已翻譯的 Markdown、圖片與筆記本的狀態。

此設計讓 Co-op Translator 能夠：

- 可靠地偵測過時的翻譯
- 一致性地處理 Markdown、圖片與筆記本
- 在大型、快速變動且多語言的儲存庫中安全擴展

透過將翻譯建模為受管理的工件，
翻譯工作流程自然與現代的
軟體相依性與工件管理實務對齊。

→ [如何管理翻譯狀態](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### 相關深入探討

- [修復 AI 翻譯中破損的 Markdown：強化生產管線](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## 開始使用

Co-op Translator 可從 CLI、Python API 或 MCP 伺服器使用。若在本地翻譯、自動化、CI 與代理/編輯器整合之間選擇，請先參閱工作流程指南。

- [選擇您的工作流程](../../docs/workflows.md)
- [設定憑證](../../docs/configuration.md)
- [從 CLI 翻譯](../../docs/cli.md)
- [使用 Python API 自動化](../../docs/api.md)
- [連接 MCP 伺服器](../../docs/mcp.md)
- [在 GitHub Actions 中執行](../../docs/github-actions.md)

配置後的最小 CLI 範例：

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS 與 Linux
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

在大型儲存庫的初次執行時，請在寫入翻譯檔案前先使用 `--dry-run`。有關內容類型標記、日誌、審查與連結遷移，請參閱 [CLI 參考](../../docs/cli.md)。

使用 Bash/Zsh 的容器快速執行：

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

使用 PowerShell 的容器快速執行：

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## 功能

- 自動翻譯 Markdown、筆記本與圖片
- 隨來源變更保持翻譯同步
- 在本地（CLI）或 CI（GitHub Actions）中運作
- 透過 MCP 提供 Markdown、筆記本、圖片、審查與專案翻譯工具
- 使用 Azure OpenAI 或 OpenAI 作為提供者的翻譯
- 允許 MCP 託管代理在無需 Co-op Translator LLM 憑證的情況下翻譯 Markdown 與筆記本區塊
- 使用 Azure AI Vision 進行圖片文字擷取與翻譯
- 以確定性檢查審查翻譯結構與新鮮度
- 保留 Markdown 格式與結構

## 文件

- [文件網站](https://azure.github.io/co-op-translator/)
- [選擇您的工作流程](../../docs/workflows.md)
- [設定](../../docs/configuration.md)
- [Azure AI 設定](../../docs/azure-ai-setup.md)
- [CLI 參考](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP 伺服器](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README 語言範本](../../docs/readme-languages-template.md)
- [支援語言](../../docs/supported-languages.md)
- [貢獻指南](../../CONTRIBUTING.md)
- [故障排除](../../docs/troubleshooting.md)

### Microsoft 專屬指南
> [!NOTE]
> 僅適用於 Microsoft “For Beginners” 倉庫的維護者。

- [更新 “other courses” 清單（僅適用於 MS Beginners 倉庫）](../../docs/microsoft-beginners.md)

## 支持我們並促進全球學習

加入我們，一同改變教育內容在全球的分享方式！在 GitHub 為 [Co-op Translator](https://github.com/azure/co-op-translator) 給予一個 ⭐，支持我們打破學習與科技的語言障礙的使命。您的興趣與貢獻會產生重大影響！程式碼貢獻與功能建議隨時歡迎。

### 用你的語言探索 Microsoft 教育內容
- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
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

## 影片簡報

👉 點擊下方圖片於 YouTube 觀看。

- **Open at Microsoft**：一個簡短的 18 分鐘介紹，以及如何使用 Co-op Translator 的快速指南。

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 貢獻

本專案歡迎貢獻與建議。想為 Azure Co-op Translator 作出貢獻嗎？請參閱我們的 [CONTRIBUTING.md](../../CONTRIBUTING.md)，了解如何幫助使 Co-op Translator 更具可及性的指引。

## 貢獻者

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行為準則

本專案已採用 [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)。
如需更多資訊，請參閱 [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)，
或就其他疑問或意見聯絡 [opencode@microsoft.com](mailto:opencode@microsoft.com)。

## 負責任的 AI

Microsoft 致力協助客戶負責任地使用我們的 AI 產品，分享我們的經驗，並透過 Transparency Notes 與 Impact Assessments 等工具建立以信任為基礎的夥伴關係。許多這類資源可在 [https://aka.ms/RAI](https://aka.ms/RAI) 找到。
Microsoft 對負責任 AI 的做法建立於我們的 AI 原則：公平性、可靠性與安全、隱私與安全、包容性、透明度及問責制。

大型的自然語言、影像與語音模型——如本範例中使用的模型——可能會以不公平、不可靠或冒犯性的方式表現，進而造成傷害。請參閱 [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) 以了解相關風險與限制。

減輕這些風險的建議做法，是在您的架構中包含一個能夠偵測並阻止有害行為的安全系統。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供一個獨立的保護層，能夠在應用程式與服務中偵測使用者產生及 AI 產生的有害內容。Azure AI Content Safety 包含可偵測有害素材的文字與影像 API。我們也提供互動式的 Content Safety Studio，讓您檢視、瀏覽並試用跨不同模態偵測有害內容的範例程式碼。以下 [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) 將引導您如何向該服務發出請求。

另一個需考量的面向是整體應用程式的效能。對於多模態與多模型的應用，我們認為效能應表示系統能如您與使用者所預期地運作，包括不產生有害輸出。使用 [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) 評估您整體應用程式的效能非常重要。

您可以在開發環境中使用 [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) 評估您的 AI 應用程式。給定測試資料集或目標後，您的生成式 AI 應用的產出可以透過內建評估器或您自選的自訂評估器進行量化測量。要開始使用 prompt flow SDK 評估系統，您可以參考 [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。執行評估後，您可以在 [Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) 中視覺化結果。

## 商標

本專案可能包含專案、產品或服務的商標或標識。對 Microsoft 商標或標識的授權使用需遵守並依循
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。
在本專案的修改版本中使用 Microsoft 商標或標識，不得造成混淆或暗示 Microsoft 贊助。
任何第三方商標或標識的使用須遵循該第三方的政策。

## 尋求協助

如果您遇到困難或對建構 AI 應用有任何疑問，請加入：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如果您在開發過程中對產品有回饋或遇到錯誤，請造訪：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)