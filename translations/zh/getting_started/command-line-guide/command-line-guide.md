<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5eb9b53c81804f04bc9456160e79940",
  "translation_date": "2025-05-07T14:00:41+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "zh"
}
-->
# 如何使用 Co-op Translator 命令行界面（CLI）

## 前提条件

- **Python 3.10 或更高版本**：运行 Co-op Translator 所需。
- **语言模型资源**：  
  - **Azure OpenAI** 或其他大型语言模型。详细信息请参见 [supported models and services](../../../../README.md)。
- **计算机视觉资源**（可选）：  
  - 用于图像翻译。如果不可用，翻译器将默认使用 [Markdown-only mode](../markdown-only-mode.md)。  
  - **Azure Computer Vision**

## 目录

1. [在根目录创建 '.env' 文件](./create-env-file.md)  
   - 包含所选语言模型服务所需的密钥。  
   - 如果省略 Azure Computer Vision 密钥或指定了 `-md`，翻译器将以 Markdown-only 模式运行。  
1. [安装 Co-op translator 包](./install-package.md)  
1. [使用 Co-op Translator 翻译你的项目](./translator-your-project.md)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。