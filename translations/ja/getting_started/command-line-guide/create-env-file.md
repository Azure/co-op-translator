<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-05-07T13:59:13+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "ja"
}
-->
# ルートディレクトリに*.env*ファイルを作成する

このチュートリアルでは、*.env*ファイルを使ってAzureサービスの環境変数を設定する方法を案内します。環境変数を利用することで、APIキーなどの機密情報をコードに直接書き込まずに安全に管理できます。

> [!IMPORTANT]
> - 言語モデルサービスはAzure OpenAIかOpenAIのいずれか一つだけ設定すれば十分です。使用したいサービスの環境変数を入力してください。複数の言語モデルの環境変数が設定されている場合は、コ・オプ翻訳機能が優先順位に基づいて一つを選択します。
> - Computer Visionの環境変数が設定されていない場合、翻訳機能は自動的に[Markdown-onlyモード](./markdown-only-mode.md)に切り替わります。

> [!NOTE]
> このガイドは主にAzureサービスに焦点を当てていますが、[対応モデルとサービス一覧](../README.md#-supported-models-and-services)から任意のサポートされている言語モデルを選択することも可能です。

## *.env*ファイルを作成する

プロジェクトのルートディレクトリに*.env*という名前のファイルを作成します。このファイルに環境変数をシンプルな形式で保存します。

> [!WARNING]
> *.env*ファイルはGitなどのバージョン管理システムにコミットしないでください。誤ってコミットしないように、.gitignoreファイルに*.env*を追加してください。

1. プロジェクトのルートディレクトリに移動します。

1. ルートディレクトリに*.env*ファイルを作成します。

1. *.env*ファイルを開き、以下のテンプレートを貼り付けます。

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
> APIキーやエンドポイントの確認方法については、[set-up-azure-ai.md](../set-up-azure-ai.md)を参照してください。

**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されています。正確性の確保に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の母国語版が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤訳について、一切の責任を負いかねますのでご了承ください。