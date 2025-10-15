<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T02:08:23+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "fr"
}
-->
# Guide de dépannage du traducteur Microsoft Co-op

## Vue d'ensemble
Le traducteur Microsoft Co-Op est un outil puissant pour traduire des documents Markdown de façon transparente. Ce guide vous aidera à résoudre les problèmes courants rencontrés lors de l'utilisation de l'outil.

## Problèmes courants et solutions

### 1. Problème de balise Markdown
**Problème :** Le document Markdown traduit inclut une balise `markdown` en haut, ce qui provoque des problèmes d'affichage.

**Solution :** Pour corriger cela, il suffit de supprimer la balise `markdown` en haut du fichier. Le fichier Markdown s'affichera alors correctement.

**Étapes :**
1. Ouvrez le fichier Markdown (`.md`) traduit.
2. Repérez la balise `markdown` en haut du document.
3. Supprimez la balise `markdown`.
4. Enregistrez les modifications.
5. Rouvrez le fichier pour vérifier qu'il s'affiche correctement.

### 2. Problème d'URL des images intégrées
**Problème :** Les URLs des images intégrées ne correspondent pas à la langue du document, ce qui entraîne des images incorrectes ou manquantes.

**Solution :** Vérifiez l'URL des images intégrées et assurez-vous qu'elle correspond à la langue du document. Toutes les images se trouvent dans le dossier `translated_images` et chaque image possède un tag de langue dans son nom de fichier.

**Étapes :**
1. Ouvrez le document Markdown traduit.
2. Identifiez les images intégrées et leurs URLs.
3. Vérifiez que le tag de langue dans le nom du fichier image correspond à la langue du document.
4. Mettez à jour les URLs si nécessaire.
5. Enregistrez les modifications et rouvrez le document pour vérifier que les images s'affichent correctement.

### 3. Précision de la traduction
**Problème :** Le contenu traduit n'est pas précis ou nécessite des modifications supplémentaires.

**Solution :** Relisez le document traduit et apportez les modifications nécessaires pour améliorer la précision et la lisibilité.

**Étapes :**
1. Ouvrez le document traduit.
2. Relisez attentivement le contenu.
3. Apportez les modifications nécessaires pour améliorer la traduction.
4. Enregistrez les changements.

## 4. Erreur de permission, contenu masqué ou 404

Si les images ou le texte ne sont pas traduits dans la bonne langue et qu'en mode debug (-d) vous obtenez une erreur 401, il s'agit d'un problème classique d'authentification : la clé est invalide, expirée ou n'est pas liée à la région de l'endpoint.

Lancez le traducteur co-op avec le [paramètre -d debug](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) pour mieux comprendre la cause du problème.

