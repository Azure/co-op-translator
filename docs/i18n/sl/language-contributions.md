# Prispevanje k izboljšavam jezikov

Vaše znanje jezika lahko pomaga izboljšati Co-op Translator. Začnite z enim primerom, predlaganim popravkom in razlago prek [obrazca za povratne informacije o prevodu](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Ni vam treba pisati kode ali plačati za zagon modela.

## Od poročila do skupne izboljšave

1. Prispevalec predloži izsek iz izvirnika, prevod in kontekst.
2. Jezikovni pregledovalec preveri pomen, naravnost in ali je predlog odvisen od določene lokalne različice ali tečaja.
3. Vzdrževalec odloči, ali popravek spada v izvorni tečaj, skupno jezikovno navodilo, konfiguracijo terminologije ali prevajalsko kodo.
4. Za skupno pravilo vzdrževalec primerja izhode pred in po spremembi na prijavljenem primeru in na nepovezanih primerih. Prispevalci lahko pregledajo te izhode, ne da bi sami zagnali orodje.
5. Rezultirajoči PR poveže poročilo in pripiše zasluge ljudem, ki so prispevali primere in pregled. Namestitev ali ponovno generiranje v porabniških repozitorijih je ločen korak.

Poročilo ne spremeni samodejno pozivov ali ne regenerira prevodov tečaja. Popravki, specifični za tečaj, naj ostanejo povezani z repozitorijem tečaja. Ne predvidevajte, da bo ročna ureditev preživela kasnejše ponovne prevode; potrdite vedenje za ta potek dela.

## Obstoječi primer: japonske Markdown povezave

[japonska datoteka z navodili](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) modelu naroči, naj prevede besedilo povezave ob ohranitvi Markdown sintakse in cilja povezave. Na primer, povezava, zapisana kot `[text](URL)`, ne sme postati `「text」（URL）`.

To je osrednji primer jezikovnega pravila, podprt z ilustracijo pravilne in nepravilne izhodne vsebine. Ni pa to dokaz, da navodila v pozivu sama po sebi zagotavljajo pravilno obravnavo Markdowna.

[Graditelj Markdown pozivov](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) naloži `templates/language/<language_code>.md` z jezikovno kodo, ki je zapisana z malimi črkami in obrezana. Če datoteka ne obstaja, uporabi splošna navodila. To opisuje pot poziva za Markdown; ne predvidevajte, da vsaka slika ali druga pot prevajanja uporablja ista navodila.

[Testi pozivov](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) preverjajo, ali so japonska navodila vključena. To preverja sestavo poziva, ne pa kakovost prevoda.

## Kaj spada v jezikovno pravilo?

Predlagajte ozko, ponovljivo popravilo z izvirnim primerom, pričakovanim vedenjem in protiprimerom, kjer pravilo ne sme veljati. Ohranite pomen, nadomestne oznake, kodo, URL-je in strukturo dokumenta. Izogibajte se spreminjanju slogovnih preferenc posameznika ali terminologije enega tečaja v univerzalno pravilo.

Trenutna [implementacija glosarja](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) ščiti izraze pred prevajanjem. Ni slovar terminologije iz vira v cilj. Preden obljubite novo obnašanje terminologije prispevalcem, se o njem pogovorite.

## Primer skupnosti: japonsko poročilo o imenu izdelka

V [poročilu #527](https://github.com/Azure/co-op-translator/issues/527) je @hyoshioka0128 odkril japonski prevod, ki je spremenil ime izdelka `Co-op Translator` v `Co-op 翻訳`. Poročilo je vključevalo povezavo do prizadetega dokumenta in posnetek zaslona, kar je olajšalo iskanje problema.

Prispevalec je prav tako priložil [sorodni PR tečaja](https://github.com/microsoft/AZD-for-beginners/pull/109). V razpravi o težavi je vzdrževalec priznal poročilo in predlagal preiskavo, zakaj se je ime spremenilo, vključno z zaščito terminologije, delovanjem glosarja in potjo prevajanja.

To pokaže, kako lahko majhno poročilo podpira preiskavo, ki presega posamezni popravek besedila. Ni pa to preverjen rezultat "pred/po" niti dokaz, da so zgornja japonska navodila za Markdown-povezave rešila to težavo z imenom izdelka.

Lahko prispevate enako: delite izvirno besedilo, trenutni prevod, predlagani popravek in zakaj je to pomembno. Dodajte povezavo do dokumenta ali posnetek zaslona, kadar je to koristno. Ni vam treba diagnosticirati vzroka ali napisati poziva, preden ga prijavite.

## Validacija pred sprejetjem pravila

Uporabite iste vzorce vira, revizijo prevoda, ponudnika/model in nastavitve generiranja za osnovne in kandidatne zagone, spreminjajoč le predlagano navodilo. Zabeležite dejansko spremembo poziva in izhode; ponovite primere po potrebi, da ločite dosleden učinek od spremenljivosti izhodov. Vključite prijavljeno napako, nasprotujoče kontekste in primere, ki se že pravilno prevajajo.

| Vzorec | Vir/kontekst | Izhod izhodišča | Izhod kandidata | Ocena recenzenta |
| --- | --- | --- | --- | --- |
| Prijavljena napaka | Za zbrati | Ni zagnano | Ni zagnano | Čaka |
| Proti primer | Za zbrati | Ni zagnano | Ni zagnano | Čaka |
| Neprizadet primer | Za zbrati | Ni zagnano | Ni zagnano | Čaka |

Preverite strukturne invariance ločeno od jezikovnih ocen. Uspešen preizkus nalaganja poziva ni ocena kakovosti, in ena točno pričakovana poved ni edini veljaven prevod. Če manjkajo kontekst, zagoni modela ali jezikovni pregled, obdržite predlog v čakanju namesto da trdite, da je težava rešena.