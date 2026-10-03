# GitHub Actions

リポジトリで変更されたドキュメントを自動的に翻訳し、生成された出力でプルリクエストを作成したい場合は、GitHub Actions を使用してください。

標準の `GITHUB_TOKEN` 設定から開始してください。これは、組織のリポジトリでポリシーが許可する場合も含みます。組織がアプリの識別を要求する場合や、下流のワークフローを自動的に実行する必要がある場合は、[GitHub アプリのセットアップ](#github-app-setup) を参照してください。

**Human edits:** これらのワークフローは変更されたソースファイルを完全に再翻訳するため、翻訳内で行った文言の編集を上書きする可能性があります。マージする前に各PRを確認してください。受け入れられた編集の Markdown ブロックレベルでの保持には、[Python API 翻訳状態プロバイダー](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) とのカスタム統合が必要です。

## 最初の README 翻訳 PR

1つのルート `README.md` と 1 つのターゲット言語から開始します。このワークフローは Markdown のみを翻訳するため、Azure AI Vision は不要です。

1. [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([GitHub でテンプレートを表示](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) を翻訳したいリポジトリの `.github/workflows/translate-readme.yml` にコピーし、そのリポジトリのデフォルトブランチにコミットします。テンプレートはルート Action として `Azure/co-op-translator@main` を使用し、同じソース ref から CLI をインストールします。再現可能な実行のためにレビュー済みのコミットを固定してください。
2. **Actions > Translate README > Run workflow** を開き、言語を選択して **Preview only** をチェックしたままにします。プレビューのステップでトークン見積もりを確認してください。プレビューはモデルプロバイダを呼び出さず、翻訳を書き込まず、PRを作成しません。
3. 1つの[テキストプロバイダ](#prerequisites)のシークレットを追加し、**設定 > Actions > 一般** の下で **GitHub Actions がプルリクエストを作成および承認することを許可する** を有効にします。テンプレートはジョブに対して `contents: write` と `pull-requests: write` を要求します。すべてのワークフローのデフォルト権限を変更する必要はありません。組織のポリシーがこれらの権限またはこの設定をブロックする場合は、管理者に承認済みの[GitHub アプリ](#github-app-setup)について問い合わせてください。
4. **Preview only** のチェックを外してワークフローを再度実行します。プレビュー、翻訳、`co-op-review --readme-only` の実行を行い、翻訳とレビューが成功した場合にのみ翻訳PRを作成または更新します。ワークフローのサマリーはPRへのリンクを含みます。
5. PR内の文言とファイル変更を確認し、準備ができたらマージします。ワークフローは自動でマージしません。

PR には `translations/<language>/README.md` とその言語メタデータファイルのみが含まれます。ソースの README は変更されず、他のドキュメントへのリンクは引き続きソースのドキュメントを指します。PR 本文には変更されたファイルと構造的レビューの結果が一覧されます。翻訳またはレビューが失敗した場合は、ワークフローのサマリーと失敗したステップのログを確認してください; PR は作成されません。変更がない場合は、新しい PR は不要です。

**組織と CI に関する注意:** GitHub App は任意であり、組織所有権の要件ではありません。`GITHUB_TOKEN` を使用したプルリクエスト用ワークフローは、PR を開く、更新する、または再オープンする際に **Approve workflows to run** を選択する書き込み権限を持つユーザーを必要とします。Push ワークフローはこのトークンでトリガーされません。無人の下流 CI については、[GitHub アプリのセットアップ](#github-app-setup) と GitHub の [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) を参照してください。

## Prerequisites

ワークフローを作成する前に、翻訳実行に必要な AI サービスのシークレットを構成してください。

テキスト翻訳には 1 つの言語モデル プロバイダーが必要です:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

画像の翻訳には追加で Azure AI Vision が必要です:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

ローカル構成の詳細については、[Configuration](configuration.md) と [Azure AI Setup](azure-ai-setup.md) を参照してください。

## 標準セットアップ

README ワークフローを試した後、このセットアップを使ってリポジトリの Markdown ファイルを複数の言語に翻訳します。PR を開く前に Markdown のレビューを実行し、Azure AI Vision は必要ありません。

### ステップ 1: リポジトリシークレットを追加

対象リポジトリで **Settings > Secrets and variables > Actions** を開き、ワークフローが使用するプロバイダのシークレットを追加します。

![Actions のシークレットを選択](../../assets/github-actions/select-setting-action.png)

### ステップ 2: ワークフローの権限を有効にする

Open **Settings** > **Actions** > **General**.

Under **Workflow permissions**:

1. **GitHub Actions がプルリクエストを作成および承認することを許可する** を有効にします。
2. Save the setting.

以下のジョブは `contents: write` と `pull-requests: write` を明示的に要求します。リポジトリのデフォルトのワークフロー権限は変更しないでください。組織のポリシーがPR作成をブロックする場合は、管理者に承認された[GitHub アプリ](#github-app-setup)について問い合わせてください。

### ステップ 3: ワークフローを追加

Create `.github/workflows/co-op-translator.yml`:

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

`TARGET_LANGUAGES` をプロジェクトが必要とする言語に変更してください。レビューは翻訳ステップと一致するようにPython APIを使用してMarkdownのみをチェックします。翻訳またはレビューのエラーはPR作成前にジョブを停止させます。ワークフローはPRを自動でマージしません。大規模なリポジトリでは、`on.push` の下に `paths:` フィルタを追加して、ドキュメントが変更された場合にのみワークフローが実行されるようにします。

### オプション: ノートブックと画像

ノートブックの場合は、翻訳コマンドに `-nb` を追加し、レビューのステップで `notebook=True` を設定します。画像内テキストの場合は、2つの[Azure AI Vision のシークレット](#prerequisites)を構成し、それらを翻訳ステップの `env` に渡し、コマンドに `-img` を追加し、PRステップの `add-paths` に `translated_images/` を追加します。翻訳された画像は目視で確認してください。決定論的なレビューは画像内テキストや言語的正確性を保証しません。

## GitHub アプリのセットアップ

組織がアプリの識別を要求する場合、または生成された PR が `GITHUB_TOKEN` の承認ステップなしで下流の CI をトリガーする必要がある場合は、承認された GitHub App を使用してください。App は組織のポリシーを無効にするものではなく、管理者がインストールと権限を管理します。

### ステップ 1: GitHub App を作成またはインストール

利用可能な場合は既存の組織提供のアプリを使用するか、**Contents** と **Pull requests** への読み書きアクセスを持つものを作成してください。必要な組織の承認を得てターゲットリポジトリにインストールします。

Record:

- App ID
- Private key contents

Store them as repository secrets:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### ステップ 2: アプリトークンを生成

このステップを既存のプルリクエストステップの直前に追加してください。README テンプレートの場合、プレビューや失敗した翻訳が App トークンを要求しないように、同じ成功条件を使用します:

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

次に既存のプルリクエストステップの `token` 入力のみを `${{ steps.generate_token.outputs.token }}` に変更します。成功条件、ブランチ、PR本文、および `add-paths` は変更しないでください。トークンはデフォルトで現在のリポジトリにスコープされます。README テンプレートの代わりに標準セットアップを適用する場合は、上記の `if` を省略してください: そのワークフローはデフォルトの成功条件を使用するため、トークン作成とPR作成は翻訳とレビューが成功した後にのみ実行されます。

See the official [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) for installation and token permissions.

## ランナーの制限

GitHub ホストのランナーにはジョブの最大実行時間があります。大規模なリポジトリや多数のターゲット言語はその制限を超える可能性があります。

For large translation workloads:

- Translate fewer languages per run.
- Use content flags such as `-md`, `-nb`, or `-img`.
- リポジトリのサイズやモデルの遅延によりホスト型ランナーが信頼できない場合はセルフホステッドランナーを使用してください。

## CIでレビュー

プルリクエストで生成された翻訳をLLMやVisionプロバイダを呼び出さずに検証する必要がある場合は、`co-op-review` を使用してください。

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` はベータ版の決定論的レビューコマンドです。そのチェックと出力スキーマは変わる可能性がありますが、ファイルを書き込んだりモデルプロバイダーを呼び出したりしないため、CI に対して安全になるよう設計されています。