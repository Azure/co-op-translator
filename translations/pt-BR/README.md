# Co-op Translator

_Automatize e mantenha facilmente traduções do seu conteúdo educacional no GitHub em vários idiomas à medida que seu projeto evolui._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Pacote Python](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Licença: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Contêiner: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Estilo de código: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Contribuidores do GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![Issues do GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![Pull requests do GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs bem-vindos](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**Comece aqui:** [Escolha seu fluxo de trabalho](https://azure.github.io/co-op-translator/workflows/) | [Configuração](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [API Python](https://azure.github.io/co-op-translator/api/) | [Servidor MCP](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Suporte a Múltiplos Idiomas

#### Suportado por [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Árabe](../ar/README.md) | [Bengalês](../bn/README.md) | [Búlgaro](../bg/README.md) | [Birmanês (Myanmar)](../my/README.md) | [Chinês (Simplificado)](../zh-CN/README.md) | [Chinês (Tradicional, Hong Kong)](../zh-HK/README.md) | [Chinês (Tradicional, Macau)](../zh-MO/README.md) | [Chinês (Tradicional, Taiwan)](../zh-TW/README.md) | [Croata](../hr/README.md) | [Tcheco](../cs/README.md) | [Dinamarquês](../da/README.md) | [Holandês](../nl/README.md) | [Estoniano](../et/README.md) | [Finlandês](../fi/README.md) | [Francês](../fr/README.md) | [Alemão](../de/README.md) | [Grego](../el/README.md) | [Hebraico](../he/README.md) | [Hindi](../hi/README.md) | [Húngaro](../hu/README.md) | [Indonésio](../id/README.md) | [Italiano](../it/README.md) | [Japonês](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Coreano](../ko/README.md) | [Lituano](../lt/README.md) | [Malaio](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalês](../ne/README.md) | [Pidgin Nigeriano](../pcm/README.md) | [Norueguês](../no/README.md) | [Persa (Farsi)](../fa/README.md) | [Polonês](../pl/README.md) | [Português (Brasil)](./README.md) | [Português (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romeno](../ro/README.md) | [Russo](../ru/README.md) | [Sérvio (Cirílico)](../sr/README.md) | [Eslovaco](../sk/README.md) | [Esloveno](../sl/README.md) | [Espanhol](../es/README.md) | [Suaíli](../sw/README.md) | [Sueco](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tâmil](../ta/README.md) | [Telugu](../te/README.md) | [Tailandês](../th/README.md) | [Turco](../tr/README.md) | [Ucraniano](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamita](../vi/README.md)

> **Prefere clonar localmente?**
>
> Este repositório inclui mais de 50 traduções de idiomas, o que aumenta significativamente o tamanho do download. Para clonar sem traduções, use sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Isso fornece tudo o que você precisa para concluir o curso com um download muito mais rápido.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![Observadores do GitHub](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![Forks do GitHub](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![Estrelas do GitHub](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Discord do Microsoft Foundry](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Abrir no GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Visão Geral

**Co-op Translator** ajuda você a localizar seu conteúdo educacional do GitHub em vários idiomas com facilidade.
Quando você atualiza seus arquivos Markdown, imagens ou notebooks, as traduções permanecem automaticamente sincronizadas, garantindo que seu conteúdo continue preciso e atualizado para aprendizes no mundo todo.

Use-o a partir da CLI para traduzir repositórios, pela API Python para automação ou através do servidor MCP para fluxos de trabalho com agentes e editores.

Exemplo de como o conteúdo traduzido é organizado:

![Exemplo](../../imgs/translation-ex.png)

## Por que o Co-op Translator?

Traduzir um arquivo é fácil. Manter um repositório de documentação inteiro
traduzido, vinculado e atualizado é a parte difícil.

| Problema | Como o Co-op Translator ajuda |
| --- | --- |
| Documentos longos não são um único prompt | Arquivos Markdown grandes são divididos em blocos, então um README extenso não depende de uma única e frágil resposta do modelo. Se um bloco falhar, o Co-op Translator pode tentar novamente e redividir apenas a parte que falhou. |
| Traduções incompletas não devem ser marcadas como atuais | Uma tradução truncada nunca deve ser considerada atualizada. O Co-op Translator verifica a integridade da tradução antes de salvar e pode detectar traduções existentes estruturalmente incompletas. |
| Os links devem corresponder à estrutura do repositório traduzido | Traduções manuais frequentemente deixam links relativos apontando de volta para a árvore de origem. O Co-op Translator reescreve links de Markdown, notebooks, imagens e README para corresponder à estrutura `translations/<lang>/...`. |
| A tradução deve funcionar em todo o repositório | O Co-op Translator lida com arquivos README, docs, notebooks e texto de imagens como parte de um único fluxo de trabalho do repositório, em vez de traduzir arquivos um por um. |
| Manter traduções importa mais do que criá-las uma vez | Hashes de origem e metadados de tradução permitem que o Co-op Translator encontre arquivos desatualizados, pule arquivos sem alterações e mantenha o conteúdo traduzido sincronizado à medida que o repositório fonte evolui. |

## Como o estado da tradução é gerenciado

Co-op Translator gerencia o conteúdo traduzido como **artefatos de software versionados**,  
não como arquivos estáticos.

A ferramenta rastreia o estado de Markdown traduzido, imagens e notebooks
usando **metadados com escopo de idioma**.

Esse desenho permite que o Co-op Translator:

- Detectar traduções desatualizadas com confiabilidade
- Tratar Markdown, imagens e notebooks de forma consistente
- Escalar com segurança em repositórios grandes, dinâmicos e multilíngues

Ao modelar traduções como artefatos gerenciados,
os fluxos de trabalho de tradução se alinham naturalmente com as práticas modernas
de gerenciamento de dependências e artefatos de software.

→ [Como o estado da tradução é gerenciado](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Artigos aprofundados relacionados

- [Corrigindo Markdown Quebrado na Tradução por IA: Fortalecendo um pipeline de produção](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Comece

O Co-op Translator pode ser usado pela CLI, pela API Python ou pelo servidor MCP. Comece com o guia de fluxo de trabalho se você estiver escolhendo entre tradução local, automação, CI e integração com agentes/editores.

- [Escolha seu fluxo de trabalho](../../docs/workflows.md)
- [Configurar credenciais](../../docs/configuration.md)
- [Traduzir pela CLI](../../docs/cli.md)
- [Automatizar com a API Python](../../docs/api.md)
- [Conectar ao servidor MCP](../../docs/mcp.md)
- [Executar no GitHub Actions](../../docs/github-actions.md)

Exemplo mínimo de CLI após a configuração:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

Para as primeiras execuções em repositórios grandes, use `--dry-run` antes de gravar os arquivos traduzidos. Veja a [Referência da CLI](../../docs/cli.md) para flags de tipo de conteúdo, logs, revisão e migração de links.

Execução rápida do contêiner com Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Execução rápida do contêiner com PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Recursos

- Tradução automatizada para Markdown, notebooks e imagens
- Mantém as traduções sincronizadas com as alterações da origem
- Funciona localmente (CLI) ou em CI (GitHub Actions)
- Expõe ferramentas de tradução de Markdown, notebooks, imagens, revisão e projeto através do MCP
- Utiliza Azure OpenAI ou OpenAI para tradução com suporte de provedor
- Permite que o MCP hospede agentes para traduzir blocos de Markdown e notebooks sem credenciais LLM do Co-op Translator
- Utiliza Azure AI Vision para extração e tradução de texto em imagens
- Revê a estrutura e a atualidade das traduções com verificações determinísticas
- Preserva a formatação e a estrutura do Markdown

## Documentação

- [Site de documentação](https://azure.github.io/co-op-translator/)
- [Escolha seu fluxo de trabalho](../../docs/workflows.md)
- [Configuração](../../docs/configuration.md)
- [Configuração do Azure AI](../../docs/azure-ai-setup.md)
- [Referência da CLI](../../docs/cli.md)
- [API Python](../../docs/api.md)
- [Servidor MCP](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [Modelo de README para idiomas](../../docs/readme-languages-template.md)
- [Idiomas suportados](../../docs/supported-languages.md)
- [Contribuindo](../../CONTRIBUTING.md)
- [Solução de problemas](../../docs/troubleshooting.md)

### Guia específico da Microsoft
> [!NOTE]
> Para mantenedores dos repositórios “For Beginners” da Microsoft apenas.

- [Atualizando a lista de “outros cursos” (somente para repositórios Microsoft 'For Beginners')](../../docs/microsoft-beginners.md)

## Apoie-nos e promova o aprendizado global

Junte-se a nós na revolução de como o conteúdo educacional é compartilhado globalmente! Dê uma ⭐ para o [Co-op Translator](https://github.com/azure/co-op-translator) no GitHub e apoie nossa missão de derrubar barreiras linguísticas no aprendizado e na tecnologia. Seu interesse e contribuições têm um impacto significativo! Contribuições de código e sugestões de recursos são sempre bem-vindas.

### Explore o conteúdo educacional da Microsoft no seu idioma
- [LangChain4j para Iniciantes](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD para Iniciantes](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI para Iniciantes](https://github.com/microsoft/edgeai-for-beginners)
- [Protocolo de Contexto de Modelo (MCP) para Iniciantes](https://github.com/microsoft/mcp-for-beginners)
- [Agentes de IA para Iniciantes](https://github.com/microsoft/ai-agents-for-beginners)
- [IA Generativa para Iniciantes com .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [IA Generativa para Iniciantes](https://github.com/microsoft/generative-ai-for-beginners)
- [IA Generativa para Iniciantes com Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [Aprendizado de Máquina para Iniciantes](https://aka.ms/ml-beginners)
- [Ciência de Dados para Iniciantes](https://aka.ms/datascience-beginners)
- [IA para Iniciantes](https://aka.ms/ai-beginners)
- [Cibersegurança para Iniciantes](https://github.com/microsoft/Security-101)
- [Desenvolvimento Web para Iniciantes](https://aka.ms/webdev-beginners)
- [IoT para Iniciantes](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Apresentações em vídeo

👉 Clique na imagem abaixo para assistir no YouTube.

- **Open at Microsoft**: Uma breve introdução de 18 minutos e um guia rápido sobre como usar o Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contribuindo

Este projeto aceita contribuições e sugestões. Interessado em contribuir com o Azure Co-op Translator? Consulte nosso [CONTRIBUTING.md](../../CONTRIBUTING.md) para obter diretrizes sobre como você pode ajudar a tornar o Co-op Translator mais acessível.

## Contribuidores

[![contribuidores do co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Código de Conduta

Este projeto adotou o [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Para mais informações veja o [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ou
entre em contato com [opencode@microsoft.com](mailto:opencode@microsoft.com) para quaisquer perguntas ou comentários adicionais.

## IA Responsável

A Microsoft está comprometida em ajudar nossos clientes a usar nossos produtos de IA de forma responsável, compartilhando nossos aprendizados e construindo parcerias baseadas na confiança por meio de ferramentas como Notas de Transparência e Avaliações de Impacto. Muitos desses recursos podem ser encontrados em [https://aka.ms/RAI](https://aka.ms/RAI).
A abordagem da Microsoft para IA responsável está fundamentada em nossos princípios de IA de justiça, confiabilidade e segurança, privacidade e segurança, inclusão, transparência e responsabilidade.

Modelos de linguagem natural, imagem e fala em grande escala - como os usados neste exemplo - podem potencialmente se comportar de maneiras que sejam injustas, pouco confiáveis ou ofensivas, causando danos. Consulte a [nota de transparência do serviço Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) para se informar sobre riscos e limitações.

A abordagem recomendada para mitigar esses riscos é incluir um sistema de segurança em sua arquitetura que possa detectar e prevenir comportamentos prejudiciais. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) fornece uma camada independente de proteção, capaz de detectar conteúdo gerado por usuários e por IA que seja prejudicial em aplicações e serviços. O Azure AI Content Safety inclui APIs de texto e imagem que permitem detectar material que é prejudicial. Também temos um Content Safety Studio interativo que permite visualizar, explorar e testar exemplos de código para detectar conteúdo prejudicial em diferentes modalidades. A seguinte [documentação de inicialização rápida](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) orienta você a fazer solicitações ao serviço.

Outro aspecto a ser levado em conta é o desempenho geral da aplicação. Em aplicações multimodais e com múltiplos modelos, consideramos desempenho como o fato de o sistema operar conforme você e seus usuários esperam, incluindo não gerar saídas prejudiciais. É importante avaliar o desempenho da sua aplicação geral usando [métricas de qualidade de geração e de risco e segurança](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Você pode avaliar sua aplicação de IA no ambiente de desenvolvimento usando o [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Considerando um conjunto de dados de teste ou um objetivo, as gerações da sua aplicação de IA generativa são medidas quantitativamente com avaliadores incorporados ou avaliadores personalizados de sua escolha. Para começar com o prompt flow SDK para avaliar seu sistema, você pode seguir o [guia de inicialização rápida](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Depois de executar uma avaliação, você pode [visualizar os resultados no Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marcas registradas

Este projeto pode conter marcas registradas ou logotipos de projetos, produtos ou serviços. O uso autorizado de marcas ou logotipos da Microsoft está sujeito a e deve seguir as [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
O uso de marcas ou logotipos da Microsoft em versões modificadas deste projeto não deve causar confusão nem implicar patrocínio da Microsoft.
Qualquer uso de marcas ou logotipos de terceiros está sujeito às políticas desses terceiros.

## Obtendo Ajuda

Se você ficar preso ou tiver alguma dúvida sobre como criar aplicativos de IA, participe:

[![Discord do Microsoft Foundry](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Se você tiver feedback sobre o produto ou encontrar erros durante o desenvolvimento, visite:

[![Fórum de Desenvolvedores do Microsoft Foundry](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)