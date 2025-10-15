<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9fac847815936ef6e6c8bfde6d191571",
  "translation_date": "2025-10-15T03:03:32+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-org.md",
  "language_code": "br"
}
-->
# Usando a GitHub Action Co-op Translator (Guia para Organizações)

**Público-alvo:** Este guia é destinado a **usuários internos da Microsoft** ou **equipes que têm acesso às credenciais necessárias para o Co-op Translator GitHub App pré-configurado** ou que podem criar seu próprio GitHub App personalizado.

Automatize a tradução da documentação do seu repositório facilmente usando a GitHub Action Co-op Translator. Este guia mostra como configurar a action para criar pull requests automaticamente com traduções atualizadas sempre que seus arquivos Markdown de origem ou imagens forem alterados.

> [!IMPORTANT]
>
> **Escolhendo o Guia Certo:**
>
> Este guia detalha a configuração usando um **GitHub App ID e uma Chave Privada**. Normalmente, você precisa deste método "Guia para Organizações" se: **`GITHUB_TOKEN` com Permissões Restritas:** As configurações da sua organização ou repositório restringem as permissões padrão concedidas ao `GITHUB_TOKEN`. Especificamente, se o `GITHUB_TOKEN` não tiver as permissões de `write` necessárias (como `contents: write` ou `pull-requests: write`), o fluxo de trabalho do [Guia Público](./github-actions-guide-public.md) falhará por falta de permissões. Usar um GitHub App dedicado com permissões explicitamente concedidas contorna essa limitação.
>
> **Se isso não se aplica a você:**
>
> Se o `GITHUB_TOKEN` padrão tem permissões suficientes no seu repositório (ou seja, você não está bloqueado por restrições organizacionais), utilize o **[Guia Público usando GITHUB_TOKEN](./github-actions-guide-public.md)**. O guia público não exige obtenção ou gerenciamento de App IDs ou Chaves Privadas e depende apenas do `GITHUB_TOKEN` padrão e das permissões do repositório.

## Pré-requisitos

Antes de configurar a GitHub Action, garanta que você já possui as credenciais do serviço de IA necessárias.

**1. Obrigatório: Credenciais do Modelo de Linguagem de IA**
Você precisa das credenciais de pelo menos um dos Modelos de Linguagem suportados:

- **Azure OpenAI**: Requer Endpoint, Chave de API, Nome do Modelo/Deployment, Versão da API.
- **OpenAI**: Requer Chave de API, (Opcional: Org ID, Base URL, Model ID).
- Veja [Modelos e Serviços Suportados](../../../../README.md) para detalhes.
- Guia de Configuração: [Configurar Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. Opcional: Credenciais de Visão Computacional (para Tradução de Imagens)**

- Necessário apenas se você precisar traduzir textos dentro de imagens.
- **Azure Computer Vision**: Requer Endpoint e Subscription Key.
- Se não for fornecido, a action funcionará no [modo apenas Markdown](../markdown-only-mode.md).
- Guia de Configuração: [Configurar Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## Configuração

Siga estes passos para configurar a GitHub Action Co-op Translator no seu repositório:

### Passo 1: Instale e Configure a Autenticação do GitHub App

O fluxo de trabalho usa autenticação via GitHub App para interagir com seu repositório de forma segura (ex: criar pull requests) em seu nome. Escolha uma opção:

#### **Opção A: Instale o Co-op Translator GitHub App Pré-configurado (para uso interno Microsoft)**

1. Acesse a página do [Co-op Translator GitHub App](https://github.com/apps/co-op-translator).

1. Selecione **Install** e escolha a conta ou organização onde está o repositório desejado.

    ![Instalar app](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.br.png)

1. Escolha **Only select repositories** e selecione seu repositório alvo (ex: `PhiCookBook`). Clique em **Install**. Pode ser necessário autenticar.

    ![Instalar autorizar](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.br.png)

1. **Obtenha as Credenciais do App (Processo Interno Necessário):** Para permitir que o fluxo de trabalho autentique como o app, você precisa de duas informações fornecidas pela equipe do Co-op Translator:
  - **App ID:** O identificador único do app Co-op Translator. O App ID é: `1164076`.
  - **Chave Privada:** Você deve obter o **conteúdo completo** do arquivo `.pem` da chave privada com o contato responsável. **Trate essa chave como uma senha e mantenha-a segura.**

1. Prossiga para o Passo 2.

#### **Opção B: Use seu Próprio GitHub App Personalizado**

- Se preferir, você pode criar e configurar seu próprio GitHub App. Certifique-se de que ele tenha acesso de leitura e escrita a Contents e Pull requests. Você precisará do App ID e de uma Chave Privada gerada.

### Passo 2: Configure os Segredos do Repositório

Você precisa adicionar as credenciais do GitHub App e as credenciais do serviço de IA como segredos criptografados nas configurações do seu repositório.

1. Acesse seu repositório no GitHub (ex: `PhiCookBook`).

1. Vá em **Settings** > **Secrets and variables** > **Actions**.

1. Em **Repository secrets**, clique em **New repository secret** para cada segredo listado abaixo.

   ![Selecionar configuração action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.br.png)

**Segredos Obrigatórios (para Autenticação do GitHub App):**

| Nome do Segredo      | Descrição                                         | Fonte do Valor                                   |
| :------------------- | :------------------------------------------------ | :----------------------------------------------- |
| `GH_APP_ID`          | O App ID do GitHub App (do Passo 1).              | Configurações do GitHub App                      |
| `GH_APP_PRIVATE_KEY` | **Conteúdo completo** do arquivo `.pem` baixado.  | Arquivo `.pem` (do Passo 1)                      |

**Segredos do Serviço de IA (Adicione TODOS que se aplicam conforme seus Pré-requisitos):**

| Nome do Segredo                      | Descrição                                   | Fonte do Valor                  |
| :----------------------------------- | :------------------------------------------ | :------------------------------ |
| `AZURE_AI_SERVICE_API_KEY`           | Chave do Azure AI Service (Computer Vision) | Azure AI Foundry                |
| `AZURE_AI_SERVICE_ENDPOINT`          | Endpoint do Azure AI Service (Computer Vision) | Azure AI Foundry             |
| `AZURE_OPENAI_API_KEY`               | Chave do serviço Azure OpenAI               | Azure AI Foundry                |
| `AZURE_OPENAI_ENDPOINT`              | Endpoint do serviço Azure OpenAI            | Azure AI Foundry                |
| `AZURE_OPENAI_MODEL_NAME`            | Nome do seu Modelo Azure OpenAI             | Azure AI Foundry                |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`  | Nome do Deployment Azure OpenAI             | Azure AI Foundry                |
| `AZURE_OPENAI_API_VERSION`           | Versão da API do Azure OpenAI               | Azure AI Foundry                |
| `OPENAI_API_KEY`                     | Chave de API do OpenAI                      | Plataforma OpenAI               |
| `OPENAI_ORG_ID`                      | ID da Organização OpenAI                    | Plataforma OpenAI               |
| `OPENAI_CHAT_MODEL_ID`               | ID do modelo específico do OpenAI           | Plataforma OpenAI               |
| `OPENAI_BASE_URL`                    | Base URL personalizada da API do OpenAI      | Plataforma OpenAI               |

![Digite o nome da variável de ambiente](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.br.png)

### Passo 3: Crie o Arquivo de Workflow

Por fim, crie o arquivo YAML que define o fluxo de trabalho automatizado.

1. No diretório raiz do seu repositório, crie o diretório `.github/workflows/` se ele ainda não existir.

1. Dentro de `.github/workflows/`, crie um arquivo chamado `co-op-translator.yml`.

1. Cole o seguinte conteúdo em co-op-translator.yml.

```
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # Azure AI Service Credentials
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}

          # Azure OpenAI Credentials
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}

          # OpenAI Credentials
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Authenticate GitHub App
        id: generate_token
        uses: tibdex/github-app-token@v1
        with:
          app_id: ${{ secrets.GH_APP_ID }}
          private_key: ${{ secrets.GH_APP_PRIVATE_KEY }}

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ steps.generate_token.outputs.token }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/

