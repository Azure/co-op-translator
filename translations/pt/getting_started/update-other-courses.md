<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:42:03+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "pt"
}
-->
# Atualizar a secção "Outros Cursos" (repositórios Microsoft Beginners)

Este guia explica como fazer a secção "Outros Cursos" sincronizar automaticamente usando o Co-op Translator, e como atualizar o modelo global para todos os repositórios.

- Aplica-se a: apenas repositórios Microsoft Beginners
- Funciona com: Co-op Translator CLI e GitHub Actions
- Fonte do modelo: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Início rápido: Ativar a sincronização automática no seu repositório

Adicione os seguintes marcadores à volta da secção "Outros Cursos" no seu README. O Co-op Translator irá substituir tudo o que estiver entre estes marcadores em cada execução.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Cada vez que o Co-op Translator é executado — via CLI (ex.: `translate -l "<language codes>"`) ou GitHub Actions — atualiza automaticamente a secção "Outros Cursos" delimitada por estes marcadores.

> [!NOTE]
> Se já tiver uma lista existente, basta envolvê-la com os mesmos marcadores. Na próxima execução, será substituída pelo conteúdo padronizado mais recente.

---

## Como alterar o conteúdo global

Se quiser atualizar o conteúdo padronizado que aparece em todos os repositórios Beginners:

1. Edite o modelo: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Abra um pull request no repositório do Co-op Translator com as suas alterações
3. Depois de o PR ser aceite, a versão do Co-op Translator será atualizada
4. Na próxima vez que o Co-op Translator for executado (CLI ou GitHub Action) num repositório alvo, irá sincronizar automaticamente a secção atualizada

Isto garante uma única fonte de verdade para o conteúdo "Outros Cursos" em todos os repositórios Beginners.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->