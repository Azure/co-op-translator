<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-05-06T17:41:08+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "fr"
}
-->
# Référence des commandes
L'interface en ligne de commande **Co-op Translator** offre plusieurs options pour personnaliser le processus de traduction :

Commande                                      | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Traduit votre projet dans les langues spécifiées. Exemple : translate -l "es fr de" traduit en espagnol, français et allemand. Utilisez translate -l "all" pour traduire dans toutes les langues prises en charge.
translate -l "language_codes" -u              | Met à jour les traductions en supprimant les existantes puis en les recréant. Attention : cela supprimera toutes les traductions actuelles pour les langues spécifiées.
translate -l "language_codes" -img            | Traduit uniquement les fichiers image.
translate -l "language_codes" -md             | Traduit uniquement les fichiers Markdown.
translate -l "language_codes" -chk            | Vérifie les fichiers traduits pour détecter des erreurs et relance la traduction si nécessaire.
translate -l "language_codes" -d              | Active le mode debug pour un journal détaillé.
translate -l "language_codes" -r "root_dir"   | Spécifie le répertoire racine du projet.
translate -l "language_codes" -f              | Utilise le mode rapide pour la traduction des images (jusqu’à 3 fois plus rapide, au léger prix de la qualité et de l’alignement).
translate -l "language_codes" -y              | Confirme automatiquement toutes les invites (utile pour les pipelines CI/CD).
translate -l "language_codes" --help          | Affiche l’aide dans la CLI avec les commandes disponibles.

### Exemples d’utilisation :

  1. Comportement par défaut (ajoute de nouvelles traductions sans supprimer les existantes) :   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Ajouter uniquement de nouvelles traductions d’images en coréen (aucune traduction existante n’est supprimée) :    translate -l "ko" -img

  3. Mettre à jour toutes les traductions coréennes (Attention : cela supprime toutes les traductions coréennes existantes avant de retraduire) :    translate -l "ko" -u

  4. Mettre à jour uniquement les images coréennes (Attention : cela supprime toutes les images coréennes existantes avant de retraduire) :    translate -l "ko" -img -u

  5. Ajouter de nouvelles traductions Markdown pour le coréen sans affecter les autres traductions :    translate -l "ko" -md

  6. Vérifier les fichiers traduits pour détecter des erreurs et relancer la traduction si nécessaire : translate -l "ko" -chk

  7. Vérifier les fichiers traduits pour détecter des erreurs et relancer la traduction (uniquement Markdown) : translate -l "ko" -chk -md

  8. Vérifier les fichiers traduits pour détecter des erreurs et relancer la traduction (uniquement images) : translate -l "ko" -chk -img

  9. Utiliser le mode rapide pour la traduction des images :    translate -l "ko" -img -f

  10. Exemple de mode debug : - translate -l "ko" -d : Active la journalisation en mode debug.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle humaine. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.