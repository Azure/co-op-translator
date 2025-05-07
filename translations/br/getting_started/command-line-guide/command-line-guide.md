<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5eb9b53c81804f04bc9456160e79940",
  "translation_date": "2025-05-07T14:08:11+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "br"
}
-->
# Como usar a interface de linha de comando (CLI) do Co-op Translator

## Pré-requisitos

- **Python 3.10 ou superior**: Necessário para executar o Co-op Translator.  
- **Recurso de Modelo de Linguagem**:  
  - **Azure OpenAI** ou outros LLMs. Detalhes podem ser encontrados em [modelos e serviços suportados](../../../../README.md).  
- **Recurso de Visão Computacional** (opcional):  
  - Para tradução de imagens. Se não estiver disponível, o tradutor usará o [modo somente Markdown](../markdown-only-mode.md).  
  - **Azure Computer Vision**

## Índice

1. [Crie um arquivo '.env' no diretório raiz](./create-env-file.md)  
   - Inclua as chaves necessárias para o serviço de modelo de linguagem escolhido.  
   - Se as chaves do Azure Computer Vision forem omitidas ou `-md` for especificado, o tradutor funcionará no modo somente Markdown.  
1. [Instale o pacote Co-op translator](./install-package.md)  
1. [Traduza seu projeto usando o Co-op Translator](./translator-your-project.md)

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.