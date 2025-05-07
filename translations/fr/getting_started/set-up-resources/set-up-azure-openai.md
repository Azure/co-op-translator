<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10d8cb07ad0d2ee6705439d4e382ecc9",
  "translation_date": "2025-05-06T18:15:17+00:00",
  "source_file": "getting_started/set-up-resources/set-up-azure-openai.md",
  "language_code": "fr"
}
-->
# Configurer Azure OpenAI pour la traduction de langues

## Créer une ressource Azure OpenAI dans Azure AI Foundry

Pour configurer Azure OpenAI dans Azure AI Foundry, suivez ces étapes :

### Création d’un Hub

1. Connectez-vous au [portail Azure AI Foundry](https://ai.azure.com) : Assurez-vous d’être connecté avec votre compte Azure.

2. Accédez au Centre de gestion : Depuis la page d’accueil, sélectionnez « Management Center » dans le menu de gauche.

3. Créez un nouveau Hub : Cliquez sur « + New hub » et saisissez les informations nécessaires telles que l’Abonnement, le Groupe de ressources et le nom du Hub. Nous recommandons de déployer le hub dans la région East US car cette région prend en charge la vision cognitive et les modèles GPT.

4. Vérifiez et créez : Contrôlez les informations puis cliquez sur « Create » pour configurer votre hub.

### Création d’un projet

1. Rendez-vous à la page d’accueil : Si vous n’y êtes pas déjà, cliquez sur « Azure AI Foundry » en haut à gauche de la page pour revenir à l’accueil.

2. Créez un projet : Cliquez sur « + Create project » et entrez un nom pour votre projet.

3. Sélectionnez un Hub : Si vous avez plusieurs hubs, choisissez celui que vous souhaitez utiliser. Si vous voulez créer un nouveau hub, vous pouvez le faire à cette étape.

4. Configurez le projet : Suivez les instructions pour configurer votre projet selon vos besoins.

5. Créez le projet : Cliquez sur « Create » pour finaliser la configuration.

### Déploiement d’un modèle et d’un point de terminaison pour un modèle OpenAI

1. Connectez-vous au [portail Azure AI Foundry](https://ai.azure.com) : Assurez-vous d’être connecté avec l’abonnement Azure qui contient votre ressource Azure OpenAI Service.

2. Accédez à Modèles et Points de terminaison : Depuis la page d’accueil Azure AI Foundry, trouvez la tuile correspondante et sélectionnez « Let’s go. » ou bien cliquez sur « Model and Endpoints » dans le menu de gauche.

3. Si vous n’avez pas encore déployé de modèle GPT, sélectionnez « deploy model » : choisissez un modèle GPT, nous recommandons GPT-4o, GPT-4o-mini ou o3-mini.

4. Accédez à vos ressources : Vous devriez voir vos ressources Azure OpenAI Service existantes. Si vous en avez plusieurs, utilisez le sélecteur pour choisir celle avec laquelle vous souhaitez travailler.

Pour des instructions plus détaillées, vous pouvez consulter la documentation officielle d’Azure AI Foundry.

[How to Create a project](https://learn.microsoft.com/azure/ai-studio/how-to/create-project)

[How to Create resources](https://learn.microsoft.com/azure/ai-studio/how-to/create-azure-ai-resource)

[How to use OpenAI Model in AI Foundry](https://learn.microsoft.com/azure/ai-studio/ai-services/how-to/connect-azure-openai)

[OpenAI Services in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/azure-openai-in-ai-studio)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.