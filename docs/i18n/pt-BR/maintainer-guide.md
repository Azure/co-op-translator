# Guia do Mantenedor

Esta página resume como a API, a CLI e o site de documentação estão conectados.

## Limite da API Pública

A API Python estável é exportada de:

```python
co_op_translator.api
```

A API pública está organizada em ajudantes de tradução de conteúdo, ajudantes de reescrita de caminhos, orquestração de projetos e revisão:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

`TranslationStateProvider` é a fronteira de persistência para integrações hospedadas.
Deve manter candidatos gerados separados das linhas de base aceitas para que uma
tradução não mesclada não se torne a fonte da verdade.

Ao adicionar novas APIs públicas, atualize:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- testes de API relevantes em `tests/co_op_translator/`, como `test_api.py` ou `test_review_api.py`

Evite documentar módulos `core` de baixo nível como API estável, a menos que o projeto pretenda suportá-los diretamente.

## Pontos de entrada da CLI

O pacote define estes scripts do Poetry:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` encaminha por nome do script:

- `translate` chama `co_op_translator.cli.translate.translate_command`
- `evaluate` chama `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` chama `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` chama `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` ignora `__main__.py` e chama `co_op_translator.mcp.server:main` diretamente.

Ao adicionar ou alterar opções da CLI, atualize:

- o comando relevante em `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- testes relacionados à CLI, se o comportamento mudar

## MCP server

O servidor MCP é implementado em:

```python
co_op_translator.mcp.server
```

O servidor envolve intencionalmente a API pública Python em vez de chamar módulos `core` de nível inferior. Mantenha essa fronteira intacta para que clientes MCP, chamadores Python e a CLI compartilhem o mesmo comportamento.

Ao adicionar ou alterar ferramentas MCP, atualize:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` se a superfície da API pública mudar

As ferramentas de tradução do repositório são chamáveis por modelo através do MCP e podem gravar muitos arquivos. Mantenha `dry_run=True` como padrão e exija `confirm_write=True` antes da tradução do projeto em modo não dry-run.

## Fluxo de tradução

O fluxo de tradução de projeto em alto nível é:

1. Analise argumentos da CLI ou parâmetros da API.
2. Valide a configuração do LLM com `LLMConfig`.
3. Valide o Azure AI Vision quando a tradução de imagens for selecionada.
4. Normalize códigos de idioma.
5. Detecte aliases legados de pastas de idioma.
6. Estime o volume de tradução.
7. Atualize seções de idioma/curso do README quando aplicável.
8. Delegue a tradução do projeto para `ProjectTranslator`.
9. `ProjectTranslator` delega o processamento de arquivos para `TranslationManager`.

`TranslationManager` é composto por mixins focados por tipo de arquivo:

- `ProjectMarkdownTranslationMixin` lida com leituras de arquivos Markdown, tradução de conteúdo, reescrita de caminhos, metadados, avisos e gravações.
- `ProjectNotebookTranslationMixin` lida com leituras de arquivos de notebook, tradução de células Markdown, reescrita de caminhos, metadados, avisos e gravações.
- `ProjectImageTranslationMixin` lida com descoberta de imagens, extração/tradução de texto, gravação de imagens renderizadas e metadados.

As APIs de conteúdo de nível inferior ignoram o fluxo de trabalho do projeto:

1. `translate_markdown_content` e `translate_notebook_content` traduzem apenas conteúdo em memória.
2. `translate_image_content` traduz o texto em uma única imagem e retorna um objeto de imagem renderizada.
3. `rewrite_markdown_paths` e `rewrite_notebook_paths` são auxiliares de pós-processamento explícitos. Eles não realizam tradução nem gravações no projeto.

## Fluxo de revisão

O fluxo de revisão determinístico é:

1. Analise argumentos da CLI ou parâmetros da API.
2. Normalize os códigos de idioma solicitados.
3. Construa um ou mais alvos de revisão a partir de `root_dir`, `root_dirs` ou `groups`.
4. Opcionalmente limite arquivos de origem com `--changed-from`.
5. Execute verificações determinísticas para estrutura, atualidade da tradução, integridade do Markdown e caminhos de links/imagens locais.
6. Imprima a saída em texto ou Markdown no estilo GitHub.
7. Saia com falha quando erros de revisão forem encontrados.

O fluxo de revisão não requer chaves de API e permanece disponível para verificações locais ou CI opcional do consumidor. Este repositório não executa `co-op-review` automaticamente em cada pull request.

## Site de documentação

O site de documentação é configurado por:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

O diretório `docs/` é a fonte canônica da documentação. Não adicione novos guias para usuários finais fora deste diretório, a menos que o projeto introduza intencionalmente outra superfície de documentação publicada.

Construa localmente:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Pré-visualizar localmente:

```bash
python -m mkdocs serve
```

O site gerado é gravado em `site/`, que é ignorado pelo git.

## Fluxo de trabalho do GitHub Pages

`.github/workflows/docs.yml` constrói o site em pull requests e o implanta em pushes para `main`.

O fluxo de trabalho instala:

```bash
pip install -r requirements-docs.txt
```

O fluxo de trabalho de documentação instala apenas a cadeia de ferramentas de documentação. `mkdocs.yml` aponta `mkdocstrings` para `src/` para que as páginas da API pública possam ser renderizadas a partir da árvore de código-fonte sem instalar o conjunto completo de dependências em tempo de execução. Se futuras documentações da API exigirem importar provedores de tempo de execução opcionais durante a compilação, atualize tanto `.github/workflows/docs.yml` quanto este guia.

## Barra de qualidade da documentação

Antes de mesclar alterações na documentação, execute:

```bash
python -m mkdocs build --strict
git diff --check
```

Use compilações estritas para que links quebrados, entradas de navegação inválidas e problemas de renderização da API sejam detectados cedo.