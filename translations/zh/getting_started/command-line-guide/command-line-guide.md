<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d8eec418d6325416b9fab19a2dfcbf41",
  "translation_date": "2025-05-06T17:51:59+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "zh"
}
-->
# 如何使用 Co-op Translator 命令行界面 (CLI)

## 前提条件

- **Python 3.10 或更高版本**：运行 Co-op Translator 所必需。
- **语言模型资源**：
  - **Azure OpenAI** 或其他大型语言模型。详情请参阅 [supported models and services](../../../../README.md)。
- **计算机视觉资源**（可选）：
  - 用于图像翻译。如果不可用，翻译器将默认使用 [Markdown-only mode](../markdown-only-mode.md)。
  - **Azure Computer Vision**

### 初始设置

开始之前，请确保完成以下资源的配置：

- [设置 Azure OpenAI](../set-up-resources/set-up-azure-openai.md)
- [设置 Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md)（可选）

## 目录

1. [在根目录创建 '.env' 文件](./create-env-file.md)
   - 包含所选语言模型服务所需的密钥。
   - 如果省略 Azure Computer Vision 密钥或指定了 `-md`，翻译器将以 Markdown-only mode 运行。
3. [安装 Co-op translator 包](./install-package.md)
4. [使用 Co-op Translator 翻译你的项目](./translator-your-project.md)

**免责声明**：  
本文件由AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)翻译而成。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。