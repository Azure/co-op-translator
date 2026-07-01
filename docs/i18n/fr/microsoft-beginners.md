# Dépôts Microsoft pour débutants

Cette page est destinée aux mainteneurs des dépôts Microsoft "For Beginners" qui utilisent la section README partagée "Other Courses".

La plupart des utilisateurs de Co-op Translator n'ont pas besoin de cette page.

## Synchronisation automatique de la section Other Courses

Ajoutez ces marqueurs autour de la section "Other Courses" de votre README :

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Chaque fois que Co-op Translator est exécuté via le CLI ou GitHub Actions, il remplace le contenu situé entre les marqueurs par le modèle empaqueté.

## Mettre à jour le modèle partagé

La source du modèle se trouve à :

```text
src/co_op_translator/templates/other_courses.md
```

Pour mettre à jour le contenu partagé :

1. Modifiez le modèle.
2. Ouvrez une pull request vers Co-op Translator.
3. Une fois la modification publiée, exécutez Co-op Translator dans le dépôt cible.

## Avis sur le Sparse Checkout

Les grands dépôts de cours peuvent devenir coûteux à cloner lorsqu'ils incluent de nombreuses sorties traduites. Vous pouvez inclure cet avis dans les sections linguistiques générées :

```markdown
> **Prefer to Clone Locally?**
>
> This repository includes many language translations, which can significantly increase download size. To clone without translations, use sparse checkout:
>
> ```bash
> git clone --filter=blob:none --sparse https://github.com/org/repo.git
> cd repo
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
```