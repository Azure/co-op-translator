# Guia do Mantenedor

Esta página resume como a API, o CLI e o site de documentação estão conectados.

## Limite da API pública

A API Python estável é exportada de:

```python
co_op_translator.api
```

A API pública é organizada em auxiliares de tradução de conteúdo, auxiliares de reescrita de caminhos, orquestração de projetos e revisão:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
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

Ao adicionar novas APIs públicas, atualize:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- os testes relevantes da API em `tests/co_op_translator/`, como `test_api.py` ou `test_review_api.py`

Evite documentar módulos de nível inferior `core` como API estável a menos que o projeto pretenda suportá-los diretamente.

## Pontos de entrada do CLI

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

`co-op-translator-mcp` contorna `__main__.py` e chama `co_op_translator.mcp.server:main` diretamente.

Ao adicionar ou alterar opções do CLI, atualize:

- o comando relevante em `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- testes relacionados ao CLI, se o comportamento mudar

## Servidor MCP

O servidor MCP é implementado em:

```python
co_op_translator.mcp.server
```

O servidor envolve intencionalmente a API Python pública em vez de chamar módulos `core` de nível inferior. Mantenha essa fronteira intacta para que clientes MCP, chamadores Python e o CLI compartilhem o mesmo comportamento.

Ao adicionar ou alterar ferramentas MCP, atualize:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` se a superfície da API pública mudar

As ferramentas de tradução do repositório podem ser chamadas por modelos via MCP e podem escrever muitos arquivos. Mantenha `dry_run=True` como o padrão e exija `confirm_write=True` antes de realizar a tradução do projeto sem dry run.

## Fluxo de tradução

O fluxo de tradução de alto nível do projeto é:

1. Analise argumentos do CLI ou parâmetros da API.
2. Valide a configuração do LLM com `LLMConfig`.
3. Valide o Azure AI Vision quando a tradução de imagens for selecionada.
4. Normalize os códigos de idioma.
5. Detecte aliases legados de pastas de idioma.
6. Estime o volume de tradução.
7. Atualize as seções de idioma/curso do README quando aplicável.
8. Delegue a tradução do projeto para `ProjectTranslator`.
9. `ProjectTranslator` delega o processamento de arquivos para `TranslationManager`.

`TranslationManager` é composto por mixins focados por tipo de arquivo:

- `ProjectMarkdownTranslationMixin` lida com leitura de arquivos Markdown, tradução de conteúdo, reescrita de caminhos, metadados, avisos e escrita.
- `ProjectNotebookTranslationMixin` lida com leitura de arquivos de notebook, tradução de células Markdown, reescrita de caminhos, metadados, avisos e escrita.
- `ProjectImageTranslationMixin` lida com descoberta de imagens, extração/tradução de texto, gravação de imagens renderizadas e metadados.

As APIs de conteúdo de nível inferior ignoram o fluxo de trabalho do projeto:

1. `translate_markdown_content` e `translate_notebook_content` traduzem apenas conteúdo em memória.
2. `translate_image_content` traduz o texto em uma única imagem e retorna um objeto de imagem renderizada.
3. `rewrite_markdown_paths` e `rewrite_notebook_paths` são auxiliares explícitos de pós-processamento. Eles não realizam tradução nem gravação de projeto.

## Fluxo de revisão

O fluxo de revisão determinístico é:

1. Analise argumentos do CLI ou parâmetros da API.
2. Normalize os códigos de idioma solicitados.
3. Construa um ou mais alvos de revisão a partir de `root_dir`, `root_dirs` ou `groups`.
4. Opcionalmente limite arquivos de origem com `--changed-from`.
5. Execute verificações determinísticas para estrutura, atualidade da tradução, integridade do Markdown e caminhos locais de links/imagens.
6. Imprima saída em texto ou Markdown com formatação do GitHub.
7. Finalize com falha quando erros de revisão forem encontrados.

O fluxo de revisão não requer chaves de API e deve permanecer adequado para CI de pull request. O fluxo de trabalho de pull request grava um resumo de verificação a cada execução e só posta um comentário no PR quando `co-op-review` falha.

## Site de documentação

O site de documentação é configurado por:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

O diretório `docs/` é a fonte canônica de documentação. Não adicione novos guias para o usuário final fora deste diretório, a menos que o projeto introduza intencionalmente outra superfície de documentação publicada.

Build locally:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview locally:

```bash
python -m mkdocs serve
```

O site gerado é escrito em `site/`, que é ignorado pelo git.

## Fluxo de trabalho do GitHub Pages

`.github/workflows/docs.yml` constrói o site em pull requests e o implanta em pushes para `main`.

O workflow instala:

```bash
pip install -r requirements-docs.txt
```

O workflow de docs instala apenas a cadeia de ferramentas de documentação. `mkdocs.yml` aponta o `mkdocstrings` para `src/` para que páginas de API pública possam ser renderizadas a partir da árvore de origem sem instalar o conjunto completo de dependências de tempo de execução. Se futuras documentações de API exigirem importar provedores de tempo de execução opcionais durante a compilação, atualize tanto `.github/workflows/docs.yml` quanto este guia em conjunto.

## Padrão de qualidade da documentação

Antes de mesclar alterações na documentação, execute:

```bash
python -m mkdocs build --strict
git diff --check
```

Use builds estritos para que links quebrados, entradas de navegação inválidas e problemas de renderização de API falhem cedo.