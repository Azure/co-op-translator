# 为语言改进做贡献

您的语言知识可以帮助改进 Co-op Translator。请通过使用[翻译反馈表单](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml) 提交示例、建议的更正和说明开始。您不需要编写代码或为模型运行付费。

## 从报告到共享改进

1. 贡献者提供原文片段、其翻译和上下文。
2. 语言审阅者检查含义、自然程度，以及建议是否依赖于特定的地区或课程。
3. 维护者决定该修复是属于源课程、共享语言指令、术语配置，还是翻译代码。
4. 对于共享规则，维护者在报告的示例和不相关示例上比较更改前后的输出。贡献者可以在不自己运行工具的情况下审查这些输出。
5. 生成的 PR 会链接该报告并署名提供示例和审阅的人。部署或在使用仓库中重新生成是一个单独的步骤。

报告不会自动更改提示或重新生成课程翻译。特定课程的更正应保持与课程仓库的关联。不要假设手动编辑在之后的重新翻译中会保留；请确认该工作流的行为。

## 现有示例：日语 Markdown 链接

The [日语说明文件](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) 告诉模型在保留 Markdown 语法和链接目标的同时翻译链接文本。例如，写作 `[text](URL)` 的链接不得变为 `「text」（URL）`。

这是一个通过正确与错误输出示例支撑的有针对性的语言规则示例。它并不能证明仅靠提示说明就能保证正确的 Markdown。

The [Markdown prompt builder](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) 加载 `templates/language/<language_code>.md`，使用小写并去掉空白的语言代码。如果没有该文件，则使用通用说明。这描述了 Markdown 提示的路径；不要假设每个图像或其他翻译路径都使用相同的说明。

The [prompt tests](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) 检查是否包含日语说明。这验证的是提示组装，而非翻译质量。

## 语言规则应包含什么？

提出一个狭窄且可重复的更正，附带原文示例、期望行为以及规则不应适用的反例。保留含义、占位符、代码、URL 和文档结构。避免将某个人的风格偏好或某门课程的术语变成普适规则。

当前的 [术语表实现](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) 可防止术语被翻译。它并不是一个源到目标的术语词典。在向贡献者承诺新术语行为之前，请先讨论该行为。

## 社区示例：日语产品名称报告

在[报告 #527](https://github.com/Azure/co-op-translator/issues/527) 中，@hyoshioka0128 发现一个日文翻译将产品名称 `Co-op Translator` 改为 `Co-op 翻訳`。该报告包含受影响文档的链接和截图，使问题易于定位。

贡献者还链接了[相关课程的 PR](https://github.com/microsoft/AZD-for-beginners/pull/109)。在问题讨论中，维护者已确认该报告并提议调查名称变化的原因，包括术语保护、术语表行为以及翻译路径。

这展示了一个小报告如何支持超出单个措辞更正的调查。这并不是经验证的前后结果，也不是证据表明上述日语 Markdown 链接说明修复了此产品名称问题。

您可以以相同方式做出贡献：分享原文、当前翻译、建议的更正以及其重要性。在有用时添加文档链接或截图。您无需在报告前诊断原因或编写提示。

## 采纳规则前的验证

在基线和候选运行中使用相同的源样本、译者修订、提供者/模型和生成设置，只更改建议的指令。记录实际的提示更改和输出；在需要时重复示例以区分一致的效果与输出变异性。包括报告的失败、对比上下文以及已正确翻译的示例。

| 样本 | 来源/上下文 | 基线输出 | 候选输出 | 审阅者评估 |
| --- | --- | --- | --- | --- |
| 报告的失败 | 待收集 | 未运行 | 未运行 | 待定 |
| 反例 | 待收集 | 未运行 | 未运行 | 待定 |
| 不受影响的示例 | 待收集 | 未运行 | 未运行 | 待定 |

分开检查结构不变量与语言判断。成功的提示加载测试并不是质量评估，而且一条完全匹配的期望句子并非唯一有效翻译。如果缺少上下文、模型运行或语言审阅，请将提案保持待定，而不是声称问题已解决。