<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:47:50+00:00",
  "source_file": "README.md",
  "language_code": "hu"
}
-->
# Co-op Translator

_Automatikusan lefordíthatod oktatási GitHub tartalmaidat több nyelvre, hogy világszerte elérhesd a közönséged._

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

### 🌐 Többnyelvű támogatás

#### Támogatja a [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arab](../ar/README.md) | [Bengáli](../bn/README.md) | [Bolgár](../bg/README.md) | [Burmai (Mianmar)](../my/README.md) | [Kínai (egyszerűsített)](../zh/README.md) | [Kínai (hagyományos, Hongkong)](../hk/README.md) | [Kínai (hagyományos, Makaó)](../mo/README.md) | [Kínai (hagyományos, Tajvan)](../tw/README.md) | [Horvát](../hr/README.md) | [Cseh](../cs/README.md) | [Dán](../da/README.md) | [Holland](../nl/README.md) | [Észt](../et/README.md) | [Finn](../fi/README.md) | [Francia](../fr/README.md) | [Német](../de/README.md) | [Görög](../el/README.md) | [Héber](../he/README.md) | [Hindi](../hi/README.md) | [Magyar](./README.md) | [Indonéz](../id/README.md) | [Olasz](../it/README.md) | [Japán](../ja/README.md) | [Koreai](../ko/README.md) | [Litván](../lt/README.md) | [Maláj](../ms/README.md) | [Marathi](../mr/README.md) | [Nepáli](../ne/README.md) | [Norvég](../no/README.md) | [Perzsa (fárszi)](../fa/README.md) | [Lengyel](../pl/README.md) | [Portugál (Brazília)](../br/README.md) | [Portugál (Portugália)](../pt/README.md) | [Pandzsábi (Gurmukhi)](../pa/README.md) | [Román](../ro/README.md) | [Orosz](../ru/README.md) | [Szerb (cirill)](../sr/README.md) | [Szlovák](../sk/README.md) | [Szlovén](../sl/README.md) | [Spanyol](../es/README.md) | [Szuahéli](../sw/README.md) | [Svéd](../sv/README.md) | [Tagalog (filippínó)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Török](../tr/README.md) | [Ukrán](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnámi](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Áttekintés

A **Co-op Translator** segítségével gyorsan lefordíthatod oktatási GitHub tartalmaidat több nyelvre, így könnyedén elérheted a nemzetközi közönséget. Ha frissíted a Markdown fájlokat, képeket vagy Jupyter notebookokat, a fordítások automatikusan szinkronizálódnak, így a tartalmad mindig naprakész és releváns marad a külföldi felhasználók számára.

Nézd meg, hogyan rendszerezi a Co-op Translator a lefordított oktatási GitHub tartalmakat:

![Példa](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.hu.png)

## Gyors kezdés

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

## Minimális beállítás

- Hozz létre egy `.env` fájlt a sablon alapján: [.env.template](../../.env.template)
- Állíts be egy LLM szolgáltatót (Azure OpenAI vagy OpenAI)
- Képfordításhoz (`-img`) állítsd be az Azure AI Vision-t is
- Ajánlott: Ha más eszközökkel generált fordításaid vannak, előbb tisztítsd meg őket, hogy elkerüld az ütközéseket (például: `translations/`).
- Ajánlott: Add hozzá a fordítások szekciót a README-hez a [README nyelvi sablon](./README_languages_template.md) segítségével
- Lásd: [Azure AI beállítása](./getting_started/set-up-azure-ai.md)

## Használat

Minden támogatott típus fordítása:

```bash
translate -l "ko ja"
```

Csak Markdown:

```bash
translate -l "de" -md
```

Markdown + képek:

```bash
translate -l "pt" -md -img
```

Csak notebookok:

```bash
translate -l "zh" -nb
```

További kapcsolók: [Parancsok leírása](./getting_started/command-reference.md)

## Funkciók

- Automatikus fordítás Markdown, notebookok és képek esetén
- A fordítások mindig szinkronban maradnak a forrással
- Működik helyben (CLI) vagy CI-ben (GitHub Actions)
- Azure OpenAI vagy OpenAI használata; képekhez opcionális Azure AI Vision
- Megőrzi a Markdown formázást és szerkezetet

## Dokumentáció

- [Parancssori útmutató](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions útmutató (nyilvános repók & standard titkok)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions útmutató (Microsoft szervezeti repók & szervezeti beállítások)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Támogatott nyelvek](./getting_started/supported-languages.md)
- [Hibaelhárítás](./getting_started/troubleshooting.md)

## Támogass minket és segítsd a globális tanulást

