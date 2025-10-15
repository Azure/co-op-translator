<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T02:08:47+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "fr"
}
-->
# Traduisez votre projet avec Co-op Translator

Le **Co-op Translator** est un outil en ligne de commande (CLI) qui vous aide à traduire les fichiers markdown et image de votre projet dans plusieurs langues. Cette section explique comment utiliser l’outil, détaille les différentes options CLI et propose des exemples pour divers cas d’utilisation.

> [!NOTE]
> Pour la liste complète des commandes et leurs descriptions détaillées, consultez la [Référence des commandes](./command-reference.md).

---

## Scénarios d’exemple et commandes

Voici quelques cas d’utilisation courants du **Co-op Translator**, avec les commandes appropriées à exécuter.

### 1. Traduction basique (une seule langue)

Pour traduire l’ensemble de votre projet (fichiers markdown et images) dans une seule langue, comme le coréen, utilisez la commande suivante :

```bash
translate -l "ko"
```

Cette commande traduira tous les fichiers markdown et image en coréen, en ajoutant de nouvelles traductions sans supprimer celles déjà existantes.

> [!TIP]
>
> Vous souhaitez connaître les codes de langue disponibles dans **Co-op Translator** ? Consultez la section [Langues prises en charge](https://github.com/Azure/co-op-translator#supported-languages) du dépôt pour plus d’informations.

#### Exemple sur Phi-3 CookBook

Dans le **Phi-3 CookBook**, j’ai utilisé la méthode suivante pour ajouter la traduction coréenne aux fichiers markdown et images existants.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Traduire dans plusieurs langues

Pour traduire votre projet dans plusieurs langues (par exemple espagnol, français et allemand), utilisez cette commande :

```bash
translate -l "es fr de"
```

Cette commande traduira le projet en espagnol, français et allemand, en ajoutant de nouvelles traductions sans écraser celles déjà présentes.

#### Exemple sur Phi-3 CookBook

Dans le **Phi-3 CookBook**, après avoir récupéré les dernières modifications pour refléter les derniers commits, j’ai utilisé la méthode suivante pour traduire les nouveaux fichiers markdown et images ajoutés.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Il est généralement recommandé de traduire une langue à la fois, mais dans des situations comme celle-ci où des changements spécifiques doivent être ajoutés, traduire plusieurs langues en même temps peut être efficace.

### 3. Mettre à jour les traductions (supprime les traductions existantes)

Pour mettre à jour les traductions existantes (c’est-à-dire supprimer les traductions actuelles et les remplacer par de nouvelles), utilisez l’option `-u`. Cela supprimera toutes les traductions existantes pour les langues spécifiées et les retraduira.

```bash
translate -l "ko" -u
```

Attention : cette commande vous demandera une confirmation avant de supprimer les traductions existantes.

#### Exemple sur Phi-3 CookBook

Dans le **Phi-3 CookBook**, j’ai utilisé la méthode suivante pour mettre à jour tous les fichiers traduits en espagnol. Je recommande cette méthode lorsqu’il y a des changements importants dans le contenu original sur plusieurs documents markdown. S’il n’y a que quelques fichiers markdown traduits à mettre à jour, il est plus efficace de supprimer manuellement ces fichiers spécifiques puis d’utiliser la méthode `-a` pour ajouter les traductions mises à jour.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Traduire uniquement les images

Pour traduire uniquement les fichiers image de votre projet, utilisez l’option `-img` :

```bash
translate -l "ko" -img
```

Cette commande traduira uniquement les images en coréen, sans toucher aux fichiers markdown.

### 6. Traduire uniquement les fichiers Markdown

Pour traduire uniquement les fichiers markdown de votre projet, utilisez l’option `-md` :

```bash
translate -l "ko" -md
```

#### Exemple sur Phi-3 CookBook

Dans le **Phi-3 CookBook**, j’ai utilisé la méthode suivante pour vérifier les erreurs de traduction dans les fichiers coréens et relancer automatiquement la traduction pour les fichiers présentant des problèmes détectés.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Cette option vérifie les erreurs de traduction. Actuellement, si la différence de sauts de ligne entre le fichier original et le fichier traduit dépasse six, le fichier est signalé comme ayant une erreur de traduction. Je prévois d’améliorer ce critère pour plus de flexibilité à l’avenir.

Par exemple, cette méthode est utile pour détecter les morceaux manquants ou les traductions corrompues, et elle relancera automatiquement la traduction pour ces fichiers.

Cependant, si vous savez déjà quels fichiers posent problème, il est plus efficace de supprimer manuellement ces fichiers et d’utiliser l’option `-a` pour les retraduire.

### 8. Mode débogage

Pour activer une journalisation détaillée afin de faciliter le dépannage, utilisez l’option `-d` :

```bash
translate -l "ko" -d
```

Cette commande exécutera la traduction en mode débogage, fournissant des informations de journalisation supplémentaires qui peuvent vous aider à identifier les problèmes lors du processus de traduction.

#### Exemple sur Phi-3 CookBook

Dans le **Phi-3 CookBook**, j’ai rencontré un problème où les traductions comportant de nombreux liens dans les fichiers markdown provoquaient des erreurs de formatage, comme des traductions cassées et des sauts de ligne ignorés. Pour diagnostiquer ce problème, j’ai utilisé l’option `-d` pour voir comment le processus de traduction fonctionnait.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Traduire dans toutes les langues

Si vous souhaitez traduire le projet dans toutes les langues prises en charge, utilisez le mot-clé all.

> [!WARNING]
> Traduire dans toutes les langues en une seule fois peut prendre beaucoup de temps selon la taille du projet. Par exemple, la traduction du **Phi-3 CookBook** en espagnol a pris environ 2 heures. Vu l’ampleur, il n’est pas réaliste pour une seule personne de gérer 20 langues. Il est recommandé de répartir le travail entre plusieurs contributeurs, chacun s’occupant d’une ou deux langues, et de mettre à jour les traductions progressivement.

```bash
translate -l "all"
```

Cette commande traduira le projet dans toutes les langues disponibles. Si vous continuez, la traduction peut prendre beaucoup de temps selon la taille du projet.

> [!TIP]
>
> ### Suppression manuelle des fichiers traduits (optionnel)
> Les fichiers traduits sont désormais automatiquement détectés et nettoyés lorsqu’un fichier source est mis à jour.
>
> Cependant, si vous souhaitez mettre à jour manuellement une traduction – par exemple, pour refaire un fichier spécifique ou passer outre le comportement du système – vous pouvez utiliser la commande suivante pour supprimer toutes les versions du fichier dans les dossiers de langue.
>
> ### Sous Windows :
> 1. **Avec l’invite de commande** :
>    - Ouvrez l’invite de commande.
>    - Naviguez jusqu’au dossier où se trouvent les fichiers avec la commande `cd`.
>    - Utilisez la commande suivante pour supprimer les fichiers :
>      ```
>      del /s *filename*
>      ```
>      Remplacez `filename` par la partie spécifique du nom de fichier recherchée. L’option `/s` recherche dans les sous-répertoires.
>
> 2. **Avec PowerShell** :
>    - Ouvrez PowerShell.
>    - Exécutez cette commande :
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Remplacez `"C:\YourPath"` par le chemin du dossier et `filename` par le nom spécifique.
>
> ### Sous macOS/Linux :
> 1. **Avec le Terminal** :
>   - Ouvrez le Terminal.
>   - Naviguez jusqu’au répertoire avec `cd`.
>   - Utilisez la commande `find` :
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Remplacez `filename` par le nom spécifique.
>
> Vérifiez toujours les fichiers avant de les supprimer pour éviter toute perte accidentelle.
>
> Une fois les fichiers à remplacer supprimés, il suffit de relancer votre commande `translate -l` pour mettre à jour les derniers changements du fichier.

---

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent comporter des erreurs ou des imprécisions. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.