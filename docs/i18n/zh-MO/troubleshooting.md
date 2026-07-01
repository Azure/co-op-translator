# 疑難排解

當翻譯執行意外成功、在設定期間失敗，或產生需要審閱的輸出時，請使用此頁面。

## 從這裡開始

1. 先執行一個焦點命令，例如 `translate -l "ko" -md`。
2. 加上 `-d` 以獲得主控台除錯日誌。
3. 加上 `-s` 以將除錯日誌儲存在 `<root-dir>/logs/` 下。
4. 翻譯後執行 `co-op-review` 以檢查新鮮度、結構與本地連結。

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
- 驗證那些變數在執行命令的環境中是否存在。
- 若在本機使用，請將它們放在專案根目錄的 `.env`。

請參閱 [設定](configuration.md)。

### 在沒有 Azure AI Vision 的情況下進行圖像翻譯

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

- 確認該金鑰屬於與端點相同的 Azure 資源。
- 在使用 `-img` 時，確認該資源支援 Vision。
- 確認 Azure OpenAI 的部署名稱與 API 版本與你的部署相符。
- 使用除錯日誌執行：`translate -l "ko" -md -d -s`。

## 沒有檔案被翻譯

常見原因：

- 選取的旗標不符合你的檔案。
- 已存在已翻譯的檔案。
- 來源檔案位於被排除的目錄中。
- 命令在錯誤的專案根目錄下執行。

檢查：

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

當命令在專案根目錄外執行時，請使用 `--root-dir`。

## 連結行為異常

連結重寫取決於所選的內容類型：

- `-nb` included: 筆記本連結可以指向已翻譯的筆記本。
- `-nb` excluded: 筆記本連結可以保持指向原始筆記本。
- `-img` included: 圖片連結可以指向已翻譯的圖片。
- `-img` excluded: 圖片連結可以保持指向原始圖片。

當所有內部連結都應優先指向翻譯輸出時，執行完整內容翻譯：

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
- 檢查程式碼區塊的 fence 標記數量在來源與翻譯檔案間是否一致。
- 執行 `co-op-review` 以捕捉常見的結構問題。
- 如果輸出已損毀，請重新翻譯該特定檔案。

```bash
co-op-review -l "ko" --format github
```

## GitHub Action 已執行但未建立 Pull Request

如果 `peter-evans/create-pull-request` 報告分支並未領先於 base，表示工作流程沒有找到可提交的檔案。

可能原因：

- 翻譯執行未產生任何變更。
- `.gitignore` 排除了 `translations/`、`translated_images/` 或已翻譯的筆記本。
- `add-paths` 與產生的輸出目錄不符。
- 翻譯步驟提早結束。

解決方法：

1. 確認已在 `translations/` 或 `translated_images/` 中產生檔案。
2. 確認 `.gitignore` 未忽略產生的輸出。
3. 使用相符的 `add-paths`：

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. 臨時在 translate 指令加入除錯旗標：

   ```bash
   translate -l "ko" -md -d -s
   ```

5. 確認工作流程的權限包含：

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## 翻譯品質

機器翻譯可能需要人工審閱。只有在您想要實驗性品質評分與低信心修復工作流程時才使用 `evaluate`。

!!! warning "Experimental"
    `evaluate` can use rule-based and LLM-based checks, and its scoring model and metadata behavior may change. Keep it out of required CI gates unless your workflow is prepared for changes.

對於具決定性的 CI 檢查，請改用 `co-op-review`。