Csatlakozz hozzánk, hogy forradalmasítsuk az oktatási tartalmak globális megosztását! Adj egy ⭐-t a [Co-op Translator](https://github.com/azure/co-op-translator) projektnek a GitHubon, és támogasd küldetésünket, hogy lebontsuk a nyelvi akadályokat a tanulásban és technológiában. Az érdeklődésed és hozzájárulásod sokat számít! Kódhozzájárulásokat és ötleteket mindig szívesen fogadunk.

### Fedezd fel a Microsoft oktatási tartalmait a saját nyelveden

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

## Videós bemutatók

Ismerd meg jobban a Co-op Translator-t bemutatóinkon keresztül _(Kattints a képre, hogy megnézd YouTube-on.)_:

- **Open at Microsoft**: Egy rövid, 18 perces bemutató és gyors útmutató a Co-op Translator használatához.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.hu.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Közreműködés

A projekt szívesen fogad minden hozzájárulást és javaslatot. Szeretnél részt venni az Azure Co-op Translator fejlesztésében? Olvasd el a [CONTRIBUTING.md](./CONTRIBUTING.md) útmutatót, hogy megtudd, hogyan segíthetsz hozzáférhetőbbé tenni a Co-op Translator-t.

## Közreműködők

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Magatartási kódex

Ez a projekt a [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) magatartási kódexet alkalmazza.
További információért lásd a [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) oldalt, vagy
keress minket az [opencode@microsoft.com](mailto:opencode@microsoft.com) címen kérdéseiddel vagy észrevételeiddel.

## Felelős AI

A Microsoft elkötelezett amellett, hogy ügyfeleink felelősen használják AI termékeinket, megosztjuk tapasztalatainkat, és bizalmon alapuló partnerségeket építünk olyan eszközökön keresztül, mint a Transparency Notes és Impact Assessments. Ezeket az erőforrásokat megtalálod itt: [https://aka.ms/RAI](https://aka.ms/RAI).
A Microsoft felelős AI megközelítése az igazságosság, megbízhatóság és biztonság, adatvédelem és biztonság, befogadás, átláthatóság és elszámoltathatóság elvein alapul.

A nagy nyelvi, képi és beszédmodellek – mint amilyeneket ez a példa is használ – előfordulhat, hogy igazságtalanul, megbízhatatlanul vagy sértően viselkednek, ami károkat okozhat. Kérjük, olvasd el az [Azure OpenAI szolgáltatás Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) dokumentumot, hogy tisztában legyél a kockázatokkal és korlátokkal.

A kockázatok csökkentésére ajánlott, hogy építs be egy biztonsági rendszert az architektúrádba, amely képes felismerni és megelőzni a káros viselkedést. Az [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) egy független védelmi réteget biztosít, amely képes felismerni a felhasználók vagy AI által generált káros tartalmakat alkalmazásokban és szolgáltatásokban. Az Azure AI Content Safety szöveg- és kép API-kat kínál, amelyekkel felismerheted a káros anyagokat. Emellett van egy interaktív Content Safety Studio, ahol megtekintheted, kipróbálhatod a mintakódokat különböző tartalomtípusokhoz. Az alábbi [gyorsindító dokumentáció](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) segít a szolgáltatás használatának elsajátításában.
Egy másik szempont, amit figyelembe kell venni, az alkalmazás általános teljesítménye. Többmódú és többmodellű alkalmazások esetén a teljesítmény alatt azt értjük, hogy a rendszer úgy működik, ahogy Ön és a felhasználói elvárják, beleértve azt is, hogy nem generál káros kimeneteket. Fontos, hogy az alkalmazás teljesítményét [generálási minőség, kockázat és biztonsági metrikák](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) alapján értékelje.

Az AI alkalmazását a fejlesztői környezetben a [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) segítségével értékelheti. Akár tesztadatokat, akár egy célt ad meg, a generatív AI alkalmazás generációi számszerűen mérhetők beépített vagy egyéni értékelőkkel, amelyeket Ön választ. Ha szeretné elkezdeni a prompt flow sdk használatát a rendszer értékeléséhez, kövesse a [gyorsindítási útmutatót](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Miután lefuttatott egy értékelési futást, [vizualizálhatja az eredményeket az Azure AI Studio-ban](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Védjegyek

Ez a projekt tartalmazhat védjegyeket vagy logókat projektekhez, termékekhez vagy szolgáltatásokhoz. A Microsoft védjegyek vagy logók engedélyezett használata a [Microsoft védjegy- és márkaútmutató](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) szerint történhet.
A Microsoft védjegyek vagy logók használata a projekt módosított verzióiban nem okozhat félreértést, és nem keltheti azt a látszatot, hogy a Microsoft támogatja azt.
Harmadik fél védjegyeinek vagy logóinak használata az adott harmadik fél szabályzatai szerint történik.

## Segítségkérés

Ha elakad, vagy kérdése van AI alkalmazások fejlesztésével kapcsolatban, csatlakozzon:

<a href="https://aka.ms/foundry/discord"><img src="https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff" alt="Azure AI Foundry Discord"></a>

Ha termékvisszajelzése van, vagy hibát tapasztal fejlesztés közben, látogasson el ide:

<a href="https://aka.ms/foundry/forum"><img src="https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff" alt="Azure AI Foundry Developer Forum"></a>

---

**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasoljuk a professzionális, emberi fordítást. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.