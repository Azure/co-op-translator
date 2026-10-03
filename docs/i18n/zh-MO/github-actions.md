# GitHub Actions

當您希望儲存庫自動翻譯已變更的文件並以產生的輸出建立拉取請求時，請使用 GitHub Actions。

在支援的情況下，先從標準的 `GITHUB_TOKEN` 設定開始，包括組織儲存庫。若您的組織需要以 App 身份運作或需要自動的下游工作流程執行時，請參閱 [GitHub App Setup](#github-app-setup)。

**Human edits:** 這些工作流程會完整重新翻譯已變更的來源檔案，可能會覆寫其翻譯中已編輯的措辭。合併前請審查每個 PR。要保留已接受編輯的 Markdown 區塊級內容，需要與 [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) 的自訂整合。

## 您的第一個 README 翻譯 PR

從一個根 `README.md` 和一種目標語言開始。此工作流程僅翻譯 Markdown，因此不需要 Azure AI Vision。

1. 將 [translate-readme.yml](../../assets/workflows/translate-readme.yml)（[在 GitHub 上檢視範本](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)）複製到您要翻譯的儲存庫內的 `.github/workflows/translate-readme.yml`，並提交到該儲存庫的預設分支。該範本使用 `Azure/co-op-translator@main` 的根 Action，會從相同的來源 ref 安裝 CLI。為了可重現的執行，請固定到已審查的 commit。
2. 打開 **Actions > Translate README > Run workflow**，選擇語言，並保持勾選 **Preview only**。在預覽步驟中檢查代幣估算。預覽不會呼叫模型提供者、不會寫入翻譯，也不會建立 PR。
3. 新增一個 [文字提供者](#prerequisites) 的密鑰（secrets），並在 **設定 > Actions > 一般** 下啟用 **允許 GitHub Actions 建立並核准拉取請求**。該範本的工作需要 `contents: write` 和 `pull-requests: write` 權限；您不需要更改每個工作流程的預設權限。如果組織政策封鎖這些權限或此設定，請向管理員查詢有關獲核准的 [GitHub 應用程式](#github-app-setup)。
4. 再次執行工作流程並取消勾選 **Preview only**。此流程會先預覽、翻譯、執行 `co-op-review --readme-only`，且僅在翻譯和審查成功後才建立或更新翻譯 PR。工作流程摘要會連結到該 PR。
5. 在 PR 中檢查措辭與檔案變更，準備好後再合併。工作流程不會自動合併。

PR 僅包含 `translations/<language>/README.md` 及其語言對應的 metadata 檔案。來源 README 保持不變，且其他文件的連結仍指向來源文件。PR 內容會列出已變更的檔案與結構性審查結果。若翻譯或審查失敗，請檢查工作流程摘要與失敗步驟的日誌；此情況下不會建立 PR。若沒有任何變更，則不需要新的 PR。

**Organization and CI note:** GitHub App 是可選的，並非組織所有權的必要條件。使用 `GITHUB_TOKEN` 時，用於開啟、更新或重新開啟 PR 的拉取請求工作流程需要有寫入權限的使用者選取 **Approve workflows to run**。此 token 不會觸發 push 類型的工作流程。欲進行無人值守的下游 CI，請參閱 [GitHub App Setup](#github-app-setup) 與 GitHub 的 [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)。

## 先決條件

在建立工作流程之前，設定翻譯執行所需的 AI 服務密鑰（secrets）。

文字翻譯需要一個語言模型提供者：

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`，以及可選的 `OPENAI_ORG_ID` 和 `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`，以及可選的 `ANTHROPIC_BASE_URL`

圖像翻譯此外還需要 Azure AI Vision：

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

有關本地設定的詳情，請參閱 [Configuration](configuration.md) 與 [Azure AI Setup](azure-ai-setup.md)。

## 標準設定

在嘗試 README 工作流程之後，可以使用此設定將儲存庫的 Markdown 檔案翻譯成多種語言。它會在開啟 PR 之前執行 Markdown 審查，且不需要 Azure AI Vision。

### 步驟 1：新增儲存庫密鑰 (Secrets)

在目標儲存庫中，打開 **Settings** > **Secrets and variables** > **Actions**，然後新增工作流程將使用的 provider secrets。

![選取 Actions 密鑰](../../assets/github-actions/select-setting-action.png)

### 步驟 2：啟用工作流程權限

打開 **Settings** > **Actions** > **General**。

在 **Workflow permissions** 下：

1. 啟用 **允許 GitHub Actions 建立並核准拉取請求**。
2. 儲存此設定。

下方的工作會明確請求 `contents: write` 和 `pull-requests: write`。請保持儲存庫的預設工作流程權限不變。如果組織政策阻止建立 PR，請向管理員詢問已核准的 [GitHub App](#github-app-setup)。

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

將 `TARGET_LANGUAGES` 更改為您的專案所需的語言。審查使用 Python API 只檢查 Markdown，與翻譯步驟相符。翻譯或審查錯誤會在建立 PR 之前停止該工作。工作流程不會自動合併 PR。對於大型儲存庫，請在 `on.push` 下新增 `paths:` 篩選，讓工作流程僅在文件變更時執行。

### 選用：筆記本（notebooks）與圖片

對於筆記本，於翻譯命令中加入 `-nb`，並在審查步驟中將 `notebook=True` 設定。對於圖片文字，設定兩個 [Azure AI Vision secrets](#prerequisites)，在翻譯步驟的 `env` 中傳入它們，於命令中加入 `-img`，並在 PR 步驟的 `add-paths` 加上 `translated_images/`。以視覺方式檢視翻譯後的圖片；決定性的審查不會保證圖片文字或語言上的準確性。

## GitHub App 設定

當您的組織需要 App 身分識別，或產生的 PR 需在不使用 `GITHUB_TOKEN` 核准步驟下觸發下游 CI 時，請使用已核准的 GitHub App。App 並不會繞過組織政策；管理員仍掌控其安裝與權限。

### 步驟 1：建立或安裝 GitHub App

若有組織提供的現有 App，請使用該 App；否則建立一個具有對 **Contents** 和 **Pull requests** 的讀寫權限的 App。依所需的組織核准，將其安裝到目標儲存庫。

記錄：

- App ID
- 私鑰內容

將它們儲存為儲存庫的 secrets：

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### 步驟 2：產生 App 代幣（Token）

在現有的拉取請求步驟之前立即加入此步驟。對於 README 範本，請使用相同的成功條件，以便預覽和失敗的翻譯不會要求 App 代幣：

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

接著只將現有拉取請求步驟的 `token` 輸入更改為 `${{ steps.generate_token.outputs.token }}`。保持其成功條件、分支、PR 內容與 `add-paths` 不變。該 token 預設被限定在目前儲存庫的範圍內。當改用標準設定而非 README 範本時，省略上方的 `if`：該工作流程使用預設的成功條件，因此只有在翻譯和審查成功後才會執行 token 建立與 PR 建立。

有關安裝與 token 權限，請參閱官方的 [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2)。

## 執行器限制

GitHub 托管的 runners 有最大工作時長限制。大型儲存庫或多個目標語言可能會超出該限制。

對於大型翻譯工作量：

- 每次執行翻譯較少的語言。
- 使用內容旗標（flags），例如 `-md`、`-nb` 或 `-img`。
- 當儲存庫大小或模型延遲使託管 runner 不可靠時，使用自我管理（self-hosted）runner。

## 在 CI 中審查

當需要在拉取請求中驗證產生的翻譯，而不呼叫 LLM 或 Vision 提供者時，請使用 `co-op-review`。

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` 是一個 beta 的決定性審查指令。其檢查與輸出結構可能會演進，但設計上適合在 CI 中使用，因為它不會寫入檔案或呼叫模型提供者。