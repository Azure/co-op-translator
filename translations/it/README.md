# Co-op Translator

_Semplifica l'automazione e la manutenzione delle traduzioni per i tuoi contenuti didattici su GitHub in più lingue man mano che il tuo progetto evolve._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Pacchetto Python](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Licenza: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Download](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Download](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Contenitore: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Stile del codice: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Contributori GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![Problemi GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![Pull request GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PR benvenute](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**Inizia qui:** [Scegli il tuo flusso di lavoro](https://azure.github.io/co-op-translator/workflows/) | [Configurazione](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [API Python](https://azure.github.io/co-op-translator/api/) | [Server MCP](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Supporto multi-lingua

#### Supportato da [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabo](../ar/README.md) | [Bengalese](../bn/README.md) | [Bulgaro](../bg/README.md) | [Birmano (Myanmar)](../my/README.md) | [Cinese (Semplificato)](../zh-CN/README.md) | [Cinese (Tradizionale, Hong Kong)](../zh-HK/README.md) | [Cinese (Tradizionale, Macao)](../zh-MO/README.md) | [Cinese (Tradizionale, Taiwan)](../zh-TW/README.md) | [Croato](../hr/README.md) | [Ceco](../cs/README.md) | [Danese](../da/README.md) | [Olandese](../nl/README.md) | [Estone](../et/README.md) | [Finlandese](../fi/README.md) | [Francese](../fr/README.md) | [Tedesco](../de/README.md) | [Greco](../el/README.md) | [Ebraico](../he/README.md) | [Hindi](../hi/README.md) | [Ungherese](../hu/README.md) | [Indonesiano](../id/README.md) | [Italiano](./README.md) | [Giapponese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Coreano](../ko/README.md) | [Lituano](../lt/README.md) | [Malese](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalese](../ne/README.md) | [Pidgin nigeriano](../pcm/README.md) | [Norvegese](../no/README.md) | [Persiano (Farsi)](../fa/README.md) | [Polacco](../pl/README.md) | [Portoghese (Brasile)](../pt-BR/README.md) | [Portoghese (Portogallo)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumeno](../ro/README.md) | [Russo](../ru/README.md) | [Serbo (Cirillico)](../sr/README.md) | [Slovacchio](../sk/README.md) | [Sloveno](../sl/README.md) | [Spagnolo](../es/README.md) | [Swahili](../sw/README.md) | [Svedese](../sv/README.md) | [Tagalog (Filippino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thailandese](../th/README.md) | [Turco](../tr/README.md) | [Ucraino](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamita](../vi/README.md)

