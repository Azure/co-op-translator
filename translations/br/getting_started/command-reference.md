<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:02:28+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "br"
}
-->
# Referência de comandos

O CLI do **Co-op Translator** oferece várias opções para personalizar o processo de tradução:

Comando                                       | Descrição
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "códigos_de_idioma"              | Traduz seu projeto para os idiomas especificados. Exemplo: translate -l "es fr de" traduz para espanhol, francês e alemão. Use translate -l "all" para traduzir para todos os idiomas suportados.
translate -l "códigos_de_idioma" -u           | Atualiza as traduções excluindo as existentes e recriando-as. Atenção: Isso irá apagar todas as traduções atuais dos idiomas especificados.
translate -l "códigos_de_idioma" -img         | Traduz apenas arquivos de imagem.
translate -l "códigos_de_idioma" -md          | Traduz apenas arquivos Markdown.
translate -l "códigos_de_idioma" -nb          | Traduz apenas arquivos de notebook Jupyter (.ipynb).
translate -l "códigos_de_idioma" --fix        | Retraduz arquivos com pontuação de confiança baixa com base nos resultados de avaliações anteriores.
translate -l "códigos_de_idioma" -d           | Ativa o modo de depuração para logs detalhados.
translate -l "códigos_de_idioma" --save-logs, -s | Salva logs de nível DEBUG em arquivos na pasta <root_dir>/logs/ (o console permanece controlado pelo -d)
translate -l "códigos_de_idioma" -r "root_dir"| Especifica o diretório raiz do projeto
translate -l "códigos_de_idioma" -f           | Usa o modo rápido para tradução de imagens (até 3x mais rápido, com leve perda de qualidade e alinhamento).
translate -l "códigos_de_idioma" -y           | Confirma automaticamente todos os prompts (útil para pipelines CI/CD)
translate -l "códigos_de_idioma" --help       | Detalhes de ajuda no CLI mostrando os comandos disponíveis
evaluate -l "código_de_idioma"                | Avalia a qualidade da tradução para um idioma específico e fornece pontuações de confiança
evaluate -l "código_de_idioma" -c 0.8         | Avalia traduções com limiar de confiança personalizado
evaluate -l "código_de_idioma" -f             | Modo de avaliação rápida (apenas baseado em regras, sem LLM)
evaluate -l "código_de_idioma" -D             | Modo de avaliação profunda (apenas LLM, mais detalhado porém mais lento)
evaluate -l "código_de_idioma" --save-logs, -s| Salva logs de nível DEBUG em arquivos na pasta <root_dir>/logs/
migrate-links -l "códigos_de_idioma"          | Reprocessa arquivos Markdown traduzidos para atualizar links para notebooks (.ipynb). Prefere notebooks traduzidos quando disponíveis; caso contrário, pode usar os originais.
migrate-links -l "códigos_de_idioma" -r       | Especifica o diretório raiz do projeto (padrão: diretório atual).
migrate-links -l "códigos_de_idioma" --dry-run| Mostra quais arquivos seriam alterados sem salvar as mudanças.
migrate-links -l "códigos_de_idioma" --no-fallback-to-original | Não reescreve links para notebooks originais quando os traduzidos estiverem ausentes (só atualiza quando o traduzido existe).
migrate-links -l "códigos_de_idioma" -d       | Ativa o modo de depuração para logs detalhados.
migrate-links -l "códigos_de_idioma" --save-logs, -s | Salva logs de nível DEBUG em arquivos na pasta <root_dir>/logs/
migrate-links -l "all" -y                     | Processa todos os idiomas e confirma automaticamente o aviso.

## Exemplos de uso

  1. Comportamento padrão (adiciona novas traduções sem apagar as existentes):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Adiciona apenas novas traduções de imagens em coreano (não apaga traduções existentes):    translate -l "ko" -img

  3. Atualiza todas as traduções em coreano (Atenção: Isso apaga todas as traduções coreanas antes de retraduzir):    translate -l "ko" -u

  4. Atualiza apenas imagens em coreano (Atenção: Isso apaga todas as imagens coreanas antes de retraduzir):    translate -l "ko" -img -u

  5. Adiciona novas traduções Markdown para coreano sem afetar outras traduções:    translate -l "ko" -md

  6. Corrige traduções com baixa confiança com base em avaliações anteriores: translate -l "ko" --fix

  7. Corrige traduções com baixa confiança apenas para arquivos específicos (markdown): translate -l "ko" --fix -md

  8. Corrige traduções com baixa confiança apenas para arquivos específicos (imagens): translate -l "ko" --fix -img

  9. Usa modo rápido para tradução de imagens:    translate -l "ko" -img -f

  10. Corrige traduções com baixa confiança usando limiar personalizado: translate -l "ko" --fix -c 0.8

  11. Exemplo de modo de depuração: - translate -l "ko" -d: Ativa logs de depuração.
  12. Salva logs em arquivos: translate -l "ko" -s
  13. DEBUG no console e em arquivo: translate -l "ko" -d -s

  14. Migra links de notebooks para traduções coreanas (atualiza links para notebooks traduzidos quando disponíveis):    migrate-links -l "ko"

  15. Migra links em modo dry-run (sem salvar arquivos):    migrate-links -l "ko" --dry-run

  16. Atualiza links apenas quando notebooks traduzidos existem (não usa originais):    migrate-links -l "ko" --no-fallback-to-original

  17. Processa todos os idiomas com prompt de confirmação:    migrate-links -l "all"

  18. Processa todos os idiomas e confirma automaticamente:    migrate-links -l "all" -y
  19. Salva logs em arquivos para migrate-links:    migrate-links -l "ko ja" -s

### Exemplos de avaliação

> [!WARNING]  
> **Funcionalidade Beta**: A funcionalidade de avaliação está atualmente em beta. Este recurso foi lançado para avaliar documentos traduzidos, e os métodos de avaliação e implementação detalhada ainda estão em desenvolvimento e podem mudar.

  1. Avalia traduções coreanas: evaluate -l "ko"

  2. Avalia com limiar de confiança personalizado: evaluate -l "ko" -c 0.8

  3. Avaliação rápida (apenas baseada em regras): evaluate -l "ko" -f

  4. Avaliação profunda (apenas baseada em LLM): evaluate -l "ko" -D

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.