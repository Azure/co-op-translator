<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T09:41:08+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "fr"
}
-->
# Contribution à Co-op Translator

Ce projet accueille les contributions et suggestions. La plupart des contributions nécessitent que vous acceptiez un
Accord de Licence de Contributeur (CLA) déclarant que vous avez le droit, et que vous accordez effectivement,
les droits d'utilisation de votre contribution. Pour plus de détails, consultez https://cla.opensource.microsoft.com.

Lorsque vous soumettez une pull request, un bot CLA déterminera automatiquement si vous devez fournir
un CLA et annotera la PR en conséquence (par exemple, vérification de statut, commentaire). Suivez simplement les instructions
fournies par le bot. Vous n'aurez à le faire qu'une seule fois pour tous les dépôts utilisant notre CLA.

## Configuration de l'environnement de développement

Pour configurer l'environnement de développement de ce projet, nous recommandons d'utiliser Poetry pour gérer les dépendances. Nous utilisons `pyproject.toml` pour gérer les dépendances du projet, et donc, pour installer les dépendances, vous devez utiliser Poetry.

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

### Installation du package et des packages requis

#### Avec Poetry (depuis pyproject.toml)

```bash
poetry install
```

### Tests manuels

Avant de soumettre une PR, il est important de tester la fonctionnalité de traduction avec une documentation réelle :

1. Créez un répertoire de test à la racine du projet :
    ```bash
    mkdir test_docs
    ```

2. Copiez dans ce répertoire de test quelques documents markdown et images que vous souhaitez traduire. Par exemple :
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

5. Vérifiez les fichiers traduits dans `test_docs/translations` et `test_docs/translated_images` pour confirmer :
   - La qualité de la traduction
   - La justesse des commentaires de métadonnées
   - La préservation de la structure markdown originale
   - Le bon fonctionnement des liens et images

Ces tests manuels permettent de s'assurer que vos modifications fonctionnent bien dans des scénarios réels.

### Variables d'environnement

1. Créez un fichier `.env` à la racine en copiant le fichier `.env.template` fourni.
1. Remplissez les variables d'environnement comme indiqué.

> [!TIP]
>
> ### Options supplémentaires pour l'environnement de développement
>
> En plus d'exécuter le projet localement, vous pouvez aussi utiliser GitHub Codespaces ou les conteneurs de développement VS Code pour une configuration alternative de l'environnement de développement.
>
> #### GitHub Codespaces
>
> Vous pouvez exécuter ces exemples virtuellement en utilisant GitHub Codespaces sans configuration supplémentaire.
>
> Le bouton ouvrira une instance VS Code basée sur le web dans votre navigateur :
>
> 1. Ouvrez le modèle (cela peut prendre quelques minutes) :
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Exécution locale avec les conteneurs de développement VS Code
>
> ⚠️ Cette option ne fonctionnera que si Docker Desktop dispose d'au moins 16 Go de RAM alloués. Si vous avez moins de 16 Go, vous pouvez essayer l’[option GitHub Codespaces](../..) ou [configurer localement](../..).
>
> Une option associée est l’utilisation des conteneurs de développement VS Code, qui ouvrira le projet dans votre VS Code local avec l’[extension Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) :
>
> 1. Lancez Docker Desktop (installez-le si ce n’est pas déjà fait)
> 2. Ouvrez le projet :
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Style de code

