<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T02:07:53+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "fr"
}
-->
# Référence des commandes

Le CLI **Co-op Translator** propose plusieurs options pour personnaliser le processus de traduction :

Commande                                       | Description
-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                  | Traduit votre projet dans les langues spécifiées. Exemple : translate -l "es fr de" traduit en espagnol, français et allemand. Utilisez translate -l "all" pour traduire dans toutes les langues prises en charge.
translate -l "language_codes" -u               | Met à jour les traductions en supprimant les existantes et en les recréant. Attention : cela supprimera toutes les traductions actuelles pour les langues spécifiées.
translate -l "language_codes" -img             | Traduit uniquement les fichiers image.
translate -l "language_codes" -md              | Traduit uniquement les fichiers Markdown.
translate -l "language_codes" -nb              | Traduit uniquement les fichiers Jupyter notebook (.ipynb).
translate -l "language_codes" --fix            | Retraduit les fichiers avec des scores de confiance faibles selon les résultats d’évaluation précédents.
translate -l "language_codes" -d               | Active le mode debug pour un journal détaillé.
translate -l "language_codes" --save-logs, -s  | Sauvegarde les logs de niveau DEBUG dans des fichiers sous <root_dir>/logs/ (la console reste contrôlée par -d)
translate -l "language_codes" -r "root_dir"    | Spécifie le répertoire racine du projet
translate -l "language_codes" -f               | Utilise le mode rapide pour la traduction d’images (jusqu’à 3x plus rapide, avec une légère perte de qualité et d’alignement).
translate -l "language_codes" -y               | Confirme automatiquement toutes les demandes (utile pour les pipelines CI/CD)
translate -l "language_codes" --help           | Affiche l’aide dans le CLI avec les commandes disponibles
evaluate -l "language_code"                    | Évalue la qualité de la traduction pour une langue spécifique et fournit des scores de confiance
evaluate -l "language_code" -c 0.8             | Évalue les traductions avec un seuil de confiance personnalisé
evaluate -l "language_code" -f                 | Mode d’évaluation rapide (basé sur des règles uniquement, sans LLM)
evaluate -l "language_code" -D                 | Mode d’évaluation approfondi (basé sur LLM uniquement, plus complet mais plus lent)
evaluate -l "language_code" --save-logs, -s    | Sauvegarde les logs de niveau DEBUG dans des fichiers sous <root_dir>/logs/
migrate-links -l "language_codes"              | Re-traite les fichiers Markdown traduits pour mettre à jour les liens vers les notebooks (.ipynb). Privilégie les notebooks traduits si disponibles ; sinon peut revenir aux notebooks originaux.
migrate-links -l "language_codes" -r           | Spécifie le répertoire racine du projet (par défaut : répertoire courant).
migrate-links -l "language_codes" --dry-run    | Affiche les fichiers qui seraient modifiés sans écrire les changements.
migrate-links -l "language_codes" --no-fallback-to-original | Ne pas réécrire les liens vers les notebooks originaux si les versions traduites sont absentes (mettre à jour uniquement si la version traduite existe).
migrate-links -l "language_codes" -d           | Active le mode debug pour un journal détaillé.
migrate-links -l "language_codes" --save-logs, -s | Sauvegarde les logs de niveau DEBUG dans des fichiers sous <root_dir>/logs/
migrate-links -l "all" -y                      | Traite toutes les langues et confirme automatiquement l’avertissement.

## Exemples d’utilisation

  1. Comportement par défaut (ajoute de nouvelles traductions sans supprimer les existantes) :   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Ajouter uniquement de nouvelles traductions d’images en coréen (aucune traduction existante n’est supprimée) :    translate -l "ko" -img

  3. Mettre à jour toutes les traductions coréennes (Attention : cela supprime toutes les traductions coréennes existantes avant de retraduire) :    translate -l "ko" -u

  4. Mettre à jour uniquement les images coréennes (Attention : cela supprime toutes les images coréennes existantes avant de retraduire) :    translate -l "ko" -img -u

  5. Ajouter de nouvelles traductions Markdown en coréen sans affecter les autres traductions :    translate -l "ko" -md

  6. Corriger les traductions à faible confiance selon les résultats d’évaluation précédents : translate -l "ko" --fix

  7. Corriger les traductions à faible confiance pour certains fichiers seulement (markdown) : translate -l "ko" --fix -md

  8. Corriger les traductions à faible confiance pour certains fichiers seulement (images) : translate -l "ko" --fix -img

  9. Utiliser le mode rapide pour la traduction d’images :    translate -l "ko" -img -f

  10. Corriger les traductions à faible confiance avec un seuil personnalisé : translate -l "ko" --fix -c 0.8

  11. Exemple de mode debug : - translate -l "ko" -d : Active le journal de debug.
  12. Sauvegarder les logs dans des fichiers : translate -l "ko" -s
  13. DEBUG console et DEBUG fichier : translate -l "ko" -d -s

  14. Migrer les liens de notebooks pour les traductions coréennes (mettre à jour les liens vers les notebooks traduits si disponibles) :    migrate-links -l "ko"

  15. Migration des liens en mode dry-run (aucune écriture de fichier) :    migrate-links -l "ko" --dry-run

  16. Mettre à jour les liens uniquement si les notebooks traduits existent (ne pas revenir aux originaux) :    migrate-links -l "ko" --no-fallback-to-original

  17. Traiter toutes les langues avec confirmation :    migrate-links -l "all"

  18. Traiter toutes les langues et confirmer automatiquement :    migrate-links -l "all" -y
  19. Sauvegarder les logs dans des fichiers pour migrate-links :    migrate-links -l "ko ja" -s

### Exemples d’évaluation

> [!WARNING]  
> **Fonctionnalité bêta** : La fonctionnalité d’évaluation est actuellement en version bêta. Cette fonctionnalité a été publiée pour évaluer les documents traduits, et les méthodes d’évaluation ainsi que leur implémentation détaillée sont encore en cours de développement et susceptibles d’être modifiées.

  1. Évaluer les traductions coréennes : evaluate -l "ko"

  2. Évaluer avec un seuil de confiance personnalisé : evaluate -l "ko" -c 0.8

  3. Évaluation rapide (basée sur des règles uniquement) : evaluate -l "ko" -f

  4. Évaluation approfondie (basée sur LLM uniquement) : evaluate -l "ko" -D

---

**Avertissement** :
Ce document a été traduit à l’aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des imprécisions. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.