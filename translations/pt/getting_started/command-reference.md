<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T10:52:49+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "pt"
}
-->
# Referência de comandos

A CLI **Co-op Translator** oferece várias opções para personalizar o processo de tradução:

Comando                                      | Descrição
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                | Traduz o seu projeto para as línguas especificadas. Exemplo: translate -l "es fr de" traduz para espanhol, francês e alemão. Use translate -l "all" para traduzir para todas as línguas suportadas.
translate -l "language_codes" -u             | Atualiza traduções eliminando as existentes e recriando-as. Aviso: Isto irá apagar todas as traduções atuais para as línguas especificadas.
translate -l "language_codes" -img           | Traduz apenas ficheiros de imagem.
translate -l "language_codes" -md            | Traduz apenas ficheiros Markdown.
translate -l "language_codes" -nb            | Traduz apenas ficheiros Jupyter notebook (.ipynb).
translate -l "language_codes" --fix          | Retraduz ficheiros com pontuações de confiança baixas com base em resultados de avaliação anteriores.
translate -l "language_codes" -d              | Ativa o modo de depuração para registo detalhado.
translate -l "language_codes" --save-logs, -s | Guarda registos de nível DEBUG em ficheiros na pasta <root_dir>/logs/ (o console mantém-se controlado por -d)
translate -l "language_codes" -r "root_dir"  | Especifica o diretório raiz do projeto
translate -l "language_codes" -f              | Usa modo rápido para tradução de imagens (até 3x mais rápido a desenhar, com ligeira perda de qualidade e alinhamento).
translate -l "language_codes" -y              | Confirma automaticamente todos os prompts (útil para pipelines CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Ativa ou desativa a adição de uma secção de aviso de tradução automática em markdowns e notebooks traduzidos (padrão: ativado).
translate -l "language_codes" --help          | Mostra detalhes de ajuda na CLI com os comandos disponíveis
evaluate -l "language_code"                   | Avalia a qualidade da tradução para uma língua específica e fornece pontuações de confiança
evaluate -l "language_code" -c 0.8            | Avalia traduções com um limiar de confiança personalizado
evaluate -l "language_code" -f                | Modo de avaliação rápida (apenas baseado em regras, sem LLM)
evaluate -l "language_code" -D                | Modo de avaliação profunda (apenas baseado em LLM, mais rigoroso mas mais lento)
evaluate -l "language_code" --save-logs, -s   | Guarda registos de nível DEBUG em ficheiros na pasta <root_dir>/logs/
migrate-links -l "language_codes"             | Reprocessa ficheiros Markdown traduzidos para atualizar links para notebooks (.ipynb). Prefere notebooks traduzidos quando disponíveis; caso contrário, pode recorrer aos originais.
migrate-links -l "language_codes" -r          | Especifica o diretório raiz do projeto (padrão: diretório atual).
migrate-links -l "language_codes" --dry-run   | Mostra quais ficheiros seriam alterados sem escrever alterações.
migrate-links -l "language_codes" --no-fallback-to-original | Não reescreve links para notebooks originais quando as versões traduzidas estão em falta (atualiza apenas quando a tradução existe).
migrate-links -l "language_codes" -d          | Ativa modo de depuração para registo detalhado.
migrate-links -l "language_codes" --save-logs, -s | Guarda registos de nível DEBUG em ficheiros na pasta <root_dir>/logs/
migrate-links -l "all" -y                      | Processa todas as línguas e confirma automaticamente o aviso.

## Exemplos de utilização

  1. Comportamento padrão (adiciona novas traduções sem apagar as existentes):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Adiciona apenas novas traduções de imagens em coreano (não apaga traduções existentes):    translate -l "ko" -img

  3. Atualiza todas as traduções em coreano (Aviso: Isto apaga todas as traduções coreanas existentes antes de retraduzir):    translate -l "ko" -u

  4. Atualiza apenas imagens coreanas (Aviso: Isto apaga todas as imagens coreanas existentes antes de retraduzir):    translate -l "ko" -img -u

  5. Adiciona novas traduções markdown para coreano sem afetar outras traduções:    translate -l "ko" -md

  6. Corrige traduções com baixa confiança com base em avaliações anteriores: translate -l "ko" --fix

  7. Corrige traduções com baixa confiança apenas para ficheiros específicos (markdown): translate -l "ko" --fix -md

  8. Corrige traduções com baixa confiança apenas para ficheiros específicos (imagens): translate -l "ko" --fix -img

  9. Usa modo rápido para tradução de imagens:    translate -l "ko" -img -f

  10. Corrige traduções com baixa confiança com limiar personalizado: translate -l "ko" --fix -c 0.8

  11. Exemplo de modo de depuração: - translate -l "ko" -d: Ativa registo de depuração.
  12. Guarda registos em ficheiros: translate -l "ko" -s
  13. DEBUG no console e em ficheiros: translate -l "ko" -d -s
  14. Traduz sem adicionar avisos de tradução automática às saídas: translate -l "ko" --no-disclaimer

  15. Migra links de notebooks para traduções coreanas (atualiza links para notebooks traduzidos quando disponíveis):    migrate-links -l "ko"

  15. Migra links com dry-run (sem escrever ficheiros):    migrate-links -l "ko" --dry-run

  16. Atualiza links apenas quando existirem notebooks traduzidos (não recorre aos originais):    migrate-links -l "ko" --no-fallback-to-original

  17. Processa todas as línguas com prompt de confirmação:    migrate-links -l "all"

  18. Processa todas as línguas e confirma automaticamente:    migrate-links -l "all" -y
  19. Guarda registos em ficheiros para migrate-links:    migrate-links -l "ko ja" -s

### Exemplos de avaliação

> [!WARNING]  
> **Funcionalidade Beta**: A funcionalidade de avaliação está atualmente em beta. Esta funcionalidade foi lançada para avaliar documentos traduzidos, e os métodos de avaliação e implementação detalhada ainda estão em desenvolvimento e sujeitos a alterações.

  1. Avaliar traduções coreanas: evaluate -l "ko"

  2. Avaliar com limiar de confiança personalizado: evaluate -l "ko" -c 0.8

  3. Avaliação rápida (apenas baseada em regras): evaluate -l "ko" -f

  4. Avaliação profunda (apenas baseada em LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->