# Co-op Translator

_Automatizează și menține cu ușurință traducerile pentru conținutul educațional GitHub în mai multe limbi pe măsură ce proiectul tău evoluează._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Pachet Python](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Licență: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Descărcări](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Descărcări](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Stil de cod: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Contributori GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![Probleme GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![Pull requests GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PR-uri binevenite](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**Începe aici:** [Alegeți fluxul de lucru](https://azure.github.io/co-op-translator/workflows/) | [Configurare](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [API Python](https://azure.github.io/co-op-translator/api/) | [Server MCP](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Suport multilingv

#### Susținut de [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabă](../ar/README.md) | [Bengaleză](../bn/README.md) | [Bulgară](../bg/README.md) | [Birmană (Myanmar)](../my/README.md) | [Chineză (simplificată)](../zh-CN/README.md) | [Chineză (tradițională, Hong Kong)](../zh-HK/README.md) | [Chineză (tradițională, Macau)](../zh-MO/README.md) | [Chineză (tradițională, Taiwan)](../zh-TW/README.md) | [Croată](../hr/README.md) | [Cehă](../cs/README.md) | [Daneză](../da/README.md) | [Olandeză](../nl/README.md) | [Estonă](../et/README.md) | [Finlandeză](../fi/README.md) | [Franceză](../fr/README.md) | [Germană](../de/README.md) | [Greacă](../el/README.md) | [Ebraică](../he/README.md) | [Hindi](../hi/README.md) | [Maghiară](../hu/README.md) | [Indoneziană](../id/README.md) | [Italiană](../it/README.md) | [Japoneză](../ja/README.md) | [Kannada](../kn/README.md) | [Khmeră](../km/README.md) | [Coreeană](../ko/README.md) | [Lituaniană](../lt/README.md) | [Malaeză](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepaleză](../ne/README.md) | [Pidgin nigerian](../pcm/README.md) | [Norvegiană](../no/README.md) | [Persană (Farsi)](../fa/README.md) | [Poloneză](../pl/README.md) | [Portugheză (Brazilia)](../pt-BR/README.md) | [Portugheză (Portugalia)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Română](./README.md) | [Rusă](../ru/README.md) | [Sârbă (chirilică)](../sr/README.md) | [Slovacă](../sk/README.md) | [Slovenă](../sl/README.md) | [Spaniolă](../es/README.md) | [Swahili](../sw/README.md) | [Suedeză](../sv/README.md) | [Tagalog (filipineză)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thailandeză](../th/README.md) | [Turcă](../tr/README.md) | [Ucraineană](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnameză](../vi/README.md)

> **Preferi să clonezi local?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
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
> Aceasta îți oferă tot ce ai nevoie pentru a finaliza cursul, cu o descărcare mult mai rapidă.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![Urmăritori GitHub](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![Fork-uri GitHub](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![Stele GitHub](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Discord Microsoft Foundry](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Deschide în GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Prezentare generală

**Co-op Translator** te ajută să localizezi conținutul educațional de pe GitHub în mai multe limbi fără efort. Când actualizezi fișierele Markdown, imaginile sau notebook-urile, traducerile rămân sincronizate automat, asigurând că materialele tale sunt corecte și la zi pentru cursanții din întreaga lume.

Folosește-l din CLI pentru traducerea depozitului, din API-ul Python pentru automatizare sau prin serverul MCP pentru fluxuri cu agenți și editori.

Exemplu de organizare a conținutului tradus:

![Exemplu](../../imgs/translation-ex.png)

## De ce Co-op Translator?

Traducerea unui singur fișier e ușoară. Menținerea întregului depozit de documentație tradus, cu linkuri corecte și la zi, este partea dificilă.

| Problema | Cum ajută Co-op Translator |
| --- | --- |
| Documentația lungă nu este un singur prompt | Fișierele Markdown mari sunt împărțite în segmente, astfel încât un README lung să nu depindă de un singur răspuns fragil al modelului. Dacă un segment eșuează, Co-op Translator poate reîncerca și poate resegmenta doar partea eșuată. |
| Traducerile incomplete nu ar trebui marcate ca actuale | O traducere trunchiată nu ar trebui niciodată marcată ca actualizată. Co-op Translator verifică integritatea traducerii înainte de salvare și poate detecta traduceri existente structural incomplete. |
| Linkurile trebuie să se potrivească cu structura depozitului tradus | Traducerile manuale adesea lasă linkuri relative care indică înapoi spre arborele sursă. Co-op Translator rescrie linkurile din Markdown, notebook-uri, imagini și README pentru a se potrivi structurii `translations/<lang>/...`. |
| Traducerea ar trebui să funcționeze pentru întregul depozit | Co-op Translator se ocupă de fișierele README, documentație, notebook-uri și text din imagini ca parte a unui singur flux de lucru pentru depozit, în loc să traducă fișierele unul câte unul. |
| Menținerea traducerilor contează mai mult decât crearea lor o singură dată | Hash-urile sursă și metadata traducerii permit Co-op Translator să găsească fișiere învechite, să sară peste fișierele neschimbate și să păstreze conținutul tradus sincron pe măsură ce depozitul sursă evoluează. |

## Cum este gestionată starea traducerii

Co-op Translator gestionează conținutul tradus ca **artefacte software versiunate**,  
nu ca fișiere statice.

Unealta urmărește starea fișierelor Markdown traduse, a imaginilor și a notebook-urilor folosind **metadata specifică limbii**.

Acest design permite Co-op Translator să:

- Detecteze în mod fiabil traducerile învechite
- Trateze Markdown, imaginile și notebook-urile în mod consecvent
- Se scaleze sigur pe depozite mari, cu mișcare rapidă, multilingve

Prin modelarea traducerilor ca artefacte gestionate, fluxurile de lucru de traducere se aliniază în mod natural cu practicile moderne de gestionare a dependențelor și a artefactelor software.

→ [Cum este gestionată starea traducerii](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Analize aprofundate conexe

- [Remedierea Markdown-ului defect în traducerea AI: Întărirea unui pipeline de producție](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Începe

Co-op Translator poate fi folosit din CLI, din API-ul Python sau prin serverul MCP. Începe cu ghidul fluxului de lucru dacă alegi între traducere locală, automatizare, CI și integrarea agenților/editorilor.

- [Alegeți fluxul de lucru](../../docs/workflows.md)
- [Configurează acreditările](../../docs/configuration.md)
- [Tradu din CLI](../../docs/cli.md)
- [Automatizează cu API-ul Python](../../docs/api.md)
- [Conectează-te la serverul MCP](../../docs/mcp.md)
- [Rulează în GitHub Actions](../../docs/github-actions.md)

Exemplu minimal CLI după configurare:

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

Pentru primele rulări pe depozite mari, folosește `--dry-run` înainte de a scrie fișierele traduse. Vezi [Referința CLI](../../docs/cli.md) pentru flaguri pentru tipuri de conținut, jurnale, revizuire și migrarea linkurilor.

Rulare rapidă în container cu Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Rulare rapidă în container cu PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Caracteristici

- Traducere automată pentru Markdown, notebook-uri și imagini
- Păstrează traducerile sincronizate cu modificările sursei
- Funcționează local (CLI) sau în CI (GitHub Actions)
- Expune instrumente de traducere pentru Markdown, notebook-uri, imagini, revizuire și proiect prin MCP
- Folosește Azure OpenAI sau OpenAI pentru traduceri susținute de furnizor
- Permite serverului MCP să găzduiască agenți care traduc segmente de Markdown și notebook fără autentificările LLM ale Co-op Translator
- Folosește Azure AI Vision pentru extragerea și traducerea textului din imagini
- Revizuiește structura și prospețimea traducerii cu verificări deterministe
- Păstrează formatarea și structura Markdown

## Documentație

- [Site-ul documentației](https://azure.github.io/co-op-translator/)
- [Alegeți fluxul de lucru](../../docs/workflows.md)
- [Configurare](../../docs/configuration.md)
- [Configurare Azure AI](../../docs/azure-ai-setup.md)
- [Referința CLI](../../docs/cli.md)
- [API Python](../../docs/api.md)
- [Server MCP](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [Șablon README pentru limbi](../../docs/readme-languages-template.md)
- [Limbi suportate](../../docs/supported-languages.md)
- [Contribuie](../../CONTRIBUTING.md)
- [Depanare](../../docs/troubleshooting.md)

### Ghid specific Microsoft
> [!NOTE]
> Doar pentru administratorii depozitelor Microsoft „For Beginners”.

- [Actualizarea listei “other courses” (doar pentru depozitele MS Beginners)](../../docs/microsoft-beginners.md)

## Sprijină-ne și promovează învățarea globală

Alătură-te nouă în revoluționarea modului în care conținutul educațional este distribuit la nivel global! Dă [Co-op Translator](https://github.com/azure/co-op-translator) o ⭐ pe GitHub și susține misiunea noastră de a elimina barierele lingvistice în învățare și tehnologie. Interesul și contribuțiile tale au un impact semnificativ! Contribuțiile de cod și sugestiile de funcționalități sunt mereu binevenite.

### Explorează conținutul educațional Microsoft în limba ta
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

## Prezentări video

👉 Faceți clic pe imaginea de mai jos pentru a urmări pe YouTube.

- **Open at Microsoft**: O scurtă introducere de 18 minute și un ghid rapid despre cum să folosiți Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contribuții

Acest proiect acceptă contribuții și sugestii. Sunteți interesat să contribuiți la Azure Co-op Translator? Vă rugăm să consultați [CONTRIBUTING.md](../../CONTRIBUTING.md) pentru ghiduri despre cum puteți ajuta la creșterea accesibilității Co-op Translator.

## Contribuitori

[![contribuitori co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Cod de conduită

Acest proiect a adoptat [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Pentru mai multe informații consultați [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) sau
contactați [opencode@microsoft.com](mailto:opencode@microsoft.com) pentru orice întrebări sau comentarii suplimentare.

## Inteligență artificială responsabilă

Microsoft se angajează să ajute clienții noștri să utilizeze produsele noastre AI în mod responsabil, să împărtășească ceea ce am învățat și să construim parteneriate bazate pe încredere prin instrumente precum Transparency Notes și Impact Assessments. Multe dintre aceste resurse pot fi găsite la [https://aka.ms/RAI](https://aka.ms/RAI).
Abordarea Microsoft privind AI responsabil este ancorată în principiile noastre AI: corectitudine, fiabilitate și siguranță, confidențialitate și securitate, incluziune, transparență și responsabilitate.

Modelele la scară largă pentru limbaj natural, imagine și voce - precum cele folosite în acest exemplu - pot avea comportamente care sunt nedrepte, nefiabile sau ofensatoare, cauzând astfel daune. Vă rugăm să consultați [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) pentru a fi informat despre riscuri și limitări.

Abordarea recomandată pentru a atenua aceste riscuri este includerea unui sistem de siguranță în arhitectura dvs. care poate detecta și preveni comportamentele dăunătoare. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) oferă un strat independent de protecție, capabil să detecteze conținut generat de utilizatori și de AI dăunător în aplicații și servicii. Azure AI Content Safety include API-uri pentru text și imagine care vă permit să detectați materiale dăunătoare. De asemenea, avem un Content Safety Studio interactiv care vă permite să vizualizați, să explorați și să încercați codul de exemplu pentru detectarea conținutului dăunător în diferite modalități. Următoarea [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vă ghidează prin efectuarea cererilor către serviciu.

Un alt aspect de luat în considerare este performanța generală a aplicației. În aplicațiile multimodale și cu mai multe modele, considerăm performanța ca semnificând faptul că sistemul funcționează așa cum vă așteptați dvs. și utilizatorii dvs., inclusiv prin faptul că nu generează rezultate dăunătoare. Este important să evaluați performanța aplicației dvs. per ansamblu folosind [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Puteți evalua aplicația dvs. AI în mediul de dezvoltare folosind [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Având fie un set de date de test, fie un obiectiv, generațiile aplicației dvs. generative AI sunt măsurate cantitativ cu evaluatori încorporați sau evaluatori personalizați la alegere. Pentru a începe cu prompt flow sdk pentru a vă evalua sistemul, puteți urma [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). După ce executați o rulare de evaluare, puteți [vizualiza rezultatele în Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Mărci înregistrate

Acest proiect poate conține mărci comerciale sau logouri pentru proiecte, produse sau servicii. Utilizarea autorizată a mărcilor sau logourilor Microsoft este supusă și trebuie să urmeze [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Utilizarea mărcilor sau logourilor Microsoft în versiuni modificate ale acestui proiect nu trebuie să creeze confuzie sau să sugereze sponsorizarea de către Microsoft.
Orice utilizare a mărcilor sau logourilor terțe părți este supusă politicilor acelor terțe părți.

## Obținerea asistenței

Dacă întâmpinați probleme sau aveți întrebări despre dezvoltarea aplicațiilor AI, alăturați-vă:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Dacă aveți feedback despre produs sau întâlniți erori în timpul dezvoltării vizitați:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)