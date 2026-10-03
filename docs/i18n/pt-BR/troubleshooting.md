# Solução de problemas

Use esta página quando uma execução de tradução for bem-sucedida de forma inesperada, falhar durante a configuração ou gerar saída que precisa ser revisada.

## Comece aqui

1. Execute primeiro um comando direcionado, como `translate -l "ko" -md`.
2. Adicione `-d` para logs de depuração no console.
3. Adicione `-s` para salvar os logs de depuração em `<root-dir>/logs/`.
4. Execute `co-op-review` após a tradução para verificar atualidade, estrutura e links locais.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Erros de configuração

### Nenhum provedor de modelo de linguagem

Erro:

```text
No language model configuration found.
```

Correção:

- Configure Azure OpenAI, OpenAI ou Anthropic.
- Verifique se as variáveis estão no ambiente onde o comando é executado.
- Para uso local, coloque-as em `.env` na raiz do projeto.

Veja [Configuração](configuration.md).

### Tradução de imagens sem Azure AI Vision

Erro:

```text
Image translation requested but Azure AI Service is not configured.
```

Correção:

- Adicione `AZURE_AI_SERVICE_API_KEY`.
- Adicione `AZURE_AI_SERVICE_ENDPOINT`.
- Ou execute um comando apenas de texto, como `translate -l "ko" -md`.

### Chave ou endpoint inválidos

Os sintomas podem incluir `401`, erros de permissão ocultos ou erros de acesso ao endpoint.

Correção:

- Confirme se a chave pertence ao mesmo recurso do Azure que o endpoint.
- Confirme se o recurso suporta Vision ao usar `-img`.
- Confirme se o nome da implantação do Azure OpenAI e a versão da API correspondem à sua implantação.
- Execute com logs de depuração: `translate -l "ko" -md -d -s`.

## Nenhum arquivo foi traduzido

Causas comuns:

- As flags selecionadas não correspondem aos seus arquivos.
- Arquivos traduzidos existentes já estão presentes.
- Arquivos de origem estão em diretórios excluídos.
- O comando está sendo executado a partir da raiz do projeto errada.

Verificações:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Use `--root-dir` quando o comando for executado fora da raiz do projeto.

## Comportamento inesperado de links

A reescrita de links depende dos tipos de conteúdo selecionados:

- `-nb` incluído: links de notebook podem apontar para notebooks traduzidos.
- `-nb` excluído: links de notebook podem permanecer apontando para os notebooks de origem.
- `-img` incluído: links de imagem podem apontar para imagens traduzidas.
- `-img` excluído: links de imagem podem permanecer apontando para as imagens de origem.

Execute uma tradução completa do conteúdo quando todos os links internos devem preferir as saídas traduzidas:

```bash
translate -l "ko" -md -nb -img
```

Execute a revisão de links após a tradução:

```bash
co-op-review -l "ko"
```

## Problemas de renderização de Markdown

Se o Markdown traduzido for renderizado incorretamente:

- Verifique se o frontmatter começa e termina com `---`.
- Verifique se a contagem de blocos de código corresponde entre os arquivos de origem e traduzidos.
- Execute `co-op-review` para detectar problemas comuns de estrutura.
- Re-traduza o arquivo específico se a saída estiver corrompida.

```bash
co-op-review -l "ko" --format github
```

## A GitHub Action foi executada, mas nenhum Pull Request foi criado

Se `peter-evans/create-pull-request` relatar que o branch não está à frente da base, o workflow não encontrou arquivos para fazer commit.

Possíveis causas:

- A execução de tradução não produziu alterações.
- `.gitignore` exclui `translations/`, `translated_images/` ou notebooks traduzidos.
- `add-paths` não corresponde aos diretórios de saída gerados.
- A etapa de tradução encerrou prematuramente.

Correções:

1. Confirme se os arquivos gerados existem em `translations/` ou `translated_images/`.
2. Confirme se o `.gitignore` não ignora as saídas geradas.
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

5. Confirme se as permissões do workflow incluem:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Qualidade da tradução

Traduções automáticas podem necessitar de revisão humana. Use `evaluate` somente quando desejar pontuação de qualidade experimental e fluxos de trabalho de reparo para baixa confiança.

!!! warning "Experimental"
    `evaluate` pode usar verificações baseadas em regras e em LLM, e seu modelo de pontuação e comportamento de metadados podem mudar. Mantenha-o fora de gates de CI obrigatórios, a menos que seu fluxo de trabalho esteja preparado para mudanças.

Para verificações determinísticas de CI, use `co-op-review` em vez disso.