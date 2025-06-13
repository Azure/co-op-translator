<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:25:56+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "br"
}
-->
# Guia de Solução de Problemas do Microsoft Co-op Translator

## Visão Geral  
O Microsoft Co-Op Translator é uma ferramenta poderosa para traduzir documentos Markdown de forma fluida. Este guia ajudará você a solucionar problemas comuns encontrados ao usar a ferramenta.

## Problemas Comuns e Soluções

### 1. Problema com Tag Markdown  
**Problema:** O documento Markdown traduzido inclui uma tag `markdown` no topo, causando problemas na renderização.

**Solução:** Para resolver, basta deletar a tag `markdown` no topo do arquivo. Isso permitirá que o arquivo Markdown seja renderizado corretamente.

**Passos:**  
1. Abra o arquivo Markdown traduzido (`.md`).  
2. Localize a tag `markdown` no topo do documento.  
3. Delete a tag `markdown`.  
4. Salve as alterações no arquivo.  
5. Reabra o arquivo para garantir que ele renderize corretamente.

### 2. Problema com URLs de Imagens Embutidas  
**Problema:** As URLs das imagens embutidas não correspondem ao idioma local, levando a imagens incorretas ou ausentes.

**Solução:** Verifique a URL das imagens embutidas e certifique-se de que correspondem ao idioma local. Todas as imagens estão na pasta `translated_images`, cada imagem possui uma tag de idioma no nome do arquivo.

**Passos:**  
1. Abra o documento Markdown traduzido.  
2. Identifique as imagens embutidas e suas URLs.  
3. Verifique se o idioma no nome do arquivo da imagem corresponde ao idioma do documento.  
4. Atualize as URLs se necessário.  
5. Salve as alterações e reabra o documento para confirmar que as imagens são exibidas corretamente.

### 3. Precisão da Tradução  
**Problema:** O conteúdo traduzido não está preciso ou precisa de ajustes adicionais.

**Solução:** Revise o documento traduzido e faça as edições necessárias para melhorar a precisão e a legibilidade.

**Passos:**  
1. Abra o documento traduzido.  
2. Revise o conteúdo com atenção.  
3. Faça as edições necessárias para melhorar a precisão da tradução.  
4. Salve as alterações.

### 4. Problemas de Formatação do Arquivo  
**Problema:** A formatação do documento traduzido está incorreta. Isso pode ocorrer em tabelas, aqui um ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` adicional ajudará a resolver os problemas da tabela.

**Passos:**  
1. Abra o documento traduzido.  
2. Compare com o documento original para identificar problemas de formatação.  
3. Ajuste a formatação para que corresponda ao documento original.  
4. Salve as alterações.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.