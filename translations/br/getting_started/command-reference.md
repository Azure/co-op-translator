<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T10:56:07+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "br"
}
-->
# Referência de comandos

A CLI do **Co-op Translator** oferece várias opções para personalizar o processo de tradução:

Comando                                      | Descrição
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                | Traduz seu projeto para os idiomas especificados. Exemplo: translate -l "es fr de" traduz para espanhol, francês e alemão. Use translate -l "all" para traduzir para todos os idiomas suportados.
translate -l "language_codes" -u             | Atualiza traduções excluindo as existentes e recriando-as. Aviso: Isso apagará todas as traduções atuais para os idiomas especificados.
translate -l "language_codes" -img           | Traduz apenas arquivos de imagem.
translate -l "language_codes" -md            | Traduz apenas arquivos Markdown.
translate -l "language_codes" -nb            | Traduz apenas arquivos de notebook Jupyter (.ipynb).
translate -l "language_codes" --fix          | Retraduz arquivos com baixa confiança com base nos resultados de avaliação anteriores.
translate -l "language_codes" -d             | Ativa o modo de depuração para logs detalhados.
translate -l "language_codes" --save-logs, -s| Salva logs de nível DEBUG em arquivos dentro de <root_dir>/logs/ (o console permanece controlado por -d)
translate -l "language_codes" -r "root_dir"  | Especifica o diretório raiz do projeto
translate -l "language_codes" -f             | Usa modo rápido para tradução de imagens (até 3x mais rápido, com pequena perda na qualidade e alinhamento).
translate -l "language_codes" -y             | Confirma automaticamente todos os prompts (útil para pipelines CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Ativa ou desativa a adição de uma seção de aviso de tradução automática em markdowns e notebooks traduzidos (padrão: ativado).
translate -l "language_codes" --help         | Exibe detalhes de ajuda dentro da CLI mostrando os comandos disponíveis
evaluate -l "language_code"                   | Avalia a qualidade da tradução para um idioma específico e fornece pontuações de confiança
evaluate -l "language_code" -c 0.8            | Avalia traduções com limiar de confiança personalizado
evaluate -l "language_code" -f                | Modo de avaliação rápida (apenas baseado em regras, sem LLM)
evaluate -l "language_code" -D                | Modo de avaliação profunda (apenas baseado em LLM, mais detalhado porém mais lento)
evaluate -l "language_code" --save-logs, -s   | Salva logs de nível DEBUG em arquivos dentro de <root_dir>/logs/
migrate-links -l "language_codes"             | Reprocessa arquivos Markdown traduzidos para atualizar links para notebooks (.ipynb). Prefere notebooks traduzidos quando disponíveis; caso contrário, pode usar os originais.
migrate-links -l "language_codes" -r          | Especifica o diretório raiz do projeto (padrão: diretório atual).
migrate-links -l "language_codes" --dry-run   | Mostra quais arquivos seriam alterados sem gravar as mudanças.
migrate-links -l "language_codes" --no-fallback-to-original | Não reescreve links para notebooks originais quando as versões traduzidas estiverem ausentes (atualiza apenas quando a tradução existe).
migrate-links -l "language_codes" -d          | Ativa modo de depuração para logs detalhados.
migrate-links -l "language_codes" --save-logs, -s | Salva logs de nível DEBUG em arquivos dentro de <root_dir>/logs/
migrate-links -l "all" -y                      | Processa todos os idiomas e confirma automaticamente o aviso.

## Exemplos de uso

  1. Comportamento padrão (adiciona novas traduções sem apagar as existentes):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Adiciona apenas novas traduções de imagens em coreano (não apaga traduções existentes):    translate -l "ko" -img

  3. Atualiza todas as traduções em coreano (Aviso: isso apaga todas as traduções coreanas existentes antes de retraduzir):    translate -l "ko" -u

  4. Atualiza apenas imagens coreanas (Aviso: isso apaga todas as imagens coreanas existentes antes de retraduzir):    translate -l "ko" -img -u

  5. Adiciona novas traduções markdown para coreano sem afetar outras traduções:    translate -l "ko" -md

  6. Corrige traduções com baixa confiança com base em avaliações anteriores: translate -l "ko" --fix

  7. Corrige traduções com baixa confiança para arquivos específicos (markdown): translate -l "ko" --fix -md

  8. Corrige traduções com baixa confiança para arquivos específicos (imagens): translate -l "ko" --fix -img

  9. Usa modo rápido para tradução de imagens:    translate -l "ko" -img -f

  10. Corrige traduções com baixa confiança com limiar personalizado: translate -l "ko" --fix -c 0.8

  11. Exemplo de modo de depuração: - translate -l "ko" -d: Ativa logs de depuração.
  12. Salva logs em arquivos: translate -l "ko" -s
  13. DEBUG no console e em arquivo: translate -l "ko" -d -s
  14. Traduz sem adicionar avisos de tradução automática nas saídas: translate -l "ko" --no-disclaimer

  15. Migra links de notebooks para traduções coreanas (atualiza links para notebooks traduzidos quando disponíveis):    migrate-links -l "ko"

  15. Migra links com dry-run (sem gravação de arquivos):    migrate-links -l "ko" --dry-run

  16. Atualiza links apenas quando notebooks traduzidos existirem (não usa os originais):    migrate-links -l "ko" --no-fallback-to-original

  17. Processa todos os idiomas com prompt de confirmação:    migrate-links -l "all"

  18. Processa todos os idiomas e confirma automaticamente:    migrate-links -l "all" -y
  19. Salva logs em arquivos para migrate-links:    migrate-links -l "ko ja" -s

### Exemplos de avaliação

> [!WARNING]  
> **Funcionalidade Beta**: A funcionalidade de avaliação está atualmente em beta. Este recurso foi lançado para avaliar documentos traduzidos, e os métodos de avaliação e a implementação detalhada ainda estão em desenvolvimento e sujeitos a mudanças.

  1. Avaliar traduções em coreano: evaluate -l "ko"

  2. Avaliar com limiar de confiança personalizado: evaluate -l "ko" -c 0.8

  3. Avaliação rápida (apenas baseada em regras): evaluate -l "ko" -f

  4. Avaliação profunda (apenas baseada em LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->