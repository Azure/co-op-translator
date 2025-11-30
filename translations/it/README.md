<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T10:58:57+00:00",
  "source_file": "README.md",
  "language_code": "it"
}
-->
# Co-op Translator

_Automatizza facilmente la traduzione dei tuoi contenuti educativi su GitHub in più lingue per raggiungere un pubblico globale._

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

### 🌐 Supporto Multilingue

#### Supportato da [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabo](../ar/README.md) | [Bengalese](../bn/README.md) | [Bulgaro](../bg/README.md) | [Birmano (Myanmar)](../my/README.md) | [Cinese (semplificato)](../zh/README.md) | [Cinese (tradizionale, Hong Kong)](../hk/README.md) | [Cinese (tradizionale, Macao)](../mo/README.md) | [Cinese (tradizionale, Taiwan)](../tw/README.md) | [Croato](../hr/README.md) | [Ceco](../cs/README.md) | [Danese](../da/README.md) | [Olandese](../nl/README.md) | [Estone](../et/README.md) | [Finlandese](../fi/README.md) | [Francese](../fr/README.md) | [Tedesco](../de/README.md) | [Greco](../el/README.md) | [Ebraico](../he/README.md) | [Hindi](../hi/README.md) | [Ungherese](../hu/README.md) | [Indonesiano](../id/README.md) | [Italiano](./README.md) | [Giapponese](../ja/README.md) | [Kannada](../kn/README.md) | [Coreano](../ko/README.md) | [Lituano](../lt/README.md) | [Malese](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalese](../ne/README.md) | [Pidgin Nigeriano](../pcm/README.md) | [Norvegese](../no/README.md) | [Persiano (Farsi)](../fa/README.md) | [Polacco](../pl/README.md) | [Portoghese (Brasile)](../br/README.md) | [Portoghese (Portogallo)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumeno](../ro/README.md) | [Russo](../ru/README.md) | [Serbo (Cirillico)](../sr/README.md) | [Slovacco](../sk/README.md) | [Sloveno](../sl/README.md) | [Spagnolo](../es/README.md) | [Swahili](../sw/README.md) | [Svedese](../sv/README.md) | [Tagalog (Filippino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thailandese](../th/README.md) | [Turco](../tr/README.md) | [Ucraino](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamita](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Panoramica

**Co-op Translator** ti aiuta a localizzare i tuoi contenuti educativi su GitHub in più lingue senza sforzo.
Quando aggiorni i tuoi file Markdown, immagini o notebook, le traduzioni si sincronizzano automaticamente, garantendo che i tuoi contenuti rimangano precisi e aggiornati per gli studenti di tutto il mondo.

Esempio di come è organizzato il contenuto tradotto:

![Esempio](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.it.png)

## Avvio rapido

```bash
# Crea e attiva un ambiente virtuale (consigliato)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Installa il pacchetto
pip install co-op-translator
# Traduci
translate -l "ko ja fr" -md
```

Docker:

