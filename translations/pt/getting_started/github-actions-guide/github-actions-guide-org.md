<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9fac847815936ef6e6c8bfde6d191571",
  "translation_date": "2025-10-15T03:01:08+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-org.md",
  "language_code": "pt"
}
-->
# Utilizar a GitHub Action Co-op Translator (Guia para Organizações)

**Público-alvo:** Este guia destina-se a **utilizadores internos da Microsoft** ou **equipas que tenham acesso às credenciais necessárias para a App GitHub Co-op Translator pré-configurada** ou que possam criar a sua própria App GitHub personalizada.

Automatize a tradução da documentação do seu repositório de forma simples utilizando a GitHub Action Co-op Translator. Este guia explica como configurar a action para criar automaticamente pull requests com traduções atualizadas sempre que os seus ficheiros Markdown de origem ou imagens forem alterados.

> [!IMPORTANT]
>
> **Escolher o Guia Certo:**
>
> Este guia detalha a configuração utilizando um **GitHub App ID e uma Chave Privada**. Normalmente, precisa deste método "Guia para Organizações" se: **`GITHUB_TOKEN` com Permissões Restritas:** As definições da sua organização ou repositório restringem as permissões padrão concedidas ao `GITHUB_TOKEN`. Especificamente, se o `GITHUB_TOKEN` não tiver as permissões de `write` necessárias (como `contents: write` ou `pull-requests: write`), o workflow do [Guia de Configuração Pública](./github-actions-guide-public.md) irá falhar devido a permissões insuficientes. Utilizar uma App GitHub dedicada com permissões explicitamente atribuídas contorna esta limitação.
>
> **Se o acima não se aplicar a si:**
>
> Se o `GITHUB_TOKEN` padrão tiver permissões suficientes no seu repositório (ou seja, não está bloqueado por restrições organizacionais), utilize o **[Guia de Configuração Pública com GITHUB_TOKEN](./github-actions-guide-public.md)**. O guia público não requer obtenção ou gestão de App IDs ou Chaves Privadas e baseia-se apenas no `GITHUB_TOKEN` padrão e nas permissões do repositório.

## Pré-requisitos

Antes de configurar a GitHub Action, certifique-se de que tem as credenciais do serviço de IA necessárias.

**1. Obrigatório: Credenciais do Modelo de Linguagem de IA**
Precisa de credenciais para pelo menos um dos Modelos de Linguagem suportados:

