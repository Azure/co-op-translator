<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:21:44+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "fr"
}
-->
# Guide de dépannage du Microsoft Co-op Translator


## Vue d'ensemble
Le Microsoft Co-Op Translator est un outil puissant pour traduire des documents Markdown de manière fluide. Ce guide vous aidera à résoudre les problèmes courants rencontrés lors de l'utilisation de cet outil.

## Problèmes courants et solutions

### 1. Problème de balise Markdown
**Problème :** Le document Markdown traduit inclut une balise `markdown` en haut, ce qui cause des problèmes d'affichage.

**Solution :** Pour résoudre ce problème, il suffit de supprimer la balise `markdown` en haut du fichier. Cela permettra au fichier Markdown de s'afficher correctement.

**Étapes :**
1. Ouvrez le fichier Markdown traduit (`.md`).
2. Repérez la balise `markdown` en haut du document.
3. Supprimez la balise `markdown`.
4. Enregistrez les modifications.
5. Rouvrez le fichier pour vérifier que l'affichage est correct.

### 2. Problème d’URL des images intégrées
**Problème :** Les URL des images intégrées ne correspondent pas à la locale de la langue, ce qui entraîne des images incorrectes ou manquantes.

**Solution :** Vérifiez l’URL des images intégrées et assurez-vous qu’elles correspondent à la locale de la langue. Toutes les images se trouvent dans le dossier `translated_images`, chaque image ayant une étiquette de locale dans son nom de fichier.

**Étapes :**
1. Ouvrez le document Markdown traduit.
2. Identifiez les images intégrées et leurs URL.
3. Vérifiez que la locale dans le nom du fichier image correspond à la langue du document.
4. Mettez à jour les URL si nécessaire.
5. Enregistrez les modifications et rouvrez le document pour confirmer que les images s’affichent correctement.

### 3. Précision de la traduction
**Problème :** Le contenu traduit n’est pas précis ou nécessite des corrections supplémentaires.

**Solution :** Relisez le document traduit et apportez les modifications nécessaires pour améliorer la précision et la lisibilité.

**Étapes :**
1. Ouvrez le document traduit.
2. Relisez attentivement le contenu.
3. Effectuez les modifications nécessaires pour améliorer la précision de la traduction.
4. Enregistrez les modifications.

### 4. Problèmes de formatage du fichier
**Problème :** Le formatage du document traduit est incorrect. Cela peut se produire dans les tableaux, ici un ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` supplémentaire permettra de résoudre les problèmes de tableau.

**Étapes :**
1. Ouvrez le document traduit.
2. Comparez-le avec le document original pour identifier les problèmes de formatage.
3. Ajustez le formatage pour qu’il corresponde à celui du document original.
4. Enregistrez les modifications.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous ne sommes pas responsables des malentendus ou des erreurs d’interprétation résultant de l’utilisation de cette traduction.