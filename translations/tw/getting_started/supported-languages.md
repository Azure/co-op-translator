<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ba33aa8d5da0d3dd14322b77fcb63deb",
  "translation_date": "2025-05-06T17:47:02+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "tw"
}
-->
# Supported languages

以下表格列出目前 **Co-op Translator** 支援的語言，包含語言代碼、語言名稱，以及該語言相關的已知問題。如果您想新增語言支援，請在位於 `src/co_op_translator/fonts/` 的 `font_language_mappings.yml` 檔案中新增相對應的語言代碼、名稱及適用字型，並在測試後提交 Pull Request。

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | 英文                 | NotoSans-Medium.ttf               | 否          | 無           |
| fr            | 法文                 | NotoSans-Medium.ttf               | 否          | 無           |
| es            | 西班牙文             | NotoSans-Medium.ttf               | 否          | 無           |
| de            | 德文                 | NotoSans-Medium.ttf               | 否          | 無           |
| ru            | 俄文                 | NotoSans-Medium.ttf               | 否          | 無           |
| ar            | 阿拉伯文             | NotoSansArabic-Medium.ttf         | 是          | 無           |
| fa            | 波斯文 (法爾西語)    | NotoSansArabic-Medium.ttf         | 是          | 無           |
| ur            | 烏爾都文             | NotoSansArabic-Medium.ttf         | 是          | 無           |
| zh            | 中文 (簡體)          | NotoSansCJK-Medium.ttc            | 否          | 無           |
| mo            | 中文 (繁體，澳門)     | NotoSansCJK-Medium.ttc            | 否          | 無           |
| hk            | 中文 (繁體，香港)     | NotoSansCJK-Medium.ttc            | 否          | 無           |
| tw            | 中文 (繁體，台灣)     | NotoSansCJK-Medium.ttc            | 否          | 無           |
| ja            | 日文                 | NotoSansCJK-Medium.ttc            | 否          | 無           |
| ko            | 韓文                 | NotoSansCJK-Medium.ttc            | 否          | 無           |
| hi            | 印地文               | NotoSansDevanagari-Medium.ttf     | 否          | 無           |
| bn            | 孟加拉文             | NotoSansBengali-Medium.ttf        | 否          | 無           |
| mr            | 馬拉地文             | NotoSansDevanagari-Medium.ttf     | 否          | 無           |
| ne            | 尼泊爾文             | NotoSansDevanagari-Medium.ttf     | 否          | 無           |
| pa            | 旁遮普文 (古魯穆奇)  | NotoSansGurmukhi-Medium.ttf       | 否          | 無           |
| pt            | 葡萄牙文 (葡萄牙)    | NotoSans-Medium.ttf               | 否          | 無           |
| br            | 葡萄牙文 (巴西)      | NotoSans-Medium.ttf               | 否          | 無           |
| it            | 義大利文             | NotoSans-Medium.ttf               | 否          | 無           |
| pl            | 波蘭文               | NotoSans-Medium.ttf               | 否          | 無           |
| tr            | 土耳其文             | NotoSans-Medium.ttf               | 否          | 無           |
| el            | 希臘文               | NotoSans-Medium.ttf               | 否          | 無           |
| th            | 泰文                 | NotoSansThai-Medium.ttf           | 否          | 無           |
| sv            | 瑞典文               | NotoSans-Medium.ttf               | 否          | 無           |
| da            | 丹麥文               | NotoSans-Medium.ttf               | 否          | 無           |
| no            | 挪威文               | NotoSans-Medium.ttf               | 否          | 無           |
| fi            | 芬蘭文               | NotoSans-Medium.ttf               | 否          | 無           |
| nl            | 荷蘭文               | NotoSans-Medium.ttf               | 否          | 無           |
| he            | 希伯來文             | NotoSansHebrew-Medium.ttf         | 是          | 無           |
| vi            | 越南文               | NotoSans-Medium.ttf               | 否          | 無           |
| id            | 印尼文               | NotoSans-Medium.ttf               | 否          | 無           |
| ms            | 馬來文               | NotoSans-Medium.ttf               | 否          | 無           |
| tl            | 他加祿文 (菲律賓語)  | NotoSans-Medium.ttf               | 否          | 無           |
| sw            | 斯瓦希里文           | NotoSans-Medium.ttf               | 否          | 無           |
| hu            | 匈牙利文             | NotoSans-Medium.ttf               | 否          | 無           |
| cs            | 捷克文               | NotoSans-Medium.ttf               | 否          | 無           |
| sk            | 斯洛伐克文           | NotoSans-Medium.ttf               | 否          | 無           |
| ro            | 羅馬尼亞文           | NotoSans-Medium.ttf               | 否          | 無           |
| bg            | 保加利亞文           | NotoSans-Medium.ttf               | 否          | 無           |
| sr            | 塞爾維亞文 (西里爾字母) | NotoSans-Medium.ttf             | 否          | 無           |
| hr            | 克羅埃西亞文         | NotoSans-Medium.ttf               | 否          | 無           |
| sl            | 斯洛維尼亞文         | NotoSans-Medium.ttf               | 否          | 無           |

## Adding a new language

要新增語言支援：

1. 前往 [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml)。
2. 新增語言代碼、名稱，以及對應的字型檔名。如果語言是由右至左書寫，請務必加上 `rtl` 屬性。
3. 若需使用新字型，請先確認該字型在開源專案中是免費可用，並檢查其授權及版權條款。確認無誤後，將字型檔案加入 `src/co_op_translator/fonts/` 目錄。
4. 在本機測試修改，確保新語言能正常支援。
5. 提交 Pull Request，並在 PR 說明中註明新增語言。

範例：

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威資料來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生之任何誤解或誤釋負責。