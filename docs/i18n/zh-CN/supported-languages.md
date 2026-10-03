# 支持的语言

Co-op Translator 支持以下语言代码，用于文本、笔记本和图像的翻译输出。

如果您想添加新语言，请在 `src/co_op_translator/fonts/` 下更新语言和字体映射，并在打开拉取请求之前测试该语言。

| 语言代码 | 语言名称 | 字体 | RTL 支持 | 已知问题 |
| --- | --- | --- | --- | --- |
| en | 英语 | NotoSans-Medium.ttf | 否 | 否 |
| fr | 法语 | NotoSans-Medium.ttf | 否 | 否 |
| es | 西班牙语 | NotoSans-Medium.ttf | 否 | 否 |
| de | 德语 | NotoSans-Medium.ttf | 否 | 否 |
| ru | 俄语 | NotoSans-Medium.ttf | 否 | 否 |
| ar | 阿拉伯语 | NotoSansArabic-Medium.ttf | 是 | 否 |
| fa | 波斯语 (Farsi) | NotoSansArabic-Medium.ttf | 是 | 否 |
| ur | 乌尔都语 | NotoSansArabic-Medium.ttf | 是 | 否 |
| zh-CN | 中文 (简体) | NotoSansCJK-Medium.ttc | 否 | 否 |
| zh-MO | 中文 (繁体，澳门) | NotoSansCJK-Medium.ttc | 否 | 否 |
| zh-HK | 中文 (繁体，香港) | NotoSansCJK-Medium.ttc | 否 | 否 |
| zh-TW | 中文 (繁体，台湾) | NotoSansCJK-Medium.ttc | 否 | 否 |
| ja | 日语 | NotoSansCJK-Medium.ttc | 否 | 否 |
| ko | 韩语 | NotoSansCJK-Medium.ttc | 否 | 否 |
| hi | 印地语 | NotoSansDevanagari-Medium.ttf | 否 | 否 |
| bn | 孟加拉语 | NotoSansBengali-Medium.ttf | 否 | 否 |
| mr | 马拉地语 | NotoSansDevanagari-Medium.ttf | 否 | 否 |
| ne | 尼泊尔语 | NotoSansDevanagari-Medium.ttf | 否 | 否 |
| pa | 旁遮普语 (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | 否 | 否 |
| pt-PT | 葡萄牙语 (葡萄牙) | NotoSans-Medium.ttf | 否 | 否 |
| pt-BR | 葡萄牙语 (巴西) | NotoSans-Medium.ttf | 否 | 否 |
| it | 意大利语 | NotoSans-Medium.ttf | 否 | 否 |
| lt | 立陶宛语 | NotoSans-Medium.ttf | 否 | 否 |
| pl | 波兰语 | NotoSans-Medium.ttf | 否 | 否 |
| tr | 土耳其语 | NotoSans-Medium.ttf | 否 | 否 |
| el | 希腊语 | NotoSans-Medium.ttf | 否 | 否 |
| th | 泰语 | NotoSansThai-Medium.ttf | 否 | 否 |
| sv | 瑞典语 | NotoSans-Medium.ttf | 否 | 否 |
| da | 丹麦语 | NotoSans-Medium.ttf | 否 | 否 |
| no | 挪威语 | NotoSans-Medium.ttf | 否 | 否 |
| fi | 芬兰语 | NotoSans-Medium.ttf | 否 | 否 |
| nl | 荷兰语 | NotoSans-Medium.ttf | 否 | 否 |
| he | 希伯来语 | NotoSansHebrew-Medium.ttf | 是 | 否 |
| vi | 越南语 | NotoSans-Medium.ttf | 否 | 否 |
| id | 印度尼西亚语 | NotoSans-Medium.ttf | 否 | 否 |
| ms | 马来语 | NotoSans-Medium.ttf | 否 | 否 |
| tl | 他加禄语 (菲律宾语) | NotoSans-Medium.ttf | 否 | 否 |
| sw | 斯瓦希里语 | NotoSans-Medium.ttf | 否 | 否 |
| hu | 匈牙利语 | NotoSans-Medium.ttf | 否 | 否 |
| cs | 捷克语 | NotoSans-Medium.ttf | 否 | 否 |
| sk | 斯洛伐克语 | NotoSans-Medium.ttf | 否 | 否 |
| ro | 罗马尼亚语 | NotoSans-Medium.ttf | 否 | 否 |
| bg | 保加利亚语 | NotoSans-Medium.ttf | 否 | 否 |
| sr | 塞尔维亚语 (西里尔字母) | NotoSans-Medium.ttf | 否 | 否 |
| hr | 克罗地亚语 | NotoSans-Medium.ttf | 否 | 否 |
| sl | 斯洛文尼亚语 | NotoSans-Medium.ttf | 否 | 否 |
| uk | 乌克兰语 | NotoSans-Medium.ttf | 否 | 否 |
| my | 缅甸语 (Myanmar) | NotoSansMyanmar-Medium.ttf | 否 | 否 |
| ta | 泰米尔语 | NotoSansTamil-Medium.ttf | 否 | 否 |
| et | 爱沙尼亚语 | NotoSans-Medium.ttf | 否 | 否 |
| pcm | 尼日利亚皮钦语 | NotoSans-Medium.ttf | 否 | 否 |
| te | 泰卢固语 | NotoSans-Medium.ttf | 否 | 否 |
| ml | 马拉雅拉姆语 | NotoSans-Medium.ttf | 否 | 否 |
| kn | 卡纳达语 | NotoSans-Medium.ttf | 否 | 否 |
| km | 高棉语 | NotoSansKhmer-Medium.ttf | 否 | 否 |
| mni | 曼尼普里语 (Meitei Mayek) | NotoSansMeeteiMayek-Medium.ttf | 否 | 否 |

## 添加语言

要为新语言添加支持：

1. 将语言代码和显示名称添加到语言工具中。
2. 在 `src/co_op_translator/fonts/font_language_mappings.yml` 中添加或映射字体。
3. 测试 Markdown 和图像的翻译输出。
4. 提交包含映射和验证说明的拉取请求。