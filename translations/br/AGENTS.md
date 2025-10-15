<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:26:08+00:00",
  "source_file": "AGENTS.md",
  "language_code": "br"
}
-->
## Visão Geral do Projeto

O Co‑op Translator é uma ferramenta de linha de comando em Python e um workflow do GitHub Actions que traduz arquivos Markdown, notebooks Jupyter e texto de imagens para vários idiomas. Ele organiza as saídas em pastas específicas por idioma e mantém as traduções sincronizadas com o conteúdo original. O projeto é estruturado como uma biblioteca gerenciada pelo Poetry com pontos de entrada CLI.

### Visão geral da arquitetura

- Pontos de entrada CLI (`translate`, `migrate-links`, `evaluate`) chamam uma CLI unificada que direciona para os fluxos de tradução, migração de links e avaliação.
- O carregador de configuração lê o `.env` e detecta automaticamente o provedor de LLM (Azure OpenAI ou OpenAI) e, se solicitado, o provedor de visão (Azure AI Service) para extração de texto de imagens.
- O núcleo de tradução lida com Markdown e notebooks; o pipeline de visão extrai texto de imagens quando o parâmetro `-img` é usado.
- As saídas são organizadas em `translations/<lang>/` para texto e `translated_images/` para imagens, preservando a estrutura original.

### Principais tecnologias e frameworks

- Python 3.10–3.12, Poetry para empacotamento
- CLI: `click`
- SDKs de LLM/IA: Azure OpenAI, OpenAI
- Visão: Azure AI Service (Computer Vision)
- HTTP e dados: `httpx`, `pydantic`
- Imagens: `pillow`, `opencv-python`, `matplotlib`
- Ferramentas: `pytest`, `black`, `ruff`

## Comandos de Configuração

### Pré-requisitos

- Python 3.10–3.12
- Assinatura Azure (opcional, para serviços Azure AI)
- Acesso à internet para APIs de LLM/Visão (ex.: Azure OpenAI/OpenAI, Azure AI Vision)

### Opção A: Poetry (recomendado)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Opção B: pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## Uso pelo Usuário Final

### Docker (imagem publicada)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Notas:
- O ponto de entrada padrão é `translate`. Use `--entrypoint migrate-links` para migração de links.
- Certifique-se de que o pacote GHCR esteja Público para permitir pulls anônimos.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Configuração de ambiente

Crie um arquivo `.env` na raiz do repositório e forneça credenciais/endpoints para o modelo de linguagem escolhido e (opcionalmente) para o serviço de visão. Para configuração específica de cada provedor, veja `getting_started/set-up-azure-ai.md`.

### Variáveis de Ambiente Obrigatórias

Pelo menos um provedor de LLM deve ser configurado. Para tradução de imagens, o Azure AI Service também deve ser configurado.

- Azure OpenAI (tradução de texto):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternativa para tradução de texto):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (opcional)
  - `OPENAI_CHAT_MODEL_ID` (obrigatório ao usar OpenAI)
  - `OPENAI_BASE_URL` (opcional; padrão é `https://api.openai.com/v1`)

