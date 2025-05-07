<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "329abbc9354793ea422f7e7ebf66be2c",
  "translation_date": "2025-05-07T01:54:42+00:00",
  "source_file": "README.md",
  "language_code": "br"
}
-->
![Logo](../../imgs/logo.png)

# Co-op Translator: Automatize a Tradução de Documentação Educacional Sem Esforço

_Automatize facilmente a tradução da sua documentação para múltiplos idiomas e alcance um público global._

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### Suporte de Idiomas com Tecnologia Co-op Translator

[Korean](../ko/README.md) | [Japanese](../ja/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Spanish](../es/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Portuguese (Brazil)](./README.md) | [Hindi](../hi/README.md) | [Russian](../ru/README.md) | [Turkish](../tr/README.md) | [Arabic](../ar/README.md) | [Indonesian](../id/README.md) | [Vietnamese](../vi/README.md)

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
> **Automação Poderosa**: Agora com suporte a GitHub Actions! Traduza automaticamente sua documentação sempre que houver alterações no seu repositório, mantendo tudo atualizado com facilidade. [Saiba mais](../..).

## Modelos e Serviços Suportados

| Tipo                  | Nome                           |
|-----------------------|--------------------------------|
| Language Model        | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| Computer Vision       | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> Se um serviço de visão computacional não estiver disponível, o co-op translator alternará para o [modo somente Markdown](./getting_started/markdown-only-mode.md).

## Visão Geral: Simplifique a Tradução do Seu Conteúdo Educacional

Barreiras linguísticas dificultam significativamente o acesso a recursos educacionais valiosos e conhecimento técnico para aprendizes e desenvolvedores ao redor do mundo. Isso limita a participação e desacelera o ritmo da inovação e aprendizado global.

**Co-op Translator** nasceu da necessidade de resolver o processo manual ineficiente de tradução para a própria série educacional de grande escala da Microsoft (como os guias "Para Iniciantes"). Evoluiu para uma ferramenta fácil de usar e poderosa, criada para derrubar essas barreiras para todos. Ao oferecer traduções automatizadas de alta qualidade via CLI e GitHub Actions, o Co-op Translator capacita educadores, estudantes, pesquisadores e desenvolvedores globalmente a compartilhar e acessar conhecimento sem limitações de idioma.

Veja como o Co-op Translator organiza o conteúdo educacional traduzido:

![Example](../../imgs/translation-ex.png)

Arquivos Markdown e textos de imagens são traduzidos automaticamente e organizados cuidadosamente em pastas específicas por idioma.

**Desbloqueie o acesso global ao seu conteúdo educacional com o Co-op Translator hoje mesmo!**

## Apoio ao Acesso Global para os Recursos de Aprendizado da Microsoft

O Co-op Translator ajuda a superar a barreira do idioma para iniciativas educacionais importantes da Microsoft, automatizando o processo de tradução para repositórios que atendem a uma comunidade global de desenvolvedores. Exemplos que já usam o Co-op Translator incluem:

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## Principais Recursos

- **Traduções Automatizadas**: Traduza textos para vários idiomas com facilidade.
- **Integração com GitHub Actions**: Automatize traduções como parte do seu pipeline CI/CD.
- **Preservação do Markdown**: Mantenha a sintaxe correta do Markdown durante a tradução.
- **Tradução de Texto em Imagens**: Extraia e traduza textos presentes em imagens.
- **Tecnologia Avançada de LLM**: Utilize modelos de linguagem de ponta para traduções de alta qualidade.
- **Integração Fácil**: Integre-se perfeitamente ao seu projeto existente.
- **Simplifique a Localização**: Agilize o processo de localização do seu projeto para mercados internacionais.

## Como Funciona

![Architecture](../../imgs/architecture_241019.png)

O Co-op Translator pega arquivos Markdown e imagens da sua pasta de projeto e processa da seguinte forma:

1. **Extração de Texto**: Extrai texto dos arquivos Markdown e, se configurado (ex: com Azure Computer Vision), também o texto presente nas imagens.
1. **Tradução por IA**: Envia o texto extraído para o LLM configurado (Azure OpenAI, OpenAI, etc.) para tradução.
1. **Salvamento do Resultado**: Salva os arquivos Markdown traduzidos e as imagens (com texto traduzido) em pastas específicas por idioma, preservando a formatação original.

## Começando

Comece rapidamente com a CLI ou configure a automação completa com GitHub Actions.

### Início Rápido: Linha de Comando

Para um início rápido usando a linha de comando:

1. Instale o pacote:
    ```bash
    pip install co-op-translator
    ```
2. Configure as Credenciais:
  - Crie um arquivo `.env` file in your project's root directory.
  - Copy the contents from the [.env.template](../../.env.template) file into your new `.env` file.
  - Fill in the required API keys and endpoint information in your `.env` file.
3. Run Translation:
  - Navigate to your project's root directory in your terminal.
  - Execute the translate command, specifying target languages with the `-l` com a flag:
    ```bash
    translate -l "ko ja fr"
    ```
    *(Substitua `"ko ja fr"` with your desired space-separated language codes)*

### Detailed Usage Guides

Choose the approach that best fits your workflow:

#### 1. Using the Command Line (CLI)

- Best for: One-time translations, manual control, or integration into custom scripts.
- Requires: Local installation of Python and the `co-op-translator` package.
- Guide: [Command Line Guide](./getting_started/command-line-guide/command-line-guide.md)

#### 2. Using GitHub Actions (Automation)

