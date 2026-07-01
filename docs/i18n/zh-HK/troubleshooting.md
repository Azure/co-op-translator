# 疑難排解

當翻譯執行意外成功、在設定期間失敗，或產生需要檢視的輸出時，請使用此頁面。

## 從這裡開始

1. 首先執行一個有針對性的指令，例如 `translate -l "ko" -md`。
2. 加上 `-d` 以啟用主控台除錯日誌。
3. 加上 `-s` 將除錯日誌儲存在 `<root-dir>/logs/`。
4. 翻譯後執行 `co-op-review` 以檢查新鮮度、結構和本地連結。

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## 設定錯誤

### 沒有語言模型提供者

錯誤：

```text
No language model configuration found.
```

解決方法：

- 設定 Azure OpenAI 或 OpenAI。
- 確認變數存在於執行該指令的環境中。
- 若在本地使用，請將它們放在專案根目錄的 `.env`。

參見 [設定](configuration.md)。

### 在沒有 Azure AI Vision 的情況下進行圖片翻譯

錯誤：

```text
Image translation requested but Azure AI Service is not configured.
```

解決方法：

- 新增 `AZURE_AI_SERVICE_API_KEY`。
- 新增 `AZURE_AI_SERVICE_ENDPOINT`。
- 或執行只處理文字的指令，例如 `translate -l "ko" -md`。

### 無效的金鑰或端點

癥狀可能包括 `401`、被隱藏的權限錯誤，或端點存取錯誤。

解決方法：

- 確認金鑰屬於與端點相同的 Azure 資源。
- 若使用 `-img`，確認該資源支援 Vision。
- 確認 Azure OpenAI 的部署名稱和 API 版本與你的部署相符。
- 使用除錯日誌執行：`translate -l "ko" -md -d -s`。

## 沒有任何檔案被翻譯

常見原因：

- 選取的旗標與你的檔案不相符。
- 已有翻譯檔案存在。
- 原始檔案位於被排除的目錄下。
- 指令是在錯誤的專案根目錄執行。

檢查項目：

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

當指令在專案根目錄之外執行時，使用 `--root-dir`。

## 意外的連結行為

連結重寫取決於所選的內容類型：

- 包含 `-nb`：筆記本連結可以指向已翻譯的筆記本。
- 排除 `-nb`：筆記本連結可以仍然指向原始筆記本。
- 包含 `-img`：圖片連結可以指向已翻譯的圖片。
- 排除 `-img`：圖片連結可以仍然指向原始圖片。

當所有內部連結都應優先指向已翻譯的輸出時，執行完整內容翻譯：

```bash
translate -l "ko" -md -nb -img
```

翻譯後執行連結檢查：

```bash
co-op-review -l "ko"
```

## Markdown 呈現問題

如果翻譯後的 Markdown 呈現不正確：

- 檢查 frontmatter 是否以 `---` 開頭和結尾。
- 檢查程式碼區塊（code fence）的數量在原始檔案和翻譯檔案之間是否相符。
- 執行 `co-op-review` 以找出常見的結構問題。
- 若輸出被損壞，請重新翻譯該特定檔案。

```bash
co-op-review -l "ko" --format github
```

## GitHub Action 執行但未建立 Pull Request

如果 `peter-evans/create-pull-request` 報告分支沒有領先於 base，表示工作流程找不到要提交的檔案。

可能原因：

- 翻譯執行未產生任何變更。
- `.gitignore` 排除了 `translations/`、`translated_images/` 或已翻譯的筆記本。
- `add-paths` 與產生的輸出目錄不匹配。
- 翻譯步驟提前結束。

解決方法：

1. 確認在 `translations/` 或 `translated_images/` 中存在產生的檔案。
2. 確認 `.gitignore` 沒有忽略產生的輸出。
3. 使用相符的 `add-paths`：

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. 臨時在 translate 指令中加入除錯旗標：

   ```bash
   translate -l "ko" -md -d -s
   ```

5. 確認工作流程權限包含：

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## 翻譯品質

機器翻譯可能需要人工審核。僅在你想要進行實驗性的品質評分和低信心修復工作流程時才使用 `evaluate`。

!!! warning "實驗性"
    `evaluate` 可能會使用基於規則和基於 LLM 的檢查，其評分模型與元資料行為可能會改變。除非你的工作流程已準備好因應變動，否則不要將它放入必要的 CI 閘道中。

對於確定性的 CI 檢查，請改用 `co-op-review`。