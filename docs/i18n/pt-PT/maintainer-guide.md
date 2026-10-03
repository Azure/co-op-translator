# Guia do Mantenedor

Esta página resume como a API, a CLI e o site de documentação estão interligados.

## Limite da API pública

A API Python estável é exportada a partir de:

```python
co_op_translator.api
```

A API pública está organizada em auxiliares de tradução de conteúdo, auxiliares de reescrita de caminhos, orquestração de projetos e revisão:

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
Deve manter os candidatos gerados separados das linhas de base aceites para que uma
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

`src/co_op_translator/__main__.py` encaminha conforme o nome do script:

- `translate` chama `co_op_translator.cli.translate.translate_command`
- `evaluate` chama `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` chama `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` chama `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` contorna `__main__.py` e chama `co_op_translator.mcp.server:main` diretamente.

Ao adicionar ou alterar opções da CLI, atualize:

- o comando relevante em `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- testes relacionados com a CLI, caso o comportamento mude

## Servidor MCP

O servidor MCP está implementado em:

```python
co_op_translator.mcp.server
```

O servidor envolve propositadamente a API Python pública em vez de chamar módulos `core` de nível inferior. Mantenha essa fronteira intacta para que os clientes MCP, chamadores Python e a CLI partilhem o mesmo comportamento.

Ao adicionar ou alterar ferramentas MCP, atualize:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` se a superfície da API pública mudar

As ferramentas de tradução do repositório são invocáveis por modelo através do MCP e podem escrever muitos ficheiros. Mantenha `dry_run=True` como padrão e exija `confirm_write=True` antes da tradução do projeto fora do modo dry-run.

## Fluxo de tradução

O fluxo de tradução de alto nível do projeto é:

1. Analisar argumentos da CLI ou parâmetros da API.
2. Validar a configuração LLM com `LLMConfig`.
3. Validar o Azure AI Vision quando a tradução de imagens for selecionada.
4. Normalizar códigos de idioma.
5. Detetar aliases de pastas de idioma legadas.
6. Estimar o volume de tradução.
7. Atualizar secções de idioma/curso do README quando aplicável.
8. Delegar a tradução do projeto para `ProjectTranslator`.
9. `ProjectTranslator` delega o processamento de ficheiros a `TranslationManager`.

`TranslationManager` é composto por mixins focados por tipo de ficheiro:

- `ProjectMarkdownTranslationMixin` trata da leitura de ficheiros Markdown, tradução de conteúdo, reescrita de caminhos, metadados, avisos e gravações.
- `ProjectNotebookTranslationMixin` trata da leitura de ficheiros de notebook, tradução de células Markdown, reescrita de caminhos, metadados, avisos e gravações.
- `ProjectImageTranslationMixin` trata da descoberta de imagens, extração/tradução de texto, gravação de imagens renderizadas e metadados.

As APIs de conteúdo de nível inferior ignoram o fluxo de trabalho do projeto:

1. `translate_markdown_content` e `translate_notebook_content` traduzem apenas conteúdo em memória.
2. `translate_image_content` traduz texto numa única imagem e devolve um objeto de imagem renderizada.
3. `rewrite_markdown_paths` e `rewrite_notebook_paths` são auxiliares de pós-processamento explícitos. Não efetuam tradução nem gravações no projeto.

## Fluxo de revisão

O fluxo de revisão determinístico é:

1. Analisar argumentos da CLI ou parâmetros da API.
2. Normalizar os códigos de idioma solicitados.
3. Construir um ou mais alvos de revisão a partir de `root_dir`, `root_dirs` ou `groups`.
4. Opcionalmente, limitar ficheiros de origem com `--changed-from`.
5. Executar verificações determinísticas para estrutura, atualidade da tradução, integridade do Markdown e caminhos locais de ligações/imagens.
6. Imprimir saída em texto ou Markdown no formato GitHub.
7. Sair com falha quando forem encontrados erros de revisão.

O fluxo de revisão não requer chaves de API e permanece disponível para verificações locais ou CI de consumidor com opt-in. Este repositório não executa `co-op-review` automaticamente em cada pull request.

## Site de documentação

O site de documentação é configurado por:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

O diretório `docs/` é a fonte canónica da documentação. Não adicione novos guias para utilizadores finais fora deste diretório, a menos que o projeto introduza intencionalmente outra superfície de documentação publicada.

Construir localmente:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Pré-visualizar localmente:

```bash
python -m mkdocs serve
```

O site gerado é escrito em `site/`, que é ignorado pelo git.

## Fluxo de trabalho do GitHub Pages

`.github/workflows/docs.yml` constrói o site em pull requests e faz o deploy quando há pushes para `main`.

O fluxo de trabalho instala:

```bash
pip install -r requirements-docs.txt
```

O fluxo de documentação instala apenas a cadeia de ferramentas de documentação. O `mkdocs.yml` aponta o `mkdocstrings` para `src/` para que as páginas da API pública possam ser renderizadas a partir da árvore de código sem instalar o conjunto completo de dependências de runtime. Se documentação futura da API exigir a importação de provedores de runtime opcionais durante a construção, atualize tanto `.github/workflows/docs.yml` quanto este guia em conjunto.

## Padrão de qualidade da documentação

Antes de fundir alterações na documentação, execute:

```bash
python -m mkdocs build --strict
git diff --check
```

Use compilações estritas para que ligações quebradas, entradas de navegação inválidas e problemas de renderização da API sejam detetados precocemente.