<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:57:01+00:00",
  "source_file": "README.md",
  "language_code": "ro"
}
-->
# Co-op Translator

_Automatizează cu ușurință traducerea conținutului educațional de pe GitHub în mai multe limbi pentru a ajunge la o audiență globală._

[![Pachet Python](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Licență: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Descărcări](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Descărcări](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Stil cod: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Contribuitori GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![Probleme GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![Pull-request-uri GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PR-uri binevenite](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Suport multilingv

#### Suportat de [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabă](../ar/README.md) | [Bengaleză](../bn/README.md) | [Bulgară](../bg/README.md) | [Birmană (Myanmar)](../my/README.md) | [Chineză (Simplificată)](../zh/README.md) | [Chineză (Tradițională, Hong Kong)](../hk/README.md) | [Chineză (Tradițională, Macau)](../mo/README.md) | [Chineză (Tradițională, Taiwan)](../tw/README.md) | [Croată](../hr/README.md) | [Cehă](../cs/README.md) | [Daneză](../da/README.md) | [Olandeză](../nl/README.md) | [Estonă](../et/README.md) | [Finlandeză](../fi/README.md) | [Franceză](../fr/README.md) | [Germană](../de/README.md) | [Greacă](../el/README.md) | [Ebraică](../he/README.md) | [Hindi](../hi/README.md) | [Maghiară](../hu/README.md) | [Indoneziană](../id/README.md) | [Italiană](../it/README.md) | [Japoneză](../ja/README.md) | [Coreeană](../ko/README.md) | [Lituaniană](../lt/README.md) | [Malaeziană](../ms/README.md) | [Marathi](../mr/README.md) | [Nepaleză](../ne/README.md) | [Norvegiană](../no/README.md) | [Persană (Farsi)](../fa/README.md) | [Poloneză](../pl/README.md) | [Portugheză (Brazilia)](../br/README.md) | [Portugheză (Portugalia)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Română](./README.md) | [Rusă](../ru/README.md) | [Sârbă (Chirilică)](../sr/README.md) | [Slovacă](../sk/README.md) | [Slovenă](../sl/README.md) | [Spaniolă](../es/README.md) | [Swahili](../sw/README.md) | [Suedeză](../sv/README.md) | [Tagalog (Filipineză)](../tl/README.md) | [Tamil](../ta/README.md) | [Thailandeză](../th/README.md) | [Turcă](../tr/README.md) | [Ucraineană](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnameză](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![Observatori GitHub](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![Fork-uri GitHub](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![Stele GitHub](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Deschide în GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Prezentare generală

**Co-op Translator** îți permite să traduci rapid conținutul educațional de pe GitHub în mai multe limbi, ajungând fără efort la o audiență globală. Când actualizezi fișierele Markdown, imaginile sau notițele Jupyter, traducerile sunt sincronizate automat pentru ca materialele tale educaționale să rămână mereu actualizate și relevante pentru utilizatorii internaționali.

Vezi cum Co-op Translator organizează conținutul educațional tradus pe GitHub:

![Exemplu](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.ro.png)

## Ghid rapid

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

## Configurare minimă

- Creează un fișier `.env` folosind șablonul: [.env.template](../../.env.template)
- Configurează un furnizor LLM (Azure OpenAI sau OpenAI)
- Pentru traducerea imaginilor (`-img`), configurează și Azure AI Vision
- Recomandat: Dacă ai traduceri generate cu alte instrumente, curăță-le mai întâi pentru a evita conflictele (de exemplu: `translations/`).
- Recomandat: Adaugă o secțiune de traduceri în README folosind [șablonul de limbi README](./README_languages_template.md)
- Vezi: [Configurează Azure AI](./getting_started/set-up-azure-ai.md)

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
- [Ghid GitHub Actions (repo publice & secrete standard)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Ghid GitHub Actions (repo Microsoft & configurări la nivel de organizație)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Limbi suportate](./getting_started/supported-languages.md)
- [Depanare](./getting_started/troubleshooting.md)

## Susține-ne și promovează învățarea globală

Alătură-te nouă pentru a revoluționa modul în care conținutul educațional este distribuit la nivel global! Oferă [Co-op Translator](https://github.com/azure/co-op-translator) o ⭐ pe GitHub și susține misiunea noastră de a elimina barierele lingvistice în educație și tehnologie. Interesul și contribuțiile tale contează! Orice contribuție la cod sau sugestie de funcționalitate este binevenită.

### Explorează conținut educațional Microsoft în limba ta

- [AZD pentru Începători](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI pentru Începători](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) Pentru Începători](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents pentru Începători](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI pentru Începători cu .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI pentru Începători](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI pentru Începători cu Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML pentru Începători](https://aka.ms/ml-beginners)
- [Data Science pentru Începători](https://aka.ms/datascience-beginners)
- [AI pentru Începători](https://aka.ms/ai-beginners)
- [Cybersecurity pentru Începători](https://github.com/microsoft/Security-101)
- [Web Dev pentru Începători](https://aka.ms/webdev-beginners)
- [IoT pentru Începători](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Prezentări video

Află mai multe despre Co-op Translator din prezentările noastre _(Click pe imaginea de mai jos pentru a viziona pe YouTube.)_:

- **Open at Microsoft**: O introducere scurtă de 18 minute și un ghid rapid despre cum să folosești Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.ro.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contribuie

Acest proiect încurajează contribuțiile și sugestiile. Vrei să contribui la Azure Co-op Translator? Vezi [CONTRIBUTING.md](./CONTRIBUTING.md) pentru instrucțiuni despre cum poți ajuta la îmbunătățirea accesibilității Co-op Translator.

## Contribuitori

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Cod de conduită

Acest proiect a adoptat [Codul de conduită Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/).
Pentru mai multe informații, vezi [Întrebări frecvente despre Codul de conduită](https://opensource.microsoft.com/codeofconduct/faq/) sau
contactează [opencode@microsoft.com](mailto:opencode@microsoft.com) pentru întrebări sau comentarii suplimentare.

## AI responsabil

Microsoft se angajează să ajute clienții să folosească produsele noastre AI în mod responsabil, să împărtășească lecțiile învățate și să construiască parteneriate bazate pe încredere prin instrumente precum Transparency Notes și Impact Assessments. Multe dintre aceste resurse pot fi găsite la [https://aka.ms/RAI](https://aka.ms/RAI).
Abordarea Microsoft privind AI responsabil se bazează pe principiile noastre: echitate, fiabilitate și siguranță, confidențialitate și securitate, incluziune, transparență și responsabilitate.

Modelele de limbaj, imagine și vorbire la scară largă – precum cele folosite în acest exemplu – pot avea comportamente nedrepte, nesigure sau ofensatoare, ceea ce poate duce la efecte negative. Consultă [nota de transparență pentru serviciul Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) pentru a fi informat despre riscuri și limitări.

Recomandarea pentru reducerea acestor riscuri este să incluzi un sistem de siguranță în arhitectura ta care să detecteze și să prevină comportamentele dăunătoare. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) oferă un strat independent de protecție, capabil să detecteze conținut dăunător generat de utilizatori sau AI în aplicații și servicii. Azure AI Content Safety include API-uri pentru text și imagine care permit detectarea materialelor dăunătoare. Avem și un Content Safety Studio interactiv unde poți explora și testa cod pentru detectarea conținutului dăunător pe diferite tipuri de date. Următoarea [documentație de start rapid](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) te ghidează pentru a face cereri către serviciu.
Un alt aspect de luat în considerare este performanța generală a aplicației. În cazul aplicațiilor multi-modale și cu mai multe modele, performanța înseamnă că sistemul funcționează așa cum vă așteptați tu și utilizatorii tăi, inclusiv să nu genereze rezultate dăunătoare. Este important să evaluezi performanța aplicației tale folosind [metrice de calitate a generării și de risc și siguranță](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Poți evalua aplicația ta AI în mediul de dezvoltare folosind [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Având la dispoziție fie un set de date de test, fie un obiectiv, generările aplicației tale AI generative sunt măsurate cantitativ cu evaluatori integrați sau personalizați, după preferință. Pentru a începe cu prompt flow sdk și a evalua sistemul tău, poți urma [ghidul de început rapid](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). După ce execuți o rundă de evaluare, poți [vizualiza rezultatele în Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Mărci înregistrate

Acest proiect poate conține mărci înregistrate sau logo-uri pentru proiecte, produse sau servicii. Utilizarea autorizată a mărcilor sau logo-urilor Microsoft este supusă și trebuie să respecte [Ghidul de utilizare a mărcilor și brandului Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Utilizarea mărcilor sau logo-urilor Microsoft în versiuni modificate ale acestui proiect nu trebuie să creeze confuzie sau să implice sponsorizarea Microsoft.
Orice utilizare a mărcilor sau logo-urilor terților este supusă politicilor acelor terți.

## Obținerea de ajutor

Dacă întâmpini dificultăți sau ai întrebări despre dezvoltarea aplicațiilor AI, alătură-te:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Dacă ai feedback despre produs sau erori în timpul dezvoltării, vizitează:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Declarație de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm răspunderea pentru orice neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.