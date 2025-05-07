<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-05-06T17:43:59+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "br"
}
-->
# Usando o Modo Somente Markdown

## Introdução  
O modo somente Markdown foi criado para traduzir apenas o conteúdo em Markdown do seu projeto. Esse modo ignora a tradução de imagens e foca exclusivamente no texto, sendo ideal para situações em que a tradução de imagens não é necessária ou quando as variáveis de ambiente para Computer Vision não estão configuradas.

## Quando Usar  
- Quando as variáveis de ambiente relacionadas ao Computer Vision não estiverem configuradas.  
- Quando você quiser traduzir apenas o texto, sem atualizar os links das imagens.  
- Quando for especificado explicitamente pelo usuário usando a opção `-md` na linha de comando.

## Como Ativar  
Para ativar o modo somente Markdown, use a opção `-md` no seu comando. Por exemplo:  
```
translate -l "ko" -md
```

Ou, se as variáveis de ambiente relacionadas ao Computer Vision não estiverem configuradas, executar `translate -l "ko"` ativará automaticamente o modo somente Markdown.

```
translate -l "ko"
```

Esse comando traduz o conteúdo Markdown para coreano e mantém os links das imagens apontando para seus caminhos originais, sem modificá-los para caminhos de imagens traduzidas.

## Comportamento  
No modo somente Markdown:  
- O processo de tradução ignora a etapa de tradução de imagens.  
- Os links das imagens no Markdown permanecem inalterados, apontando para seus caminhos originais.

## Exemplos  
### Antes  
```markdown
![Image](../../../getting_started/translated/path/to/image.png)
```  
### Depois de usar o modo somente Markdown  
```markdown
![Image](../../../getting_started/original/path/to/image.png)
```

## Solução de Problemas  
- Certifique-se de que a opção `-md` está corretamente especificada no comando.  
- Verifique se nenhuma variável de ambiente do Computer Vision está interferindo no processo.

## Conclusão  
O modo somente Markdown oferece uma forma simplificada de traduzir o conteúdo de texto sem modificar os links das imagens. É especialmente útil quando a tradução de imagens não é necessária ou quando se trabalha em ambientes sem configuração de Computer Vision.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.