# Microsoft Beginners Repositories

Deze pagina is voor beheerders van Microsoft "For Beginners" repositories die de gedeelde "Other Courses" README-sectie gebruiken.

De meeste Co-op Translator-gebruikers hebben deze pagina niet nodig.

## Automatisch synchroniseren van de 'Other Courses'-sectie

Voeg deze markers toe rond de 'Other Courses'-sectie in uw README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Elke keer dat Co-op Translator via de CLI of GitHub Actions wordt uitgevoerd, vervangt het de inhoud tussen de markers door het verpakte sjabloon.

## Werk het gedeelde sjabloon bij

De bron van het sjabloon bevindt zich op:

```text
src/co_op_translator/templates/other_courses.md
```

Om de gedeelde inhoud bij te werken:

1. Bewerk het sjabloon.
2. Open een pull request naar Co-op Translator.
3. Nadat de wijziging is vrijgegeven, voert u Co-op Translator uit in de doelrepository.

## Sparse Checkout-advies

Grote cursusrepositories kunnen duur worden om te klonen wanneer ze veel vertaalde output bevatten. U kunt dit advies opnemen in de gegenereerde taalsecties:

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