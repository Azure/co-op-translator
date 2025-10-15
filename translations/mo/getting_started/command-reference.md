<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T02:29:18+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "mo"
}
-->
# 指令參考

**Co-op Translator** CLI 提供多種選項，讓你可以自訂翻譯流程：

指令                                       | 說明
--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"               | 將你的專案翻譯成指定語言。例如：translate -l "es fr de" 會翻譯成西班牙語、法語和德語。使用 translate -l "all" 可翻譯成所有支援語言。
translate -l "language_codes" -u            | 更新翻譯，會刪除現有翻譯並重新建立。警告：這會刪除指定語言的所有現有翻譯。
translate -l "language_codes" -img          | 只翻譯圖片檔案。
translate -l "language_codes" -md           | 只翻譯 Markdown 檔案。
translate -l "language_codes" -nb           | 只翻譯 Jupyter notebook 檔案（.ipynb）。
translate -l "language_codes" --fix         | 根據先前評估結果，重新翻譯信心分數較低的檔案。
translate -l "language_codes" -d            | 啟用除錯模式，顯示詳細日誌。
translate -l "language_codes" --save-logs, -s | 將 DEBUG 級別日誌儲存到 <root_dir>/logs/（主控台日誌仍由 -d 控制）
translate -l "language_codes" -r "root_dir" | 指定專案根目錄
translate -l "language_codes" -f            | 圖片翻譯使用快速模式（繪圖速度提升最多 3 倍，但品質和對齊度略有損失）。
translate -l "language_codes" -y            | 自動確認所有提示（適合 CI/CD 流程）
translate -l "language_codes" --help        | CLI 內顯示可用指令的說明
evaluate -l "language_code"                 | 評估指定語言的翻譯品質並提供信心分數
evaluate -l "language_code" -c 0.8          | 以自訂信心門檻評估翻譯
evaluate -l "language_code" -f              | 快速評估模式（僅規則式，無 LLM）
evaluate -l "language_code" -D              | 深度評估模式（僅 LLM，較徹底但較慢）
evaluate -l "language_code" --save-logs, -s | 將 DEBUG 級別日誌儲存到 <root_dir>/logs/
migrate-links -l "language_codes"           | 重新處理已翻譯的 Markdown 檔案，更新 notebook（.ipynb）連結。若有翻譯版 notebook 優先使用，否則可回退到原始 notebook。
migrate-links -l "language_codes" -r        | 指定專案根目錄（預設：目前目錄）。
migrate-links -l "language_codes" --dry-run | 顯示哪些檔案會被更動，但不實際寫入。
migrate-links -l "language_codes" --no-fallback-to-original | 當缺少翻譯版 notebook 時，不會將連結改回原始 notebook（只在有翻譯時才更新）。
migrate-links -l "language_codes" -d        | 啟用除錯模式，顯示詳細日誌。
migrate-links -l "language_codes" --save-logs, -s | 將 DEBUG 級別日誌儲存到 <root_dir>/logs/
migrate-links -l "all" -y                   | 處理所有語言並自動確認警告提示。

## 使用範例

  1. 預設行為（新增翻譯，不刪除現有翻譯）：   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 只新增韓文圖片翻譯（不會刪除現有翻譯）：    translate -l "ko" -img

  3. 更新所有韓文翻譯（警告：這會先刪除所有現有韓文翻譯再重新翻譯）：    translate -l "ko" -u

  4. 只更新韓文圖片（警告：這會先刪除所有現有韓文圖片再重新翻譯）：    translate -l "ko" -img -u

  5. 只新增韓文 Markdown 翻譯，不影響其他翻譯：    translate -l "ko" -md

  6. 根據先前評估結果修正信心分數低的翻譯： translate -l "ko" --fix

  7. 只修正特定檔案的低信心翻譯（Markdown）： translate -l "ko" --fix -md

  8. 只修正特定檔案的低信心翻譯（圖片）： translate -l "ko" --fix -img

  9. 圖片翻譯使用快速模式：    translate -l "ko" -img -f

  10. 以自訂門檻修正低信心翻譯： translate -l "ko" --fix -c 0.8

  11. 除錯模式範例： - translate -l "ko" -d：啟用除錯日誌。
  12. 將日誌儲存到檔案： translate -l "ko" -s
  13. 主控台 DEBUG 與檔案 DEBUG： translate -l "ko" -d -s

  14. 為韓文翻譯遷移 notebook 連結（有翻譯 notebook 時更新連結）：    migrate-links -l "ko"

  15. 遷移連結但僅預覽（不寫入檔案）：    migrate-links -l "ko" --dry-run

  16. 只有在有翻譯 notebook 時才更新連結（不回退到原始檔）：    migrate-links -l "ko" --no-fallback-to-original

  17. 處理所有語言並顯示確認提示：    migrate-links -l "all"

  18. 處理所有語言並自動確認：    migrate-links -l "all" -y
  19. 將 migrate-links 日誌儲存到檔案：    migrate-links -l "ko ja" -s

### 評估範例

> [!WARNING]  
> **Beta 功能**：評估功能目前為測試版。此功能用於評估翻譯文件，評估方法與細節仍在開發中，未來可能會有變動。

  1. 評估韓文翻譯： evaluate -l "ko"

  2. 以自訂信心門檻評估： evaluate -l "ko" -c 0.8

  3. 快速評估（僅規則式）： evaluate -l "ko" -f

  4. 深度評估（僅 LLM）： evaluate -l "ko" -D

---

**免責聲明**：
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始語言的文件應視為最具權威的來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。