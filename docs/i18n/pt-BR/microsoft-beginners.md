# Repositórios Microsoft "For Beginners"

Esta página é para mantenedores dos repositórios Microsoft "For Beginners" que usam a seção compartilhada "Other Courses" do README.

A maioria dos usuários do Co-op Translator não precisa desta página.

## Sincronização automática da seção "Other Courses"

Adicione estes marcadores ao redor da seção "Other Courses" no seu README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Cada vez que o Co-op Translator é executado via CLI ou GitHub Actions, ele substitui o conteúdo entre os marcadores pelo template empacotado.

## Atualizar o template compartilhado

A fonte do template está em:

```text
src/co_op_translator/templates/other_courses.md
```

Para atualizar o conteúdo compartilhado:

1. Edite o template.
2. Abra um pull request para o Co-op Translator.
3. Depois que a alteração for publicada, execute o Co-op Translator no repositório de destino.

## Aviso sobre Sparse Checkout

Repositórios de cursos grandes podem ficar caros para clonar quando incluem muitas saídas traduzidas. Você pode incluir este aviso nas seções de idioma geradas:

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