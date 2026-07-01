# 支援的語言

Co-op Translator 支援下列語言代碼，用於文字、筆記本和圖片翻譯輸出。

如果您想要新增語言，請更新 `src/co_op_translator/fonts/` 底下的語言與字型對應，並在開啟 pull request 之前測試該語言。

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | 英文 | NotoSans-Medium.ttf | 否 | 否 |
| fr | 法文 | NotoSans-Medium.ttf | 否 | 否 |
| es | 西班牙語 | NotoSans-Medium.ttf | 否 | 否 |
| de | 德文 | NotoSans-Medium.ttf | 否 | 否 |
| ru | 俄文 | NotoSans-Medium.ttf | 否 | 否 |
| ar | 阿拉伯文 | NotoSansArabic-Medium.ttf | 是 | 否 |
| fa | 波斯語 (Farsi) | NotoSansArabic-Medium.ttf | 是 | 否 |
| ur | 烏爾都語 | NotoSansArabic-Medium.ttf | 是 | 否 |
| zh-CN | 中文 (簡體) | NotoSansCJK-Medium.ttc | 否 | 否 |
| zh-MO | 中文 (繁體, Macau) | NotoSansCJK-Medium.ttc | 否 | 否 |
| zh-HK | 中文 (繁體, Hong Kong) | NotoSansCJK-Medium.ttc | 否 | 否 |
| zh-TW | 中文 (繁體, Taiwan) | NotoSansCJK-Medium.ttc | 否 | 否 |
| ja | 日文 | NotoSansCJK-Medium.ttc | 否 | 否 |
| ko | 韓文 | NotoSansCJK-Medium.ttc | 否 | 否 |
| hi | 印地語 | NotoSansDevanagari-Medium.ttf | 否 | 否 |
| bn | 孟加拉語 | NotoSansBengali-Medium.ttf | 否 | 否 |
| mr | 馬拉地語 | NotoSansDevanagari-Medium.ttf | 否 | 否 |
| ne | 尼泊爾語 | NotoSansDevanagari-Medium.ttf | 否 | 否 |
| pa | 旁遮普語 (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | 否 | 否 |
| pt-PT | 葡萄牙語 (Portugal) | NotoSans-Medium.ttf | 否 | 否 |
| pt-BR | 葡萄牙語 (Brazil) | NotoSans-Medium.ttf | 否 | 否 |
| it | 義大利語 | NotoSans-Medium.ttf | 否 | 否 |
| lt | 立陶宛語 | NotoSans-Medium.ttf | 否 | 否 |
| pl | 波蘭語 | NotoSans-Medium.ttf | 否 | 否 |
| tr | 土耳其語 | NotoSans-Medium.ttf | 否 | 否 |
| el | 希臘語 | NotoSans-Medium.ttf | 否 | 否 |
| th | 泰語 | NotoSansThai-Medium.ttf | 否 | 否 |
| sv | 瑞典語 | NotoSans-Medium.ttf | 否 | 否 |
| da | 丹麥語 | NotoSans-Medium.ttf | 否 | 否 |
| no | 挪威語 | NotoSans-Medium.ttf | 否 | 否 |
| fi | 芬蘭語 | NotoSans-Medium.ttf | 否 | 否 |
| nl | 荷蘭語 | NotoSans-Medium.ttf | 否 | 否 |
| he | 希伯來語 | NotoSansHebrew-Medium.ttf | 是 | 否 |
| vi | 越南語 | NotoSans-Medium.ttf | 否 | 否 |
| id | 印尼語 | NotoSans-Medium.ttf | 否 | 否 |
| ms | 馬來語 | NotoSans-Medium.ttf | 否 | 否 |
| tl | 塔加洛語 (Filipino) | NotoSans-Medium.ttf | 否 | 否 |
| sw | 史瓦希里語 | NotoSans-Medium.ttf | 否 | 否 |
| hu | 匈牙利語 | NotoSans-Medium.ttf | 否 | 否 |
| cs | 捷克語 | NotoSans-Medium.ttf | 否 | 否 |
| sk | 斯洛伐克語 | NotoSans-Medium.ttf | 否 | 否 |
| ro | 羅馬尼亞語 | NotoSans-Medium.ttf | 否 | 否 |
| bg | 保加利亞語 | NotoSans-Medium.ttf | 否 | 否 |
| sr | 塞爾維亞語 (Cyrillic) | NotoSans-Medium.ttf | 否 | 否 |
| hr | 克羅埃西亞語 | NotoSans-Medium.ttf | 否 | 否 |
| sl | 斯洛維尼亞語 | NotoSans-Medium.ttf | 否 | 否 |
| uk | 烏克蘭語 | NotoSans-Medium.ttf | 否 | 否 |
| my | 緬甸語 | NotoSansMyanmar-Medium.ttf | 否 | 否 |
| ta | 泰米爾語 | NotoSansTamil-Medium.ttf | 否 | 否 |
| et | 愛沙尼亞語 | NotoSans-Medium.ttf | 否 | 否 |
| pcm | 奈及利亞皮欽語 | NotoSans-Medium.ttf | 否 | 否 |
| te | 泰盧固語 | NotoSans-Medium.ttf | 否 | 否 |
| ml | 馬拉雅拉姆語 | NotoSans-Medium.ttf | 否 | 否 |
| kn | 坎納達語 | NotoSans-Medium.ttf | 否 | 否 |
| km | 高棉語 | NotoSansKhmer-Medium.ttf | 否 | 否 |

## 新增語言

To add support for a new language:

1. 將語言代碼和顯示名稱新增到語言工具。
2. 在 `src/co_op_translator/fonts/font_language_mappings.yml` 中新增或映射字型。
3. 測試 Markdown 和圖片翻譯輸出。
4. 開啟一個包含對應映射與驗證說明的 pull request。