- Best for: Automatically translating content whenever changes are pushed to your repository. Keeps translations consistently up-to-date.
- Requires: Setting up a workflow file (`.github/workflows`) no seu repositório. Nenhuma instalação local é necessária.
- Guias:
  - [Guia GitHub Actions (Repositórios Públicos & Segredos Padrão)](./getting_started/github-actions-guide/github-actions-guide-public.md) - Use este para a maioria dos repositórios públicos ou pessoais que utilizam segredos padrão do repositório.
  - [Guia GitHub Actions (Repositórios da Organização Microsoft & Configurações em Nível de Organização)](./getting_started/github-actions-guide/github-actions-guide-org.md) - Use este guia se você trabalha dentro da organização Microsoft no GitHub ou precisa usar segredos ou runners em nível organizacional.

> [!NOTE]
> Embora este tutorial foque em recursos Azure, você pode usar qualquer modelo de linguagem suportado da lista de [modelos e serviços suportados](../..).

### Solução de Problemas e Dicas

- [Guia de Solução de Problemas](./getting_started/troubleshooting.md)

### Recursos Adicionais

- [Referência de Comandos](./getting_started/command-reference.md): Guia detalhado de todos os comandos e opções disponíveis.
- [Configuração de Suporte Multilíngue](./getting_started/multi-language-support.md): Como adicionar uma tabela com links para versões traduzidas no seu README.
- [Idiomas Suportados](./getting_started/supported-languages.md): Confira a lista de idiomas suportados e instruções para adicionar novos.
- [Modo Somente Markdown](./getting_started/markdown-only-mode.md): Como traduzir apenas o texto, sem tradução de imagens.

## Apresentações em Vídeo

Saiba mais sobre o Co-op Translator através das nossas apresentações _(clique na imagem abaixo para assistir no YouTube)_:

- **Open at Microsoft**: Uma introdução rápida de 18 minutos e guia prático sobre como usar o Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**: Um guia detalhado de uma hora, passo a passo, cobrindo desde o que é o Co-op Translator, configuração da ferramenta, uso eficaz até uma demonstração ao vivo mostrando suas capacidades em ação.

  [![Microsoft Reactor](../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## Apoie-nos e Promova o Aprendizado Global

Junte-se a nós para revolucionar a forma como o conteúdo educacional é compartilhado globalmente! Dê uma ⭐ para o [Co-op Translator](https://github.com/azure/co-op-translator) no GitHub e apoie nossa missão de derrubar barreiras linguísticas no aprendizado e na tecnologia. Seu interesse e contribuições fazem uma grande diferença! Contribuições de código e sugestões de recursos são sempre bem-vindas.

## Contribuindo

Este projeto recebe contribuições e sugestões. Quer contribuir com o Azure Co-op Translator? Consulte nosso [CONTRIBUTING.md](./CONTRIBUTING.md) para orientações sobre como ajudar a tornar o Co-op Translator mais acessível.

## Colaboradores

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Código de Conduta

Este projeto adotou o [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Para mais informações, veja o [FAQ do Código de Conduta](https://opensource.microsoft.com/codeofconduct/faq/) ou
entre em contato pelo email [opencode@microsoft.com](mailto:opencode@microsoft.com) para dúvidas ou comentários adicionais.

## IA Responsável

A Microsoft está comprometida em ajudar nossos clientes a usar nossos produtos de IA de forma responsável, compartilhando aprendizados e construindo parcerias baseadas na confiança por meio de ferramentas como Transparency Notes e Impact Assessments. Muitos desses recursos podem ser encontrados em [https://aka.ms/RAI](https://aka.ms/RAI).
A abordagem da Microsoft para IA responsável se baseia em nossos princípios de IA: justiça, confiabilidade e segurança, privacidade e segurança, inclusão, transparência e responsabilidade.

Modelos de linguagem, imagem e voz em larga escala — como os usados neste exemplo — podem eventualmente apresentar comportamentos injustos, não confiáveis ou ofensivos, causando danos. Consulte a [Transparency note do serviço Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) para se informar sobre riscos e limitações.
A abordagem recomendada para mitigar esses riscos é incluir um sistema de segurança na sua arquitetura que possa detectar e prevenir comportamentos nocivos. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) oferece uma camada independente de proteção, capaz de identificar conteúdos nocivos gerados por usuários e por IA em aplicações e serviços. O Azure AI Content Safety inclui APIs de texto e imagem que permitem detectar material prejudicial. Também dispomos de um Content Safety Studio interativo que permite visualizar, explorar e testar exemplos de código para detectar conteúdo nocivo em diferentes modalidades. A seguinte [documentação de início rápido](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) orienta você a fazer requisições ao serviço.

Outro aspecto a considerar é o desempenho geral da aplicação. Em aplicações multimodais e multimodelos, consideramos desempenho como a capacidade do sistema de funcionar conforme esperado por você e seus usuários, incluindo não gerar saídas nocivas. É importante avaliar o desempenho da sua aplicação como um todo utilizando [métricas de qualidade de geração e de risco e segurança](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Você pode avaliar sua aplicação de IA no ambiente de desenvolvimento usando o [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Dado um conjunto de dados de teste ou um objetivo, as gerações da sua aplicação de IA generativa são medidas quantitativamente com avaliadores integrados ou avaliadores personalizados de sua escolha. Para começar a usar o prompt flow sdk para avaliar seu sistema, você pode seguir o [guia de início rápido](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Depois de executar uma avaliação, você pode [visualizar os resultados no Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Trademarks

Este projeto pode conter marcas registradas ou logos de projetos, produtos ou serviços. O uso autorizado das marcas registradas ou logos da Microsoft está sujeito e deve seguir as [Diretrizes de Marca e Trademark da Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). O uso das marcas registradas ou logos da Microsoft em versões modificadas deste projeto não deve causar confusão nem implicar patrocínio da Microsoft. Qualquer uso de marcas registradas ou logos de terceiros está sujeito às políticas desses terceiros.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.