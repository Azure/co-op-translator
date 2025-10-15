<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:02:01+00:00",
  "source_file": "README.md",
  "language_code": "br"
}
-->
# Co-op Translator

_Automatize facilmente a tradução do seu conteúdo educacional do GitHub para vários idiomas e alcance uma audiência global._

[![Pacote Python](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Licença: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Estilo de código: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Contribuidores do GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![Issues do GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![Pull-requests do GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Suporte a múltiplos idiomas

#### Suportado pelo [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Árabe](../ar/README.md) | [Bengali](../bn/README.md) | [Búlgaro](../bg/README.md) | [Birmanês (Myanmar)](../my/README.md) | [Chinês (Simplificado)](../zh/README.md) | [Chinês (Tradicional, Hong Kong)](../hk/README.md) | [Chinês (Tradicional, Macau)](../mo/README.md) | [Chinês (Tradicional, Taiwan)](../tw/README.md) | [Croata](../hr/README.md) | [Tcheco](../cs/README.md) | [Dinamarquês](../da/README.md) | [Holandês](../nl/README.md) | [Estoniano](../et/README.md) | [Finlandês](../fi/README.md) | [Francês](../fr/README.md) | [Alemão](../de/README.md) | [Grego](../el/README.md) | [Hebraico](../he/README.md) | [Hindi](../hi/README.md) | [Húngaro](../hu/README.md) | [Indonésio](../id/README.md) | [Italiano](../it/README.md) | [Japonês](../ja/README.md) | [Coreano](../ko/README.md) | [Lituano](../lt/README.md) | [Malaio](../ms/README.md) | [Marathi](../mr/README.md) | [Nepalês](../ne/README.md) | [Norueguês](../no/README.md) | [Persa (Farsi)](../fa/README.md) | [Polonês](../pl/README.md) | [Português (Brasil)](./README.md) | [Português (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romeno](../ro/README.md) | [Russo](../ru/README.md) | [Sérvio (Cirílico)](../sr/README.md) | [Eslovaco](../sk/README.md) | [Esloveno](../sl/README.md) | [Espanhol](../es/README.md) | [Suaíli](../sw/README.md) | [Sueco](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tâmil](../ta/README.md) | [Tailandês](../th/README.md) | [Turco](../tr/README.md) | [Ucraniano](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamita](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![Observadores do GitHub](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![Forks do GitHub](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![Estrelas do GitHub](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Abrir no GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Visão geral

O **Co-op Translator** permite que você traduza rapidamente seu conteúdo educacional do GitHub para vários idiomas, alcançando uma audiência global sem esforço. Quando você atualiza seus arquivos Markdown, imagens ou notebooks Jupyter, as traduções são sincronizadas automaticamente para garantir que seu conteúdo educacional no GitHub permaneça atualizado e relevante para usuários internacionais.

Veja como o Co-op Translator organiza o conteúdo educacional traduzido no GitHub:

![Exemplo](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.br.png)

## Início rápido

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

Docker:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Configuração mínima

- Crie um arquivo `.env` usando o template: [.env.template](../../.env.template)
- Configure um provedor LLM (Azure OpenAI ou OpenAI)
- Para tradução de imagens (`-img`), também configure o Azure AI Vision
- Recomendado: Se você já tem traduções geradas por outras ferramentas, limpe-as antes para evitar conflitos (por exemplo: `translations/`).
- Recomendado: Adicione uma seção de traduções ao seu README usando o [template de idiomas do README](./README_languages_template.md)
- Veja: [Configurar Azure AI](./getting_started/set-up-azure-ai.md)

## Uso

Traduzir todos os tipos suportados:

```bash
translate -l "ko ja"
```

Apenas Markdown:

```bash
translate -l "de" -md
```

Markdown + imagens:

```bash
translate -l "pt" -md -img
```

Apenas notebooks:

```bash
translate -l "zh" -nb
```

Mais opções: [Referência de comandos](./getting_started/command-reference.md)

## Funcionalidades

- Tradução automática para Markdown, notebooks e imagens
- Mantém as traduções sincronizadas com alterações na fonte
- Funciona localmente (CLI) ou em CI (GitHub Actions)
- Usa Azure OpenAI ou OpenAI; opcional Azure AI Vision para imagens
- Preserva a formatação e estrutura do Markdown

## Documentação

- [Guia de linha de comando](./getting_started/command-line-guide/command-line-guide.md)
- [Guia do GitHub Actions (Repositórios públicos & segredos padrão)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Guia do GitHub Actions (Repositórios de organização Microsoft & configurações de nível organizacional)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Idiomas suportados](./getting_started/supported-languages.md)
- [Solução de problemas](./getting_started/troubleshooting.md)

## Apoie e incentive o aprendizado global

Junte-se a nós para revolucionar a forma como o conteúdo educacional é compartilhado globalmente! Dê uma ⭐ no [Co-op Translator](https://github.com/azure/co-op-translator) no GitHub e apoie nossa missão de quebrar barreiras linguísticas no aprendizado e na tecnologia. Seu interesse e contribuições fazem toda a diferença! Contribuições de código e sugestões de funcionalidades são sempre bem-vindas.

### Explore conteúdo educacional da Microsoft no seu idioma

- [AZD para Iniciantes](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI para Iniciantes](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) Para Iniciantes](https://github.com/microsoft/mcp-for-beginners)
- [Agentes de IA para Iniciantes](https://github.com/microsoft/ai-agents-for-beginners)
- [IA Generativa para Iniciantes usando .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [IA Generativa para Iniciantes](https://github.com/microsoft/generative-ai-for-beginners)
- [IA Generativa para Iniciantes usando Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML para Iniciantes](https://aka.ms/ml-beginners)
- [Ciência de Dados para Iniciantes](https://aka.ms/datascience-beginners)
- [IA para Iniciantes](https://aka.ms/ai-beginners)
- [Cibersegurança para Iniciantes](https://github.com/microsoft/Security-101)
- [Desenvolvimento Web para Iniciantes](https://aka.ms/webdev-beginners)
- [IoT para Iniciantes](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Apresentações em vídeo

Saiba mais sobre o Co-op Translator através das nossas apresentações _(Clique na imagem abaixo para assistir no YouTube.)_:

- **Open at Microsoft**: Uma breve introdução de 18 minutos e guia rápido de como usar o Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.br.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contribuindo

Este projeto recebe contribuições e sugestões de braços abertos. Interessado em contribuir com o Azure Co-op Translator? Veja nosso [CONTRIBUTING.md](./CONTRIBUTING.md) para orientações de como você pode ajudar a tornar o Co-op Translator mais acessível.

## Contribuidores

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Código de Conduta

Este projeto adotou o [Código de Conduta de Código Aberto da Microsoft](https://opensource.microsoft.com/codeofconduct/).
Para mais informações, veja o [FAQ do Código de Conduta](https://opensource.microsoft.com/codeofconduct/faq/) ou
entre em contato pelo [opencode@microsoft.com](mailto:opencode@microsoft.com) para dúvidas ou comentários adicionais.

## IA Responsável

A Microsoft está comprometida em ajudar nossos clientes a usar nossos produtos de IA de forma responsável, compartilhando nossos aprendizados e construindo parcerias baseadas em confiança por meio de ferramentas como Transparency Notes e Impact Assessments. Muitos desses recursos podem ser encontrados em [https://aka.ms/RAI](https://aka.ms/RAI).
A abordagem da Microsoft para IA responsável é baseada em nossos princípios de IA: justiça, confiabilidade e segurança, privacidade e proteção, inclusão, transparência e responsabilidade.

Modelos de linguagem, imagem e fala em larga escala – como os usados neste exemplo – podem se comportar de maneiras injustas, não confiáveis ou ofensivas, podendo causar danos. Consulte a [nota de transparência do serviço Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) para se informar sobre riscos e limitações.

A abordagem recomendada para mitigar esses riscos é incluir um sistema de segurança na sua arquitetura que possa detectar e prevenir comportamentos prejudiciais. O [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) oferece uma camada independente de proteção, capaz de detectar conteúdo prejudicial gerado por usuários e por IA em aplicativos e serviços. O Azure AI Content Safety inclui APIs de texto e imagem que permitem detectar material nocivo. Também temos o Content Safety Studio interativo, que permite visualizar, explorar e testar exemplos de código para detectar conteúdo prejudicial em diferentes modalidades. A seguinte [documentação de início rápido](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) orienta você sobre como fazer requisições ao serviço.
Outro aspecto a ser considerado é o desempenho geral do aplicativo. Em aplicações multimodais e com múltiplos modelos, consideramos desempenho como a capacidade do sistema de funcionar conforme você e seus usuários esperam, incluindo não gerar resultados prejudiciais. É importante avaliar o desempenho do seu aplicativo como um todo usando [métricas de qualidade de geração, risco e segurança](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Você pode avaliar seu aplicativo de IA no ambiente de desenvolvimento usando o [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Com um conjunto de dados de teste ou um alvo definido, as gerações do seu aplicativo de IA generativa são medidas quantitativamente com avaliadores integrados ou personalizados, conforme sua escolha. Para começar a usar o prompt flow sdk para avaliar seu sistema, siga o [guia de início rápido](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Depois de executar uma avaliação, você pode [visualizar os resultados no Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marcas Registradas

Este projeto pode conter marcas registradas ou logotipos de projetos, produtos ou serviços. O uso autorizado de marcas registradas ou logotipos da Microsoft está sujeito e deve seguir as [Diretrizes de Marca Registrada e Marca da Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). O uso de marcas registradas ou logotipos da Microsoft em versões modificadas deste projeto não deve causar confusão ou sugerir patrocínio da Microsoft. Qualquer uso de marcas registradas ou logotipos de terceiros está sujeito às políticas desses terceiros.

## Obtendo Ajuda

Se você tiver dúvidas ou dificuldades ao criar aplicativos de IA, participe:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Se você tiver feedback sobre o produto ou encontrar erros durante o desenvolvimento, acesse:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.