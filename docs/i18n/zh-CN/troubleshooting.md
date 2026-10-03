# 故障排除

当翻译运行意外成功、在配置期间失败，或产生需要审阅的输出时，请使用此页面。

## 从这里开始

1. 首先运行一个有针对性的命令，例如 `translate -l "ko" -md`。
2. 添加 `-d` 以获取控制台调试日志。
3. 添加 `-s` 将调试日志保存到 `<root-dir>/logs/`。
4. 在翻译后运行 `co-op-review` 以检查新鲜度、结构和本地链接。

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## 配置错误

### 没有语言模型提供者

错误：

```text
No language model configuration found.
```

修复：

- 配置 Azure OpenAI、OpenAI 或 Anthropic。
- 验证这些变量是否在运行命令的环境中。
- 对于本地使用，请将它们放在项目根目录的 `.env` 中。

参见 [配置](configuration.md)。

### 在没有 Azure AI Vision 的情况下进行图像翻译

错误：

```text
Image translation requested but Azure AI Service is not configured.
```

修复：

- 添加 `AZURE_AI_SERVICE_API_KEY`。
- 添加 `AZURE_AI_SERVICE_ENDPOINT`。
- 或运行仅文本命令，例如 `translate -l "ko" -md`。

### 无效的密钥或端点

症状可能包括 `401`、被遮蔽的权限错误或端点访问错误。

修复：

- 确认密钥属于与端点相同的 Azure 资源。
- 使用 `-img` 时确认该资源支持 Vision。
- 确认 Azure OpenAI 的部署名称和 API 版本与您的部署匹配。
- 使用调试日志运行：`translate -l "ko" -md -d -s`。

## 没有文件被翻译

常见原因：

- 所选标志与您的文件不匹配。
- 已存在翻译后的文件。
- 源文件位于被排除的目录中。
- 命令在错误的项目根目录中运行。

检查项：

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

当命令在项目根目录之外运行时使用 `--root-dir`。

## 意外的链接行为

链接重写取决于所选内容类型：

- `-nb` 包含：笔记本链接可以指向已翻译的笔记本。
- `-nb` 排除：笔记本链接可以仍然指向源笔记本。
- `-img` 包含：图像链接可以指向已翻译的图像。
- `-img` 排除：图像链接可以仍然指向源图像。

当所有内部链接应优先指向翻译后的输出时，请运行完整内容翻译：

```bash
translate -l "ko" -md -nb -img
```

在翻译后运行链接审查：

```bash
co-op-review -l "ko"
```

## Markdown 渲染问题

如果翻译后的 Markdown 渲染不正确：

- 检查 frontmatter 是否以 `---` 开始并结束。
- 检查源文件和翻译文件之间的代码围栏数量是否匹配。
- 运行 `co-op-review` 以捕捉常见的结构问题。
- 如果输出损坏，请重新翻译该文件。

```bash
co-op-review -l "ko" --format github
```

## GitHub Action 运行但未创建拉取请求

如果 `peter-evans/create-pull-request` 报告分支没有比基线领先，则工作流未找到要提交的文件。

可能的原因：

- 翻译运行未产生更改。
- `.gitignore` 排除了 `translations/`、`translated_images/` 或翻译后的笔记本。
- `add-paths` 与生成的输出目录不匹配。
- 翻译步骤提前退出。

修复方法：

1. 确认生成的文件存在于 `translations/` 或 `translated_images/` 中。
2. 确认 `.gitignore` 未忽略生成的输出。
3. 使用匹配的 `add-paths`：

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. 暂时向 translate 命令添加调试标志：

   ```bash
   translate -l "ko" -md -d -s
   ```

5. 确认工作流权限包括：

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## 翻译质量

机器翻译可能需要人工审校。仅在你希望使用实验性的质量评分和低置信度修复工作流时使用 `evaluate`。

!!! warning "Experimental"
    `evaluate` 可以使用基于规则和基于 LLM 的检查，其评分模型和元数据行为可能会发生变化。除非你的工作流已做好应对变化的准备，否则不要将其纳入必需的 CI 检查中。

对于确定性的 CI 检查，请改用 `co-op-review`。