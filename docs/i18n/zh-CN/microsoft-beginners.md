# Microsoft 为初学者的仓库

本页面适用于维护使用共享 “Other Courses” README 部分的 Microsoft “For Beginners” 仓库的维护者。

大多数 Co-op Translator 用户不需要此页面。

## 自动同步 Other Courses 部分

在你的 README 中的 “Other Courses” 部分周围添加这些标记：

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

每次 Co-op Translator 通过 CLI 或 GitHub Actions 运行时，它都会用打包的模板替换标记之间的内容。

## 更新共享模板

模板源位于：

```text
src/co_op_translator/templates/other_courses.md
```

To update the shared content:

1. Edit the template.
2. 向 Co-op Translator 提交拉取请求.
3. 更改发布后，在目标仓库中运行 Co-op Translator。

## 稀疏检出建议

当大型课程仓库包含许多翻译输出时，克隆可能会变得昂贵。你可以在生成的语言部分中包含此建议：

```markdown
> **Prefer to Clone Locally?**
>
> This repository includes many language translations, which can significantly increase download size. To clone without translations, use sparse checkout:
>
> ```bash
> git clone --filter=blob:none --sparse https://github.com/org/repo.git
> cd repo
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
```