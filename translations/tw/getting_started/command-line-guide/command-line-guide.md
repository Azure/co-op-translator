<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d8eec418d6325416b9fab19a2dfcbf41",
  "translation_date": "2025-05-06T17:52:04+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "tw"
}
-->
# 如何使用 Co-op Translator 指令列介面 (CLI)

## 先決條件

- **Python 3.10 或以上版本**：執行 Co-op Translator 所需。
- **語言模型資源**：  
  - **Azure OpenAI** 或其他大型語言模型。詳細資訊請參考 [supported models and services](../../../../README.md)。
- **電腦視覺資源**（選用）：  
  - 用於圖片翻譯。如果沒有，翻譯器會自動切換到 [Markdown-only mode](../markdown-only-mode.md)。  
  - **Azure Computer Vision**

### 初始設定

開始前，請先準備以下資源：

- [Set up Azure OpenAI](../set-up-resources/set-up-azure-openai.md)  
- [Set up Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md)（選用）

## 目錄

1. [在根目錄建立 '.env' 檔案](./create-env-file.md)  
   - 包含所選語言模型服務所需的金鑰。  
   - 若未提供 Azure Computer Vision 金鑰或指定 `-md`，翻譯器將以 Markdown-only 模式運作。  
3. [安裝 Co-op translator 套件](./install-package.md)  
4. [使用 Co-op Translator 翻譯你的專案](./translator-your-project.md)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威資料來源。對於重要資訊，建議採用專業人工翻譯。我們對於因使用本翻譯而產生的任何誤解或誤譯不負任何責任。