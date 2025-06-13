<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:23:14+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "zh"
}
-->
# Microsoft Co-op Translator 故障排除指南


## 概述
Microsoft Co-Op Translator 是一个强大的工具，能够无缝翻译 Markdown 文档。本指南将帮助你解决使用该工具时常见的问题。

## 常见问题及解决方案

### 1. Markdown 标签问题
**问题：** 翻译后的 Markdown 文档顶部包含 `markdown` 标签，导致渲染异常。

**解决方案：** 只需删除文件顶部的 `markdown` 标签，即可使 Markdown 文件正确渲染。

**步骤：**
1. 打开翻译后的 Markdown (`.md`) 文件。
2. 找到文档顶部的 `markdown` 标签。
3. 删除该 `markdown` 标签。
4. 保存文件更改。
5. 重新打开文件，确认渲染正常。

### 2. 嵌入图片 URL 问题
**问题：** 嵌入图片的 URL 与语言区域不匹配，导致图片显示错误或缺失。

**解决方案：** 检查嵌入图片的 URL，确保其语言区域与文档一致。所有图片都存放在 `translated_images` 文件夹中，每张图片的文件名都带有语言区域标签。

**步骤：**
1. 打开翻译后的 Markdown 文档。
2. 找出所有嵌入的图片及其 URL。
3. 确认图片文件名中的语言区域标签与文档语言匹配。
4. 如有必要，更新图片 URL。
5. 保存更改并重新打开文档，确认图片正确显示。

### 3. 翻译准确性
**问题：** 翻译内容不准确或需要进一步修改。

**解决方案：** 认真审阅翻译文档，进行必要的编辑以提升准确性和可读性。

**步骤：**
1. 打开翻译文档。
2. 仔细审阅内容。
3. 根据需要修改，提升翻译准确度。
4. 保存更改。

### 4. 文件格式问题
**问题：** 翻译文档的格式不正确，例如表格格式有误。这里额外的 ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` 可以解决表格相关的问题。

**步骤：**
1. 打开翻译文档。
2. 将其与原始文档进行对比，找出格式问题。
3. 调整格式，使其与原始文档保持一致。
4. 保存更改。

**免责声明**：  
本文件使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于关键信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。