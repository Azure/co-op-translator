# Prisidėjimas prie kalbos patobulinimų

Jūsų kalbos žinios gali padėti pagerinti Co-op Translator. Pradėkite su pavyzdžiu, siūloma pataisa ir paaiškinimu naudodamiesi [vertimo atsiliepimų forma](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Jums nereikia rašyti kodo arba mokėti už modelio paleidimą.

## Nuo pranešimo iki bendro patobulinimo

1. Prisidėjęs asmuo pateikia šaltinio ištrauką, jos vertimą ir kontekstą.
2. Kalbos peržiūrėtojas patikrina prasmę, natūralumą ir ar pasiūlymas priklauso nuo konkrečios lokalės ar kurso.
3. Prižiūrėjas nusprendžia, ar pataisa priklauso šaltinio kursui, bendroms kalbos instrukcijoms, terminologijos konfigūracijai ar vertimo kodui.
4. Dėl bendros taisyklės prižiūrėjas palygina išvestis prieš ir po pakeitimo praneštame pavyzdyje ir nesusijusiuose pavyzdžiuose. Prisidėjusieji gali peržiūrėti šias išvestis neįjungdami įrankio patys.
5. Gautas PR susieja pranešimą ir priskiria kreditus žmonėms, pateikusiems pavyzdžius ir peržiūrą. Diegimas arba regeneravimas naudojančiuose saugyklose yra atskiras žingsnis.

Pranešimas automatiškai nekeičia užklausų arba nepergeneruoja kurso vertimų. Kursui būdingos pataisos turėtų likti susietos su kurso saugykla. Neprielaikaukite, kad rankinis redagavimas išliks po vėlesnio pervertimo; patvirtinkite tokio darbo eigos elgesį.

## Esamas pavyzdys: japonų Markdown nuorodos

Šis [japonų instrukcijų failas](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) informuoja modelį, kad reikia išversti nuorodos tekstą, išsaugant Markdown sintaksę ir nuorodos paskirties vietą. Pavyzdžiui, nuoroda, užrašyta kaip `[text](URL)`, neturi tapti `「text」（URL）`.

Tai yra sutelktas kalbos taisyklės pavyzdys, paremta teisingos ir neteisingos išvesties iliustracija. Tai nėra įrodymas, kad vien tik užklausos instrukcijos garantuoja teisingą Markdown.

Šis [Markdown paraginio kūrėjas](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) įkrauna `templates/language/<language_code>.md` naudodamas mažosiomis raidemis parašytą, apkarpytą kalbos kodą. Jei tokio failo nėra, jis naudoja bendrąsias instrukcijas. Tai aprašo Markdown paraginimo kelią; nesiimkite manyti, kad kiekvienas paveikslėlis ar kitas vertimo kelias naudoja tas pačias instrukcijas.

Šie [prompt testai](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) tikrina, ar japonų instrukcijos yra įtrauktos. Tai patvirtina prompto sudarymą, o ne vertimo kokybę.

## Ką turi apimti kalbos taisyklė?

Pasiūlykite siaurą, pakartotiną pataisą su šaltinio pavyzdžiu, tikiminuosiu elgesiu ir kontrapavyzdžiu, kuriame taisyklė neturėtų būti taikoma. Išsaugokite prasmę, vietos rezervavimo žymes, kodą, URL ir dokumento struktūrą. Venkite vieno žmogaus stiliaus pageidavimų ar vieno kurso terminologijos paversti universalia taisykle.

Dabartinė [glosarijaus implementacija](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) apsaugo terminus nuo vertimo. Tai nėra terminų žodynas nuo šaltinio iki tikslo. Aptarkite naują terminijos elgseną prieš žadant ją bendruomenės dalyviams.

## Bendruomenės pavyzdys: japonų produkto pavadinimo ataskaita

Pranešime [ataskaita #527](https://github.com/Azure/co-op-translator/issues/527) @hyoshioka0128 nustatė japonų vertimą, kuris pakeitė produkto pavadinimą `Co-op Translator` į `Co-op 翻訳`. Pranešime buvo nuoroda į paveiktą dokumentą ir ekrano kopija, todėl problemą buvo lengva rasti.

Prisidėjęs asmuo taip pat pridėjo nuorodą į [susijusį kurso PR](https://github.com/microsoft/AZD-for-beginners/pull/109). Diskusijoje dėl klausimo prižiūrėtojas patvirtino pranešimą ir pasiūlė ištirti, kodėl pavadinimas pasikeitė — įskaitant terminų apsaugą, glosoriaus elgseną ir vertimo kelią.

Tai parodo, kaip mažas pranešimas gali paremti tyrimą, kuris viršija pavienę žodžių pataisą. Tai nėra patvirtintas prieš/po rezultatas arba įrodymas, kad aukščiau pateiktos japonų Markdown-nuorodų instrukcijos išsprendė šią produkto pavadinimo problemą.

Galite prisidėti taip pat: pateikite originalų tekstą, esamą vertimą, siūlomą pataisymą ir paaiškinkite, kodėl tai svarbu. Prireikus pridėkite dokumento nuorodą arba ekrano kopiją. Jums nereikia diagnozuoti priežasties ar rašyti užklausą prieš pranešant.

## Patvirtinimas prieš taisyklės priėmimą

Naudokite tuos pačius šaltinio pavyzdžius, vertėjo reviziją, tiekėją/modelį ir generavimo nustatymus tiek palyginimo, tiek kandidato paleidimams, keisdami tik siūlomą instrukciją. Užfiksuokite faktinį paraginimo pokytį ir išvesčių rezultatus; kartokite pavyzdžius, kai reikia, kad atskirtumėte nuoseklų efektą nuo išvesties kintamumo. Įtraukite praneštą klaidą, kontrastuojančius kontekstus ir pavyzdžius, kurie jau verčiami teisingai.

| Pavyzdys | Šaltinis/kontekstas | Bazinis rezultatas | Kandidato rezultatas | Peržiūrėtojo įvertinimas |
| --- | --- | --- | --- | --- |
| Pranešta klaida | Surinkti | Nepaleista | Nepaleista | Laukiama |
| Kontrapavyzdžys | Surinkti | Nepaleista | Nepaleista | Laukiama |
| Nepaveiktas pavyzdys | Surinkti | Nepaleista | Nepaleista | Laukiama |

Patikrinkite struktūrinius invariantus atskirai nuo lingvistinių vertinimų. Sėkmingas užklausos įkėlimo testas nėra kokybės vertinimas, o vienas tikslus laukiamas sakinys nėra vienintelis galiojantis vertimas. Jei trūksta konteksto, modelio paleidimų ar kalbos peržiūros, palikite pasiūlymą laukiančioje būsenoje, o ne teigkite, kad problema išspręsta.