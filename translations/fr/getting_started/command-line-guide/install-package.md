<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-05-06T17:56:31+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "fr"
}
-->
# Installer le package Co-op translator

Le **Co-op Translator** est un outil en ligne de commande (CLI) conçu pour vous aider à traduire tous les fichiers markdown et images de votre projet en plusieurs langues. Ce tutoriel vous guidera pour configurer le traducteur et l’exécuter selon différents cas d’usage.

### Créer un environnement virtuel

Vous pouvez créer un environnement virtuel en utilisant soit `pip` soit `Poetry`. Tapez l’une des commandes suivantes dans votre terminal.

#### Avec pip

```bash
python -m venv .venv
```

#### Avec Poetry

```bash
poetry init
```

### Activer l’environnement virtuel

Après avoir créé l’environnement virtuel, vous devez l’activer. Les étapes varient selon votre système d’exploitation. Tapez la commande suivante dans votre terminal.

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

1. Si vous avez créé l’environnement avec Poetry, tapez la commande suivante dans votre terminal pour l’activer.

    ```bash
    poetry shell
    ```

### Installer le package et les dépendances requises

Une fois votre environnement virtuel configuré et activé, l’étape suivante consiste à installer les dépendances nécessaires.

### Installation rapide

Installer Co-Op Translator via pip

```
pip install co-op-translator
```  
Ou  

Installer via Poetry  
```
poetry add co-op-translator
```

#### Avec pip (depuis requirements.txt) si vous clonez ce dépôt

![NOTE] Veuillez NE PAS faire cela si vous installez co-op translator via l’installation rapide.

1. Si vous utilisez pip, tapez la commande suivante dans votre terminal. Cela installera automatiquement les packages requis spécifiés dans le fichier `requirements.txt` :

    ```bash
    pip install -r requirements.txt
    ```

#### Avec Poetry (depuis pyproject.toml)

1. Si vous utilisez Poetry, tapez la commande suivante dans votre terminal. Cela installera automatiquement les packages requis spécifiés dans le fichier `pyproject.toml` :

    ```bash
    poetry install
    ```

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.