# 疑難排解

當翻譯執行意外成功、在設定期間失敗或產生需要審查的輸出時，請使用此頁面。

## 從這裡開始

1. 先執行一個有針對性的命令，例如 `translate -l "ko" -md`。
2. 加入 `-d` 以取得主控台除錯日誌。
3. 加入 `-s` 將除錯日誌儲存在 `<root-dir>/logs/`。
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

修復方法：

- 設定 Azure OpenAI、OpenAI 或 Anthropic。
- 確認該變數存在於執行命令的環境中。
- For local usage, put them in `.env` at the project root.

請參閱 [設定](configuration.md)。

### 沒有 Azure AI Vision 的影像翻譯

錯誤：

```text
Image translation requested but Azure AI Service is not configured.
```

修復方法：

- Add `AZURE_AI_SERVICE_API_KEY`.
- Add `AZURE_AI_SERVICE_ENDPOINT`.
- Or run a text-only command such as `translate -l "ko" -md`.

### 無效的金鑰或端點

症狀可能包括 `401`、被遮蔽的權限錯誤，或端點存取錯誤。

修復方法：

- 確認金鑰屬於與端點相同的 Azure 資源。
- 確認該資源在使用 `-img` 時支援 Vision。
- 確認 Azure OpenAI 的部署名稱和 API 版本與你的部署相符。
- Run with debug logs: `translate -l "ko" -md -d -s`.

## 未翻譯任何檔案

常見原因：

- 選取的旗標與你的檔案不符。
- 已有已翻譯的檔案存在。
- 原始檔案位於被排除的目錄中。
- 此指令是在錯誤的專案根目錄中執行。

檢查：

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

當命令在專案根目錄外執行時，使用 `--root-dir`。

## 意外的連結行為

連結重寫取決於所選內容類型：

- `-nb` 已包含：筆記本連結可以指向已翻譯的筆記本。
- `-nb` 排除：筆記本連結可維持指向原始筆記本。
- `-img` 已包含：圖片連結可以指向已翻譯的圖片。
- `-img` 排除：圖片連結可維持指向原始圖片。

當所有內部連結應優先使用翻譯結果時，執行完整內容翻譯：

```bash
translate -l "ko" -md -nb -img
```

翻譯後執行連結審查：

```bash
co-op-review -l "ko"
```

## Markdown 呈現問題

如果翻譯後的 Markdown 呈現不正確：

- 檢查 frontmatter 是否以 `---` 開頭與結尾。
- 檢查程式碼圍欄（code fence）數量在來源與翻譯檔案間是否相符。
- 執行 `co-op-review` 以抓出常見結構問題。
- 若輸出被破壞，請重新翻譯該特定檔案。

```bash
co-op-review -l "ko" --format github
```

## GitHub Action 已執行但未建立 Pull Request

如果 `peter-evans/create-pull-request` 報告該分支未領先於 base，代表工作流程找不到可提交的檔案。

可能的原因：

- 翻譯執行未產生任何變更。
- `.gitignore` excludes `translations/`, `translated_images/`, or translated notebooks.
- `add-paths` 與產生的輸出目錄不符。
- The translation step exited early.

修正：

1. 確認在 `translations/` 或 `translated_images/` 中存在生成的檔案。
2. 確認 `.gitignore` 不會忽略生成的輸出。
3. Use matching `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. 暫時在 translate 命令中加入除錯旗標：

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

機器翻譯可能需要人工審查。僅在你需要實驗性質的品質評分和低信心修復工作流程時使用 `evaluate`。

!!! warning "Experimental"
    `evaluate` 可能會使用基於規則與基於 LLM 的檢查，其評分模型與 metadata 行為可能會改變。除非你的工作流程已準備好應對變動，否則不要將它放入必要的 CI 閘（gates）。

對於確定性的 CI 檢查，改為使用 `co-op-review`。