<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:34:49+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "fr"
}
-->
# Mettre à jour la section "Autres cours" (dépôts Microsoft Beginners)

Ce guide explique comment rendre la section "Autres cours" auto‑synchronisable grâce à Co‑op Translator, et comment mettre à jour le modèle global pour tous les dépôts.

- S’applique à : uniquement les dépôts Microsoft Beginners
- Fonctionne avec : Co‑op Translator CLI et GitHub Actions
- Source du modèle : [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Démarrage rapide : activer l’auto‑synchronisation dans votre dépôt

Ajoutez les marqueurs suivants autour de la section "Autres cours" dans votre README. Co‑op Translator remplacera tout ce qui se trouve entre ces marqueurs à chaque exécution.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

À chaque exécution de Co‑op Translator — via CLI (par exemple, `translate -l "<language codes>"`) ou GitHub Actions — la section "Autres cours" encadrée par ces marqueurs est automatiquement mise à jour.

> [!NOTE]
> Si vous avez déjà une liste existante, il suffit de l’entourer avec les mêmes marqueurs. La prochaine exécution la remplacera par le contenu standardisé le plus récent.

---

## Comment modifier le contenu global

Si vous souhaitez mettre à jour le contenu standardisé qui apparaît dans tous les dépôts Beginners :

1. Modifiez le modèle : [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Ouvrez une pull request dans le dépôt Co-op Translator avec vos modifications
3. Une fois la PR fusionnée, la version de Co‑op Translator sera mise à jour
4. La prochaine fois que Co‑op Translator s’exécutera (CLI ou GitHub Action) dans un dépôt cible, il synchronisera automatiquement la section mise à jour

Cela garantit une source unique et fiable pour le contenu "Autres cours" dans tous les dépôts Beginners.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->