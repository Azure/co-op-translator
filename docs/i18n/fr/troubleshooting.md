# Dépannage

Utilisez cette page lorsque l'exécution d'une traduction réussit de manière inattendue, échoue pendant la configuration ou produit un résultat nécessitant une révision.

## Commencez ici

1. Exécutez d'abord une commande ciblée, par exemple `translate -l "ko" -md`.
2. Ajoutez `-d` pour les journaux de débogage dans la console.
3. Ajoutez `-s` pour enregistrer les journaux de débogage sous `<root-dir>/logs/`.
4. Exécutez `co-op-review` après la traduction pour vérifier l'actualité, la structure et les liens locaux.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Erreurs de configuration

### Aucun fournisseur de modèle linguistique

Erreur :

```text
No language model configuration found.
```

Solution :

- Configurez Azure OpenAI ou OpenAI.
- Vérifiez que les variables se trouvent dans l'environnement où la commande s'exécute.
- Pour une utilisation locale, placez-les dans `.env` à la racine du projet.

Voir [Configuration](configuration.md).

### Traduction d'images sans Azure AI Vision

Erreur :

```text
Image translation requested but Azure AI Service is not configured.
```

Solution :

- Ajoutez `AZURE_AI_SERVICE_API_KEY`.
- Ajoutez `AZURE_AI_SERVICE_ENDPOINT`.
- Ou exécutez une commande uniquement texte comme `translate -l "ko" -md`.

### Clé ou point de terminaison invalide

Les symptômes peuvent inclure `401`, des erreurs d'autorisation masquées, ou des erreurs d'accès au point de terminaison.

Solution :

- Confirmez que la clé appartient à la même ressource Azure que le point de terminaison.
- Confirmez que la ressource prend en charge Vision lorsque vous utilisez `-img`.
- Confirmez que le nom de déploiement Azure OpenAI et la version de l'API correspondent à votre déploiement.
- Exécutez avec les journaux de débogage : `translate -l "ko" -md -d -s`.

## Aucun fichier n'a été traduit

Causes courantes :

- Les indicateurs sélectionnés ne correspondent pas à vos fichiers.
- Des fichiers traduits existent déjà.
- Les fichiers source se trouvent dans des répertoires exclus.
- La commande est exécutée depuis la racine de projet incorrecte.

Vérifications :

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Utilisez `--root-dir` lorsque la commande est exécutée en dehors de la racine du projet.

## Comportement inattendu des liens

La réécriture des liens dépend des types de contenu sélectionnés :

- `-nb` inclus : les liens vers des notebooks peuvent pointer vers des notebooks traduits.
- `-nb` exclu : les liens vers des notebooks peuvent rester pointés vers les notebooks sources.
- `-img` inclus : les liens d'images peuvent pointer vers des images traduites.
- `-img` exclu : les liens d'images peuvent rester pointés vers les images sources.

Exécutez une traduction complète du contenu quand tous les liens internes doivent préférer les versions traduites :

```bash
translate -l "ko" -md -nb -img
```

Exécutez la révision des liens après la traduction :

```bash
co-op-review -l "ko"
```

## Problèmes de rendu Markdown

Si le Markdown traduit s'affiche incorrectement :

- Vérifiez que le frontmatter commence et se termine par `---`.
- Vérifiez que le nombre de délimiteurs de blocs de code correspond entre les fichiers source et traduits.
- Exécutez `co-op-review` pour détecter les problèmes de structure courants.
- Retraduisez le fichier spécifique si la sortie a été corrompue.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action exécuté mais aucune pull request n'a été créée

Si `peter-evans/create-pull-request` indique que la branche n'est pas en avance sur la base, le workflow n'a trouvé aucun fichier à valider.

Causes probables :

- L'exécution de la traduction n'a produit aucun changement.
- `.gitignore` exclut `translations/`, `translated_images/` ou des notebooks traduits.
- `add-paths` ne correspond pas aux répertoires de sortie générés.
- L'étape de traduction s'est terminée prématurément.

Solutions :

1. Confirmez que les fichiers générés existent dans `translations/` ou `translated_images/`.
2. Confirmez que `.gitignore` n'ignore pas les sorties générées.
3. Utilisez des `add-paths` correspondants :

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Ajoutez temporairement des indicateurs de débogage à la commande translate :

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Confirmez que les autorisations du workflow incluent :

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Qualité de la traduction

Les traductions automatiques peuvent nécessiter une relecture humaine. Utilisez `evaluate` uniquement lorsque vous voulez un scoring de qualité expérimental et des workflows de réparation pour les cas de faible confiance.

!!! warning "Experimental"
    `evaluate` peut utiliser des contrôles basés sur des règles et des LLM, et son modèle de scoring ainsi que le comportement des métadonnées peuvent changer. Évitez de l'inclure dans les validations CI obligatoires à moins que votre workflow ne soit préparé à ces changements.

Pour des vérifications CI déterministes, utilisez plutôt `co-op-review`.