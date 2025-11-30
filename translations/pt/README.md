<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T10:51:38+00:00",
  "source_file": "README.md",
  "language_code": "pt"
}
-->
# Co-op Translator

_Automatize facilmente a tradução do seu conteúdo educativo no GitHub para múltiplas línguas e alcance um público global._

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

### 🌐 Suporte Multilíngue

#### Suportado pelo [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Árabe](../ar/README.md) | [Bengali](../bn/README.md) | [Búlgaro](../bg/README.md) | [Birmanês (Myanmar)](../my/README.md) | [Chinês (Simplificado)](../zh/README.md) | [Chinês (Tradicional, Hong Kong)](../hk/README.md) | [Chinês (Tradicional, Macau)](../mo/README.md) | [Chinês (Tradicional, Taiwan)](../tw/README.md) | [Croata](../hr/README.md) | [Checo](../cs/README.md) | [Dinamarquês](../da/README.md) | [Holandês](../nl/README.md) | [Estónio](../et/README.md) | [Finlandês](../fi/README.md) | [Francês](../fr/README.md) | [Alemão](../de/README.md) | [Grego](../el/README.md) | [Hebraico](../he/README.md) | [Hindi](../hi/README.md) | [Húngaro](../hu/README.md) | [Indonésio](../id/README.md) | [Italiano](../it/README.md) | [Japonês](../ja/README.md) | [Kannada](../kn/README.md) | [Coreano](../ko/README.md) | [Lituano](../lt/README.md) | [Malaio](../ms/README.md) | [Malaiala](../ml/README.md) | [Marata](../mr/README.md) | [Nepali](../ne/README.md) | [Pidgin Nigeriano](../pcm/README.md) | [Norueguês](../no/README.md) | [Persa (Farsi)](../fa/README.md) | [Polaco](../pl/README.md) | [Português (Brasil)](../br/README.md) | [Português (Portugal)](./README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romeno](../ro/README.md) | [Russo](../ru/README.md) | [Sérvio (Cirílico)](../sr/README.md) | [Eslovaco](../sk/README.md) | [Esloveno](../sl/README.md) | [Espanhol](../es/README.md) | [Suaíli](../sw/README.md) | [Sueco](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Tailandês](../th/README.md) | [Turco](../tr/README.md) | [Ucraniano](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamita](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Visão Geral

**Co-op Translator** ajuda a localizar o seu conteúdo educativo no GitHub em várias línguas de forma simples.
Quando atualiza os seus ficheiros Markdown, imagens ou notebooks, as traduções mantêm-se automaticamente sincronizadas, garantindo que o seu conteúdo está sempre correto e atualizado para aprendizes em todo o mundo.

Exemplo de como o conteúdo traduzido é organizado:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.pt.png)

## Início rápido

```bash
# Criar e ativar um ambiente virtual (recomendado)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Instalar o pacote
pip install co-op-translator
# Traduzir
translate -l "ko ja fr" -md
```

Docker:

