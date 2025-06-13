<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4ed48f23ec418b31e90a02fe629fcde",
  "translation_date": "2025-06-12T12:03:44+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "zh"
}
-->
# 支持的语言

下表列出了**Co-op Translator**当前支持的语言。表中包含语言代码、语言名称以及每种语言的已知问题。如果您想添加对新语言的支持，请在位于`src/co_op_translator/fonts/`的`font_language_mappings.yml`文件中添加相应的语言代码、名称和合适的字体，并在测试后提交拉取请求。

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | 英语                 | NotoSans-Medium.ttf               | 否          | 无           |
| fr            | 法语                 | NotoSans-Medium.ttf               | 否          | 无           |
| es            | 西班牙语             | NotoSans-Medium.ttf               | 否          | 无           |
| de            | 德语                 | NotoSans-Medium.ttf               | 否          | 无           |
| ru            | 俄语                 | NotoSans-Medium.ttf               | 否          | 无           |
| ar            | 阿拉伯语             | NotoSansArabic-Medium.ttf         | 是          | 无           |
| fa            | 波斯语（法尔西语）   | NotoSansArabic-Medium.ttf         | 否          | 无           |
| ur            | 乌尔都语             | NotoSansArabic-Medium.ttf         | 否          | 无           |
| zh            | 中文（简体）         | NotoSansCJK-Medium.ttc            | 否          | 无           |
| mo            | 中文（繁体，澳门）    | NotoSansCJK-Medium.ttc            | 否          | 无           |
| hk            | 中文（繁体，香港）    | NotoSansCJK-Medium.ttc            | 否          | 无           |
| tw            | 中文（繁体，台湾）    | NotoSansCJK-Medium.ttc            | 否          | 无           |
| ja            | 日语                 | NotoSansCJK-Medium.ttc            | 否          | 无           |
| ko            | 韩语                 | NotoSansCJK-Medium.ttc            | 否          | 无           |
| hi            | 印地语               | NotoSansDevanagari-Medium.ttf     | 否          | 无           |
| bn            | 孟加拉语             | NotoSansBengali-Medium.ttf        | 否          | 无           |
| mr            | 马拉地语             | NotoSansDevanagari-Medium.ttf     | 否          | 无           |
| ne            | 尼泊尔语             | NotoSansDevanagari-Medium.ttf     | 否          | 无           |
| pa            | 旁遮普语（古鲁姆克希体）| NotoSansGurmukhi-Medium.ttf     | 否          | 无           |
| pt            | 葡萄牙语（葡萄牙）   | NotoSans-Medium.ttf               | 否          | 无           |
| br            | 葡萄牙语（巴西）     | NotoSans-Medium.ttf               | 否          | 无           |
| it            | 意大利语             | NotoSans-Medium.ttf               | 否          | 无           |
| pl            | 波兰语               | NotoSans-Medium.ttf               | 否          | 无           |
| tr            | 土耳其语             | NotoSans-Medium.ttf               | 否          | 无           |
| el            | 希腊语               | NotoSans-Medium.ttf               | 否          | 无           |
| th            | 泰语                 | NotoSansThai-Medium.ttf           | 否          | 无           |
| sv            | 瑞典语               | NotoSans-Medium.ttf               | 否          | 无           |
| da            | 丹麦语               | NotoSans-Medium.ttf               | 否          | 无           |
| no            | 挪威语               | NotoSans-Medium.ttf               | 否          | 无           |
| fi            | 芬兰语               | NotoSans-Medium.ttf               | 否          | 无           |
| nl            | 荷兰语               | NotoSans-Medium.ttf               | 否          | 无           |
| he            | 希伯来语             | NotoSansHebrew-Medium.ttf         | 否          | 无           |
| vi            | 越南语               | NotoSans-Medium.ttf               | 否          | 无           |
| id            | 印度尼西亚语         | NotoSans-Medium.ttf               | 否          | 无           |
| ms            | 马来语               | NotoSans-Medium.ttf               | 否          | 无           |
| tl            | 他加禄语（菲律宾语） | NotoSans-Medium.ttf               | 否          | 无           |
| sw            | 斯瓦希里语           | NotoSans-Medium.ttf               | 否          | 无           |
| hu            | 匈牙利语             | NotoSans-Medium.ttf               | 否          | 无           |
| cs            | 捷克语               | NotoSans-Medium.ttf               | 否          | 无           |
| sk            | 斯洛伐克语           | NotoSans-Medium.ttf               | 否          | 无           |
| ro            | 罗马尼亚语           | NotoSans-Medium.ttf               | 否          | 无           |
| bg            | 保加利亚语           | NotoSans-Medium.ttf               | 否          | 无           |
| sr            | 塞尔维亚语（西里尔字母）| NotoSans-Medium.ttf           | 否          | 无           |
| hr            | 克罗地亚语           | NotoSans-Medium.ttf               | 否          | 无           |
| sl            | 斯洛文尼亚语         | NotoSans-Medium.ttf               | 否          | 无           |
| uk            | 乌克兰语             | NotoSans-Medium.ttf               | 否          | 无           |
| my            | 缅甸语（缅甸）       | NotoSans-Medium.ttf               | 否          | 无           |

## 添加新语言

要添加对新语言的支持：

1. 访问 [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml)。
2. 添加语言代码、名称和对应的字体文件名。如果语言是从右到左，请确保包含`rtl`属性。
3. 如果需要使用新字体，请确认该字体在开源项目中免费使用，检查其许可和版权条款。确认无误后，将字体文件添加到`src/co_op_translator/fonts/`目录。
4. 在本地测试更改，确保新语言得到正确支持。
5. 提交包含更改的拉取请求，并在PR描述中注明添加了新语言。

示例：

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。