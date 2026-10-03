# Fordíts, szerkessz és ellenőrizz egy kis projektet

Kezdd két rövid Markdown fájllal és egy célnyelvvel. Meglátod, hova kerülnek a fordítások, mi történik, ha a forrás változik, és hogyan ellenőrizheted az eredményt.

## Rögzített eredmények

A példát 2026. szeptember 19-én futtatták a Co-op Translator 0.21.0-val és az Azure OpenAI-vel (`gpt-5-mini`). A módosítatlan CLI parancsokat a Click `CliRunner`-én keresztül hívták meg a lefordított wheel és a meglévő Python-függőségek használatával.

| Lépés | Eredmény |
| --- | --- |
| Előnézet | Kilépés 0; nem kértek modell-fordítást |
| Kezdeti fordítás | Kilépés 0; 27.36 másodperc |
| Kezdeti ellenőrzés | Kilépés 0 |
| README szerkesztése és ellenőrzése | Kilépés 1; elavult fordítás észlelve |
| Fordítás frissítése | Kilépés 0; 22.17 másodperc |
| Ellenőrzés frissítés után | Kilépés 0; hibák és figyelmeztetések nélkül |
| Változatlan útmutató | Azonos bájtok a README frissítése előtt és után |
| Futtatás újra | Kilépés 0; az összes fordítási fájl hash-ének egyezése |

Ezek egyedi futtatási mérések, nem teljesítménygaranciák. A beállítási idő nincs benne; a szolgáltató számlázása nem volt mérve. Egy változatlan futtatás továbbra is végezhet szolgáltató-állapotellenőrzést.

Tekintsd meg a [kezdeti fordítást](../../assets/demo/before.txt), [frissített fordítást](../../assets/demo/after.txt), [teljes fordítási diffet](../../assets/demo/update.diff), [elavult ellenőrzést](../../assets/demo/review-stale.txt), [végső ellenőrzést](../../assets/demo/review-after.txt), és a [futtatás részleteit](../../assets/demo/results.json). A teljes fájl fordítása megváltoztathat más megfogalmazásokat, ahogy a rögzített diff mutatja. Mindkét szöveges anyag megtartja a generált záradékot.

Az emberi felülvizsgálat továbbra is számít: a rögzített frissítés a `[사용 가이드](guide.md)을` kifejezést használja; a koreai ragnak `[사용 가이드](guide.md)를`-nek kellene lennie. A szöveges anyagok ezt a kimenetet változtatás nélkül megtartják, ahelyett, hogy szerkesztett fordítást mutatnának modell-kimenetként. A szerkezeti ellenőrzés a megfogalmazási problémától függetlenül megfelel.

## 1. Készíts elő egy kis mappát

Használd a Python 3.11–3.14-et és a [virtuális környezet beállítását](configuration.md#local-runtime-setup). Telepítsd azt a verziót, amelyet ehhez a példához használtak:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Töltsd le a [README.txt](../../assets/demo/README.txt)-t és a [guide.txt](../../assets/demo/guide.txt)-t ebbe a mappába, és mentsd őket `README.md` és `guide.md` néven. Kis, fiktív projekt-dokumentumok; nincs szükség alkalmazás telepítésére.

A README tartalmaz egy kódblokkot és egy hivatkozást a `guide.md`-re. Az utolsó mondata:

```text
Notes are saved locally.
```

Tartsd ebben a mappában csak ezeket a két forrásdokumentumot. Az összes következő parancs a `translation-demo` belsejében fut, és működik Bash-ben és PowerShell-ben.

## 2. Előnézet hitelesítő adatok nélkül

```bash
translate -l "ko" -md --dry-run
```

Az előnézet megbecsüli a fordítási munkát anélkül, hogy modellt hívna meg vagy fordításokat írna. A tokenbecslések nem számlázási ajánlatok. Az első futtatásnak mindkét Markdown fájlt új munkaként kell azonosítania.

## 3. Válassz szolgáltatót és fordíts

Állíts be egy szolgáltatót a [konfigurációs útmutató](configuration.md) használatával: Azure OpenAI, OpenAI vagy Anthropic. Az OpenAI és az Anthropic szövegfordításhoz nem szükséges Azure-fiók. Kép-szolgáltatások nem kellenek ehhez a példához.

Ha helyi `.env` fájlt használsz, add hozzá a `.env`-t ennek a mappa `.gitignore` fájlához. A fordítási hívások a szolgáltatói fiókodat használják, és költségeket vonhatnak maguk után.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Nyisd meg a `translations/ko/README.md`-t és a `translations/ko/guide.md`-t. Ellenőrizd a koreai megfogalmazást, a kódblokkot, és a hivatkozást a lefordított README-ből a lefordított útmutatóra. A kimenet megfogalmazása modelltől függően változik.

`co-op-review` ellenőrzi a frissességet, a szerkezetet és a helyi hivatkozásokat. A sikeres eredmény nem tanúsítja a nyelvi pontosságot. Oldd meg a jelentett hibákat folytatás előtt.

Rögzítsd a sikeres alapállapotot Git-tel (ha szükséges, állítsd be először a Git-identitásodat):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Változtasd meg a forrást

A `README.md`-ben cseréld le a `Notes are saved locally.` szöveget erre:

```text
Notes are saved locally as Markdown files.
```

Hagyd a `guide.md`-t változatlanul. Ezután futtasd:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Az ellenőrzésnek a README fordítását elavultként kell jelentenie és sikertelenül ki kell lépnie. Ez a várt köztes állapot. Az előnézetnek munkát kell azonosítania a megváltozott README-hez.

## 5. Frissítsd és vizsgáld meg a diffet

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Vizsgáld meg a valós diffet: az alapértelmezett CLI újrafordítja a megváltozott fájlt, így a modell más megfogalmazásokat is módosíthat abban a fájlban. A változatlan útmutatónak nem szabad diffet mutatnia. Az ellenőrzésnek többé nem szabad a README-t elavultként jelentenie; vizsgáld ki az egyéb észleléseket ahelyett, hogy figyelmen kívül hagynád őket.

A blokk-szintű emberi Markdown-szerkesztések megőrzéséhez opcionális fordítási állapot-szolgáltató szükséges a [Python API](api.md)-ban. Ez nincs engedélyezve ezekkel a CLI parancsokkal.

## 6. Futtasd újra változtatások nélkül

Commitáld a frissített forrást és fordítást:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

A jelenlegi fordításokkal és változatlan konfigurációval a fordító kihagyja a fájlokat. Az utolsó Git-parancsnak nem szabad diffet előállítania és sikeresen kell kilépnie.

## Következő lépések

- [Csak egy README fordítása és pull request nyitása](github-actions.md#your-first-readme-translation-pr).
- [Válassz CLI-t, Python API-t vagy MCP-t](workflows.md).
- [Jelents problémát a fordítással kapcsolatban kódolás nélkül](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).