# Escolha seu fluxo de trabalho

O Co-op Translator pode ser usado de três maneiras: o CLI, a Python API e o servidor MCP. Eles compartilham as mesmas capacidades de tradução, mas cada um se encaixa em um fluxo de trabalho diferente.

Use esta página quando estiver decidindo por onde começar.

**Se você editar traduções manualmente:** os fluxos padrão do CLI e do Actions re-traduzem os arquivos de origem alterados por completo, então sua redação nesses arquivos pode ser sobrescrita. Revise o diff antes de aceitar uma atualização. Para preservação em nível de bloco Markdown das edições aceitas, use o opcional [provedor de estado de tradução da Python API](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Decisão Rápida

| Se você quer... | Use | Comece aqui |
| --- | --- | --- |
| Traduzir ou revisar um repositório a partir de um terminal | CLI | [Referência do CLI](cli.md) |
| Adicionar tradução a um script Python, serviço, notebook ou trabalho de CI | Python API | [Python API](api.md) |
| Permitir que um agente, editor ou cliente compatível com MCP traduza conteúdo para você | MCP Server | [Servidor MCP](mcp.md) |
| Traduzir um documento Markdown, notebook ou imagem que seu app já carregou | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Traduzir um repositório inteiro com pastas de saída padrão e metadados | CLI or `run_translation` | [Referência do CLI](cli.md) or [Python API](api.md) |

## Use o CLI quando

Escolha o CLI quando uma pessoa ou um trabalho de CI estiver conduzindo a tradução do repositório a partir de um shell.

O CLI é o caminho mais direto quando você quer que o Co-op Translator descubra arquivos do projeto, crie outputs traduzidos, preserve o layout do projeto, atualize metadados e execute comandos de revisão.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Este exemplo traduz Markdown e notebooks. Adicione `-img` somente após configurar [Azure AI Vision](configuration.md#azure-ai-vision). Para uma primeira execução apenas com Markdown, siga [Sua primeira tradução](first-translation.md).

Bom para:

- Você está traduzindo um repositório a partir do seu terminal.
- Você quer um comando repetível para fluxos de trabalho de CI ou de release.
- Você quer descoberta de projeto integrada, caminhos de saída, metadados, limpeza e revisão.
- Você prefere uma interface por comando em vez de escrever código Python.

## Use a Python API quando

Escolha a Python API quando seu próprio código deve controlar o fluxo de trabalho.

A API é útil para aplicações, scripts de automação, notebooks, serviços e pipelines customizados. Ela permite chamar APIs de tradução de conteúdo de baixo nível para arquivos individuais, ou executar a mesma orquestração em nível de repositório usada pelo CLI.

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
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

Bom para:

- Seu aplicativo já lê arquivos, buffers, notebooks ou bytes de imagem.
- Você precisa de validação personalizada, armazenamento, registro (logging), tentativas (retries) ou fluxos de aprovação.
- Você quer traduzir um documento, notebook ou imagem sem processar um repositório inteiro.
- Você quer traduzir um repositório, mas a partir de automação em Python em vez de um comando de shell.

## Use o Servidor MCP quando

Escolha o servidor MCP quando um agente, editor ou um cliente compatível com MCP deve chamar as ferramentas do Co-op Translator.

Na configuração local normal, o usuário não mantém manualmente um servidor em execução. O cliente MCP inicia `co-op-translator-mcp` sobre `stdio` quando precisa das ferramentas.

Exemplos de solicitações de usuário que um agente poderia atender:

- "Traduzir este arquivo Markdown para coreano e manter os links corretos."
- "Traduzir este arquivo Markdown para coreano com o fluxo de trabalho MCP assistido por agente, usando seu próprio modelo para os trechos traduzidos."
- "Traduzir este notebook para coreano, preservar células de código e usar o MCP do Co-op Translator para reconstruir o notebook."
- "Traduzir o texto nesta imagem para japonês e salvar o resultado."
- "Fazer um dry-run de tradução de repositório para espanhol e me dizer o que mudaria."
- "Revisar se a saída da tradução para coreano está atualizada."

Para Markdown e notebooks, o MCP pode operar em dois modos:

| Modo | Use quando | Principais ferramentas |
| --- | --- | --- |
| Agent-assisted | O agente host MCP deve traduzir trechos com seu próprio modelo, sem credenciais de provedor LLM do Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | O Co-op Translator deve chamar Azure OpenAI, OpenAI ou Anthropic diretamente. | `translate_markdown_content`, `translate_notebook_content` |

Formato da chamada da ferramenta Markdown com provedor no MCP:

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

A tradução do repositório é executada em dry-run por padrão via MCP:

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
- Você quer tradução de Markdown ou notebook onde o modelo do agente host traduz trechos preparados.
- Você quer que o agente traduza conteúdo selecionado em vez de um repositório inteiro.
- Você quer uma etapa de aprovação antes de escritas em todo o repositório.
- Você quer uma interface que exponha ferramentas para Markdown, notebook, imagem, revisão e reescrita de caminhos.

## Como eles se encaixam

O CLI é a melhor opção padrão para humanos que traduzem repositórios. A Python API é a melhor quando seu código controla o fluxo de trabalho. O servidor MCP é a melhor quando um agente ou editor controla o fluxo de trabalho.

Os três caminhos usam a mesma API pública do Co-op Translator, então você pode começar com o CLI, automatizar com Python depois e expor as mesmas capacidades a clientes MCP quando precisar de fluxos de trabalho conduzidos por agentes.