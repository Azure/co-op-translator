<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:23:38+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "hk"
}
-->
# Microsoft Co-op Translator 故障排除指南

## 概覽  
Microsoft Co-Op Translator 係一個強大嘅工具，可以無縫翻譯 Markdown 文件。呢份指南會幫你解決使用工具時常見嘅問題。

## 常見問題同解決方法

### 1. Markdown 標籤問題  
**問題：** 翻譯後嘅 Markdown 文件頂部出現咗 `markdown` 標籤，導致渲染出錯。

**解決方法：** 只需要刪除文件頂部嘅 `markdown` 標籤，就可以令 Markdown 文件正常渲染。

**步驟：**  
1. 打開翻譯後嘅 Markdown (`.md`) 文件。  
2. 搵出文件頂部嘅 `markdown` 標籤。  
3. 刪除 `markdown` 標籤。  
4. 儲存文件更改。  
5. 重新打開文件，確認渲染正常。

### 2. 嵌入圖片 URL 問題  
**問題：** 嵌入圖片嘅 URL 同語言地區唔匹配，導致圖片錯誤或者缺失。

**解決方法：** 檢查嵌入圖片嘅 URL，確保同語言地區一致。所有圖片都喺 `translated_images` 文件夾，每張圖片文件名都有語言地區標籤。

**步驟：**  
1. 打開翻譯後嘅 Markdown 文件。  
2. 找出嵌入嘅圖片同佢哋嘅 URL。  
3. 確認圖片文件名嘅語言地區標籤同文件語言一致。  
4. 如有需要，更新 URL。  
5. 儲存更改，重新打開文件，確認圖片正常顯示。

### 3. 翻譯準確度  
**問題：** 翻譯內容唔準確或者需要進一步修改。

**解決方法：** 仔細檢查翻譯文件，作出必要嘅修改，提升準確度同可讀性。

**步驟：**  
1. 打開翻譯文件。  
2. 仔細審閱內容。  
3. 作出需要嘅修改以提升翻譯準確度。  
4. 儲存更改。

### 4. 文件格式問題  
**問題：** 翻譯後嘅文件格式錯誤，例如表格格式唔正確。以下嘅 ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` 可以解決表格問題。

**步驟：**  
1. 打開翻譯文件。  
2. 同原始文件比較，搵出格式問題。  
3. 調整格式令佢同原始文件一致。  
4. 儲存更改。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋致力於準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件嘅母語版本應視為權威來源。對於重要資料，建議採用專業人工翻譯。我哋對因使用此翻譯而引起嘅任何誤解或誤釋概不負責。