# GitHub Actions

Use o GitHub Actions quando quiser que um repositório traduza automaticamente a documentação alterada e crie um pull request com os resultados gerados.

Comece com a configuração padrão `GITHUB_TOKEN`, incluindo para repositórios de organização onde a política o permita. Consulte [Configuração da App do GitHub](#github-app-setup) quando a sua organização exigir uma identidade de App ou precisar de execuções automáticas de workflows a jusante.

**Edições humanas:** estes workflows retraduzem na íntegra os ficheiros de origem alterados e podem sobrescrever a redação editada nas suas traduções. Reveja cada PR antes de o mesclar. A preservação a nível de blocos do Markdown das edições aceites requer uma integração personalizada com o [fornecedor de estado de tradução da API Python](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## O seu primeiro PR de tradução do README

Comece com um único `README.md` raiz e uma língua de destino. Este workflow traduz apenas Markdown, portanto o Azure AI Vision não é necessário.

1. Copie [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([ver o modelo no GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) para `.github/workflows/translate-readme.yml` no repositório que pretende traduzir, e comite-o na branch predefinida desse repositório. O modelo usa a Action raiz em `Azure/co-op-translator@main`, que instala o CLI a partir da mesma referência de origem. Afixe um commit revisto para execuções reproduzíveis.
2. Abra **Actions > Translate README > Run workflow**, escolha uma língua e deixe **Apenas pré-visualizar** selecionado. Reveja a estimativa de tokens na etapa de pré-visualização. A pré-visualização não chama fornecedores de modelo, não grava traduções nem cria um PR.
3. Adicione os segredos para um [fornecedor de texto](#prerequisites), e ative **Permitir que o GitHub Actions crie e aprove pull requests** em **Settings > Actions > General**. O modelo solicita `contents: write` e `pull-requests: write` para o seu job; não é necessário alterar as permissões predefinidas para cada workflow. Se a política da organização bloquear estas permissões ou esta definição, peça a um administrador informações sobre uma [Configuração da App do GitHub](#github-app-setup) aprovada.
4. Execute o workflow novamente com **Apenas pré-visualizar** desmarcado. Ele pré-visualiza, traduz, executa `co-op-review --readme-only`, e cria ou atualiza um PR de tradução apenas depois de a tradução e a revisão terem sucesso. O resumo do workflow liga ao PR.
5. Reveja a redação e as alterações de ficheiro no PR, e depois faça merge quando estiver pronto. O workflow não faz o merge automaticamente.

O PR contém apenas `translations/<language>/README.md` e o seu ficheiro de metadados de língua. O README de origem permanece inalterado, e os links para outros documentos continuam a apontar para os documentos de origem. O corpo do PR lista os ficheiros alterados e os resultados da revisão estrutural. Se a tradução ou revisão falhar, inspeccione o resumo do workflow e os logs da etapa com falha; nenhum PR é criado. Se não houver alterações, não é necessário um novo PR.

**Nota sobre Organização e CI:** Uma App do GitHub é opcional, não um requisito da propriedade da organização. Com `GITHUB_TOKEN`, os workflows de pull request para abrir, atualizar ou reabrir um PR exigem um utilizador com acesso de escrita para selecionar **Aprovar a execução de workflows**. Os workflows de push não são acionados por este token. Para CI a jusante não assistido, consulte [Configuração da App do GitHub](#github-app-setup) e as [regras de acionamento de workflows](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) do GitHub.

## Pré-requisitos

Antes de criar o workflow, configure os segredos do serviço de IA de que a sua execução de tradução necessita.

A tradução de texto requer um fornecedor de modelos de linguagem:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

A tradução de imagens requer adicionalmente o Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Consulte [Configuração](configuration.md) e [Configuração do Azure AI](azure-ai-setup.md) para detalhes de configuração local.

## Configuração padrão

Depois de experimentar o workflow do README, use esta configuração para traduzir os ficheiros Markdown de um repositório para várias línguas. Ele executa uma revisão de Markdown antes de abrir um PR e não requer o Azure AI Vision.

### Passo 1: Adicionar segredos do repositório

No repositório de destino, abra **Settings** > **Secrets and variables** > **Actions**, e adicione os segredos do fornecedor que o seu workflow irá usar.

![Selecionar segredos das Actions](../../assets/github-actions/select-setting-action.png)

### Passo 2: Ativar permissões do workflow

Abra **Settings** > **Actions** > **General**.

Em **Permissões do workflow**:

1. Ative **Permitir que o GitHub Actions crie e aprove pull requests**.
2. Guarde a definição.

O job abaixo solicita explicitamente `contents: write` e `pull-requests: write`. Mantenha as permissões predefinidas de workflow do repositório inalteradas. Se a política da organização bloquear a criação de PRs, peça a um administrador informações sobre uma [Configuração da App do GitHub](#github-app-setup) aprovada.

### Passo 3: Adicionar o workflow

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

Altere `TARGET_LANGUAGES` para as línguas de que o seu projeto precisa. A revisão usa a API Python para verificar apenas Markdown, correspondendo à etapa de tradução. Um erro de tradução ou revisão interrompe o job antes da criação do PR. O workflow não faz o merge do PR automaticamente. Para repositórios grandes, adicione um filtro `paths:` sob `on.push` para que o workflow só seja executado quando houver alterações na documentação.

### Opcional: notebooks e imagens

Para notebooks, adicione `-nb` ao comando de tradução e defina `notebook=True` na etapa de revisão. Para texto em imagens, configure os dois [segredos do Azure AI Vision](#prerequisites), passe-os no `env` da etapa de tradução, adicione `-img` ao comando e acrescente `translated_images/` aos `add-paths` da etapa de PR. Reveja as imagens traduzidas visualmente; a revisão determinística não certifica a exatidão do texto nas imagens nem a precisão linguística.

## Configuração da App do GitHub

Utilize uma App do GitHub aprovada quando a sua organização exigir uma identidade de App, ou quando o PR gerado precisar de acionar CI a jusante sem o passo de aprovação do `GITHUB_TOKEN`. Uma App não contorna a política da organização; os administradores continuam a controlar a sua instalação e permissões.

### Passo 1: Criar ou instalar uma App do GitHub

Utilize uma App fornecida pela organização quando disponível, ou crie uma com acesso de leitura/escrita a **Contents** e **Pull requests**. Instale-a no repositório de destino com qualquer aprovação de organização necessária.

Registe:

- ID da App
- Conteúdo da chave privada

Guarde-os como segredos do repositório:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Passo 2: Gerar um token da App

Adicione esta etapa imediatamente antes da etapa de pull request existente. Para o modelo README, use a mesma condição de sucesso para que pré-visualizações e traduções com falha não solicitem um token da App:

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

Depois altere apenas a entrada `token` da etapa de pull request existente para `${{ steps.generate_token.outputs.token }}`. Mantenha a sua condição de sucesso, branch, corpo do PR e `add-paths` inalterados. O token é limitado ao repositório atual por predefinição. Ao adaptar a configuração padrão em vez do modelo README, omita o `if` acima: esse workflow usa a condição de sucesso predefinida, por isso a criação do token e a criação do PR só são executadas depois de a tradução e a revisão terem sucesso.

Consulte a Action oficial [create-github-app-token](https://github.com/actions/create-github-app-token/tree/v2) para instalação e permissões do token.

## Limites dos runners

Os runners hospedados pelo GitHub têm uma duração máxima de job. Repositórios grandes ou muitas línguas de destino podem exceder esse limite.

Para cargas de tradução elevadas:

- Traduza menos línguas por execução.
- Utilize flags de conteúdo como `-md`, `-nb` ou `-img`.
- Utilize um runner auto-hospedado quando o tamanho do repositório ou a latência do modelo tornar os runners hospedados pouco fiáveis.

## Revisão no CI

Utilize `co-op-review` quando um pull request deve validar traduções geradas sem chamar fornecedores LLM ou Vision.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` é um comando de revisão determinístico em beta. As suas verificações e o esquema de saída podem evoluir, mas foi desenhado para ser seguro para CI porque não grava ficheiros nem chama fornecedores de modelo.