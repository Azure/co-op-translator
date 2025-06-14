<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-14T12:50:03+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "mo"
}
-->
# Microsoft Co-op Translator 疑難排解指南

## 概述
Microsoft Co-Op Translator 是一款強大的工具，可以無縫翻譯 Markdown 文件。本指南將幫助您解決使用此工具時遇到的常見問題。

## 常見問題及解決方案

### 1. Markdown 標籤問題
**問題：** 翻譯後的 Markdown 文件在頂部包含 `markdown` 標籤，導致渲染問題。

**解決方案：** 要解決此問題，只需刪除文件頂部的 `markdown` 標籤。這將使 Markdown 文件能夠正確渲染。

**步驟：**
1. 打開翻譯後的 Markdown (`.md`) 文件。
2. 找到文件頂部的 `markdown` 標籤。
3. 刪除 `markdown` 標籤。
4. 保存文件的更改。
5. 重新打開文件以確保其正確渲染。

### 2. 嵌入圖片 URL 問題
**問題：** 嵌入圖片的 URL 與語言地區不匹配，導致圖片不正確或缺失。

**解決方案：** 檢查嵌入圖片的 URL，確保它們與語言地區相匹配。所有圖片都位於 `translated_images` 文件夾中，每個圖片的文件名中都有語言地區標籤。

**步驟：**
1. 打開翻譯後的 Markdown 文件。
2. 確認嵌入圖片及其 URL。
3. 驗證圖片文件名中的語言地區是否與文件的語言匹配。
4. 如有必要，更新 URL。
5. 保存更改並重新打開文件以確認圖片正確渲染。

### 3. 翻譯準確性
**問題：** 翻譯內容不準確或需要進一步編輯。

**解決方案：** 查看翻譯文件並進行必要的編輯以提高準確性和可讀性。

**步驟：**
1. 打開翻譯文件。
2. 仔細查看內容。
3. 進行必要的編輯以提高翻譯準確性。
4. 保存更改。

### 4. 文件格式問題
**問題：** 翻譯文件的格式不正確。在表格中可能出現問題，這裡的附加 ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` 可以解決表格問題。

**步驟：**
1. 打開翻譯文件。
2. 與原始文件進行比較以識別格式問題。
3. 調整格式以匹配原始文件。
4. 保存更改。

**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。對於因使用此翻譯而產生的任何誤解或誤釋，我們不承擔責任。