> **Preferisci clonare localmente?**
>
> Questo repository include più di 50 traduzioni linguistiche che aumentano notevolmente la dimensione del download. Per clonare senza le traduzioni, usa lo sparse checkout:
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
> Questo ti dà tutto il necessario per completare il corso con un download molto più rapido.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![Osservatori GitHub](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![Fork GitHub](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![Stelle GitHub](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Discord Microsoft Foundry](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Apri in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Panoramica

**Co-op Translator** ti aiuta a localizzare i tuoi contenuti didattici su GitHub in più lingue senza sforzo.
Quando aggiorni i tuoi file Markdown, le immagini o i notebook, le traduzioni rimangono automaticamente sincronizzate, garantendo che i tuoi contenuti siano accurati e aggiornati per gli studenti di tutto il mondo.

Usalo dalla CLI per tradurre repository, dall'API Python per l'automazione o tramite il server MCP per flussi di lavoro con agenti e editor.

Esempio di come è organizzato il contenuto tradotto:

![Esempio](../../imgs/translation-ex.png)

## Perché Co-op Translator?

Tradurre un singolo file è facile. Mantenere l'intero repository di documentazione
tradotto, collegato e aggiornato è la parte difficile.

| Problema | Come Co-op Translator aiuta |
| --- | --- |
| Long docs are not one prompt | I lunghi file Markdown vengono suddivisi in frammenti, quindi un README esteso non dipende da una singola risposta fragile del modello. Se un frammento fallisce, Co-op Translator può riprovare e suddividere nuovamente solo la parte fallita. |
| Incomplete translations should not be marked current | Una traduzione troncata non dovrebbe mai essere contrassegnata come aggiornata. Co-op Translator verifica l'integrità della traduzione prima di salvare e può rilevare traduzioni esistenti strutturalmente incomplete. |
| Links should match the translated repo structure | Le traduzioni manuali spesso lasciano link relativi che puntano nuovamente all'albero sorgente. Co-op Translator riscrive i link di Markdown, notebook, immagini e README per adattarli alla struttura `translations/<lang>/...`. |
| Translation should work across an entire repo | Co-op Translator gestisce file README, documentazione, notebook e testo delle immagini come parte di un unico flusso di lavoro per repository, invece di tradurre i file uno per uno. |
| Maintaining translations matters more than creating them once | Hash di origine e metadata delle traduzioni permettono a Co-op Translator di trovare file obsoleti, saltare file invariati e mantenere i contenuti tradotti sincronizzati man mano che il repository sorgente evolve. |

## Come viene gestito lo stato delle traduzioni

Co-op Translator gestisce i contenuti tradotti come **artifact software versionati**,  
non come file statici.

Lo strumento traccia lo stato dei Markdown, delle immagini e dei notebook tradotti
usando **metadata con ambito linguistico**.

Questo design consente a Co-op Translator di:

- Rilevare in modo affidabile le traduzioni non aggiornate
- Trattare Markdown, immagini e notebook in modo coerente
- Scalare in sicurezza su repository multi-lingua grandi e in rapido movimento

Modellando le traduzioni come artifact gestiti,
i flussi di lavoro di traduzione si allineano naturalmente con le pratiche moderne
di gestione delle dipendenze e degli artifact software.

→ [Come viene gestito lo stato delle traduzioni](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Approfondimenti correlati

- [Correggere il Markdown danneggiato nella traduzione AI: rinforzare una pipeline di produzione](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Inizia

Co-op Translator può essere usato dalla CLI, dall'API Python o dal server MCP. Inizia con la guida ai flussi di lavoro se stai scegliendo tra traduzione locale, automazione, CI e integrazione con agenti/editor.

- [Scegli il tuo flusso di lavoro](../../docs/workflows.md)
- [Configura le credenziali](../../docs/configuration.md)
- [Traduci dalla CLI](../../docs/cli.md)
- [Automatizza con l'API Python](../../docs/api.md)
- [Connettiti con il server MCP](../../docs/mcp.md)
- [Esegui in GitHub Actions](../../docs/github-actions.md)

Esempio CLI minimale dopo la configurazione:

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

Per le prime esecuzioni su repository di grandi dimensioni, usa `--dry-run` prima di scrivere i file tradotti. Consulta il [Riferimento CLI](../../docs/cli.md) per flag sui tipi di contenuto, log, revisioni e migrazione dei link.

Esecuzione rapida del contenitore con Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Esecuzione rapida del contenitore con PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Funzionalità

- Traduzione automatizzata per Markdown, notebook e immagini
- Mantiene le traduzioni sincronizzate con le modifiche sorgente
- Funziona in locale (CLI) o in CI (GitHub Actions)
- Espone strumenti di traduzione per Markdown, notebook, immagini, revisioni e progetto tramite MCP
- Utilizza Azure OpenAI o OpenAI per la traduzione con provider
- Permette a MCP di ospitare agenti per tradurre frammenti di Markdown e notebook senza credenziali LLM di Co-op Translator
- Usa Azure AI Vision per l'estrazione e la traduzione del testo nelle immagini
- Revisiona la struttura e la freschezza delle traduzioni con controlli deterministici
- Preserva la formattazione e la struttura del Markdown

## Documentazione

- [Sito della documentazione](https://azure.github.io/co-op-translator/)
- [Scegli il tuo flusso di lavoro](../../docs/workflows.md)
- [Configurazione](../../docs/configuration.md)
- [Configurazione Azure AI](../../docs/azure-ai-setup.md)
- [Riferimento CLI](../../docs/cli.md)
- [API Python](../../docs/api.md)
- [Server MCP](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [Template per lingue del README](../../docs/readme-languages-template.md)
- [Lingue supportate](../../docs/supported-languages.md)
- [Contribuire](../../CONTRIBUTING.md)
- [Risoluzione problemi](../../docs/troubleshooting.md)

### Guida specifica Microsoft
> [!NOTE]
> Per i manutentori dei repository Microsoft “For Beginners” soltanto.

- [Aggiornare la lista “other courses” (solo per i repository MS Beginners)](../../docs/microsoft-beginners.md)

## Supportaci e favorisci l'apprendimento globale

Unisciti a noi nella rivoluzione del modo in cui i contenuti didattici vengono condivisi a livello globale! Dai una ⭐ a [Co-op Translator](https://github.com/azure/co-op-translator) su GitHub e supporta la nostra missione di abbattere le barriere linguistiche nell'apprendimento e nella tecnologia. Il tuo interesse e i tuoi contributi hanno un impatto significativo! I contributi al codice e le proposte di funzionalità sono sempre benvenuti.

### Esplora i contenuti didattici Microsoft nella tua lingua
- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
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

👉 Fai clic sull'immagine qui sotto per guardare su YouTube.

- **Open at Microsoft**: Una breve introduzione di 18 minuti e una guida rapida su come usare Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contribuire

Questo progetto accoglie contributi e suggerimenti. Sei interessato a contribuire ad Azure Co-op Translator? Per favore consulta il nostro [CONTRIBUTING.md](../../CONTRIBUTING.md) per le linee guida su come puoi aiutare a rendere Co-op Translator più accessibile.

## Contributori

[![contributori di co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Codice di Condotta

Questo progetto ha adottato il [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Per maggiori informazioni consulta le [FAQ del Codice di Condotta](https://opensource.microsoft.com/codeofconduct/faq/) o contatta [opencode@microsoft.com](mailto:opencode@microsoft.com) per eventuali domande o commenti aggiuntivi.

## IA responsabile

Microsoft si impegna ad aiutare i nostri clienti a utilizzare i prodotti di IA in modo responsabile, condividere le nostre esperienze e costruire partnership basate sulla fiducia attraverso strumenti come Transparency Notes and Impact Assessments. Molte di queste risorse possono essere trovate su [https://aka.ms/RAI](https://aka.ms/RAI).
L'approccio di Microsoft all'IA responsabile è fondato sui nostri principi di IA: equità, affidabilità e sicurezza, privacy e protezione, inclusività, trasparenza e responsabilità.

I modelli su larga scala per linguaggio naturale, immagini e voce - come quelli utilizzati in questo esempio - possono potenzialmente comportarsi in modi ingiusti, inaffidabili o offensivi, causando danni. Si prega di consultare la [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) per essere informati sui rischi e le limitazioni.

L'approccio raccomandato per mitigare questi rischi è includere un sistema di sicurezza nella propria architettura in grado di rilevare e prevenire comportamenti dannosi. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) fornisce un livello indipendente di protezione, in grado di rilevare contenuti dannosi generati dagli utenti e dall'IA in applicazioni e servizi. Azure AI Content Safety include API per testo e immagini che consentono di rilevare materiale dannoso. Abbiamo inoltre un Content Safety Studio interattivo che permette di visualizzare, esplorare e provare esempi di codice per rilevare contenuti dannosi attraverso diverse modalità. La seguente [documentazione di avvio rapido](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ti guida nell'invio di richieste al servizio.

Un altro aspetto da tenere in considerazione è le prestazioni complessive dell'applicazione. Con applicazioni multimodali e multi-modello, intendiamo per prestazioni il fatto che il sistema operi come tu e i tuoi utenti vi aspettate, incluso il non generare output dannosi. È importante valutare le prestazioni della tua applicazione complessiva utilizzando le [metriche per qualità di generazione, rischio e sicurezza](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Puoi valutare la tua applicazione di IA nel tuo ambiente di sviluppo utilizzando il [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Dato un dataset di test o un obiettivo, le generazioni della tua applicazione di IA generativa vengono misurate quantitativamente con valutatori integrati o valutatori personalizzati a tua scelta. Per iniziare con il prompt flow sdk per valutare il tuo sistema, puoi seguire la [guida di avvio rapido](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Una volta eseguita una valutazione, puoi [visualizzare i risultati in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marchi

Questo progetto può contenere marchi o loghi per progetti, prodotti o servizi. L'uso autorizzato dei marchi o dei loghi Microsoft è soggetto e deve attenersi alle [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
L'uso dei marchi o dei loghi Microsoft in versioni modificate di questo progetto non deve causare confusione né implicare sponsorizzazione da parte di Microsoft.
Qualsiasi uso di marchi o loghi di terzi è soggetto alle politiche di tali terze parti.

## Ottenere aiuto

Se rimani bloccato o hai domande sulla creazione di app di IA, unisciti a:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Se hai feedback sul prodotto o riscontri errori durante lo sviluppo visita:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)