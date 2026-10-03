# 翻譯、編輯和審查一個小專案

從兩個短的 Markdown 檔案和一個目標語言開始。你會看到翻譯寫在哪裡、當原始檔案變更時會發生什麼，以及如何檢查結果。

## 已記錄的結果

此範例於 2026 年 9 月 19 日以 Co-op Translator 0.21.0 和 Azure OpenAI (`gpt-5-mini`) 執行。未修改的 CLI 指令透過 Click 的 `CliRunner` 以建置的 wheel 與現有的 Python 相依套件被呼叫。

| 步驟 | 結果 |
| --- | --- |
| 預覽 | 退出 0；未請求模型翻譯 |
| 初始翻譯 | 退出 0；27.36 秒 |
| 初始審閱 | 退出 0 |
| 編輯 README 並審閱 | 退出 1；偵測到過時的翻譯 |
| 更新翻譯 | 退出 0；22.17 秒 |
| 更新後審閱 | 退出 0；無錯誤或警告 |
| 未變更的指南 | 在 README 更新前後位元組相同 |
| 再次執行 | 退出 0；所有翻譯檔案的雜湊相同 |

這些是單次執行的測量值，並非效能保證。設定時間不包括在內；未測量供應者計費。即使在未變更的執行中，也可能會執行供應者健康檢查。

檢閱 [初始翻譯](../../assets/demo/before.txt)、[更新後的翻譯](../../assets/demo/after.txt)、[完整翻譯差異](../../assets/demo/update.diff)、[過時的審閱](../../assets/demo/review-stale.txt)、[最終審閱](../../assets/demo/review-after.txt)，以及 [執行詳細資訊](../../assets/demo/results.json)。完整檔案翻譯可能會改變其他措辭，如擷取的差異所示。兩個文字產物皆保留自動產生的免責聲明。

人工審閱仍然重要：擷取的更新使用 `[사용 가이드](guide.md)을`；正確的韓語格助詞應該是 `[사용 가이드](guide.md)를`。文字產物保留此輸出原樣，而不是將編輯過的翻譯當成模型輸出呈現。結構審閱雖然有措辭問題但仍通過。

## 1. 準備一個小資料夾

使用 Python 3.11–3.14 以及 [虛擬環境設定](configuration.md#local-runtime-setup)。安裝此範例所用的版本：

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

將 [README.txt](../../assets/demo/README.txt) 與 [guide.txt](../../assets/demo/guide.txt) 下載到此資料夾，並分別儲存為 `README.md` 與 `guide.md`。它們是小型虛構專案文件；不需安裝任何應用程式。

README 包含一個程式碼區塊和一個指向 `guide.md` 的連結。它的最後一句是：

```text
Notes are saved locally.
```

此資料夾僅保留這兩個原始文件。所有後續指令皆在 `translation-demo` 內執行，並可在 Bash 與 PowerShell 上運作。

## 2. 在無憑證下預覽

```bash
translate -l "ko" -md --dry-run
```

預覽會估算翻譯工作量，但不會呼叫模型或產生翻譯。代幣估算並非計費報價。第一次執行應會將兩個 Markdown 檔案標示為新的工作。

## 3. 選擇供應商並翻譯

使用[設定指南](configuration.md): Azure OpenAI、OpenAI，或 Anthropic。OpenAI 與 Anthropic 的文字翻譯不需要 Azure 帳戶。此範例不需要影像服務。

如果您使用本地的 `.env` 檔案，請將 `.env` 新增到此資料夾的 `.gitignore`。翻譯呼叫會使用您的供應商帳戶，並可能產生費用。

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

打開 `translations/ko/README.md` 和 `translations/ko/guide.md`。檢查韓文措辭、程式碼區塊，以及從已翻譯的 README 到已翻譯的指南的連結。輸出措辭會依模型而異。

`co-op-review` 會檢查是否為最新、結構，以及本地連結。通過的結果並不保證語言上的正確性。請在繼續之前解決任何被回報的錯誤。

使用 Git 記錄成功的基準（如需要，先設定您的 Git 身份）:

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. 更改來源

In `README.md`, replace `Notes are saved locally.` with:

```text
Notes are saved locally as Markdown files.
```

Leave `guide.md` unchanged. Then run:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

審查應該回報 README 的翻譯為過時並以失敗狀態退出。這是預期的中間狀態。預覽應該會指出針對已變更 README 的工作項目。

## 5. 更新並檢查差異

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

檢視實際的差異：預設的 CLI 會重新翻譯已變更的檔案，因此模型也可能修正該檔案中其他措辭。未變更的指南應該不會有差異。審查應該不再回報 README 為過時；對於任何其他發現請進行調查，而不是忽略它們。

要在區塊層級保留人工的 Markdown 編輯，需在 [Python API](api.md) 中提供一個可選的翻譯狀態提供器。這些 CLI 指令並未啟用它。

## 6. 再次執行（不作任何變更）

提交已更新的原始檔和翻譯：

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

在目前的翻譯與未更改的設定下，翻譯器會跳過這些檔案。最後的 Git 指令不應產生任何 diff，並且應成功退出。

## 後續步驟

- [只翻譯 README 並開啟一個 pull request](github-actions.md#your-first-readme-translation-pr).
- [Choose CLI, Python API, or MCP](workflows.md).
- [回報翻譯問題（不需撰寫程式）](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).
