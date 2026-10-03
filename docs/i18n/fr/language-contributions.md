# Contribuer aux améliorations linguistiques

Votre connaissance linguistique peut aider à améliorer Co-op Translator. Commencez par un exemple, une correction suggérée et une explication en utilisant le [formulaire de retour sur la traduction](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Vous n'avez pas besoin d'écrire du code ni de payer pour exécuter un modèle.

## D'un signalement à une amélioration partagée

1. Un contributeur fournit un extrait source, sa traduction et le contexte.
2. Un relecteur linguistique vérifie le sens, la naturalité et si la suggestion dépend d'un paramètre régional ou d'un cours particulier.
3. Un responsable décide si la correction appartient au cours source, à une instruction linguistique partagée, à la configuration de terminologie ou au code de traduction.
4. Pour une règle partagée, un responsable compare les sorties avant et après la modification sur l'exemple signalé et sur des exemples non liés. Les contributeurs peuvent examiner ces sorties sans exécuter l'outil eux-mêmes.
5. La PR résultante lie le signalement et crédite les personnes ayant fourni des exemples et des relectures. Le déploiement ou la régénération dans les dépôts consommateurs constitue une étape distincte.

Un signalement ne modifie pas automatiquement les invites ni ne régénère les traductions de cours. Les corrections spécifiques à un cours doivent rester liées au dépôt du cours. Ne supposez pas qu'une modification manuelle survivra à une retraduction ultérieure ; confirmez le comportement pour ce flux de travail.

## Exemple existant : liens Markdown japonais

Le [fichier d'instructions japonais](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) indique au modèle de traduire le texte des liens tout en préservant la syntaxe Markdown et la destination du lien. Par exemple, un lien écrit `[text](URL)` ne doit pas devenir `「text」（URL）`.

Ceci est un exemple ciblé d'une règle linguistique illustrée par une sortie correcte et incorrecte. Ce n'est pas une preuve que les instructions d'invite seules garantissent un Markdown correct.

Le [générateur d'invite Markdown](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) charge `templates/language/<language_code>.md` en utilisant un code de langue mis en minuscules et épuré. Si aucun fichier n'existe, il utilise les instructions communes. Cela décrit le chemin de l'invite Markdown ; ne supposez pas que chaque image ou autre chemin de traduction utilise les mêmes instructions.

Les [tests d'invite](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) vérifient que les instructions japonaises sont incluses. Cela vérifie l'assemblage de l'invite, pas la qualité de la traduction.

## Qu'est-ce qui relève d'une règle linguistique ?

Proposez une correction ciblée et répétable avec un exemple source, le comportement attendu et un contre-exemple où la règle ne doit pas s'appliquer. Préservez le sens, les espaces réservés, le code, les URL et la structure du document. Évitez de transformer la préférence de style d'une personne ou la terminologie d'un cours en règle universelle.

L'[implémentation du glossaire](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) actuelle protège les termes contre la traduction. Ce n'est pas un dictionnaire de terminologie source-vers-cible. Discutez du nouveau comportement terminologique avant de le promettre aux contributeurs.

## Exemple communautaire : un signalement de nom de produit en japonais

Dans le [rapport n°527](https://github.com/Azure/co-op-translator/issues/527), @hyoshioka0128 a identifié une traduction japonaise qui a changé le nom du produit `Co-op Translator` en `Co-op 翻訳`. Le signalement incluait un lien vers le document affecté et une capture d'écran, facilitant la localisation du problème.

Le contributeur a également lié une [PR de cours connexe](https://github.com/microsoft/AZD-for-beginners/pull/109). Dans la discussion du problème, le responsable a reconnu le signalement et proposé d'enquêter sur les raisons du changement de nom, notamment la protection terminologique, le comportement du glossaire et le parcours de traduction.

Cela montre comment un petit signalement peut soutenir une enquête au-delà d'une simple correction de formulation. Ce n'est pas un résultat avant/après vérifié ni une preuve que les instructions Markdown pour les liens japonais ci-dessus ont corrigé ce problème de nom de produit.

Vous pouvez contribuer de la même manière : partagez le texte original, la traduction actuelle, la correction suggérée et pourquoi cela importe. Ajoutez un lien vers le document ou une capture d'écran si utile. Vous n'avez pas besoin de diagnostiquer la cause ni d'écrire une invite avant de le signaler.

## Validation avant d'adopter une règle

Utilisez les mêmes exemples sources, révision du traducteur, fournisseur/modèle et paramètres de génération pour les exécutions de référence et candidates, en ne changeant que l'instruction proposée. Enregistrez le changement réel de l'invite et les sorties ; répétez les exemples si nécessaire pour distinguer un effet cohérent de la variabilité des sorties. Incluez la défaillance signalée, les contextes contrastés et les exemples qui sont déjà correctement traduits.

| Exemple | Source/contexte | Sortie de référence | Sortie candidate | Évaluation du relecteur |
| --- | --- | --- | --- | --- |
| Défaillance signalée | À recueillir | Non exécuté | Non exécuté | En attente |
| Contre-exemple | À recueillir | Non exécuté | Non exécuté | En attente |
| Exemple non affecté | À recueillir | Non exécuté | Non exécuté | En attente |

Vérifiez les invariants structurels séparément des jugements linguistiques. Un test de chargement d'invite réussi n'est pas une évaluation de qualité, et une phrase exacte attendue n'est pas la seule traduction valide. Si le contexte, les exécutions de modèle ou la relecture linguistique manquent, laissez la proposition en attente plutôt que d'affirmer que le problème est résolu.