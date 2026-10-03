# 翻譯、編輯及審閱一個小型專案

從兩個簡短的 Markdown 檔案和一個目標語言開始。你會看到翻譯會寫在哪裡、原始檔案變更時會發生什麼，以及如何檢查結果。

## 記錄的結果

此範例於 2026 年 9 月 19 日使用 Co-op Translator 0.21.0 和 Azure OpenAI (`gpt-5-mini`) 執行。未修改的 CLI 命令透過 Click 的 `CliRunner` 使用已建置的 wheel 與現有的 Python 相依項目來呼叫。

| 步驟 | 結果 |
| --- | --- |
| 預覽 | 退出 0；沒有要求模型翻譯 |
| 初始翻譯 | 退出 0；27.36 秒 |
| 初始審查 | 退出 0 |
| 編輯 README 並審查 | 退出 1；偵測到翻譯已過時 |
| 更新翻譯 | 退出 0；22.17 秒 |
| 更新後審查 | 退出 0；無錯誤或警告 |
| 未變更的 guide | 在 README 更新前後位元相同 |
| 再次執行 | 退出 0；所有翻譯檔案的雜湊相同 |

這些是單次執行的測量值，並非效能保證。設定時間未計入；未測量供應商計費。即使沒有變更，執行仍可能進行供應商健康檢查。

檢視 [初始翻譯](../../assets/demo/before.txt)、[更新後翻譯](../../assets/demo/after.txt)、[完整翻譯差異](../../assets/demo/update.diff)、[過時的審查](../../assets/demo/review-stale.txt)、[最終審查](../../assets/demo/review-after.txt)，以及[執行詳細資訊](../../assets/demo/results.json)。整個檔案的翻譯可能會改變其他措辭，如擷取的差異所示。兩個文字檔都保留了自動產生的免責聲明。

人工審查仍然很重要：擷取到的更新使用了 `[사용 가이드](guide.md)을`；但正確的韓文助詞應該是 `[사용 가이드](guide.md)를`。文字檔案保留了此輸出原狀，而不是將經編輯的翻譯視為模型輸出。結構審查雖然通過，但仍有此措辭問題。

## 1. 準備一個小資料夾

使用 Python 3.11–3.14 與 [虛擬環境設定](configuration.md#local-runtime-setup)。安裝本範例所使用的版本：

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

將 [README.txt](../../assets/demo/README.txt) 和 [guide.txt](../../assets/demo/guide.txt) 下載到此資料夾，並儲存為 `README.md` 與 `guide.md`。它們是小型的虛構專案文件；不需要安裝任何應用程式。

README 包含一個程式碼區塊以及連結到 `guide.md`。其最後一句是：

```text
Notes are saved locally.
```

此資料夾內只保留這兩個原始文件。以下所有命令皆在 `translation-demo` 內執行，並可在 Bash 及 PowerShell 上運行。

## 2. 在沒有憑證下預覽

```bash
translate -l "ko" -md --dry-run
```

預覽會估算翻譯工作量，但不會呼叫模型或寫入翻譯。token 估算並非計費報價。第一次執行應該會將兩個 Markdown 檔案標示為新的工作。

## 3. 選擇一個供應商並進行翻譯

依據 [設定指南](configuration.md) 設定一個供應商：Azure OpenAI、OpenAI，或 Anthropic。OpenAI 與 Anthropic 的文字翻譯不需要 Azure 帳戶。此範例不需要影像服務。

如果你使用本機的 `.env` 檔案，請將 `.env` 新增到此資料夾的 `.gitignore`。翻譯呼叫會使用你的供應商帳戶，可能會產生費用。

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

打開 `translations/ko/README.md` 與 `translations/ko/guide.md`。檢查韓文措辭、程式碼區塊，以及從翻譯後的 README 到翻譯後 guide 的連結。輸出措辭會依模型而異。

`co-op-review` 會檢查新鮮度、結構和本地連結。通過的結果並不代表語言準確性。請在繼續之前解決任何報告的錯誤。

使用 Git 記錄成功的基準（如有需要，請先設定你的 Git 身份）：

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. 更改原始檔

在 `README.md` 中，將 `Notes are saved locally.` 替換為：

```text
Notes are saved locally as Markdown files.
```

保持 `guide.md` 不變。然後執行：

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

審查應回報 README 的翻譯為已過時並以失敗狀態退出。這是預期的中間狀態。預覽應該會將變更過的 README 標示為需處理的工作。

## 5. 更新並檢視差異

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

檢查真正的差異：預設的 CLI 會重新翻譯已變更的檔案，因此模型也可能修訂該檔案中的其他用詞。未變更的 guide 應該沒有差異。審查不應再回報 README 為已過時；對任何其他發現務必調查，不要忽略。

要在區塊層級保留人類的 Markdown 編輯，需在 [Python API](api.md) 中使用可選的翻譯狀態提供者。這些 CLI 命令並未啟用此功能。

## 6. 在未變更下再次執行

提交已更新的原始檔與翻譯：

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

在現有翻譯與未變更的設定下，翻譯程式會跳過這些檔案。最終的 Git 命令應該不會產生差異並成功退出。

## 下一步

- [只翻譯 README 並開啟一個拉取請求](github-actions.md#your-first-readme-translation-pr).
- [選擇 CLI、Python API 或 MCP](workflows.md).
- [在不撰寫程式碼下回報翻譯問題](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).