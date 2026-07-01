# Co-op Translator

_Egyszerűen automatizálja és tartsa karban oktatási GitHub-tartalmainak fordításait több nyelven, ahogyan projektje fejlődik._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
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

**Kezdje itt:** [Válassza ki a munkafolyamatot](https://azure.github.io/co-op-translator/workflows/) | [Konfiguráció](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Többnyelvű támogatás

#### Támogatott a [Co-op Translator](https://github.com/Azure/co-op-translator) által

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arab](../ar/README.md) | [Bengáli](../bn/README.md) | [Bolgár](../bg/README.md) | [Burmai (Mianmar)](../my/README.md) | [Kínai (egyszerűsített)](../zh-CN/README.md) | [Kínai (hagyományos, Hongkong)](../zh-HK/README.md) | [Kínai (hagyományos, Makaó)](../zh-MO/README.md) | [Kínai (hagyományos, Tajvan)](../zh-TW/README.md) | [Horvát](../hr/README.md) | [Cseh](../cs/README.md) | [Dán](../da/README.md) | [Holland](../nl/README.md) | [Észt](../et/README.md) | [Finn](../fi/README.md) | [Francia](../fr/README.md) | [Német](../de/README.md) | [Görög](../el/README.md) | [Héber](../he/README.md) | [Hindi](../hi/README.md) | [Magyar](./README.md) | [Indonéz](../id/README.md) | [Olasz](../it/README.md) | [Japán](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Koreai](../ko/README.md) | [Litván](../lt/README.md) | [Maláj](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepáli](../ne/README.md) | [Nigériai pidgin](../pcm/README.md) | [Norvég](../no/README.md) | [Perzsa (Fárszi)](../fa/README.md) | [Lengyel](../pl/README.md) | [Portugál (Brazília)](../pt-BR/README.md) | [Portugál (Portugália)](../pt-PT/README.md) | [Pandzsábi (Gurmukhi)](../pa/README.md) | [Román](../ro/README.md) | [Orosz](../ru/README.md) | [Szerb (cirill)](../sr/README.md) | [Szlovák](../sk/README.md) | [Szlovén](../sl/README.md) | [Spanyol](../es/README.md) | [Svahili](../sw/README.md) | [Svéd](../sv/README.md) | [Tagalog (filippínó)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Török](../tr/README.md) | [Ukrán](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnami](../vi/README.md)

> **Szeretne helyben klónozni?**
>
> Ez a tároló 50+ nyelvű fordítást tartalmaz, ami jelentősen megnöveli a letöltési méretet. Ha a fordítások nélkül szeretne klónozni, használja a sparse checkout-ot:
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
> Ez mindent megad, amire szüksége van a kurzus elvégzéséhez sokkal gyorsabb letöltéssel.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Áttekintés

A **Co-op Translator** segít egyszerűen lokalizálni oktatási GitHub-tartalmait több nyelvre.
Amikor frissíti Markdown fájljait, képeit vagy jegyzeteit, a fordítások automatikusan szinkronban maradnak, biztosítva, hogy tartalma pontos és naprakész maradjon a tanulók számára világszerte.

Használja a parancssorból (CLI) tárházfordításhoz, a Python API-ból automatizáláshoz, vagy az MCP szerveren ügynök- és szerkesztői munkafolyamatokhoz.

Példa arra, hogyan van rendszerezve a lefordított tartalom:

![Példa](../../imgs/translation-ex.png)

## Miért a Co-op Translator?

Egy fájl fordítása egyszerű. Egy teljes dokumentációs tárház
fordításának, linkelésének és naprakészen tartásának biztosítása a nehéz része.

| Probléma | Hogyan segít a Co-op Translator |
| --- | --- |
| Hosszú dokumentumok nem egyetlen prompt | A nagy Markdown fájlokat darabokra bontjuk, így egy hosszú README nem függ egyetlen sérülékeny modellválasztól. Ha egy darab megbukik, a Co-op Translator újrapróbálkozhat és csak a sikertelen részt bonthatja újra. |
| A hiányos fordítások ne legyenek jelölve naprakésznek | Egy csonkított fordítás soha ne legyen lezárva naprakészként. A Co-op Translator ellenőrzi a fordítás integritását mentés előtt, és képes felismerni szerkezetileg hiányos meglévő fordításokat. |
| A linkeknek illeszkedniük kell a lefordított repo struktúrájához | A manuális fordítások gyakran hagynak relatív linkeket, amelyek visszamutatnak az eredeti fájlszerkezetre. A Co-op Translator átírja a Markdown-, jegyzet-, kép- és README-linkeket, hogy illeszkedjenek a `translations/<lang>/...` struktúrához. |
| A fordításnak az egész repo-nak működnie kell | A Co-op Translator kezeli a README fájlokat, a dokumentációkat, a jegyzeteket és a képszöveget egyetlen tárház-munkafolyamat részeként, ahelyett, hogy fájlonként fordítana. |
| A fordítások karbantartása fontosabb, mint egyszeri létrehozásuk | Forrás-hash-ek és fordítási metaadatok segítségével a Co-op Translator megtalálja az elavult fájlokat, kihagyja a nem változott fájlokat, és szinkronban tartja a lefordított tartalmat, ahogy a forrásrepo fejlődik. |

