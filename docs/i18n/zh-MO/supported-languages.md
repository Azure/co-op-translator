# 支援的語言

Co-op Translator 支援下列語言代碼，用於文字、筆記本及影像翻譯輸出。

若要新增語言，請更新 `src/co_op_translator/fonts/` 下的語言與字型對應，並在開啟 pull request 前測試該語言。

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | 英文 | NotoSans-Medium.ttf | 否 | 無 |
| fr | 法文 | NotoSans-Medium.ttf | 否 | 無 |
| es | 西班牙文 | NotoSans-Medium.ttf | 否 | 無 |
| de | 德文 | NotoSans-Medium.ttf | 否 | 無 |
| ru | 俄文 | NotoSans-Medium.ttf | 否 | 無 |
| ar | 阿拉伯文 | NotoSansArabic-Medium.ttf | 是 | 無 |
| fa | 波斯語（法爾西） | NotoSansArabic-Medium.ttf | 是 | 無 |
| ur | 烏爾都語 | NotoSansArabic-Medium.ttf | 是 | 無 |
| zh-CN | 中文（簡體） | NotoSansCJK-Medium.ttc | 否 | 無 |
| zh-MO | 中文（繁體，澳門） | NotoSansCJK-Medium.ttc | 否 | 無 |
| zh-HK | 中文（繁體，香港） | NotoSansCJK-Medium.ttc | 否 | 無 |
| zh-TW | 中文（繁體，台灣） | NotoSansCJK-Medium.ttc | 否 | 無 |
| ja | 日文 | NotoSansCJK-Medium.ttc | 否 | 無 |
| ko | 韓文 | NotoSansCJK-Medium.ttc | 否 | 無 |
| hi | 印地語 | NotoSansDevanagari-Medium.ttf | 否 | 無 |
| bn | 孟加拉語 | NotoSansBengali-Medium.ttf | 否 | 無 |
| mr | 馬拉地語 | NotoSansDevanagari-Medium.ttf | 否 | 無 |
| ne | 尼泊爾語 | NotoSansDevanagari-Medium.ttf | 否 | 無 |
| pa | 旁遮普語（Gurmukhi） | NotoSansGurmukhi-Medium.ttf | 否 | 無 |
| pt-PT | 葡萄牙文（葡萄牙） | NotoSans-Medium.ttf | 否 | 無 |
| pt-BR | 葡萄牙文（巴西） | NotoSans-Medium.ttf | 否 | 無 |
| it | 義大利文 | NotoSans-Medium.ttf | 否 | 無 |
| lt | 立陶宛語 | NotoSans-Medium.ttf | 否 | 無 |
| pl | 波蘭語 | NotoSans-Medium.ttf | 否 | 無 |
| tr | 土耳其語 | NotoSans-Medium.ttf | 否 | 無 |
| el | 希臘語 | NotoSans-Medium.ttf | 否 | 無 |
| th | 泰語 | NotoSansThai-Medium.ttf | 否 | 無 |
| sv | 瑞典語 | NotoSans-Medium.ttf | 否 | 無 |
| da | 丹麥語 | NotoSans-Medium.ttf | 否 | 無 |
| no | 挪威語 | NotoSans-Medium.ttf | 否 | 無 |
| fi | 芬蘭語 | NotoSans-Medium.ttf | 否 | 無 |
| nl | 荷蘭語 | NotoSans-Medium.ttf | 否 | 無 |
| he | 希伯來語 | NotoSansHebrew-Medium.ttf | 是 | 無 |
| vi | 越南語 | NotoSans-Medium.ttf | 否 | 無 |
| id | 印尼語 | NotoSans-Medium.ttf | 否 | 無 |
| ms | 馬來語 | NotoSans-Medium.ttf | 否 | 無 |
| tl | 他加祿語（菲律賓） | NotoSans-Medium.ttf | 否 | 無 |
| sw | 斯瓦希里語 | NotoSans-Medium.ttf | 否 | 無 |
| hu | 匈牙利語 | NotoSans-Medium.ttf | 否 | 無 |
| cs | 捷克語 | NotoSans-Medium.ttf | 否 | 無 |
| sk | 斯洛伐克語 | NotoSans-Medium.ttf | 否 | 無 |
| ro | 羅馬尼亞語 | NotoSans-Medium.ttf | 否 | 無 |
| bg | 保加利亞語 | NotoSans-Medium.ttf | 否 | 無 |
| sr | 塞爾維亞語（西里爾字母） | NotoSans-Medium.ttf | 否 | 無 |
| hr | 克羅地亞語 | NotoSans-Medium.ttf | 否 | 無 |
| sl | 斯洛維尼亞語 | NotoSans-Medium.ttf | 否 | 無 |
| uk | 烏克蘭語 | NotoSans-Medium.ttf | 否 | 無 |
| my | 緬甸語（緬甸） | NotoSansMyanmar-Medium.ttf | 否 | 無 |
| ta | 泰米爾語 | NotoSansTamil-Medium.ttf | 否 | 無 |
| et | 愛沙尼亞語 | NotoSans-Medium.ttf | 否 | 無 |
| pcm | 尼日利亞皮欽語 | NotoSans-Medium.ttf | 否 | 無 |
| te | 泰盧固語 | NotoSans-Medium.ttf | 否 | 無 |
| ml | 馬拉雅拉姆語 | NotoSans-Medium.ttf | 否 | 無 |
| kn | 坎納達語 | NotoSans-Medium.ttf | 否 | 無 |
| km | 高棉語 | NotoSansKhmer-Medium.ttf | 否 | 無 |

## 新增語言

To add support for a new language:

1. 將語言代碼與顯示名稱新增至語言公用程式。
2. 在 `src/co_op_translator/fonts/font_language_mappings.yml` 新增或對應字型。
3. 測試 Markdown 與影像翻譯輸出。
4. 開啟包含對應與驗證說明的 pull request。