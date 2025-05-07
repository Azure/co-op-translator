<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-05-07T14:05:53+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "fr"
}
-->
# Traduisez votre projet avec Co-op Translator

Le **Co-op Translator** est un outil en ligne de commande (CLI) qui vous aide à traduire les fichiers markdown et images de votre projet dans plusieurs langues. Cette section explique comment utiliser l’outil, présente les différentes options de la CLI et fournit des exemples pour divers cas d’usage.

> [!NOTE]
> Pour une liste complète des commandes et leurs descriptions détaillées, veuillez consulter la [Référence des commandes](./command-reference.md).

---

## Scénarios et commandes exemples

Voici quelques cas d’usage courants pour le **Co-op Translator**, ainsi que les commandes appropriées à exécuter.

### 1. Traduction basique (une seule langue)

Pour traduire l’ensemble de votre projet (fichiers markdown et images) dans une seule langue, comme le coréen, utilisez la commande suivante :

```bash
translate -l "ko"
```

Cette commande traduira tous les fichiers markdown et images en coréen, en ajoutant les nouvelles traductions sans supprimer celles déjà existantes.

> [!TIP]
>
> Vous voulez savoir quels codes de langue sont disponibles dans **Co-op Translator** ? Rendez-vous dans la section [Langues supportées](https://github.com/Azure/co-op-translator#supported-languages) du dépôt pour plus d’informations.

#### Exemple sur Phi-3 CookBook

Dans le **Phi-3 CookBook**, j’ai utilisé la méthode suivante pour ajouter la traduction coréenne aux fichiers markdown et images existants.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Traduction en plusieurs langues

Pour traduire votre projet dans plusieurs langues (par exemple espagnol, français et allemand), utilisez cette commande :

```bash
translate -l "es fr de"
```

Cette commande traduira le projet en espagnol, français et allemand, en ajoutant les nouvelles traductions sans écraser les anciennes.

#### Exemple sur Phi-3 CookBook

Dans le **Phi-3 CookBook**, après avoir récupéré les derniers changements pour refléter les commits les plus récents, j’ai utilisé la méthode suivante pour traduire les fichiers markdown et images nouvellement ajoutés.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Bien qu’il soit généralement recommandé de traduire une langue à la fois, dans des cas comme celui-ci où des modifications spécifiques doivent être ajoutées, traduire plusieurs langues simultanément peut être efficace.

### 3. Mise à jour des traductions (suppression des traductions existantes)

Pour mettre à jour les traductions existantes (c’est-à-dire supprimer les traductions actuelles et les remplacer par de nouvelles), utilisez l’option `-u`. Cela supprimera toutes les traductions existantes pour les langues spécifiées et les retraduira.

```bash
translate -l "ko" -u
```

Attention : cette commande vous demandera une confirmation avant de procéder à la suppression des traductions existantes.

#### Exemple sur Phi-3 CookBook

Dans le **Phi-3 CookBook**, j’ai utilisé la méthode suivante pour mettre à jour tous les fichiers traduits en espagnol. Je recommande cette méthode lorsqu’il y a des changements importants dans le contenu original sur plusieurs documents markdown. S’il n’y a que quelques fichiers markdown traduits à mettre à jour, il est plus efficace de supprimer manuellement ces fichiers spécifiques, puis d’utiliser la méthode `-a` pour ajouter les traductions mises à jour.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Traduire uniquement les images

Pour ne traduire que les fichiers images de votre projet, utilisez l’option `-img` :

```bash
translate -l "ko" -img
```

Cette commande traduira uniquement les images en coréen, sans toucher aux fichiers markdown.

### 6. Traduire uniquement les fichiers markdown

Pour ne traduire que les fichiers markdown de votre projet, utilisez l’option `-md` :

```bash
translate -l "ko" -md
```

### 7. Vérifier les erreurs dans les fichiers traduits

Si vous souhaitez vérifier les fichiers traduits pour détecter des erreurs et relancer la traduction si nécessaire, utilisez l’option `-chk` :

```bash
translate -l "ko" -chk
```

Cette commande analysera les fichiers markdown traduits et relancera la traduction pour ceux présentant des erreurs.

#### Exemple sur Phi-3 CookBook

Dans le **Phi-3 CookBook**, j’ai utilisé la méthode suivante pour vérifier les erreurs de traduction dans les fichiers coréens et relancer automatiquement la traduction pour ceux qui présentaient des problèmes.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Cette option détecte les erreurs de traduction. Actuellement, si la différence dans les sauts de ligne entre les fichiers originaux et traduits dépasse six, le fichier est signalé comme ayant une erreur de traduction. Je prévois d’améliorer ce critère pour plus de souplesse à l’avenir.

Par exemple, cette méthode est utile pour détecter des segments manquants ou des traductions corrompues, et elle relance automatiquement la traduction pour ces fichiers.

Cependant, si vous savez déjà quels fichiers posent problème, il est plus efficace de supprimer manuellement ces fichiers puis d’utiliser l’option `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` :

```bash
translate -l "ko" -d
```

Cette commande lance la traduction en mode debug, fournissant des informations de journalisation supplémentaires qui peuvent vous aider à identifier les problèmes lors du processus de traduction.

#### Exemple sur Phi-3 CookBook

Dans le **Phi-3 CookBook**, j’ai rencontré un problème où les traductions contenant de nombreux liens dans les fichiers markdown provoquaient des erreurs de formatage, telles que des traductions cassées et des sauts de ligne ignorés. Pour diagnostiquer ce problème, j’ai utilisé l’option `-d` afin de voir comment le processus de traduction fonctionnait.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Traduire toutes les langues

Si vous souhaitez traduire le projet dans toutes les langues supportées, utilisez le mot-clé all.

> [!WARNING]
> Traduire toutes les langues en une seule fois peut prendre beaucoup de temps selon la taille du projet. Par exemple, traduire le **Phi-3 CookBook** en espagnol a pris environ 2 heures. Au vu de l’ampleur, il n’est pas réaliste qu’une seule personne gère 20 langues. Il est recommandé de répartir le travail entre plusieurs contributeurs, chacun prenant en charge une ou deux langues, et de mettre à jour les traductions progressivement.

```bash
translate -l "all"
```

Cette commande traduira le projet dans toutes les langues disponibles. Si vous continuez, la traduction peut prendre un temps considérable selon la taille du projet.

> [!TIP]
>
> ### Suppression manuelle des fichiers traduits (optionnel)
> Les fichiers traduits sont désormais automatiquement détectés et nettoyés lorsqu’un fichier source est mis à jour.
>
> Cependant, si vous souhaitez mettre à jour manuellement une traduction – par exemple pour refaire un fichier spécifique ou contourner le comportement du système – vous pouvez utiliser la commande suivante pour supprimer toutes les versions du fichier dans les dossiers de langues.
>
> ### Sous Windows :
> 1. **Avec l’invite de commandes** :
>    - Ouvrez l’invite de commandes.
>    - Naviguez vers le dossier où se trouvent les fichiers avec la commande `cd`.
>    - Utilisez la commande suivante pour supprimer les fichiers :
>      ```
>      del /s *filename*
>      ```
>      L’option `/s` recherche aussi dans les sous-répertoires.
>
> 2. **Avec PowerShell** :
>    - Ouvrez PowerShell.
>    - Exécutez cette commande :
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Remplacez `"C:\YourPath"` par le chemin approprié.
>
> ### Pour naviguer et rechercher un fichier spécifique :
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>
> ### Pour mettre à jour les fichiers modifiés les plus récents :
>     Utilisez la commande `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l`.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.