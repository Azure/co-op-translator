<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4ed48f23ec418b31e90a02fe629fcde",
  "translation_date": "2025-06-14T12:49:44+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "mo"
}
-->
# 支援的語言

下表列出了目前由 **Co-op Translator** 支援的語言。它包含語言代碼、語言名稱及每種語言已知的問題。如果您希望增加對新語言的支援，請在位於 `src/co_op_translator/fonts/` 的 `font_language_mappings.yml` 文件中添加相應的語言代碼、名稱及適當的字體，並在測試後提交拉取請求。

| 語言代碼 | 語言名稱                  | 字體                               | RTL 支援 | 已知問題 |
|----------|---------------------------|-----------------------------------|----------|----------|
| en       | 英語                      | NotoSans-Medium.ttf               | 否       | 否       |
| fr       | 法語                      | NotoSans-Medium.ttf               | 否       | 否       |
| es       | 西班牙語                  | NotoSans-Medium.ttf               | 否       | 否       |
| de       | 德語                      | NotoSans-Medium.ttf               | 否       | 否       |
| ru       | 俄語                      | NotoSans-Medium.ttf               | 否       | 否       |
| ar       | 阿拉伯語                  | NotoSansArabic-Medium.ttf         | 是       | 否       |
| fa       | 波斯語 (法爾西語)         | NotoSansArabic-Medium.ttf         | 否       | 否       |
| ur       | 烏爾都語                  | NotoSansArabic-Medium.ttf         | 否       | 否       |
| zh       | 中文 (簡體)               | NotoSansCJK-Medium.ttc            | 否       | 否       |
| mo       | 中文 (繁體, 澳門)         | NotoSansCJK-Medium.ttc            | 否       | 否       |
| hk       | 中文 (繁體, 香港)         | NotoSansCJK-Medium.ttc            | 否       | 否       |
| tw       | 中文 (繁體, 台灣)         | NotoSansCJK-Medium.ttc            | 否       | 否       |
| ja       | 日語                      | NotoSansCJK-Medium.ttc            | 否       | 否       |
| ko       | 韓語                      | NotoSansCJK-Medium.ttc            | 否       | 否       |
| hi       | 印地語                    | NotoSansDevanagari-Medium.ttf     | 否       | 否       |
| bn       | 孟加拉語                  | NotoSansBengali-Medium.ttf        | 否       | 否       |
| mr       | 馬拉地語                  | NotoSansDevanagari-Medium.ttf     | 否       | 否       |
| ne       | 尼泊爾語                  | NotoSansDevanagari-Medium.ttf     | 否       | 否       |
| pa       | 旁遮普語 (古爾穆基語)     | NotoSansGurmukhi-Medium.ttf       | 否       | 否       |
| pt       | 葡萄牙語 (葡萄牙)         | NotoSans-Medium.ttf               | 否       | 否       |
| br       | 葡萄牙語 (巴西)           | NotoSans-Medium.ttf               | 否       | 否       |
| it       | 意大利語                  | NotoSans-Medium.ttf               | 否       | 否       |
| pl       | 波蘭語                    | NotoSans-Medium.ttf               | 否       | 否       |
| tr       | 土耳其語                  | NotoSans-Medium.ttf               | 否       | 否       |
| el       | 希臘語                    | NotoSans-Medium.ttf               | 否       | 否       |
| th       | 泰語                      | NotoSansThai-Medium.ttf           | 否       | 否       |
| sv       | 瑞典語                    | NotoSans-Medium.ttf               | 否       | 否       |
| da       | 丹麥語                    | NotoSans-Medium.ttf               | 否       | 否       |
| no       | 挪威語                    | NotoSans-Medium.ttf               | 否       | 否       |
| fi       | 芬蘭語                    | NotoSans-Medium.ttf               | 否       | 否       |
| nl       | 荷蘭語                    | NotoSans-Medium.ttf               | 否       | 否       |
| he       | 希伯來語                  | NotoSansHebrew-Medium.ttf         | 否       | 否       |
| vi       | 越南語                    | NotoSans-Medium.ttf               | 否       | 否       |
| id       | 印尼語                    | NotoSans-Medium.ttf               | 否       | 否       |
| ms       | 馬來語                    | NotoSans-Medium.ttf               | 否       | 否       |
| tl       | 塔加洛語 (菲律賓語)       | NotoSans-Medium.ttf               | 否       | 否       |
| sw       | 斯瓦希里語                | NotoSans-Medium.ttf               | 否       | 否       |
| hu       | 匈牙利語                  | NotoSans-Medium.ttf               | 否       | 否       |
| cs       | 捷克語                    | NotoSans-Medium.ttf               | 否       | 否       |
| sk       | 斯洛伐克語                | NotoSans-Medium.ttf               | 否       | 否       |
| ro       | 羅馬尼亞語                | NotoSans-Medium.ttf               | 否       | 否       |
| bg       | 保加利亞語                | NotoSans-Medium.ttf               | 否       | 否       |
| sr       | 塞爾維亞語 (西里爾字母)   | NotoSans-Medium.ttf               | 否       | 否       |
| hr       | 克羅地亞語                | NotoSans-Medium.ttf               | 否       | 否       |
| sl       | 斯洛文尼亞語              | NotoSans-Medium.ttf               | 否       | 否       |
| uk       | 烏克蘭語                  | NotoSans-Medium.ttf               | 否       | 否       |
| my       | 緬甸語 (緬甸)             | NotoSans-Medium.ttf               | 否       | 否       |

## 添加新語言

要增加對新語言的支援：

1. 前往 [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml)。
2. 添加語言代碼、名稱及適當的字體文件名稱。確保包括 `rtl` 屬性如果語言是從右到左。
3. 如果需要使用新的字體，請確保該字體可以在開源項目中免費使用，並檢查其許可和版權條款。在確認後，將字體文件添加到 `src/co_op_translator/fonts/` 目錄。
4. 在本地測試您的更改，以確保新語言得到正確支援。
5. 提交包含您更改的拉取請求，並在 PR 描述中指出新語言的添加。

範例：

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對使用此翻譯引起的任何誤解或誤釋不承擔責任。