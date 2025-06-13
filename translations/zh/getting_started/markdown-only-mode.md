<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:37:09+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "zh"
}
-->
# 仅使用 Markdown 模式

## 介绍
仅使用 Markdown 模式旨在只翻译项目中的 Markdown 内容。此模式跳过图像翻译过程，专注于文本内容，适用于不需要图像翻译或未设置计算机视觉相关环境变量的场景。

## 何时使用
- 当未配置计算机视觉相关环境变量时。
- 当只想翻译文本内容而不更新图像链接时。
- 当用户通过 `-md` 命令行选项明确指定时。

## 如何启用
要启用仅使用 Markdown 模式，请在命令中使用 `-md` 选项。例如：
```
translate -l "ko" -md
```

或者当未配置计算机视觉相关环境变量时，运行 `translate -l "ko"` 会自动切换到仅使用 Markdown 模式。

```
translate -l "ko"
```

该命令将 Markdown 内容翻译成韩语，并将图像链接保持为原始路径，而不会修改为翻译后的图像路径。

## 行为
在仅使用 Markdown 模式下：
- 翻译过程跳过图像翻译步骤。
- Markdown 中的图像链接保持不变，指向其原始路径。

## 示例
### 之前
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.zh.png)
```
### 使用仅 Markdown 模式之后
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.zh.png)
```

## 故障排除
- 确保命令中正确指定了 `-md` 选项。
- 确认没有计算机视觉环境变量干扰该过程。

## 结论
仅使用 Markdown 模式提供了一种简化的方式来翻译文本内容，而不修改图像链接。它在不需要图像翻译或缺少计算机视觉环境配置的情况下尤其有用。

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。虽然我们力求准确，但请注意，自动翻译可能存在错误或不准确之处。原始文件的原文版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。