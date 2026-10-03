# GitHub Actions

当你希望仓库自动翻译已更改的文档并使用生成的输出打开拉取请求时，请使用 GitHub Actions。

从标准的 `GITHUB_TOKEN` 配置开始，包括在策略允许的组织仓库中。若组织要求使用应用身份或需要自动触发下游工作流，请参阅 [GitHub App Setup](#github-app-setup)。

**人工编辑：** 这些工作流会完整地重新翻译已更改的源文件，可能会覆盖其翻译中已编辑的措辞。在合并之前请审查每个 PR。要在 Markdown 块级别保留已接受的编辑，需要与 [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) 的自定义集成。

## 你的第一个 README 翻译 PR

从一个根 `README.md` 和一种目标语言开始。此工作流仅翻译 Markdown，因此不需要 Azure AI Vision。

1. 将 [translate-readme.yml](../../assets/workflows/translate-readme.yml)（[在 GitHub 上查看模板](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)）复制到要翻译的仓库中的 `.github/workflows/translate-readme.yml`，并将其提交到该仓库的默认分支。该模板使用 `Azure/co-op-translator@main` 中的根 Action，从相同的源引用安装 CLI。为了可复现的运行，请固定为已审核的提交。
2. 打开 **Actions > Translate README > Run workflow**，选择一种语言，并保持 **Preview only** 已勾选。在预览步骤中查看 token 估算。预览不会调用模型提供者、写入翻译或创建 PR。
3. 为一个[文本提供者](#prerequisites) 添加密钥，并在 **Settings > Actions > General** 下启用 **允许 GitHub Actions 创建并批准拉取请求**。该模板为其作业请求 `contents: write` 和 `pull-requests: write`；你不需要更改每个工作流的默认权限。如果组织策略阻止这些权限或此设置，请咨询管理员有关已批准的 [GitHub 应用](#github-app-setup)。
4. 取消选中 **Preview only** 后再次运行工作流。它会进行预览、翻译、运行 `co-op-review --readme-only`，并且仅在翻译和审核成功后创建或更新翻译 PR。工作流摘要会链接到该 PR。
5. 在 PR 中审查措辞和文件更改，然后准备好时合并。该工作流不会自动合并。

该 PR 仅包含 `translations/<language>/README.md` 及其语言元数据文件。源 README 保持不变，对其他文档的链接仍指向源文档。PR 正文列出更改的文件和结构性审核结果。如果翻译或审核失败，请检查工作流摘要和失败步骤的日志；不会创建 PR。如果没有更改，则不需要新的 PR。

**组织和 CI 说明：** GitHub App 是可选的，并非组织所有权的必需。如果使用 `GITHUB_TOKEN`，用于打开、更新或重新打开 PR 的拉取请求工作流需要具有写权限的用户选择 **Approve workflows to run**。推送工作流不会由此令牌触发。要实现无人值守的下游 CI，请参阅 [GitHub App Setup](#github-app-setup) 和 GitHub 的 [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)。

## Prerequisites

在创建工作流之前，配置翻译运行所需的 AI 服务密钥。

文本翻译需要一个语言模型提供者：

- Azure OpenAI： `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI： `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, 以及可选的 `OPENAI_ORG_ID` 和 `OPENAI_BASE_URL`
- Anthropic： `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, 以及可选的 `ANTHROPIC_BASE_URL`

图像翻译还需要 Azure AI Vision：

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

有关本地配置的详细信息，请参阅 [配置](configuration.md) 和 [Azure AI 设置](azure-ai-setup.md)。

## 标准设置

在尝试 README 工作流之后，使用此设置将仓库的 Markdown 文件翻译为多种语言。它在打开 PR 之前运行 Markdown 审核，并且不需要 Azure AI Vision。

### 步骤 1：添加仓库机密

在目标仓库中，打开 **Settings > Secrets and variables > Actions**，然后添加工作流将使用的提供者密钥。

![选择 Actions 密钥](../../assets/github-actions/select-setting-action.png)

### 步骤 2：启用工作流程权限

打开 **Settings > Actions > General**。

在 **Workflow permissions** 下：

1. 启用 **允许 GitHub Actions 创建并批准拉取请求**。
2. 保存设置。

下面的作业明确请求 `contents: write` 和 `pull-requests: write`。保持仓库的默认工作流权限不变。如果组织策略阻止创建 PR，请咨询管理员有关已批准的 [GitHub App](#github-app-setup)。

### 第3步：添加工作流

创建 `.github/workflows/co-op-translator.yml`：

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest
    env:
      TARGET_LANGUAGES: "es fr de"

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.11"

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ANTHROPIC_MODEL: ${{ secrets.ANTHROPIC_MODEL }}
          ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL }}
        run: |
          translate -l "$TARGET_LANGUAGES" -md -y

      - name: Review Markdown translations
        run: |
          python - <<'PY'
          import os
          from co_op_translator.api import run_review

          run_review(
              language_codes=os.environ["TARGET_LANGUAGES"].split(),
              markdown=True,
              notebook=False,
              output_format="github",
          )
          PY

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "Update translations via Co-op Translator"
          title: "Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.
            Markdown structure, freshness, and local links were reviewed.
            Review translation wording before merging.

            Generated by Co-op Translator.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
```

将 `TARGET_LANGUAGES` 更改为你的项目所需的语言。审核使用 Python API 仅检查 Markdown，与翻译步骤一致。翻译或审核错误会在创建 PR 之前停止作业。该工作流不会自动合并 PR。对于大型仓库，在 `on.push` 下添加 `paths:` 过滤，以便只有在文档更改时才运行工作流。

### 可选：笔记本和镜像

对于笔记本，请在翻译命令中添加 `-nb` 并在审核步骤中将 `notebook=True` 设置为真。对于图像文本，请配置两个 [Azure AI Vision secrets](#prerequisites)，在翻译步骤的 `env` 中传入它们，在命令中添加 `-img`，并将 `translated_images/` 添加到 PR 步骤的 `add-paths`。请目视审查翻译后的图像；确定性审核并不保证图像文本或语言的准确性。

## GitHub 应用设置

当你的组织要求使用应用身份，或生成的 PR 需要在没有 `GITHUB_TOKEN` 批准步骤的情况下触发下游 CI 时，请使用已批准的 GitHub 应用。应用并不能绕过组织策略；管理员仍然控制其安装和权限。

### 步骤 1：创建或安装 GitHub 应用

如有可用，请使用组织提供的现有应用，或创建一个具有对 **Contents** 和 **Pull requests** 的读/写访问权限的应用。按需在目标仓库安装它并获得组织批准。

记录：

- 应用 ID
- 私钥内容

将它们作为仓库密钥存储：

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### 步骤 2：生成应用令牌

在现有的拉取请求步骤之前立即添加此步骤。对于 README 模板，使用相同的成功条件，以便预览和失败的翻译不会请求应用令牌：

```yaml
      - name: Authenticate GitHub App
        id: generate_token
        if: ${{ !inputs.preview && steps.translate.outcome == 'success' && steps.review.outcome == 'success' }}
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.GH_APP_ID }}
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
          permission-contents: write
          permission-pull-requests: write
```

然后仅将现有拉取请求步骤的 `token` 输入更改为 `${{ steps.generate_token.outputs.token }}`。保持其成功条件、分支、PR 正文和 `add-paths` 不变。该令牌默认为当前仓库范围。当适配标准设置而不是 README 模板时，省略上面的 `if`：该工作流使用默认的成功条件，因此令牌创建和 PR 创建仅在翻译和审核成功后运行。

有关安装和令牌权限，请参阅官方 [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2)。

## 运行器限制

由 GitHub 托管的运行器具有作业最长持续时间限制。大型仓库或许多目标语言可能会超过该限制。

对于大型翻译工作量：

- 每次运行翻译更少的语言。
- 使用内容标志，例如 `-md`、`-nb` 或 `-img`。
- 当仓库大小或模型延迟使托管运行器不可靠时，使用自托管运行器。

## 在 CI 中审查

当拉取请求应在不调用 LLM 或 Vision 提供者的情况下验证生成的翻译时，使用 `co-op-review`。

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` 是一个处于测试阶段的确定性审核命令。它的检查和输出模式可能会演化，但被设计为对 CI 安全，因为它不会写入文件或调用模型提供者。