<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "87bf95d45e684475ef1e67d8dae5f6eb",
  "translation_date": "2025-05-06T18:10:28+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "ja"
}
-->
# Co-op Translator GitHub Action の使い方（パブリック設定）

**対象読者:** このガイドは、標準の GitHub Actions 権限があれば十分な、ほとんどのパブリックまたはプライベートリポジトリのユーザー向けです。組み込みの `GITHUB_TOKEN` を利用します。

Co-op Translator GitHub Action を使って、リポジトリのドキュメント翻訳を自動化しましょう。このガイドでは、ソースの Markdown ファイルや画像が変更されるたびに、翻訳が更新されたプルリクエストを自動作成するアクションの設定方法を説明します。

> [!IMPORTANT]
>
> **適切なガイドの選択:**
>
> 本ガイドは、**標準の `GITHUB_TOKEN` を使ったより簡単なセットアップ**について解説しています。これは、機密性の高い GitHub App Private Key を管理する必要がないため、ほとんどのユーザーに推奨される方法です。
>

## 前提条件

GitHub Action を設定する前に、必要な AI サービスの認証情報を準備してください。

**1. 必須: AI 言語モデルの認証情報**  
サポートされているいずれかの言語モデルの認証情報が必要です:

- **Azure OpenAI**: エンドポイント、API キー、モデル/デプロイメント名、API バージョンが必要です。
- **OpenAI**: API キー、（任意で）組織 ID、ベース URL、モデル ID が必要です。
- 詳細は [Supported Models and Services](../../../../README.md) を参照してください。
- セットアップガイド: [Azure OpenAI のセットアップ](../set-up-resources/set-up-azure-openai.md)。

**2. 任意: コンピュータービジョンの認証情報（画像翻訳用）**

- 画像内のテキストを翻訳したい場合のみ必要です。
- **Azure Computer Vision**: エンドポイントとサブスクリプションキーが必要です。
- 未設定の場合、アクションは [Markdown のみモード](../markdown-only-mode.md) で動作します。
- セットアップガイド: [Azure Computer Vision のセットアップ](../set-up-resources/set-up-azure-computer-vision.md)。

## セットアップと設定

標準の `GITHUB_TOKEN` を使って、リポジトリ内で Co-op Translator GitHub Action を設定する手順は以下の通りです。

### ステップ 1: 認証の理解（`GITHUB_TOKEN` の利用）

このワークフローは、GitHub Actions が提供する組み込みの `GITHUB_TOKEN` を使用します。このトークンは、**ステップ 3** で設定した権限に基づいて、ワークフローがリポジトリにアクセスする権限を自動的に付与します。

### ステップ 2: リポジトリシークレットの設定

リポジトリ設定で、**AI サービスの認証情報**を暗号化されたシークレットとして追加するだけでOKです。

1. 対象の GitHub リポジトリに移動します。  
2. **Settings** > **Secrets and variables** > **Actions** に進みます。  
3. **Repository secrets** の下で、必要な AI サービスのシークレットごとに **New repository secret** をクリックします。

    ![Select setting action](../../../../getting_started/github-actions-guide/imgs/select-setting-action.png) *(画像参照: シークレット追加箇所)*

**必須 AI サービスシークレット（前提条件に応じて該当するものをすべて追加してください）:**

| シークレット名                       | 説明                                   | 値の提供元                      |
| :---------------------------------- | :------------------------------------ | :------------------------------ |
| `AZURE_SUBSCRIPTION_KEY`            | Azure AI サービス（Computer Vision）用キー  | ご自身の Azure AI Foundry        |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI サービス（Computer Vision）用エンドポイント | ご自身の Azure AI Foundry        |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI サービス用キー              | ご自身の Azure AI Foundry        |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI サービス用エンドポイント     | ご自身の Azure AI Foundry        |
| `AZURE_OPENAI_MODEL_NAME`           | Azure OpenAI モデル名                    | ご自身の Azure AI Foundry        |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Azure OpenAI デプロイメント名              | ご自身の Azure AI Foundry        |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI API バージョン              | ご自身の Azure AI Foundry        |
| `OPENAI_API_KEY`                    | OpenAI API キー                       | ご自身の OpenAI プラットフォーム |
| `OPENAI_ORG_ID`                     | OpenAI 組織 ID（任意）                   | ご自身の OpenAI プラットフォーム |
| `OPENAI_CHAT_MODEL_ID`              | 特定の OpenAI モデル ID（任意）           | ご自身の OpenAI プラットフォーム |
| `OPENAI_BASE_URL`                   | カスタム OpenAI API ベース URL（任意）     | ご自身の OpenAI プラットフォーム |

### ステップ 3: ワークフロー権限の設定

GitHub Action は、`GITHUB_TOKEN` を通じてコードのチェックアウトやプルリクエスト作成の権限が必要です。

1. リポジトリの **Settings** > **Actions** > **General** に移動します。  
2. 下にスクロールして **Workflow permissions** セクションを見つけます。  
3. **Read and write permissions** を選択します。これにより、`GITHUB_TOKEN` にこのワークフローに必要な `contents: write` と `pull-requests: write` の権限が付与されます。  
4. **Allow GitHub Actions to create and approve pull requests** のチェックボックスがオンになっていることを確認します。  
5. **Save** をクリックします。

![Permission setting](../../../../getting_started/github-actions-guide/imgs/permission-setting.png)

### ステップ 4: ワークフローファイルの作成

最後に、`GITHUB_TOKEN` を使った自動ワークフローを定義する YAML ファイルを作成します。

1. リポジトリのルートディレクトリに、`.github/workflows/` フォルダーがなければ作成します。  
2. `.github/workflows/` の中に `co-op-translator.yml` という名前のファイルを作成します。  
3. 以下の内容を `co-op-translator.yml` に貼り付けます。

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
          AZURE_SUBSCRIPTION_KEY: ${{ secrets.AZURE_SUBSCRIPTION_KEY }}
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
4. **ワークフローのカスタマイズ:**  
  - **[!IMPORTANT] 対象言語:** 必要に応じて `Run Co-op Translator` step, you **MUST review and modify the list of language codes** within the `translate -l "..." -y` command to match your project's requirements. The example list (`ar de es...`) needs to be replaced or adjusted.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see commented example in the YAML) to run the workflow only when relevant files (e.g., source documentation) change, saving runner minutes.
  - **PR Details:** Customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request` ステップ内の言語リストを調整してください。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されています。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご承知おきください。原文の言語による原本が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。