<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "33db54f4f3ca9f0321be05374b591f2b",
  "translation_date": "2025-05-06T17:59:01+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "tw"
}
-->
# Translate your project using Co-op Translator

**Co-op Translator** 是一個命令列介面（CLI）工具，幫助你將專案中的 markdown 與圖片檔案翻譯成多種語言。本節說明如何使用這個工具，介紹各種 CLI 選項，並提供不同使用情境的範例。

> [!NOTE]
> 有關完整指令清單及詳細說明，請參考 [Command reference](./command-reference.md)。

---

## 範例情境與指令

以下列出幾個常見的 **Co-op Translator** 使用情境，並附上相對應的執行指令。

### 1. 基本翻譯（單一語言）

若要將整個專案（markdown 檔與圖片）翻譯成單一語言，例如韓文，請使用以下指令：

```bash
translate -l "ko"
```

此指令會將所有 markdown 和圖片檔翻譯成韓文，並新增翻譯內容，不會刪除已存在的翻譯。

> [!TIP]
>
> 想知道 **Co-op Translator** 支援哪些語言代碼？請到專案的 [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) 區段查看。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 中，我用以下方式為現有的 markdown 檔與圖片新增韓文翻譯。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. 多語言翻譯

若要將專案翻譯成多種語言（例如西班牙文、法文和德文），請使用這個指令：

```bash
translate -l "es fr de"
```

此指令會將專案翻譯成西班牙文、法文和德文，新增翻譯內容而不會覆蓋現有的翻譯。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 中，拉取最新變更以反映最近的提交後，我用以下方式翻譯新加入的 markdown 檔與圖片。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> 通常建議一次只翻譯一種語言，但在需要新增特定變更的情況下，一次翻譯多種語言會更有效率。

### 3. 指定根目錄

預設情況下，翻譯工具會使用目前工作目錄。如果你的專案位於其他位置，請用 -r 選項指定根目錄：

```bash
translate -l "es fr de" -r "./my_project"
```

此指令會翻譯 `./my_project` 目錄中的檔案。

```bash
translate -l "ko" -u
```

此指令搭配 `-u` 選項，會刪除指定語言的所有既有翻譯並重新翻譯。

警告：執行此指令前會提示你確認，避免誤刪現有翻譯。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 中，我用以下方式更新所有西班牙文翻譯檔。當原始內容在多個 markdown 文件中有大量變更時，建議使用此方法。若只需更新少數翻譯檔，手動刪除那些檔案後再用 `-a` 參數新增翻譯會更有效率。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 6. 僅翻譯圖片

若只想翻譯專案中的圖片檔，請使用 `-img` 選項：

```bash
translate -l "ko" -img
```

此指令只會將圖片翻譯成韓文，不會影響任何 markdown 檔。

### 7. 僅翻譯 Markdown 檔案

若只想翻譯專案中的 markdown 檔，請使用 `-md` 選項：

```bash
translate -l "ko" -md
```

### 8. 檢查翻譯檔錯誤

若想檢查翻譯檔是否有錯誤，並在必要時重新嘗試翻譯，請使用 `-chk` 選項：

```bash
translate -l "ko" -chk
```

此指令會掃描已翻譯的 markdown 檔，並對有錯誤的檔案重新翻譯。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 中，我用以下方法檢查韓文翻譯檔的錯誤，並自動重試有問題的檔案翻譯。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

此選項會檢查翻譯錯誤。現在判定標準是：如果原文與譯文的換行差異超過六行，該檔案就會被標記為翻譯錯誤。未來計畫改進此標準，讓判斷更彈性。

例如，這個方法有助於偵測遺漏的段落或損壞的翻譯，並自動重試該檔案的翻譯。

不過，如果你已知道哪些檔案有問題，手動刪除那些檔案後，使用 `-a` option to re-translate them.

### 9. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` 參數會更有效率：

```bash
translate -l "ko" -d
```

此指令會以除錯模式執行翻譯，提供更多日誌資訊，方便你找出翻譯過程中的問題。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 中，我遇到 markdown 檔中含有大量連結的翻譯造成格式錯誤（例如翻譯斷裂、換行被忽略）。為了診斷問題，我使用 `-d` 選項查看翻譯流程的運作狀況。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 10. 翻譯所有語言

若想將專案翻譯成所有支援的語言，請使用 all 關鍵字。

> [!WARNING]
> 一次翻譯所有語言可能會花費大量時間，視專案大小而定。例如，將 **Phi-3 CookBook** 翻譯成西班牙文約需 2 小時。以此規模來看，一人要處理 20 種語言並不實際。建議分配給多位貢獻者，各負責一至兩種語言，並逐步更新翻譯。

```bash
translate -l "all"
```

此指令會將專案翻譯成所有可用語言。若繼續執行，翻譯時間可能會依專案大小而大幅增加。

> [!TIP]
>
> ### 刪除需要更新的檔案
> 若要更新 Pull Request 中最近變更的檔案，第一步是刪除所有翻譯資料夾中該檔案的既有版本。你可以用以下指令批次刪除翻譯資料夾中指定名稱的所有檔案。
>
> ### Windows 系統：
> 1. **使用命令提示字元**：
>    - 開啟命令提示字元。
>    - 使用 `cd` 指令切換到檔案所在資料夾。
>    - 執行以下指令刪除檔案：
>      ```
>      del /s *filename*
>      ```
>      其中 `/s` 選項會搜尋子目錄。
>
> 2. **使用 PowerShell**：
>    - 開啟 PowerShell。
>    - 執行以下指令：
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      將 `"C:\YourPath"` 替換為實際路徑。
>
> 使用 `cd` 搭配 `find` 指令：
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
> 將 `filename` 替換成目標檔名。
>
> 使用 `translate -l` 指令更新最新檔案變更。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們致力於提供準確的翻譯，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。