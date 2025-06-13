<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:39:33+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "br"
}
-->
# Modo Somente Markdown

## Introdução
O modo somente Markdown foi criado para traduzir apenas o conteúdo em Markdown do seu projeto. Esse modo ignora o processo de tradução de imagens e foca exclusivamente no conteúdo textual, sendo ideal para situações em que a tradução de imagens não é necessária ou as variáveis de ambiente para Computer Vision não estão configuradas.

## Quando Usar
- Quando as variáveis de ambiente relacionadas ao Computer Vision não estiverem configuradas.
- Quando você quiser traduzir apenas o texto, sem atualizar os links das imagens.
- Quando for especificado explicitamente pelo usuário usando a opção `-md` na linha de comando.

## Como Ativar
Para ativar o modo somente Markdown, use a opção `-md` no seu comando. Por exemplo:
```
translate -l "ko" -md
```

Ou, se as variáveis de ambiente relacionadas ao Computer Vision não estiverem configuradas. Executar `translate -l "ko"` automaticamente ativará o modo somente Markdown.

```
translate -l "ko"
```

Esse comando traduz o conteúdo em Markdown para coreano e mantém os links das imagens apontando para seus caminhos originais, ao invés de modificar para caminhos traduzidos.

## Comportamento
No modo somente Markdown:
- O processo de tradução ignora a etapa de tradução de imagens.
- Os links das imagens no Markdown permanecem inalterados, apontando para seus caminhos originais.

## Exemplos
### Antes
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.br.png)
```
### Depois de usar o modo somente Markdown
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.br.png)
```

## Solução de Problemas
- Verifique se a opção `-md` está corretamente especificada no comando.
- Confirme que nenhuma variável de ambiente do Computer Vision está interferindo no processo.

## Conclusão
O modo somente Markdown oferece uma forma simplificada de traduzir o conteúdo textual sem alterar os links das imagens. É especialmente útil quando a tradução de imagens não é necessária ou quando se trabalha em ambientes sem configuração de Computer Vision.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.