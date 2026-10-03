# 疑難排解

當翻譯執行意外成功、在配置過程中失敗，或產生需要審查的輸出時，請使用此頁面。

## 從這裡開始

1. 先執行一個有針對性的命令，例如 `translate -l "ko" -md`。
2. 加上 `-d` 以輸出控制台除錯日誌。
3. 加上 `-s` 將除錯日誌儲存在 `<root-dir>/logs/`。
4. 在翻譯後執行 `co-op-review` 以檢查是否為最新、結構與本地連結。

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

- 設定 Azure OpenAI、OpenAI 或 Anthropic。
- 確認變數存在於執行命令的環境中。
- 若在本機使用，請將它們放在專案根目錄的 `.env`。

請參閱 [設定](configuration.md)。

### 未使用 Azure AI Vision 的影像翻譯

錯誤：

```text
Image translation requested but Azure AI Service is not configured.
```

解決方法：

- 新增 `AZURE_AI_SERVICE_API_KEY`。
- 新增 `AZURE_AI_SERVICE_ENDPOINT`。
- 或執行僅文字的命令，例如 `translate -l "ko" -md`。

### 金鑰或端點無效

徵狀可能包括 `401`、被遮蔽的權限錯誤或端點存取錯誤。

解決方法：

- 確認該金鑰屬於與端點相同的 Azure 資源。
- 在使用 `-img` 時確認該資源支援 Vision。
- 確認 Azure OpenAI 的部署名稱與 API 版本與你的部署相符。
- 使用除錯日誌執行：`translate -l "ko" -md -d -s`。

## 沒有檔案被翻譯

常見原因：

- 選取的旗標與你的檔案不符合。
- 已存在已翻譯的檔案。
- 原始檔案位於被排除的目錄中。
- 命令是在錯誤的專案根目錄執行。

檢查：

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

當命令在專案根目錄外執行時，使用 `--root-dir`。

## 意外的連結行為

連結重寫取決於所選的內容類型：

- `-nb` 包含：筆記本連結可以指向已翻譯的筆記本。
- `-nb` 未包含：筆記本連結可以維持指向原始筆記本。
- `-img` 包含：影像連結可以指向已翻譯的影像。
- `-img` 未包含：影像連結可以維持指向原始影像。

當所有內部連結都應偏好已翻譯的輸出時，執行完整內容翻譯：

```bash
translate -l "ko" -md -nb -img
```

在翻譯後執行連結審查：

```bash
co-op-review -l "ko"
```

## Markdown 呈現問題

如果翻譯後的 Markdown 呈現不正確：

- 檢查 frontmatter 是否以 `---` 開頭及結尾。
- 檢查原始與翻譯檔案之間的程式碼區塊（code fence）數量是否相符。
- 執行 `co-op-review` 以抓出常見的結構問題。
- 若輸出已損壞，請重新翻譯該特定檔案。

```bash
co-op-review -l "ko" --format github
```

## GitHub Action 已執行但未建立 Pull Request

如果 `peter-evans/create-pull-request` 報告該分支沒有超前基底，表示工作流程找不到要提交的檔案。

可能原因：

- 翻譯執行未產生變更。
- `.gitignore` 忽略了 `translations/`、`translated_images/` 或已翻譯的筆記本。
- `add-paths` 與產生的輸出目錄不匹配。
- 翻譯步驟提早結束。

解決方法：

1. 確認 `translations/` 或 `translated_images/` 中存在產生的檔案。
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

## 翻譯質量

機器翻譯可能需要人工審核。只有在需要實驗性質的質量評分和低信心修復工作流程時才使用 `evaluate`。

!!! warning "實驗性"
    `evaluate` 可能使用基於規則及基於 LLM 的檢查，其評分模型與元資料行為可能會變更。除非你的工作流程已準備好應對變更，否則不要將其納入必要的 CI 閘道。

對於具決定性的 CI 檢查，請改用 `co-op-review`。