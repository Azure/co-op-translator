<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:37:35+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "zh"
}
-->
# 更新“其他课程”部分（Microsoft 初学者仓库）

本指南介绍如何使用 Co-op Translator 实现“其他课程”部分的自动同步，以及如何更新所有仓库的全局模板。

- 适用范围：仅限 Microsoft 初学者仓库
- 适用工具：Co-op Translator CLI 和 GitHub Actions
- 模板来源：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## 快速开始：在你的仓库中启用自动同步

在 README 中“其他课程”部分的前后添加以下标记。Co-op Translator 会在每次运行时替换这两个标记之间的所有内容。

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

每次 Co-op Translator 运行时——无论是通过 CLI（例如 `translate -l "<language codes>"`）还是 GitHub Actions——都会自动更新被这些标记包裹的“其他课程”部分。

> [!NOTE]
> 如果你已有现成的列表，只需用相同的标记包裹起来。下一次运行时，它会被最新的标准化内容替换。

---

## 如何更改全局内容

如果你想更新所有初学者仓库中统一显示的标准化内容：

1. 编辑模板文件：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. 向 Co-op Translator 仓库提交包含你更改的拉取请求
3. PR 合并后，Co-op Translator 版本将被更新
4. 下一次 Co-op Translator 在目标仓库中运行（无论是 CLI 还是 GitHub Action）时，会自动同步更新后的内容

这样可以确保所有初学者仓库中的“其他课程”内容保持统一的权威来源。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。虽然我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->