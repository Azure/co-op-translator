<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-07-04T08:13:01+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "ja"
}
-->
# ルートディレクトリに*.env*ファイルを作成する

このチュートリアルでは、*.env*ファイルを使用してAzureサービスの環境変数を設定する方法を説明します。環境変数を使用すると、APIキーなどの機密情報をコードベースにハードコーディングすることなく安全に管理できます。

> [!IMPORTANT]
> - 設定が必要なのは、Azure OpenAIまたはOpenAIのいずれかの言語モデルサービスのみです。希望するサービスの環境変数を入力してください。複数の言語モデルの環境変数が設定されている場合、協力翻訳者は優先順位に基づいて1つを選択します。
> - Computer Visionの環境変数が設定されていない場合、翻訳者は自動的に[Markdown-onlyモード](./markdown-only-mode.md)に切り替わります。

> [!NOTE]
> このガイドは主にAzureサービスに焦点を当てていますが、[サポートされているモデルとサービスのリスト](../README.md#-supported-models-and-services)から任意のサポートされている言語モデルを選択できます。

## *.env*ファイルを作成する

プロジェクトのルートディレクトリに*.env*という名前のファイルを作成します。このファイルには、すべての環境変数が簡単な形式で保存されます。

> [!WARNING]
> *.env*ファイルをGitなどのバージョン管理システムにコミットしないでください。誤ってコミットしないように、*.env*を.gitignoreファイルに追加してください。

1. プロジェクトのルートディレクトリに移動します。

1. プロジェクトのルートディレクトリに*.env*ファイルを作成します。

1. *.env*ファイルを開き、次のテンプレートを貼り付けます：

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"
    ```

> [!NOTE]
> APIキーとエンドポイントを見つけたい場合は、[Azure AI のセットアップ方法](../set-up-azure-ai.md)を参照してください。

**免責事項**:
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知ください。元の言語での原文が信頼できる情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。
