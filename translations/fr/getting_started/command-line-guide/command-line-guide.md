<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5eb9b53c81804f04bc9456160e79940",
  "translation_date": "2025-05-07T14:05:40+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "fr"
}
-->
# Comment utiliser l'interface en ligne de commande (CLI) de Co-op Translator

## Prérequis

- **Python 3.10 ou supérieur** : Nécessaire pour exécuter Co-op Translator.
- **Ressource de modèle de langage** :  
  - **Azure OpenAI** ou autres LLMs. Les détails sont disponibles dans la section [modèles et services supportés](../../../../README.md).
- **Ressource de vision par ordinateur** (optionnel) :  
  - Pour la traduction d’images. Si non disponible, le traducteur passe en [mode Markdown uniquement](../markdown-only-mode.md).  
  - **Azure Computer Vision**

## Table des matières

1. [Créer un fichier '.env' à la racine](./create-env-file.md)  
   - Inclure les clés nécessaires pour le service de modèle de langage choisi.  
   - Si les clés Azure Computer Vision sont omises ou que `-md` est spécifié, le traducteur fonctionnera en mode Markdown uniquement.  
1. [Installer le package Co-op translator](./install-package.md)  
1. [Traduire votre projet avec Co-op Translator](./translator-your-project.md)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle humaine est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.