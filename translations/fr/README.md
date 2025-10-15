<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b94f74bd151736dfef6318f822828bf9",
  "translation_date": "2025-10-15T07:13:50+00:00",
  "source_file": "README.md",
  "language_code": "fr"
}
-->
# Co-op Translator

_Automatisez facilement la traduction de votre contenu éducatif GitHub dans plusieurs langues pour toucher un public mondial._

[![Paquet Python](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Licence : MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Téléchargements](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Téléchargements](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Conteneur : GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Style de code : black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Contributeurs GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![Issues GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![Pull-requests GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Bienvenus](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Prise en charge multilingue

#### Pris en charge par [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabe](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgare](../bg/README.md) | [Birman (Myanmar)](../my/README.md) | [Chinois (simplifié)](../zh/README.md) | [Chinois (traditionnel, Hong Kong)](../hk/README.md) | [Chinois (traditionnel, Macao)](../mo/README.md) | [Chinois (traditionnel, Taïwan)](../tw/README.md) | [Croate](../hr/README.md) | [Tchèque](../cs/README.md) | [Danois](../da/README.md) | [Néerlandais](../nl/README.md) | [Estonien](../et/README.md) | [Finnois](../fi/README.md) | [Français](./README.md) | [Allemand](../de/README.md) | [Grec](../el/README.md) | [Hébreu](../he/README.md) | [Hindi](../hi/README.md) | [Hongrois](../hu/README.md) | [Indonésien](../id/README.md) | [Italien](../it/README.md) | [Japonais](../ja/README.md) | [Coréen](../ko/README.md) | [Lituanien](../lt/README.md) | [Malais](../ms/README.md) | [Marathi](../mr/README.md) | [Népalais](../ne/README.md) | [Norvégien](../no/README.md) | [Persan (Farsi)](../fa/README.md) | [Polonais](../pl/README.md) | [Portugais (Brésil)](../br/README.md) | [Portugais (Portugal)](../pt/README.md) | [Pendjabi (Gurmukhi)](../pa/README.md) | [Roumain](../ro/README.md) | [Russe](../ru/README.md) | [Serbe (cyrillique)](../sr/README.md) | [Slovaque](../sk/README.md) | [Slovène](../sl/README.md) | [Espagnol](../es/README.md) | [Swahili](../sw/README.md) | [Suédois](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamoul](../ta/README.md) | [Thaï](../th/README.md) | [Turc](../tr/README.md) | [Ukrainien](../uk/README.md) | [Ourdou](../ur/README.md) | [Vietnamien](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![Observateurs GitHub](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![Forks GitHub](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![Étoiles GitHub](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Ouvrir dans GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Présentation

**Co-op Translator** vous permet de traduire rapidement votre contenu éducatif GitHub dans plusieurs langues, pour toucher facilement un public international. Lorsque vous mettez à jour vos fichiers Markdown, images ou notebooks Jupyter, les traductions sont automatiquement synchronisées pour garantir que votre contenu éducatif GitHub reste à jour et pertinent pour les utilisateurs du monde entier.

Découvrez comment Co-op Translator organise le contenu éducatif GitHub traduit :

![Exemple](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.fr.png)

## Démarrage rapide

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

Docker :

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Configuration minimale

- Créez un fichier `.env` en utilisant le modèle : [.env.template](../../.env.template)
- Configurez un fournisseur LLM (Azure OpenAI ou OpenAI)
- Pour la traduction d’images (`-img`), configurez aussi Azure AI Vision
- Recommandé : Si vous avez des traductions générées par d’autres outils, nettoyez-les d’abord pour éviter les conflits (par exemple : `translations/`).
- Recommandé : Ajoutez une section de traductions à votre README en utilisant le [modèle de langues README](./README_languages_template.md)
- Voir : [Configurer Azure AI](./getting_started/set-up-azure-ai.md)

## Utilisation

Traduire tous les types pris en charge :

```bash
translate -l "ko ja"
```

Seulement Markdown :

```bash
translate -l "de" -md
```

Markdown + images :

```bash
translate -l "pt" -md -img
```

Seulement notebooks :

```bash
translate -l "zh" -nb
```

Plus d’options : [Référence des commandes](./getting_started/command-reference.md)

## Fonctionnalités

- Traduction automatisée pour Markdown, notebooks et images
- Synchronise les traductions avec les modifications de la source
- Fonctionne en local (CLI) ou en CI (GitHub Actions)
- Utilise Azure OpenAI ou OpenAI ; Azure AI Vision en option pour les images
- Préserve la mise en forme et la structure Markdown

## Documentation

- [Guide en ligne de commande](./getting_started/command-line-guide/command-line-guide.md)
- [Guide GitHub Actions (Dépôts publics & secrets standards)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Guide GitHub Actions (Dépôts organisation Microsoft & configurations org)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Langues prises en charge](./getting_started/supported-languages.md)
- [Dépannage](./getting_started/troubleshooting.md)

## Soutenez-nous et favorisez l’apprentissage mondial

Rejoignez-nous pour révolutionner le partage du contenu éducatif à l’échelle mondiale ! Donnez une ⭐ à [Co-op Translator](https://github.com/azure/co-op-translator) sur GitHub et soutenez notre mission pour lever les barrières linguistiques dans l’apprentissage et la technologie. Votre intérêt et vos contributions ont un impact réel ! Les contributions au code et les suggestions de fonctionnalités sont toujours les bienvenues.

### Découvrez le contenu éducatif Microsoft dans votre langue

- [AZD pour les débutants](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI pour les débutants](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) pour les débutants](https://github.com/microsoft/mcp-for-beginners)
- [Agents IA pour les débutants](https://github.com/microsoft/ai-agents-for-beginners)
- [IA générative pour les débutants avec .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [IA générative pour les débutants](https://github.com/microsoft/generative-ai-for-beginners)
- [IA générative pour les débutants avec Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML pour les débutants](https://aka.ms/ml-beginners)
- [Data Science pour les débutants](https://aka.ms/datascience-beginners)
- [IA pour les débutants](https://aka.ms/ai-beginners)
- [Cybersécurité pour les débutants](https://github.com/microsoft/Security-101)
- [Développement Web pour les débutants](https://aka.ms/webdev-beginners)
- [IoT pour les débutants](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Présentations vidéo

Découvrez Co-op Translator à travers nos présentations _(Cliquez sur l’image ci-dessous pour regarder sur YouTube.)_ :

- **Open at Microsoft** : Une introduction rapide de 18 minutes et un guide pour utiliser Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.fr.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contribution

Ce projet accueille volontiers les contributions et suggestions. Vous souhaitez contribuer à Azure Co-op Translator ? Consultez notre [CONTRIBUTING.md](./CONTRIBUTING.md) pour savoir comment rendre Co-op Translator plus accessible.

## Contributeurs

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code de conduite

Ce projet a adopté le [Code de conduite Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/).
Pour plus d’informations, consultez la [FAQ du Code de conduite](https://opensource.microsoft.com/codeofconduct/faq/) ou
contactez [opencode@microsoft.com](mailto:opencode@microsoft.com) pour toute question ou commentaire supplémentaire.

## IA responsable

Microsoft s’engage à aider ses clients à utiliser ses produits d’IA de façon responsable, à partager ses apprentissages et à établir des partenariats de confiance grâce à des outils comme les Transparency Notes et les Impact Assessments. Beaucoup de ces ressources sont disponibles sur [https://aka.ms/RAI](https://aka.ms/RAI).
L’approche de Microsoft en matière d’IA responsable repose sur nos principes d’équité, de fiabilité et sécurité, de confidentialité et sécurité, d’inclusivité, de transparence et de responsabilité.

Les modèles de langage, d’image et de parole à grande échelle – comme ceux utilisés dans cet exemple – peuvent parfois se comporter de manière injuste, peu fiable ou offensante, ce qui peut causer des préjudices. Veuillez consulter la [Transparency note du service Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) pour être informé des risques et limitations.

La meilleure façon de réduire ces risques est d’intégrer un système de sécurité dans votre architecture, capable de détecter et de prévenir les comportements nuisibles. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) offre une couche de protection indépendante, capable de détecter les contenus nuisibles générés par les utilisateurs ou l’IA dans les applications et services. Azure AI Content Safety inclut des API texte et image permettant de détecter les contenus dangereux. Nous proposons aussi un Content Safety Studio interactif pour explorer et tester du code d’exemple pour la détection de contenus nuisibles sur différents supports. La [documentation de démarrage rapide](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vous guide pour effectuer des requêtes vers le service.


Un autre aspect à prendre en compte est la performance globale de l’application. Pour les applications multi-modales et multi-modèles, la performance signifie que le système fonctionne comme vous et vos utilisateurs l’attendent, y compris en évitant de générer des contenus nuisibles. Il est important d’évaluer la performance de votre application dans son ensemble à l’aide des [indicateurs de qualité de génération et de risques et sécurité](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Vous pouvez évaluer votre application d’IA dans votre environnement de développement en utilisant le [SDK prompt flow](https://microsoft.github.io/promptflow/index.html). À partir d’un jeu de données de test ou d’une cible, les générations de votre application d’IA générative sont mesurées quantitativement avec des évaluateurs intégrés ou personnalisés selon votre choix. Pour commencer à utiliser le SDK prompt flow pour évaluer votre système, vous pouvez suivre le [guide de démarrage rapide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Une fois que vous avez lancé une évaluation, vous pouvez [visualiser les résultats dans Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marques déposées

Ce projet peut contenir des marques déposées ou des logos de projets, produits ou services. L’utilisation autorisée des marques ou logos Microsoft est soumise aux
[Directives sur les marques et l’image de marque de Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
L’utilisation des marques ou logos Microsoft dans des versions modifiées de ce projet ne doit pas prêter à confusion ni suggérer un parrainage de Microsoft.
Toute utilisation de marques ou logos de tiers est soumise aux politiques de ces tiers.

## Obtenir de l’aide

Si vous rencontrez des difficultés ou avez des questions sur la création d’applications d’IA, rejoignez :

<a href="https://aka.ms/foundry/discord"><img src="https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff" alt="Discord Azure AI Foundry Communauté"></a>

Si vous souhaitez donner votre avis sur le produit ou signaler des erreurs lors du développement, rendez-vous sur :

<a href="https://aka.ms/foundry/forum"><img src="https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff" alt="Forum des développeurs Azure AI Foundry sur GitHub"></a>

---

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent comporter des erreurs ou des imprécisions. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.