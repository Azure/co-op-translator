# 翻译、编辑并审阅一个小项目

从两个简短的 Markdown 文件和一种目标语言开始。你将看到翻译写在哪里、当源文件更改时会发生什么，以及如何检查结果。

## 记录的结果

该示例于2026年9月19日使用 Co-op Translator 0.21.0 和 Azure OpenAI（`gpt-5-mini`）运行。未经修改的 CLI 命令通过 Click 的 `CliRunner` 调用，使用构建的 wheel 和现有的 Python 依赖项。

| 步骤 | 结果 |
| --- | --- |
| 预览 | 退出 0；未请求模型翻译 |
| 初始翻译 | 退出 0；27.36 秒 |
| 初始审阅 | 退出 0 |
| 编辑 README 并审阅 | 退出 1；检测到陈旧的翻译 |
| 更新翻译 | 退出 0；22.17 秒 |
| 更新后审阅 | 退出 0；无错误或警告 |
| 未更改的指南 | 在 README 更新前后字节相同 |
| 再次运行 | 退出 0；所有翻译文件哈希相同 |

这些是单次运行的测量值，不是性能保证。未计入设置时间；未测量提供商计费。未更改的运行仍可能执行提供商健康检查。

检查 [初始翻译](../../assets/demo/before.txt)、[更新后的翻译](../../assets/demo/after.txt)、[完整翻译差异](../../assets/demo/update.diff)、[陈旧的审阅](../../assets/demo/review-stale.txt)、[最终审阅](../../assets/demo/review-after.txt) 和 [运行详情](../../assets/demo/results.json)。完整文件的翻译可能会更改其他措辞，如所捕获的差异所示。两个文本工件均保留生成的免责声明。

人工审阅仍然很重要：捕获的更新使用了 `[사용 가이드](guide.md)을`；正确的韩语助词应为 `[사용 가이드](guide.md)를`。文本工件保留了该输出的原样，而不是将编辑后的翻译作为模型输出呈现。尽管存在此措辞问题，结构性审查仍然通过。

## 1. 准备一个小文件夹

使用 Python 3.11–3.14 和 [虚拟环境设置](configuration.md#local-runtime-setup)。安装本示例使用的版本：

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

将 [README.txt](../../assets/demo/README.txt) 和 [guide.txt](../../assets/demo/guide.txt) 下载到此文件夹，保存为 `README.md` 和 `guide.md`。它们是小型虚构项目文档；无需安装应用程序。

README 包含一个代码块并链接到 `guide.md`。其最后一句是：

```text
Notes are saved locally.
```

在此文件夹中仅保留这两个源文档。所有后续命令都在 `translation-demo` 内运行，并在 Bash 和 PowerShell 中可用。

## 2. 在无凭据情况下预览

```bash
translate -l "ko" -md --dry-run
```

预览会估算翻译工作量，而不会调用模型或写入翻译。令牌估算不是计费报价。第一次运行应将两个 Markdown 文件识别为新任务。

## 3. 选择提供商并翻译

使用 [配置指南](configuration.md) 配置一个提供商：Azure OpenAI、OpenAI 或 Anthropic。OpenAI 和 Anthropic 的文本翻译不需要 Azure 帐户。本示例不需要图像服务。

如果使用本地 `.env` 文件，请将 `.env` 添加到此文件夹的 `.gitignore` 中。翻译调用使用您的提供商账户，可能会产生费用。

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

打开 `translations/ko/README.md` 和 `translations/ko/guide.md`。检查韩语用词、代码块以及从翻译后的 README 到翻译后 guide 的链接。输出措辞会因模型而异。

`co-op-review` 会检查新鲜度、结构和本地链接。通过的结果并不保证语言准确性。在继续之前请解决任何报告的错误。

使用 Git 记录成功的基线（如有需要，先配置您的 Git 身份）：

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. 更改源文件

在 `README.md` 中，将 `Notes are saved locally.` 替换为：

```text
Notes are saved locally as Markdown files.
```

保持 `guide.md` 不变。然后运行：

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

审阅应报告 README 翻译为过时并以失败状态退出。这是预期的中间状态。预览应识别出已更改 README 的工作。

## 5. 更新并检查差异

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

检查实际差异：默认 CLI 会重新翻译已更改的文件，因此模型也可能修改该文件中的其他措辞。未更改的 guide 应该没有差异。审阅不应再报告 README 为过时；请调查其他任何发现，而不是忽略它们。

要在块级保留人工 Markdown 编辑，需要在 [Python API](api.md) 中使用可选的翻译状态提供程序。此功能不由这些 CLI 命令启用。

## 6. 在不更改的情况下再次运行

提交已更新的源文件和翻译：

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

在当前翻译和未更改的配置下，翻译器会跳过这些文件。最后的 Git 命令应该不产生差异并成功退出。

## 后续步骤

- [仅翻译 README 并打开一个拉取请求](github-actions.md#your-first-readme-translation-pr).
- [选择 CLI、Python API 或 MCP](workflows.md).
- [在不编写代码的情况下报告翻译问题](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).