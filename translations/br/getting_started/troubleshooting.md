<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-05-06T17:50:33+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "br"
}
-->
# Microsoft Co-op Translator Troubleshooting Guide


## Overview
O Microsoft Co-Op Translator é uma ferramenta poderosa para traduzir documentos Markdown de forma fluida. Este guia ajudará você a solucionar problemas comuns encontrados ao usar a ferramenta.

## Common Issues and Solutions

### 1. Markdown Tag Issue
**Problem:** O documento Markdown traduzido inclui uma tag `markdown` no topo, causando problemas na renderização.

**Solution:** Para resolver, basta excluir a tag `markdown` no início do arquivo. Isso permitirá que o arquivo Markdown seja exibido corretamente.

**Steps:**
1. Abra o arquivo Markdown traduzido (`.md`).
2. Localize a tag `markdown` no topo do documento.
3. Apague a tag `markdown`.
4. Salve as alterações no arquivo.
5. Reabra o arquivo para garantir que ele seja exibido corretamente.

### 2. Embedded Images URL Issue
**Problem:** As URLs das imagens incorporadas não correspondem ao idioma do documento, resultando em imagens incorretas ou ausentes.

**Solution:** Verifique a URL das imagens incorporadas e confirme que elas correspondem ao idioma do documento. Todas as imagens estão na pasta `translated_images` e cada imagem possui um identificador de idioma no nome do arquivo.

**Steps:**
1. Abra o documento Markdown traduzido.
2. Identifique as imagens incorporadas e suas URLs.
3. Verifique se o idioma no nome do arquivo da imagem corresponde ao idioma do documento.
4. Atualize as URLs, se necessário.
5. Salve as alterações e reabra o documento para confirmar que as imagens são exibidas corretamente.

### 3. Translation Accuracy
**Problem:** O conteúdo traduzido não está preciso ou precisa de ajustes adicionais.

**Solution:** Revise o documento traduzido e faça as edições necessárias para melhorar a precisão e a clareza.

**Steps:**
1. Abra o documento traduzido.
2. Revise o conteúdo com atenção.
3. Faça as edições necessárias para aprimorar a precisão da tradução.
4. Salve as alterações.

### 4. File Formatting Issues
**Problem:** A formatação do documento traduzido está incorreta. Isso pode ocorrer em tabelas; aqui, um ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` adicional ajudará a corrigir os problemas da tabela.

**Steps:**
1. Abra o documento traduzido.
2. Compare com o documento original para identificar problemas de formatação.
3. Ajuste a formatação para que corresponda ao documento original.
4. Salve as alterações.

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.