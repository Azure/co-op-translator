<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T02:59:33+00:00",
  "source_file": "README.md",
  "language_code": "pt"
}
-->
# Co-op Translator

_Automaticamente traduza o seu conteúdo educativo do GitHub para várias línguas e chegue a uma audiência global._

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Suporte Multi-Língua

#### Suportado por [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Árabe](../ar/README.md) | [Bengali](../bn/README.md) | [Búlgaro](../bg/README.md) | [Birmanês (Myanmar)](../my/README.md) | [Chinês (Simplificado)](../zh/README.md) | [Chinês (Tradicional, Hong Kong)](../hk/README.md) | [Chinês (Tradicional, Macau)](../mo/README.md) | [Chinês (Tradicional, Taiwan)](../tw/README.md) | [Croata](../hr/README.md) | [Checo](../cs/README.md) | [Dinamarquês](../da/README.md) | [Holandês](../nl/README.md) | [Estónio](../et/README.md) | [Finlandês](../fi/README.md) | [Francês](../fr/README.md) | [Alemão](../de/README.md) | [Grego](../el/README.md) | [Hebraico](../he/README.md) | [Hindi](../hi/README.md) | [Húngaro](../hu/README.md) | [Indonésio](../id/README.md) | [Italiano](../it/README.md) | [Japonês](../ja/README.md) | [Coreano](../ko/README.md) | [Lituano](../lt/README.md) | [Malaio](../ms/README.md) | [Marata](../mr/README.md) | [Nepalês](../ne/README.md) | [Norueguês](../no/README.md) | [Persa (Farsi)](../fa/README.md) | [Polaco](../pl/README.md) | [Português (Brasil)](../br/README.md) | [Português (Portugal)](./README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romeno](../ro/README.md) | [Russo](../ru/README.md) | [Sérvio (Cirílico)](../sr/README.md) | [Eslovaco](../sk/README.md) | [Esloveno](../sl/README.md) | [Espanhol](../es/README.md) | [Suaíli](../sw/README.md) | [Sueco](../sv/README.md) | [Tagalo (Filipino)](../tl/README.md) | [Tâmil](../ta/README.md) | [Tailandês](../th/README.md) | [Turco](../tr/README.md) | [Ucraniano](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamita](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Visão geral

O **Co-op Translator** permite-lhe traduzir rapidamente o seu conteúdo educativo do GitHub para várias línguas, alcançando facilmente uma audiência global. Sempre que atualizar os seus ficheiros Markdown, imagens ou notebooks Jupyter, as traduções são automaticamente sincronizadas para garantir que o seu conteúdo educativo no GitHub se mantém atualizado e relevante para utilizadores internacionais.

Veja como o Co-op Translator organiza o conteúdo educativo traduzido no GitHub:

![Exemplo](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.pt.png)

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

- Crie um ficheiro `.env` usando o modelo: [.env.template](../../.env.template)
- Configure um fornecedor LLM (Azure OpenAI ou OpenAI)
- Para tradução de imagens (`-img`), configure também o Azure AI Vision
- Recomendado: Se já tem traduções geradas por outras ferramentas, limpe-as primeiro para evitar conflitos (por exemplo: `translations/`).
- Recomendado: Adicione uma secção de traduções ao seu README usando o [modelo de línguas para README](./README_languages_template.md)
- Veja: [Configurar Azure AI](./getting_started/set-up-azure-ai.md)

## Utilização

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

- Tradução automática de Markdown, notebooks e imagens
- Mantém as traduções sincronizadas com as alterações da fonte
- Funciona localmente (CLI) ou em CI (GitHub Actions)
- Utiliza Azure OpenAI ou OpenAI; Azure AI Vision opcional para imagens
- Preserva a formatação e estrutura do Markdown

## Documentação

- [Guia de linha de comandos](./getting_started/command-line-guide/command-line-guide.md)
- [Guia GitHub Actions (Repositórios públicos & segredos padrão)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Guia GitHub Actions (Repositórios de organizações Microsoft & configurações a nível de organização)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Línguas suportadas](./getting_started/supported-languages.md)
- [Resolução de problemas](./getting_started/troubleshooting.md)

## Apoie-nos e Promova a Aprendizagem Global

