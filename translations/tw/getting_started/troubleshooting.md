<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:23:51+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "tw"
}
-->
# Microsoft Co-op Translator 疑難排解指南

## 概覽
Microsoft Co-Op Translator 是一個強大的工具，能夠順暢地翻譯 Markdown 文件。本指南將協助你排解使用此工具時常見的問題。

## 常見問題與解決方案

### 1. Markdown 標籤問題
**問題：** 翻譯後的 Markdown 文件頂端出現 `markdown` 標籤，導致顯示異常。

**解決方案：** 請刪除文件頂端的 `markdown` 標籤，即可讓 Markdown 文件正確呈現。

**步驟：**
1. 開啟翻譯後的 Markdown (`.md`) 文件。
2. 找到文件頂端的 `markdown` 標籤。
3. 刪除 `markdown` 標籤。
4. 儲存檔案。
5. 重新開啟檔案，確認顯示正常。

### 2. 內嵌圖片 URL 問題
**問題：** 內嵌圖片的 URL 與語言區域不符，導致圖片顯示錯誤或遺失。

**解決方案：** 檢查內嵌圖片的 URL，確保與語言區域相符。所有圖片都放在 `translated_images` 資料夾中，每張圖片檔名都包含語言區域標籤。

**步驟：**
1. 開啟翻譯後的 Markdown 文件。
2. 找出內嵌圖片及其 URL。
3. 確認圖片檔名中的語言區域是否與文件語言一致。
4. 如有需要，更新 URL。
5. 儲存並重新開啟文件，確認圖片正確顯示。

### 3. 翻譯準確度
**問題：** 翻譯內容不夠準確或需要進一步編輯。

**解決方案：** 仔細檢查翻譯文件，並進行必要的修改，以提升準確度與可讀性。

**步驟：**
1. 開啟翻譯後的文件。
2. 仔細審閱內容。
3. 進行必要的修改以提升翻譯品質。
4. 儲存變更。

### 4. 文件格式問題
**問題：** 翻譯文件的格式不正確，表格部分可能有問題，這裡的額外 ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` 會解決表格的問題。

**步驟：**
1. 開啟翻譯後的文件。
2. 與原始文件比對，找出格式問題。
3. 調整格式，使其符合原始文件。
4. 儲存變更。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生之任何誤解或誤釋負責。