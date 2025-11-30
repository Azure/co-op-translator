<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T09:41:46+00:00",
  "source_file": "README.md",
  "language_code": "fr"
}
-->
# Traducteur Co-op

_Automatisez facilement la traduction de votre contenu éducatif GitHub en plusieurs langues pour toucher un public mondial._

[![Package Python](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Licence : MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Téléchargements](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Téléchargements](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Conteneur : GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Style de code : black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Contributeurs GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![Problèmes GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![Pull requests GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Bienvenues](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Support multilingue

#### Pris en charge par [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabe](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgare](../bg/README.md) | [Birman (Myanmar)](../my/README.md) | [Chinois (simplifié)](../zh/README.md) | [Chinois (traditionnel, Hong Kong)](../hk/README.md) | [Chinois (traditionnel, Macao)](../mo/README.md) | [Chinois (traditionnel, Taïwan)](../tw/README.md) | [Croate](../hr/README.md) | [Tchèque](../cs/README.md) | [Danois](../da/README.md) | [Néerlandais](../nl/README.md) | [Estonien](../et/README.md) | [Finnois](../fi/README.md) | [Français](./README.md) | [Allemand](../de/README.md) | [Grec](../el/README.md) | [Hébreu](../he/README.md) | [Hindi](../hi/README.md) | [Hongrois](../hu/README.md) | [Indonésien](../id/README.md) | [Italien](../it/README.md) | [Japonais](../ja/README.md) | [Kannada](../kn/README.md) | [Coréen](../ko/README.md) | [Lituanien](../lt/README.md) | [Malais](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Népalais](../ne/README.md) | [Pidgin nigérian](../pcm/README.md) | [Norvégien](../no/README.md) | [Persan (Farsi)](../fa/README.md) | [Polonais](../pl/README.md) | [Portugais (Brésil)](../br/README.md) | [Portugais (Portugal)](../pt/README.md) | [Pendjabi (Gurmukhi)](../pa/README.md) | [Roumain](../ro/README.md) | [Russe](../ru/README.md) | [Serbe (cyrillique)](../sr/README.md) | [Slovaque](../sk/README.md) | [Slovène](../sl/README.md) | [Espagnol](../es/README.md) | [Swahili](../sw/README.md) | [Suédois](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamoul](../ta/README.md) | [Télougou](../te/README.md) | [Thaï](../th/README.md) | [Turc](../tr/README.md) | [Ukrainien](../uk/README.md) | [Ourdou](../ur/README.md) | [Vietnamien](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![Observateurs GitHub](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![Forks GitHub](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![Étoiles GitHub](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Ouvrir dans GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Présentation

**Co-op Translator** vous aide à localiser facilement votre contenu éducatif GitHub en plusieurs langues.  
Lorsque vous mettez à jour vos fichiers Markdown, images ou notebooks, les traductions restent automatiquement synchronisées, garantissant que votre contenu reste précis et à jour pour les apprenants du monde entier.

Exemple d’organisation du contenu traduit :

![Exemple](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.fr.png)

## Démarrage rapide

```bash
# Créez et activez un environnement virtuel (recommandé)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Installez le paquet
pip install co-op-translator
# Traduire
translate -l "ko ja fr" -md
```

Docker :

```bash
# Récupérer l'image publique depuis GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Exécuter avec le dossier actuel monté et le fichier .env fourni (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Configuration minimale

1. Créez un fichier `.env` à partir du modèle : [.env.template](../../.env.template)  
2. Configurez un fournisseur LLM (Azure OpenAI ou OpenAI)  
3. (Optionnel) Pour la traduction d’images (`-img`), configurez Azure AI Vision  
4. (Recommandé) Nettoyez les traductions précédentes pour éviter les conflits (ex. : `translations/`)  
5. (Recommandé) Ajoutez une section de traduction à votre README en utilisant le [modèle README languages](./getting_started/README_languages_template.md)  
6. Consultez : [Configurer Azure AI](./getting_started/set-up-azure-ai.md)

## Utilisation

Traduisez tous les types pris en charge :

```bash
translate -l "ko ja"
```

Markdown uniquement :

```bash
translate -l "de" -md
```

Markdown + images :

```bash
translate -l "pt" -md -img
```

Notebooks uniquement :

```bash
translate -l "zh" -nb
```

Plus d’options : [Référence des commandes](./getting_started/command-reference.md)

## Fonctionnalités

- Traduction automatisée pour Markdown, notebooks et images  
- Synchronisation des traductions avec les modifications sources  
- Fonctionne localement (CLI) ou en CI (GitHub Actions)  
- Utilise Azure OpenAI ou OpenAI ; Azure AI Vision optionnel pour les images  
- Préserve la mise en forme et la structure Markdown

## Documentation

- [Guide en ligne de commande](./getting_started/command-line-guide/command-line-guide.md)  
- [Guide GitHub Actions (dépôts publics & secrets standards)](./getting_started/github-actions-guide/github-actions-guide-public.md)  
- [Guide GitHub Actions (dépôts organisation Microsoft & configurations au niveau org)](./getting_started/github-actions-guide/github-actions-guide-org.md)  
- [Modèle README languages](./getting_started/README_languages_template.md)  
- [Langues prises en charge](./getting_started/supported-languages.md)  
- [Contribuer](./CONTRIBUTING.md)  
- [Dépannage](./getting_started/troubleshooting.md)

### Guide spécifique Microsoft
> [!NOTE]
> Pour les mainteneurs des dépôts Microsoft « For Beginners » uniquement.

- [Mise à jour de la liste « autres cours » (uniquement pour les dépôts MS Beginners)](./getting_started/update-other-courses.md)

## Soutenez-nous et favorisez l’apprentissage mondial

Rejoignez-nous pour révolutionner la manière dont le contenu éducatif est partagé à l’échelle mondiale ! Donnez une ⭐ à [Co-op Translator](https://github.com/azure/co-op-translator) sur GitHub et soutenez notre mission de briser les barrières linguistiques dans l’apprentissage et la technologie. Votre intérêt et vos contributions ont un impact important ! Les contributions de code et suggestions de fonctionnalités sont toujours les bienvenues.

### Découvrez le contenu éducatif Microsoft dans votre langue

- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)  
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)  
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)  
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)  
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)  
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)  
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)  
- [ML for Beginners](https://aka.ms/ml-beginners)  
- [Data Science for Beginners](https://aka.ms/datascience-beginners)  
- [AI for Beginners](https://aka.ms/ai-beginners)  
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)  
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)  
- [IoT for Beginners](https://aka.ms/iot-beginners)  
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Présentations vidéo

👉 Cliquez sur l’image ci-dessous pour regarder sur YouTube.

- **Open at Microsoft** : Une introduction rapide de 18 minutes et un guide express pour utiliser Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.fr.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contribution

Ce projet accueille contributions et suggestions. Vous souhaitez contribuer à Azure Co-op Translator ? Veuillez consulter notre [CONTRIBUTING.md](./CONTRIBUTING.md) pour connaître les directives et découvrir comment rendre Co-op Translator plus accessible.

## Contributeurs

[![contributeurs co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code de conduite

Ce projet a adopté le [Code de conduite Open Source Microsoft](https://opensource.microsoft.com/codeofconduct/).  
Pour plus d’informations, consultez la [FAQ du Code de conduite](https://opensource.microsoft.com/codeofconduct/faq/) ou contactez [opencode@microsoft.com](mailto:opencode@microsoft.com) pour toute question ou remarque supplémentaire.

## IA responsable

Microsoft s’engage à aider ses clients à utiliser ses produits d’IA de manière responsable, à partager ses apprentissages et à construire des partenariats basés sur la confiance grâce à des outils comme les Notes de transparence et les Évaluations d’impact. Vous trouverez de nombreuses ressources sur [https://aka.ms/RAI](https://aka.ms/RAI).  
L’approche de Microsoft en matière d’IA responsable repose sur nos principes d’IA : équité, fiabilité et sécurité, confidentialité et sécurité, inclusion, transparence et responsabilité.

Les modèles à grande échelle de langage naturel, d’image et de parole – comme ceux utilisés dans cet exemple – peuvent potentiellement se comporter de manière injuste, peu fiable ou offensante, causant ainsi des préjudices. Veuillez consulter la [note de transparence du service Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) pour être informé des risques et limites.
L'approche recommandée pour atténuer ces risques est d'inclure un système de sécurité dans votre architecture capable de détecter et de prévenir les comportements nuisibles. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) offre une couche de protection indépendante, capable de détecter les contenus nuisibles générés par les utilisateurs et par l'IA dans les applications et services. Azure AI Content Safety comprend des API de texte et d'image qui vous permettent de détecter les contenus nuisibles. Nous proposons également un Content Safety Studio interactif qui vous permet de visualiser, d'explorer et d'essayer des exemples de code pour détecter les contenus nuisibles dans différentes modalités. La [documentation de démarrage rapide](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) suivante vous guide pour effectuer des requêtes vers le service.

Un autre aspect à prendre en compte est la performance globale de l'application. Pour les applications multi-modales et multi-modèles, la performance signifie que le système fonctionne comme vous et vos utilisateurs l'attendez, y compris en ne générant pas de résultats nuisibles. Il est important d'évaluer la performance de votre application globale en utilisant les [métriques de qualité de génération, de risque et de sécurité](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Vous pouvez évaluer votre application IA dans votre environnement de développement en utilisant le [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Que vous disposiez d'un jeu de données de test ou d'un objectif, les générations de votre application d'IA générative sont mesurées quantitativement avec des évaluateurs intégrés ou des évaluateurs personnalisés de votre choix. Pour commencer avec le prompt flow SDK afin d’évaluer votre système, vous pouvez suivre le [guide de démarrage rapide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Une fois que vous avez exécuté une évaluation, vous pouvez [visualiser les résultats dans Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marques déposées

Ce projet peut contenir des marques ou logos de projets, produits ou services. L'utilisation autorisée des marques ou logos Microsoft est soumise aux [Directives sur les marques et la marque de Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).  
L'utilisation des marques ou logos Microsoft dans des versions modifiées de ce projet ne doit pas créer de confusion ni laisser entendre un parrainage par Microsoft.  
Toute utilisation de marques ou logos tiers est soumise aux politiques de ces tiers.

## Obtenir de l'aide

Si vous êtes bloqué ou avez des questions sur la création d'applications IA, rejoignez :

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Si vous avez des retours sur le produit ou rencontrez des erreurs lors du développement, visitez :

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->