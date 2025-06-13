<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:25:42+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "pt"
}
-->
# Guia de Solução de Problemas do Microsoft Co-op Translator

## Visão Geral  
O Microsoft Co-Op Translator é uma ferramenta poderosa para traduzir documentos Markdown de forma fluida. Este guia ajudará você a resolver problemas comuns ao usar a ferramenta.

## Problemas Comuns e Soluções

### 1. Problema com Tag Markdown  
**Problema:** O documento Markdown traduzido inclui uma tag `markdown` no topo, causando problemas na renderização.

**Solução:** Para resolver isso, basta excluir a tag `markdown` no início do arquivo. Isso permitirá que o arquivo Markdown seja renderizado corretamente.

**Passos:**  
1. Abra o arquivo Markdown traduzido (`.md`).  
2. Localize a tag `markdown` no topo do documento.  
3. Exclua a tag `markdown`.  
4. Salve as alterações no arquivo.  
5. Reabra o arquivo para garantir que ele seja renderizado corretamente.

### 2. Problema com URL de Imagens Incorporadas  
**Problema:** As URLs das imagens incorporadas não correspondem ao local de idioma, resultando em imagens incorretas ou ausentes.

**Solução:** Verifique a URL das imagens incorporadas e certifique-se de que correspondam ao local de idioma. Todas as imagens estão na pasta `translated_images` e cada imagem possui uma tag de local de idioma no nome do arquivo.

**Passos:**  
1. Abra o documento Markdown traduzido.  
2. Identifique as imagens incorporadas e suas URLs.  
3. Verifique se o local de idioma no nome do arquivo da imagem corresponde ao idioma do documento.  
4. Atualize as URLs, se necessário.  
5. Salve as alterações e reabra o documento para confirmar que as imagens são exibidas corretamente.

### 3. Precisão da Tradução  
**Problema:** O conteúdo traduzido não está preciso ou precisa de mais ajustes.

**Solução:** Revise o documento traduzido e faça as edições necessárias para melhorar a precisão e a legibilidade.

**Passos:**  
1. Abra o documento traduzido.  
2. Revise o conteúdo cuidadosamente.  
3. Faça as edições necessárias para aprimorar a precisão da tradução.  
4. Salve as alterações.

### 4. Problemas de Formatação do Arquivo  
**Problema:** A formatação do documento traduzido está incorreta. Isso pode ocorrer em tabelas; aqui, o adicional ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` resolverá os problemas da tabela.

**Passos:**  
1. Abra o documento traduzido.  
2. Compare-o com o documento original para identificar problemas de formatação.  
3. Ajuste a formatação para corresponder ao documento original.  
4. Salve as alterações.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.