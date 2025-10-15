<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T02:08:40+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "fr"
}
-->
# Installer le package Co-op Translator

Le **Co-op Translator** est un outil en ligne de commande (CLI) conçu pour vous aider à traduire tous les fichiers markdown et images de votre projet dans plusieurs langues. Ce tutoriel va vous guider pour configurer le traducteur et l'utiliser dans différents cas de figure.

### Créer un environnement virtuel

Vous pouvez créer un environnement virtuel en utilisant soit `pip`, soit `Poetry`. Tapez l'une des commandes suivantes dans votre terminal.

#### Avec pip

```bash
python -m venv .venv
```

#### Avec Poetry

```bash
poetry init
```

### Activer l'environnement virtuel

Après avoir créé l'environnement virtuel, vous devrez l'activer. Les étapes varient selon votre système d'exploitation. Tapez la commande suivante dans votre terminal.

#### Pour pip et Poetry

- Windows :

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux :

    ```bash
    source .venv/bin/activate
    ```

#### Avec Poetry

1. Si vous avez créé l'environnement avec Poetry, tapez la commande suivante dans votre terminal pour l'activer.

    ```bash
    poetry shell
    ```

### Installer le package et les dépendances nécessaires

Une fois votre environnement virtuel prêt et activé, l'étape suivante consiste à installer les dépendances requises.

### Installation rapide

Installez Co-Op Translator via pip

```
pip install co-op-translator
```
Ou 

Installez via poetry
```
poetry add co-op-translator
```

#### Avec pip (à partir de requirements.txt) si vous clonez ce dépôt

> [!NOTE]
> Veuillez NE PAS faire cela si vous installez co-op translator via l'installation rapide.

1. Si vous utilisez pip, tapez la commande suivante dans votre terminal. Elle installera automatiquement les packages nécessaires indiqués dans le fichier `requirements.txt` :

    ```bash
    pip install -r requirements.txt
    ```

#### Avec Poetry (à partir de pyproject.toml)

1. Si vous utilisez Poetry, tapez la commande suivante dans votre terminal. Elle installera automatiquement les packages nécessaires indiqués dans le fichier `pyproject.toml` :

    ```bash
    poetry install
    ```

---

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent comporter des erreurs ou des imprécisions. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.