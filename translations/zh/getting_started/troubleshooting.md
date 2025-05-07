<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-05-06T17:49:53+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "zh"
}
-->
# Microsoft Co-op Translator 故障排除指南


## 概述
Microsoft Co-Op Translator 是一个强大的工具，可以无缝翻译 Markdown 文档。本指南将帮助您解决使用该工具时遇到的常见问题。

## 常见问题及解决方案

### 1. Markdown 标签问题
**问题：** 翻译后的 Markdown 文档顶部包含 `markdown` 标签，导致渲染异常。

**解决方案：** 只需删除文件顶部的 `markdown` 标签，即可让 Markdown 文件正常渲染。

**步骤：**
1. 打开翻译后的 Markdown (`.md`) 文件。
2. 找到文档顶部的 `markdown` 标签。
3. 删除该 `markdown` 标签。
4. 保存文件。
5. 重新打开文件，确认渲染正常。

### 2. 嵌入图片 URL 问题
**问题：** 嵌入图片的 URL 与语言区域不匹配，导致图片显示错误或缺失。

**解决方案：** 检查嵌入图片的 URL，确保其语言区域与文档匹配。所有图片均存放在 `translated_images` 文件夹中，且图片文件名中包含语言区域标签。

**步骤：**
1. 打开翻译后的 Markdown 文档。
2. 找出嵌入的图片及其 URL。
3. 确认图片文件名中的语言区域标签与文档语言一致。
4. 如有需要，更新图片 URL。
5. 保存更改并重新打开文档，确认图片正常显示。

### 3. 翻译准确性
**问题：** 翻译内容不准确或需要进一步编辑。

**解决方案：** 审核翻译文档，进行必要的修改以提升准确性和可读性。

**步骤：**
1. 打开翻译文档。
2. 认真审核内容。
3. 进行必要的修改，提升翻译质量。
4. 保存更改。

### 4. 文件格式问题
**问题：** 翻译后的文档格式不正确，可能发生在表格中，后续的 ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` 将解决表格相关问题。

**步骤：**
1. 打开翻译文档。
2. 与原始文档对比，找出格式问题。
3. 调整格式，使其与原文一致。
4. 保存更改。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文件应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。