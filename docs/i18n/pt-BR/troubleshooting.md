# Solução de problemas

Use esta página quando uma execução de tradução for bem-sucedida inesperadamente, falhar durante a configuração ou produzir saída que precise de revisão.

## Comece Aqui

1. Execute primeiro um comando focado, como `translate -l "ko" -md`.
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

- Configure Azure OpenAI ou OpenAI.
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

### Chave ou endpoint inválido

Os sintomas podem incluir `401`, erros de permissão ocultos ou erros de acesso ao endpoint.

Correção:

- Confirme que a chave pertence ao mesmo recurso do Azure que o endpoint.
- Confirme que o recurso suporta Vision ao usar `-img`.
- Confirme que o nome de implantação do Azure OpenAI e a versão da API correspondem à sua implantação.
- Execute com logs de depuração: `translate -l "ko" -md -d -s`.

## Nenhum arquivo foi traduzido

Causas comuns:

- As flags selecionadas não correspondem aos seus arquivos.
- Arquivos traduzidos já existentes estão presentes.
- Os arquivos de origem estão em diretórios excluídos.
- O comando está sendo executado a partir do diretório raiz do projeto incorreto.

Verificações:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Use `--root-dir` quando o comando for executado fora da raiz do projeto.

## Comportamento inesperado de links

A reescrita de links depende dos tipos de conteúdo selecionados:

- `-nb` incluído: links de notebooks podem apontar para notebooks traduzidos.
- `-nb` excluído: links de notebooks podem permanecer apontando para notebooks de origem.
- `-img` incluído: links de imagens podem apontar para imagens traduzidas.
- `-img` excluído: links de imagens podem permanecer apontando para imagens de origem.

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
- Verifique se a contagem de cercas de código corresponde entre os arquivos de origem e os traduzidos.
- Execute `co-op-review` para identificar problemas comuns de estrutura.
- Retraduza o arquivo específico se a saída estiver corrompida.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action executado, mas nenhum Pull Request foi criado

Se `peter-evans/create-pull-request` relatar que o branch não está à frente da base, o fluxo de trabalho não encontrou arquivos para commitar.

Causas prováveis:

- A execução da tradução não produziu alterações.
- O `.gitignore` exclui `translations/`, `translated_images/` ou notebooks traduzidos.
- `add-paths` não corresponde aos diretórios de saída gerados.
- A etapa de tradução terminou prematuramente.

Soluções:

1. Confirme se os arquivos gerados existem em `translations/` ou `translated_images/`.
2. Confirme que `.gitignore` não ignora as saídas geradas.
3. Use `add-paths` correspondentes:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Adicione temporariamente flags de depuração ao comando de tradução:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Confirme que as permissões do workflow incluem:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Qualidade da tradução

Traduções automáticas podem precisar de revisão humana. Use `evaluate` apenas quando desejar pontuação de qualidade experimental e fluxos de trabalho de reparo para baixa confiança.

!!! warning "Experimental"
    `evaluate` pode usar verificações baseadas em regras e em LLMs, e seu modelo de pontuação e comportamento de metadados podem mudar. Mantenha-o fora de gates de CI obrigatórios, a menos que seu fluxo de trabalho esteja preparado para mudanças.

Para verificações de CI determinísticas, use `co-op-review` em vez disso.