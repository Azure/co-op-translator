# Repositórios Microsoft "For Beginners"

Esta página destina-se aos mantenedores dos repositórios Microsoft "For Beginners" que utilizam a secção README partilhada "Other Courses".

A maioria dos utilizadores do Co-op Translator não precisa desta página.

## Auto-Sync the Other Courses Section

Adicione estes marcadores à volta da secção "Other Courses" no seu README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Cada vez que o Co-op Translator é executado através da CLI ou do GitHub Actions, substitui o conteúdo entre os marcadores pelo modelo empacotado.

## Update the Shared Template

A origem do modelo encontra-se em:

```text
src/co_op_translator/templates/other_courses.md
```

Para atualizar o conteúdo partilhado:

1. Edite o modelo.
2. Abra um pull request para o Co-op Translator.
3. Depois de a alteração ser lançada, execute o Co-op Translator no repositório de destino.

## Sparse Checkout Advisory

Repositórios grandes de cursos podem tornar-se dispendiosos de clonar quando incluem muitas saídas traduzidas. Pode incluir este aviso nas secções de idioma geradas:

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