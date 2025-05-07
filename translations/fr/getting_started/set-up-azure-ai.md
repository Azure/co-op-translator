<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "220341925e9a67a0e467d1ba94d3cf7d",
  "translation_date": "2025-05-07T14:18:54+00:00",
  "source_file": "getting_started/set-up-azure-ai.md",
  "language_code": "fr"
}
-->
# Configuration d’Azure AI pour Co-op Translator (Azure OpenAI & Azure AI Vision)

Ce guide vous accompagne dans la configuration d’Azure OpenAI pour la traduction linguistique et d’Azure Computer Vision pour l’analyse du contenu des images (qui peut ensuite être utilisé pour la traduction basée sur l’image) au sein d’Azure AI Foundry.

**Prérequis :**
- Un compte Azure avec un abonnement actif.
- Les permissions nécessaires pour créer des ressources et des déploiements dans votre abonnement Azure.

## Créer un projet Azure AI

Commencez par créer un projet Azure AI, qui servira de point central pour gérer vos ressources d’IA.

1. Rendez-vous sur [https://ai.azure.com](https://ai.azure.com) et connectez-vous avec votre compte Azure.

1. Sélectionnez **+Create** pour créer un nouveau projet.

1. Effectuez les actions suivantes :
   - Saisissez un **Nom de projet** (par exemple `CoopTranslator-Project`).
   - Sélectionnez le **AI hub** (par exemple `CoopTranslator-Hub`) (Créez-en un nouveau si nécessaire).

1. Cliquez sur "**Review and Create**" pour configurer votre projet. Vous serez redirigé vers la page de présentation de votre projet.

## Configurer Azure OpenAI pour la traduction linguistique

Dans votre projet, vous allez déployer un modèle Azure OpenAI qui servira de backend pour la traduction de texte.

### Accéder à votre projet

Si ce n’est pas déjà fait, ouvrez votre projet récemment créé (par exemple `CoopTranslator-Project`) dans Azure AI Foundry.

### Déployer un modèle OpenAI

1. Dans le menu de gauche de votre projet, sous "My assets", sélectionnez "**Models + endpoints**".

1. Cliquez sur **+ Deploy model**.

1. Choisissez **Deploy Base Model**.

1. Une liste des modèles disponibles s’affichera. Filtrez ou recherchez un modèle GPT adapté. Nous recommandons `gpt-4o`.

1. Sélectionnez le modèle souhaité et cliquez sur **Confirm**.

1. Cliquez sur **Deploy**.

### Configuration d’Azure OpenAI

Une fois déployé, vous pouvez sélectionner le déploiement depuis la page "**Models + endpoints**" pour retrouver son **URL de point de terminaison REST**, sa **clé**, le **nom du déploiement**, le **nom du modèle** et la **version de l’API**. Ces informations seront nécessaires pour intégrer le modèle de traduction dans votre application.

## Configurer Azure Computer Vision pour la traduction d’images

Pour activer la traduction du texte contenu dans les images, vous devez récupérer la clé API et le point de terminaison du service Azure AI.

1. Accédez à votre projet Azure AI (par exemple `CoopTranslator-Project`). Assurez-vous d’être sur la page de présentation du projet.

### Configuration du service Azure AI

Trouvez la clé API et le point de terminaison depuis le service Azure AI.

1. Accédez à votre projet Azure AI (par exemple `CoopTranslator-Project`). Assurez-vous d’être sur la page de présentation du projet.

1. Repérez la **clé API** et le **point de terminaison** dans l’onglet Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Cette connexion rend les fonctionnalités de la ressource Azure AI Services associée (y compris l’analyse d’image) disponibles dans votre projet AI Foundry. Vous pourrez alors utiliser cette connexion dans vos notebooks ou applications pour extraire le texte des images, qui pourra ensuite être envoyé au modèle Azure OpenAI pour traduction.

## Regroupement de vos identifiants

À ce stade, vous devriez avoir rassemblé les éléments suivants :

**Pour Azure OpenAI (Traduction de texte) :**
- Point de terminaison Azure OpenAI
- Clé API Azure OpenAI
- Nom du modèle Azure OpenAI (par exemple `gpt-4o`)
- Nom du déploiement Azure OpenAI (par exemple `cooptranslator-gpt4o`)
- Version de l’API Azure OpenAI

**Pour Azure AI Services (Extraction de texte d’image via Vision) :**
- Point de terminaison Azure AI Service
- Clé API Azure AI Service

### Exemple : Configuration des variables d’environnement (aperçu)

Plus tard, lors du développement de votre application, vous configurerez probablement ces informations en tant que variables d’environnement comme suit :

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

### Lectures complémentaires

- [Comment créer un projet dans Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Comment créer des ressources Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Comment déployer des modèles OpenAI dans Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations résultant de l'utilisation de cette traduction.