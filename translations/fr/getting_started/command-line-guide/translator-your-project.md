<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "33db54f4f3ca9f0321be05374b591f2b",
  "translation_date": "2025-05-06T17:59:33+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "fr"
}
-->
# Traduisez votre projet avec Co-op Translator

Le **Co-op Translator** est un outil en ligne de commande (CLI) qui vous aide à traduire les fichiers markdown et images de votre projet dans plusieurs langues. Cette section explique comment utiliser l’outil, présente les différentes options de la CLI et fournit des exemples pour divers cas d’utilisation.

> [!NOTE]
> Pour une liste complète des commandes et leurs descriptions détaillées, veuillez consulter la [référence des commandes](./command-reference.md).

---

## Scénarios et commandes exemples

Voici quelques cas d’utilisation courants pour le **Co-op Translator**, ainsi que les commandes appropriées à exécuter.

### 1. Traduction basique (une seule langue)

Pour traduire l’ensemble de votre projet (fichiers markdown et images) dans une seule langue, comme le coréen, utilisez la commande suivante :

```bash
translate -l "ko"
```

Cette commande traduira tous les fichiers markdown et images en coréen, en ajoutant les nouvelles traductions sans supprimer celles existantes.

> [!TIP]
>
> Vous souhaitez connaître les codes de langues disponibles dans **Co-op Translator** ? Rendez-vous dans la section [Langues supportées](https://github.com/Azure/co-op-translator#supported-languages) du dépôt pour plus de détails.

#### Exemple sur Phi-3 CookBook

Dans le **Phi-3 CookBook**, j’ai utilisé la méthode suivante pour ajouter la traduction coréenne aux fichiers markdown et images existants.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Traduction en plusieurs langues

Pour traduire votre projet dans plusieurs langues (par exemple, espagnol, français et allemand), utilisez cette commande :

```bash
translate -l "es fr de"
```

Cette commande traduira le projet en espagnol, français et allemand, en ajoutant les nouvelles traductions sans écraser les existantes.

#### Exemple sur Phi-3 CookBook

Dans le **Phi-3 CookBook**, après avoir récupéré les dernières modifications pour refléter les commits les plus récents, j’ai utilisé la méthode suivante pour traduire les nouveaux fichiers markdown et images ajoutés.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Bien qu’il soit généralement recommandé de traduire une langue à la fois, dans des situations comme celle-ci où des modifications spécifiques doivent être ajoutées, traduire plusieurs langues en une seule fois peut être efficace.

### 3. Spécifier le répertoire racine

Par défaut, le traducteur utilise le répertoire de travail courant. Si votre projet se trouve ailleurs, spécifiez le répertoire racine avec l’option -r :

```bash
translate -l "es fr de" -r "./my_project"
```

Cette commande traduit les fichiers dans `./my_project` into Spanish, French, and German.

### 4. Updating Translations (Deletes Existing Translations)

To update existing translations (i.e., delete the current translations and replace them with new ones), use the `-u` option. Cela supprimera toutes les traductions existantes pour les langues spécifiées et les retraduira.

```bash
translate -l "ko" -u
```

Attention : cette commande vous demandera une confirmation avant de procéder à la suppression des traductions existantes.

#### Exemple sur Phi-3 CookBook

Dans le **Phi-3 CookBook**, j’ai utilisé la méthode suivante pour mettre à jour tous les fichiers traduits en espagnol. Je recommande d’utiliser cette méthode lorsqu’il y a des changements importants dans le contenu original à travers plusieurs documents markdown. S’il n’y a que quelques fichiers markdown traduits à mettre à jour, il est plus efficace de supprimer manuellement ces fichiers spécifiques puis d’utiliser la méthode `-a` pour ajouter les traductions mises à jour.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 6. Traduire uniquement les images

Pour ne traduire que les fichiers images de votre projet, utilisez l’option `-img` :

```bash
translate -l "ko" -img
```

Cette commande traduira uniquement les images en coréen, sans affecter les fichiers markdown.

### 7. Traduire uniquement les fichiers Markdown

Pour ne traduire que les fichiers markdown de votre projet, utilisez l’option `-md` :

```bash
translate -l "ko" -md
```

### 8. Vérifier les erreurs dans les fichiers traduits

Si vous souhaitez vérifier les fichiers traduits pour détecter des erreurs et relancer la traduction si nécessaire, utilisez l’option `-chk` :

```bash
translate -l "ko" -chk
```

Cette commande analysera les fichiers markdown traduits et relancera la traduction pour tous les fichiers contenant des erreurs.

#### Exemple sur Phi-3 CookBook

Dans le **Phi-3 CookBook**, j’ai utilisé la méthode suivante pour vérifier les erreurs de traduction dans les fichiers coréens et relancer automatiquement la traduction pour tous les fichiers présentant des problèmes détectés.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Cette option vérifie les erreurs de traduction. Actuellement, si la différence de saut de ligne entre les fichiers originaux et traduits dépasse six, le fichier est signalé comme ayant une erreur de traduction. Je prévois d’améliorer ce critère pour plus de flexibilité à l’avenir.

Par exemple, cette méthode est utile pour détecter les morceaux manquants ou les traductions corrompues, et elle relancera automatiquement la traduction pour ces fichiers.

Cependant, si vous savez déjà quels fichiers posent problème, il est plus efficace de supprimer manuellement ces fichiers puis d’utiliser l’option `-a` option to re-translate them.

### 9. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` :

```bash
translate -l "ko" -d
```

Cette commande lancera la traduction en mode debug, fournissant des informations de journalisation supplémentaires qui peuvent vous aider à identifier les problèmes durant le processus de traduction.

#### Exemple sur Phi-3 CookBook

Dans le **Phi-3 CookBook**, j’ai rencontré un problème où les traductions comportant de nombreux liens dans les fichiers markdown provoquaient des erreurs de formatage, telles que des traductions cassées et des sauts de ligne ignorés. Pour diagnostiquer ce problème, j’ai utilisé l’option `-d` pour voir comment se déroulait le processus de traduction.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 10. Traduire toutes les langues

Si vous souhaitez traduire le projet dans toutes les langues supportées, utilisez le mot-clé all.

> [!WARNING]
> Traduire toutes les langues en une seule fois peut prendre beaucoup de temps selon la taille du projet. Par exemple, traduire le **Phi-3 CookBook** en espagnol a pris environ 2 heures. Vu l’ampleur, il n’est pas réaliste qu’une seule personne gère 20 langues. Il est recommandé de répartir le travail entre plusieurs contributeurs, chacun prenant en charge une ou deux langues, et de mettre à jour les traductions progressivement.

```bash
translate -l "all"
```

Cette commande traduira le projet dans toutes les langues disponibles. Si vous continuez, la traduction peut prendre un temps important selon la taille du projet.

> [!TIP]
>
> ### Supprimer les fichiers à mettre à jour  
> Pour mettre à jour les fichiers récemment modifiés dans une Pull Request, la première étape consiste à supprimer toutes les versions existantes du fichier spécifique situées dans les différents dossiers de traduction des langues. Vous pouvez faire cela en masse avec la commande suivante pour supprimer tous les fichiers portant un nom spécifique dans les dossiers de traduction.
>
> ### Sous Windows :
> 1. **Avec l’invite de commandes** :
>    - Ouvrez l’invite de commandes.
>    - Naviguez jusqu’au dossier où se trouvent les fichiers avec la commande `cd`.
>    - Utilisez la commande suivante pour supprimer les fichiers :
>      ```
>      del /s *filename*
>      ```
>      L’option `/s` recherche également dans les sous-répertoires.
>
> 2. **Avec PowerShell** :
>    - Ouvrez PowerShell.
>    - Exécutez cette commande :
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Remplacez `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` par la commande :
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Remplacez `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` par la commande pour mettre à jour les fichiers les plus récents.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.