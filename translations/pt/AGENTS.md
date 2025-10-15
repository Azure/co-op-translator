<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:25:47+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pt"
}
-->
## Visão Geral do Projeto

O Co‑op Translator é uma ferramenta de linha de comandos em Python e um workflow do GitHub Actions que traduz ficheiros Markdown, notebooks Jupyter e texto de imagens para vários idiomas. Organiza os resultados em pastas específicas por idioma e mantém as traduções sincronizadas com o conteúdo original. O projeto está estruturado como uma biblioteca gerida por Poetry com pontos de entrada CLI.

### Visão geral da arquitetura

- Pontos de entrada CLI (`translate`, `migrate-links`, `evaluate`) invocam uma CLI unificada que encaminha para os fluxos de tradução, migração de links e avaliação.
- O carregador de configuração lê o `.env` e deteta automaticamente o fornecedor de LLM (Azure OpenAI ou OpenAI) e, se solicitado, o fornecedor de visão (Azure AI Service) para extração de texto de imagens.
- O núcleo de tradução trata Markdown e notebooks; o pipeline de visão extrai texto de imagens quando se usa `-img`.
- Os resultados são organizados em `translations/<lang>/` para texto e `translated_images/` para imagens, preservando a estrutura original.

### Tecnologias e frameworks principais

- Python 3.10–3.12, Poetry para empacotamento
- CLI: `click`
- SDKs LLM/IA: Azure OpenAI, OpenAI
- Visão: Azure AI Service (Computer Vision)
- HTTP e dados: `httpx`, `pydantic`
- Imagem: `pillow`, `opencv-python`, `matplotlib`
- Ferramentas: `pytest`, `black`, `ruff`

## Comandos de Configuração

### Pré-requisitos

- Python 3.10–3.12
- Subscrição Azure (opcional, para serviços Azure AI)
- Acesso à internet para APIs LLM/Visão (ex: Azure OpenAI/OpenAI, Azure AI Vision)

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

## Utilização pelo Utilizador Final

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
- O ponto de entrada por defeito é `translate`. Pode ser alterado para `--entrypoint migrate-links` para migração de links.
- Certifique-se de que a visibilidade do pacote GHCR está em Público para permitir pulls anónimos.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Configuração do ambiente

Crie um ficheiro `.env` na raiz do repositório e forneça credenciais/endpoints para o modelo de linguagem escolhido e (opcionalmente) para o serviço de visão. Para configuração específica do fornecedor, consulte `getting_started/set-up-azure-ai.md`.

### Variáveis de Ambiente Obrigatórias

Pelo menos um fornecedor LLM deve estar configurado. Para tradução de imagens, o Azure AI Service também deve estar configurado.

- Azure OpenAI (tradução de texto):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternativa para tradução de texto):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (opcional)
  - `OPENAI_CHAT_MODEL_ID` (obrigatório ao usar o fornecedor OpenAI)
  - `OPENAI_BASE_URL` (opcional; por defeito `https://api.openai.com/v1`)

