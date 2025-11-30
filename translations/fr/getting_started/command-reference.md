<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T09:43:06+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "fr"
}
-->
# Référence des commandes

L'interface en ligne de commande **Co-op Translator** propose plusieurs options pour personnaliser le processus de traduction :

Commande                                      | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Traduit votre projet dans les langues spécifiées. Exemple : translate -l "es fr de" traduit en espagnol, français et allemand. Utilisez translate -l "all" pour traduire dans toutes les langues prises en charge.
translate -l "language_codes" -u              | Met à jour les traductions en supprimant les existantes puis en les recréant. Attention : cela supprimera toutes les traductions actuelles pour les langues spécifiées.
translate -l "language_codes" -img            | Traduit uniquement les fichiers image.
translate -l "language_codes" -md             | Traduit uniquement les fichiers Markdown.
translate -l "language_codes" -nb             | Traduit uniquement les fichiers Jupyter notebook (.ipynb).
translate -l "language_codes" --fix           | Retraduit les fichiers avec des scores de confiance faibles selon les résultats d’évaluation précédents.
translate -l "language_codes" -d              | Active le mode debug pour un journal détaillé.
translate -l "language_codes" --save-logs, -s | Sauvegarde les journaux de niveau DEBUG dans des fichiers sous <root_dir>/logs/ (la console reste contrôlée par -d)
translate -l "language_codes" -r "root_dir"   | Spécifie le répertoire racine du projet
translate -l "language_codes" -f              | Utilise le mode rapide pour la traduction d’images (jusqu’à 3x plus rapide avec un léger compromis sur la qualité et l’alignement).
translate -l "language_codes" -y              | Confirme automatiquement toutes les invites (utile pour les pipelines CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Active ou désactive l’ajout d’une section de mention indiquant une traduction automatique dans les fichiers markdown et notebooks traduits (par défaut : activé).
translate -l "language_codes" --help          | Affiche l’aide dans la CLI avec les commandes disponibles
evaluate -l "language_code"                  | Évalue la qualité de la traduction pour une langue spécifique et fournit des scores de confiance
evaluate -l "language_code" -c 0.8           | Évalue les traductions avec un seuil de confiance personnalisé
evaluate -l "language_code" -f               | Mode d’évaluation rapide (basé sur des règles uniquement, sans LLM)
evaluate -l "language_code" -D               | Mode d’évaluation approfondi (basé sur LLM uniquement, plus complet mais plus lent)
evaluate -l "language_code" --save-logs, -s  | Sauvegarde les journaux de niveau DEBUG dans des fichiers sous <root_dir>/logs/
migrate-links -l "language_codes"             | Reprocessus des fichiers Markdown traduits pour mettre à jour les liens vers les notebooks (.ipynb). Privilégie les notebooks traduits quand disponibles ; sinon peut revenir aux notebooks originaux.
migrate-links -l "language_codes" -r          | Spécifie le répertoire racine du projet (par défaut : répertoire courant).
migrate-links -l "language_codes" --dry-run   | Affiche les fichiers qui seraient modifiés sans écrire les changements.
migrate-links -l "language_codes" --no-fallback-to-original | Ne réécrit pas les liens vers les notebooks originaux lorsque les versions traduites sont manquantes (met à jour uniquement quand la traduction existe).
migrate-links -l "language_codes" -d          | Active le mode debug pour un journal détaillé.
migrate-links -l "language_codes" --save-logs, -s | Sauvegarde les journaux de niveau DEBUG dans des fichiers sous <root_dir>/logs/
migrate-links -l "all" -y                      | Traite toutes les langues et confirme automatiquement l’avertissement.

## Exemples d’utilisation

  1. Comportement par défaut (ajoute de nouvelles traductions sans supprimer les existantes) :   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Ajoute uniquement de nouvelles traductions d’images en coréen (aucune traduction existante n’est supprimée) :    translate -l "ko" -img

  3. Met à jour toutes les traductions coréennes (Attention : cela supprime toutes les traductions coréennes existantes avant de retraduire) :    translate -l "ko" -u

  4. Met à jour uniquement les images coréennes (Attention : cela supprime toutes les images coréennes existantes avant de retraduire) :    translate -l "ko" -img -u

  5. Ajoute de nouvelles traductions markdown pour le coréen sans affecter les autres traductions :    translate -l "ko" -md

  6. Corrige les traductions à faible confiance selon les résultats d’évaluation précédents : translate -l "ko" --fix

  7. Corrige les traductions à faible confiance pour des fichiers spécifiques uniquement (markdown) : translate -l "ko" --fix -md

  8. Corrige les traductions à faible confiance pour des fichiers spécifiques uniquement (images) : translate -l "ko" --fix -img

  9. Utilise le mode rapide pour la traduction d’images :    translate -l "ko" -img -f

  10. Corrige les traductions à faible confiance avec un seuil personnalisé : translate -l "ko" --fix -c 0.8

  11. Exemple de mode debug : - translate -l "ko" -d : active la journalisation debug.
  12. Sauvegarde les journaux dans des fichiers : translate -l "ko" -s
  13. DEBUG console et DEBUG fichier : translate -l "ko" -d -s
  14. Traduire sans ajouter de mentions de traduction automatique dans les sorties : translate -l "ko" --no-disclaimer

  15. Migrer les liens des notebooks pour les traductions coréennes (met à jour les liens vers les notebooks traduits quand disponibles) :    migrate-links -l "ko"

  15. Migration des liens en mode dry-run (sans écrire dans les fichiers) :    migrate-links -l "ko" --dry-run

  16. Met à jour les liens uniquement quand les notebooks traduits existent (ne revient pas aux originaux) :    migrate-links -l "ko" --no-fallback-to-original

  17. Traite toutes les langues avec invite de confirmation :    migrate-links -l "all"

  18. Traite toutes les langues et confirme automatiquement :    migrate-links -l "all" -y
  19. Sauvegarde les journaux dans des fichiers pour migrate-links :    migrate-links -l "ko ja" -s

### Exemples d’évaluation

> [!WARNING]  
> **Fonctionnalité Beta** : La fonctionnalité d’évaluation est actuellement en version beta. Cette fonctionnalité a été publiée pour évaluer les documents traduits, et les méthodes d’évaluation ainsi que la mise en œuvre détaillée sont encore en cours de développement et susceptibles d’évoluer.

  1. Évaluer les traductions coréennes : evaluate -l "ko"

  2. Évaluer avec un seuil de confiance personnalisé : evaluate -l "ko" -c 0.8

  3. Évaluation rapide (basée sur des règles uniquement) : evaluate -l "ko" -f

  4. Évaluation approfondie (basée sur LLM uniquement) : evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->