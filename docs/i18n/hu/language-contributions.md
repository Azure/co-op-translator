# Hozzájárulás a nyelvi fejlesztésekhez

Nyelvi tudásod segíthet a Co-op Translator fejlesztésében. Kezdd egy példával, egy javasolt javítással és egy magyarázattal a [fordítási visszajelző űrlap](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml) segítségével. Nem kell kódot írnod vagy fizetned egy modell futtatásáért.

## Egy jelentéstől a megosztott fejlesztésig

1. Egy közreműködő benyújt egy forrásrészletet, annak fordítását és a kontextust.
2. Egy nyelvi lektor ellenőrzi az értelemét, a természetességét és azt, hogy a javaslat függ-e egy adott helyi nyelvi beállítástól vagy kurzustól.
3. Egy karbantartó eldönti, hogy a javítás a forráskurzusba, egy megosztott nyelvi utasításba, a terminológiai beállításokba vagy a fordítási kódba tartozik-e.
4. Egy megosztott szabály esetén a karbantartó összehasonlítja a kimeneteket a változtatás előtti és utáni állapotban a bejelentett példán és független példákon. A közreműködők ezek ellenőrzését elvégezhetik anélkül, hogy maguk futtatnák az eszközt.
5. A létrejövő PR összekapcsolja a jelentést és megadja a kreditálást azoknak, akik példákat és lektorálást biztosítottak. A bevezetés vagy a fogyasztó tárolókban történő újragenerálás külön lépés.

Egy jelentés nem változtatja meg automatikusan a promptokat, és nem generálja újra a kurzusfordításokat. A kurzus-specifikus javításoknak a kurzus tárolójához kell kapcsolódniuk. Ne feltételezd, hogy egy kézi szerkesztés túléli a későbbi újrafordítást; erősítsd meg ennek a munkafolyamatnak a viselkedését.

## Meglévő példa: japán Markdown-hivatkozások

A [japán utasításfájl](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) azt mondja a modellnek, hogy fordítsa le a hivatkozás szövegét miközben megőrzi a Markdown szintaxist és a hivatkozás célját. Például egy link, amely `[text](URL)` formátumban van, nem válhat `「text」（URL）`.

Ez egy fókuszált példa egy nyelvi szabályra, amelyet a helyes és helytelen kimenet illusztrációja támaszt alá. Ez nem bizonyíték arra, hogy önmagukban a promptutasítások garantálják a helyes Markdown-t.

A [Markdown prompt-építő](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) betölti a `templates/language/<language_code>.md` fájlt egy kisbetűsre alakított, levágott nyelvkóddal. Ha nincs fájl, az általános utasításokat használja. Ez leírja a Markdown prompt útvonalát; ne feltételezd, hogy minden kép vagy más fordítási út ugyanazokat az utasításokat használja.

A [prompt tesztek](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) ellenőrzik, hogy a japán utasítások szerepelnek-e. Ez a prompt összeállítását igazolja, nem a fordítás minőségét.

## Mi tartozik egy nyelvi szabályba?

Javasolj egy szűk, ismételhető javítást forráspéldával, várt viselkedéssel és egy ellenspéldával, ahol a szabálynak nem szabad alkalmazódnia. Őrizd meg a jelentést, a helykitöltőket, a kódot, az URL-eket és a dokumentumszerkezetet. Kerüld el, hogy egy személy stíluspreferenciáját vagy egy kurzus terminológiáját általános szabállyá tedd.

A jelenlegi [szójegyzék-megoldás](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) megvédi a kifejezéseket a fordítástól. Ez nem egy forrás-cél terminológiai szótár. Vitassátok meg az új terminológiai viselkedést, mielőtt ilyet ígértek a közreműködőknek.

## Közösségi példa: egy japán terméknév-jelentés

A [jelentés #527](https://github.com/Azure/co-op-translator/issues/527) szerint @hyoshioka0128 egy japán fordítást azonosított, amely a terméknevet `Co-op Translator`-ról `Co-op 翻訳`-re változtatta. A jelentés tartalmazott linket az érintett dokumentumra és egy képernyőképet, így a probléma könnyen megtalálható volt.

A közreműködő linkelte a [kapcsolódó kurzus PR](https://github.com/microsoft/AZD-for-beginners/pull/109)-t is. A vita során a karbantartó elismerte a jelentést és javasolta annak kivizsgálását, miért változott a név, ideértve a terminológia védelmét, a szójegyzék viselkedését és a fordítási útvonalat.

Ez megmutatja, hogyan támogathat egy kis jelentés egy vizsgálatot az egyéni megfogalmazás-javításon túl. Ez nem egy ellenőrzött előtte/utána eredmény, és nem bizonyíték arra, hogy a fenti japán Markdown-hivatkozás-utasítások megoldották volna ezt a terméknév-problémát.

Ugyanígy hozzájárulhatsz: oszd meg az eredeti szöveget, a jelenlegi fordítást, a javasolt javítást és hogy miért fontos. Adj dokumentumlinket vagy képernyőképet, ha hasznos. Nem kell megállapítanod az okát vagy promptot írnod a bejelentés előtt.

## Érvényesítés a szabály elfogadása előtt

Használd ugyanazokat a forrásmintákat, a fordító verzióját, a szolgáltatót/modellt és a generálási beállításokat az alap és a jelölt futtatásokhoz, csak a javasolt utasítást változtatva. Rögzítsd a tényleges promptváltoztatást és a kimeneteket; ismételd meg a példákat, amikor szükséges, hogy megkülönböztesd az állandó hatást a kimenet ingadozásától. Add meg a bejelentett hibát, a kontrasztáló kontextusokat és azokat a példákat, amelyek már helyesen fordulnak.

| Minta | Forrás/kontextus | Alap kimenet | Jelölt kimenet | Lektor értékelése |
| --- | --- | --- | --- | --- |
| Bejelentett hiba | Összegyűjtendő | Nem futott | Nem futott | Függőben |
| Ellenspélda | Összegyűjtendő | Nem futott | Nem futott | Függőben |
| Nem érintett példa | Összegyűjtendő | Nem futott | Nem futott | Függőben |

Ellenőrizd a szerkezeti invariánsokat külön a nyelvi értékelésektől. Egy sikeres promptbetöltési teszt nem minőségértékelés, és egyetlen pontos elvárt mondat nem az egyetlen érvényes fordítás. Ha hiányzik a kontextus, a modellfuttatások vagy a nyelvi lektorálás, tartsd függőben a javaslatot ahelyett, hogy azt állítanád, a probléma megoldódott.