Nous utilisons [Black](https://github.com/psf/black) comme formateur de code Python pour maintenir un style cohérent dans tout le projet. Black est un formateur de code sans compromis qui reformate automatiquement le code Python pour respecter le style Black.

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

2. Formatez un fichier ou un répertoire spécifique :
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Avec pip

1. Formatez tous les fichiers Python du projet :
    ```bash
    black .
    ```

2. Formatez un fichier ou un répertoire spécifique :
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Nous recommandons de configurer votre éditeur pour formater automatiquement le code avec Black à chaque sauvegarde. La plupart des éditeurs modernes supportent cela via des extensions ou plugins.

## Exécuter Co-op Translator

Pour exécuter Co-op Translator avec Poetry dans votre environnement, suivez ces étapes :

1. Rendez-vous dans le répertoire où vous souhaitez effectuer des tests de traduction ou créez un dossier temporaire à cet effet.

2. Exécutez la commande suivante. Remplacez `-l ko` par le code de la langue dans laquelle vous souhaitez traduire. Le flag `-d` active le mode debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Assurez-vous que votre environnement Poetry est activé (poetry shell) avant d’exécuter la commande.

## Contribuer une nouvelle langue

Nous accueillons les contributions ajoutant la prise en charge de nouvelles langues. Avant d’ouvrir une PR, veuillez compléter les étapes ci-dessous pour faciliter la revue.

1. Ajoutez la langue dans la correspondance des polices
   - Modifiez `src/co_op_translator/fonts/font_language_mappings.yml`
   - Ajoutez une entrée avec :
     - `code` : code de langue de type ISO (ex. `vi`)
     - `name` : nom affiché convivial
     - `font` : une police fournie dans `src/co_op_translator/fonts/` qui supporte le script
     - `rtl` : `true` si écriture de droite à gauche, sinon `false`

2. Incluez les fichiers de police requis (si nécessaire)
   - Si une nouvelle police est nécessaire, vérifiez la compatibilité de licence pour la distribution open source
   - Ajoutez le fichier de police dans `src/co_op_translator/fonts/`

3. Vérification locale
   - Lancez des traductions sur un petit échantillon (Markdown, images, notebooks selon le cas)
   - Vérifiez que le rendu est correct, y compris les polices et la mise en page RTL si applicable

4. Mettez à jour la documentation
   - Assurez-vous que la langue apparaît dans `getting_started/supported-languages.md`
   - Aucun changement n’est nécessaire dans `getting_started/README_languages_template.md` ; il est généré à partir de la liste des langues supportées

5. Ouvrez une PR
   - Décrivez la langue ajoutée et les éventuelles considérations sur les polices/licences
   - Joignez des captures d’écran des rendus si possible

Exemple d’entrée YAML :

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Tester la nouvelle langue

Vous pouvez tester la nouvelle langue en exécutant la commande suivante :

```bash
# Créez et activez un environnement virtuel
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Installez le paquet de développement
pip install -e .
# Exécutez la traduction
translate -l "new_lang"
```

## Mainteneurs

### Message de commit et stratégie de fusion

Pour garantir la cohérence et la clarté de l’historique des commits de notre projet, nous suivons un format spécifique pour le message de commit **final** lors de l’utilisation de la stratégie **Squash and Merge**.

Lorsqu’une pull request (PR) est fusionnée, les commits individuels sont regroupés en un seul commit. Le message final doit suivre le format ci-dessous pour maintenir un historique propre et cohérent.

#### Format du message de commit (pour squash and merge)

Nous utilisons le format suivant pour les messages de commit :

```bash
<type>: <description> (#<numéro PR>)
```

- **type** : Spécifie la catégorie du commit. Nous utilisons les types suivants :
  - `Docs` : pour les mises à jour de documentation.
  - `Build` : pour les modifications liées au système de build ou aux dépendances, y compris les mises à jour des fichiers de configuration, workflows CI, ou Dockerfile.
  - `Core` : pour les modifications du cœur du projet ou des fonctionnalités, notamment celles impliquant des fichiers dans le répertoire `src/co_op_translator/core`.

- **description** : un résumé concis du changement.
- **numéro PR** : le numéro de la pull request associée au commit.

**Exemples** :

- `Docs: Mise à jour des instructions d'installation pour plus de clarté (#50)`
- `Core: Amélioration de la gestion de la traduction d'images (#60)`

> [!NOTE]
> Actuellement, les préfixes **`Docs`**, **`Core`** et **`Build`** sont ajoutés automatiquement aux titres des PR en fonction des labels appliqués au code source modifié. Tant que le label correct est appliqué, vous n’avez généralement pas besoin de modifier manuellement le titre de la PR. Il suffit de vérifier que tout est correct et que le préfixe a bien été généré.

#### Stratégie de fusion

Nous utilisons **Squash and Merge** comme stratégie par défaut pour les pull requests. Cette stratégie garantit que les messages de commit respectent notre format, même si les commits individuels ne le font pas.

**Avantages** :

- Un historique de projet propre et linéaire.
- Cohérence dans les messages de commit.
- Réduction du bruit causé par des commits mineurs (ex. "correction de typo").

Lors de la fusion, assurez-vous que le message de commit final suit le format décrit ci-dessus.

**Exemple de Squash and Merge**
Si une PR contient les commits suivants :

- `fix typo`
- `update README`
- `adjust formatting`

Ils doivent être regroupés en :
`Docs: Amélioration de la clarté et du formatage de la documentation (#65)`

### Processus de publication

Cette section décrit la manière la plus simple pour les mainteneurs de publier une nouvelle version de Co-op Translator.

#### 1. Incrémenter la version dans `pyproject.toml`

1. Décidez du prochain numéro de version (nous suivons le versionnage sémantique : `MAJOR.MINOR.PATCH`).
2. Modifiez `pyproject.toml` et mettez à jour le champ `version` sous `[tool.poetry]`.
3. Ouvrez une pull request dédiée ne modifiant que la version (et les fichiers de verrouillage/métadonnées mis à jour automatiquement, le cas échéant).
4. Après revue, utilisez **Squash and Merge** et assurez-vous que le message de commit final respecte le format décrit ci-dessus.

#### 2. Créer une Release GitHub

1. Rendez-vous sur la page du dépôt GitHub et ouvrez **Releases** → **Draft a new release**.
2. Créez un nouveau tag (par exemple, `v0.13.0`) à partir de la branche `main`.
3. Donnez au titre de la release le même numéro de version (par exemple, `v0.13.0`).
4. Cliquez sur **Generate release notes** pour remplir automatiquement le changelog.
5. Modifiez éventuellement le texte (par exemple, pour mettre en avant les nouvelles langues supportées ou les changements importants).
6. Publiez la release.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->