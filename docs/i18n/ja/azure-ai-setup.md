# Azure AI セットアップ

Use this guide when you want to configure Azure OpenAI for text translation and Azure AI Vision for image text extraction.

## Prerequisites

- Azure サブスクリプション。
- Azure AI リソースおよびモデルのデプロイを作成または使用する権限。
- Azure AI Foundry のプロジェクト、または Azure OpenAI と Azure AI Vision リソースへの同等のアクセス。

## Create an Azure AI Project

1. [Azure AI Foundry](https://ai.azure.com) を開きます。
2. プロジェクトを作成するか選択します。
3. プロジェクトのための AI ハブを作成するか選択します。
4. 作成後にプロジェクトの概要を開きます。

## Deploy an Azure OpenAI Model

1. プロジェクト内で **Models + endpoints** を開きます。
2. **Deploy model** を選択します。
3. `gpt-4o` のような GPT モデルを選択します。
4. モデルをデプロイします。
5. エンドポイント、デプロイ名、モデル名、API キー、API バージョンを記録します。

!!! note
    Azure OpenAI の API バージョンは Azure AI Foundry に表示されるモデルのバージョンとは別物です。デプロイに対してサポートされている API バージョンを選択してください。

## Configure Azure AI Vision

画像翻訳では、翻訳する前にソース画像からテキストを抽出するために Azure AI Vision を使用します。

Azure AI プロジェクト内で、Azure AI Services のキーとエンドポイントを見つけます。

![Azure AI サービス情報の確認](../../assets/find-azure-ai-info.png)

Record:

- Azure AI Service のエンドポイント
- Azure AI Service の API キー

## Environment Variables

資格情報を `.env` ファイルまたは CI シークレットに追加します。

```bash
# 画像翻訳に必要な Azure AI Vision
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# テキスト翻訳に必要な Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator also supports optional fallback credential sets. Duplicate a complete provider set with suffixes such as `_1` or `_2`; all variables in a fallback set must share the same suffix.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Next Steps

- ローカルまたは CI の環境変数を設定するには [Configuration](configuration.md) に戻ってください。
- 翻訳コマンドについては [CLI Reference](cli.md) を使用してください。
- 翻訳のプルリクエストを自動化するには [GitHub Actions](github-actions.md) を使用してください。