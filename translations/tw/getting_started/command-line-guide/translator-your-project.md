<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:43:01+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "tw"
}
-->
# 使用 Co-op Translator 翻譯您的專案

**Co-op Translator** 是一個命令列介面（CLI）工具，可協助您將專案中的 markdown 與圖片檔案翻譯成多種語言。本節說明如何使用此工具，涵蓋各種 CLI 選項，並提供不同使用情境的範例。

> [!NOTE]
> 有關完整指令列表及詳細說明，請參考[指令參考](./command-reference.md)。

---

## 範例情境與指令

以下列出幾個常見的 **Co-op Translator** 使用情境，以及相應的指令。

### 1. 基本翻譯（單一語言）

若要將整個專案（markdown 檔案與圖片）翻譯成單一語言，例如韓文，請使用以下指令：

```bash
translate -l "ko"
```

此指令會將所有 markdown 與圖片檔案翻譯成韓文，新增翻譯內容，且不會刪除任何現有翻譯。

> [!TIP]
>
> 想知道 **Co-op Translator** 支援哪些語言代碼？請參閱專案中的[支援語言](https://github.com/Azure/co-op-translator#supported-languages)章節了解詳情。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 中，我使用以下方法為現有的 markdown 檔案與圖片新增韓文翻譯。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. 多語言翻譯

若要將專案翻譯成多種語言（例如西班牙語、法語與德語），請使用此指令：

```bash
translate -l "es fr de"
```

此指令會將專案翻譯成西班牙語、法語和德語，新增翻譯內容且不會覆蓋現有翻譯。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 中，拉取最新變更以反映最新提交後，我使用以下方法翻譯新加入的 markdown 檔案與圖片。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> 一般建議一次翻譯一種語言，但在需要針對特定變更同時新增多語言翻譯時，一次處理多種語言會更有效率。

### 3. 更新翻譯（刪除現有翻譯）

若要更新現有翻譯（即刪除目前翻譯並重新翻譯），請使用 `-u` 選項。此操作會刪除指定語言所有現有翻譯並重新翻譯。

```bash
translate -l "ko" -u
```

警告：執行此指令前會要求您確認是否刪除現有翻譯。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 中，我使用以下方法更新所有西班牙語翻譯檔案。當多個 markdown 文件的原始內容有重大變更時，建議使用此方法。如果只需更新少數翻譯檔案，手動刪除特定檔案後，再用 `-a` 方法新增更新的翻譯會更有效率。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. 僅翻譯圖片

若只想翻譯專案中的圖片檔案，請使用 `-img` 選項：

```bash
translate -l "ko" -img
```

此指令只會將圖片翻譯成韓文，不會影響任何 markdown 檔案。

### 6. 僅翻譯 Markdown 檔案

若只想翻譯專案中的 markdown 檔案，請使用 `-md` 選項：

```bash
translate -l "ko" -md
```

### 7. 檢查翻譯檔案錯誤

若想檢查翻譯檔案是否有錯誤，並在必要時重新嘗試翻譯，請使用 `-chk` 選項：

```bash
translate -l "ko" -chk
```

此指令會掃描已翻譯的 markdown 檔案，並針對有錯誤的檔案重新嘗試翻譯。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 中，我使用以下方法檢查韓文檔案的翻譯錯誤，並自動重試有問題的檔案翻譯。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

此選項用於檢查翻譯錯誤。目前若原始檔與翻譯檔的換行差異超過六行，該檔案即被判定為有翻譯錯誤。我計畫未來改進此判斷標準，使其更具彈性。

舉例來說，此方法適合偵測遺漏區塊或翻譯錯誤，並自動重試這些檔案的翻譯。

不過，如果您已知道哪些檔案有問題，手動刪除那些檔案後，再使用 `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` 選項會更有效率：

```bash
translate -l "ko" -d
```

此指令會以除錯模式執行翻譯，提供額外的日誌資訊，幫助您找出翻譯過程中的問題。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 中，我遇到 markdown 檔案中大量連結造成格式錯誤的問題，例如翻譯斷裂與忽略換行。為診斷此問題，我使用 `-d` 選項觀察翻譯過程的運作方式。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. 翻譯所有語言

若想將專案翻譯成所有支援語言，請使用 `all` 關鍵字。

> [!WARNING]
> 一次翻譯所有語言可能需要相當長的時間，視專案大小而定。例如，將 **Phi-3 CookBook** 翻譯成西班牙語約需 2 小時。考量工作量，單人同時處理 20 種語言並不實際。建議將工作分配給多位貢獻者，每人負責一至兩種語言，並逐步更新翻譯。

```bash
translate -l "all"
```

此指令會將專案翻譯成所有可用語言。若繼續執行，翻譯時間可能會因專案大小而大幅增加。

> [!TIP]
>
> ### 手動刪除翻譯檔案（選用）
> 當原始檔案更新時，系統會自動偵測並清理相關翻譯檔案。
>
> 不過，若您想手動更新翻譯——例如重做特定檔案或覆寫系統行為——可以使用以下指令刪除所有語言資料夾中該檔案的版本。
>
> ### Windows 系統：
> 1. **使用命令提示字元**：
>    - 開啟命令提示字元。
>    - 使用 `cd` 指令切換到檔案所在資料夾。
>    - 使用以下指令刪除檔案：
>      ```
>      del /s *filename*
>      ```
>      `filename` with the specific part of the file name you're looking for. The `/s` 選項會搜尋子目錄。
>
> 2. **使用 PowerShell**：
>    - 開啟 PowerShell。
>    - 執行此指令：
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      替換 `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` 指令：
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     替換 `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` 指令以更新最近檔案變更。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。對於因使用本翻譯而產生之任何誤解或誤譯，我們概不負責。