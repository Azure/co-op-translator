# 故障排除

Use this page when a translation run succeeds unexpectedly, fails during configuration, or produces output that needs review.

## 从这里开始

1. 首先运行一个针对性的命令，例如 `translate -l "ko" -md`。
2. 添加 `-d` 以启用控制台调试日志。
3. 添加 `-s` 将调试日志保存到 `<root-dir>/logs/` 下。
4. 翻译后运行 `co-op-review` 以检查新鲜度、结构和本地链接。

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

- 配置 Azure OpenAI 或 OpenAI。
- 确认这些变量存在于运行命令的环境中。
- 在本地使用时，将它们放在项目根目录的 `.env` 中。

参见 [配置](configuration.md)。

### 在没有 Azure AI Vision 的情况下进行图像翻译

错误：

```text
Image translation requested but Azure AI Service is not configured.
```

修复：

- 添加 `AZURE_AI_SERVICE_API_KEY`。
- 添加 `AZURE_AI_SERVICE_ENDPOINT`。
- 或者运行仅文本的命令，例如 `translate -l "ko" -md`。

### 密钥或端点无效

症状可能包括 `401`、权限错误（被屏蔽）或端点访问错误。

修复：

- 确认该密钥属于与端点相同的 Azure 资源。
- 在使用 `-img` 时确认该资源支持 Vision。
- 确认 Azure OpenAI 部署名称和 API 版本与您的部署匹配。
- 使用调试日志运行：`translate -l "ko" -md -d -s`。

## 没有文件被翻译

常见原因：

- 所选标志与您的文件不匹配。
- 已存在已翻译的文件。
- 源文件位于被排除的目录下。
- 命令从错误的项目根目录运行。

检查：

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

当命令在项目根目录之外运行时，使用 `--root-dir`。

## 意外的链接行为

链接重写取决于所选的内容类型：

- `-nb` 已包含：笔记本链接可以指向已翻译的笔记本。
- `-nb` 被排除：笔记本链接可以保持指向源笔记本。
- `-img` 已包含：图片链接可以指向已翻译的图片。
- `-img` 被排除：图片链接可以保持指向源图片。

当所有内部链接都应优先指向翻译后的输出时，运行完整内容翻译：

```bash
translate -l "ko" -md -nb -img
```

翻译后运行链接审查：

```bash
co-op-review -l "ko"
```

## Markdown 渲染问题

如果翻译后的 Markdown 渲染不正确：

- 检查 frontmatter 是否以 `---` 开始和结束。
- 检查代码块围栏数量在源文件和翻译文件之间是否匹配。
- 运行 `co-op-review` 以捕捉常见结构问题。
- 如果输出被损坏，请重新翻译该特定文件。

```bash
co-op-review -l "ko" --format github
```

## GitHub Action 已运行但未创建 Pull Request

如果 `peter-evans/create-pull-request` 报告该分支没有领先于基线，则工作流未找到可提交的文件。

可能原因：

- 翻译运行未产生任何更改。
- `.gitignore` 排除了 `translations/`、`translated_images/` 或已翻译的笔记本。
- `add-paths` 与生成的输出目录不匹配。
- 翻译步骤提前退出。

解决方法：

1. 确认生成的文件存在于 `translations/` 或 `translated_images/`。
2. 确认 `.gitignore` 未忽略生成的输出。
3. 使用匹配的 `add-paths`：

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. 临时向 translate 命令添加调试标志：

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

机器翻译可能需要人工审校。仅在您希望进行实验性质量评分和低置信度修复工作流时才使用 `evaluate`。

!!! warning "实验性"
    `evaluate` 可以使用基于规则和基于 LLM 的检查，其评分模型和元数据行为可能会发生变化。除非您的工作流已准备好应对更改，否则不要将其纳入必需的 CI 门。

对于确定性的 CI 检查，请改用 `co-op-review`。