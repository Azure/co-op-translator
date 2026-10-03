# Escolha o seu fluxo de trabalho

O Co-op Translator pode ser usado de três formas: a CLI, a Python API e o servidor MCP. Partilham as mesmas capacidades de tradução, mas cada um se encaixa num fluxo de trabalho diferente.

Use esta página quando estiver a decidir por onde começar.

**Se editar traduções manualmente:** os fluxos de trabalho padrão da CLI e do Actions retraduzem os ficheiros fonte alterados na íntegra, pelo que a sua redação nesses ficheiros pode ser sobrescrita. Reveja o diff antes de aceitar uma atualização. Para preservação ao nível de bloco Markdown das edições aceites, use o opcional [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Decisão rápida

| Se pretende... | Utilize | Comece aqui |
| --- | --- | --- |
| Traduzir ou rever um repositório a partir de um terminal | CLI | [Referência da CLI](cli.md) |
| Adicionar tradução a um script Python, serviço, notebook, ou trabalho de CI | Python API | [API Python](api.md) |
| Permitir que um agente, editor ou cliente compatível com MCP traduza conteúdo para si | MCP Server | [Servidor MCP](mcp.md) |
| Traduzir um documento Markdown, notebook ou imagem que a sua app já carregou | Python API or MCP Server | [API Python](api.md) or [Servidor MCP](mcp.md) |
| Traduzir um repositório inteiro com pastas de saída padrão e metadados | CLI or `run_translation` | [Referência da CLI](cli.md) or [API Python](api.md) |

## Use a CLI quando

Escolha a CLI quando uma pessoa ou um trabalho de CI estiver a controlar a tradução do repositório a partir de um shell.

A CLI é o caminho mais direto quando pretende que o Co-op Translator descubra ficheiros do projeto, crie saídas traduzidas, preserve a estrutura do projeto, atualize metadados e execute comandos de revisão.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Este exemplo traduz Markdown e notebooks. Adicione `-img` só depois de configurar o [Azure AI Vision](configuration.md#azure-ai-vision). Para uma primeira execução apenas com Markdown, siga [A sua primeira tradução](first-translation.md).

Adequado para:

- Está a traduzir um repositório a partir do seu terminal.
- Quer um comando repetível para workflows de CI ou de lançamento.
- Quer descoberta de projeto incorporada, caminhos de saída, metadados, limpeza e revisão.
- Prefere uma interface de comandos em vez de escrever código Python.

## Use a Python API quando

Escolha a API Python quando o seu próprio código deve controlar o fluxo de trabalho.

A API é útil para aplicações, scripts de automação, notebooks, serviços e pipelines personalizados. Permite chamar APIs de tradução de conteúdo de baixo nível para ficheiros individuais, ou executar a mesma orquestração ao nível do repositório usada pela CLI.

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
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

Adequado para:

- A sua aplicação já lê ficheiros, buffers, notebooks ou bytes de imagem.
- Precisa de validação personalizada, armazenamento, registo, tentativas ou fluxos de aprovação.
- Quer traduzir um documento, notebook ou imagem sem processar todo o repositório.
- Quer a tradução de um repositório, mas através de automação Python em vez de um comando shell.

## Use o servidor MCP quando

Escolha o servidor MCP quando um agente, editor ou cliente compatível com MCP deverá invocar as ferramentas do Co-op Translator.

Na configuração local habitual, o utilizador não mantém manualmente um servidor em execução. O cliente MCP inicia `co-op-translator-mcp` sobre `stdio` quando necessita das ferramentas.

Exemplos de pedidos de utilizador que um agente poderia tratar:

- "Traduza este ficheiro Markdown para coreano e mantenha os links corretos."
- "Traduza este ficheiro Markdown para coreano com o workflow MCP assistido por agente, usando o seu próprio modelo para os blocos traduzidos."
- "Traduza este notebook para coreano, preserve as células de código e use o Co-op Translator MCP para reconstruir o notebook."
- "Traduza o texto nesta imagem para japonês e guarde o resultado."
- "Faça uma execução em simulação de uma tradução de repositório para espanhol e diga-me o que mudaria."
- "Reveja se a saída da tradução para coreano está atualizada."

Para Markdown e notebooks, o MCP pode funcionar em dois modos:

| Modo | Use quando | Ferramentas principais |
| --- | --- | --- |
| Assistido por agente | O agente anfitrião MCP deve traduzir os blocos com o seu próprio modelo, sem credenciais de fornecedor LLM do Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Suportado por fornecedor | O Co-op Translator deve chamar Azure OpenAI, OpenAI ou Anthropic diretamente. | `translate_markdown_content`, `translate_notebook_content` |

Formato da chamada da ferramenta Markdown no modo suportado por fornecedor MCP:

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

Formato da chamada da ferramenta de imagens MCP:

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

A tradução do repositório é feita em simulação por defeito através do MCP:

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

Adequado para:

- Quer fluxos de trabalho de tradução em linguagem natural dentro de um agente ou editor.
- Quer tradução de Markdown ou notebooks onde o modelo do agente anfitrião traduza os blocos preparados.
- Quer que o agente traduza conteúdo selecionado em vez de um repositório inteiro.
- Pretende uma etapa de aprovação antes de escritas em todo o repositório.
- Quer uma interface que exponha ferramentas de Markdown, notebooks, imagens, revisão e reescrita de caminhos.

## Como funcionam em conjunto

A CLI é a melhor opção por defeito para pessoas a traduzirem repositórios. A API Python é a melhor quando o seu código gere o fluxo de trabalho. O servidor MCP é a melhor quando um agente ou editor gere o fluxo de trabalho.

Os três caminhos usam a mesma API pública do Co-op Translator, por isso pode começar com a CLI, automatizar com Python mais tarde, e expor as mesmas capacidades a clientes MCP quando precisar de fluxos de trabalho conduzidos por agentes.