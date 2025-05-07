<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "53c99ea0ead7a3500149d4bb96be5811",
  "translation_date": "2025-05-06T17:54:21+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "fr"
}
-->
# Créez le fichier *.env* à la racine du répertoire

Dans ce tutoriel, nous allons vous guider pour configurer vos variables d’environnement pour les services Azure à l’aide d’un fichier *.env*. Les variables d’environnement vous permettent de gérer en toute sécurité des informations sensibles, comme des clés API, sans les coder en dur dans votre base de code.

> [!IMPORTANT]
> - Un seul service de modèle de langage (Azure OpenAI ou OpenAI) doit être configuré. Remplissez les variables d’environnement pour le service que vous préférez. Si plusieurs variables d’environnement pour différents modèles de langage sont définies, le traducteur coopératif en choisira une selon la priorité.
> - Si les variables d’environnement Computer Vision ne sont pas configurées, le traducteur basculera automatiquement en [mode Markdown uniquement](./markdown-only-mode.md).

> [!NOTE]
> Ce guide se concentre principalement sur les services Azure, mais vous pouvez choisir n’importe quel modèle de langage supporté dans la [liste des modèles et services supportés](../README.md#-supported-models-and-services).

## Créez le fichier *.env*

À la racine de votre projet, créez un fichier nommé *.env*. Ce fichier contiendra toutes vos variables d’environnement dans un format simple.

> [!WARNING]
> Ne validez pas votre fichier *.env* dans les systèmes de gestion de version comme Git. Ajoutez *.env* à votre fichier .gitignore pour éviter toute validation accidentelle.

1. Rendez-vous à la racine de votre projet.

1. Créez un fichier *.env* à la racine de votre projet.

    ![Créer le fichier *.env*.](../../../../imgs/create-env.png)

1. Ouvrez le fichier *.env* et collez le modèle suivant :

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

## Récupérez vos identifiants Azure

Vous aurez besoin des identifiants Azure suivants pour configurer l’environnement :

Vous pouvez obtenir tous les détails depuis la page d’aperçu du projet dans [AI Foundry](https://ai.azure.com/build/overview)

![Aperçu Foundry](../../../../imgs/foundry-overview.png)

### Pour le service Azure AI :

    - Clé d’abonnement Azure : votre clé API des services Azure AI, qui vous permet d’accéder aux services Azure AI.
    - Endpoint du service Azure AI : l’URL de point de terminaison pour votre service Azure AI spécifique.

### Pour le service Azure OpenAI :

    - Clé API Azure OpenAI : la clé API pour accéder aux services Azure OpenAI.
    - Endpoint Azure OpenAI : l’URL de point de terminaison pour votre service Azure OpenAI.

1. Copiez et collez votre clé et endpoint AI Services dans le fichier *.env*.
2. Copiez et collez votre clé API Azure OpenAI et l’endpoint dans le fichier *.env*.

### Détails du modèle

Sélectionnez Modèle et Endpoints dans le menu de gauche

![Modèles Foundry](../../../../imgs/gpt-models.png)

Vous devez maintenant choisir le modèle que vous souhaitez utiliser pour obtenir les détails du modèle

![Détails du modèle](../../../../imgs/model-deployment-name.png)

Pour le fichier .env, nous avons besoin des informations suivantes

    - Nom du modèle Azure OpenAI : le nom du modèle avec lequel vous interagirez.
    - Nom Azure OpenAI : le nom de votre déploiement pour les modèles Azure OpenAI.
    - Version API Azure OpenAI : la version de l’API Azure OpenAI que vous utilisez, visible à la fin de la chaîne URL.

Pour obtenir ces informations, sélectionnez le déploiement du modèle

![Infos modèle Foundry](../../../../imgs/foundry-model-info.png)

### Ajoutez les variables d’environnement Azure

3. Copiez et collez votre **Nom** Azure OpenAI et la **Version** du modèle dans le fichier *.env*.
4. Enregistrez le fichier *.env*.
5. Vous pouvez désormais accéder à ces variables d’environnement pour utiliser **Co-op Translator** avec vos services Azure.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.