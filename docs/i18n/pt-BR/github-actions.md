# GitHub Actions

Use o GitHub Actions quando quiser que um repositório traduza automaticamente a documentação alterada e abra um pull request com as saídas geradas.

Comece com a configuração padrão do `GITHUB_TOKEN`, inclusive para repositórios de organização onde a política permitir. Veja [Configuração do GitHub App](#github-app-setup) quando sua organização exigir uma identidade de App ou você precisar de execuções automáticas de workflows downstream.

**Edições humanas:** esses workflows retraduzem arquivos-fonte alterados por completo e podem sobrescrever a redação editada em suas traduções. A preservação em nível de bloco do Markdown das edições aceitas requer uma integração personalizada com o [provedor de estado de tradução da API Python](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Seu primeiro PR de tradução do README

Comece com um `README.md` raiz e um idioma alvo. Este workflow traduz somente Markdown, portanto o Azure AI Vision não é necessário.

1. Copie [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([ver o modelo no GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) para `.github/workflows/translate-readme.yml` no repositório que você quer traduzir e faça commit para o branch padrão desse repositório. O modelo usa a Action raiz em `Azure/co-op-translator@main`, que instala a CLI a partir do mesmo ref de origem. Prenda um commit revisado para execuções reprodutíveis.
2. Abra **Actions > Translate README > Run workflow**, escolha um idioma e deixe **Preview only** marcado. Revise a estimativa de tokens na etapa de pré-visualização. A pré-visualização não chama provedores de modelos, não grava traduções nem cria um PR.
3. Adicione os secrets para um [provedor de texto](#prerequisites) e habilite **Permitir que o GitHub Actions crie e aprove pull requests** em **Configurações > Actions > Geral**. O modelo solicita `contents: write` e `pull-requests: write` para seu job; você não precisa alterar as permissões padrão para cada workflow. Se a política da organização bloquear essas permissões ou essa configuração, consulte um administrador sobre um [GitHub App](#github-app-setup) aprovado.
4. Execute o workflow novamente com **Preview only** desmarcado. Ele pré-visualiza, traduz, executa `co-op-review --readme-only` e cria ou atualiza um PR de tradução somente após a tradução e a revisão terem sucesso. O resumo do workflow contém um link para o PR.
5. Reveja a redação e as alterações de arquivo no PR e, quando estiver pronto, faça o merge. O workflow não faz o merge automaticamente.

O PR contém apenas `translations/<language>/README.md` e seu arquivo de metadados de idioma. O README fonte permanece inalterado, e links para outros documentos continuam apontando para os documentos-fonte. O corpo do PR lista os arquivos alterados e os resultados da revisão estrutural. Se a tradução ou a revisão falhar, inspecione o resumo do workflow e os logs da etapa com falha; nenhum PR será criado. Se não houver alterações, nenhum novo PR é necessário.

**Observação sobre organização e CI:** Um GitHub App é opcional, não um requisito de propriedade da organização. Com `GITHUB_TOKEN`, workflows de pull request para abrir, atualizar ou reabrir um PR exigem que um usuário com acesso de gravação selecione **Approve workflows to run**. Workflows de push não são acionados por esse token. Para CI downstream sem supervisão, veja [Configuração do GitHub App](#github-app-setup) e as [regras de acionamento de workflow](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) do GitHub.

## Pré-requisitos

Antes de criar o workflow, configure os secrets dos serviços de IA que sua execução de tradução precisa.

A tradução de texto requer um provedor de modelo de linguagem:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

A tradução de imagens adicionalmente requer o Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Veja [Configuração](configuration.md) e [Configuração do Azure AI](azure-ai-setup.md) para detalhes de configuração local.

## Configuração padrão

Após testar o workflow do README, use essa configuração para traduzir os arquivos Markdown de um repositório para vários idiomas. Ele executa uma revisão de Markdown antes de abrir um PR e não requer o Azure AI Vision.

### Passo 1: Adicione os secrets do repositório

No repositório alvo, abra **Settings** > **Secrets and variables** > **Actions**, então adicione os secrets do provedor que seu workflow irá usar.

![Selecionar secrets do Actions](../../assets/github-actions/select-setting-action.png)

### Passo 2: Habilitar permissões do workflow

Abra **Settings** > **Actions** > **General**.

Em **Workflow permissions**:

1. Habilite **Permitir que o GitHub Actions crie e aprove pull requests**.
2. Salve a configuração.

O job abaixo solicita explicitamente `contents: write` e `pull-requests: write`. Mantenha as permissões padrão de workflow do repositório inalteradas. Se a política da organização bloquear a criação de PRs, consulte um administrador sobre um [GitHub App](#github-app-setup) aprovado.

### Passo 3: Adicione o workflow

Crie `.github/workflows/co-op-translator.yml`:

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest
    env:
      TARGET_LANGUAGES: "es fr de"

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.11"

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ANTHROPIC_MODEL: ${{ secrets.ANTHROPIC_MODEL }}
          ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL }}
        run: |
          translate -l "$TARGET_LANGUAGES" -md -y

      - name: Review Markdown translations
        run: |
          python - <<'PY'
          import os
          from co_op_translator.api import run_review

          run_review(
              language_codes=os.environ["TARGET_LANGUAGES"].split(),
              markdown=True,
              notebook=False,
              output_format="github",
          )
          PY

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "Update translations via Co-op Translator"
          title: "Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.
            Markdown structure, freshness, and local links were reviewed.
            Review translation wording before merging.

            Generated by Co-op Translator.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
```

Altere `TARGET_LANGUAGES` para os idiomas que seu projeto precisa. A revisão usa a Python API para verificar somente Markdown, correspondendo à etapa de tradução. Um erro na tradução ou na revisão interrompe o job antes da criação do PR. O workflow não faz o merge do PR automaticamente. Para repositórios grandes, adicione um filtro `paths:` sob `on.push` para que o workflow seja executado apenas quando a documentação mudar.

### Opcional: notebooks e imagens

Para notebooks, adicione `-nb` ao comando de tradução e defina `notebook=True` na etapa de revisão. Para texto em imagens, configure os dois [secrets do Azure AI Vision](#prerequisites), passe-os no `env` da etapa de tradução, adicione `-img` ao comando e inclua `translated_images/` em `add-paths` na etapa do PR. Revise as imagens traduzidas visualmente; a revisão determinística não certifica o texto da imagem nem a acurácia linguística.

## Configuração do GitHub App

Use um GitHub App aprovado quando sua organização exigir uma identidade de App, ou quando o PR gerado precisar acionar CI downstream sem a etapa de aprovação do `GITHUB_TOKEN`. Um App não contorna a política da organização; os administradores ainda controlam sua instalação e permissões.

### Passo 1: Criar ou instalar um GitHub App

Use um App fornecido pela organização quando disponível, ou crie um com acesso de leitura/escrita a **Contents** e **Pull requests**. Instale-o no repositório alvo com qualquer aprovação de organização necessária.

Anote:

- App ID
- Conteúdo da chave privada

Armazene-os como secrets do repositório:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Passo 2: Gerar um token do App

Adicione essa etapa imediatamente antes da etapa existente de pull request. Para o template do README, use a mesma condição de sucesso para que pré-visualizações e traduções com falha não solicitem um token do App:

```yaml
      - name: Authenticate GitHub App
        id: generate_token
        if: ${{ !inputs.preview && steps.translate.outcome == 'success' && steps.review.outcome == 'success' }}
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.GH_APP_ID }}
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
          permission-contents: write
          permission-pull-requests: write
```

Então altere apenas a entrada `token` da etapa existente de pull request para `${{ steps.generate_token.outputs.token }}`. Mantenha sua condição de sucesso, branch, corpo do PR e `add-paths` inalterados. O token é limitado ao repositório atual por padrão. Ao adaptar a configuração padrão em vez do template do README, omita o `if` acima: aquele workflow usa a condição de sucesso padrão, então a criação do token e a criação do PR são executadas apenas após a tradução e a revisão terem sucesso.

Consulte a Action oficial [create-github-app-token](https://github.com/actions/create-github-app-token/tree/v2) para instalação e permissões do token.

## Limites dos runners

Runners hospedados pelo GitHub têm uma duração máxima por job. Repositórios grandes ou muitos idiomas-alvo podem exceder esse limite.

Para cargas de tradução grandes:

- Traduza menos idiomas por execução.
- Use flags de conteúdo como `-md`, `-nb` ou `-img`.
- Use um runner auto-hospedado quando o tamanho do repositório ou a latência do modelo tornar os runners hospedados instáveis.

## Revisão no CI

Use `co-op-review` quando um pull request deve validar traduções geradas sem chamar provedores de LLM ou Vision.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` é um comando de revisão determinística em beta. Suas verificações e esquema de saída podem evoluir, mas ele foi projetado para ser seguro no CI porque não grava arquivos nem chama provedores de modelos.