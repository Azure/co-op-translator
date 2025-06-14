<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-14T12:49:05+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "mo"
}
-->
# 指令參考
**Co-op Translator** CLI 提供多種選項來自訂翻譯過程：

指令                                       | 描述
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 將您的專案翻譯成指定語言。例如：translate -l "es fr de" 會翻譯成西班牙文、法文和德文。使用 translate -l "all" 來翻譯成所有支援的語言。
translate -l "language_codes" -u              | 更新翻譯，刪除現有的並重新創建。警告：這將刪除指定語言的所有現有翻譯。
translate -l "language_codes" -img            | 僅翻譯圖片文件。
translate -l "language_codes" -md             | 僅翻譯 Markdown 文件。
translate -l "language_codes" -chk            | 檢查翻譯文件中的錯誤，必要時重試翻譯。
translate -l "language_codes" -d              | 啟用除錯模式以獲取詳細日誌。
translate -l "language_codes" -r "root_dir"   | 指定專案的根目錄
translate -l "language_codes" -f              | 使用快速模式進行圖片翻譯（最多可快 3 倍，略微犧牲質量和對齊）。
translate -l "language_codes" -y              | 自動確認所有提示（對於 CI/CD 管線很有用）
translate -l "language_codes" --help          | CLI 內的幫助詳情，顯示可用指令

### 使用範例：

  1. 預設行為（新增翻譯而不刪除現有的）：   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 僅新增新的韓文圖片翻譯（不刪除現有翻譯）：    translate -l "ko" -img

  3. 更新所有韓文翻譯（警告：這會刪除所有現有韓文翻譯後重新翻譯）：    translate -l "ko" -u

  4. 僅更新韓文圖片（警告：這會刪除所有現有韓文圖片後重新翻譯）：    translate -l "ko" -img -u

  5. 新增韓文的 Markdown 翻譯而不影響其他翻譯：    translate -l "ko" -md

  6. 檢查翻譯文件中的錯誤，必要時重試翻譯： translate -l "ko" -chk

  7. 檢查翻譯文件中的錯誤，必要時重試翻譯（僅限 Markdown）： translate -l "ko" -chk -md

  8. 檢查翻譯文件中的錯誤，必要時重試翻譯（僅限圖片）： translate -l "ko" -chk -img

  9. 使用快速模式進行圖片翻譯：    translate -l "ko" -img -f

  10. 除錯模式範例： - translate -l "ko" -d: 啟用除錯日誌。

**免責聲明**：
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始語言的文件視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。對於因使用此翻譯而產生的任何誤解或誤釋，我們不承擔責任。