<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:04:30+00:00",
  "source_file": "README.md",
  "language_code": "it"
}
-->
# Co-op Translator

_Automatizza facilmente la traduzione dei tuoi contenuti educativi su GitHub in più lingue per raggiungere un pubblico globale._

[![Pacchetto Python](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Licenza: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Download](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Download](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Stile del codice: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Contributori GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![Problemi GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![Pull-request GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Supporto multilingue

#### Supportato da [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabo](../ar/README.md) | [Bengalese](../bn/README.md) | [Bulgaro](../bg/README.md) | [Birmano (Myanmar)](../my/README.md) | [Cinese (Semplificato)](../zh/README.md) | [Cinese (Tradizionale, Hong Kong)](../hk/README.md) | [Cinese (Tradizionale, Macao)](../mo/README.md) | [Cinese (Tradizionale, Taiwan)](../tw/README.md) | [Croato](../hr/README.md) | [Ceco](../cs/README.md) | [Danese](../da/README.md) | [Olandese](../nl/README.md) | [Estone](../et/README.md) | [Finlandese](../fi/README.md) | [Francese](../fr/README.md) | [Tedesco](../de/README.md) | [Greco](../el/README.md) | [Ebraico](../he/README.md) | [Hindi](../hi/README.md) | [Ungherese](../hu/README.md) | [Indonesiano](../id/README.md) | [Italiano](./README.md) | [Giapponese](../ja/README.md) | [Coreano](../ko/README.md) | [Lituano](../lt/README.md) | [Malese](../ms/README.md) | [Marathi](../mr/README.md) | [Nepalese](../ne/README.md) | [Norvegese](../no/README.md) | [Persiano (Farsi)](../fa/README.md) | [Polacco](../pl/README.md) | [Portoghese (Brasile)](../br/README.md) | [Portoghese (Portogallo)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romeno](../ro/README.md) | [Russo](../ru/README.md) | [Serbo (Cirillico)](../sr/README.md) | [Slovacco](../sk/README.md) | [Sloveno](../sl/README.md) | [Spagnolo](../es/README.md) | [Swahili](../sw/README.md) | [Svedese](../sv/README.md) | [Tagalog (Filippino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thailandese](../th/README.md) | [Turco](../tr/README.md) | [Ucraino](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamita](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![Osservatori GitHub](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![Fork GitHub](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![Stelle GitHub](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Apri in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Panoramica

**Co-op Translator** ti permette di tradurre rapidamente i tuoi contenuti educativi su GitHub in diverse lingue, raggiungendo facilmente utenti da tutto il mondo. Quando aggiorni i tuoi file Markdown, immagini o notebook Jupyter, le traduzioni vengono sincronizzate automaticamente per mantenere i tuoi contenuti sempre aggiornati e rilevanti per gli utenti internazionali.

Ecco come Co-op Translator organizza i contenuti educativi tradotti su GitHub:

![Esempio](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.it.png)

## Avvio rapido

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

## Configurazione minima

- Crea un file `.env` usando il template: [.env.template](../../.env.template)
- Configura un provider LLM (Azure OpenAI o OpenAI)
- Per la traduzione delle immagini (`-img`), configura anche Azure AI Vision
- Consigliato: Se hai traduzioni generate da altri strumenti, puliscile prima per evitare conflitti (ad esempio: `translations/`).
- Consigliato: Aggiungi una sezione traduzioni al tuo README usando il [template lingue README](./README_languages_template.md)
- Vedi: [Configura Azure AI](./getting_started/set-up-azure-ai.md)

## Utilizzo

Traduci tutti i tipi supportati:

```bash
translate -l "ko ja"
```

Solo Markdown:

```bash
translate -l "de" -md
```

Markdown + immagini:

```bash
translate -l "pt" -md -img
```

Solo notebook:

```bash
translate -l "zh" -nb
```

Altre opzioni: [Riferimento comandi](./getting_started/command-reference.md)

## Funzionalità

- Traduzione automatica di Markdown, notebook e immagini
- Mantiene le traduzioni sincronizzate con le modifiche alla fonte
- Funziona in locale (CLI) o in CI (GitHub Actions)
- Utilizza Azure OpenAI o OpenAI; opzionale Azure AI Vision per le immagini
- Mantiene la formattazione e la struttura Markdown

## Documentazione

- [Guida da riga di comando](./getting_started/command-line-guide/command-line-guide.md)
- [Guida GitHub Actions (Repository pubblici & segreti standard)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Guida GitHub Actions (Repository Microsoft & configurazioni a livello di organizzazione)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Lingue supportate](./getting_started/supported-languages.md)
- [Risoluzione dei problemi](./getting_started/troubleshooting.md)

## Sostienici e promuovi l'apprendimento globale

Unisciti a noi per rivoluzionare la condivisione dei contenuti educativi nel mondo! Dai una ⭐ a [Co-op Translator](https://github.com/azure/co-op-translator) su GitHub e sostieni la nostra missione di abbattere le barriere linguistiche nell'apprendimento e nella tecnologia. Il tuo interesse e i tuoi contributi fanno davvero la differenza! Sono sempre benvenuti suggerimenti e contributi al codice.

### Esplora i contenuti educativi Microsoft nella tua lingua

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

## Presentazioni video

Scopri di più su Co-op Translator attraverso le nostre presentazioni _(Clicca sull'immagine qui sotto per guardare su YouTube.)_:

- **Open at Microsoft**: Una breve introduzione di 18 minuti e guida rapida su come usare Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.it.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contribuire

Questo progetto accoglie con piacere contributi e suggerimenti. Vuoi contribuire ad Azure Co-op Translator? Consulta il nostro [CONTRIBUTING.md](./CONTRIBUTING.md) per le linee guida su come rendere Co-op Translator più accessibile.

## Contributori

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Codice di condotta

Questo progetto adotta il [Codice di condotta Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/).
Per maggiori informazioni consulta le [FAQ sul Codice di condotta](https://opensource.microsoft.com/codeofconduct/faq/) oppure
contatta [opencode@microsoft.com](mailto:opencode@microsoft.com) per domande o commenti aggiuntivi.

## AI responsabile

Microsoft si impegna ad aiutare i propri clienti a utilizzare i prodotti AI in modo responsabile, condividendo le proprie esperienze e costruendo partnership basate sulla fiducia tramite strumenti come Transparency Notes e Impact Assessments. Molte di queste risorse sono disponibili su [https://aka.ms/RAI](https://aka.ms/RAI).
L'approccio di Microsoft all'AI responsabile si basa sui principi di equità, affidabilità e sicurezza, privacy e protezione, inclusività, trasparenza e responsabilità.

I modelli su larga scala di linguaggio naturale, immagini e voce – come quelli usati in questo esempio – possono talvolta comportarsi in modo non equo, inaffidabile o offensivo, causando potenziali danni. Consulta la [Transparency note del servizio Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) per essere informato su rischi e limitazioni.

Il modo consigliato per mitigare questi rischi è includere un sistema di sicurezza nell'architettura che possa rilevare e prevenire comportamenti dannosi. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) offre un livello di protezione indipendente, in grado di rilevare contenuti dannosi generati da utenti e AI in applicazioni e servizi. Azure AI Content Safety include API per testo e immagini che permettono di individuare materiale dannoso. Abbiamo anche un Content Safety Studio interattivo che consente di visualizzare, esplorare e provare codice di esempio per rilevare contenuti dannosi in diverse modalità. La seguente [documentazione di avvio rapido](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ti guida nella richiesta al servizio.


Un altro aspetto da considerare è la performance complessiva dell'applicazione. Con applicazioni multi-modali e multi-modello, per performance si intende che il sistema si comporti come tu e i tuoi utenti vi aspettate, incluso il fatto di non generare output dannosi. È importante valutare le prestazioni della tua applicazione nel suo insieme utilizzando le [metriche di qualità della generazione, rischio e sicurezza](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Puoi valutare la tua applicazione AI nell'ambiente di sviluppo usando il [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Fornendo un dataset di test o un obiettivo, le generazioni della tua applicazione AI generativa vengono misurate quantitativamente con valutatori integrati o personalizzati a tua scelta. Per iniziare a usare il prompt flow sdk per valutare il tuo sistema, puoi seguire la [guida rapida](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Una volta eseguita una valutazione, puoi [visualizzare i risultati in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marchi

Questo progetto può contenere marchi o loghi relativi a progetti, prodotti o servizi. L'uso autorizzato dei marchi o loghi Microsoft è soggetto e deve rispettare le
[Linee guida sui marchi e sul brand di Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
L'utilizzo dei marchi o loghi Microsoft in versioni modificate di questo progetto non deve causare confusione o suggerire una sponsorizzazione da parte di Microsoft.
Qualsiasi utilizzo di marchi o loghi di terze parti è soggetto alle politiche di tali terze parti.

## Assistenza

Se hai difficoltà o domande sulla creazione di app AI, unisciti a:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Se vuoi inviare feedback sul prodotto o riscontri errori durante lo sviluppo, visita:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.