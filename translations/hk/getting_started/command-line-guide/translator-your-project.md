<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:42:37+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "hk"
}
-->
# 使用 Co-op Translator 翻譯你的專案

**Co-op Translator** 是一個命令行介面（CLI）工具，可以幫助你將專案中的 markdown 和圖片檔案翻譯成多種語言。本節將說明如何使用此工具，介紹各種 CLI 選項，並提供不同使用情境的範例。

> [!NOTE]
> 有關完整指令列表及詳細說明，請參考 [Command reference](./command-reference.md)。

---

## 範例情境與指令

以下列出幾個常見的 **Co-op Translator** 使用情境，並附上對應的執行指令。

### 1. 基本翻譯（單一語言）

若要將整個專案（markdown 檔案及圖片）翻譯成單一語言，例如韓文，請使用以下指令：

```bash
translate -l "ko"
```

此指令會將所有 markdown 和圖片檔案翻譯成韓文，新增翻譯內容而不會刪除現有翻譯。

> [!TIP]
>
> 想知道 **Co-op Translator** 支援哪些語言代碼嗎？請參考倉庫中的 [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) 部分了解詳情。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 中，我使用以下方式為現有的 markdown 檔案和圖片新增韓文翻譯。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. 多語言翻譯

若要將專案翻譯成多種語言（例如西班牙語、法語和德語），請使用此指令：

```bash
translate -l "es fr de"
```

此指令會將專案翻譯成西班牙語、法語和德語，新增翻譯內容而不會覆蓋現有翻譯。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 中，拉取最新變更以反映最近的提交後，我使用以下方法翻譯新加入的 markdown 檔案和圖片。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> 一般建議一次翻譯一種語言，但在需要針對特定變更同時加入多種語言時，一次翻譯多語言會比較有效率。

### 3. 更新翻譯（刪除現有翻譯）

若要更新現有翻譯（即刪除現有翻譯並重新翻譯），請使用 `-u` 選項。此操作會刪除指定語言的所有現有翻譯並重新翻譯。

```bash
translate -l "ko" -u
```

警告：此指令執行前會要求你確認是否刪除現有翻譯。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 中，我使用以下方法更新所有西班牙語翻譯檔案。當原始內容在多個 markdown 文件中有重大變更時，建議使用此方法。如果只需更新少數翻譯檔案，則手動刪除那些檔案後，再用 `-a` 方法新增更新後的翻譯會更有效率。

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

### 6. 僅翻譯 markdown 檔案

若只想翻譯專案中的 markdown 檔案，請使用 `-md` 選項：

```bash
translate -l "ko" -md
```

### 7. 檢查翻譯檔案錯誤

若想檢查翻譯檔案是否有錯誤，並在必要時重試翻譯，請使用 `-chk` 選項：

```bash
translate -l "ko" -chk
```

此指令會掃描已翻譯的 markdown 檔案，並對有錯誤的檔案重新嘗試翻譯。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 中，我使用以下方法檢查韓文檔案的翻譯錯誤，並自動重試有問題的檔案翻譯。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

此選項用於檢查翻譯錯誤。目前判定標準是：若原文與譯文的換行符號差異超過六行，該檔案會被標記為翻譯錯誤。未來我計劃改進此標準，使其更具彈性。

例如，這方法對於偵測缺少翻譯區塊或翻譯損壞非常有用，且會自動重新嘗試翻譯這些檔案。

不過，如果你已知道哪些檔案有問題，手動刪除那些檔案，然後使用 `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` 選項會更有效率：

```bash
translate -l "ko" -d
```

此指令會以除錯模式執行翻譯，提供額外的日誌資訊，幫助你找出翻譯過程中的問題。

#### Phi-3 CookBook 範例

在 **Phi-3 CookBook** 中，我遇到過 markdown 檔案中含大量連結的翻譯導致格式錯誤，例如翻譯斷裂與換行被忽略。為了診斷問題，我使用了 `-d` 選項來觀察翻譯流程。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. 翻譯所有語言

若想將專案翻譯成所有支援語言，請使用 all 關鍵字。

> [!WARNING]
> 一次翻譯所有語言可能會耗費大量時間，視專案規模而定。例如，將 **Phi-3 CookBook** 翻譯成西班牙語約花了 2 小時。考慮到規模，單人處理 20 種語言並不實際。建議分配給多位貢獻者，每人負責一到兩種語言，並逐步更新翻譯。

```bash
translate -l "all"
```

此指令會將專案翻譯成所有可用語言。若執行，翻譯時間會因專案大小而異。

> [!TIP]
>
> ### 手動刪除翻譯檔案（可選）
> 當原始檔案更新時，翻譯檔案現在會自動被偵測並清理。
>
> 不過，如果你想手動更新翻譯，例如重新翻譯特定檔案或覆寫系統行為，可以使用以下指令刪除所有語言資料夾中該檔案的版本。
>
> ### 在 Windows 上：
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
> Once you have deleted the files which need to be replace simply rerun your `translate -l` 指令以更新最新檔案變更。

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。對於因使用本翻譯而引起的任何誤解或誤譯，我們概不負責。