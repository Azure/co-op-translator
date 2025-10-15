<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T02:33:08+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "hk"
}
-->
# 使用 Co-op Translator 翻譯你的項目

**Co-op Translator** 是一個命令列介面（CLI）工具，可以幫你將項目中的 markdown 和圖片檔案翻譯成多種語言。這一部分會說明如何使用這個工具、各種 CLI 選項，以及不同情境下的使用範例。

> [!NOTE]
> 如需完整指令列表及詳細說明，請參考 [指令參考](./command-reference.md)。

---

## 範例情境及指令

以下是一些常見的 **Co-op Translator** 用法，以及相應的指令。

### 1. 基本翻譯（單一語言）

如果你想將整個項目（包括 markdown 檔案和圖片）翻譯成單一語言，例如韓文，可以使用以下指令：

```bash
translate -l "ko"
```

這個指令會將所有 markdown 和圖片檔案翻譯成韓文，並新增翻譯，不會刪除現有的翻譯。

> [!TIP]
>
> 想知道 **Co-op Translator** 支援哪些語言代碼？可以到 [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) 查看詳細資料。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 裡，我用以下方法為現有的 markdown 檔案和圖片新增韓文翻譯。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. 多語言翻譯

如果你想將項目翻譯成多種語言（例如西班牙文、法文和德文），可以用這個指令：

```bash
translate -l "es fr de"
```

這個指令會將項目翻譯成西班牙文、法文和德文，並新增翻譯，不會覆蓋現有的翻譯。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 裡，拉取最新的變更以反映最近的提交後，我用以下方法翻譯新加入的 markdown 檔案和圖片。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> 一般建議一次只翻譯一種語言，但像這種需要加入特定變更的情況下，同時翻譯多種語言會更有效率。

### 3. 更新翻譯（刪除現有翻譯）

如果你要更新現有翻譯（即刪除目前的翻譯並重新翻譯），可以用 `-u` 選項。這會刪除指定語言的所有現有翻譯，然後重新翻譯。

```bash
translate -l "ko" -u
```

注意：這個指令會在刪除現有翻譯前提示你確認。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 裡，我用以下方法更新所有西班牙文翻譯檔案。如果原始內容在多個 markdown 文件有重大變更，建議用這個方法。如果只需要更新少量翻譯檔案，手動刪除那些檔案後再用 `-a` 方法新增翻譯會更有效率。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. 只翻譯圖片

如果你只想翻譯項目中的圖片檔案，可以用 `-img` 選項：

```bash
translate -l "ko" -img
```

這個指令只會將圖片翻譯成韓文，不會影響 markdown 檔案。

### 6. 只翻譯 Markdown 檔案

如果你只想翻譯項目中的 markdown 檔案，可以用 `-md` 選項：

```bash
translate -l "ko" -md
```

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 裡，我用以下方法檢查韓文檔案的翻譯錯誤，並自動重試有問題的檔案。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

這個選項會檢查翻譯錯誤。目前，如果原始檔案和翻譯檔案的換行數差距超過六行，該檔案會被標記為有翻譯錯誤。未來我會改善這個判斷標準，讓它更有彈性。

例如，這個方法可以用來偵測缺漏段落或損壞的翻譯，並自動重試翻譯那些檔案。

但如果你已經知道哪些檔案有問題，手動刪除那些檔案後用 `-a` 選項重新翻譯會更有效率。

### 8. 除錯模式

如果你需要詳細日誌來排查問題，可以用 `-d` 選項：

```bash
translate -l "ko" -d
```

這個指令會在除錯模式下執行翻譯，提供更多日誌資訊，幫助你找出翻譯過程中的問題。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 裡，我遇到 markdown 檔案裡有很多連結時，翻譯會出現格式錯誤，例如翻譯斷裂或換行被忽略。為了診斷這個問題，我用 `-d` 選項來查看翻譯過程的細節。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. 翻譯所有語言

如果你想將項目翻譯成所有支援的語言，可以用 all 關鍵字。

> [!WARNING]
> 一次翻譯所有語言可能會花很長時間，視項目大小而定。例如，將 **Phi-3 CookBook** 翻譯成西班牙文就花了約兩小時。以這個規模來說，一個人要處理 20 種語言並不實際。建議分工，由多位貢獻者各自負責一至兩種語言，逐步更新翻譯。

```bash
translate -l "all"
```

這個指令會將項目翻譯成所有可用語言。如果你執行這個指令，翻譯時間會依項目大小而定，可能會很久。

> [!TIP]
>
> ### 手動刪除翻譯檔案（選用）
> 現在只要原始檔案有更新，翻譯檔案會自動偵測並清理。
>
> 不過，如果你想手動更新翻譯（例如重做某個檔案或覆蓋系統行為），可以用以下指令刪除該檔案在所有語言資料夾的版本。
>
> ### Windows 系統：
> 1. **使用命令提示字元**：
>    - 開啟命令提示字元。
>    - 用 `cd` 指令切換到檔案所在的資料夾。
>    - 用以下指令刪除檔案：
>      ```
>      del /s *filename*
>      ```
>      把 `filename` 換成你要找的檔案名稱片段。`/s` 參數會搜尋子目錄。
>
> 2. **使用 PowerShell**：
>    - 開啟 PowerShell。
>    - 執行這個指令：
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      把 `"C:\YourPath"` 換成資料夾路徑，`filename` 換成檔案名稱。
>
> ### macOS/Linux 系統：
> 1. **使用終端機**：
>   - 開啟終端機。
>   - 用 `cd` 切換到目錄。
>   - 用 `find` 指令：
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     把 `filename` 換成檔案名稱。
>
> 刪除前請務必再次確認檔案，以免誤刪。
>
> 刪除需要重做的檔案後，只要重新執行 `translate -l` 指令，就能更新最新的檔案內容。

---

**免責聲明**：
本文件經由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能會包含錯誤或不準確之處。原始語言版本應被視為具權威性的來源。對於重要資訊，建議使用專業人工翻譯。因使用本翻譯而引起的任何誤解或錯誤，我們概不負責。