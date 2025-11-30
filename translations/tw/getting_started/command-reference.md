<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T10:22:01+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "tw"
}
-->
# 指令參考

**Co-op Translator** CLI 提供多種選項來自訂翻譯流程：

指令                                         | 說明
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 將專案翻譯成指定語言。例如：translate -l "es fr de" 會翻譯成西班牙語、法語和德語。使用 translate -l "all" 可翻譯成所有支援語言。
translate -l "language_codes" -u              | 更新翻譯，會刪除現有翻譯並重新建立。警告：這會刪除指定語言的所有現有翻譯。
translate -l "language_codes" -img            | 僅翻譯圖片檔案。
translate -l "language_codes" -md             | 僅翻譯 Markdown 檔案。
translate -l "language_codes" -nb             | 僅翻譯 Jupyter 筆記本檔案（.ipynb）。
translate -l "language_codes" --fix           | 根據先前評估結果，重新翻譯信心度較低的檔案。
translate -l "language_codes" -d              | 啟用除錯模式，提供詳細日誌。
translate -l "language_codes" --save-logs, -s | 將 DEBUG 級別日誌儲存至 <root_dir>/logs/ 目錄（控制台仍受 -d 控制）
translate -l "language_codes" -r "root_dir"   | 指定專案根目錄
translate -l "language_codes" -f              | 使用快速模式翻譯圖片（繪圖速度最高可快 3 倍，但品質與對齊略有影響）。
translate -l "language_codes" -y              | 自動確認所有提示（適用於 CI/CD 流程）
translate -l "language_codes" --add-disclaimer/--no-disclaimer | 啟用或停用在翻譯的 Markdown 和筆記本中加入機器翻譯免責聲明區塊（預設：啟用）。
translate -l "language_codes" --help          | 顯示 CLI 內的幫助細節與可用指令
evaluate -l "language_code"                  | 評估特定語言的翻譯品質並提供信心分數
evaluate -l "language_code" -c 0.8           | 使用自訂信心門檻評估翻譯
evaluate -l "language_code" -f               | 快速評估模式（僅規則基礎，無 LLM）
evaluate -l "language_code" -D               | 深度評估模式（僅 LLM，較詳盡但較慢）
evaluate -l "language_code" --save-logs, -s  | 將 DEBUG 級別日誌儲存至 <root_dir>/logs/
migrate-links -l "language_codes"             | 重新處理翻譯後的 Markdown 檔案，更新筆記本（.ipynb）連結。優先使用翻譯後的筆記本，若無則可回退至原始筆記本。
migrate-links -l "language_codes" -r          | 指定專案根目錄（預設為目前目錄）。
migrate-links -l "language_codes" --dry-run   | 顯示將會變更的檔案，但不寫入變更。
migrate-links -l "language_codes" --no-fallback-to-original | 當翻譯筆記本不存在時，不改寫連結至原始筆記本（僅在翻譯筆記本存在時更新連結）。
migrate-links -l "language_codes" -d          | 啟用除錯模式，提供詳細日誌。
migrate-links -l "language_codes" --save-logs, -s | 將 DEBUG 級別日誌儲存至 <root_dir>/logs/
migrate-links -l "all" -y                      | 處理所有語言並自動確認警告提示。

## 使用範例

  1. 預設行為（新增翻譯，不刪除現有翻譯）：   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 僅新增韓文圖片翻譯（不刪除現有翻譯）：    translate -l "ko" -img

  3. 更新所有韓文翻譯（警告：會先刪除所有現有韓文翻譯再重新翻譯）：    translate -l "ko" -u

  4. 僅更新韓文圖片（警告：會先刪除所有現有韓文圖片再重新翻譯）：    translate -l "ko" -img -u

  5. 僅新增韓文 Markdown 翻譯，不影響其他翻譯：    translate -l "ko" -md

  6. 根據先前評估結果修正信心度低的翻譯： translate -l "ko" --fix

  7. 僅修正特定檔案的信心度低翻譯（Markdown）： translate -l "ko" --fix -md

  8. 僅修正特定檔案的信心度低翻譯（圖片）： translate -l "ko" --fix -img

  9. 使用快速模式翻譯圖片：    translate -l "ko" -img -f

  10. 使用自訂門檻修正信心度低的翻譯： translate -l "ko" --fix -c 0.8

  11. 除錯模式範例： - translate -l "ko" -d：啟用除錯日誌。
  12. 將日誌儲存至檔案： translate -l "ko" -s
  13. 控制台與檔案皆為 DEBUG 級別： translate -l "ko" -d -s
  14. 翻譯時不加入機器翻譯免責聲明： translate -l "ko" --no-disclaimer

  15. 為韓文翻譯遷移筆記本連結（有翻譯筆記本時更新連結）：    migrate-links -l "ko"

  15. 以 dry-run 模式遷移連結（不寫入檔案）：    migrate-links -l "ko" --dry-run

  16. 僅在翻譯筆記本存在時更新連結（不回退至原始筆記本）：    migrate-links -l "ko" --no-fallback-to-original

  17. 處理所有語言並顯示確認提示：    migrate-links -l "all"

  18. 處理所有語言並自動確認：    migrate-links -l "all" -y
  19. 為 migrate-links 儲存日誌至檔案：    migrate-links -l "ko ja" -s

### 評估範例

> [!WARNING]  
> **Beta 功能**：評估功能目前仍處於測試階段。此功能用於評估翻譯文件，評估方法與詳細實作仍在開發中，未來可能會有所變動。

  1. 評估韓文翻譯： evaluate -l "ko"

  2. 使用自訂信心門檻評估： evaluate -l "ko" -c 0.8

  3. 快速評估（僅規則基礎）： evaluate -l "ko" -f

  4. 深度評估（僅 LLM）： evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->