```bash
# Puxe a imagem pública do GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Execute com a pasta atual montada e .env fornecido (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Configuração mínima

1. Crie um ficheiro `.env` usando o modelo: [.env.template](../../.env.template)
2. Configure um fornecedor LLM (Azure OpenAI ou OpenAI)
3. (Opcional) Para tradução de imagens (`-img`), configure o Azure AI Vision
4. (Recomendado) Limpe quaisquer traduções anteriores para evitar conflitos (ex.: `translations/`)
5. (Recomendado) Adicione uma secção de tradução ao seu README usando o [modelo de línguas para README](./getting_started/README_languages_template.md)
6. Veja: [Configurar Azure AI](./getting_started/set-up-azure-ai.md)

## Utilização

Traduza todos os tipos suportados:

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

Mais flags: [Referência de comandos](./getting_started/command-reference.md)

## Funcionalidades

- Tradução automática para Markdown, notebooks e imagens
- Mantém as traduções sincronizadas com as alterações na origem
- Funciona localmente (CLI) ou em CI (GitHub Actions)
- Usa Azure OpenAI ou OpenAI; Azure AI Vision opcional para imagens
- Preserva a formatação e estrutura do Markdown

## Documentação

- [Guia da linha de comandos](./getting_started/command-line-guide/command-line-guide.md)
- [Guia GitHub Actions (repositórios públicos & segredos padrão)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Guia GitHub Actions (repositórios da organização Microsoft & configurações a nível de organização)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Modelo de línguas para README](./getting_started/README_languages_template.md)
- [Línguas suportadas](./getting_started/supported-languages.md)
- [Contribuir](./CONTRIBUTING.md)
- [Resolução de problemas](./getting_started/troubleshooting.md)

### Guia específico Microsoft
> [!NOTE]
> Apenas para mantenedores dos repositórios “For Beginners” da Microsoft.

- [Atualizar a lista de “outros cursos” (apenas para repositórios MS Beginners)](./getting_started/update-other-courses.md)

## Apoie-nos e promova a aprendizagem global

Junte-se a nós para revolucionar a forma como o conteúdo educativo é partilhado globalmente! Dê uma ⭐ ao [Co-op Translator](https://github.com/azure/co-op-translator) no GitHub e apoie a nossa missão de derrubar barreiras linguísticas na aprendizagem e tecnologia. O seu interesse e contribuições fazem uma grande diferença! Contribuições de código e sugestões de funcionalidades são sempre bem-vindas.

### Explore conteúdo educativo Microsoft na sua língua

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

👉 Clique na imagem abaixo para assistir no YouTube.

- **Open at Microsoft**: Uma breve introdução de 18 minutos e guia rápido sobre como usar o Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.pt.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contribuir

Este projeto aceita contribuições e sugestões. Quer contribuir para o Azure Co-op Translator? Por favor, consulte o nosso [CONTRIBUTING.md](./CONTRIBUTING.md) para orientações sobre como pode ajudar a tornar o Co-op Translator mais acessível.

## Contribuidores

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Código de Conduta

Este projeto adotou o [Código de Conduta Open Source da Microsoft](https://opensource.microsoft.com/codeofconduct/).
Para mais informações, consulte as [FAQ do Código de Conduta](https://opensource.microsoft.com/codeofconduct/faq/) ou
contacte [opencode@microsoft.com](mailto:opencode@microsoft.com) para quaisquer dúvidas ou comentários adicionais.

## IA Responsável

A Microsoft está comprometida em ajudar os seus clientes a usar os nossos produtos de IA de forma responsável, partilhando as nossas aprendizagens e construindo parcerias baseadas na confiança através de ferramentas como Notas de Transparência e Avaliações de Impacto. Muitos destes recursos podem ser encontrados em [https://aka.ms/RAI](https://aka.ms/RAI).
A abordagem da Microsoft à IA responsável baseia-se nos nossos princípios de IA: justiça, fiabilidade e segurança, privacidade e segurança, inclusão, transparência e responsabilidade.

Modelos de larga escala para linguagem natural, imagem e voz — como os usados neste exemplo — podem comportar-se de formas injustas, pouco fiáveis ou ofensivas, causando danos. Por favor, consulte a [nota de transparência do serviço Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) para estar informado sobre riscos e limitações.
A abordagem recomendada para mitigar estes riscos é incluir um sistema de segurança na sua arquitetura que possa detetar e prevenir comportamentos prejudiciais. O [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) fornece uma camada independente de proteção, capaz de detetar conteúdos prejudiciais gerados por utilizadores e por IA em aplicações e serviços. O Azure AI Content Safety inclui APIs de texto e imagem que permitem detetar material prejudicial. Também dispomos de um Content Safety Studio interativo que permite visualizar, explorar e experimentar código de exemplo para detetar conteúdos prejudiciais em diferentes modalidades. A seguinte [documentação de início rápido](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) orienta-o na realização de pedidos ao serviço.

Outro aspeto a ter em conta é o desempenho geral da aplicação. Em aplicações multimodais e com múltiplos modelos, consideramos desempenho como o facto do sistema funcionar conforme o esperado por si e pelos seus utilizadores, incluindo não gerar resultados prejudiciais. É importante avaliar o desempenho da sua aplicação global utilizando [métricas de qualidade de geração e de risco e segurança](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Pode avaliar a sua aplicação de IA no seu ambiente de desenvolvimento usando o [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Dado um conjunto de dados de teste ou um objetivo, as gerações da sua aplicação de IA generativa são medidas quantitativamente com avaliadores incorporados ou avaliadores personalizados à sua escolha. Para começar a usar o prompt flow sdk para avaliar o seu sistema, pode seguir o [guia de início rápido](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Depois de executar uma avaliação, pode [visualizar os resultados no Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marcas Registadas

Este projeto pode conter marcas registadas ou logótipos de projetos, produtos ou serviços. O uso autorizado das marcas ou logótipos da Microsoft está sujeito e deve seguir as [Diretrizes de Marcas e Identidade da Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).  
O uso de marcas ou logótipos da Microsoft em versões modificadas deste projeto não deve causar confusão nem implicar patrocínio da Microsoft.  
Qualquer uso de marcas ou logótipos de terceiros está sujeito às políticas desses terceiros.

## Obter Ajuda

Se ficar bloqueado ou tiver dúvidas sobre como criar aplicações de IA, junte-se a:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Se tiver feedback sobre o produto ou encontrar erros durante o desenvolvimento, visite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->