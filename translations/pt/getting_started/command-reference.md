<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:00:01+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "pt"
}
-->
# Referência de comandos

A linha de comandos do **Co-op Translator** oferece várias opções para personalizar o processo de tradução:

Comando                                       | Descrição
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "códigos_idioma"                 | Traduz o seu projeto para os idiomas especificados. Exemplo: translate -l "es fr de" traduz para espanhol, francês e alemão. Use translate -l "all" para traduzir para todos os idiomas suportados.
translate -l "códigos_idioma" -u              | Atualiza as traduções, eliminando as existentes e recriando-as. Atenção: Isto elimina todas as traduções atuais dos idiomas especificados.
translate -l "códigos_idioma" -img            | Traduz apenas ficheiros de imagem.
translate -l "códigos_idioma" -md             | Traduz apenas ficheiros Markdown.
translate -l "códigos_idioma" -nb             | Traduz apenas ficheiros Jupyter notebook (.ipynb).
translate -l "códigos_idioma" --fix           | Retraduz ficheiros com pontuações de confiança baixas, com base em resultados de avaliações anteriores.
translate -l "códigos_idioma" -d              | Ativa o modo de depuração para registo detalhado.
translate -l "códigos_idioma" --save-logs, -s | Guarda registos de nível DEBUG em ficheiros na pasta <root_dir>/logs/ (a consola continua controlada por -d)
translate -l "códigos_idioma" -r "root_dir"   | Especifica a pasta raiz do projeto
translate -l "códigos_idioma" -f              | Utiliza o modo rápido para tradução de imagens (até 3x mais rápido, com ligeira perda de qualidade e alinhamento).
translate -l "códigos_idioma" -y              | Confirma automaticamente todos os avisos (útil para pipelines CI/CD)
translate -l "códigos_idioma" --help          | Detalhes de ajuda na linha de comandos, mostrando os comandos disponíveis
evaluate -l "código_idioma"                  | Avalia a qualidade da tradução para um idioma específico e apresenta pontuações de confiança
evaluate -l "código_idioma" -c 0.8           | Avalia traduções com um limiar de confiança personalizado
evaluate -l "código_idioma" -f               | Modo de avaliação rápida (apenas baseado em regras, sem LLM)
evaluate -l "código_idioma" -D               | Modo de avaliação profunda (apenas LLM, mais rigoroso mas mais lento)
evaluate -l "código_idioma" --save-logs, -s  | Guarda registos de nível DEBUG em ficheiros na pasta <root_dir>/logs/
migrate-links -l "códigos_idioma"             | Reprocessa ficheiros Markdown traduzidos para atualizar links para notebooks (.ipynb). Prefere notebooks traduzidos quando disponíveis; caso contrário, pode recorrer aos originais.
migrate-links -l "códigos_idioma" -r          | Especifica a pasta raiz do projeto (por defeito: pasta atual).
migrate-links -l "códigos_idioma" --dry-run   | Mostra quais os ficheiros que seriam alterados sem gravar alterações.
migrate-links -l "códigos_idioma" --no-fallback-to-original | Não reescreve links para notebooks originais quando não existem versões traduzidas (só atualiza quando existe tradução).
migrate-links -l "códigos_idioma" -d          | Ativa o modo de depuração para registo detalhado.
migrate-links -l "códigos_idioma" --save-logs, -s | Guarda registos de nível DEBUG em ficheiros na pasta <root_dir>/logs/
migrate-links -l "all" -y                      | Processa todos os idiomas e confirma automaticamente o aviso.

## Exemplos de utilização

  1. Comportamento por defeito (adiciona novas traduções sem eliminar as existentes):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Adiciona apenas novas traduções de imagens em coreano (não elimina traduções existentes):    translate -l "ko" -img

  3. Atualiza todas as traduções em coreano (Atenção: Elimina todas as traduções existentes em coreano antes de retraduzir):    translate -l "ko" -u

  4. Atualiza apenas imagens em coreano (Atenção: Elimina todas as imagens existentes em coreano antes de retraduzir):    translate -l "ko" -img -u

  5. Adiciona novas traduções Markdown para coreano sem afetar outras traduções:    translate -l "ko" -md

  6. Corrige traduções com baixa confiança com base em resultados de avaliações anteriores: translate -l "ko" --fix

  7. Corrige traduções com baixa confiança apenas para ficheiros específicos (markdown): translate -l "ko" --fix -md

  8. Corrige traduções com baixa confiança apenas para ficheiros específicos (imagens): translate -l "ko" --fix -img

  9. Utiliza o modo rápido para tradução de imagens:    translate -l "ko" -img -f

  10. Corrige traduções com baixa confiança com limiar personalizado: translate -l "ko" --fix -c 0.8

  11. Exemplo de modo de depuração: - translate -l "ko" -d: Ativa o registo de depuração.
  12. Guarda registos em ficheiros: translate -l "ko" -s
  13. DEBUG na consola e em ficheiro: translate -l "ko" -d -s

  14. Migra links de notebooks para traduções em coreano (atualiza links para notebooks traduzidos quando disponíveis):    migrate-links -l "ko"

  15. Migra links em modo dry-run (sem gravar ficheiros):    migrate-links -l "ko" --dry-run

  16. Só atualiza links quando existem notebooks traduzidos (não recorre aos originais):    migrate-links -l "ko" --no-fallback-to-original

  17. Processa todos os idiomas com aviso de confirmação:    migrate-links -l "all"

  18. Processa todos os idiomas e confirma automaticamente:    migrate-links -l "all" -y
  19. Guarda registos em ficheiros para migrate-links:    migrate-links -l "ko ja" -s

### Exemplos de avaliação

> [!WARNING]  
> **Funcionalidade Beta**: A funcionalidade de avaliação está atualmente em fase beta. Esta funcionalidade foi lançada para avaliar documentos traduzidos, e os métodos de avaliação e implementação detalhada ainda estão em desenvolvimento e podem sofrer alterações.

  1. Avaliar traduções em coreano: evaluate -l "ko"

  2. Avaliar com limiar de confiança personalizado: evaluate -l "ko" -c 0.8

  3. Avaliação rápida (apenas baseada em regras): evaluate -l "ko" -f

  4. Avaliação profunda (apenas baseada em LLM): evaluate -l "ko" -D

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original, na sua língua nativa, deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.