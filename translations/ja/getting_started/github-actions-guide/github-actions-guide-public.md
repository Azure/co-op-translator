<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a52587a512e667f70d92db853d3c61d5",
  "translation_date": "2025-06-12T19:24:27+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "ja"
}
-->
# Co-op Translator GitHub Actionの使い方（パブリックセットアップ）

**対象ユーザー:** このガイドは、標準のGitHub Actions権限で十分なほとんどのパブリックまたはプライベートリポジトリのユーザーを対象としています。組み込みの`GITHUB_TOKEN`を利用します。

Co-op Translator GitHub Actionを使って、リポジトリのドキュメント翻訳を簡単に自動化しましょう。このガイドでは、ソースのMarkdownファイルや画像が変更されるたびに、更新された翻訳を含むプルリクエストを自動で作成するアクションの設定方法を説明します。

> [!IMPORTANT]
>
> **適切なガイドの選択について：**
>
> 本ガイドは、**標準の`GITHUB_TOKEN`を使ったより簡単なセットアップ方法**を詳述しています。これは多くのユーザーに推奨される方法で、GitHub Appの秘密鍵を管理する必要がありません。
>

## 前提条件

GitHub Actionを設定する前に、必要なAIサービスの認証情報を用意してください。

**1. 必須: AI言語モデルの認証情報**  
サポートされているいずれかの言語モデルの認証情報が必要です：

- **Azure OpenAI**: エンドポイント、APIキー、モデル/デプロイメント名、APIバージョンが必要です。  
- **OpenAI**: APIキー、（任意で）組織ID、ベースURL、モデルIDが必要です。  
- 詳細は[Supported Models and Services](../../../../README.md)を参照してください。

**2. 任意: AI Vision認証情報（画像翻訳用）**

- 画像内のテキスト翻訳が必要な場合のみ。  
- **Azure AI Vision**: エンドポイントとサブスクリプションキーが必要です。  
- 提供しない場合は、アクションは[Markdownのみモード](../markdown-only-mode.md)で動作します。

## セットアップと設定

標準の`GITHUB_TOKEN`を使って、リポジトリにCo-op Translator GitHub Actionを設定する手順を説明します。

### ステップ1: 認証の理解（`GITHUB_TOKEN`の使用）

このワークフローはGitHub Actionsが提供する組み込みの`GITHUB_TOKEN`を使用します。このトークンは、**ステップ3**で設定する権限に基づいて、自動的にワークフローにリポジトリへのアクセス権を付与します。

### ステップ2: リポジトリのシークレットを設定する

リポジトリの設定で、**AIサービスの認証情報**を暗号化されたシークレットとして追加するだけでOKです。

1. 対象のGitHubリポジトリにアクセスします。  
2. **Settings** > **Secrets and variables** > **Actions** に移動します。  
3. **Repository secrets**の下で、必要なAIサービスのシークレットごとに**New repository secret**をクリックして追加します。

    ![Select setting action](../../../../translated_images/select-setting-action.32e2394813d09dc148494f34daea40724f24ff406de889f26cbbbf05f98ed621.ja.png) *(画像参照: シークレット追加箇所)*

**必要なAIサービスのシークレット（前提条件に応じてすべて追加してください）：**

| シークレット名                         | 説明                                     | 値の提供元                       |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_SUBSCRIPTION_KEY`            | Azure AIサービス（コンピュータビジョン）のキー | ご利用のAzure AI Foundry          |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AIサービス（コンピュータビジョン）のエンドポイント | ご利用のAzure AI Foundry          |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAIサービスのキー                  | ご利用のAzure AI Foundry          |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAIサービスのエンドポイント         | ご利用のAzure AI Foundry          |
| `AZURE_OPENAI_MODEL_NAME`           | Azure OpenAIモデル名                         | ご利用のAzure AI Foundry          |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Azure OpenAIデプロイメント名                 | ご利用のAzure AI Foundry          |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAIのAPIバージョン                   | ご利用のAzure AI Foundry          |
| `OPENAI_API_KEY`                    | OpenAIのAPIキー                            | ご利用のOpenAIプラットフォーム     |
| `OPENAI_ORG_ID`                     | OpenAI組織ID（任意）                         | ご利用のOpenAIプラットフォーム     |
| `OPENAI_CHAT_MODEL_ID`              | 特定のOpenAIモデルID（任意）                   | ご利用のOpenAIプラットフォーム     |
| `OPENAI_BASE_URL`                   | カスタムOpenAI APIベースURL（任意）             | ご利用のOpenAIプラットフォーム     |

### ステップ3: ワークフローの権限を設定する

GitHub Actionがコードのチェックアウトやプルリクエストの作成を行うために、`GITHUB_TOKEN`に適切な権限を付与する必要があります。

1. リポジトリの **Settings** > **Actions** > **General** に移動します。  
2. 下にスクロールして**Workflow permissions**セクションを探します。  
3. **Read and write permissions**を選択します。これにより、`GITHUB_TOKEN`にこのワークフローに必要な`contents: write`と`pull-requests: write`の権限が付与されます。  
4. **Allow GitHub Actions to create and approve pull requests**のチェックボックスがオンになっていることを確認します。  
5. **Save**をクリックします。

![Permission setting](../../../../translated_images/permission-setting.cb1f57fdb5194f0743b1f6932f221e404ae2928ee88d77f1de39aba46fbf774a.ja.png)

### ステップ4: ワークフローファイルを作成する

最後に、`GITHUB_TOKEN`を使った自動化ワークフローを定義するYAMLファイルを作成します。

1. リポジトリのルートディレクトリに`.github/workflows/`ディレクトリがなければ作成します。  
2. `.github/workflows/`内に`co-op-translator.yml`という名前のファイルを作成します。  
3. `co-op-translator.yml`に以下の内容を貼り付けます。

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
  - **[!IMPORTANT] 対象言語:** 必要に応じて`Run Co-op Translator` step, you **MUST review and modify the list of language codes** within the `translate -l "..." -y` command to match your project's requirements. The example list (`ar de es...`) needs to be replaced or adjusted.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see commented example in the YAML) to run the workflow only when relevant files (e.g., source documentation) change, saving runner minutes.
  - **PR Details:** Customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request`ステップ内の言語指定を変更してください。

**免責事項**:  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈の相違についても、当方は責任を負いかねます。