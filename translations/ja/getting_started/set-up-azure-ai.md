<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "220341925e9a67a0e467d1ba94d3cf7d",
  "translation_date": "2025-05-07T14:18:02+00:00",
  "source_file": "getting_started/set-up-azure-ai.md",
  "language_code": "ja"
}
-->
# Co-op Translator 用 Azure AI のセットアップ (Azure OpenAI & Azure AI Vision)

このガイドでは、Azure AI Foundry 内で言語翻訳用の Azure OpenAI と、画像コンテンツ解析（画像ベースの翻訳に利用可能）用の Azure Computer Vision のセットアップ手順を説明します。

**前提条件:**
- 有効なサブスクリプションを持つ Azure アカウント
- Azure サブスクリプション内でリソースやデプロイメントを作成するための十分な権限

## Azure AI プロジェクトの作成

まず、AI リソースを一元管理するための Azure AI プロジェクトを作成します。

1. [https://ai.azure.com](https://ai.azure.com) にアクセスし、Azure アカウントでサインインします。

1. **+Create** を選択して新しいプロジェクトを作成します。

1. 以下の項目を入力します:
   - **Project name**（例: `CoopTranslator-Project`）
   - **AI hub** を選択（例: `CoopTranslator-Hub`）（必要に応じて新規作成）

1. "**Review and Create**" をクリックしてプロジェクトを作成します。プロジェクトの概要ページに移動します。

## 言語翻訳用 Azure OpenAI のセットアップ

プロジェクト内で、テキスト翻訳のバックエンドとして Azure OpenAI モデルをデプロイします。

### プロジェクトに移動

まだであれば、作成したプロジェクト（例: `CoopTranslator-Project`）を Azure AI Foundry で開きます。

### OpenAI モデルのデプロイ

1. プロジェクトの左メニューの「My assets」から "**Models + endpoints**" を選択します。

1. **+ Deploy model** を選択します。

1. **Deploy Base Model** を選択します。

1. 利用可能なモデルの一覧が表示されます。適切な GPT モデルをフィルターまたは検索します。おすすめは `gpt-4o` です。

1. 希望のモデルを選択し、**Confirm** をクリックします。

1. **Deploy** を選択します。

### Azure OpenAI の設定

デプロイ完了後、"**Models + endpoints**" ページから該当デプロイメントを選択すると、**REST endpoint URL**、**Key**、**Deployment name**、**Model name**、**API version** が確認できます。これらは翻訳モデルをアプリケーションに統合する際に必要です。

## 画像翻訳用 Azure Computer Vision のセットアップ

画像内のテキスト翻訳を可能にするため、Azure AI Service の API キーとエンドポイントを取得します。

1. Azure AI プロジェクト（例: `CoopTranslator-Project`）に移動し、プロジェクトの概要ページにいることを確認します。

### Azure AI Service の設定

Azure AI Service タブから API キーとエンドポイントを確認します。

1. Azure AI プロジェクト（例: `CoopTranslator-Project`）の概要ページにアクセスします。

1. Azure AI Service タブで **API Key** と **Endpoint** を探します。

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

この接続により、リンクされた Azure AI Services リソースの機能（画像解析を含む）が AI Foundry プロジェクトで利用可能になります。これをノートブックやアプリケーションで使用し、画像からテキストを抽出、その後 Azure OpenAI モデルへ送信して翻訳できます。

## 資格情報のまとめ

ここまでで以下の情報を取得できているはずです。

**Azure OpenAI（テキスト翻訳用）:**
- Azure OpenAI エンドポイント
- Azure OpenAI API キー
- Azure OpenAI モデル名（例: `gpt-4o`）
- Azure OpenAI デプロイメント名（例: `cooptranslator-gpt4o`）
- Azure OpenAI API バージョン

**Azure AI Services（Vision による画像テキスト抽出用）:**
- Azure AI Service エンドポイント
- Azure AI Service API キー

### 例: 環境変数の設定（プレビュー）

後でアプリケーションを構築する際に、これらの資格情報を環境変数として設定することが多いでしょう。例えば以下のように設定します。

```bash
# Azure AI Service Credentials (Required for image translation)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # e.g., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Azure OpenAI Credentials (Required for text translation)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # e.g., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # e.g., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # e.g., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # e.g., 2024-02-01
```

---

### 参考リンク

- [Azure AI Foundry でのプロジェクト作成方法](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI リソースの作成方法](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundry での OpenAI モデルのデプロイ方法](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

**免責事項**:  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されています。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご了承ください。原文はあくまで正式な情報源とみなされるべきです。重要な情報については、専門の人間翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は一切責任を負いかねます。