<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9fac847815936ef6e6c8bfde6d191571",
  "translation_date": "2025-10-15T02:39:23+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-org.md",
  "language_code": "ja"
}
-->
# Co-op Translator GitHub Action の利用方法（組織向けガイド）

**対象読者:** このガイドは、**Microsoft 社内ユーザー**や、事前構築済みの Co-op Translator GitHub App の必要な認証情報にアクセスできるチーム、または独自のカスタム GitHub App を作成できる方を対象としています。

Co-op Translator GitHub Action を使えば、リポジトリのドキュメント翻訳を自動化できます。このガイドでは、ソースの Markdown ファイルや画像が変更された際に、自動で翻訳を更新し、プルリクエストを作成する設定手順を説明します。

> [!IMPORTANT]
> 
> **ガイドの選び方:**
>
> このガイドは、**GitHub App ID とプライベートキー**を使ったセットアップ方法を説明しています。通常、以下の場合にこの「組織向けガイド」が必要です：**`GITHUB_TOKEN` の権限が制限されている場合:** 組織やリポジトリの設定で、標準の `GITHUB_TOKEN` に付与されるデフォルト権限が制限されている場合です。特に、`GITHUB_TOKEN` に必要な `write` 権限（例: `contents: write` や `pull-requests: write`）が許可されていない場合、[パブリックセットアップガイド](./github-actions-guide-public.md) のワークフローは権限不足で失敗します。専用の GitHub App を使い、明示的に権限を付与することでこの制限を回避できます。
>
> **上記が当てはまらない場合:**
>
> 標準の `GITHUB_TOKEN` がリポジトリで十分な権限を持っている場合（組織の制限でブロックされていない場合）、**[GITHUB_TOKEN を使ったパブリックセットアップガイド](./github-actions-guide-public.md)** をご利用ください。パブリックガイドでは App ID やプライベートキーの取得・管理は不要で、標準の `GITHUB_TOKEN` とリポジトリ権限のみで動作します。

## 前提条件

GitHub Action の設定前に、必要な AI サービスの認証情報を用意してください。

**1. 必須: AI 言語モデルの認証情報**
サポートされているいずれかの言語モデルの認証情報が必要です。

- **Azure OpenAI**: Endpoint、API Key、Model/Deployment 名、API Version が必要です。
- **OpenAI**: API Key（オプションで Org ID、Base URL、Model ID）。
- 詳細は [サポートされているモデルとサービス](../../../../README.md) を参照してください。
- セットアップガイド: [Azure OpenAI のセットアップ](../set-up-resources/set-up-azure-openai.md)。

**2. オプション: コンピュータビジョン認証情報（画像翻訳用）**

- 画像内テキストの翻訳が必要な場合のみ必要です。
- **Azure Computer Vision**: Endpoint と Subscription Key が必要です。
- 未設定の場合、アクションは [Markdown のみモード](../markdown-only-mode.md) で動作します。
- セットアップガイド: [Azure Computer Vision のセットアップ](../set-up-resources/set-up-azure-computer-vision.md)。

## セットアップと構成

以下の手順で、リポジトリに Co-op Translator GitHub Action を設定します。

### ステップ 1: GitHub App 認証のインストールと設定

このワークフローは、GitHub App 認証を使ってリポジトリと安全にやり取りします（例: プルリクエストの作成）。以下のいずれかを選択してください。

#### **オプションA: 事前構築済み Co-op Translator GitHub App のインストール（Microsoft 社内向け）**