```bash
# Estrai l'immagine pubblica da GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Esegui con la cartella corrente montata e .env fornito (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Configurazione minima

1. Crea un file `.env` usando il modello: [.env.template](../../.env.template)
2. Configura un provider LLM (Azure OpenAI o OpenAI)
3. (Opzionale) Per la traduzione delle immagini (`-img`), configura Azure AI Vision
4. (Consigliato) Pulisci eventuali traduzioni precedenti per evitare conflitti (es. `translations/`)
5. (Consigliato) Aggiungi una sezione di traduzione al tuo README usando il [modello per lingue README](./getting_started/README_languages_template.md)
6. Consulta: [Configura Azure AI](./getting_started/set-up-azure-ai.md)

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

Altri flag: [Riferimento comandi](./getting_started/command-reference.md)

## Funzionalità

- Traduzione automatica per Markdown, notebook e immagini
- Mantiene le traduzioni sincronizzate con le modifiche alla sorgente
- Funziona localmente (CLI) o in CI (GitHub Actions)
- Usa Azure OpenAI o OpenAI; opzionale Azure AI Vision per le immagini
- Preserva la formattazione e la struttura Markdown

## Documentazione

- [Guida da linea di comando](./getting_started/command-line-guide/command-line-guide.md)
- [Guida GitHub Actions (repository pubblici e segreti standard)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Guida GitHub Actions (repository Microsoft e configurazioni a livello di organizzazione)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Modello lingue README](./getting_started/README_languages_template.md)
- [Lingue supportate](./getting_started/supported-languages.md)
- [Contribuire](./CONTRIBUTING.md)
- [Risoluzione problemi](./getting_started/troubleshooting.md)

### Guida specifica Microsoft
> [!NOTE]
> Solo per i manutentori dei repository Microsoft “For Beginners”.

- [Aggiornare la lista “altri corsi” (solo per repository MS Beginners)](./getting_started/update-other-courses.md)

## Supportaci e promuovi l’apprendimento globale

Unisciti a noi nella rivoluzione del modo in cui i contenuti educativi vengono condivisi a livello globale! Dai una ⭐ a [Co-op Translator](https://github.com/azure/co-op-translator) su GitHub e sostieni la nostra missione di abbattere le barriere linguistiche nell’apprendimento e nella tecnologia. Il tuo interesse e i tuoi contributi fanno la differenza! Contributi di codice e suggerimenti per nuove funzionalità sono sempre benvenuti.

### Esplora i contenuti educativi Microsoft nella tua lingua

- [AZD per principianti](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI per principianti](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) per principianti](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents per principianti](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI per principianti con .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI per principianti](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI per principianti con Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML per principianti](https://aka.ms/ml-beginners)
- [Data Science per principianti](https://aka.ms/datascience-beginners)
- [AI per principianti](https://aka.ms/ai-beginners)
- [Cybersecurity per principianti](https://github.com/microsoft/Security-101)
- [Sviluppo Web per principianti](https://aka.ms/webdev-beginners)
- [IoT per principianti](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Presentazioni video

👉 Clicca sull’immagine qui sotto per guardare su YouTube.

- **Open at Microsoft**: Una breve introduzione di 18 minuti e una guida rapida su come usare Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.it.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contribuire

Questo progetto accoglie contributi e suggerimenti. Sei interessato a contribuire a Azure Co-op Translator? Consulta il nostro [CONTRIBUTING.md](./CONTRIBUTING.md) per le linee guida su come aiutare a rendere Co-op Translator più accessibile.

## Collaboratori

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Codice di condotta

Questo progetto ha adottato il [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Per maggiori informazioni consulta le [FAQ sul Codice di Condotta](https://opensource.microsoft.com/codeofconduct/faq/) o
contatta [opencode@microsoft.com](mailto:opencode@microsoft.com) per domande o commenti aggiuntivi.

## Intelligenza Artificiale Responsabile

Microsoft si impegna ad aiutare i clienti a usare i nostri prodotti di AI in modo responsabile, condividendo le nostre esperienze e costruendo partnership basate sulla fiducia tramite strumenti come le Transparency Notes e le Impact Assessments. Molte di queste risorse sono disponibili su [https://aka.ms/RAI](https://aka.ms/RAI).
L’approccio di Microsoft all’AI responsabile si basa sui nostri principi di equità, affidabilità e sicurezza, privacy e protezione, inclusività, trasparenza e responsabilità.

I modelli su larga scala per linguaggio naturale, immagini e voce - come quelli usati in questo esempio - possono comportarsi in modi non equi, inaffidabili o offensivi, causando potenziali danni. Consulta la [Transparency note del servizio Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) per essere informato sui rischi e le limitazioni.
L'approccio consigliato per mitigare questi rischi è includere un sistema di sicurezza nella tua architettura in grado di rilevare e prevenire comportamenti dannosi. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) offre un livello di protezione indipendente, capace di individuare contenuti dannosi generati dagli utenti e dall'IA nelle applicazioni e nei servizi. Azure AI Content Safety include API per testo e immagini che ti permettono di rilevare materiale dannoso. Disponiamo anche di un Content Safety Studio interattivo che consente di visualizzare, esplorare e provare esempi di codice per il rilevamento di contenuti dannosi in diverse modalità. La seguente [documentazione quickstart](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ti guida nel fare richieste al servizio.

Un altro aspetto da considerare è la performance complessiva dell'applicazione. Con applicazioni multimodali e multimodello, intendiamo per performance il fatto che il sistema funzioni come tu e i tuoi utenti vi aspettate, incluso il non generare output dannosi. È importante valutare la performance della tua applicazione complessiva utilizzando le [metriche di qualità di generazione e di rischio e sicurezza](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Puoi valutare la tua applicazione AI nel tuo ambiente di sviluppo usando l’[SDK prompt flow](https://microsoft.github.io/promptflow/index.html). Dato un dataset di test o un obiettivo, le generazioni della tua applicazione AI generativa vengono misurate quantitativamente con valutatori integrati o valutatori personalizzati a tua scelta. Per iniziare con l’SDK prompt flow per valutare il tuo sistema, puoi seguire la [guida quickstart](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Una volta eseguita una valutazione, puoi [visualizzare i risultati in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marchi

Questo progetto può contenere marchi o loghi di progetti, prodotti o servizi. L’uso autorizzato dei marchi o loghi Microsoft è soggetto e deve seguire le [Linee guida sui marchi e sul brand Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). L’uso di marchi o loghi Microsoft in versioni modificate di questo progetto non deve causare confusione né implicare sponsorizzazione da parte di Microsoft. Qualsiasi uso di marchi o loghi di terze parti è soggetto alle politiche di tali terze parti.

## Ottenere aiuto

Se incontri difficoltà o hai domande sulla creazione di app AI, unisciti a:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Se hai feedback sul prodotto o riscontri errori durante lo sviluppo, visita:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->