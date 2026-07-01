# 支持的语言

Co-op Translator 支持以下语言代码，用于文本、笔记本和图像翻译输出。

如果您想添加新的语言，请在 `src/co_op_translator/fonts/` 下更新语言和字体映射，并在打开拉取请求之前测试该语言。

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | 英语 | NotoSans-Medium.ttf | 否 | 无 |
| fr | 法语 | NotoSans-Medium.ttf | 否 | 无 |
| es | 西班牙语 | NotoSans-Medium.ttf | 否 | 无 |
| de | 德语 | NotoSans-Medium.ttf | 否 | 无 |
| ru | 俄语 | NotoSans-Medium.ttf | 否 | 无 |
| ar | 阿拉伯语 | NotoSansArabic-Medium.ttf | 是 | 无 |
| fa | 波斯语（法尔西语） | NotoSansArabic-Medium.ttf | 是 | 无 |
| ur | 乌尔都语 | NotoSansArabic-Medium.ttf | 是 | 无 |
| zh-CN | 中文 (Simplified) | NotoSansCJK-Medium.ttc | 否 | 无 |
| zh-MO | 中文 (Traditional, Macau) | NotoSansCJK-Medium.ttc | 否 | 无 |
| zh-HK | 中文 (Traditional, Hong Kong) | NotoSansCJK-Medium.ttc | 否 | 无 |
| zh-TW | 中文 (Traditional, Taiwan) | NotoSansCJK-Medium.ttc | 否 | 无 |
| ja | 日语 | NotoSansCJK-Medium.ttc | 否 | 无 |
| ko | 韩语 | NotoSansCJK-Medium.ttc | 否 | 无 |
| hi | 印地语 | NotoSansDevanagari-Medium.ttf | 否 | 无 |
| bn | 孟加拉语 | NotoSansBengali-Medium.ttf | 否 | 无 |
| mr | 马拉地语 | NotoSansDevanagari-Medium.ttf | 否 | 无 |
| ne | 尼泊尔语 | NotoSansDevanagari-Medium.ttf | 否 | 无 |
| pa | 旁遮普语（古鲁姆基） | NotoSansGurmukhi-Medium.ttf | 否 | 无 |
| pt-PT | 葡萄牙语（葡萄牙） | NotoSans-Medium.ttf | 否 | 无 |
| pt-BR | 葡萄牙语（巴西） | NotoSans-Medium.ttf | 否 | 无 |
| it | 意大利语 | NotoSans-Medium.ttf | 否 | 无 |
| lt | 立陶宛语 | NotoSans-Medium.ttf | 否 | 无 |
| pl | 波兰语 | NotoSans-Medium.ttf | 否 | 无 |
| tr | 土耳其语 | NotoSans-Medium.ttf | 否 | 无 |
| el | 希腊语 | NotoSans-Medium.ttf | 否 | 无 |
| th | 泰语 | NotoSansThai-Medium.ttf | 否 | 无 |
| sv | 瑞典语 | NotoSans-Medium.ttf | 否 | 无 |
| da | 丹麦语 | NotoSans-Medium.ttf | 否 | 无 |
| no | 挪威语 | NotoSans-Medium.ttf | 否 | 无 |
| fi | 芬兰语 | NotoSans-Medium.ttf | 否 | 无 |
| nl | 荷兰语 | NotoSans-Medium.ttf | 否 | 无 |
| he | 希伯来语 | NotoSansHebrew-Medium.ttf | 是 | 无 |
| vi | 越南语 | NotoSans-Medium.ttf | 否 | 无 |
| id | 印度尼西亚语 | NotoSans-Medium.ttf | 否 | 无 |
| ms | 马来语 | NotoSans-Medium.ttf | 否 | 无 |
| tl | 他加禄语（菲律宾语） | NotoSans-Medium.ttf | 否 | 无 |
| sw | 斯瓦希里语 | NotoSans-Medium.ttf | 否 | 无 |
| hu | 匈牙利语 | NotoSans-Medium.ttf | 否 | 无 |
| cs | 捷克语 | NotoSans-Medium.ttf | 否 | 无 |
| sk | 斯洛伐克语 | NotoSans-Medium.ttf | 否 | 无 |
| ro | 罗马尼亚语 | NotoSans-Medium.ttf | 否 | 无 |
| bg | 保加利亚语 | NotoSans-Medium.ttf | 否 | 无 |
| sr | 塞尔维亚语（西里尔文） | NotoSans-Medium.ttf | 否 | 无 |
| hr | 克罗地亚语 | NotoSans-Medium.ttf | 否 | 无 |
| sl | 斯洛文尼亚语 | NotoSans-Medium.ttf | 否 | 无 |
| uk | 乌克兰语 | NotoSans-Medium.ttf | 否 | 无 |
| my | 缅甸语（Myanmar） | NotoSansMyanmar-Medium.ttf | 否 | 无 |
| ta | 泰米尔语 | NotoSansTamil-Medium.ttf | 否 | 无 |
| et | 爱沙尼亚语 | NotoSans-Medium.ttf | 否 | 无 |
| pcm | 尼日利亚皮钦语 | NotoSans-Medium.ttf | 否 | 无 |
| te | 泰卢固语 | NotoSans-Medium.ttf | 否 | 无 |
| ml | 马拉雅拉姆语 | NotoSans-Medium.ttf | 否 | 无 |
| kn | 卡纳达语 | NotoSans-Medium.ttf | 否 | 无 |
| km | 高棉语 | NotoSansKhmer-Medium.ttf | 否 | 无 |

## 添加语言

要添加对新语言的支持：

1. 将语言代码和显示名称添加到语言实用程序。
2. 在 `src/co_op_translator/fonts/font_language_mappings.yml` 中添加或映射字体。
3. 测试 Markdown 和图像的翻译输出。
4. 提交一个包含映射和验证说明的拉取请求。