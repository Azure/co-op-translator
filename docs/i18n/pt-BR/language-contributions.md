# Contribuindo com melhorias de idioma

Seu conhecimento de idioma pode ajudar a melhorar o Co-op Translator. Comece com um exemplo, uma sugestão de correção e uma explicação usando o [formulário de feedback de tradução](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Você não precisa escrever código nem pagar por uma execução de modelo.

## De um relatório para uma melhoria compartilhada

1. Um contribuidor fornece um trecho da fonte, sua tradução e o contexto.
2. Um revisor de idioma verifica o significado, a naturalidade e se a sugestão depende de uma localidade específica ou do curso.
3. Um mantenedor decide se a correção pertence ao curso-fonte, a uma instrução de idioma compartilhada, à configuração de terminologia ou ao código de tradução.
4. Para uma regra compartilhada, um mantenedor compara as saídas antes e depois da mudança no exemplo reportado e em exemplos não relacionados. Os contribuidores podem revisar essas saídas sem executar a ferramenta por conta própria.
5. O PR resultante vincula o relatório e credita as pessoas que forneceram exemplos e revisão. Implantação ou regeneração nos repositórios que consomem é uma etapa separada.

Um relatório não altera automaticamente os prompts nem regenera traduções de cursos. Correções específicas de um curso devem permanecer conectadas ao repositório do curso. Não presuma que uma edição manual sobreviverá a uma retradução posterior; confirme o comportamento para esse fluxo de trabalho.

## Exemplo existente: links Markdown em japonês

O [arquivo de instruções em japonês](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) instrui o modelo a traduzir o texto do link preservando a sintaxe Markdown e o destino do link. Por exemplo, um link escrito como `[text](URL)` não deve se tornar `「text」（URL）`.

Este é um exemplo focado de uma regra de idioma, respaldado por uma ilustração de saída correta e incorreta. Não é evidência de que apenas as instruções do prompt garantam Markdown correto.

O [construtor de prompt Markdown](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) carrega `templates/language/<language_code>.md` usando um código de idioma em letras minúsculas e sem espaços nas extremidades. Se nenhum arquivo existir, ele usa as instruções comuns. Isso descreve o caminho do prompt Markdown; não presuma que cada imagem ou outro caminho de tradução use as mesmas instruções.

Os [testes de prompt](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) verificam se as instruções em japonês estão incluídas. Isso verifica a montagem do prompt, não a qualidade da tradução.

## O que deve constar em uma regra de idioma?

Proponha uma correção estreita e repetível com um exemplo de origem, comportamento esperado e um contraexemplo onde a regra não deve ser aplicada. Preserve o significado, os placeholders, o código, os URLs e a estrutura do documento. Evite transformar a preferência de estilo de uma pessoa ou a terminologia de um curso em uma regra universal.

A atual [implementação de glossário](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) protege termos da tradução. Não é um dicionário de terminologia de origem-para-alvo. Discuta o novo comportamento de terminologia antes de prometer isso aos contribuidores.

## Exemplo da comunidade: um relatório sobre nome de produto em japonês

No [relatório #527](https://github.com/Azure/co-op-translator/issues/527), @hyoshioka0128 identificou uma tradução em japonês que mudou o nome do produto `Co-op Translator` para `Co-op 翻訳`. O relatório incluiu um link para o documento afetado e uma captura de tela, facilitando a localização do problema.

O contribuinte também vinculou um [PR de curso relacionado](https://github.com/microsoft/AZD-for-beginners/pull/109). Na discussão do problema, o mantenedor reconheceu o relatório e propôs investigar por que o nome mudou, incluindo proteção de terminologia, comportamento do glossário e o caminho de tradução.

Isso mostra como um pequeno relatório pode apoiar uma investigação além de uma correção individual de redação. Não é um resultado verificado de antes/depois nem evidência de que as instruções de links Markdown em japonês acima corrigiram este problema de nome de produto.

Você pode contribuir da mesma maneira: compartilhe o texto original, a tradução atual, a correção sugerida e por que isso importa. Adicione um link do documento ou captura de tela quando for útil. Você não precisa diagnosticar a causa ou escrever um prompt antes de reportá-lo.

## Validação antes de adotar uma regra

Use as mesmas amostras de origem, revisão do tradutor, provedor/modelo e configurações de geração para as execuções baseline e candidata, alterando apenas a instrução proposta. Registre a alteração real do prompt e as saídas; repita exemplos quando necessário para distinguir um efeito consistente da variabilidade de saída. Inclua a falha reportada, contextos contrastantes e exemplos que já traduzem corretamente.

| Amostra | Fonte/contexto | Saída baseline | Saída candidata | Avaliação do revisor |
| --- | --- | --- | --- | --- |
| Falha reportada | A coletar | Não executado | Não executado | Pendente |
| Contraexemplo | A coletar | Não executado | Não executado | Pendente |
| Exemplo não afetado | A coletar | Não executado | Não executado | Pendente |

Verifique invariantes estruturais separadamente dos julgamentos linguísticos. Um teste bem-sucedido de carregamento de prompt não é uma avaliação de qualidade, e uma sentença exata esperada não é a única tradução válida. Se estiverem faltando contexto, execuções do modelo ou revisão linguística, mantenha a proposta pendente em vez de afirmar que o problema foi resolvido.