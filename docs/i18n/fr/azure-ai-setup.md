# Configuration d'Azure AI

Utilisez ce guide lorsque vous souhaitez configurer Azure OpenAI pour la traduction de texte et Azure AI Vision pour l'extraction de texte à partir d'images.

## Prérequis

- Un abonnement Azure.
- L'autorisation de créer ou d'utiliser des ressources Azure AI et des déploiements de modèles.
- Un projet dans Azure AI Foundry ou un accès équivalent aux ressources Azure OpenAI et Azure AI Vision.

## Créer un projet Azure AI

1. Ouvrez [Azure AI Foundry](https://ai.azure.com).
2. Créez ou sélectionnez un projet.
3. Créez ou sélectionnez un hub d'IA pour le projet.
4. Ouvrez l'aperçu du projet après sa création.

## Déployer un modèle Azure OpenAI

1. Dans le projet, ouvrez **Modèles + points de terminaison**.
2. Sélectionnez **Déployer le modèle**.
3. Choisissez un modèle GPT tel que `gpt-4o`.
4. Déployez le modèle.
5. Notez le point de terminaison, le nom du déploiement, le nom du modèle, la clé API et la version de l'API.

!!! note
    La version de l'API Azure OpenAI est distincte de la version du modèle affichée dans Azure AI Foundry. Choisissez une version d'API prise en charge pour votre déploiement.

## Configurer Azure AI Vision

La traduction d'images utilise Azure AI Vision pour extraire le texte des images sources avant que le texte ne soit traduit.

Dans votre projet Azure AI, trouvez la clé et le point de terminaison du service Azure AI.

![Trouver les informations sur le service Azure AI](../../assets/find-azure-ai-info.png)

Notez :

- Point de terminaison du service Azure AI
- Clé API du service Azure AI

## Variables d'environnement

Ajoutez les identifiants à votre fichier `.env` ou aux secrets CI.

```bash
# Azure AI Vision, nécessaire pour la traduction d'images
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, nécessaire pour la traduction de texte
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator prend également en charge des jeux d'identifiants de secours optionnels. Dupliquez un ensemble complet de paramètres de fournisseur avec des suffixes tels que `_1` ou `_2` ; toutes les variables d'un ensemble de secours doivent avoir le même suffixe.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Étapes suivantes

- Retournez à [Configuration](configuration.md) pour configurer les variables d'environnement locales ou CI.
- Utilisez la [référence CLI](cli.md) pour les commandes de traduction.
- Utilisez [GitHub Actions](github-actions.md) pour automatiser les pull requests de traduction.