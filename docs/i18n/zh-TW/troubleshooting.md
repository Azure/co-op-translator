# 疑難排解

當翻譯執行意外成功、在設定期間失敗，或產生需要審查的輸出時，請使用此頁面。

## 從這裡開始

1. 首先執行一個聚焦命令，例如 `translate -l "ko" -md`。
2. 新增 `-d` 以顯示主控台除錯日誌。
3. 新增 `-s` 將除錯日誌儲存在 `<root-dir>/logs/`。
4. 翻譯後執行 `co-op-review` 以檢查是否為最新、結構與本地連結。

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

修正：

- 設定 Azure OpenAI 或 OpenAI。
- 驗證變數存在於執行命令的環境中。
- 若於本機使用，將它們放在專案根目錄的 `.env`。

請參閱 [設定](configuration.md)。

### 在沒有 Azure AI Vision 的情況下進行圖片翻譯

錯誤：

```text
Image translation requested but Azure AI Service is not configured.
```

修正：

- 新增 `AZURE_AI_SERVICE_API_KEY`。
- 新增 `AZURE_AI_SERVICE_ENDPOINT`。
- 或執行僅文字的命令，例如 `translate -l "ko" -md`。

### 無效的金鑰或端點

症狀可能包含 `401`、被遮蔽的權限錯誤，或端點存取錯誤。

修正：

- 確認金鑰與端點屬於相同的 Azure 資源。
- 在使用 `-img` 時，確認該資源支援 Vision。
- 確認 Azure OpenAI 的部署名稱與 API 版本符合您的部署。
- 使用除錯日誌執行：`translate -l "ko" -md -d -s`。

## 沒有檔案被翻譯

常見原因：

- 選取的旗標與您的檔案不符。
- 已存在翻譯後的檔案。
- 原始檔案位於被排除的目錄下。
- 命令在錯誤的專案根目錄執行。

檢查項目：

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

當命令在專案根目錄外執行時，使用 `--root-dir`。

## 連結行為異常

連結重寫取決於所選的內容類型：

- 若包含 `-nb`：筆記本連結可以指向已翻譯的筆記本。
- 若排除 `-nb`：筆記本連結可以維持指向原始筆記本。
- 若包含 `-img`：圖片連結可以指向已翻譯的圖片。
- 若排除 `-img`：圖片連結可以維持指向原始圖片。

當所有內部連結都應偏好指向已翻譯輸出時，執行完整內容翻譯：

```bash
translate -l "ko" -md -nb -img
```

翻譯後執行連結審查：

```bash
co-op-review -l "ko"
```

## Markdown 呈現問題

若翻譯後的 Markdown 呈現不正確：

- 檢查 frontmatter 是否以 `---` 開始和結束。
- 檢查程式碼區塊的 fence 數量在原始與翻譯檔案間是否匹配。
- 執行 `co-op-review` 以捕捉常見結構問題。
- 若輸出被損壞，請重新翻譯該檔案。

```bash
co-op-review -l "ko" --format github
```

## GitHub Action 已執行但未建立 Pull Request

若 `peter-evans/create-pull-request` 回報該分支不領先於 base，表示工作流程未找到可提交的檔案。

可能原因：

- 翻譯執行未產生變更。
- `.gitignore` 忽略了 `translations/`、`translated_images/` 或已翻譯的筆記本。
- `add-paths` 與產生的輸出目錄不符。
- 翻譯步驟提早結束。

修正方法：

1. 確認在 `translations/` 或 `translated_images/` 中存在產生的檔案。
2. 確認 `.gitignore` 沒有忽略產生的輸出。
3. 使用相符的 `add-paths`：

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. 暫時在 translate 命令加入除錯旗標：

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

機器翻譯可能需要人工審查。僅在您需要實驗性品質評分與低信心修復工作流程時使用 `evaluate`。

!!! warning "實驗性"
    `evaluate` 可能使用基於規則與基於 LLM 的檢查，其評分模型與 metadata 行為可能會變動。除非您的工作流程已準備好應對變更，否則請勿將它納入必要的 CI gate。

對於具決定性的 CI 檢查，請改用 `co-op-review`。