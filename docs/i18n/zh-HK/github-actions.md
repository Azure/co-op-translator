# GitHub Actions

當你希望儲存庫自動翻譯已更改的文件並建立一個包含產生輸出的拉取請求時，請使用 GitHub Actions。

從標準的 `GITHUB_TOKEN` 設定開始，在組織儲存庫且政策允許時也包含此設定。當你的組織需要以 App 身份或需要自動觸發下游工作流程執行時，請參閱 [GitHub App 設定](#github-app-setup)。

**人工編輯：** 這些工作流程會完整地重新翻譯已更改的來源檔案，並可能覆蓋翻譯中已由人工修改的措辭。合併前請檢閱每個 PR。要保留 Markdown 的區塊級已接受編輯，需要與 [Python API 轉譯狀態提供器](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) 做自訂整合。

## 你的第一個 README 翻譯 PR

從一個根目錄的 `README.md` 和一個目標語言開始。此工作流程僅翻譯 Markdown，因此不需要 Azure AI Vision。

1. 將 [translate-readme.yml](../../assets/workflows/translate-readme.yml)（[在 GitHub 檢視範本](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)）複製到你要翻譯的儲存庫中的 `.github/workflows/translate-readme.yml`，並提交到該儲存庫的預設分支。範本使用根 Action `Azure/co-op-translator@main`，它會從相同的來源 ref 安裝 CLI。為了可重現的執行，請將已審核的提交鎖定（pin）。
2. 開啟 **Actions > Translate README > Run workflow**，選擇一個語言，並保持 <strong>僅預覽</strong> 勾選。於預覽步驟中檢閱 token 的估計。預覽不會呼叫模型提供者、不會寫入翻譯，也不會建立 PR。
3. 新增一個 [文字提供者](#prerequisites) 的機密，並於 **設定 > Actions > 一般** 下啟用 **允許 GitHub Actions 建立並核准拉取請求**。範本的工作流程會要求其工作權限為 `contents: write` 和 `pull-requests: write`；你毋須為每個工作流程更改預設權限。如果組織政策封鎖這些權限或此設定，請向管理員查詢是否有已獲核准的 [GitHub App](#github-app-setup)。
4. 再次執行工作流程並取消勾選 <strong>僅預覽</strong>。它會先預覽、翻譯、執行 `co-op-review --readme-only`，只有在翻譯與檢閱成功後才會建立或更新翻譯 PR。工作流程摘要會連結到該 PR。
5. 檢閱 PR 中的措辭與檔案變更，準備好後再合併。工作流程不會自動合併。

PR 僅包含 `translations/<language>/README.md` 與其語言對應的 metadata 檔案。來源的 README 保持不變，且指向其他文件的連結仍會指向來源文件。PR 內文會列出已變更的檔案與結構性檢閱結果。若翻譯或檢閱失敗，請檢查工作流程摘要與失敗步驟的日誌；不會建立 PR。若沒有變更，則不需要新的 PR。

**組織與 CI 注意事項：** GitHub App 是可選的，非組織擁有權的必要條件。使用 `GITHUB_TOKEN` 時，打開、更新或重新開啟 PR 的工作流程需要具有寫入權的使用者選取 **Approve workflows to run**。此 token 不會觸發 push 工作流程。若需無人值守的下游 CI，請參閱 [GitHub App 設定](#github-app-setup) 與 GitHub 的 [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)。

## Prerequisites

在建立工作流程之前，先設定翻譯執行所需的 AI 服務機密。

文字翻譯需要一個語言模型提供者：

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

圖像翻譯另外需要 Azure AI Vision：

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

請參閱 [設定](configuration.md) 與 [Azure AI 設定](azure-ai-setup.md) 以取得本機設定細節。

## 標準設定

在試用 README 工作流程後，使用此設定將儲存庫的 Markdown 檔案翻譯成多種語言。它會在開啟 PR 之前執行 Markdown 檢閱，且不需要 Azure AI Vision。

### 步驟 1: 新增儲存庫機密

在你的目標儲存庫中，開啟 **Settings** > **Secrets and variables** > **Actions**，然後新增工作流程將使用的提供者機密。

![選取 Actions 機密](../../assets/github-actions/select-setting-action.png)

### 步驟 2: 啟用工作流程權限

開啟 **Settings** > **Actions** > **General**。

在 **Workflow permissions** 底下：

1. 啟用 **允許 GitHub Actions 建立並核准拉取請求**。
2. 儲存該設定。

下方的工作會明確要求 `contents: write` 和 `pull-requests: write`。請保持儲存庫的預設工作流程權限不變。如果組織政策封鎖 PR 建立，請詢問管理員是否有核准的 [GitHub App](#github-app-setup)。

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

將 `TARGET_LANGUAGES` 改為你的專案所需的語言。檢閱使用 Python API 只檢查 Markdown，與翻譯步驟相符。翻譯或檢閱錯誤會在建立 PR 之前終止工作。工作流程不會自動合併 PR。對於大型儲存庫，請在 `on.push` 下加入 `paths:` 篩選，讓工作流程僅在文件變更時執行。

### 可選：筆記本與圖像

對於 notebooks，於翻譯指令中加入 `-nb` 並在檢閱步驟設定 `notebook=True`。對於影像文字，請設定兩個 [Azure AI Vision 機密](#prerequisites)，在翻譯步驟的 `env` 中傳遞它們，於指令中加入 `-img`，並在 PR 步驟的 `add-paths` 裡加入 `translated_images/`。請視覺上檢閱翻譯後的影像；該確定性檢閱不保證影像文字或語言上的準確性。

## GitHub 應用程式設定

當你的組織要求以 App 身份或產生的 PR 需要在沒有 `GITHUB_TOKEN` 核准步驟下觸發下游 CI 時，請使用核准的 GitHub App。App 不會繞過組織政策；管理員仍然控管其安裝與權限。

### 步驟 1：建立或安裝 GitHub App

若有現成的組織提供的 App 可用，請使用它；或建立一個具有對 **Contents** 與 **Pull requests** 的讀寫存取的 App。依所需的組織核准將其安裝到目標儲存庫。

記錄：

- App ID
- 私鑰內容

將它們儲存為儲存庫的機密：

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### 步驟 2：產生應用程式權杖

在現有的 pull request 步驟之前立即新增此步驟。對於 README 範本，請使用相同的成功條件，這樣預覽與失敗的翻譯就不會請求 App token：

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

然後僅將現有 pull request 步驟的 `token` 輸入改為 `${{ steps.generate_token.outputs.token }}`。保持其成功條件、分支、PR 內容與 `add-paths` 不變。該 token 預設被限定在目前的儲存庫。當你改作標準設定而非 README 範本時，省略上方的 `if`：該工作流程使用預設的成功條件，因此只有在翻譯與檢閱成功後才會執行 token 建立與 PR 建立。

有關安裝與 token 權限，請參閱官方的 [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2)。

## 執行器限制

GitHub 託管的 runner 有最長的工作時限。大型儲存庫或多個目標語言可能會超過該限制。

對於大型的翻譯工作量：

- 每次執行翻譯較少的語言。
- 使用內容旗標，例如 `-md`、`-nb` 或 `-img`。
- 當儲存庫大小或模型延遲使託管 runner 變得不可靠時，使用自託管 runner。

## 在 CI 中審查

當拉取請求應在不呼叫 LLM 或 Vision 提供者的情況下驗證產生的翻譯時，請使用 `co-op-review`。

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` 是一個測試階段的確定性檢閱命令。其檢查與輸出 schema 可能會演進，但為 CI 設計時考量安全性，因為它不會寫入檔案或呼叫模型提供者。