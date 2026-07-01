# Escolha Seu Fluxo de Trabalho

Co-op Translator pode ser usado de três maneiras: a CLI, a API Python e o servidor MCP. Elas compartilham as mesmas capacidades de tradução, mas cada uma se encaixa em um fluxo de trabalho diferente.

Use esta página quando estiver decidindo por onde começar.

## Decisão Rápida

| Se você quiser... | Usar | Comece aqui |
| --- | --- | --- |
| Traduzir ou revisar um repositório pelo terminal | CLI | [Referência da CLI](cli.md) |
| Adicionar tradução a um script Python, serviço, notebook ou tarefa de CI | Python API | [API Python](api.md) |
| Permitir que um agente, editor ou cliente compatível com MCP traduza conteúdo para você | MCP Server | [Servidor MCP](mcp.md) |
| Traduzir um documento Markdown, notebook ou imagem que seu aplicativo já carregou | Python API ou MCP Server | [API Python](api.md) ou [Servidor MCP](mcp.md) |
| Traduzir um repositório inteiro com pastas de saída padrão e metadados | CLI ou `run_translation` | [Referência da CLI](cli.md) ou [API Python](api.md) |

## Use a CLI quando

Escolha a CLI quando uma pessoa ou uma tarefa de CI estiver conduzindo a tradução do repositório a partir de um shell.

A CLI é o caminho mais direto quando você quer que o Co-op Translator descubra arquivos do projeto, crie saídas traduzidas, preserve o layout do projeto, atualize metadados e execute comandos de revisão.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Bom para:

- Você está traduzindo um repositório pelo terminal.
- Você quer um comando reprodutível para fluxos de trabalho de CI ou de release.
- Você quer descoberta de projeto integrada, caminhos de saída, metadados, limpeza e revisão.
- Você prefere uma interface por comando em vez de escrever código Python.

## Use a API Python quando

Escolha a API Python quando seu próprio código deve controlar o fluxo de trabalho.

A API é útil para aplicações, scripts de automação, notebooks, serviços e pipelines personalizados. Ela permite chamar APIs de tradução de conteúdo de baixo nível para arquivos individuais, ou executar a mesma orquestração em nível de repositório usada pela CLI.

Traduza um documento Markdown e decida onde salvá-lo:

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

Bom para:

- Sua aplicação já lê arquivos, buffers, notebooks ou bytes de imagem.
- Você precisa de validação personalizada, armazenamento, logs, retentativas ou fluxos de aprovação.
- Você quer traduzir um documento, notebook ou imagem sem processar um repositório inteiro.
- Você quer tradução de repositório, mas a partir de automação Python em vez de um comando de shell.

## Use o Servidor MCP quando

Escolha o servidor MCP quando um agente, editor ou cliente compatível com MCP deve chamar as ferramentas do Co-op Translator.

Na configuração local normal, o usuário não mantém manualmente um servidor em execução. O cliente MCP inicia `co-op-translator-mcp` sobre `stdio` quando precisa das ferramentas.

Exemplos de solicitações de usuário que um agente poderia tratar:

- "Traduza este arquivo Markdown para coreano e mantenha os links corretos."
- "Traduza este arquivo Markdown para coreano com o fluxo de trabalho MCP assistido por agente, usando seu próprio modelo para os trechos traduzidos."
- "Traduza este notebook para coreano, preserve as células de código e use o MCP do Co-op Translator para reconstruir o notebook."
- "Traduza o texto desta imagem para japonês e salve o resultado."
- "Faça um dry-run de uma tradução de repositório para espanhol e me diga o que mudaria."
- "Verifique se a saída da tradução para coreano está atualizada."

Para Markdown e notebooks, o MCP pode funcionar em dois modos:

| Modo | Quando usar | Principais ferramentas |
| --- | --- | --- |
| Assistido por agente | O agente host MCP deve traduzir trechos com seu próprio modelo, sem credenciais de provedor LLM do Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Com provedor | O Co-op Translator deve chamar Azure OpenAI ou OpenAI diretamente. | `translate_markdown_content`, `translate_notebook_content` |

Formato da chamada da ferramenta Markdown com provedor MCP:

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

Formato da chamada da ferramenta de imagem MCP:

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

A tradução de repositório é executada como simulação por padrão via MCP:

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

Bom para:

- Você quer fluxos de trabalho de tradução em linguagem natural dentro de um agente ou editor.
- Você quer tradução de Markdown ou notebooks onde o modelo do agente host traduz trechos preparados.
- Você quer que o agente traduza conteúdo selecionado em vez de um repositório inteiro.
- Você quer uma etapa de aprovação antes de escrever em todo o repositório.
- Você quer uma interface única que exponha ferramentas de Markdown, notebook, imagem, revisão e reescrita de caminhos.

## Como eles se encaixam

A CLI é a melhor opção padrão para pessoas que traduzem repositórios. A API Python é a melhor quando seu código domina o fluxo de trabalho. O servidor MCP é o melhor quando um agente ou editor domina o fluxo de trabalho.

Os três caminhos usam a mesma API pública do Co-op Translator, então você pode começar com a CLI, automatizar com Python depois e expor as mesmas capacidades para clientes MCP quando precisar de fluxos de trabalho dirigidos por agentes.