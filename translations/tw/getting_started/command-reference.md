<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:25:09+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "tw"
}
-->
# Command reference
**Co-op Translator** CLI 提供多種選項來客製化翻譯流程：

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 將你的專案翻譯成指定的語言。例如：translate -l "es fr de" 會翻譯成西班牙語、法語和德語。使用 translate -l "all" 可以翻譯成所有支援的語言。
translate -l "language_codes" -u              | 更新翻譯，會刪除現有翻譯並重新建立。警告：這會刪除指定語言的所有現有翻譯。
translate -l "language_codes" -img            | 僅翻譯圖片檔案。
translate -l "language_codes" -md             | 僅翻譯 Markdown 檔案。
translate -l "language_codes" -chk            | 檢查翻譯檔案是否有錯誤，並在需要時重試翻譯。
translate -l "language_codes" -d              | 啟用除錯模式以取得詳細日誌。
translate -l "language_codes" -r "root_dir"   | 指定專案的根目錄。
translate -l "language_codes" -f              | 使用快速模式翻譯圖片（繪製速度最高可快 3 倍，但畫質和對齊會稍微受影響）。
translate -l "language_codes" -y              | 自動確認所有提示（適合 CI/CD 流程）。
translate -l "language_codes" --help          | CLI 內的說明細節，顯示可用指令。

### Usage examples:

  1. 預設行為（新增翻譯而不刪除現有翻譯）：   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 僅新增韓文圖片翻譯（不刪除現有翻譯）：    translate -l "ko" -img

  3. 更新所有韓文翻譯（警告：這會先刪除所有現有韓文翻譯再重新翻譯）：    translate -l "ko" -u

  4. 僅更新韓文圖片（警告：這會先刪除所有現有韓文圖片再重新翻譯）：    translate -l "ko" -img -u

  5. 新增韓文 Markdown 翻譯，不影響其他翻譯：    translate -l "ko" -md

  6. 檢查翻譯檔案錯誤並在需要時重試翻譯： translate -l "ko" -chk

  7. 檢查翻譯檔案錯誤並重試翻譯（僅限 Markdown）： translate -l "ko" -chk -md

  8. 檢查翻譯檔案錯誤並重試翻譯（僅限圖片）： translate -l "ko" -chk -img

  9. 使用快速模式翻譯圖片：    translate -l "ko" -img -f

  10. 除錯模式範例： - translate -l "ko" -d：啟用除錯日誌。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們努力確保翻譯的準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生之任何誤解或誤釋負責。