# Contribuir com melhorias linguísticas

O seu conhecimento de línguas pode ajudar a melhorar o Co-op Translator. Comece com um exemplo, uma sugestão de correção e uma explicação usando o [formulário de feedback de tradução](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Não precisa de escrever código nem de pagar por uma execução do modelo.

## De um relatório para uma melhoria partilhada

1. Um contribuinte fornece um excerto da fonte, a sua tradução e o contexto.
2. Um revisor linguístico verifica o significado, a naturalidade e se a sugestão depende de uma localidade ou curso específico.
3. Um mantenedor decide se a correção pertence ao curso de origem, a uma instrução linguística partilhada, à configuração de terminologia ou ao código de tradução.
4. Para uma regra partilhada, um mantenedor compara as saídas antes e depois da alteração no exemplo reportado e em exemplos não relacionados. Os contribuidores podem rever estas saídas sem executar a ferramenta eles próprios.
5. O PR resultante liga o relatório e credita as pessoas que forneceram exemplos e revisão. A implementação ou a regeneração nos repositórios consumidores é uma etapa separada.

Um relatório não altera automaticamente os prompts nem regenera traduções de cursos. As correções específicas de um curso devem permanecer ligadas ao repositório do curso. Não presuma que uma edição manual sobreviva a uma retradução posterior; confirme o comportamento para esse fluxo de trabalho.

## Exemplo existente: ligações Markdown em japonês

O [ficheiro de instruções japonês](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) instrui o modelo a traduzir o texto do link preservando a sintaxe Markdown e o destino do link. Por exemplo, um link escrito como `[text](URL)` não deve tornar-se `「text」（URL）`.

Este é um exemplo focado de uma regra linguística suportada por uma ilustração de saída correta e incorreta. Não é prova de que as instruções do prompt, por si sós, garantam Markdown correcto.

O [Markdown prompt builder](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) carrega `templates/language/<language_code>.md` usando um código de língua em minúsculas e sem espaços. Se não existir ficheiro, utiliza as instruções comuns. Isto descreve o caminho do prompt Markdown; não presuma que cada imagem ou outro caminho de tradução use as mesmas instruções.

Os [testes de prompt](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) verificam que as instruções japonesas estão incluídas. Isso verifica a montagem do prompt, não a qualidade da tradução.

## O que deve constar numa regra linguística?

Proponha uma correção específica e repetível com um exemplo de origem, comportamento esperado e um contraexemplo onde a regra não deve aplicar-se. Preserve o significado, os marcadores de posição, o código, URLs e a estrutura do documento. Evite transformar a preferência de estilo de uma pessoa ou a terminologia de um curso numa regra universal.

A implementação atual do [glossário](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) protege termos da tradução. Não é um dicionário de terminologia de origem para destino. Discuta o novo comportamento da terminologia antes de o prometer aos contribuidores.

## Exemplo da comunidade: um relatório sobre nome de produto em japonês

No [relatório #527](https://github.com/Azure/co-op-translator/issues/527), @hyoshioka0128 identificou uma tradução para japonês que alterou o nome do produto `Co-op Translator` para `Co-op 翻訳`. O relatório incluía um link para o documento afetado e uma captura de ecrã, tornando o problema fácil de localizar.

O contribuinte também ligou um [PR do curso relacionado](https://github.com/microsoft/AZD-for-beginners/pull/109). Na discussão do problema, o mantenedor reconheceu o relatório e propôs investigar por que o nome mudou, incluindo proteção de terminologia, comportamento do glossário e o caminho de tradução.

Isto mostra como um pequeno relatório pode apoiar uma investigação para além de uma correção de redação individual. Não é um resultado verificado de antes/depois nem prova de que as instruções japonesas para ligações Markdown acima corrigiram este problema do nome do produto.

Pode contribuir da mesma forma: partilhe o texto original, a tradução atual, a correção sugerida e por que isso importa. Adicione um link para o documento ou uma captura de ecrã quando for útil. Não precisa de diagnosticar a causa nem de escrever um prompt antes de o reportar.

## Validação antes de adotar uma regra

Use as mesmas amostras de origem, revisão do tradutor, fornecedor/modelo e definições de geração para as execuções de base e candidatas, alterando apenas a instrução proposta. Registe a alteração real do prompt e as saídas; repita os exemplos quando necessário para distinguir um efeito consistente da variabilidade das saídas. Inclua a falha reportada, contextos contrastantes e exemplos que já são traduzidos corretamente.

| Amostra | Fonte/contexto | Saída base | Saída candidata | Avaliação do revisor |
| --- | --- | --- | --- | --- |
| Falha reportada | Por recolher | Não executado | Não executado | Pendente |
| Contraexemplo | Por recolher | Não executado | Não executado | Pendente |
| Exemplo não afetado | Por recolher | Não executado | Não executado | Pendente |

Verifique invariantes estruturais separadamente de julgamentos linguísticos. Um teste de carregamento de prompt bem-sucedido não é uma avaliação de qualidade, e uma única sentença exata esperada não é a única tradução válida. Se faltarem contexto, execuções do modelo ou revisão linguística, mantenha a proposta pendente em vez de afirmar que o problema está resolvido.