## Hogyan kezelik a fordítás állapotát

A Co-op Translator a lefordított tartalmakat **verziózott szoftver-artefaktumokként**,  
nem statikus fájlokként kezeli.

Az eszköz nyelvi hatókörű metaadatok segítségével követi a lefordított Markdown, képek és jegyzetek állapotát.

Ez a kialakítás lehetővé teszi a Co-op Translator számára, hogy:

- Megbízhatóan észlelje az elavult fordításokat
- Következetesen kezelje a Markdown-t, képeket és jegyzeteket
- Biztonságosan skálázható legyen nagy, gyorsan változó, többnyelvű tárházak esetén

Azáltal, hogy a fordításokat kezelt artefaktumokként modellezi,
a fordítási munkafolyamatok természetesen illeszkednek a modern
szoftverfüggőségi és artefaktum-kezelési gyakorlatokhoz.

→ [Hogyan kezelik a fordítás állapotát](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Kapcsolódó mélyebb elemzések

- [A törött Markdown javítása AI-fordításnál: Egy gyártási pipeline megerősítése](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Kezdjen hozzá

A Co-op Translator használható a CLI-ből, a Python API-ból vagy az MCP szerverből. Kezdje a munkafolyamat útmutatóval, ha a helyi fordítás, automatizálás, CI és ügynök/szerkesztő integráció között választ.

- [Válassza ki a munkafolyamatot](../../docs/workflows.md)
- [Hitelesítő adatok konfigurálása](../../docs/configuration.md)
- [Fordítás a CLI-ből](../../docs/cli.md)
- [Automatizálás a Python API-val](../../docs/api.md)
- [Kapcsolódás az MCP szerverrel](../../docs/mcp.md)
- [Futtatás GitHub Actions-ben](../../docs/github-actions.md)

Minimális CLI példa a konfiguráció után:

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

Nagy tárházak első futtatásaihoz használja a `--dry-run` opciót, mielőtt valóban írna lefordított fájlokat. Lásd a [CLI Reference](../../docs/cli.md) részt a tartalomtípus-flagek, naplók, felülvizsgálat és linkmigráció kapcsán.

Konténer gyors futtatás Bash/Zsh alatt:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Konténer gyors futtatás PowerShell alatt:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Funkciók

- Automatikus fordítás Markdownhoz, jegyzetekhez és képekhez
- A fordítások szinkronban tartása a forrásváltozásokkal
- Helyben (CLI) vagy CI-ben (GitHub Actions) működik
- Markdown, jegyzet, kép, felülvizsgálat és projektfordítási eszközöket tesz elérhetővé MCP-n keresztül
- Azure OpenAI-t vagy OpenAI-t használ szolgáltatóként a fordításhoz
- Lehetővé teszi, hogy az MCP hosztolt ügynökei LLM hitelesítő adatok nélkül fordítsanak Markdown és jegyzet darabokat
- Azure AI Vision-t használ a képszöveg kinyeréséhez és fordításához
- Determinisztikus ellenőrzésekkel vizsgálja a fordítás szerkezetét és frissességét
- Megőrzi a Markdown formázását és szerkezetét

## Dokumentáció

- [Dokumentációs oldal](https://azure.github.io/co-op-translator/)
- [Válassza ki a munkafolyamatot](../../docs/workflows.md)
- [Konfiguráció](../../docs/configuration.md)
- [Azure AI beállítása](../../docs/azure-ai-setup.md)
- [CLI referencia](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README nyelvek sablonja](../../docs/readme-languages-template.md)
- [Támogatott nyelvek](../../docs/supported-languages.md)
- [Hozzájárulás](../../CONTRIBUTING.md)
- [Hibaelhárítás](../../docs/troubleshooting.md)

### Microsoft-specifikus útmutató
> [!NOTE]
> Csak a Microsoft “For Beginners” tárolók karbantartói számára.

- [A „további kurzusok” lista frissítése (csak MS Beginners tárolókhoz)](../../docs/microsoft-beginners.md)

## Támogasson minket és segítse a globális tanulást

Csatlakozzon hozzánk az oktatási tartalmak globális megosztásának forradalmasításában! Adjon egy ⭐-t a [Co-op Translator](https://github.com/azure/co-op-translator) projektnek a GitHubon, és támogassa küldetésünket, hogy lebontsuk a nyelvi akadályokat a tanulásban és a technológiában. Az Ön érdeklődése és hozzájárulásai jelentős hatással vannak! Kódbeli hozzájárulások és funkciójavaslatok mindig szívesen fogadottak.

### Fedezze fel a Microsoft oktatási tartalmait az Ön nyelvén
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

## Video presentations

👉 Kattints a lentebbi képre a YouTube-on való megtekintéshez.

- **Open at Microsoft**: Rövid, 18 perces bevezető és gyors útmutató a Co-op Translator használatához.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contributing

Ez a projekt örömmel fogadja a hozzájárulásokat és javaslatokat. Érdekel a hozzájárulás az Azure Co-op Translatorhoz? Kérjük, olvasd el a [CONTRIBUTING.md](../../CONTRIBUTING.md) fájlunkat az útmutatásért, hogyan segíthetsz abban, hogy a Co-op Translator hozzáférhetőbb legyen.

## Contributors

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code of Conduct

Ez a projekt elfogadta a [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) dokumentumát.
További információért lásd a [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) oldalt, vagy
lépj kapcsolatba az [opencode@microsoft.com](mailto:opencode@microsoft.com) címen további kérdésekkel vagy észrevételekkel.

## Responsible AI

A Microsoft elkötelezett amellett, hogy segítse ügyfeleit AI termékeink felelősségteljes használatában, megossza tapasztalatait, és bizalmon alapuló partnerségeket építsen olyan eszközökkel, mint az Átláthatósági jegyzetek és a Hatásvizsgálatok. Ezeknek az erőforrásoknak nagy része megtalálható a [https://aka.ms/RAI](https://aka.ms/RAI) címen.
A Microsoft felelős MI-hez való megközelítése a méltányosság, megbízhatóság és biztonság, adatvédelem és biztonság, inkluzivitás, átláthatóság és elszámoltathatóság elvein alapul.

A nagyméretű nyelvi, képi és beszédmodellek - mint amilyeneket ebben a példában is használunk - potenciálisan igazságtalanul, megbízhatatlanul vagy sértően viselkedhetnek, ami károkat okozhat. Kérjük, tekintse meg az [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) dokumentumot, hogy tájékozódjon a kockázatokról és korlátokról.

A kockázatok mérséklésének javasolt megközelítése, hogy a rendszerbe olyan biztonsági réteget építsen, amely képes észlelni és megakadályozni a káros viselkedést. Az [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) független védelmi réteget kínál, amely képes felismerni a felhasználók által létrehozott és az MI által generált káros tartalmakat alkalmazásokban és szolgáltatásokban. Az Azure AI Content Safety szöveg- és kép-API-kat tartalmaz, amelyek lehetővé teszik a káros anyagok felismerését. Emellett interaktív Content Safety Studio-t is biztosítunk, amely lehetővé teszi a mintakódok megtekintését, felfedezését és kipróbálását a különböző modalitásokban történő káros tartalom észleléséhez. A következő [quickstart dokumentáció](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) végigvezeti a szolgáltatásnak küldött kérelmek létrehozásán.

Egy másik szempontra érdemes figyelni az alkalmazás teljesítményét. Többmodalitású és többmodellű alkalmazások esetén a teljesítmény azt jelenti, hogy a rendszer úgy működik, ahogy te és a felhasználóid elvárják, beleértve azt is, hogy nem generál káros kimeneteket. Fontos értékelni az alkalmazás teljesítményét a [generálás minőségére és kockázat- és biztonsági metrikákra vonatkozó](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) mutatók használatával.

Fejlesztési környezetében kiértékelheti MI alkalmazását a [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) használatával. Legyen szó tesztadatkészletről vagy célról, a generatív MI alkalmazás kimenetei kvantitatívan mérhetők beépített értékelőkkel vagy az Ön által választott egyedi értékelőkkel. A prompt flow sdk-val való értékelés megkezdéséhez kövesse a [quickstart útmutatót](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Miután végrehajtott egy értékelést, [vizualizálhatja az eredményeket az Azure AI Studio-ban](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Trademarks

Ez a projekt tartalmazhat védjegyeket vagy logókat projektekhez, termékekhez vagy szolgáltatásokhoz kapcsolódóan. A Microsoft védjegyeinek vagy logóinak engedélyezett használata a [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) szabályainak és feltételeinek megfelelően történhet.
A Microsoft védjegyeinek vagy logóinak használata a projekt módosított változataiban nem okozhat félreértést és nem sugallhat Microsoft általi támogatást.
Harmadik felek védjegyeinek vagy logóinak használata a vonatkozó harmadik fél irányelveinek hatálya alá tartozik.

## Getting Help

Ha elakad vagy kérdése van az MI-alkalmazások építésével kapcsolatban, csatlakozz:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ha termékvisszajelzése van vagy hibába ütközik a fejlesztés során, látogasson el:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)