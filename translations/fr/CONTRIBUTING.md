<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:23:47+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "fr"
}
-->
# Contribuer à Co-op Translator

Ce projet accueille les contributions et suggestions. La plupart des contributions nécessitent que vous acceptiez un  
Contrat de Licence de Contributeur (CLA) déclarant que vous avez le droit, et que vous accordez effectivement,  
les droits d’utiliser votre contribution. Pour plus de détails, consultez https://cla.opensource.microsoft.com.

Lorsque vous soumettez une pull request, un bot CLA déterminera automatiquement si vous devez fournir  
un CLA et décorera la PR en conséquence (par exemple, vérification de statut, commentaire). Il vous suffit de suivre les instructions  
du bot. Vous n’aurez à le faire qu’une seule fois pour tous les dépôts utilisant notre CLA.

## Configuration de l’environnement de développement

Pour configurer l’environnement de développement de ce projet, nous recommandons d’utiliser Poetry pour gérer les dépendances. Nous utilisons `pyproject.toml` pour gérer les dépendances du projet, et donc, pour installer les dépendances, vous devez utiliser Poetry.

### Créer un environnement virtuel

#### Avec pip

```bash
python -m venv .venv
```

#### Avec Poetry

```bash
poetry init
```

### Activer l’environnement virtuel

#### Pour pip et Poetry

- Windows :

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux :

    ```bash
    source .venv/bin/activate
    ```

#### Avec Poetry

```bash
poetry shell
```

### Installation du package et des dépendances requises

#### Avec Poetry (depuis pyproject.toml)

```bash
poetry install
```

### Tests manuels

Avant de soumettre une PR, il est important de tester la fonctionnalité de traduction avec une documentation réelle :

1. Créez un dossier test à la racine du projet :  
    ```bash
    mkdir test_docs
    ```

2. Copiez dans ce dossier test des fichiers markdown et images que vous souhaitez traduire. Par exemple :  
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Installez le package localement :  
    ```bash
    pip install -e .
    ```

4. Lancez Co-op Translator sur vos documents de test :  
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Vérifiez les fichiers traduits dans `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`.  
1. Remplissez les variables d’environnement comme indiqué.

> [!TIP]
>
> ### Options supplémentaires pour l’environnement de développement
>
> En plus d’exécuter le projet localement, vous pouvez aussi utiliser GitHub Codespaces ou les conteneurs de développement VS Code pour une autre configuration d’environnement de développement.
>
> #### GitHub Codespaces
>
> Vous pouvez exécuter ces exemples virtuellement en utilisant GitHub Codespaces sans paramétrage ou configuration supplémentaire.
>
> Le bouton ouvrira une instance VS Code basée sur le web dans votre navigateur :
>
> 1. Ouvrez le modèle (cela peut prendre quelques minutes) :
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Exécution locale avec VS Code Dev Containers
>
> ⚠️ Cette option ne fonctionnera que si Docker Desktop dispose d’au moins 16 Go de RAM alloués. Si vous avez moins de 16 Go de RAM, vous pouvez essayer l’[option GitHub Codespaces](../..) ou [configurer localement](../..).
>
> Une option associée est VS Code Dev Containers, qui ouvrira le projet dans votre VS Code local en utilisant l’[extension Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) :
>
> 1. Lancez Docker Desktop (installez-le si ce n’est pas déjà fait)
> 2. Ouvrez le projet :
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Style de code

Nous utilisons [Black](https://github.com/psf/black) comme formateur de code Python pour maintenir un style cohérent dans tout le projet. Black est un formateur de code strict qui reformate automatiquement le code Python pour respecter le style Black.

#### Configuration

La configuration de Black est spécifiée dans notre `pyproject.toml` :

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installation de Black

Vous pouvez installer Black avec Poetry (recommandé) ou pip :

##### Avec Poetry

Black est installé automatiquement lors de la configuration de l’environnement de développement :  
```bash
poetry install
```

##### Avec pip

Si vous utilisez pip, vous pouvez installer Black directement :  
```bash
pip install black
```

#### Utilisation de Black

##### Avec Poetry

1. Formatez tous les fichiers Python du projet :  
    ```bash
    poetry run black .
    ```

2. Formatez un fichier ou un dossier spécifique :  
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Avec pip

1. Formatez tous les fichiers Python du projet :  
    ```bash
    black .
    ```

2. Formatez un fichier ou un dossier spécifique :  
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Nous recommandons de configurer votre éditeur pour formater automatiquement le code avec Black à chaque sauvegarde. La plupart des éditeurs modernes supportent cela via des extensions ou plugins.

## Exécuter Co-op Translator

Pour exécuter Co-op Translator avec Poetry dans votre environnement, suivez ces étapes :

1. Placez-vous dans le dossier où vous souhaitez effectuer les tests de traduction ou créez un dossier temporaire à cet effet.

2. Exécutez la commande suivante. Le flag `-l ko` with the language code you wish to translate into. The `-d` indique le mode debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Assurez-vous que votre environnement Poetry est activé (poetry shell) avant de lancer la commande.

## Mainteneurs

### Message de commit et stratégie de fusion

Pour garantir la cohérence et la clarté de l’historique des commits de notre projet, nous suivons un format spécifique pour le message de commit **final** lors de l’utilisation de la stratégie **Squash and Merge**.

Quand une pull request (PR) est fusionnée, les commits individuels sont compressés en un seul commit. Le message final doit respecter le format ci-dessous pour maintenir un historique propre et cohérent.

#### Format du message de commit (pour squash and merge)

Nous utilisons le format suivant pour les messages de commit :

```bash
<type>: <description> (#<PR number>)
```

- **type** : Spécifie la catégorie du commit. Nous utilisons les types suivants :  
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Mise à jour des instructions d’installation pour plus de clarté (#50)`
- `Core: Amélioration de la gestion de la traduction des images (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `correction de faute`
- `mise à jour du README`
- `ajustement du format`

They should be squashed into:
`Docs : Amélioration de la clarté et du formatage de la documentation (#65)`

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.