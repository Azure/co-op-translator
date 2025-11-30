<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:42:26+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "br"
}
-->
# Atualize a seção "Outros Cursos" (repositórios Microsoft Beginners)

Este guia explica como fazer a seção "Outros Cursos" sincronizar automaticamente usando o Co-op Translator, e como atualizar o template global para todos os repositórios.

- Aplica-se a: apenas repositórios Microsoft Beginners
- Funciona com: Co-op Translator CLI e GitHub Actions
- Fonte do template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Início rápido: Ative a sincronização automática no seu repositório

Adicione os seguintes marcadores ao redor da seção "Outros Cursos" no seu README. O Co-op Translator substituirá tudo entre esses marcadores a cada execução.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Cada vez que o Co-op Translator for executado — via CLI (ex: `translate -l "<language codes>"`) ou GitHub Actions — ele atualiza automaticamente a seção "Outros Cursos" delimitada por esses marcadores.

> [!NOTE]
> Se você já tiver uma lista existente, basta envolvê-la com os mesmos marcadores. Na próxima execução, ela será substituída pelo conteúdo padronizado mais recente.

---

## Como alterar o conteúdo global

Se quiser atualizar o conteúdo padronizado que aparece em todos os repositórios Beginners:

1. Edite o template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Abra um pull request no repositório do Co-op Translator com suas alterações
3. Após a mesclagem do PR, a versão do Co-op Translator será atualizada
4. Na próxima vez que o Co-op Translator rodar (CLI ou GitHub Action) em um repositório alvo, ele sincronizará automaticamente a seção atualizada

Isso garante uma fonte única e confiável para o conteúdo "Outros Cursos" em todos os repositórios Beginners.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->