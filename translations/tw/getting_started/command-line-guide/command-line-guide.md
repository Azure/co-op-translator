<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5eb9b53c81804f04bc9456160e79940",
  "translation_date": "2025-05-07T14:02:18+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "tw"
}
-->
# 如何使用 Co-op Translator 指令列介面 (CLI)

## 先決條件

- **Python 3.10 或更新版本**：執行 Co-op Translator 所需。
- **語言模型資源**：
  - **Azure OpenAI** 或其他大型語言模型。詳細資訊請參考 [supported models and services](../../../../README.md)。
- **電腦視覺資源**（可選）：
  - 用於圖片翻譯。若無此資源，翻譯器將預設為 [Markdown-only mode](../markdown-only-mode.md)。
  - **Azure Computer Vision**

## 目錄

1. [在根目錄建立 '.env' 檔案](./create-env-file.md)
   - 包含所選語言模型服務所需的金鑰。
   - 若省略 Azure Computer Vision 金鑰或指定 `-md`，翻譯器將以 Markdown-only 模式運作。
1. [安裝 Co-op translator 套件](./install-package.md)
1. [使用 Co-op Translator 翻譯你的專案](./translator-your-project.md)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用本翻譯而產生之任何誤解或誤譯負責。