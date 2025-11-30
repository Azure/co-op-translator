<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T10:09:36+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "zh"
}
-->
# 命令参考

**Co-op Translator** CLI 提供多种选项以自定义翻译流程：

命令                                         | 说明
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 将项目翻译成指定语言。例如：translate -l "es fr de" 会翻译成西班牙语、法语和德语。使用 translate -l "all" 可翻译成所有支持的语言。
translate -l "language_codes" -u              | 更新翻译，先删除现有翻译再重新创建。警告：这会删除指定语言的所有当前翻译。
translate -l "language_codes" -img            | 仅翻译图片文件。
translate -l "language_codes" -md             | 仅翻译 Markdown 文件。
translate -l "language_codes" -nb             | 仅翻译 Jupyter 笔记本文件（.ipynb）。
translate -l "language_codes" --fix           | 根据之前的评估结果，重新翻译置信度较低的文件。
translate -l "language_codes" -d              | 启用调试模式，输出详细日志。
translate -l "language_codes" --save-logs, -s | 将 DEBUG 级别日志保存到 <root_dir>/logs/ 目录下（控制台日志仍由 -d 控制）。
translate -l "language_codes" -r "root_dir"   | 指定项目根目录。
translate -l "language_codes" -f              | 使用快速模式翻译图片（绘图速度提升最多3倍，质量和对齐略有影响）。
translate -l "language_codes" -y              | 自动确认所有提示（适用于 CI/CD 流水线）。
translate -l "language_codes" --add-disclaimer/--no-disclaimer | 启用或禁用在翻译的 Markdown 和笔记本中添加机器翻译免责声明部分（默认启用）。
translate -l "language_codes" --help          | 显示 CLI 内的帮助详情和可用命令。
evaluate -l "language_code"                  | 评估指定语言的翻译质量并提供置信度评分。
evaluate -l "language_code" -c 0.8           | 使用自定义置信度阈值评估翻译。
evaluate -l "language_code" -f               | 快速评估模式（仅基于规则，无大语言模型）。
evaluate -l "language_code" -D               | 深度评估模式（仅基于大语言模型，更全面但较慢）。
evaluate -l "language_code" --save-logs, -s  | 将 DEBUG 级别日志保存到 <root_dir>/logs/。
migrate-links -l "language_codes"             | 重新处理翻译后的 Markdown 文件，更新笔记本（.ipynb）链接。优先使用翻译后的笔记本，否则可回退到原始笔记本。
migrate-links -l "language_codes" -r          | 指定项目根目录（默认当前目录）。
migrate-links -l "language_codes" --dry-run   | 显示将要更改的文件，但不写入更改。
migrate-links -l "language_codes" --no-fallback-to-original | 当缺少翻译笔记本时，不重写为原始笔记本链接（仅在翻译笔记本存在时更新）。
migrate-links -l "language_codes" -d          | 启用调试模式，输出详细日志。
migrate-links -l "language_codes" --save-logs, -s | 将 DEBUG 级别日志保存到 <root_dir>/logs/。
migrate-links -l "all" -y                      | 处理所有语言并自动确认警告提示。

## 使用示例

  1. 默认行为（添加新翻译，不删除现有翻译）：   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 仅添加新的韩文图片翻译（不删除现有翻译）：    translate -l "ko" -img

  3. 更新所有韩文翻译（警告：这会先删除所有现有韩文翻译再重新翻译）：    translate -l "ko" -u

  4. 仅更新韩文图片（警告：这会先删除所有现有韩文图片再重新翻译）：    translate -l "ko" -img -u

  5. 仅添加韩文 Markdown 新翻译，不影响其他翻译：    translate -l "ko" -md

  6. 根据之前评估结果修正置信度低的翻译： translate -l "ko" --fix

  7. 仅修正特定文件的置信度低翻译（Markdown）： translate -l "ko" --fix -md

  8. 仅修正特定文件的置信度低翻译（图片）： translate -l "ko" --fix -img

  9. 图片翻译使用快速模式：    translate -l "ko" -img -f

  10. 使用自定义阈值修正置信度低的翻译： translate -l "ko" --fix -c 0.8

  11. 调试模式示例： - translate -l "ko" -d：启用调试日志。
  12. 保存日志到文件： translate -l "ko" -s
  13. 控制台和文件均输出 DEBUG 日志： translate -l "ko" -d -s
  14. 翻译时不添加机器翻译免责声明： translate -l "ko" --no-disclaimer

  15. 迁移韩文翻译的笔记本链接（有翻译笔记本时更新链接）：    migrate-links -l "ko"

  15. 迁移链接时进行模拟运行（不写入文件）：    migrate-links -l "ko" --dry-run

  16. 仅当翻译笔记本存在时更新链接（不回退到原始笔记本）：    migrate-links -l "ko" --no-fallback-to-original

  17. 处理所有语言并显示确认提示：    migrate-links -l "all"

  18. 处理所有语言并自动确认：    migrate-links -l "all" -y
  19. 为 migrate-links 保存日志到文件：    migrate-links -l "ko ja" -s

### 评估示例

> [!WARNING]  
> **Beta 功能**：评估功能目前处于测试阶段。该功能用于评估翻译文档，评估方法和具体实现仍在开发中，可能会有变动。

  1. 评估韩文翻译： evaluate -l "ko"

  2. 使用自定义置信度阈值评估： evaluate -l "ko" -c 0.8

  3. 快速评估（仅基于规则）： evaluate -l "ko" -f

  4. 深度评估（仅基于大语言模型）： evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->