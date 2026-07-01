# Co-op Translator

_Facilitez l'automatisation et la maintenance des traductions de votre contenu éducatif GitHub dans plusieurs langues au fur et à mesure de l'évolution de votre projet._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Package Python](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Licence : MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Téléchargements](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Téléchargements](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Conteneur : GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Style de code : black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Contributeurs GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![Problèmes GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![Pull-requests GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs bienvenus](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**Commencez ici :** [Choisissez votre flux de travail](https://azure.github.io/co-op-translator/workflows/) | [Configuration](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [API Python](https://azure.github.io/co-op-translator/api/) | [Serveur MCP](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Support multilingue

#### Pris en charge par [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabe](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgare](../bg/README.md) | [Birman (Myanmar)](../my/README.md) | [Chinois (simplifié)](../zh-CN/README.md) | [Chinois (traditionnel, Hong Kong)](../zh-HK/README.md) | [Chinois (traditionnel, Macau)](../zh-MO/README.md) | [Chinois (traditionnel, Taïwan)](../zh-TW/README.md) | [Croate](../hr/README.md) | [Tchèque](../cs/README.md) | [Danois](../da/README.md) | [Néerlandais](../nl/README.md) | [Estonien](../et/README.md) | [Finnois](../fi/README.md) | [Français](./README.md) | [Allemand](../de/README.md) | [Grec](../el/README.md) | [Hébreu](../he/README.md) | [Hindi](../hi/README.md) | [Hongrois](../hu/README.md) | [Indonésien](../id/README.md) | [Italien](../it/README.md) | [Japonais](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Coréen](../ko/README.md) | [Lituanien](../lt/README.md) | [Malais](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Népalais](../ne/README.md) | [Pidgin nigérian](../pcm/README.md) | [Norvégien](../no/README.md) | [Persan (farsi)](../fa/README.md) | [Polonais](../pl/README.md) | [Portugais (Brésil)](../pt-BR/README.md) | [Portugais (Portugal)](../pt-PT/README.md) | [Pendjabi (Gurmukhi)](../pa/README.md) | [Roumain](../ro/README.md) | [Russe](../ru/README.md) | [Serbe (cyrillique)](../sr/README.md) | [Slovaque](../sk/README.md) | [Slovène](../sl/README.md) | [Espagnol](../es/README.md) | [Swahili](../sw/README.md) | [Suédois](../sv/README.md) | [Tagalog (philippin)](../tl/README.md) | [Tamoul](../ta/README.md) | [Télougou](../te/README.md) | [Thaï](../th/README.md) | [Turc](../tr/README.md) | [Ukrainien](../uk/README.md) | [Ourdou](../ur/README.md) | [Vietnamien](../vi/README.md)

> **Préférez cloner localement ?**
>
> Ce dépôt inclut plus de 50 traductions de langues, ce qui augmente considérablement la taille du téléchargement. Pour cloner sans les traductions, utilisez le sparse checkout :
>
> **Bash / macOS / Linux :**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows) :**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Cela vous fournit tout ce dont vous avez besoin pour suivre le cours avec un téléchargement beaucoup plus rapide.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![Observateurs GitHub](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![Forks GitHub](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![Étoiles GitHub](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Ouvrir dans GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Aperçu

**Co-op Translator** vous aide à localiser facilement votre contenu éducatif GitHub dans plusieurs langues.
Lorsque vous mettez à jour vos fichiers Markdown, images ou notebooks, les traductions restent automatiquement synchronisées, garantissant que votre contenu reste précis et à jour pour les apprenants du monde entier.

Utilisez-le depuis la CLI pour la traduction du dépôt, depuis l'API Python pour l'automatisation, ou via le serveur MCP pour des flux de travail agent et éditeur.

Exemple d'organisation du contenu traduit :

![Exemple](../../imgs/translation-ex.png)

## Pourquoi Co-op Translator ?

Traduire un fichier est facile. Maintenir l'ensemble d'un dépôt de documentation
traduit, lié et à jour est la partie difficile.

| Problème | Comment Co-op Translator aide |
| --- | --- |
| Les longs documents ne tiennent pas dans une seule invite | Les gros fichiers Markdown sont divisés en morceaux, de sorte qu'un README volumineux ne dépend pas d'une réponse fragile du modèle. Si un morceau échoue, Co-op Translator peut réessayer et redécouper uniquement la partie échouée. |
| Les traductions incomplètes ne doivent pas être marquées comme actuelles | Une traduction tronquée ne doit jamais être considérée comme à jour. Co-op Translator vérifie l'intégrité des traductions avant de les enregistrer et peut détecter des traductions existantes structurellement incomplètes. |
| Les liens doivent correspondre à la structure du dépôt traduit | Les traductions manuelles laissent souvent des liens relatifs pointant vers l'arbre source. Co-op Translator réécrit les liens Markdown, notebook, image et README pour correspondre à la structure `translations/<lang>/...`. |
| La traduction doit fonctionner sur l'ensemble d'un dépôt | Co-op Translator gère les fichiers README, la documentation, les notebooks et le texte des images dans le cadre d'un même flux de travail de dépôt, au lieu de traduire les fichiers un par un. |
| La maintenance des traductions est plus importante que leur création ponctuelle | Les hachages source et les métadonnées de traduction permettent à Co-op Translator de trouver les fichiers obsolètes, d'ignorer les fichiers inchangés et de garder le contenu traduit synchronisé au fur et à mesure que le dépôt source évolue. |

## Comment l'état de la traduction est géré

Co-op Translator gère le contenu traduit comme des **artefacts logiciels versionnés**,  
et non comme des fichiers statiques.

L'outil suit l'état des fichiers Markdown, des images et des notebooks traduits
en utilisant des **métadonnées liées à la langue**.

Cette conception permet à Co-op Translator de :

- Détecter de manière fiable les traductions obsolètes
- Traiter de manière cohérente les fichiers Markdown, les images et les notebooks
- Monter en charge en toute sécurité sur des dépôts multilingues volumineux et en évolution rapide

En modélisant les traductions comme des artefacts gérés,
les flux de travail de traduction s'alignent naturellement sur les pratiques modernes
de gestion des dépendances et des artefacts logiciels.

→ [Comment l'état de la traduction est géré](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Articles approfondis connexes

- [Corriger le Markdown cassé dans la traduction par IA : durcir une chaîne de production](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Commencer

Co-op Translator peut être utilisé depuis la CLI, l'API Python ou le serveur MCP. Commencez par le guide des flux de travail si vous devez choisir entre traduction locale, automatisation, CI et intégration agent/éditeur.

- [Choisissez votre flux de travail](../../docs/workflows.md)
- [Configurer les identifiants](../../docs/configuration.md)
- [Traduire depuis la CLI](../../docs/cli.md)
- [Automatiser avec l'API Python](../../docs/api.md)
- [Se connecter au serveur MCP](../../docs/mcp.md)
- [Exécuter dans GitHub Actions](../../docs/github-actions.md)

Exemple minimal de CLI après configuration :

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

Pour les premières exécutions sur de grands dépôts, utilisez `--dry-run` avant d'écrire les fichiers traduits. Consultez la [référence CLI](../../docs/cli.md) pour les indicateurs de type de contenu, les journaux, la revue et la migration des liens.

Exécution rapide en conteneur avec Bash/Zsh :

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Exécution rapide en conteneur avec PowerShell :

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Fonctionnalités

- Traduction automatisée pour Markdown, notebooks et images
- Maintient les traductions synchronisées avec les modifications de la source
- Fonctionne localement (CLI) ou en CI (GitHub Actions)
- Expose des outils de traduction pour Markdown, notebooks, images, revue et projets via MCP
- Utilise Azure OpenAI ou OpenAI pour la traduction fournie par un prestataire
- Permet à MCP d'héberger des agents traduisant des segments de Markdown et de notebooks sans les identifiants LLM de Co-op Translator
- Utilise Azure AI Vision pour l'extraction et la traduction du texte des images
- Vérifie la structure et la fraîcheur des traductions avec des contrôles déterministes
- Préserve le formatage et la structure Markdown

## Documentation

- [Site de documentation](https://azure.github.io/co-op-translator/)
- [Choisissez votre flux de travail](../../docs/workflows.md)
- [Configuration](../../docs/configuration.md)
- [Configuration Azure AI](../../docs/azure-ai-setup.md)
- [Référence CLI](../../docs/cli.md)
- [API Python](../../docs/api.md)
- [Serveur MCP](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [Modèle README pour les langues](../../docs/readme-languages-template.md)
- [Langues prises en charge](../../docs/supported-languages.md)
- [Contribuer](../../CONTRIBUTING.md)
- [Dépannage](../../docs/troubleshooting.md)

### Guide spécifique à Microsoft
> [!NOTE]
> Pour les mainteneurs des dépôts Microsoft « For Beginners » uniquement.

- [Mise à jour de la liste « autres cours » (uniquement pour les dépôts MS Beginners)](../../docs/microsoft-beginners.md)

## Soutenez-nous et favorisez l'apprentissage mondial

Rejoignez-nous pour révolutionner la manière dont le contenu éducatif est partagé dans le monde ! Donnez une ⭐ à [Co-op Translator](https://github.com/azure/co-op-translator) sur GitHub et soutenez notre mission de lever les barrières linguistiques dans l'apprentissage et la technologie. Votre intérêt et vos contributions ont un impact significatif ! Les contributions de code et les suggestions de fonctionnalités sont toujours les bienvenues.

### Explorez le contenu éducatif Microsoft dans votre langue
- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD pour débutants](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI pour débutants](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) pour débutants](https://github.com/microsoft/mcp-for-beginners)
- [Agents d'IA pour débutants](https://github.com/microsoft/ai-agents-for-beginners)
- [IA générative pour débutants utilisant .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [IA générative pour débutants](https://github.com/microsoft/generative-ai-for-beginners)
- [IA générative pour débutants utilisant Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML pour débutants](https://aka.ms/ml-beginners)
- [Science des données pour débutants](https://aka.ms/datascience-beginners)
- [IA pour débutants](https://aka.ms/ai-beginners)
- [Cybersécurité pour débutants](https://github.com/microsoft/Security-101)
- [Développement Web pour débutants](https://aka.ms/webdev-beginners)
- [IoT pour débutants](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Présentations vidéo

👉 Cliquez sur l'image ci-dessous pour regarder sur YouTube.

- **Open chez Microsoft**: Une brève introduction de 18 minutes et un guide rapide sur la façon d'utiliser Co-op Translator.

  [![Open chez Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contribution

Ce projet accueille les contributions et suggestions. Vous souhaitez contribuer à Azure Co-op Translator ? Veuillez consulter notre [CONTRIBUTING.md](../../CONTRIBUTING.md) pour les directives sur la manière dont vous pouvez aider à rendre Co-op Translator plus accessible.

## Contributeurs

[![contributeurs de co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code de conduite

Ce projet a adopté le [Code de conduite Open Source de Microsoft](https://opensource.microsoft.com/codeofconduct/).
Pour plus d'informations, consultez la [FAQ du Code de conduite](https://opensource.microsoft.com/codeofconduct/faq/) ou contactez [opencode@microsoft.com](mailto:opencode@microsoft.com) pour toute question ou commentaire supplémentaire.

## IA responsable

Microsoft s'engage à aider ses clients à utiliser nos produits d'IA de manière responsable, à partager nos enseignements et à établir des partenariats basés sur la confiance grâce à des outils tels que les Transparency Notes et les Impact Assessments. Nombre de ces ressources sont disponibles à [https://aka.ms/RAI](https://aka.ms/RAI).
L'approche de Microsoft en matière d'IA responsable repose sur nos principes d'IA : équité, fiabilité et sécurité, confidentialité et sécurité, inclusion, transparence et responsabilité.

Les modèles à grande échelle de langage naturel, d'image et de parole - comme ceux utilisés dans cet exemple - peuvent potentiellement se comporter de manière injuste, peu fiable ou offensante, causant ainsi des préjudices. Veuillez consulter la [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) pour être informé des risques et des limites.

L'approche recommandée pour atténuer ces risques est d'inclure un système de sécurité dans votre architecture capable de détecter et de prévenir les comportements nuisibles. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) fournit une couche de protection indépendante, capable de détecter les contenus nuisibles générés par les utilisateurs et par l'IA dans les applications et services. Azure AI Content Safety inclut des API texte et image qui permettent de détecter les contenus potentiellement dangereux. Nous proposons également un Content Safety Studio interactif qui vous permet de visualiser, d'explorer et d'essayer des exemples de code pour détecter les contenus nuisibles à travers différentes modalités. La [documentation de démarrage rapide](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) suivante vous guide pour effectuer des requêtes vers le service.

Un autre aspect à prendre en compte est la performance globale de l'application. Pour les applications multi-modales et multi-modèles, nous entendons par performance que le système fonctionne comme vous et vos utilisateurs l'attendez, y compris en n'engendrant pas de sorties nuisibles. Il est important d'évaluer la performance de votre application globale en utilisant les [métriques de qualité de génération ainsi que de risque et de sécurité](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Vous pouvez évaluer votre application d'IA dans votre environnement de développement à l'aide du [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Avec un jeu de données de test ou un objectif, les générations de votre application d'IA générative sont mesurées quantitativement avec des évaluateurs intégrés ou des évaluateurs personnalisés de votre choix. Pour commencer avec le prompt flow sdk afin d'évaluer votre système, vous pouvez suivre le [guide de démarrage rapide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Une fois que vous avez exécuté une évaluation, vous pouvez [visualiser les résultats dans Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marques

Ce projet peut contenir des marques ou des logos de projets, produits ou services. L'utilisation autorisée des marques ou logos Microsoft est soumise à et doit suivre les [Directives sur les marques et l'image de marque de Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
L'utilisation des marques ou logos Microsoft dans les versions modifiées de ce projet ne doit pas créer de confusion ni laisser entendre un parrainage par Microsoft.
Toute utilisation de marques ou logos de tiers est soumise aux politiques de ces tiers.

## Obtenir de l'aide

Si vous êtes bloqué ou avez des questions sur le développement d'applications d'IA, rejoignez :

[![Discord de Microsoft Foundry](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Si vous avez des retours sur le produit ou des erreurs lors du développement, visitez :

[![Forum des développeurs Microsoft Foundry](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)