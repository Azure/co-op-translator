<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d8eec418d6325416b9fab19a2dfcbf41",
  "translation_date": "2025-05-06T17:52:20+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "fr"
}
-->
# Comment utiliser l'interface en ligne de commande (CLI) de Co-op Translator

## Prérequis

- **Python 3.10 ou supérieur** : Nécessaire pour exécuter Co-op Translator.
- **Ressource de modèle de langue** :  
  - **Azure OpenAI** ou autres LLM. Les détails sont disponibles dans la section [modèles et services pris en charge](../../../../README.md).
- **Ressource de vision par ordinateur** (optionnelle) :  
  - Pour la traduction d’images. Si elle n’est pas disponible, le traducteur passe en [mode Markdown uniquement](../markdown-only-mode.md).  
  - **Azure Computer Vision**

### Configuration initiale

Avant de commencer, assurez-vous de configurer les ressources suivantes :

- [Configurer Azure OpenAI](../set-up-resources/set-up-azure-openai.md)  
- [Configurer Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md) (optionnel)

## Table des matières

1. [Créer un fichier '.env' à la racine](./create-env-file.md)  
   - Inclure les clés nécessaires pour le service de modèle de langue choisi.  
   - Si les clés Azure Computer Vision sont omises ou si `-md` est spécifié, le traducteur fonctionnera en mode Markdown uniquement.  
3. [Installer le package Co-op Translator](./install-package.md)  
4. [Traduire votre projet avec Co-op Translator](./translator-your-project.md)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle humaine est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.