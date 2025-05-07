<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-05-07T14:05:45+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "fr"
}
-->
# Créez le fichier *.env* à la racine du répertoire

Dans ce tutoriel, nous vous guiderons pour configurer vos variables d’environnement pour les services Azure en utilisant un fichier *.env*. Les variables d’environnement vous permettent de gérer en toute sécurité des informations sensibles, comme les clés API, sans les coder en dur dans votre base de code.

> [!IMPORTANT]
> - Un seul service de modèle de langage (Azure OpenAI ou OpenAI) doit être configuré. Remplissez les variables d’environnement pour le service que vous préférez. Si plusieurs variables pour différents modèles de langage sont définies, le traducteur coopératif en choisira un selon la priorité.
> - Si les variables d’environnement pour Computer Vision ne sont pas définies, le traducteur basculera automatiquement en [mode Markdown uniquement](./markdown-only-mode.md).

> [!NOTE]
> Ce guide se concentre principalement sur les services Azure, mais vous pouvez choisir n’importe quel modèle de langage pris en charge dans la [liste des modèles et services supportés](../README.md#-supported-models-and-services).

## Créez le fichier *.env*

À la racine de votre projet, créez un fichier nommé *.env*. Ce fichier contiendra toutes vos variables d’environnement dans un format simple.

> [!WARNING]
> Ne validez pas votre fichier *.env* dans un système de contrôle de version comme Git. Ajoutez *.env* à votre fichier .gitignore pour éviter des validations accidentelles.

1. Rendez-vous à la racine de votre projet.

1. Créez un fichier *.env* à la racine de votre projet.

1. Ouvrez le fichier *.env* et collez le modèle suivant :

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
> Si vous souhaitez retrouver vos clés API et points de terminaison, vous pouvez consulter [set-up-azure-ai.md](../set-up-azure-ai.md).

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.