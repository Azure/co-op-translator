<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T12:17:31+00:00",
  "source_file": "README.md",
  "language_code": "ro"
}
-->
# Co-op Translator

_Automatizează cu ușurință traducerea conținutului educațional de pe GitHub în mai multe limbi pentru a ajunge la un public global._

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

### 🌐 Suport multilingv

#### Susținut de [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabă](../ar/README.md) | [Bengaleză](../bn/README.md) | [Bulgară](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chineză (Simplificată)](../zh/README.md) | [Chineză (Tradițională, Hong Kong)](../hk/README.md) | [Chineză (Tradițională, Macau)](../mo/README.md) | [Chineză (Tradițională, Taiwan)](../tw/README.md) | [Croată](../hr/README.md) | [Cehă](../cs/README.md) | [Daneză](../da/README.md) | [Olandeză](../nl/README.md) | [Estonă](../et/README.md) | [Finlandeză](../fi/README.md) | [Franceză](../fr/README.md) | [Germană](../de/README.md) | [Greacă](../el/README.md) | [Ebraică](../he/README.md) | [Hindi](../hi/README.md) | [Maghiară](../hu/README.md) | [Indoneziană](../id/README.md) | [Italiană](../it/README.md) | [Japoneză](../ja/README.md) | [Kannada](../kn/README.md) | [Coreeană](../ko/README.md) | [Lituaniană](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepaleză](../ne/README.md) | [Pidgin Nigerian](../pcm/README.md) | [Norvegiană](../no/README.md) | [Persană (Farsi)](../fa/README.md) | [Poloneză](../pl/README.md) | [Portugheză (Brazilia)](../br/README.md) | [Portugheză (Portugalia)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Română](./README.md) | [Rusă](../ru/README.md) | [Sârbă (Chirilică)](../sr/README.md) | [Slovacă](../sk/README.md) | [Slovenă](../sl/README.md) | [Spaniolă](../es/README.md) | [Swahili](../sw/README.md) | [Suedeză](../sv/README.md) | [Tagalog (Filipineză)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thailandeză](../th/README.md) | [Turcă](../tr/README.md) | [Ucraineană](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnameză](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Prezentare generală

**Co-op Translator** te ajută să localizezi conținutul educațional de pe GitHub în mai multe limbi fără efort.
Când actualizezi fișierele Markdown, imaginile sau notebook-urile, traducerile rămân sincronizate automat, asigurând că materialul tău este corect și actualizat pentru cursanți din întreaga lume.

Exemplu de organizare a conținutului tradus:

![Exemplu](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.ro.png)

## Pornire rapidă

```bash
# Creează și activează un mediu virtual (recomandat)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Instalează pachetul
pip install co-op-translator
# Traduce
translate -l "ko ja fr" -md
```

Docker:

