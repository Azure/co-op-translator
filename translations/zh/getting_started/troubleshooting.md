<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T02:27:15+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "zh"
}
-->
# Microsoft Co-op Translator 故障排查指南

## 概述
Microsoft Co-Op Translator 是一款强大的工具，可以无缝翻译 Markdown 文档。本指南将帮助你排查使用过程中常见的问题。

## 常见问题及解决方法

### 1. Markdown 标签问题
**问题：** 翻译后的 Markdown 文档顶部出现了 `markdown` 标签，导致渲染异常。

**解决方法：** 只需删除文件顶部的 `markdown` 标签，Markdown 文件即可正常渲染。

**操作步骤：**
1. 打开翻译后的 Markdown (`.md`) 文件。
2. 找到文档顶部的 `markdown` 标签。
3. 删除该标签。
4. 保存文件。
5. 重新打开文件，确认渲染正常。

### 2. 内嵌图片 URL 问题
**问题：** 内嵌图片的 URL 与语言区域不匹配，导致图片显示错误或缺失。

**解决方法：** 检查图片的 URL，确保与文档语言区域一致。所有图片都在 `translated_images` 文件夹下，每张图片的文件名都带有语言区域标识。

**操作步骤：**
1. 打开翻译后的 Markdown 文档。
2. 找到内嵌图片及其 URL。
3. 检查图片文件名中的语言区域是否与文档一致。
4. 如有需要，更新图片 URL。
5. 保存并重新打开文档，确认图片显示正常。

### 3. 翻译准确性
**问题：** 翻译内容不准确或需要进一步编辑。

**解决方法：** 仔细检查翻译后的文档，进行必要的修改以提升准确性和可读性。

**操作步骤：**
1. 打开翻译后的文档。
2. 仔细检查内容。
3. 根据需要进行修改。
4. 保存更改。

## 4. 权限错误、内容被屏蔽或 404

如果图片或文本没有被正确翻译，且在使用 -d debug 模式时遇到 401 错误，这通常是认证失败——密钥无效、过期或未绑定到正确的端点区域。

建议使用 [-d debug 开关](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) 运行 co-op translator，以进一步了解根本原因。

- **错误信息**：`Access denied due to invalid subscription key or wrong API endpoint.`
- **可能原因**：
  - 请求中的订阅密钥被屏蔽或填写错误。
  - AI 服务密钥或订阅密钥属于其他 Azure 资源（如 Translator 或 OpenAI），而不是 **Azure AI Vision** 资源。

 **资源类型**
  - 前往 [Azure Portal](https://portal.azure.com) 或 [Azure AI Foundry](https://ai.azure.com)，确保资源类型为 `Azure AI services` → `Vision`。
  - 验证密钥，确保使用的是正确的密钥。

## 5. 配置错误（新错误处理机制）

从新的选择性翻译系统开始，Co-op Translator 会在所需服务未配置时明确提示错误信息。

### 5.1. 未配置 Azure AI Service 导致图片翻译失败

**问题：** 请求了图片翻译（`-img` 标志），但 Azure AI Service 未正确配置。

**错误信息：**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**解决方法：**
1. **方案一**：配置 Azure AI Service
   - 在 `.env` 文件中添加 `AZURE_AI_SERVICE_API_KEY`
   - 在 `.env` 文件中添加 `AZURE_AI_SERVICE_ENDPOINT`
   - 验证服务可访问

2. **方案二**：移除图片翻译请求
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. 缺少必要配置

**问题：** 缺少关键的 LLM 配置。

**错误信息：**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**解决方法：**
1. 检查 `.env` 文件，确保至少有以下 LLM 配置之一：
   - **Azure OpenAI**：`AZURE_OPENAI_API_KEY` 和 `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**：`OPENAI_API_KEY`
   
   只需配置 Azure OpenAI 或 OpenAI 其中之一，无需同时配置。

### 5.3. 选择性翻译未生效

**问题：** 命令执行成功但没有文件被翻译。

**可能原因：**
- 文件类型标志（`-md`, `-img`, `-nb`）错误
- 项目中没有匹配的文件
- 目录结构不正确

**解决方法：**
1. **使用 debug 模式** 查看详细信息：
   ```bash
   translate -l "ko" -md -d
   ```

2. **检查项目中的文件类型**：
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **核查标志组合**：
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. 旧系统迁移

### 6.1. Markdown-only 模式已废弃

**问题：** 依赖自动 markdown-only 回退的命令不再按预期工作。

**旧行为：**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**新行为：**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**解决方法：**
- **明确指定**需要翻译的内容：
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. 链接行为异常

**问题：** 翻译后的文件中的链接指向了意外的位置。

**原因：** 动态链接处理会根据选择的文件类型发生变化。

**解决方法：**
1. **了解新的链接行为**：
   - 包含 `-nb`：笔记本链接指向翻译后的版本
   - 不含 `-nb`：笔记本链接指向原始文件
   - 包含 `-img`：图片链接指向翻译后的版本
   - 不含 `-img`：图片链接指向原始文件

2. **根据实际需求选择合适的组合**：
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action 执行但未创建 Pull Request (PR)

**现象：** `peter-evans/create-pull-request` 的工作流日志显示：

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**可能原因：**
- **未检测到变更：** 翻译步骤没有产生差异（仓库已是最新）。
- **输出被忽略：** `.gitignore` 排除了你希望提交的文件（如 `*.ipynb`, `translations/`, `translated_images/`）。
- **add-paths 不匹配：** 提供给 action 的路径与实际输出位置不符。
- **工作流逻辑/条件：** 翻译步骤提前退出或写入了意外的目录。

**如何修复/验证：**
1. **确认输出文件存在：** 翻译后，检查工作区是否有 `translations/` 和/或 `translated_images/` 下的新/变更文件。
   - 如果翻译笔记本，确保 `.ipynb` 文件实际写入到 `translations/<lang>/...` 下。
2. **检查 `.gitignore`：** 不要忽略生成的输出。确保没有忽略：
   - `translations/`
   - `translated_images/`
   - `*.ipynb`（如翻译笔记本）
3. **确保 add-paths 与输出匹配：** 使用多行值，必要时同时包含两个文件夹：
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **调试时强制创建 PR：** 临时允许空提交，确认流程是否正确：
   ```yaml
   with:
     commit-empty: true
   ```
5. **使用 debug 模式运行：** 在翻译命令中加 `-d`，打印发现和写入的文件。
6. **权限（GITHUB_TOKEN）：** 确保工作流有写入权限，可创建提交和 PR：
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## 快速排查清单

排查翻译问题时：

1. **使用 debug 模式**：加 `-d` 标志查看详细日志
2. **检查命令标志**：确保 `-md`, `-img`, `-nb` 与实际需求一致
3. **核查配置文件**：`.env` 文件中有必要的密钥
4. **逐步测试**：先只用 `-md`，再逐步添加其他类型
5. **检查文件结构**：确保源文件存在且可访问

如需了解更多命令和参数，请参阅 [命令参考](./command-reference.md)。

---

**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版本应被视为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误读，我们概不负责。