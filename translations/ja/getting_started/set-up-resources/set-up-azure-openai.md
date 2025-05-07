<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10d8cb07ad0d2ee6705439d4e382ecc9",
  "translation_date": "2025-05-06T18:14:49+00:00",
  "source_file": "getting_started/set-up-resources/set-up-azure-openai.md",
  "language_code": "ja"
}
-->
# Set up Azure OpenAI for language translation

## Azure AI FoundryでAzure OpenAIリソースを作成する

Azure AI FoundryでAzure OpenAIを設定するには、以下の手順に従ってください。

### ハブの作成

1. [Azure AI Foundryポータル](https://ai.azure.com)にサインインする：Azureアカウントでサインインしていることを確認してください。

2. 管理センターに移動する：ホームページの左メニューから「Management Center」を選択します。

3. 新しいハブを作成する：「+ New hub」をクリックし、サブスクリプション、リソースグループ、ハブ名など必要な情報を入力します。Cognitive VisionやGPTモデルをサポートしているEast USリージョンへの展開を推奨します。

4. 内容を確認して作成する：内容を確認し、「Create」をクリックしてハブを作成します。

### プロジェクトの作成

1. ホームページに移動する：まだホームページにいない場合は、ページ左上の「Azure AI Foundry」を選択してホームページに戻ります。

2. プロジェクトを作成する：「+ Create project」をクリックし、プロジェクト名を入力します。

3. ハブを選択する：複数のハブがある場合は使用したいハブを選びます。新しいハブを作成したい場合は、このステップで作成可能です。

4. プロジェクトを設定する：案内に従ってプロジェクトを必要に応じて設定します。

5. プロジェクトを作成する：「Create」をクリックして設定を完了します。

### OpenAIモデルのモデルとエンドポイントのデプロイ

1. [Azure AI Foundryポータル](https://ai.azure.com)にサインインする：Azure OpenAI Serviceリソースを含むAzureサブスクリプションでサインインしていることを確認してください。

2. モデルとエンドポイントに移動する：Azure AI Foundryのホームページから、「Let's go.」または左メニューの「Model and Endpoints」を選択します。

3. まだGPTモデルをデプロイしていない場合は、モデルをデプロイを選択：GPT-4o、GPT-4o-mini、またはo3-miniのいずれかのモデルを推奨します。

4. リソースにアクセスする：既存のAzure OpenAI Serviceリソースが表示されます。複数ある場合は、使用したいリソースを選択してください。

詳細な手順については、公式のAzure AI Foundryドキュメントをご参照ください。

[How to Create a project](https://learn.microsoft.com/azure/ai-studio/how-to/create-project)

[How to Create resources](https://learn.microsoft.com/azure/ai-studio/how-to/create-azure-ai-resource)

[How to use OpenAI Model in AI Foundry](https://learn.microsoft.com/azure/ai-studio/ai-services/how-to/connect-azure-openai)

[OpenAI Services in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/azure-openai-in-ai-studio)

**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。正式な情報源としては、原文のオリジナル文書を参照してください。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。