```bash
# Trage imaginea publică de pe GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Rulează cu folderul curent montat și .env furnizat (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Configurare minimală

1. Creează un fișier `.env` folosind șablonul: [.env.template](../../.env.template)
2. Configurează un furnizor LLM (Azure OpenAI sau OpenAI)
3. (Opțional) Pentru traducerea imaginilor (`-img`), configurează Azure AI Vision
4. (Recomandat) Curăță orice traduceri anterioare pentru a evita conflictele (ex: `translations/`)
5. (Recomandat) Adaugă o secțiune de traduceri în README folosind [șablonul pentru limbi din README](./getting_started/README_languages_template.md)
6. Vezi: [Configurare Azure AI](./getting_started/set-up-azure-ai.md)

## Utilizare

Tradu toate tipurile suportate:

```bash
translate -l "ko ja"
```

Doar Markdown:

```bash
translate -l "de" -md
```

Markdown + imagini:

```bash
translate -l "pt" -md -img
```

Doar notebook-uri:

```bash
translate -l "zh" -nb
```

Mai multe opțiuni: [Referință comenzi](./getting_started/command-reference.md)

## Funcționalități

- Traducere automată pentru Markdown, notebook-uri și imagini
- Menține traducerile sincronizate cu modificările sursei
- Funcționează local (CLI) sau în CI (GitHub Actions)
- Folosește Azure OpenAI sau OpenAI; opțional Azure AI Vision pentru imagini
- Păstrează formatul și structura Markdown

## Documentație

- [Ghid linie de comandă](./getting_started/command-line-guide/command-line-guide.md)
- [Ghid GitHub Actions (repositorii publice & secrete standard)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Ghid GitHub Actions (repositorii organizație Microsoft & configurări la nivel de organizație)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Șablon limbi README](./getting_started/README_languages_template.md)
- [Limbi suportate](./getting_started/supported-languages.md)
- [Contribuții](./CONTRIBUTING.md)
- [Depanare](./getting_started/troubleshooting.md)

### Ghid specific Microsoft
> [!NOTE]
> Doar pentru întreținătorii depozitelor Microsoft „Pentru Începători”.

- [Actualizarea listei „alte cursuri” (doar pentru depozitele MS Beginners)](./getting_started/update-other-courses.md)

## Susține-ne și promovează învățarea globală

Alătură-te revoluției în modul în care conținutul educațional este distribuit la nivel global! Dă un ⭐ proiectului [Co-op Translator](https://github.com/azure/co-op-translator) pe GitHub și susține misiunea noastră de a elimina barierele lingvistice în învățare și tehnologie. Interesul și contribuțiile tale au un impact semnificativ! Contribuțiile de cod și sugestiile de funcționalități sunt întotdeauna binevenite.

### Explorează conținut educațional Microsoft în limba ta

- [AZD pentru Începători](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI pentru Începători](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) Pentru Începători](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents pentru Începători](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI pentru Începători folosind .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI pentru Începători](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI pentru Începători folosind Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML pentru Începători](https://aka.ms/ml-beginners)
- [Data Science pentru Începători](https://aka.ms/datascience-beginners)
- [AI pentru Începători](https://aka.ms/ai-beginners)
- [Cybersecurity pentru Începători](https://github.com/microsoft/Security-101)
- [Web Dev pentru Începători](https://aka.ms/webdev-beginners)
- [IoT pentru Începători](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Prezentări video

👉 Apasă pe imaginea de mai jos pentru a viziona pe YouTube.

- **Open at Microsoft**: O scurtă introducere de 18 minute și un ghid rapid despre cum să folosești Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.ro.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contribuții

Acest proiect primește cu plăcere contribuții și sugestii. Ești interesat să contribui la Azure Co-op Translator? Te rugăm să consulți [CONTRIBUTING.md](./CONTRIBUTING.md) pentru ghiduri despre cum poți ajuta la creșterea accesibilității Co-op Translator.

## Contribuitori

[![contribuitori co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Cod de conduită

Acest proiect a adoptat [Codul de Conduită Open Source Microsoft](https://opensource.microsoft.com/codeofconduct/).
Pentru mai multe informații vezi [Întrebări frecvente despre Codul de Conduită](https://opensource.microsoft.com/codeofconduct/faq/) sau contactează [opencode@microsoft.com](mailto:opencode@microsoft.com) pentru întrebări sau comentarii suplimentare.

## Inteligență Artificială Responsabilă

Microsoft este dedicat să ajute clienții să folosească produsele noastre AI în mod responsabil, împărtășind experiențele noastre și construind parteneriate bazate pe încredere prin instrumente precum Notele de Transparență și Evaluările Impactului. Multe dintre aceste resurse pot fi găsite la [https://aka.ms/RAI](https://aka.ms/RAI).
Abordarea Microsoft privind AI responsabilă se bazează pe principiile noastre AI de corectitudine, fiabilitate și siguranță, confidențialitate și securitate, incluziune, transparență și responsabilitate.

Modelele de limbaj natural, imagine și vorbire la scară largă - precum cele folosite în acest exemplu - pot avea comportamente care să fie nedrepte, nesigure sau ofensatoare, cauzând astfel daune. Te rugăm să consulți [Nota de transparență a serviciului Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) pentru a fi informat despre riscuri și limitări.
Abordarea recomandată pentru a atenua aceste riscuri este să includeți un sistem de siguranță în arhitectura dvs. care să poată detecta și preveni comportamentul dăunător. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) oferă un strat independent de protecție, capabil să detecteze conținutul dăunător generat de utilizatori și de AI în aplicații și servicii. Azure AI Content Safety include API-uri pentru text și imagini care vă permit să detectați materiale dăunătoare. De asemenea, avem un Content Safety Studio interactiv care vă permite să vizualizați, să explorați și să încercați coduri de exemplu pentru detectarea conținutului dăunător în diferite modalități. Următoarea [documentație quickstart](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vă ghidează prin procesul de a face cereri către serviciu.

Un alt aspect de luat în considerare este performanța generală a aplicației. În cazul aplicațiilor multimodale și multimodel, considerăm că performanța înseamnă că sistemul funcționează așa cum vă așteptați dvs. și utilizatorii dvs., inclusiv să nu genereze rezultate dăunătoare. Este important să evaluați performanța aplicației dvs. folosind [metrici de calitate a generării și de risc și siguranță](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Puteți evalua aplicația dvs. AI în mediul de dezvoltare folosind [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Având un set de date de test sau un obiectiv, generațiile aplicației dvs. AI generative sunt măsurate cantitativ cu evaluatori încorporați sau evaluatori personalizați la alegerea dvs. Pentru a începe să utilizați prompt flow sdk pentru a evalua sistemul, puteți urma [ghidul quickstart](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). După ce executați o rulare de evaluare, puteți [vizualiza rezultatele în Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Mărci comerciale

Acest proiect poate conține mărci comerciale sau logo-uri pentru proiecte, produse sau servicii. Utilizarea autorizată a mărcilor comerciale sau logo-urilor Microsoft este supusă și trebuie să respecte [Ghidul privind mărcile comerciale și brandurile Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Utilizarea mărcilor comerciale sau logo-urilor Microsoft în versiuni modificate ale acestui proiect nu trebuie să creeze confuzie sau să sugereze sponsorizarea de către Microsoft. Orice utilizare a mărcilor comerciale sau logo-urilor terților este supusă politicilor acelor terți.

## Obținerea ajutorului

Dacă întâmpinați dificultăți sau aveți întrebări despre construirea aplicațiilor AI, alăturați-vă:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Dacă aveți feedback despre produs sau erori în timpul dezvoltării, vizitați:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->