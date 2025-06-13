<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:27:39+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "br"
}
-->
# Command reference  
The **Co-op Translator** CLI oferece várias opções para personalizar o processo de tradução:

Command                                       | Description  
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
translate -l "language_codes"                 | Traduz seu projeto para os idiomas especificados. Exemplo: translate -l "es fr de" traduz para espanhol, francês e alemão. Use translate -l "all" para traduzir para todos os idiomas suportados.  
translate -l "language_codes" -u              | Atualiza as traduções apagando as existentes e recriando-as. Warning: Isso apagará todas as traduções atuais para os idiomas especificados.  
translate -l "language_codes" -img            | Traduz apenas arquivos de imagem.  
translate -l "language_codes" -md             | Traduz apenas arquivos Markdown.  
translate -l "language_codes" -chk            | Verifica arquivos traduzidos em busca de erros e tenta traduzir novamente se necessário.  
translate -l "language_codes" -d              | Ativa o modo debug para logs detalhados.  
translate -l "language_codes" -r "root_dir"   | Especifica o diretório raiz do projeto  
translate -l "language_codes" -f              | Usa modo rápido para tradução de imagens (até 3x mais rápido, com pequena perda na qualidade e alinhamento).  
translate -l "language_codes" -y              | Confirma automaticamente todos os prompts (útil para pipelines CI/CD)  
translate -l "language_codes" --help          | detalhes de ajuda dentro do CLI mostrando os comandos disponíveis  

### Exemplos de uso:  

  1. Comportamento padrão (adiciona novas traduções sem apagar as existentes):   translate -l "ko"    translate -l "es fr de" -r "./my_project"  

  2. Adiciona apenas novas traduções de imagens em coreano (não apaga traduções existentes):    translate -l "ko" -img  

  3. Atualiza todas as traduções em coreano (Warning: Isso apaga todas as traduções coreanas existentes antes de traduzir novamente):    translate -l "ko" -u  

  4. Atualiza apenas as imagens coreanas (Warning: Isso apaga todas as imagens coreanas existentes antes de traduzir novamente):    translate -l "ko" -img -u  

  5. Adiciona novas traduções markdown para coreano sem afetar outras traduções:    translate -l "ko" -md  

  6. Verifica arquivos traduzidos em busca de erros e tenta traduzir novamente se necessário: translate -l "ko" -chk  

  7. Verifica arquivos traduzidos em busca de erros e tenta traduzir novamente (apenas markdown): translate -l "ko" -chk -md  

  8. Verifica arquivos traduzidos em busca de erros e tenta traduzir novamente (apenas imagens): translate -l "ko" -chk -img  

  9. Usa modo rápido para tradução de imagens:    translate -l "ko" -img -f  

  10. Exemplo modo debug: - translate -l "ko" -d: Ativa logs de debug.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.