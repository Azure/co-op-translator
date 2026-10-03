# 翻譯、編輯與審核一個小專案

從兩個短的 Markdown 檔案和一種目標語言開始。你將看到翻譯會寫到哪裡、原始檔案變更時會發生什麼，還有如何檢查結果。

## 記錄的結果

此範例於 2026 年 9 月 19 日使用 Co-op Translator 0.21.0 與 Azure OpenAI (`gpt-5-mini`) 執行。未修改的 CLI 命令透過 Click 的 `CliRunner` 使用已建立的 wheel 與現有的 Python 相依套件來調用。

| 步驟 | 結果 |
| --- | --- |
| 預覽 | Exit 0; 未請求模型翻譯 |
| 初始翻譯 | Exit 0; 27.36 秒 |
| 初始審查 | Exit 0 |
| 編輯 README 並審查 | Exit 1; 偵測到過時的翻譯 |
| 更新翻譯 | Exit 0; 22.17 秒 |
| 更新後審查 | Exit 0; 沒有錯誤或警告 |
| 未變更的指南 | README 更新前後位元組相同 |
| 再次執行 | Exit 0; 所有翻譯檔案的雜湊值相同 |

這些是單次執行的測量值，非效能保證。設定時間不計；未衡量供應商計費。即使未變更的執行仍可能執行供應商健康檢查。

檢視 [初始翻譯](../../assets/demo/before.txt)、[更新後翻譯](../../assets/demo/after.txt)、[完整翻譯差異](../../assets/demo/update.diff)、[過時的審查](../../assets/demo/review-stale.txt)、[最終審查](../../assets/demo/review-after.txt) 與 [執行細節](../../assets/demo/results.json)。整檔翻譯可能會改變其他措辭，如擷取的差異所示。兩個文字產物都保留了產生的免責聲明。

人工審查仍然重要：擷取的更新使用了 `[사용 가이드](guide.md)을`；正確的韓語助詞應為 `[사용 가이드](guide.md)를`。文字產物保留了這個輸出內容，而不是將經過編輯的翻譯作為模型輸出呈現。儘管有這個措辭問題，結構性審查仍然通過。

## 1. 準備一個小資料夾

使用 Python 3.11–3.14 與 [虛擬環境設定](configuration.md#local-runtime-setup)。安裝本範例使用的版本：

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

下載 [README.txt](../../assets/demo/README.txt) 與 [guide.txt](../../assets/demo/guide.txt) 到此資料夾，並將它們儲存為 `README.md` 與 `guide.md`。它們是小型虛構專案文件；不需要安裝應用程式。

README 包含一個程式碼區塊與指向 `guide.md` 的連結。其最後一句是：

```text
Notes are saved locally.
```

在此資料夾中僅保留這兩個原始文件。後續所有命令皆在 `translation-demo` 中執行，且在 Bash 與 PowerShell 中可運作。

## 2. 在沒有憑證下預覽

```bash
translate -l "ko" -md --dry-run
```

預覽會估算翻譯工作量，但不會呼叫模型或寫入翻譯。標記（token）估算不是計費報價。第一次執行應該會將兩個 Markdown 檔案識別為新的工作。

## 3. 選擇供應商並翻譯

依照 [設定指南](configuration.md) 設定一個供應商：Azure OpenAI、OpenAI 或 Anthropic。OpenAI 與 Anthropic 的文字翻譯不需要 Azure 帳戶。本範例不需要影像服務。

如果你使用本機 `.env` 檔案，請將 `.env` 加入此資料夾的 `.gitignore`。翻譯呼叫會使用你的供應商帳戶，可能會產生費用。

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

打開 `translations/ko/README.md` 與 `translations/ko/guide.md`。檢查韓語措辭、程式碼區塊，以及從翻譯後 README 到翻譯後 guide 的連結。輸出措辭會因模型而異。

`co-op-review` 會檢查新鮮度、結構與本地連結。通過的結果並不保證語言上的正確性。在繼續之前請解決任何報告的錯誤。

使用 Git 記錄成功的基線（如有需要請先設定你的 Git 身份）：

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. 變更來源

在 `README.md` 中，將 `Notes are saved locally.` 替換為：

```text
Notes are saved locally as Markdown files.
```

保留 `guide.md` 不變。然後執行：

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

審查應該會報告 README 的翻譯為過時並以不成功狀態退出。這是預期的中間狀態。預覽應該會識別出已變更 README 的工作。

## 5. 更新並檢查差異

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

檢查實際差異：預設的 CLI 會重新翻譯被更改的檔案，因此模型也可能修訂該檔案中的其他措辭。未變更的 guide 應該沒有差異。審查不應再報告 README 為過時；請調查任何其他發現，而不是忽略它們。

要在區塊層級保留人工的 Markdown 編輯，需在 [Python API](api.md) 中使用可選的翻譯狀態提供者。這些 CLI 命令未啟用該功能。

## 6. 在未變更情況下再次執行

提交更新後的原始檔與翻譯：

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

在目前的翻譯與未變更的設定下，翻譯器會跳過這些檔案。最後的 Git 命令應該不會產生差異並成功退出。

## 下一步

- [只翻譯 README 並開啟 pull request](github-actions.md#your-first-readme-translation-pr).
- [選擇 CLI、Python API，或 MCP](workflows.md).
- [在不撰寫程式的情況下回報翻譯問題](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).