- **Azure OpenAI**: Requer Endpoint, Chave API, Nomes de Modelo/Deployment, Versão da API.
- **OpenAI**: Requer Chave API, (Opcional: Org ID, Base URL, Model ID).
- Consulte [Modelos e Serviços Suportados](../../../../README.md) para mais detalhes.
- Guia de Configuração: [Configurar Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. Opcional: Credenciais de Visão Computacional (para Tradução de Imagens)**

- Só é necessário se precisar de traduzir texto dentro de imagens.
- **Azure Computer Vision**: Requer Endpoint e Subscription Key.
- Se não fornecer, a action funciona em [modo apenas Markdown](../markdown-only-mode.md).
- Guia de Configuração: [Configurar Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## Configuração

Siga estes passos para configurar a GitHub Action Co-op Translator no seu repositório:

### Passo 1: Instalar e Configurar a Autenticação da GitHub App

O workflow utiliza autenticação via GitHub App para interagir de forma segura com o seu repositório (por exemplo, criar pull requests) em seu nome. Escolha uma das opções:

#### **Opção A: Instalar a App GitHub Co-op Translator Pré-configurada (para Utilizadores Internos da Microsoft)**

1. Aceda à página da [App GitHub Co-op Translator](https://github.com/apps/co-op-translator).

1. Selecione **Install** e escolha a conta ou organização onde está o seu repositório de destino.

    ![Instalar app](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.pt.png)

1. Escolha **Only select repositories** e selecione o seu repositório de destino (por exemplo, `PhiCookBook`). Clique em **Install**. Poderá ser-lhe pedido para autenticar.

    ![Instalar autorizar](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.pt.png)

1. **Obter Credenciais da App (Processo Interno Necessário):** Para permitir que o workflow autentique como a app, precisa de dois elementos fornecidos pela equipa Co-op Translator:
  - **App ID:** O identificador único da app Co-op Translator. O App ID é: `1164076`.
  - **Chave Privada:** Deve obter o **conteúdo completo** do ficheiro de chave privada `.pem` junto do contacto responsável. **Trate esta chave como uma palavra-passe e mantenha-a segura.**

1. Prossiga para o Passo 2.

#### **Opção B: Utilizar a Sua Própria App GitHub Personalizada**

- Se preferir, pode criar e configurar a sua própria App GitHub. Certifique-se de que tem acesso de Leitura & Escrita a Contents e Pull requests. Vai precisar do App ID e de uma Chave Privada gerada.

### Passo 2: Configurar Segredos do Repositório

Deve adicionar as credenciais da GitHub App e as credenciais do serviço de IA como segredos encriptados nas definições do seu repositório.

1. Aceda ao seu repositório GitHub de destino (por exemplo, `PhiCookBook`).

1. Vá a **Settings** > **Secrets and variables** > **Actions**.

1. Em **Repository secrets**, clique em **New repository secret** para cada segredo listado abaixo.

   ![Selecionar definições action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.pt.png)

**Segredos Obrigatórios (para Autenticação da GitHub App):**

| Nome do Segredo      | Descrição                                         | Fonte do Valor                                   |
| :------------------- | :------------------------------------------------ | :----------------------------------------------- |
| `GH_APP_ID`          | O App ID da GitHub App (do Passo 1).              | Definições da GitHub App                         |
| `GH_APP_PRIVATE_KEY` | O **conteúdo completo** do ficheiro `.pem` obtido. | Ficheiro `.pem` (do Passo 1)                     |

**Segredos do Serviço de IA (Adicione TODOS os que se aplicam consoante os seus Pré-requisitos):**

| Nome do Segredo                      | Descrição                                   | Fonte do Valor                  |
| :----------------------------------- | :------------------------------------------ | :------------------------------ |
| `AZURE_AI_SERVICE_API_KEY`           | Chave para Azure AI Service (Computer Vision) | Azure AI Foundry                |
| `AZURE_AI_SERVICE_ENDPOINT`          | Endpoint para Azure AI Service (Computer Vision) | Azure AI Foundry            |
| `AZURE_OPENAI_API_KEY`               | Chave para o serviço Azure OpenAI           | Azure AI Foundry                |
| `AZURE_OPENAI_ENDPOINT`              | Endpoint para o serviço Azure OpenAI        | Azure AI Foundry                |
| `AZURE_OPENAI_MODEL_NAME`            | Nome do seu Modelo Azure OpenAI             | Azure AI Foundry                |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`  | Nome do Deployment Azure OpenAI             | Azure AI Foundry                |
| `AZURE_OPENAI_API_VERSION`           | Versão da API para Azure OpenAI             | Azure AI Foundry                |
| `OPENAI_API_KEY`                     | Chave API para OpenAI                       | OpenAI Platform                 |
| `OPENAI_ORG_ID`                      | ID da Organização OpenAI                    | OpenAI Platform                 |
| `OPENAI_CHAT_MODEL_ID`               | ID específico do modelo OpenAI              | OpenAI Platform                 |
| `OPENAI_BASE_URL`                    | Base URL personalizada da API OpenAI        | OpenAI Platform                 |

![Introduzir nome da variável de ambiente](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.pt.png)

### Passo 3: Criar o Ficheiro de Workflow

Por fim, crie o ficheiro YAML que define o workflow automatizado.

1. No diretório raiz do seu repositório, crie o diretório `.github/workflows/` se ainda não existir.

1. Dentro de `.github/workflows/`, crie um ficheiro chamado `co-op-translator.yml`.

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

4.  **Personalizar o Workflow:**
  - **[!IMPORTANT] Línguas de Destino:** No passo `Run Co-op Translator`, **DEVE rever e modificar a lista de códigos de línguas** no comando `translate -l "..." -y` para corresponder aos requisitos do seu projeto. A lista de exemplo (`ar de es...`) deve ser substituída ou ajustada.
  - **Trigger (`on:`):** O trigger atual executa em cada push para `main`. Para repositórios grandes, considere adicionar um filtro `paths:` (veja o exemplo comentado no YAML) para executar o workflow apenas quando ficheiros relevantes (por exemplo, documentação de origem) forem alterados, poupando minutos de execução.
  - **Detalhes do PR:** Personalize a `commit-message`, `title`, `body`, nome da `branch` e `labels` no passo `Create Pull Request` se necessário.

## Gestão e Renovação de Credenciais

- **Segurança:** Guarde sempre credenciais sensíveis (chaves API, chaves privadas) como segredos do GitHub Actions. Nunca as exponha no ficheiro do workflow ou no código do repositório.
- **[!IMPORTANT] Renovação de Chaves (Utilizadores Internos Microsoft):** Tenha em atenção que a chave Azure OpenAI utilizada internamente na Microsoft pode ter uma política obrigatória de renovação (por exemplo, a cada 5 meses). Certifique-se de atualizar os segredos GitHub correspondentes (`AZURE_OPENAI_...`) **antes de expirarem** para evitar falhas no workflow.

## Execução do Workflow

> [!WARNING]  
> **Limite de Tempo dos Runners Hospedados pelo GitHub:**  
> Os runners hospedados pelo GitHub, como `ubuntu-latest`, têm um **limite máximo de execução de 6 horas**.  
> Para repositórios de documentação grandes, se o processo de tradução exceder as 6 horas, o workflow será automaticamente terminado.  
> Para evitar isto, considere:  
> - Utilizar um **runner self-hosted** (sem limite de tempo)  
> - Reduzir o número de línguas de destino por execução

Assim que o ficheiro `co-op-translator.yml` for integrado na sua branch principal (ou na branch especificada no trigger `on:`), o workflow será executado automaticamente sempre que forem feitas alterações nessa branch (e corresponder ao filtro `paths`, se configurado).

Se forem geradas ou atualizadas traduções, a action irá criar automaticamente um Pull Request com as alterações, pronto para revisão e integração.

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original, no seu idioma nativo, deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.