```

4.  **Personalize o Workflow:**
  - **[!IMPORTANT] Idiomas de Destino:** No passo `Run Co-op Translator`, você **DEVE revisar e modificar a lista de códigos de idiomas** dentro do comando `translate -l "..." -y` para corresponder às necessidades do seu projeto. A lista de exemplo (`ar de es...`) precisa ser substituída ou ajustada.
  - **Trigger (`on:`):** O gatilho atual executa em todo push para `main`. Para repositórios grandes, considere adicionar um filtro `paths:` (veja o exemplo comentado no YAML) para rodar o workflow apenas quando arquivos relevantes (ex: documentação fonte) forem alterados, economizando minutos do runner.
  - **Detalhes do PR:** Personalize o `commit-message`, `title`, `body`, nome do `branch` e `labels` no passo `Create Pull Request` se necessário.

## Gerenciamento e Renovação de Credenciais

- **Segurança:** Sempre armazene credenciais sensíveis (chaves de API, chaves privadas) como segredos do GitHub Actions. Nunca exponha essas informações no arquivo do workflow ou no código do repositório.
- **[!IMPORTANT] Renovação de Chaves (Usuários Internos Microsoft):** Fique atento, pois a chave do Azure OpenAI usada internamente na Microsoft pode ter uma política obrigatória de renovação (ex: a cada 5 meses). Certifique-se de atualizar os segredos correspondentes do GitHub (`AZURE_OPENAI_...`) **antes de expirarem** para evitar falhas no workflow.

## Executando o Workflow

> [!WARNING]  
> **Limite de Tempo do Runner Hospedado pelo GitHub:**  
> Runners hospedados pelo GitHub como `ubuntu-latest` têm um **tempo máximo de execução de 6 horas**.  
> Para repositórios de documentação grandes, se o processo de tradução ultrapassar 6 horas, o workflow será encerrado automaticamente.  
> Para evitar isso, considere:  
> - Usar um **runner auto-hospedado** (sem limite de tempo)  
> - Reduzir o número de idiomas de destino por execução

Assim que o arquivo `co-op-translator.yml` for mesclado ao seu branch principal (ou ao branch especificado no trigger `on:`), o workflow será executado automaticamente sempre que houver alterações nesse branch (e corresponder ao filtro `paths`, se configurado).

Se traduções forem geradas ou atualizadas, a action criará automaticamente um Pull Request com as alterações, pronto para sua revisão e merge.

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.