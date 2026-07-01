# Resolução de Problemas

Use esta página quando uma execução de tradução for bem-sucedida de forma inesperada, falhar durante a configuração ou gerar saída que necessite de revisão.

## Comece Aqui

1. Execute primeiro um comando focado, como `translate -l "ko" -md`.
2. Adicione `-d` para registos de depuração na consola.
3. Adicione `-s` para guardar os registos de depuração em `<root-dir>/logs/`.
4. Execute `co-op-review` após a tradução para verificar a atualidade, a estrutura e as ligações locais.

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

- Configure Azure OpenAI ou OpenAI.
- Verifique se as variáveis estão no ambiente onde o comando é executado.
- Para uso local, coloque-as em `.env` na raiz do projeto.

Veja [Configuração](configuration.md).

### Tradução de imagens sem Azure AI Vision

Erro:

```text
Image translation requested but Azure AI Service is not configured.
```

Solução:

- Adicione `AZURE_AI_SERVICE_API_KEY`.
- Adicione `AZURE_AI_SERVICE_ENDPOINT`.
- Ou execute um comando apenas de texto, como `translate -l "ko" -md`.

### Chave ou endpoint inválidos

Os sintomas podem incluir `401`, erros de permissão com dados ocultos ou erros de acesso ao endpoint.

Solução:

- Confirme que a chave pertence ao mesmo recurso Azure que o endpoint.
- Confirme que o recurso suporta Vision quando usar `-img`.
- Confirme que o nome de deployment do Azure OpenAI e a versão da API correspondem ao seu deployment.
- Execute com registos de depuração: `translate -l "ko" -md -d -s`.

## Nenhum Ficheiro foi Traduzido

Causas comuns:

- As flags selecionadas não correspondem aos seus ficheiros.
- Já existem ficheiros traduzidos.
- Os ficheiros de origem estão em diretórios excluídos.
- O comando está a ser executado a partir da raiz do projeto errada.

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
- `-nb` excluído: os links para notebooks podem permanecer apontados para os notebooks de origem.
- `-img` incluído: os links de imagens podem apontar para imagens traduzidas.
- `-img` excluído: os links de imagens podem permanecer apontados para as imagens de origem.

Execute uma tradução completa do conteúdo quando todos os links internos devem preferir saídas traduzidas:

```bash
translate -l "ko" -md -nb -img
```

Execute revisão de links após a tradução:

```bash
co-op-review -l "ko"
```

## Problemas de Renderização de Markdown

Se o Markdown traduzido for renderizado incorretamente:

- Verifique que o frontmatter começa e termina com `---`.
- Verifique que o número de cercas de código (code fences) corresponde entre os ficheiros de origem e traduzidos.
- Execute `co-op-review` para detectar problemas comuns de estrutura.
- Traduza novamente o ficheiro específico se a saída estiver corrompida.

```bash
co-op-review -l "ko" --format github
```

## Ação do GitHub executada mas nenhum Pull Request foi criado

Se `peter-evans/create-pull-request` reportar que a branch não está à frente da base, o workflow não encontrou ficheiros para fazer commit.

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

As traduções automáticas podem necessitar de revisão humana. Use `evaluate` apenas quando desejar pontuação de qualidade experimental e fluxos de trabalho de reparação de baixa confiança.

!!! warning "Experimental"
    `evaluate` pode usar verificações baseadas em regras e em LLMs, e o seu modelo de pontuação e comportamento de metadados pode mudar. Mantenha-o fora dos gates obrigatórios de CI, a menos que o seu fluxo de trabalho esteja preparado para alterações.

Para verificações determinísticas em CI, use `co-op-review` em vez disso.