- Azure AI Service para extração de texto de imagens (obrigatório ao usar `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (preferencial) ou legado `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Exemplo de trecho `.env`:

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

Notas:

- A ferramenta detecta automaticamente o provedor de LLM disponível; configure Azure OpenAI ou OpenAI.
- Tradução de imagens exige tanto `AZURE_AI_SERVICE_API_KEY` quanto `AZURE_AI_SERVICE_ENDPOINT`.
- A CLI mostrará um erro claro se variáveis obrigatórias estiverem faltando.

## Fluxo de Trabalho de Desenvolvimento

- O código-fonte está em `src/co_op_translator`; testes em `tests/`.
- CLIs principais (instalados via entry points):

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

Veja mais documentação de uso em `getting_started/`.

## Instruções de Teste

Execute os testes a partir da raiz do repositório. Alguns testes podem exigir credenciais de API; pule-os quando necessário.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Cobertura opcional (requer `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Diretrizes de Estilo de Código

- Formatador: Black (configurado em `pyproject.toml`, comprimento de linha 88)
- Linter: Ruff (configurado em `pyproject.toml`, comprimento de linha 120)
- Checagem de tipos: mypy (configuração presente; habilite se instalado)

Comandos:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Organize os fontes Python em `src/`, testes em `tests/`, e prefira imports explícitos dentro do namespace do pacote (`co_op_translator.*`).

## Build e Deploy

Os artefatos de build são publicados em `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automação via GitHub Actions é suportada; veja:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Imagem de Container (GHCR)

- Imagem oficial: `ghcr.io/azure/co-op-translator:<tag>`
- Tags: `latest` (na main), tags semânticas como `vX.Y.Z`, e uma tag `sha`
- Multi-arquitetura: `linux/amd64, linux/arm64` suportados via Buildx
- Padrão do Dockerfile: construa as dependências em wheels no builder (com `build-essential` e `python3-dev`) e instale do wheelhouse local no runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` constrói e publica no GHCR

## Considerações de Segurança

- Mantenha chaves de API e endpoints no `.env` ou no store de segredos do CI; nunca faça commit de segredos.
- Para tradução de imagens, são necessários chaves/endpoints do Azure AI Vision; caso contrário, omita `-img`.
- Valide cotas/limites do provedor ao executar lotes grandes de tradução.

## Diretrizes para Pull Request

### Antes de Submeter

1. **Teste suas alterações:**
   - Execute os notebooks afetados completamente
   - Verifique se todas as células executam sem erros
   - Confira se as saídas estão corretas

2. **Atualizações de documentação:**
   - Atualize o `README.md` ao adicionar novos conceitos
   - Adicione comentários em notebooks para códigos complexos
   - Certifique-se de que células markdown expliquem o propósito

3. **Alterações de arquivos:**
   - Evite commitar arquivos `.env` (use `.env.example`)
   - Não faça commit de diretórios `venv/` ou `__pycache__/`
   - Mantenha saídas de notebooks quando demonstrarem conceitos
   - Remova arquivos temporários e notebooks de backup (`*-backup.ipynb`)

4. **Estilo e formatação:**
   - Siga as diretrizes de estilo e formatação
   - Execute `poetry run black .` e `poetry run ruff check .` para verificar estilo e formatação

5. **Adicione/atualize testes e ajuda da CLI:**
   - Adicione ou atualize testes ao alterar comportamentos
   - Mantenha a ajuda da CLI consistente com as mudanças


### Mensagem de commit e estratégia de merge

Usamos Squash and Merge como padrão. A mensagem final do squash commit deve seguir:

```bash
<type>: <description> (#<PR number>)
```

Tipos permitidos:
- `Docs` — atualizações de documentação
- `Build` — sistema de build, dependências, configuração/CI
- `Core` — funcionalidades e recursos principais (ex.: `src/co_op_translator/core`)

Exemplos:
- `Docs: Atualizar instruções de instalação para maior clareza (#50)`
- `Core: Melhorar tratamento de tradução de imagens (#60)`

Notas:
- Títulos de PR geralmente são auto-prefixados conforme os labels; verifique se o prefixo gerado está correto.

### Formato do Título do PR

Use títulos claros e concisos. Prefira a mesma estrutura da mensagem final do squash commit:
- `Docs: Atualizar instruções de instalação para maior clareza`
- `Core: Melhorar tratamento de tradução de imagens`

## Depuração e Solução de Problemas

- Problemas comuns e soluções: `getting_started/troubleshooting.md`
- Idiomas suportados e observações (incluindo fontes/problemas conhecidos): `getting_started/supported-languages.md`
- Para problemas de links em notebooks, execute novamente: `migrate-links -l "all" -y`

## Notas para Agentes

- Prefira Poetry para ambientes reprodutíveis; caso contrário, use `requirements.txt`.
- Ao executar CLIs no CI, forneça os segredos necessários via variáveis de ambiente ou injeção de `.env`.
- Para consumidores de monorepo, este repositório funciona como pacote independente; não é necessário coordenação de subpacotes.

- Orientação multi-arquitetura: mantenha `linux/arm64` quando usuários ARM (Apple Silicon/servidores ARM) forem alvo; caso contrário, apenas `linux/amd64` é aceitável para simplificar.
- Indique aos usuários o Docker Quick Start em `README.md` quando preferirem uso via container; inclua variantes Bash e PowerShell devido às diferenças de aspas.

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora busquemos precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.