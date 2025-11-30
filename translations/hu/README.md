<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T12:04:50+00:00",
  "source_file": "README.md",
  "language_code": "hu"
}
-->
# Co-op Fordító

_Könnyedén automatizáld oktatási GitHub tartalmad fordítását több nyelvre, hogy globális közönséget érhess el._

[![Python csomag](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Licenc: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Letöltések](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Letöltések](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Konténer: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Kódstílus: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub közreműködők](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub hibák](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-kérelmek](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PR-k üdvözölve](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Többnyelvű támogatás

#### A [Co-op Translator](https://github.com/Azure/Co-op-Translator) támogatásával

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arab](../ar/README.md) | [Bengáli](../bn/README.md) | [Bolgár](../bg/README.md) | [Burmai (Myanmar)](../my/README.md) | [Kínai (egyszerűsített)](../zh/README.md) | [Kínai (hagyományos, Hongkong)](../hk/README.md) | [Kínai (hagyományos, Makaó)](../mo/README.md) | [Kínai (hagyományos, Tajvan)](../tw/README.md) | [Horvát](../hr/README.md) | [Cseh](../cs/README.md) | [Dán](../da/README.md) | [Holland](../nl/README.md) | [Észt](../et/README.md) | [Finn](../fi/README.md) | [Francia](../fr/README.md) | [Német](../de/README.md) | [Görög](../el/README.md) | [Héber](../he/README.md) | [Hindi](../hi/README.md) | [Magyar](./README.md) | [Indonéz](../id/README.md) | [Olasz](../it/README.md) | [Japán](../ja/README.md) | [Kannada](../kn/README.md) | [Koreai](../ko/README.md) | [Litván](../lt/README.md) | [Maláj](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepáli](../ne/README.md) | [Nigériai pidgin](../pcm/README.md) | [Norvég](../no/README.md) | [Perzsa (Fárszi)](../fa/README.md) | [Lengyel](../pl/README.md) | [Portugál (Brazília)](../br/README.md) | [Portugál (Portugália)](../pt/README.md) | [Pandzsábi (Gurmukhi)](../pa/README.md) | [Román](../ro/README.md) | [Orosz](../ru/README.md) | [Szerb (cirill)](../sr/README.md) | [Szlovák](../sk/README.md) | [Szlovén](../sl/README.md) | [Spanyol](../es/README.md) | [Szuahéli](../sw/README.md) | [Svéd](../sv/README.md) | [Tagalog (filippínó)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Török](../tr/README.md) | [Ukrán](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnami](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub figyelők](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forkok](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub csillagok](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Megnyitás GitHub Codespaces-ben](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Áttekintés

A **Co-op Translator** segít egyszerűen több nyelvre lokalizálni oktatási GitHub tartalmadat.
Amikor frissíted a Markdown fájlokat, képeket vagy jegyzetfüzeteket, a fordítások automatikusan szinkronban maradnak, így a tartalom pontos és naprakész marad a világ minden táján tanulók számára.

Példa a fordított tartalom szervezésére:

![Példa](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.hu.png)

## Gyors kezdés

```bash
# Hozzon létre és aktiváljon egy virtuális környezetet (ajánlott)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Telepítse a csomagot
pip install co-op-translator
# Fordítás
translate -l "ko ja fr" -md
```

Docker:

```bash
# Húzza le a nyilvános képet a GHCR-ről
docker pull ghcr.io/azure/co-op-translator:latest
# Futtassa a jelenlegi mappával csatolva és a .env fájl megadva (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimális beállítás

1. Hozz létre egy `.env` fájlt a sablon alapján: [.env.template](../../.env.template)
2. Állíts be egy LLM szolgáltatót (Azure OpenAI vagy OpenAI)
3. (Opcionális) Képfordításhoz (`-img`) állítsd be az Azure AI Vision-t
4. (Ajánlott) Tisztítsd meg az előző fordításokat az ütközések elkerülése érdekében (pl. `translations/`)
5. (Ajánlott) Adj hozzá egy fordítási szekciót a README-hez a [README nyelvi sablon](./getting_started/README_languages_template.md) segítségével
6. Lásd: [Azure AI beállítása](./getting_started/set-up-azure-ai.md)

## Használat

Fordítsd le az összes támogatott típust:

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

Csak jegyzetfüzetek:

```bash
translate -l "zh" -nb
```

További kapcsolók: [Parancs referencia](./getting_started/command-reference.md)

## Jellemzők

- Automatikus fordítás Markdown, jegyzetfüzetek és képek esetén
- A fordítások szinkronban maradnak a forrással
- Helyi használat (CLI) vagy CI-ben (GitHub Actions)
- Azure OpenAI vagy OpenAI használata; opcionális Azure AI Vision képekhez
- Megőrzi a Markdown formázást és szerkezetet

## Dokumentáció

- [Parancssori útmutató](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions útmutató (nyilvános tárolók és standard titkok)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions útmutató (Microsoft szervezeti tárolók és szervezeti beállítások)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README nyelvi sablon](./getting_started/README_languages_template.md)
- [Támogatott nyelvek](./getting_started/supported-languages.md)
- [Hozzájárulás](./CONTRIBUTING.md)
- [Hibaelhárítás](./getting_started/troubleshooting.md)

### Microsoft-specifikus útmutató
> [!NOTE]
> Csak a Microsoft „Kezdőknek” tárolóinak karbantartói számára.

- [„Egyéb kurzusok” lista frissítése (csak MS Kezdők tárolókhoz)](./getting_started/update-other-courses.md)

## Támogass minket és segítsd a globális tanulást

Csatlakozz hozzánk, hogy forradalmasítsuk az oktatási tartalmak globális megosztását! Adj egy ⭐-t a [Co-op Translator](https://github.com/azure/co-op-translator) projektnek a GitHubon, és támogasd küldetésünket, hogy lebontsuk a nyelvi akadályokat a tanulás és technológia terén. Az érdeklődésed és hozzájárulásaid nagy hatással vannak! Kódhozzájárulásokat és funkciójavaslatokat mindig szívesen fogadunk.

### Fedezd fel a Microsoft oktatási tartalmait a saját nyelveden

- [AZD kezdőknek](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI kezdőknek](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) kezdőknek](https://github.com/microsoft/mcp-for-beginners)
- [AI ügynökök kezdőknek](https://github.com/microsoft/ai-agents-for-beginners)
- [Generatív AI kezdőknek .NET használatával](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generatív AI kezdőknek](https://github.com/microsoft/generative-ai-for-beginners)
- [Generatív AI kezdőknek Java használatával](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML kezdőknek](https://aka.ms/ml-beginners)
- [Adattudomány kezdőknek](https://aka.ms/datascience-beginners)
- [AI kezdőknek](https://aka.ms/ai-beginners)
- [Kiberbiztonság kezdőknek](https://github.com/microsoft/Security-101)
- [Webfejlesztés kezdőknek](https://aka.ms/webdev-beginners)
- [IoT kezdőknek](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Videó bemutatók

👉 Kattints az alábbi képre a YouTube-on való megtekintéshez.

- **Open at Microsoft**: Egy rövid, 18 perces bevezető és gyors útmutató a Co-op Translator használatához.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.hu.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Hozzájárulás

Ez a projekt szívesen fogad hozzájárulásokat és javaslatokat. Érdekel, hogy hozzájárulj az Azure Co-op Translator fejlesztéséhez? Kérjük, olvasd el a [CONTRIBUTING.md](./CONTRIBUTING.md) fájlt, ahol útmutatást találsz arról, hogyan teheted elérhetőbbé a Co-op Translator-t.

## Közreműködők

[![co-op-translator közreműködők](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Magatartási kódex

Ez a projekt elfogadta a [Microsoft nyílt forráskódú magatartási kódexét](https://opensource.microsoft.com/codeofconduct/).
További információkért lásd a [Magatartási kódex GYIK](https://opensource.microsoft.com/codeofconduct/faq/) oldalt, vagy
keresd az [opencode@microsoft.com](mailto:opencode@microsoft.com) címet további kérdésekkel vagy észrevételekkel.

## Felelős mesterséges intelligencia

A Microsoft elkötelezett amellett, hogy ügyfeleink felelősségteljesen használják AI termékeinket, megosztja tapasztalatait, és bizalmon alapuló partnerségeket épít olyan eszközökkel, mint az Átláthatósági jegyzetek és Hatásértékelések. Ezeknek az erőforrásoknak sok megtalálható a [https://aka.ms/RAI](https://aka.ms/RAI) címen.
A Microsoft felelős AI megközelítése az igazságosság, megbízhatóság és biztonság, adatvédelem és biztonság, befogadás, átláthatóság és elszámoltathatóság AI elvein alapul.

A nagyméretű természetes nyelvi, képi és beszédmodellek – mint amilyenek ebben a példában is használatosak – potenciálisan igazságtalan, megbízhatatlan vagy sértő módon viselkedhetnek, ami károkat okozhat. Kérjük, tekintsd meg az [Azure OpenAI szolgáltatás Átláthatósági jegyzetét](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), hogy tájékozódj a kockázatokról és korlátokról.
A kockázatok csökkentésére javasolt megközelítés, hogy az architektúrádba beépítesz egy biztonsági rendszert, amely képes felismerni és megakadályozni a káros viselkedést. Az <a href="https://learn.microsoft.com/azure/ai-services/content-safety/overview">Azure AI Content Safety</a> egy független védelmi réteget biztosít, amely képes észlelni a káros, felhasználók vagy mesterséges intelligencia által generált tartalmakat alkalmazásokban és szolgáltatásokban. Az Azure AI Content Safety szöveg- és képi API-kat tartalmaz, amelyek lehetővé teszik a káros anyagok felismerését. Emellett rendelkezünk egy interaktív Content Safety Studioval, amelyben megtekintheted, felfedezheted és kipróbálhatod a káros tartalmak különböző modalitásokban történő felismerésére szolgáló mintakódokat. A következő <a href="https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest">gyorsindítási dokumentáció</a> végigvezet a szolgáltatásnak küldött kérések elkészítésén.

Egy másik szempont, amit figyelembe kell venni, az alkalmazás általános teljesítménye. Többmodalitású és többmodellű alkalmazások esetén a teljesítmény azt jelenti, hogy a rendszer úgy működik, ahogy te és a felhasználóid elvárják, beleértve azt is, hogy nem generál káros kimeneteket. Fontos, hogy az egész alkalmazás teljesítményét értékeld a <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in">generálási minőség és kockázat- és biztonsági mutatók</a> segítségével.

Az AI alkalmazásodat a fejlesztői környezetedben is értékelheted a <a href="https://microsoft.github.io/promptflow/index.html">prompt flow SDK</a> használatával. Egy tesztadatkészlet vagy cél alapján a generatív AI alkalmazásod generálásait mennyiségileg mérik beépített vagy általad választott egyedi értékelők. Ha szeretnéd elkezdeni a prompt flow SDK-val a rendszered értékelését, kövesd a <a href="https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk">gyorsindítási útmutatót</a>. Az értékelési futtatás végrehajtása után az eredményeket meg is jelenítheted az <a href="https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results">Azure AI Studioban</a>.

## Védjegyek

Ez a projekt tartalmazhat védjegyeket vagy logókat projektekhez, termékekhez vagy szolgáltatásokhoz. A Microsoft védjegyek vagy logók jogosult használata a <a href="https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general">Microsoft védjegy- és márka irányelveinek</a> betartásával történhet. A Microsoft védjegyek vagy logók módosított verziókban történő használata nem okozhat félreértést, és nem sugallhat Microsoft támogatást. Harmadik fél védjegyeinek vagy logóinak használata a harmadik fél szabályzatai szerint történik.

## Segítségkérés

Ha elakadsz vagy kérdésed van az AI alkalmazások fejlesztésével kapcsolatban, csatlakozz:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ha termék-visszajelzésed vagy hibajelentésed van fejlesztés közben, látogass el ide:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->