Junte-se a nós na revolução da partilha de conteúdo educativo a nível global! Dê uma ⭐ ao [Co-op Translator](https://github.com/azure/co-op-translator) no GitHub e apoie a nossa missão de eliminar barreiras linguísticas na aprendizagem e tecnologia. O seu interesse e contributos fazem toda a diferença! Contribuições de código e sugestões de funcionalidades são sempre bem-vindas.

### Explore conteúdo educativo da Microsoft na sua língua

- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Apresentações em Vídeo

Saiba mais sobre o Co-op Translator através das nossas apresentações _(Clique na imagem abaixo para ver no YouTube.)_:

- **Open at Microsoft**: Uma breve introdução de 18 minutos e um guia rápido sobre como usar o Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.pt.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contribuir

Este projeto aceita contribuições e sugestões. Interessado em contribuir para o Azure Co-op Translator? Consulte o nosso [CONTRIBUTING.md](./CONTRIBUTING.md) para saber como pode ajudar a tornar o Co-op Translator mais acessível.

## Contribuidores

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Código de Conduta

Este projeto adotou o [Código de Conduta de Open Source da Microsoft](https://opensource.microsoft.com/codeofconduct/).
Para mais informações, consulte as [Perguntas Frequentes sobre o Código de Conduta](https://opensource.microsoft.com/codeofconduct/faq/) ou
contacte [opencode@microsoft.com](mailto:opencode@microsoft.com) para quaisquer questões ou comentários adicionais.

## IA Responsável

A Microsoft está empenhada em ajudar os nossos clientes a usar os nossos produtos de IA de forma responsável, partilhando o que aprendemos e construindo parcerias baseadas na confiança através de ferramentas como Transparency Notes e Impact Assessments. Muitos destes recursos podem ser encontrados em [https://aka.ms/RAI](https://aka.ms/RAI).
A abordagem da Microsoft à IA responsável baseia-se nos nossos princípios de justiça, fiabilidade e segurança, privacidade e segurança, inclusão, transparência e responsabilidade.

Modelos de linguagem natural, imagem e voz em grande escala – como os utilizados neste exemplo – podem, por vezes, comportar-se de forma injusta, pouco fiável ou ofensiva, podendo causar danos. Consulte a [nota de transparência do serviço Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) para estar informado sobre riscos e limitações.

A abordagem recomendada para mitigar estes riscos é incluir um sistema de segurança na sua arquitetura que possa detetar e prevenir comportamentos prejudiciais. O [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) fornece uma camada independente de proteção, capaz de detetar conteúdo prejudicial gerado por utilizadores ou por IA em aplicações e serviços. O Azure AI Content Safety inclui APIs de texto e imagem que permitem detetar material prejudicial. Também temos um Content Safety Studio interativo que permite visualizar, explorar e experimentar código de exemplo para detetar conteúdo prejudicial em diferentes modalidades. A seguinte [documentação de início rápido](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) guia-o no envio de pedidos ao serviço.
Outro aspeto a ter em conta é o desempenho geral da aplicação. Em aplicações multi-modais e multi-modelos, consideramos desempenho como sendo o sistema funcionar conforme esperado por si e pelos seus utilizadores, incluindo não gerar resultados prejudiciais. É importante avaliar o desempenho da sua aplicação global utilizando [métricas de qualidade de geração, risco e segurança](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Pode avaliar a sua aplicação de IA no ambiente de desenvolvimento utilizando o [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Dado um conjunto de dados de teste ou um alvo, as gerações da sua aplicação de IA generativa são medidas quantitativamente com avaliadores incorporados ou avaliadores personalizados à sua escolha. Para começar a usar o prompt flow sdk para avaliar o seu sistema, pode seguir o [guia de introdução](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Depois de executar uma avaliação, pode [visualizar os resultados no Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marcas registadas

Este projeto pode conter marcas registadas ou logótipos de projetos, produtos ou serviços. A utilização autorizada de marcas registadas ou logótipos da Microsoft está sujeita e deve cumprir as
[Diretrizes de Marcas e Imagem da Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
A utilização de marcas registadas ou logótipos da Microsoft em versões modificadas deste projeto não deve causar confusão nem sugerir patrocínio da Microsoft.
Qualquer utilização de marcas registadas ou logótipos de terceiros está sujeita às políticas desses terceiros.

## Obter Ajuda

Se tiver dificuldades ou dúvidas sobre como criar aplicações de IA, junte-se a:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Se tiver feedback sobre o produto ou encontrar erros durante o desenvolvimento, visite:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original, na sua língua nativa, deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.