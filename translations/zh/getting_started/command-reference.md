<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T02:26:48+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "zh"
}
-->
# 命令参考

**Co-op Translator** 命令行工具提供了多种选项，可自定义翻译流程：

命令                                       | 说明
--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"               | 将你的项目翻译为指定语言。例如：translate -l "es fr de" 会翻译为西班牙语、法语和德语。使用 translate -l "all" 可翻译为所有支持的语言。
translate -l "language_codes" -u            | 更新翻译，删除现有翻译并重新生成。警告：这会删除指定语言的所有当前翻译。
translate -l "language_codes" -img          | 仅翻译图片文件。
translate -l "language_codes" -md           | 仅翻译 Markdown 文件。
translate -l "language_codes" -nb           | 仅翻译 Jupyter notebook 文件（.ipynb）。
translate -l "language_codes" --fix         | 根据之前的评估结果，重新翻译置信度较低的文件。
translate -l "language_codes" -d            | 启用调试模式，输出详细日志。
translate -l "language_codes" --save-logs, -s | 将 DEBUG 级别日志保存到 <root_dir>/logs/ 目录下（控制台日志仍由 -d 控制）
translate -l "language_codes" -r "root_dir" | 指定项目根目录
translate -l "language_codes" -f            | 图片翻译使用快速模式（绘图速度提升至 3 倍，质量和对齐略有下降）。
translate -l "language_codes" -y            | 自动确认所有提示（适用于 CI/CD 流水线）
translate -l "language_codes" --help        | 在 CLI 内显示可用命令的帮助信息
evaluate -l "language_code"                 | 评估指定语言的翻译质量，并给出置信度分数
evaluate -l "language_code" -c 0.8          | 使用自定义置信度阈值评估翻译
evaluate -l "language_code" -f              | 快速评估模式（仅基于规则，无 LLM）
evaluate -l "language_code" -D              | 深度评估模式（仅基于 LLM，更全面但速度较慢）
evaluate -l "language_code" --save-logs, -s | 将 DEBUG 级别日志保存到 <root_dir>/logs/
migrate-links -l "language_codes"           | 重新处理已翻译的 Markdown 文件，更新指向 notebook（.ipynb）的链接。优先使用已翻译的 notebook，如无则可回退到原始 notebook。
migrate-links -l "language_codes" -r        | 指定项目根目录（默认：当前目录）。
migrate-links -l "language_codes" --dry-run | 仅显示哪些文件会被更改，不实际写入更改。
migrate-links -l "language_codes" --no-fallback-to-original | 当缺少已翻译的 notebook 时，不回退到原始 notebook（仅在有翻译时更新链接）。
migrate-links -l "language_codes" -d        | 启用调试模式，输出详细日志。
migrate-links -l "language_codes" --save-logs, -s | 将 DEBUG 级别日志保存到 <root_dir>/logs/
migrate-links -l "all" -y                   | 处理所有语言并自动确认警告提示。

## 使用示例

  1. 默认行为（添加新翻译，不删除已有翻译）：   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 仅新增韩语图片翻译（不删除已有翻译）：    translate -l "ko" -img

  3. 更新所有韩语翻译（警告：此操作会先删除所有已有韩语翻译再重新翻译）：    translate -l "ko" -u

  4. 仅更新韩语图片（警告：此操作会先删除所有已有韩语图片再重新翻译）：    translate -l "ko" -img -u

  5. 仅新增韩语 Markdown 翻译，不影响其他翻译：    translate -l "ko" -md

  6. 根据之前的评估结果修复置信度低的翻译： translate -l "ko" --fix

  7. 仅修复特定文件的低置信度翻译（Markdown）： translate -l "ko" --fix -md

  8. 仅修复特定文件的低置信度翻译（图片）： translate -l "ko" --fix -img

  9. 图片翻译使用快速模式：    translate -l "ko" -img -f

  10. 使用自定义阈值修复低置信度翻译： translate -l "ko" --fix -c 0.8

  11. 调试模式示例： - translate -l "ko" -d: 启用调试日志。
  12. 日志保存到文件： translate -l "ko" -s
  13. 控制台和文件同时输出 DEBUG 日志： translate -l "ko" -d -s

  14. 为韩语翻译迁移 notebook 链接（有翻译时更新为翻译版）：    migrate-links -l "ko"

  15. 迁移链接但不写入文件（dry-run）：    migrate-links -l "ko" --dry-run

  16. 仅在有已翻译 notebook 时更新链接（不回退到原始 notebook）：    migrate-links -l "ko" --no-fallback-to-original

  17. 处理所有语言并弹出确认提示：    migrate-links -l "all"

  18. 处理所有语言并自动确认：    migrate-links -l "all" -y
  19. migrate-links 日志保存到文件：    migrate-links -l "ko ja" -s

### 评估示例

> [!WARNING]  
> **Beta 功能**：评估功能目前为测试版。该功能用于评估已翻译文档，评估方法和具体实现仍在开发中，未来可能会有变动。

  1. 评估韩语翻译： evaluate -l "ko"

  2. 使用自定义置信度阈值评估： evaluate -l "ko" -c 0.8

  3. 快速评估（仅基于规则）： evaluate -l "ko" -f

  4. 深度评估（仅基于 LLM）： evaluate -l "ko" -D

---

**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译。我们尽力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言版本应被视为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误读，我们概不负责。