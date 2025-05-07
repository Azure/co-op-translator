<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-05-06T17:40:44+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "zh"
}
-->
# 命令参考
**Co-op Translator** CLI 提供多种选项来自定义翻译流程：

命令                                         | 说明
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 将项目翻译成指定语言。例如：translate -l "es fr de" 会翻译成西班牙语、法语和德语。使用 translate -l "all" 可翻译成所有支持的语言。
translate -l "language_codes" -u              | 通过删除现有翻译并重新创建来更新翻译。警告：这会删除指定语言的所有现有翻译。
translate -l "language_codes" -img            | 仅翻译图片文件。
translate -l "language_codes" -md             | 仅翻译 Markdown 文件。
translate -l "language_codes" -chk            | 检查翻译文件是否有错误，必要时重试翻译。
translate -l "language_codes" -d              | 启用调试模式，输出详细日志。
translate -l "language_codes" -r "root_dir"   | 指定项目的根目录。
translate -l "language_codes" -f              | 使用快速模式翻译图片（绘制速度最高可达3倍，质量和对齐略有影响）。
translate -l "language_codes" -y              | 自动确认所有提示（适用于 CI/CD 流水线）。
translate -l "language_codes" --help          | 显示 CLI 内的帮助详情及可用命令。

### 使用示例：

  1. 默认行为（添加新翻译，不删除现有翻译）：   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 仅添加新的韩语图片翻译（不删除现有翻译）：    translate -l "ko" -img

  3. 更新所有韩语翻译（警告：这会先删除所有现有韩语翻译，再重新翻译）：    translate -l "ko" -u

  4. 仅更新韩语图片（警告：这会先删除所有现有韩语图片，再重新翻译）：    translate -l "ko" -img -u

  5. 仅添加韩语 Markdown 新翻译，不影响其他翻译：    translate -l "ko" -md

  6. 检查翻译文件是否有错误，必要时重试翻译： translate -l "ko" -chk

  7. 检查翻译文件是否有错误，必要时重试（仅限 Markdown）： translate -l "ko" -chk -md

  8. 检查翻译文件是否有错误，必要时重试（仅限图片）： translate -l "ko" -chk -img

  9. 图片翻译使用快速模式：    translate -l "ko" -img -f

  10. 调试模式示例： - translate -l "ko" -d：启用调试日志。

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意自动翻译可能存在错误或不准确之处。原始语言版本的文件应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而引起的任何误解或误释，我们不承担任何责任。