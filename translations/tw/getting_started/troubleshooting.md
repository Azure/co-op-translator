<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-05-06T17:50:01+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "tw"
}
-->
# Microsoft Co-op Translator 疑難排解指南


## 概覽
Microsoft Co-Op Translator 是一個強大的工具，可以順利翻譯 Markdown 文件。本指南將協助你解決使用該工具時常見的問題。

## 常見問題與解決方案

### 1. Markdown 標籤問題
**問題：** 翻譯後的 Markdown 文件頂部出現 `markdown` 標籤，導致渲染異常。

**解決方案：** 請刪除文件頂部的 `markdown` 標籤，即可讓 Markdown 文件正確渲染。

**步驟：**
1. 開啟翻譯後的 Markdown (`.md`) 文件。
2. 找到文件頂部的 `markdown` 標籤。
3. 刪除 `markdown` 標籤。
4. 儲存檔案修改。
5. 重新開啟檔案，確認渲染正常。

### 2. 內嵌圖片 URL 問題
**問題：** 內嵌圖片的 URL 與語言區域不符，導致圖片顯示錯誤或遺失。

**解決方案：** 檢查內嵌圖片的 URL，確保其語言區域標籤與文件語言一致。所有圖片都放在 `translated_images` 資料夾，每張圖片檔名中都有語言區域標籤。

**步驟：**
1. 開啟翻譯後的 Markdown 文件。
2. 找出內嵌圖片及其 URL。
3. 確認圖片檔名中的語言區域標籤與文件語言相符。
4. 如有需要，更新 URL。
5. 儲存修改並重新開啟文件，確認圖片正常顯示。

### 3. 翻譯準確度
**問題：** 翻譯內容不夠準確，或需要進一步編輯。

**解決方案：** 仔細檢視翻譯文件，並做必要的修改以提升準確度與可讀性。

**步驟：**
1. 開啟翻譯文件。
2. 細心檢查內容。
3. 進行必要的修正以提升翻譯品質。
4. 儲存修改。

### 4. 檔案格式問題
**問題：** 翻譯文件格式錯誤，例如表格格式異常。這裡可以使用額外的 ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` 來解決表格問題。

**步驟：**
1. 開啟翻譯文件。
2. 與原始文件比對，找出格式問題。
3. 調整格式，使其與原始文件一致。
4. 儲存修改。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生的任何誤解或誤釋負責。