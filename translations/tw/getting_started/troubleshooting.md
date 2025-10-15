<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T02:35:33+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "tw"
}
-->
# Microsoft Co-op Translator 疑難排解指南

## 概述
Microsoft Co-Op Translator 是一款強大的工具，能夠無縫翻譯 Markdown 文件。本指南將協助你排解在使用此工具時常見的問題。

## 常見問題與解決方法

### 1. Markdown 標籤問題
**問題：** 翻譯後的 Markdown 文件頂部出現 `markdown` 標籤，導致渲染異常。

**解決方法：** 只需刪除文件頂部的 `markdown` 標籤，即可讓 Markdown 文件正確顯示。

**步驟：**
1. 開啟翻譯後的 Markdown（.md）文件。
2. 找到文件頂部的 `markdown` 標籤。
3. 刪除該標籤。
4. 儲存文件。
5. 重新開啟文件，確認渲染正常。

### 2. 內嵌圖片 URL 問題
**問題：** 內嵌圖片的 URL 與語言地區不符，導致圖片顯示錯誤或遺失。

**解決方法：** 檢查內嵌圖片的 URL，確保其語言地區標籤與文件一致。所有圖片都位於 `translated_images` 資料夾，每張圖片檔名中都包含語言地區標籤。

**步驟：**
1. 開啟翻譯後的 Markdown 文件。
2. 找出內嵌圖片及其 URL。
3. 確認圖片檔名中的語言地區標籤與文件語言一致。
4. 如有需要，更新圖片 URL。
5. 儲存並重新開啟文件，確認圖片顯示正常。

### 3. 翻譯準確度
**問題：** 翻譯內容不夠準確或需要進一步編輯。

**解決方法：** 仔細檢查翻譯文件，進行必要的修正以提升準確度與可讀性。

**步驟：**
1. 開啟翻譯後的文件。
2. 仔細檢查內容。
3. 進行必要的修正。
4. 儲存變更。

## 4. 權限錯誤、內容被遮蔽或 404

如果圖片或文字未正確翻譯，且在使用 -d debug 模式時出現 401 錯誤，這通常是認證失敗——金鑰無效、過期，或未連結到正確的端點區域。

請使用 [-d debug 參數](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) 執行 co-op translator，以獲得更詳細的錯誤原因。

- **錯誤訊息**：`Access denied due to invalid subscription key or wrong API endpoint.`
- **可能原因**：
  - 請求中的訂閱金鑰被遮蔽或填寫錯誤。
  - AI Services Key 或 Subscription Key 屬於其他 Azure 資源（如 Translator 或 OpenAI），而非 **Azure AI Vision** 資源。

 **資源類型**
  - 前往 [Azure Portal](https://portal.azure.com) 或 [Azure AI Foundry](https://ai.azure.com)，確認資源類型為 `Azure AI services` → `Vision`。
  - 驗證金鑰，確保使用正確的金鑰。

## 5. 設定錯誤（新錯誤處理）

從新的選擇性翻譯系統開始，Co-op Translator 會在必要服務未設定時，提供明確的錯誤訊息。

### 5.1. 未設定 Azure AI 服務以進行圖片翻譯

**問題：** 你請求了圖片翻譯（`-img` 參數），但 Azure AI 服務未正確設定。

**錯誤訊息：**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**解決方法：**
1. **選項一**：設定 Azure AI 服務
   - 在 `.env` 檔案中加入 `AZURE_AI_SERVICE_API_KEY`
   - 在 `.env` 檔案中加入 `AZURE_AI_SERVICE_ENDPOINT`
   - 確認服務可正常存取

2. **選項二**：移除圖片翻譯請求
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. 缺少必要設定

**問題：** 缺少必要的 LLM 設定。

**錯誤訊息：**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**解決方法：**
1. 確認你的 `.env` 檔案中至少有下列其中一組 LLM 設定：
   - **Azure OpenAI**：`AZURE_OPENAI_API_KEY` 和 `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**：`OPENAI_API_KEY`
   
   你只需設定 Azure OpenAI 或 OpenAI 其中之一，不需同時設定。

### 5.3. 選擇性翻譯混淆

**問題：** 指令執行成功但沒有任何文件被翻譯。

**可能原因：**
- 檔案類型參數（`-md`、`-img`、`-nb`）設定錯誤
- 專案中沒有符合的檔案
- 目錄結構不正確

**解決方法：**
1. **使用 debug 模式** 觀察詳細過程：
   ```bash
   translate -l "ko" -md -d
   ```

2. **檢查專案中的檔案類型**：
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **確認參數組合正確**：
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. 舊系統遷移

### 6.1. Markdown-only 模式已棄用

**問題：** 依賴自動 markdown-only 回退的指令不再如預期運作。

**舊行為：**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**新行為：**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**解決方法：**
- **明確指定** 你要翻譯的內容：
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. 連結行為異常

**問題：** 翻譯後的文件中連結指向非預期位置。

**原因：** 連結處理方式會根據所選檔案類型動態變化。

**解決方法：**
1. **了解新的連結行為**：
   - 有加 `-nb`：筆記本連結指向翻譯後版本
   - 沒加 `-nb`：筆記本連結指向原始檔案
   - 有加 `-img`：圖片連結指向翻譯後版本
   - 沒加 `-img`：圖片連結指向原始檔案

2. **根據需求選擇正確組合**：
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action 執行但未建立 Pull Request (PR)

**現象：** `peter-evans/create-pull-request` 的 workflow 日誌顯示：

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**可能原因：**
- **沒有偵測到變更：** 翻譯步驟沒有產生差異（repo 已是最新）。
- **輸出被忽略：** `.gitignore` 排除了你預期要提交的檔案（如 `*.ipynb`、`translations/`、`translated_images/`）。
- **add-paths 不符：** action 提供的路徑與實際輸出位置不符。
- **Workflow 邏輯/條件：** 翻譯步驟提前結束或寫入了非預期目錄。

**如何修正／確認：**
1. **確認輸出存在：** 翻譯後，檢查工作目錄下 `translations/` 和／或 `translated_images/` 是否有新檔案或變更。
   - 若翻譯筆記本，確認 `.ipynb` 實際寫入 `translations/<lang>/...`。
2. **檢查 `.gitignore`：** 不要忽略產生的輸出。請確保沒有忽略：
   - `translations/`
   - `translated_images/`
   - `*.ipynb`（若有翻譯筆記本）
3. **確保 add-paths 與輸出相符：** 使用多行值，並同時包含兩個資料夾（如適用）：
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **強制建立 PR 以除錯：** 臨時允許空提交，確認流程正確：
   ```yaml
   with:
     commit-empty: true
   ```
5. **啟用 debug 模式執行：** 在 translate 指令加上 `-d`，可顯示發現與寫入的檔案。
6. **權限（GITHUB_TOKEN）：** 確認 workflow 具有建立 commit 與 PR 的寫入權限：
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## 快速除錯檢查清單

排解翻譯問題時：

1. **啟用 debug 模式**：加上 `-d` 參數，查看詳細日誌
2. **檢查參數**：確認 `-md`、`-img`、`-nb` 是否符合你的需求
3. **確認設定**：檢查 `.env` 檔案是否有必要金鑰
4. **逐步測試**：先只用 `-md`，再逐步加入其他類型
5. **檢查檔案結構**：確認來源檔案存在且可存取

如需更多指令與參數說明，請參閱 [指令參考](./command-reference.md)。

---

**免責聲明**：
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不精確之處。原始語言的文件應視為最具權威性的來源。對於重要資訊，建議採用專業人工翻譯。因使用本翻譯而產生的任何誤解或誤釋，我們概不負責。