- Azure AI Service para extração de texto de imagens (obrigatório ao usar `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (preferencial) ou antigo `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Exemplo de excerto `.env`:

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

- A ferramenta deteta automaticamente o fornecedor LLM disponível; configure Azure OpenAI ou OpenAI.
- A tradução de imagens requer ambos `AZURE_AI_SERVICE_API_KEY` e `AZURE_AI_SERVICE_ENDPOINT`.
- A CLI apresentará um erro claro se faltarem variáveis obrigatórias.

## Fluxo de Trabalho de Desenvolvimento

- O código fonte está em `src/co_op_translator`; os testes em `tests/`.
- CLIs principais (instalados via pontos de entrada):

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

Consulte documentação adicional de utilização em `getting_started/`.

## Instruções de Teste

Execute os testes a partir da raiz do repositório. Alguns testes podem requerer credenciais de API; ignore-os quando necessário.

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
- Verificações de tipo: mypy (configuração presente; ativar se instalado)

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

Organize o código Python em `src/`, testes em `tests/`, e prefira imports explícitos dentro do namespace do pacote (`co_op_translator.*`).

## Compilação e Deploy

Os artefactos de compilação são publicados em `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automação via GitHub Actions é suportada; veja:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Imagem de Contentor (GHCR)

- Imagem oficial: `ghcr.io/azure/co-op-translator:<tag>`
- Tags: `latest` (em main), tags semânticas como `vX.Y.Z`, e uma tag `sha`
- Multi-arquitetura: `linux/amd64, linux/arm64` suportado via Buildx
- Padrão Dockerfile: construa as dependências em wheels no builder (com `build-essential` e `python3-dev`) e instale do wheelhouse local no runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` constrói e publica para GHCR

## Considerações de Segurança

- Mantenha as chaves de API e endpoints no `.env` ou no store de segredos do CI; nunca faça commit de segredos.
- Para tradução de imagens, são necessárias chaves/endpoints Azure AI Vision; caso contrário, omita `-img`.
- Valide quotas/limites do fornecedor ao executar lotes grandes de tradução.

## Diretrizes para Pull Requests

### Antes de Submeter

1. **Teste as suas alterações:**
   - Execute os notebooks afetados completamente
   - Verifique que todas as células executam sem erros
   - Confirme que os resultados são adequados

2. **Atualizações de documentação:**
   - Atualize o `README.md` ao adicionar novos conceitos
   - Adicione comentários nos notebooks para código complexo
   - Certifique-se de que as células markdown explicam o propósito

3. **Alterações de ficheiros:**
   - Evite fazer commit de ficheiros `.env` (use `.env.example`)
   - Não faça commit de diretórios `venv/` ou `__pycache__/`
   - Mantenha os resultados dos notebooks quando demonstram conceitos
   - Remova ficheiros temporários e notebooks de backup (`*-backup.ipynb`)

4. **Estilo e formatação:**
   - Siga as diretrizes de estilo e formatação
   - Execute `poetry run black .` e `poetry run ruff check .` para verificar problemas de estilo e formatação

5. **Adicionar/atualizar testes e ajuda CLI:**
   - Adicione ou atualize testes ao alterar comportamentos
   - Mantenha a ajuda da CLI consistente com as alterações


### Mensagem de commit e estratégia de merge

Usamos Squash and Merge por defeito. A mensagem final do commit squash deve seguir:

```bash
<type>: <description> (#<PR number>)
```

Tipos permitidos:
- `Docs` — atualizações de documentação
- `Build` — sistema de build, dependências, configuração/CI
- `Core` — funcionalidade e características principais (ex: `src/co_op_translator/core`)

Exemplos:
- `Docs: Atualizar instruções de instalação para maior clareza (#50)`
- `Core: Melhorar tratamento de tradução de imagens (#60)`

Notas:
- Os títulos dos PR são frequentemente auto-prefixados com base nas labels; verifique se o prefixo gerado está correto.

### Formato do Título do PR

Use títulos claros e concisos. Prefira a mesma estrutura da mensagem final do squash commit:
- `Docs: Atualizar instruções de instalação para maior clareza`
- `Core: Melhorar tratamento de tradução de imagens`

## Depuração e Resolução de Problemas

- Problemas comuns e soluções: `getting_started/troubleshooting.md`
- Idiomas suportados e notas (incluindo fontes/problemas conhecidos): `getting_started/supported-languages.md`
- Para problemas de links em notebooks, execute novamente: `migrate-links -l "all" -y`

## Notas para Agentes

- Prefira Poetry para ambientes reprodutíveis; caso contrário, use `requirements.txt`.
- Ao invocar CLIs em CI, forneça os segredos necessários via variáveis de ambiente ou injeção de `.env`.
- Para consumidores em monorepo, este repositório funciona como pacote independente; não é necessária coordenação entre sub‑pacotes.

- Orientação multi-arquitetura: mantenha `linux/arm64` quando utilizadores ARM (Apple Silicon/servidores ARM) forem alvo; caso contrário, apenas `linux/amd64` é aceitável para simplicidade.
- Aponte os utilizadores para o Docker Quick Start em `README.md` se preferirem usar contentores; inclua variantes Bash e PowerShell devido às diferenças de aspas.

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original, na sua língua nativa, deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.