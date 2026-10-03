# Resolução de problemas

Use esta página quando uma execução de tradução for bem-sucedida inesperadamente, falhar durante a configuração ou produzir saída que necessite de revisão.

## Comece Aqui

1. Execute primeiro um comando focado, como `translate -l "ko" -md`.
2. Adicione `-d` para logs de depuração no console.
3. Adicione `-s` para guardar logs de depuração em `<root-dir>/logs/`.
4. Execute `co-op-review` após a tradução para verificar atualidade, estrutura e ligações locais.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Erros de Configuração

### Sem Provedor de Modelo de Linguagem

Erro:

```text
No language model configuration found.
```

Solução:

- Configure o Azure OpenAI, OpenAI ou Anthropic.
- Verifique se as variáveis estão no ambiente onde o comando é executado.
- Para uso local, coloque-as em `.env` na raiz do projeto.

Consulte [Configuração](configuration.md).

### Tradução de Imagens sem Azure AI Vision

Erro:

```text
Image translation requested but Azure AI Service is not configured.
```

Solução:

- Adicione `AZURE_AI_SERVICE_API_KEY`.
- Adicione `AZURE_AI_SERVICE_ENDPOINT`.
- Ou execute um comando apenas de texto, como `translate -l "ko" -md`.

### Chave ou Endpoint Inválido

Os sintomas podem incluir `401`, erros de permissão ocultos ou erros de acesso ao endpoint.

Solução:

- Confirme que a chave pertence ao mesmo recurso Azure que o endpoint.
- Confirme que o recurso suporta Vision quando usar `-img`.
- Confirme que o nome da implantação do Azure OpenAI e a versão da API correspondem à sua implantação.
- Execute com logs de depuração: `translate -l "ko" -md -d -s`.

## Nenhum Ficheiro Foi Traduzido

Causas comuns:

- As flags selecionadas não correspondem aos seus ficheiros.
- Ficheiros traduzidos existentes já estão presentes.
- Os ficheiros de origem estão em diretórios excluídos.
- O comando está a ser executado a partir da raiz do projeto incorreta.

Verificações:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Use `--root-dir` quando o comando for executado fora da raiz do projeto.

## Comportamento inesperado dos links

A reescrita de links depende dos tipos de conteúdo selecionados:

- `-nb` incluído: os links para notebooks podem apontar para notebooks traduzidos.
- `-nb` excluído: os links para notebooks podem continuar a apontar para os notebooks de origem.
- `-img` incluído: os links de imagens podem apontar para imagens traduzidas.
- `-img` excluído: os links de imagens podem continuar a apontar para as imagens de origem.

Execute uma tradução completa do conteúdo quando todos os links internos devem preferir os resultados traduzidos:

```bash
translate -l "ko" -md -nb -img
```

Execute a revisão de links após a tradução:

```bash
co-op-review -l "ko"
```

## Problemas de Renderização de Markdown

Se o Markdown traduzido for renderizado incorretamente:

- Verifique se o frontmatter começa e termina com `---`.
- Verifique se as marcações de blocos de código têm o mesmo número entre o ficheiro de origem e o traduzido.
- Execute `co-op-review` para detetar problemas comuns de estrutura.
- Retraduza o ficheiro específico se a saída estiver corrompida.

```bash
co-op-review -l "ko" --format github
```

## A Ação do GitHub foi Executada mas Não Foi Criado um Pull Request

Se `peter-evans/create-pull-request` reportar que a branch não está à frente da base, o workflow não encontrou ficheiros para commitar.

Causas prováveis:

- A execução de tradução não produziu alterações.
- `.gitignore` exclui `translations/`, `translated_images/` ou notebooks traduzidos.
- `add-paths` não corresponde aos diretórios de saída gerados.
- A etapa de tradução terminou prematuramente.

Soluções:

1. Confirme que os ficheiros gerados existem em `translations/` ou `translated_images/`.
2. Confirme que o `.gitignore` não ignora as saídas geradas.
3. Use `add-paths` correspondentes:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Adicione temporariamente flags de depuração ao comando translate:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Confirme que as permissões do workflow incluem:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Qualidade da Tradução

As traduções automáticas podem necessitar de revisão humana. Use `evaluate` apenas quando pretender pontuação de qualidade experimental e fluxos de trabalho de reparação de baixa confiança.

!!! warning "Experimental"
    O `evaluate` pode utilizar verificações baseadas em regras e em LLM, e o seu modelo de pontuação e o comportamento dos metadados podem mudar. Mantenha-o fora das gates obrigatórias do CI, a menos que o seu fluxo de trabalho esteja preparado para alterações.

Para verificações determinísticas no CI, utilize `co-op-review`.