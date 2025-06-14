<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-14T12:50:36+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "mo"
}
-->
# 使用 Co-op Translator 翻譯您的項目

**Co-op Translator** 是一個命令行界面 (CLI) 工具，幫助您將項目中的 Markdown 和圖片文件翻譯成多種語言。本節介紹如何使用該工具，涵蓋各種 CLI 選項，並提供不同使用案例的示例。

---

## 示例場景和命令

以下是一些常見的 **Co-op Translator** 使用案例，以及相應的命令。

### 1. 基本翻譯（單一語言）

要將整個項目（Markdown 文件和圖片）翻譯成單一語言，例如韓語，請使用以下命令：

```bash
translate -l "ko"
```

此命令將所有 Markdown 和圖片文件翻譯成韓語，添加新翻譯而不刪除任何現有翻譯。

#### Phi-3 CookBook 示例

在 **Phi-3 CookBook** 中，我使用以下方法為現有的 Markdown 文件和圖片添加韓語翻譯。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. 翻譯多種語言

要將項目翻譯成多種語言（例如西班牙語、法語和德語），請使用此命令：

```bash
translate -l "es fr de"
```

此命令將項目翻譯成西班牙語、法語和德語，添加新翻譯而不覆蓋現有翻譯。

#### Phi-3 CookBook 示例

在 **Phi-3 CookBook** 中，在拉取最新更改以反映最新提交後，我使用以下方法翻譯新添加的 Markdown 文件和圖片。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

### 3. 更新翻譯（刪除現有翻譯）

要更新現有翻譯（即刪除當前翻譯並用新翻譯替換），請使用 `-u` 選項。這將刪除指定語言的所有現有翻譯並重新翻譯。

```bash
translate -l "ko" -u
```

警告：此命令將在繼續刪除現有翻譯之前提示您確認。

#### Phi-3 CookBook 示例

在 **Phi-3 CookBook** 中，我使用以下方法更新所有西班牙語翻譯文件。我建議在原始內容在多個 Markdown 文件中有重大更改時使用此方法。如果只有少數翻譯的 Markdown 文件需要更新，手動刪除那些特定文件然後使用 `-a` 方法添加更新翻譯會更有效。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. 只翻譯圖片

要只翻譯項目中的圖片文件，請使用 `-img` 選項：

```bash
translate -l "ko" -img
```

此命令將只翻譯圖片成韓語，而不影響任何 Markdown 文件。

### 6. 只翻譯 Markdown 文件

要只翻譯項目中的 Markdown 文件，請使用 `-md` 選項：

```bash
translate -l "ko" -md
```

### 7. 檢查翻譯文件中的錯誤

如果您想檢查翻譯文件中的錯誤並在必要時重試翻譯，請使用 `-chk` 選項：

```bash
translate -l "ko" -chk
```

此命令將掃描翻譯的 Markdown 文件並對有錯誤的文件重試翻譯。

#### Phi-3 CookBook 示例

在 **Phi-3 CookBook** 中，我使用以下方法檢查韓語文件中的翻譯錯誤，並自動重試翻譯有問題的文件。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

此選項檢查翻譯錯誤。目前，如果原始文件和翻譯文件之間的換行差異超過六行，則文件被標記為翻譯錯誤。我計劃在未來改進此標準以提高靈活性。

例如，此方法有助於檢測缺失的片段或損壞的翻譯，並將自動重試翻譯那些文件。

然而，如果您已經知道哪些文件有問題，手動刪除那些文件並使用 `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` 選項會更有效：

```bash
translate -l "ko" -d
```

此命令將在調試模式下運行翻譯，提供額外的日誌信息，幫助您識別翻譯過程中的問題。

#### Phi-3 CookBook 示例

在 **Phi-3 CookBook** 中，我遇到了一個問題，即 Markdown 文件中有許多鏈接的翻譯導致格式錯誤，如翻譯破裂和忽略換行。為了診斷此問題，我使用 `-d` 選項查看翻譯過程的工作情況。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. 翻譯所有語言

如果您想將項目翻譯成所有支持的語言，請使用 all 關鍵字。

```bash
translate -l "all"
```

此命令將項目翻譯成所有可用語言。如果繼續，根據項目大小，翻譯可能需要相當長的時間。

> ### 手動刪除翻譯文件（可選）
> 翻譯文件現在會在源文件更新時自動檢測和清理。
>
> 不過，如果您想手動更新翻譯 - 例如重新翻譯特定文件或覆蓋系統行為 - 您可以使用以下命令刪除語言文件夾中的所有版本。
>
> ### 在 Windows 上：
> 1. **使用命令提示符**：
>    - 打開命令提示符。
>    - 使用 `cd` 命令導航到文件所在文件夾。
>    - 使用以下命令刪除文件：
>      ```
>      del /s *filename*
>      ```
>      替換 `filename` with the specific part of the file name you're looking for. The `/s` 選項也會搜索子目錄。
>
> 2. **使用 PowerShell**：
>    - 打開 PowerShell。
>    - 運行此命令：
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      替換 `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` 命令：
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     替換 `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` 命令以更新最新文件更改。

**免責聲明**：  
本文件已使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始語言的文件視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤讀不承擔責任。