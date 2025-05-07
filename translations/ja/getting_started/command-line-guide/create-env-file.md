<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "53c99ea0ead7a3500149d4bb96be5811",
  "translation_date": "2025-05-06T17:53:40+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "ja"
}
-->
# ルートディレクトリに*.env*ファイルを作成する

このチュートリアルでは、*.env*ファイルを使ってAzureサービスの環境変数を設定する方法を案内します。環境変数を使うことで、APIキーなどの機密情報をコードに直接書き込まずに安全に管理できます。

> [!IMPORTANT]
> - 設定する言語モデルサービスはAzure OpenAIかOpenAIのどちらか一方だけで構いません。利用したいサービスの環境変数を入力してください。複数の言語モデルの環境変数が設定されている場合、Co-op Translatorは優先順位に基づいて一つを選択します。
> - Computer Visionの環境変数が設定されていない場合、翻訳機能は自動的に[Markdown-onlyモード](./markdown-only-mode.md)に切り替わります。

> [!NOTE]
> このガイドは主にAzureサービスに焦点を当てていますが、[対応モデルとサービスの一覧](../README.md#-supported-models-and-services)から任意の対応言語モデルを選択可能です。

## *.env*ファイルを作成する

プロジェクトのルートディレクトリに*.env*という名前のファイルを作成してください。このファイルに環境変数をシンプルな形式で保存します。

> [!WARNING]
> *.env*ファイルをGitなどのバージョン管理システムにコミットしないでください。誤ってコミットしないように、*.env*を.gitignoreに追加してください。

1. プロジェクトのルートディレクトリに移動します。

1. ルートディレクトリに*.env*ファイルを作成します。

    ![Create *.env* file.](../../../../imgs/create-env.png)

1. *.env*ファイルを開き、以下のテンプレートを貼り付けます。

    ```plaintext
    # Azure Credentials
    AZURE_SUBSCRIPTION_KEY="your_azure_AIServices_api_key"
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

## Azureの認証情報を用意する

環境変数を設定するために、以下のAzure認証情報が必要です。

[AI Foundry](https://ai.azure.com/build/overview)のプロジェクト概要ページからすべての情報を取得できます。

![Foundry-overview](../../../../imgs/foundry-overview.png)


### Azure AI Serviceの場合：

    - Azure Subscription Key: Azure AIサービスにアクセスするためのAPIキー。
    - Azure AI Service Endpoint: 利用するAzure AIサービスのエンドポイントURL。

### Azure OpenAI Serviceの場合：

    - Azure OpenAI API Key: Azure OpenAIサービスにアクセスするためのAPIキー。
    - Azure OpenAI Endpoint: Azure OpenAIサービスのエンドポイントURL。


1. AI Servicesのキーとエンドポイントを*.env*ファイルにコピー＆ペーストします。
2. Azure OpenAIのAPIキーとエンドポイントを*.env*ファイルにコピー＆ペーストします。

### モデルの詳細

左側のメニューからModelとEndpointsを選択します。

![FoundryModels](../../../../imgs/gpt-models.png)

利用したいモデルを選択して、モデルの詳細を確認します。

![ModelDetails](../../../../imgs/model-deployment-name.png)

*.env*ファイルに必要な情報は以下の通りです。

    - Azure OpenAI Model Name: 使用するモデルの名前。
    - Azure OpenAI Name: Azure OpenAIモデルのデプロイメント名。
    - Azure OpenAI API Version: URLの末尾にあるAzure OpenAI APIのバージョン。

これらの情報はモデルのデプロイメントを選択すると確認できます。

![FoundryModelinfo](../../../../imgs/foundry-model-info.png)

### Azure環境変数を追加する

3. Azure OpenAIの**Name**とモデルの**Version**を*.env*ファイルにコピー＆ペーストします。
4. *.env*ファイルを保存します。
5. これでAzureサービスを使って**Co-op Translator**を利用するための環境変数が設定できました。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されています。正確性の確保に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご理解ください。原文の言語によるオリジナル文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。