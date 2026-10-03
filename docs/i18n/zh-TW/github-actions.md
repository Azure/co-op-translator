# GitHub Actions

當您希望儲存庫能自動翻譯已變更的文件並以產生的輸出建立拉取請求時，請使用 GitHub Actions。

從標準的 `GITHUB_TOKEN` 設定開始，在組織儲存庫且政策允許時亦包含此設定。當組織需要以 App 身份或需要自動觸發下游工作流程執行時，請參閱 [GitHub 應用程式設定](#github-app-setup)。

**人工編輯：** 這些工作流程會完整地重新翻譯已變更的原始檔案，可能會覆寫其翻譯中已編輯的字句。在合併前請審閱每個 PR。接受之修改的 Markdown 區塊層級保存需要與 [Python API 翻譯狀態提供者](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) 的自訂整合。

## 你的第一個 README 翻譯 PR

從一個根目錄的 `README.md` 和一個目標語言開始。此工作流程僅翻譯 Markdown，因此不需要 Azure AI Vision。

1. 複製 [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([在 GitHub 上檢視範本](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) 到您要翻譯的儲存庫中的 `.github/workflows/translate-readme.yml`，並提交到該儲存庫的預設分支。範本使用 `Azure/co-op-translator@main` 的根 Action，該 Action 從相同的來源 ref 安裝 CLI。為了可重現執行，請將已審核的提交固定（pin）。
2. 開啟 **Actions > Translate README > Run workflow**，選擇一個語言，並保持勾選 **Preview only**。在預覽步驟中檢查代幣估計。預覽不會呼叫模型提供者、寫入翻譯或建立 PR。
3. 為一個 [文字提供者](#prerequisites) 新增祕密，並在 **設定 > Actions > 一般** 下啟用 **允許 GitHub Actions 建立並核准拉取請求**。範本在其工作中請求 `contents: write` 與 `pull-requests: write`；您不需要為每個工作流程變更預設權限。如果組織政策封鎖這些權限或此設定，請向管理員詢問經核准的 [GitHub 應用程式](#github-app-setup)。
4. 再次執行工作流程並取消勾選 **Preview only**。它會預覽、翻譯、執行 `co-op-review --readme-only`，且僅在翻譯與審查成功後才建立或更新翻譯 PR。工作流程摘要會連結到該 PR。
5. 在 PR 中審查用詞與檔案變更，準備好後再合併。工作流程不會自動合併。

PR 僅包含 `translations/<language>/README.md` 及其語言對應的 metadata 檔案。原始 README 保持不變，指向其他文件的連結仍然指向原始文件。PR 主體會列出變更的檔案與結構性審查結果。如果翻譯或審查失敗，請檢查工作流程摘要與失敗步驟的日誌；此情況下不會建立 PR。如果沒有變更，則不需要新的 PR。

**組織與 CI 注意事項：** GitHub App 為選用，不是組織擁有權的必要條件。使用 `GITHUB_TOKEN` 時，開啟、更新或重新開啟 PR 的 pull-request 工作流程需要具有寫入權限的使用者選擇 **Approve workflows to run**。push 類型的工作流程不會由此代幣觸發。若需無監督的下游 CI，請參閱 [GitHub 應用程式設定](#github-app-setup) 以及 GitHub 的 [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)。

## Prerequisites

在建立工作流程之前，配置翻譯執行所需的 AI 服務祕密。

文字翻譯需要一個語言模型提供者：

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

圖像翻譯另需 Azure AI Vision：

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

有關本機配置的詳細資訊，請參閱 [Configuration](configuration.md) 與 [Azure AI Setup](azure-ai-setup.md)。

## 標準設定

在試用 README 工作流程之後，使用此設定將儲存庫的 Markdown 檔案翻譯成多種語言。它會在開啟 PR 之前執行 Markdown 審查，且不需要 Azure AI Vision。

### 步驟 1：新增儲存庫機密

在目標儲存庫中，開啟 **Settings** > **Secrets and variables** > **Actions**，然後新增工作流程將使用的提供者祕密。

![選取 Actions 的 Secrets](../../assets/github-actions/select-setting-action.png)

### 步驟 2：啟用工作流程權限

開啟 **Settings** > **Actions** > **General**。

在 **Workflow permissions** 底下：

1. 啟用 **允許 GitHub Actions 建立並核准拉取請求**。
2. 儲存此設定。

下方工作會明確請求 `contents: write` 與 `pull-requests: write`。請維持儲存庫的預設工作流程權限不變。如果組織政策封鎖 PR 建立，請向管理員詢問經核准的 [GitHub 應用程式](#github-app-setup)。

### 步驟 3：新增工作流程

建立 `.github/workflows/co-op-translator.yml`：

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

將 `TARGET_LANGUAGES` 更改為您的專案所需的語言。審查使用 Python API 僅檢查 Markdown，與翻譯步驟一致。翻譯或審查錯誤會在建立 PR 之前中止工作。工作流程不會自動合併 PR。對於大型儲存庫，請在 `on.push` 底下新增 `paths:` 篩選，讓工作流程只在文件變更時執行。

### 選用：筆記本與圖片

對於筆記本，於翻譯指令新增 `-nb` 並在審查步驟中將 `notebook=True` 設定。對於圖像文字，配置兩個 [Azure AI Vision 機密](#prerequisites)，於翻譯步驟的 `env` 中傳入它們，於指令中新增 `-img`，並將 `translated_images/` 加到 PR 步驟的 `add-paths`。以視覺方式審查翻譯後的圖像；決定性審查不保證圖像文字或語言準確性。

## GitHub 應用程式設定

當組織要求以 App 身份或產生的 PR 需要在沒有 `GITHUB_TOKEN` 批准步驟下觸發下游 CI 時，請使用經核准的 GitHub App。App 並不會繞過組織政策；管理員仍控制其安裝和權限。

### 步驟 1：建立或安裝 GitHub 應用程式

有可用的組織提供 App 時請使用既有者，否則建立一個具有對 **Contents** 與 **Pull requests** 的讀寫存取權限的 App。並將其安裝到目標儲存庫，遵循任何所需的組織核准流程。

記下：

- 應用程式 ID
- 私鑰內容

將它們儲存為儲存庫祕密：

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### 步驟 2：產生應用程式權杖

在現有的 pull request 步驟之前立即新增此步驟。對於 README 範本，請使用相同的成功條件，這樣預覽與失敗的翻譯就不會要求 App 代幣：

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

然後僅將現有 pull request 步驟的 `token` 輸入改為 `${{ steps.generate_token.outputs.token }}`。保留其成功條件、分支、PR 主體與 `add-paths` 不變。預設情況下，該代幣的作用範圍為目前儲存庫。當以標準設定調整而非 README 範本時，省略上述的 `if`：該工作流程使用預設的成功條件，因此代幣建立與 PR 建立僅在翻譯與審查成功後執行。

請參閱官方的 [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) 以取得安裝與代幣權限資訊。

## 執行者限制

GitHub 託管的 runner 有最大工作執行時間。大型儲存庫或許多目標語言可能會超過該限制。

對於大型翻譯工作負載：

- 每次執行翻譯較少的語言。
- 使用內容旗標，例如 `-md`、`-nb` 或 `-img`。
- 當儲存庫大小或模型延遲使託管 runner 不可靠時，請使用自架 runner。

## 在 CI 中檢閱

當需要在不呼叫 LLM 或 Vision 提供者的情況下驗證產生的翻譯時，請使用 `co-op-review`。

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` 是一個測試中的決定性審查指令。其檢查與輸出結構可能會演進，但它被設計成對 CI 安全，因為它不會寫入檔案或呼叫模型提供者。