<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "badae5ee6451cc1a6e367cfe5ba92efa",
  "translation_date": "2025-10-15T02:27:02+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "zh"
}
-->
# 支持的语言

下表列出了 **Co-op Translator** 当前支持的语言，包括语言代码、语言名称以及已知问题。如果你想添加对新语言的支持，请在 `src/co_op_translator/fonts/` 目录下的 `font_language_mappings.yml` 文件中添加相应的语言代码、名称和合适的字体，并在测试后提交拉取请求。

| 语言代码      | 语言名称                | 字体                              | 是否支持RTL | 已知问题     |
|---------------|------------------------|-----------------------------------|-------------|--------------|
| en            | 英语                   | NotoSans-Medium.ttf               | 否          | 无           |
| fr            | 法语                   | NotoSans-Medium.ttf               | 否          | 无           |
| es            | 西班牙语               | NotoSans-Medium.ttf               | 否          | 无           |
| de            | 德语                   | NotoSans-Medium.ttf               | 否          | 无           |
| ru            | 俄语                   | NotoSans-Medium.ttf               | 否          | 无           |
| ar            | 阿拉伯语               | NotoSansArabic-Medium.ttf         | 是          | 无           |
| fa            | 波斯语（法尔西语）      | NotoSansArabic-Medium.ttf         | 是          | 无           |
| ur            | 乌尔都语                | NotoSansArabic-Medium.ttf         | 是          | 无           |
| zh            | 中文（简体）            | NotoSansCJK-Medium.ttc            | 否          | 无           |
| mo            | 中文（繁体，澳门）      | NotoSansCJK-Medium.ttc            | 否          | 无           |
| hk            | 中文（繁体，香港）      | NotoSansCJK-Medium.ttc            | 否          | 无           |
| tw            | 中文（繁体，台湾）      | NotoSansCJK-Medium.ttc            | 否          | 无           |
| ja            | 日语                   | NotoSansCJK-Medium.ttc            | 否          | 无           |
| ko            | 韩语                   | NotoSansCJK-Medium.ttc            | 否          | 无           |
| hi            | 印地语                  | NotoSansDevanagari-Medium.ttf     | 否          | 无           |
| bn            | 孟加拉语                | NotoSansBengali-Medium.ttf        | 否          | 无           |
| mr            | 马拉地语                | NotoSansDevanagari-Medium.ttf     | 否          | 无           |
| ne            | 尼泊尔语                | NotoSansDevanagari-Medium.ttf     | 否          | 无           |
| pa            | 旁遮普语（果鲁穆奇文）   | NotoSansGurmukhi-Medium.ttf       | 否          | 无           |
| pt            | 葡萄牙语（葡萄牙）      | NotoSans-Medium.ttf               | 否          | 无           |
| br            | 葡萄牙语（巴西）        | NotoSans-Medium.ttf               | 否          | 无           |
| it            | 意大利语                | NotoSans-Medium.ttf               | 否          | 无           |
| lt            | 立陶宛语                | NotoSans-Medium.ttf               | 否          | 无           |
| pl            | 波兰语                  | NotoSans-Medium.ttf               | 否          | 无           |
| tr            | 土耳其语                | NotoSans-Medium.ttf               | 否          | 无           |
| el            | 希腊语                  | NotoSans-Medium.ttf               | 否          | 无           |
| th            | 泰语                    | NotoSansThai-Medium.ttf           | 否          | 无           |
| sv            | 瑞典语                  | NotoSans-Medium.ttf               | 否          | 无           |
| da            | 丹麦语                  | NotoSans-Medium.ttf               | 否          | 无           |
| no            | 挪威语                  | NotoSans-Medium.ttf               | 否          | 无           |
| fi            | 芬兰语                  | NotoSans-Medium.ttf               | 否          | 无           |
| nl            | 荷兰语                  | NotoSans-Medium.ttf               | 否          | 无           |
| he            | 希伯来语                | NotoSansHebrew-Medium.ttf         | 是          | 无           |
| vi            | 越南语                  | NotoSans-Medium.ttf               | 否          | 无           |
| id            | 印度尼西亚语            | NotoSans-Medium.ttf               | 否          | 无           |
| ms            | 马来语                  | NotoSans-Medium.ttf               | 否          | 无           |
| tl            | 他加禄语（菲律宾语）     | NotoSans-Medium.ttf               | 否          | 无           |
| sw            | 斯瓦希里语              | NotoSans-Medium.ttf               | 否          | 无           |
| hu            | 匈牙利语                | NotoSans-Medium.ttf               | 否          | 无           |
| cs            | 捷克语                  | NotoSans-Medium.ttf               | 否          | 无           |
| sk            | 斯洛伐克语              | NotoSans-Medium.ttf               | 否          | 无           |
| ro            | 罗马尼亚语              | NotoSans-Medium.ttf               | 否          | 无           |
| bg            | 保加利亚语              | NotoSans-Medium.ttf               | 否          | 无           |
| sr            | 塞尔维亚语（西里尔文）   | NotoSans-Medium.ttf               | 否          | 无           |
| hr            | 克罗地亚语              | NotoSans-Medium.ttf               | 否          | 无           |
| sl            | 斯洛文尼亚语            | NotoSans-Medium.ttf               | 否          | 无           |
| uk            | 乌克兰语                | NotoSans-Medium.ttf               | 否          | 无           |
| my            | 缅甸语                  | NotoSansMyanmar-Medium.ttf        | 否          | 无           |
| ta            | 泰米尔语                | NotoSansTamil-Medium.ttf          | 否          | 无           |
| et            | 爱沙尼亚语              | NotoSans-Medium.ttf               | 否          | 无           |

## 添加新语言

想要添加新语言？请按照贡献指南操作：

- 参见贡献说明：[贡献新语言](../CONTRIBUTING.md#contribute-a-new-language)

---

**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版本应被视为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误读，我们概不负责。