<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T02:07:08+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "fr"
}
-->
# Contribuer à Co-op Translator

Ce projet accueille volontiers les contributions et suggestions. La plupart des contributions nécessitent que vous acceptiez un
Contributor License Agreement (CLA) déclarant que vous avez le droit de nous accorder,
et que vous nous accordez effectivement, les droits d'utiliser votre contribution. Pour plus de détails, consultez https://cla.opensource.microsoft.com.

Lorsque vous soumettez une pull request, un bot CLA déterminera automatiquement si vous devez fournir
un CLA et annotera la PR en conséquence (par exemple, vérification de statut, commentaire). Suivez simplement les instructions
fournies par le bot. Vous n'aurez à faire cela qu'une seule fois pour tous les dépôts utilisant notre CLA.

## Configuration de l'environnement de développement

Pour configurer l'environnement de développement de ce projet, nous recommandons d'utiliser Poetry pour gérer les dépendances. Nous utilisons `pyproject.toml` pour gérer les dépendances du projet, donc pour installer les dépendances, vous devez utiliser Poetry.

### Créer un environnement virtuel

#### Avec pip

```bash
python -m venv .venv
```

#### Avec Poetry

```bash
poetry init
```

### Activer l'environnement virtuel

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

### Installer le package et les dépendances requises

#### Avec Poetry (à partir de pyproject.toml)

```bash
poetry install
```

### Tests manuels

Avant de soumettre une PR, il est important de tester la fonctionnalité de traduction avec de la documentation réelle :

1. Créez un dossier de test à la racine du projet :
    ```bash
    mkdir test_docs
    ```

2. Copiez dans ce dossier de test quelques fichiers markdown et images que vous souhaitez traduire. Par exemple :
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Installez le package en local :
    ```bash
    pip install -e .
    ```

4. Lancez Co-op Translator sur vos documents de test :
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Vérifiez les fichiers traduits dans `test_docs/translations` et `test_docs/translated_images` pour vous assurer que :
   - La qualité de la traduction est satisfaisante
   - Les commentaires de métadonnées sont corrects
   - La structure markdown originale est préservée
   - Les liens et images fonctionnent correctement

Ce test manuel permet de s'assurer que vos modifications fonctionnent bien dans des scénarios réels.

### Variables d'environnement

1. Créez un fichier `.env` à la racine du projet en copiant le fichier `.env.template` fourni.
1. Renseignez les variables d'environnement comme indiqué.

