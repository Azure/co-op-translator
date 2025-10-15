<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "527ca4d0a8d3f51087ec3317279e36ee",
  "translation_date": "2025-10-15T02:39:48+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "ja"
}
-->
# Co-op Translator GitHub Actionの利用方法（パブリックセットアップ）

**対象者:** このガイドは、ほとんどのパブリックまたはプライベートリポジトリで、標準のGitHub Actions権限が十分なユーザー向けです。組み込みの`GITHUB_TOKEN`を利用します。

Co-op Translator GitHub Actionを使えば、リポジトリのドキュメント翻訳を自動化できます。このガイドでは、ソースのMarkdownファイルや画像が変更された際に、翻訳を更新したプルリクエストを自動作成する設定方法を説明します。

> [!IMPORTANT]
>
> **ガイドの選び方:**
>
> このガイドは**標準の`GITHUB_TOKEN`を使ったシンプルなセットアップ**について説明しています。ほとんどのユーザーに推奨される方法で、GitHub Appのプライベートキー管理が不要です。
>

## 事前準備

GitHub Actionの設定前に、必要なAIサービスの認証情報を用意してください。

**1. 必須: AI言語モデルの認証情報**
サポートされている言語モデルのいずれかの認証情報が必要です:

- **Azure OpenAI**: エンドポイント、APIキー、モデル/デプロイメント名、APIバージョンが必要です。
- **OpenAI**: APIキー（オプション: Org ID、Base URL、Model ID）。
- 詳細は[サポートされているモデルとサービス](../../../../README.md)をご覧ください。

**2. オプション: AI Vision認証情報（画像翻訳用）**

- 画像内のテキストも翻訳したい場合のみ必要です。
- **Azure AI Vision**: エンドポイントとサブスクリプションキーが必要です。
- 未設定の場合、アクションは[Markdownのみモード](../markdown-only-mode.md)で動作します。

## セットアップと設定

標準の`GITHUB_TOKEN`を使って、Co-op Translator GitHub Actionをリポジトリに設定する手順です。

### ステップ1: 認証の仕組みを理解する（`GITHUB_TOKEN`の利用）

このワークフローは、GitHub Actionsが提供する組み込みの`GITHUB_TOKEN`を利用します。このトークンは、**ステップ3**で設定した権限に基づき、リポジトリ操作の権限を自動的に付与します。

### ステップ2: リポジトリシークレットの設定

**AIサービスの認証情報**のみを、リポジトリの設定で暗号化されたシークレットとして追加します。

1. 対象のGitHubリポジトリにアクセスします。
2. **Settings** > **Secrets and variables** > **Actions**に進みます。
3. **Repository secrets**の下で、必要なAIサービスごとに**New repository secret**をクリックして追加します。

    <img src="../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.ja.png" alt="Select setting action">（画像説明: シークレット追加箇所）

**必要なAIサービスシークレット（事前準備に応じてすべて追加してください）:**

| シークレット名                         | 説明                                   | 値の取得元                     |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Azure AI Service（Computer Vision）のキー  | Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Service（Computer Vision）のエンドポイント | Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAIサービスのキー              | Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAIサービスのエンドポイント         | Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`           | Azure OpenAIモデル名                    | Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Azure OpenAIデプロイメント名             | Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAIのAPIバージョン              | Azure AI Foundry               |
| `OPENAI_API_KEY`                    | OpenAIのAPIキー                        | OpenAI Platform              |
| `OPENAI_ORG_ID`                     | OpenAI組織ID（オプション）              | OpenAI Platform              |
| `OPENAI_CHAT_MODEL_ID`              | OpenAIモデルID（オプション）            | OpenAI Platform              |
| `OPENAI_BASE_URL`                   | OpenAI APIのカスタムBase URL（オプション） | OpenAI Platform              |

### ステップ3: ワークフロー権限の設定

GitHub Actionが`GITHUB_TOKEN`経由でコードのチェックアウトやプルリクエスト作成を行うための権限が必要です。

1. リポジトリで**Settings** > **Actions** > **General**に進みます。
2. **Workflow permissions**セクションまでスクロールします。
3. **Read and write permissions**を選択します。これで`GITHUB_TOKEN`に`contents: write`と`pull-requests: write`権限が付与されます。
4. **Allow GitHub Actions to create and approve pull requests**のチェックボックスが**オン**になっていることを確認します。
5. **Save**をクリックします。

<img src="../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.ja.png" alt="Permission setting">

### ステップ4: ワークフローファイルの作成

最後に、`GITHUB_TOKEN`を使った自動化ワークフローのYAMLファイルを作成します。

1. リポジトリのルートディレクトリに`.github/workflows/`ディレクトリがなければ作成します。
2. `.github/workflows/`内に`co-op-translator.yml`というファイルを作成します。
3. 下記の内容を`co-op-translator.yml`に貼り付けます。

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```
4.  **ワークフローのカスタマイズ:**
  - **[!IMPORTANT] 対象言語:** `Run Co-op Translator`ステップ内の`translate -l "..." -y`コマンドの言語コードリストは、必ずプロジェクトに合わせて見直し・修正してください。例のリスト（`ar de es...`）は置き換えや調整が必要です。
  - **トリガー（`on:`）:** 現在の設定では`main`へのpushごとに実行されます。大規模リポジトリの場合は、YAML内のコメント例のように`paths:`フィルターを追加し、関連ファイル（例: ドキュメントソース）が変更された時のみ実行することで、ランナーの消費を抑えられます。
  - **PR詳細:** `Create Pull Request`ステップの`commit-message`、`title`、`body`、`branch`名、`labels`なども必要に応じてカスタマイズしてください。

## ワークフローの実行

> [!WARNING]  
> **GitHubホストランナーの時間制限:**  
> `ubuntu-latest`などのGitHubホストランナーは**最大実行時間が6時間**です。  
> ドキュメント量が多い場合、翻訳処理が6時間を超えるとワークフローは自動的に終了します。  
> 対策として:  
> - **セルフホストランナー**の利用（時間制限なし）  
> - 実行ごとの対象言語数を減らす

`co-op-translator.yml`ファイルがmainブランチ（または`on:`トリガーで指定したブランチ）にマージされると、そのブランチへの変更がpushされるたびに（`paths`フィルターを設定していれば該当ファイル変更時のみ）ワークフローが自動実行されます。

---

**免責事項**：
本書類は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な表現が含まれる場合がありますのでご注意ください。原文（元の言語の文書）が正式な情報源となります。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用によって生じたいかなる誤解や誤認についても、当方は責任を負いかねます。