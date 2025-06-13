<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a52587a512e667f70d92db853d3c61d5",
  "translation_date": "2025-06-12T19:26:57+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "pt"
}
-->
# Utilizar a Ação do GitHub Co-op Translator (Configuração Pública)

**Público-alvo:** Este guia destina-se a utilizadores na maioria dos repositórios públicos ou privados onde as permissões padrão do GitHub Actions são suficientes. Utiliza o `GITHUB_TOKEN` incorporado.

Automatize a tradução da documentação do seu repositório de forma simples usando a Ação do GitHub Co-op Translator. Este guia orienta-o na configuração da ação para criar automaticamente pull requests com traduções atualizadas sempre que os seus ficheiros Markdown fonte ou imagens forem alterados.

> [!IMPORTANT]
>
> **Escolher o Guia Adequado:**
>
> Este guia detalha a **configuração mais simples usando o `GITHUB_TOKEN` padrão**. Este é o método recomendado para a maioria dos utilizadores, pois não requer a gestão de Chaves Privadas sensíveis de Aplicações GitHub.
>

## Pré-requisitos

Antes de configurar a Ação do GitHub, certifique-se de que tem as credenciais necessárias dos serviços de IA preparadas.

**1. Obrigatório: Credenciais do Modelo de Linguagem de IA**  
É necessário ter credenciais para pelo menos um Modelo de Linguagem suportado:

- **Azure OpenAI**: Requer Endpoint, Chave API, Nomes do Modelo/Deployment, Versão da API.  
- **OpenAI**: Requer Chave API, (Opcional: ID da Organização, URL Base, ID do Modelo).  
- Consulte [Modelos e Serviços Suportados](../../../../README.md) para detalhes.

**2. Opcional: Credenciais de Visão de IA (para Tradução de Imagens)**

- Apenas necessário se precisar de traduzir texto dentro de imagens.  
- **Azure AI Vision**: Requer Endpoint e Chave de Subscrição.  
- Caso não sejam fornecidas, a ação utiliza o [modo apenas Markdown](../markdown-only-mode.md) por defeito.

## Configuração e Definição

Siga estes passos para configurar a Ação do GitHub Co-op Translator no seu repositório usando o `GITHUB_TOKEN` padrão.

### Passo 1: Entender a Autenticação (Usando `GITHUB_TOKEN`)

Este workflow utiliza o `GITHUB_TOKEN` incorporado fornecido pelo GitHub Actions. Este token concede automaticamente permissões ao workflow para interagir com o seu repositório conforme as definições configuradas no **Passo 3**.

### Passo 2: Configurar Segredos do Repositório

Só precisa de adicionar as suas **credenciais dos serviços de IA** como segredos encriptados nas definições do repositório.

1.  Navegue até ao repositório GitHub alvo.  
2.  Vá a **Settings** > **Secrets and variables** > **Actions**.  
3.  Em **Repository secrets**, clique em **New repository secret** para cada segredo necessário dos serviços de IA listado abaixo.

    ![Select setting action](../../../../translated_images/select-setting-action.32e2394813d09dc148494f34daea40724f24ff406de889f26cbbbf05f98ed621.pt.png) *(Referência da imagem: Mostra onde adicionar segredos)*

**Segredos Obrigatórios dos Serviços de IA (Adicione TODOS os que se aplicam com base nos seus Pré-requisitos):**

| Nome do Segredo                    | Descrição                                  | Origem do Valor                 |
| :-------------------------------- | :----------------------------------------- | :------------------------------ |
| `AZURE_SUBSCRIPTION_KEY`            | Chave para o Serviço Azure AI (Visão Computacional) | A sua Azure AI Foundry           |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint para o Serviço Azure AI (Visão Computacional) | A sua Azure AI Foundry           |
| `AZURE_OPENAI_API_KEY`              | Chave para o serviço Azure OpenAI           | A sua Azure AI Foundry           |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint para o serviço Azure OpenAI        | A sua Azure AI Foundry           |
| `AZURE_OPENAI_MODEL_NAME`           | Nome do Modelo Azure OpenAI                  | A sua Azure AI Foundry           |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Nome do Deployment Azure OpenAI               | A sua Azure AI Foundry           |
| `AZURE_OPENAI_API_VERSION`          | Versão da API para Azure OpenAI               | A sua Azure AI Foundry           |
| `OPENAI_API_KEY`                    | Chave API para OpenAI                         | A sua Plataforma OpenAI          |
| `OPENAI_ORG_ID`                     | ID da Organização OpenAI (Opcional)           | A sua Plataforma OpenAI          |
| `OPENAI_CHAT_MODEL_ID`              | ID específico do modelo OpenAI (Opcional)       | A sua Plataforma OpenAI          |
| `OPENAI_BASE_URL`                   | URL Base API OpenAI personalizada (Opcional)   | A sua Plataforma OpenAI          |

### Passo 3: Configurar Permissões do Workflow

A Ação do GitHub precisa das permissões concedidas via `GITHUB_TOKEN` para fazer checkout do código e criar pull requests.

1.  No seu repositório, vá a **Settings** > **Actions** > **General**.  
2.  Desça até à secção **Workflow permissions**.  
3.  Selecione **Read and write permissions**. Isto concede ao `GITHUB_TOKEN` as permissões necessárias `contents: write` e `pull-requests: write` para este workflow.  
4.  Certifique-se de que a caixa **Allow GitHub Actions to create and approve pull requests** está **assinalada**.  
5.  Clique em **Save**.

![Permission setting](../../../../translated_images/permission-setting.cb1f57fdb5194f0743b1f6932f221e404ae2928ee88d77f1de39aba46fbf774a.pt.png)

### Passo 4: Criar o Ficheiro do Workflow

Por fim, crie o ficheiro YAML que define o workflow automatizado usando `GITHUB_TOKEN`.

1.  No diretório raiz do seu repositório, crie a pasta `.github/workflows/` se ainda não existir.  
2.  Dentro de `.github/workflows/`, crie um ficheiro chamado `co-op-translator.yml`.  
3.  Cole o seguinte conteúdo no `co-op-translator.yml`.

```yaml
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
          # === AI Service Credentials ===
          AZURE_SUBSCRIPTION_KEY: ${{ secrets.AZURE_SUBSCRIPTION_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
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

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
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
  - **[!IMPORTANT] Línguas-alvo:** No passo `Run Co-op Translator` step, you **MUST review and modify the list of language codes** within the `translate -l "..." -y` command to match your project's requirements. The example list (`ar de es...`) needs to be replaced or adjusted.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see commented example in the YAML) to run the workflow only when relevant files (e.g., source documentation) change, saving runner minutes.
  - **PR Details:** Customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request`, ajuste conforme necessário.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.