> [!TIP]
>
> ### Autres options d'environnement de développement
>
> En plus de l'exécution locale du projet, vous pouvez également utiliser GitHub Codespaces ou les Dev Containers de VS Code pour une configuration alternative de l'environnement de développement.
>
> #### GitHub Codespaces
>
> Vous pouvez exécuter ces exemples virtuellement en utilisant GitHub Codespaces, sans configuration ou paramétrage supplémentaire.
>
> Le bouton ouvrira une instance VS Code basée sur le web dans votre navigateur :
>
> 1. Ouvrez le template (cela peut prendre plusieurs minutes) :
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Exécution locale avec les Dev Containers de VS Code
>
> ⚠️ Cette option ne fonctionnera que si votre Docker Desktop dispose d'au moins 16 Go de RAM. Si vous avez moins de 16 Go de RAM, essayez l'[option GitHub Codespaces](../..) ou [installez-le localement](../..).
>
> Une option similaire est d'utiliser les Dev Containers de VS Code, qui ouvrira le projet dans votre VS Code local grâce à l'[extension Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) :
>
> 1. Démarrez Docker Desktop (installez-le si ce n'est pas déjà fait)
> 2. Ouvrez le projet :
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Style de code

Nous utilisons [Black](https://github.com/psf/black) comme formateur de code Python pour garantir un style de code cohérent dans tout le projet. Black est un formateur de code strict qui reformate automatiquement le code Python pour qu'il respecte le style Black.

#### Configuration

La configuration de Black est spécifiée dans notre `pyproject.toml` :

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installer Black

Vous pouvez installer Black avec Poetry (recommandé) ou pip :

##### Avec Poetry

Black est installé automatiquement lors de la configuration de l'environnement de développement :
```bash
poetry install
```

##### Avec pip

Si vous utilisez pip, vous pouvez installer Black directement :
```bash
pip install black
```

#### Utiliser Black

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
> Nous vous recommandons de configurer votre éditeur pour formater automatiquement le code avec Black à chaque sauvegarde. La plupart des éditeurs modernes le permettent via des extensions ou plugins.

## Exécuter Co-op Translator

Pour exécuter Co-op Translator avec Poetry dans votre environnement, suivez ces étapes :

1. Rendez-vous dans le dossier où vous souhaitez effectuer des tests de traduction ou créez un dossier temporaire à cet effet.

2. Exécutez la commande suivante. Remplacez `-l ko` par le code de la langue cible. L'option `-d` active le mode debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Assurez-vous que votre environnement Poetry est activé (poetry shell) avant d'exécuter la commande.

## Ajouter une nouvelle langue

Nous accueillons volontiers les contributions ajoutant la prise en charge de nouvelles langues. Avant d'ouvrir une PR, veuillez suivre les étapes ci-dessous pour faciliter la revue.

1. Ajoutez la langue au mapping des polices
   - Modifiez `src/co_op_translator/fonts/font_language_mappings.yml`
   - Ajoutez une entrée avec :
     - `code` : code de langue de type ISO (ex : `vi`)
     - `name` : nom lisible par un humain
     - `font` : une police présente dans `src/co_op_translator/fonts/` qui prend en charge l'écriture
     - `rtl` : `true` si la langue s'écrit de droite à gauche, sinon `false`

2. Inclure les fichiers de police nécessaires (si besoin)
   - Si une nouvelle police est requise, vérifiez la compatibilité de la licence pour une distribution open source
   - Ajoutez le fichier de police dans `src/co_op_translator/fonts/`

3. Vérification locale
   - Lancez des traductions sur un petit échantillon (Markdown, images, et notebooks si besoin)
   - Vérifiez que le rendu est correct, y compris la police et la mise en page RTL si applicable

4. Mettez à jour la documentation
   - Vérifiez que la langue apparaît dans `getting_started/supported-languages.md`
   - Pas besoin de modifier `README_languages_template.md` ; il est généré à partir de la liste des langues supportées

5. Ouvrez une PR
   - Décrivez la langue ajoutée et toute considération liée à la police ou à la licence
   - Ajoutez des captures d'écran des rendus si possible

Exemple d'entrée YAML :

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Mainteneurs

### Format des messages de commit et stratégie de fusion

Pour garantir la cohérence et la clarté de l'historique des commits du projet, nous suivons un format spécifique **pour le message de commit final** lors de l'utilisation de la stratégie **Squash and Merge**.

Lorsqu'une pull request (PR) est fusionnée, les commits individuels sont regroupés en un seul commit. Le message de commit final doit suivre le format ci-dessous pour maintenir un historique propre et cohérent.

#### Format du message de commit (pour squash and merge)

Nous utilisons le format suivant pour les messages de commit :

```bash
<type>: <description> (#<PR number>)
```

- **type** : Spécifie la catégorie du commit. Nous utilisons les types suivants :
  - `Docs` : Pour les mises à jour de la documentation.
  - `Build` : Pour les modifications liées au système de build ou aux dépendances, y compris les fichiers de configuration, les workflows CI ou le Dockerfile.
  - `Core` : Pour les modifications du cœur du projet ou des fonctionnalités principales, notamment celles concernant les fichiers du dossier `src/co_op_translator/core`.

- **description** : Un résumé concis du changement.
- **PR number** : Le numéro de la pull request associée au commit.

**Exemples** :

- `Docs: Mise à jour des instructions d'installation pour plus de clarté (#50)`
- `Core: Amélioration de la gestion de la traduction d'images (#60)`

> [!NOTE]
> Actuellement, les préfixes **`Docs`**, **`Core`** et **`Build`** sont ajoutés automatiquement aux titres des PR en fonction des labels appliqués au code source modifié. Tant que le bon label est appliqué, vous n'avez généralement pas besoin de modifier manuellement le titre de la PR. Il vous suffit de vérifier que tout est correct et que le préfixe a bien été généré.

#### Stratégie de fusion

Nous utilisons **Squash and Merge** comme stratégie par défaut pour les pull requests. Cette stratégie garantit que les messages de commit respectent notre format, même si les commits individuels ne le font pas.

**Raisons** :

- Un historique de projet propre et linéaire.
- Cohérence des messages de commit.
- Moins de bruit dû aux petits commits (ex : "fix typo").

Lors de la fusion, assurez-vous que le message de commit final respecte le format décrit ci-dessus.

**Exemple de Squash and Merge**
Si une PR contient les commits suivants :

- `fix typo`
- `update README`
- `adjust formatting`

Ils doivent être regroupés en :
`Docs: Amélioration de la clarté et du formatage de la documentation (#65)`

---

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent comporter des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.