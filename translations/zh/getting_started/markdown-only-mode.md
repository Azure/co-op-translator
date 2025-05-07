<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-05-06T17:43:24+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "zh"
}
-->
# 仅使用 Markdown 模式

## 介绍
仅使用 Markdown 模式旨在只翻译项目中的 Markdown 内容。此模式跳过图像翻译过程，专注于文本内容，适用于不需要图像翻译或未设置计算机视觉相关环境变量的场景。

## 何时使用
- 当未配置计算机视觉相关的环境变量时。
- 当只想翻译文本内容而不更新图像链接时。
- 当用户通过 `-md` 命令行选项明确指定时。

## 如何启用
要激活仅使用 Markdown 模式，请在命令中使用 `-md` 选项。例如：
```
translate -l "ko" -md
```

或者如果未配置计算机视觉相关的环境变量，运行 `translate -l "ko"` 会自动切换到仅使用 Markdown 模式。

```
translate -l "ko"
```

此命令将 Markdown 内容翻译成韩语，并将图像链接保持为原始路径，而不是修改为翻译后的图像路径。

## 行为
在仅使用 Markdown 模式下：
- 翻译过程会跳过图像翻译步骤。
- Markdown 中的图像链接保持不变，指向原始路径。

## 示例
### 之前
```markdown
![Image](../../../getting_started/translated/path/to/image.png)
```
### 使用仅 Markdown 模式后的结果
```markdown
![Image](../../../getting_started/original/path/to/image.png)
```

## 故障排除
- 确保命令中正确指定了 `-md` 选项。
- 确认没有计算机视觉相关的环境变量影响该过程。

## 结论
仅使用 Markdown 模式提供了一种简化的方式来翻译文本内容，而不修改图像链接。当不需要图像翻译或在缺乏计算机视觉环境的情况下工作时，这种模式尤其有用。

**免责声明**：  
本文件使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们不承担任何责任。