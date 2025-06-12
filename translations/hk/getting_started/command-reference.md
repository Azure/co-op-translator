<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:24:56+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "hk"
}
-->
# Command reference
**Co-op Translator** CLI 提供多種選項來自訂翻譯流程：

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 將你的專案翻譯成指定語言。例如：translate -l "es fr de" 會翻譯成西班牙語、法語和德語。使用 translate -l "all" 可翻譯成所有支援語言。
translate -l "language_codes" -u              | 更新翻譯，會先刪除現有翻譯再重新建立。警告：這會刪除指定語言的所有現有翻譯。
translate -l "language_codes" -img            | 只翻譯圖片檔案。
translate -l "language_codes" -md             | 只翻譯 Markdown 檔案。
translate -l "language_codes" -chk            | 檢查翻譯檔案是否有錯誤，必要時重新嘗試翻譯。
translate -l "language_codes" -d              | 啟用除錯模式，提供詳細記錄。
translate -l "language_codes" -r "root_dir"   | 指定專案的根目錄。
translate -l "language_codes" -f              | 使用快速模式翻譯圖片（繪圖速度可提升最多 3 倍，但品質和對齊會稍微受影響）。
translate -l "language_codes" -y              | 自動確認所有提示（適用於 CI/CD 流程）。
translate -l "language_codes" --help          | 顯示 CLI 內的說明和可用指令。

### Usage examples:

  1. 預設行為（新增翻譯但不刪除現有翻譯）：   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 只新增韓文圖片翻譯（不刪除現有翻譯）：    translate -l "ko" -img

  3. 更新所有韓文翻譯（警告：會先刪除所有現有韓文翻譯再重新翻譯）：    translate -l "ko" -u

  4. 只更新韓文圖片（警告：會先刪除所有現有韓文圖片再重新翻譯）：    translate -l "ko" -img -u

  5. 新增韓文 Markdown 翻譯，不影響其他翻譯：    translate -l "ko" -md

  6. 檢查翻譯檔案錯誤，必要時重試翻譯： translate -l "ko" -chk

  7. 檢查翻譯檔案錯誤並重試（只限 Markdown）： translate -l "ko" -chk -md

  8. 檢查翻譯檔案錯誤並重試（只限圖片）： translate -l "ko" -chk -img

  9. 使用快速模式翻譯圖片：    translate -l "ko" -img -f

  10. 除錯模式範例： - translate -l "ko" -d：啟用除錯記錄。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原文文件嘅母語版本應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我哋對因使用此翻譯而引致嘅任何誤解或誤釋概不負責。