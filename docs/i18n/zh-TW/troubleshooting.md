# 疑難排解

使用此頁面當翻譯執行意外成功、在設定期間失敗，或產生需要審查的輸出時。

## 從這裡開始

1. 先執行一個專注的指令，例如 `translate -l "ko" -md`。
2. 加上 `-d` 以取得主控台偵錯日誌。
3. 加上 `-s` 將偵錯日誌儲存在 `<root-dir>/logs/` 下。
4. 於翻譯後執行 `co-op-review` 以檢查新鮮度、結構與本機連結。

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## 設定錯誤

### 未指定語言模型提供者

錯誤：

```text
No language model configuration found.
```

修正：

- 設定 Azure OpenAI、OpenAI，或 Anthropic。
- 驗證變數已存在於執行此指令的環境中。
- 本機使用時，將它們放在專案根目錄的 `.env`。

參見 [設定](configuration.md)。

### 在沒有 Azure AI Vision 的情況下進行圖像翻譯

錯誤：

```text
Image translation requested but Azure AI Service is not configured.
```

修正：

- 新增 `AZURE_AI_SERVICE_API_KEY`。
- 新增 `AZURE_AI_SERVICE_ENDPOINT`。
- 或執行僅文字的指令，例如 `translate -l "ko" -md`。

### 無效的金鑰或端點

症狀可能包括 `401`、被遮蔽的權限錯誤或端點存取錯誤。

修正：

- 確認該金鑰屬於與端點相同的 Azure 資源。
- 使用 `-img` 時，確認該資源支援 Vision。
- 確認 Azure OpenAI 部署名稱與 API 版本與你的部署相符。
- 使用偵錯日誌執行：`translate -l "ko" -md -d -s`。

## 沒有檔案被翻譯

常見原因：

- 所選旗標與你的檔案不符。
- 已存在已翻譯的檔案。
- 原始檔案位於被排除的目錄下。
- 指令是在錯誤的專案根目錄執行。

檢查項目：

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

當指令在專案根目錄外執行時，使用 `--root-dir`。

## 意外的連結行為

連結重寫取決於所選的內容類型：

- `-nb` 包含: 筆記本連結可以指向已翻譯的筆記本.
- `-nb` 排除: 筆記本連結可以維持指向原始筆記本.
- `-img` 包含: 圖片連結可以指向已翻譯的圖片.
- `-img` 排除: 圖片連結可以維持指向原始圖片.

當所有內部連結應優先使用已翻譯的輸出時，執行完整內容翻譯：

```bash
translate -l "ko" -md -nb -img
```

於翻譯後執行連結審查：

```bash
co-op-review -l "ko"
```

## Markdown 呈現問題

如果翻譯後的 Markdown 呈現不正確：

- 檢查 frontmatter 是否以 `---` 開頭和結尾。
- 檢查程式碼區塊圍欄（code fence）在原始與翻譯檔案間的數量是否一致。
- 執行 `co-op-review` 以抓出常見的結構問題。
- 如果輸出被破壞，請重新翻譯該檔案。

```bash
co-op-review -l "ko" --format github
```

## GitHub Action 已執行但未建立 Pull Request

若 `peter-evans/create-pull-request` 報告分支未領先 base，則工作流程未找到可提交的檔案。

可能原因：

- 翻譯執行未產生變更。
- `.gitignore` 排除了 `translations/`、`translated_images/`，或已翻譯的筆記本。
- `add-paths` 與產生的輸出目錄不相符。
- 翻譯步驟提早結束。

修正：

1. 確認 `translations/` 或 `translated_images/` 中存在產生的檔案。
2. 確認 `.gitignore` 未忽略產生的輸出。
3. 使用對應的 `add-paths`：

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. 暫時在 translate 指令中加入偵錯旗標：

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

機器翻譯可能需要人工審查。僅在你想要試驗性品質評分和低信心修正工作流程時使用 `evaluate`。

!!! warning "實驗性"
    `evaluate` 可能會使用基於規則和基於 LLM 的檢查，其評分模型與 metadata 行為可能會改變。除非你的工作流程已準備好接受變更，否則不要將它放入必要的 CI 門檻。

對於決定性的 CI 檢查，請改用 `co-op-review`。