- **Message d'erreur :** `Access denied due to invalid subscription key or wrong API endpoint.`
- **Causes possibles :**
  - La clé d'abonnement a été masquée ou est incorrecte dans la requête.
  - La clé AI Services ou la clé d'abonnement appartient à une autre ressource Azure (comme Translator ou OpenAI) au lieu d'une ressource **Azure AI Vision**.

 **Type de ressource**
  - Rendez-vous sur le [Portail Azure](https://portal.azure.com) ou [Azure AI Foundry](https://ai.azure.com) et vérifiez que la ressource est de type `Azure AI services` → `Vision`.
  - Validez les clés et assurez-vous d'utiliser la bonne clé.

## 5. Erreurs de configuration (nouvelle gestion des erreurs)

Avec le nouveau système de traduction sélective, Co-op Translator fournit désormais des messages d'erreur explicites lorsque les services requis ne sont pas configurés.

### 5.1. Service Azure AI non configuré pour la traduction d'images

**Problème :** Vous avez demandé la traduction d'images (option `-img`) mais le service Azure AI n'est pas correctement configuré.

**Message d'erreur :**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Solution :**
1. **Option 1** : Configurer le service Azure AI
   - Ajoutez `AZURE_AI_SERVICE_API_KEY` à votre fichier `.env`
   - Ajoutez `AZURE_AI_SERVICE_ENDPOINT` à votre fichier `.env`
   - Vérifiez que le service est accessible

2. **Option 2** : Retirer la demande de traduction d'images
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Configuration requise manquante

**Problème :** La configuration LLM essentielle est manquante.

**Message d'erreur :**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Solution :**
1. Vérifiez que votre fichier `.env` contient au moins une des configurations LLM suivantes :
   - **Azure OpenAI** : `AZURE_OPENAI_API_KEY` et `AZURE_OPENAI_ENDPOINT`
   - **OpenAI** : `OPENAI_API_KEY`
   
   Vous devez configurer soit Azure OpenAI, soit OpenAI, mais pas les deux.

### 5.3. Confusion sur la traduction sélective

**Problème :** Aucun fichier n'a été traduit alors que la commande a réussi.

**Causes possibles :**
- Mauvais paramètres de type de fichier (`-md`, `-img`, `-nb`)
- Aucun fichier correspondant dans le projet
- Structure de répertoire incorrecte

**Solution :**
1. **Utilisez le mode debug** pour voir ce qui se passe :
   ```bash
   translate -l "ko" -md -d
   ```

2. **Vérifiez les types de fichiers** dans votre projet :
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Vérifiez les combinaisons de paramètres** :
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migration depuis l'ancien système

### 6.1. Mode Markdown uniquement obsolète

**Problème :** Les commandes qui reposaient sur le mode automatique markdown-only ne fonctionnent plus comme avant.

**Ancien comportement :**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Nouveau comportement :**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Solution :**
- **Soyez explicite** sur ce que vous souhaitez traduire :
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Comportement inattendu des liens

**Problème :** Les liens dans les fichiers traduits pointent vers des emplacements inattendus.

**Cause :** Le traitement dynamique des liens change selon les types de fichiers sélectionnés.

**Solution :**
1. **Comprenez le nouveau comportement des liens** :
   - `-nb` inclus : Les liens vers les notebooks pointent vers les versions traduites
   - `-nb` exclu : Les liens vers les notebooks pointent vers les fichiers originaux
   - `-img` inclus : Les liens vers les images pointent vers les versions traduites
   - `-img` exclu : Les liens vers les images pointent vers les fichiers originaux

2. **Choisissez la bonne combinaison** selon votre cas d'usage :
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. L'action GitHub s'est exécutée mais aucune Pull Request (PR) n'a été créée

**Symptôme :** Les logs du workflow pour `peter-evans/create-pull-request` affichent :

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Causes probables :**
- **Aucun changement détecté :** L'étape de traduction n'a produit aucune différence (le dépôt est déjà à jour).
- **Sorties ignorées :** `.gitignore` exclut les fichiers que vous souhaitez committer (ex : `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths non conforme :** Les chemins fournis à l'action ne correspondent pas aux emplacements réels des fichiers générés.
- **Logique/conditions du workflow :** L'étape de traduction s'est arrêtée prématurément ou a écrit dans des répertoires inattendus.

**Comment corriger / vérifier :**
1. **Confirmez l'existence des fichiers générés :** Après la traduction, vérifiez que l'espace de travail contient des fichiers nouveaux ou modifiés dans `translations/` et/ou `translated_images/`.
   - Si vous traduisez des notebooks, assurez-vous que les fichiers `.ipynb` sont bien écrits sous `translations/<lang>/...`.
2. **Vérifiez le `.gitignore` :** N'ignorez pas les fichiers générés. Assurez-vous de NE PAS ignorer :
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (si vous traduisez des notebooks)
3. **Assurez-vous que add-paths correspond aux sorties :** Utilisez une valeur multilignes et incluez les deux dossiers si nécessaire :
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Forcez la création d'une PR pour le debug :** Autorisez temporairement les commits vides pour vérifier le câblage :
   ```yaml
   with:
     commit-empty: true
   ```
5. **Lancez en mode debug :** Ajoutez `-d` à la commande de traduction pour afficher les fichiers découverts et écrits.
6. **Permissions (GITHUB_TOKEN) :** Vérifiez que le workflow dispose des droits d'écriture pour créer des commits et des PR :
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Liste de vérification rapide pour le dépannage

Pour résoudre les problèmes de traduction :

1. **Utilisez le mode debug** : Ajoutez le paramètre `-d` pour voir les logs détaillés
2. **Vérifiez vos paramètres** : Assurez-vous que `-md`, `-img`, `-nb` correspondent à votre intention
3. **Vérifiez la configuration** : Vérifiez que votre fichier `.env` contient les clés requises
4. **Testez progressivement** : Commencez avec `-md` uniquement, puis ajoutez les autres types
5. **Vérifiez la structure des fichiers** : Assurez-vous que les fichiers sources existent et sont accessibles

Pour plus d'informations sur les commandes et paramètres disponibles, consultez la [Référence des commandes](./command-reference.md).

---

**Avertissement** :
Ce document a été traduit à l’aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des imprécisions. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.