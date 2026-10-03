# Traduire, modifier et relire un petit projet

Commencez avec deux petits fichiers Markdown et une langue cible. Vous verrez où les traductions sont écrites, ce qui se passe lorsque la source change, et comment vérifier le résultat.

## Résultats enregistrés

L'exemple a été exécuté le 19 septembre 2026 avec Co-op Translator 0.21.0 et Azure OpenAI (`gpt-5-mini`). Les commandes CLI non modifiées ont été invoquées via `CliRunner` de Click en utilisant la roue construite et les dépendances Python existantes.

| Étape | Résultat |
| --- | --- |
| Aperçu | Code de sortie 0; aucune traduction par modèle demandée |
| Traduction initiale | Code de sortie 0; 27.36 secondes |
| Relecture initiale | Code de sortie 0 |
| Modifier le README et relire | Code de sortie 1; traduction obsolète détectée |
| Mise à jour de la traduction | Code de sortie 0; 22.17 secondes |
| Relecture après mise à jour | Code de sortie 0; aucune erreur ni avertissement |
| Guide inchangé | Octets identiques avant et après la mise à jour du README |
| Relancer | Code de sortie 0; hachages identiques pour tous les fichiers de traduction |

Il s'agit de mesures de runs individuels, pas de garanties de performance. Le temps d'installation est exclu; la facturation du fournisseur n'a pas été mesurée. Une exécution inchangée peut néanmoins effectuer un contrôle de santé du fournisseur.

Consultez la [traduction initiale](../../assets/demo/before.txt), la [traduction mise à jour](../../assets/demo/after.txt), le [diff complet de la traduction](../../assets/demo/update.diff), la [relecture périmée](../../assets/demo/review-stale.txt), la [relecture finale](../../assets/demo/review-after.txt) et les [détails de l'exécution](../../assets/demo/results.json). Une traduction de fichier complet peut modifier d'autres formulations, comme le montre le diff capturé. Les deux artefacts textuels conservent la clause de non-responsabilité générée.

L'examen humain reste important : la mise à jour capturée utilise `[사용 가이드](guide.md)을`; la particule coréenne devrait être `[사용 가이드](guide.md)를`. Les artefacts textuels conservent cette sortie telle quelle plutôt que de présenter une traduction modifiée comme sortie du modèle. La relecture structurelle réussit malgré ce problème de formulation.

## 1. Préparer un petit dossier

Utilisez Python 3.11–3.14 et le [guide de configuration de l'environnement virtuel](configuration.md#local-runtime-setup). Installez la version utilisée pour cet exemple :

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Téléchargez [README.txt](../../assets/demo/README.txt) et [guide.txt](../../assets/demo/guide.txt) dans ce dossier, en les enregistrant sous `README.md` et `guide.md`. Ce sont de petits documents fictifs de projet ; aucune installation d'application n'est nécessaire.

Le README inclut un bloc de code et un lien vers `guide.md`. Sa phrase finale est :

```text
Notes are saved locally.
```

Ne conservez que ces deux documents source dans ce dossier. Toutes les commandes suivantes s'exécutent à l'intérieur de `translation-demo` et fonctionnent sous Bash et PowerShell.

## 2. Aperçu sans identifiants

```bash
translate -l "ko" -md --dry-run
```

L'aperçu estime le travail de traduction sans appeler un modèle ni écrire de traductions. Les estimations de tokens ne constituent pas un devis de facturation. La première exécution devrait identifier les deux fichiers Markdown comme travail nouveau.

## 3. Choisir un fournisseur et traduire

Configurez un fournisseur en utilisant le [guide de configuration](configuration.md) : Azure OpenAI, OpenAI ou Anthropic. La traduction de texte avec OpenAI et Anthropic ne nécessite pas de compte Azure. Les services d'image ne sont pas nécessaires pour cet exemple.

Si vous utilisez un fichier local `.env`, ajoutez `.env` au `.gitignore` de ce dossier. Les appels de traduction utilisent votre compte fournisseur et peuvent entraîner des frais.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Ouvrez `translations/ko/README.md` et `translations/ko/guide.md`. Vérifiez le libellé coréen, le bloc de code et le lien du README traduit vers le guide traduit. La formulation de la sortie varie selon le modèle.

`co-op-review` vérifie la fraîcheur, la structure et les liens locaux. Un résultat positif ne certifie pas l'exactitude linguistique. Résolvez toute erreur signalée avant de continuer.

Enregistrez la ligne de base réussie avec Git (configurez d'abord votre identité Git si nécessaire) :

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Modifier la source

Dans `README.md`, remplacez `Notes are saved locally.` par :

```text
Notes are saved locally as Markdown files.
```

Laissez `guide.md` inchangé. Puis exécutez :

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

La relecture devrait signaler que la traduction du README est périmée et se terminer avec un échec. C'est l'état intermédiaire attendu. L'aperçu devrait identifier le travail pour le README modifié.

## 5. Mettre à jour et inspecter le diff

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Inspectez le diff réel : la CLI par défaut retraduit le fichier modifié, de sorte que le modèle peut aussi revoir d'autres formulations dans ce fichier. Le guide inchangé ne devrait pas avoir de diff. La relecture ne devrait plus signaler le README comme périmé ; examinez tout autre constat au lieu de les ignorer.

La préservation au niveau des blocs des modifications Markdown humaines nécessite un fournisseur d'état de traduction optionnel dans l'[API Python](api.md). Il n'est pas activé par ces commandes CLI.

## 6. Relancer sans modifications

Validez la source et la traduction mises à jour :

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Avec les traductions actuelles et une configuration inchangée, le traducteur ignore les fichiers. La commande Git finale ne devrait produire aucun diff et se terminer avec succès.

## Prochaines étapes

- [Traduire uniquement un README et ouvrir une pull request](github-actions.md#your-first-readme-translation-pr).
- [Choisir CLI, API Python ou MCP](workflows.md).
- [Signaler un problème de traduction sans coder](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).