1. [Co-op Translator GitHub App](https://github.com/apps/co-op-translator) ページにアクセスします。

1. **Install** を選択し、対象リポジトリがあるアカウントまたは組織を選びます。

    ![Install app](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.ja.png)

1. **Only select repositories** を選択し、対象リポジトリ（例: `PhiCookBook`）を選択して **Install** をクリックします。認証を求められる場合があります。

    ![Install authorize](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.ja.png)

1. **アプリ認証情報の取得（社内手続きが必要）:** ワークフローがアプリとして認証するために、Co-op Translator チームから以下2つの情報を入手してください。
  - **App ID:** Co-op Translator アプリの一意の識別子。App ID は `1164076` です。
  - **プライベートキー:** メンテナーから `.pem` プライベートキーファイルの**全内容**を取得してください。このキーはパスワード同様に厳重に管理してください。

1. ステップ2へ進みます。

#### **オプションB: 独自のカスタム GitHub App を利用する場合**

- 必要に応じて独自の GitHub App を作成・設定できます。Contents と Pull requests への Read & write 権限が必要です。App ID と生成したプライベートキーが必要です。

### ステップ 2: リポジトリシークレットの設定

GitHub App の認証情報と AI サービスの認証情報を、リポジトリの暗号化シークレットとして追加します。

1. 対象の GitHub リポジトリ（例: `PhiCookBook`）にアクセスします。

1. **Settings** > **Secrets and variables** > **Actions** に進みます。

1. **Repository secrets** の下で、下記の各シークレットごとに **New repository secret** をクリックします。

   ![Select setting action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.ja.png)

**必須シークレット（GitHub App 認証用）:**

| シークレット名         | 説明                                         | 値の取得元                                   |
| :------------------- | :------------------------------------------ | :------------------------------------------ |
| `GH_APP_ID`          | GitHub App の App ID（ステップ1で取得）      | GitHub App 設定                             |
| `GH_APP_PRIVATE_KEY` | ダウンロードした `.pem` ファイルの**全内容** | ステップ1で取得した `.pem` ファイル         |

**AI サービス用シークレット（前提条件に応じて該当するものすべて追加）:**

| シークレット名                         | 説明                                   | 値の取得元                     |
| :---------------------------------- | :------------------------------------ | :----------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Azure AI Service（Computer Vision）用キー  | Azure AI Foundry                |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Service（Computer Vision）用エンドポイント | Azure AI Foundry                |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI サービス用キー           | Azure AI Foundry                |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI サービス用エンドポイント | Azure AI Foundry                |
| `AZURE_OPENAI_MODEL_NAME`           | Azure OpenAI モデル名                 | Azure AI Foundry                |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Azure OpenAI デプロイメント名         | Azure AI Foundry                |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI の API バージョン         | Azure AI Foundry                |
| `OPENAI_API_KEY`                    | OpenAI 用 API キー                    | OpenAI Platform                 |
| `OPENAI_ORG_ID`                     | OpenAI 組織 ID                        | OpenAI Platform                 |
| `OPENAI_CHAT_MODEL_ID`              | OpenAI の特定モデル ID                | OpenAI Platform                 |
| `OPENAI_BASE_URL`                   | カスタム OpenAI API Base URL          | OpenAI Platform                 |

![Enter environment variable name](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.ja.png)

### ステップ 3: ワークフローファイルの作成

最後に、自動化ワークフローを定義する YAML ファイルを作成します。

1. リポジトリのルートディレクトリに `.github/workflows/` ディレクトリがなければ作成します。

1. `.github/workflows/` 内に `co-op-translator.yml` というファイルを作成します。

1. 下記の内容を co-op-translator.yml に貼り付けます。

```
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
          # Azure AI Service Credentials
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}

          # Azure OpenAI Credentials
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}

          # OpenAI Credentials
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

      - name: Authenticate GitHub App
        id: generate_token
        uses: tibdex/github-app-token@v1
        with:
          app_id: ${{ secrets.GH_APP_ID }}
          private_key: ${{ secrets.GH_APP_PRIVATE_KEY }}

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ steps.generate_token.outputs.token }}
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
  - **[!IMPORTANT] 対象言語:** `Run Co-op Translator` ステップ内の `translate -l "..." -y` コマンドの言語コードリストは、**必ずご自身のプロジェクト要件に合わせて見直し・修正してください**。例のリスト（`ar de es...`）はそのままではなく、必要に応じて変更してください。
  - **トリガー（`on:`）:** 現在の設定では `main` への push 毎に実行されます。大規模リポジトリの場合は、YAML 内コメント例のように `paths:` フィルターを追加し、関連ファイル（例: ドキュメントソース）の変更時のみワークフローが走るようにすると、ランナーの消費を抑えられます。
  - **PR 詳細:** `Create Pull Request` ステップの `commit-message`、`title`、`body`、`branch` 名や `labels` も必要に応じてカスタマイズしてください。

## 認証情報の管理と更新

- **セキュリティ:** 機密性の高い認証情報（API キーやプライベートキー）は必ず GitHub Actions シークレットとして保存し、ワークフローファイルやリポジトリコード内で公開しないでください。
- **[!IMPORTANT] キーの更新（Microsoft 社内ユーザー向け）:** Microsoft 内で利用する Azure OpenAI キーには定期的な更新ポリシー（例: 5ヶ月ごと）がある場合があります。ワークフロー停止を防ぐため、該当する GitHub シークレット（`AZURE_OPENAI_...` キー）は**有効期限前に必ず更新**してください。

## ワークフローの実行

> [!WARNING]  
> **GitHub ホストランナーの時間制限:**  
> `ubuntu-latest` などの GitHub ホストランナーには**最大6時間の実行時間制限**があります。  
> 大規模なドキュメントリポジトリの場合、翻訳処理が6時間を超えるとワークフローは自動的に終了します。  
> これを防ぐには:  
> - **セルフホストランナー**の利用（時間制限なし）  
> - 1回の実行で対象言語数を減らす

`co-op-translator.yml` ファイルが main ブランチ（または `on:` トリガーで指定したブランチ）にマージされると、そのブランチへの push（および `paths` フィルターに一致する場合）で自動的にワークフローが実行されます。

翻訳が生成・更新された場合、アクションは自動で変更内容を含むプルリクエストを作成し、レビュー・マージの準備が整います。

---

**免責事項**：  
本書類は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な表現が含まれる場合がありますのでご注意ください。原文（元の言語の文書）が正式な情報源となります。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用によって生じたいかなる誤解や誤認についても、当方は責任を負いかねます。