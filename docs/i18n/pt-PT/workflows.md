# Escolha o Seu Fluxo de Trabalho

Co-op Translator pode ser usado de três maneiras: a CLI, a API Python e o servidor MCP. Partilham as mesmas capacidades de tradução, mas cada uma se adequa a um fluxo de trabalho diferente.

Use esta página quando estiver a decidir por onde começar.

## Decisão Rápida

| Se pretende... | Utilizar | Comece aqui |
| --- | --- | --- |
| Traduzir ou rever um repositório a partir de um terminal | CLI | [Referência CLI](cli.md) |
| Adicionar tradução a um script Python, serviço, notebook ou trabalho de CI | API Python | [API Python](api.md) |
| Permitir que um agente, editor ou cliente compatível com MCP traduza conteúdo por si | Servidor MCP | [Servidor MCP](mcp.md) |
| Traduzir um documento Markdown, notebook ou imagem que a sua aplicação já carregou | API Python ou Servidor MCP | [API Python](api.md) ou [Servidor MCP](mcp.md) |
| Traduzir um repositório inteiro com pastas de saída padrão e metadados | CLI ou `run_translation` | [Referência CLI](cli.md) ou [API Python](api.md) |

## Use the CLI quando

Escolha a CLI quando uma pessoa ou uma tarefa de CI estiver a conduzir a tradução do repositório a partir de um shell.

A CLI é a via mais direta quando pretende que o Co-op Translator descubra ficheiros do projeto, crie saídas traduzidas, preserve a estrutura do projeto, atualize metadados e execute comandos de revisão.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Indicado para:

- Está a traduzir um repositório a partir do seu terminal.
- Pretende um comando repetível para fluxos de trabalho de CI ou de lançamento.
- Pretende descoberta de projetos integrada, caminhos de saída, metadados, limpeza e revisão.
- Prefere uma interface por comandos em vez de escrever código Python.

## Use the Python API quando

Escolha a API Python quando o seu código deve controlar o fluxo de trabalho.

A API é útil para aplicações, scripts de automação, notebooks, serviços e pipelines personalizados. Permite chamar APIs de tradução de conteúdo de baixo nível para ficheiros individuais, ou executar a mesma orquestração a nível de repositório usada pela CLI.

Traduza um documento Markdown e decida onde o guardar:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Execute uma tradução de repositório a partir do Python:

```python
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

Indicado para:

- A sua aplicação já lê ficheiros, buffers, notebooks ou bytes de imagem.
- Necessita de validação personalizada, armazenamento, registo, retentativas ou fluxos de aprovação.
- Quer traduzir um documento, notebook ou imagem sem processar todo o repositório.
- Quer tradução de repositório, mas a partir de automação Python em vez de um comando de shell.

## Use o Servidor MCP quando

Escolha o servidor MCP quando um agente, editor ou cliente compatível com MCP deve invocar as ferramentas do Co-op Translator.

No ambiente local normal, o utilizador não mantém manualmente um servidor em execução. O cliente MCP inicia `co-op-translator-mcp` sobre `stdio` quando precisa das ferramentas.

Exemplos de pedidos de utilizador que um agente poderia tratar:

- "Traduzir este ficheiro Markdown para coreano e manter os links corretos."
- "Traduzir este ficheiro Markdown para coreano com o fluxo de trabalho MCP assistido por agente, usando o seu próprio modelo para os fragmentos traduzidos."
- "Traduzir este notebook para coreano, preservar as células de código e usar o Co-op Translator MCP para reconstruir o notebook."
- "Traduzir o texto desta imagem para japonês e guardar o resultado."
- "Executar uma simulação de tradução de repositório para espanhol e diga-me o que mudaria."
- "Rever se a saída da tradução para coreano está atualizada."

Para Markdown e notebooks, o MCP pode funcionar em dois modos:

| Modo | Utilize quando | Ferramentas principais |
| --- | --- | --- |
| Assistido por agente | O agente anfitrião MCP deve traduzir os fragmentos com o seu próprio modelo, sem credenciais de fornecedor LLM do Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Suportado por fornecedor | O Co-op Translator deve chamar Azure OpenAI ou OpenAI diretamente. | `translate_markdown_content`, `translate_notebook_content` |

Formato da chamada da ferramenta Markdown suportada por fornecedor no MCP:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

Formato da chamada da ferramenta de imagem do MCP:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

A tradução de repositório é, por omissão, executada em modo simulação através do MCP:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

Indicado para:

- Quer fluxos de trabalho de tradução em linguagem natural dentro de um agente ou editor.
- Pretende tradução de Markdown ou notebooks onde o modelo do agente anfitrião traduz fragmentos preparados.
- Quer que o agente traduza conteúdo selecionado em vez de todo o repositório.
- Deseja um passo de aprovação antes de escritas em todo o repositório.
- Deseja uma única interface que exponha ferramentas para Markdown, notebooks, imagens, revisão e reescrita de caminhos.

## Como se Encaixam

A CLI é a melhor opção por defeito para pessoas a traduzir repositórios. A API Python é a melhor quando o seu código controla o fluxo de trabalho. O servidor MCP é a melhor quando um agente ou editor controla o fluxo de trabalho.

Todos os três caminhos usam a mesma API pública do Co-op Translator, por isso pode começar com a CLI, automatizar com Python mais tarde e expor as mesmas capacidades a clientes MCP quando precisar de fluxos de trabalho orientados por agentes.