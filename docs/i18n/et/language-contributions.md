# Keele täiustustesse panustamine

Teie keeleoskus võib aidata parandada Co-op Translatorit. Alustage näitega, soovitatud paranduse ja selgitusega, kasutades [tõlke tagasisidevormi](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Teil ei ole vaja kirjutada koodi ega maksta mudeli käituse eest.

## Raportist ühise parandamiseni

1. Panustaja esitab lähteväljavõtte, selle tõlke ja konteksti.
2. Keeletoimetaja kontrollib tähendust, loomulikkust ja seda, kas ettepanek sõltub konkreetsest piirkonnast või kursusest.
3. Haldaja otsustab, kas parandus kuulub lähtekursuse, ühise keeleinstruktsiooni, terminoloogia konfiguratsiooni või tõlkekoodi hulka.
4. Ühise reegli puhul võrdleb haldaja väljundeid enne ja pärast muudatust raporteeritud näitel ja mitteseotud näidetes. Panustajad saavad neid väljundeid üle vaadata ilma tööriista ise käivitamata.
5. Tulemuseks olev PR lingib raporti ja annab tunnustuse inimestele, kes esitasid näiteid ja tegid ülevaate. Rakendamine või uuesti genereerimine tarbivates repositooriumites on eraldi samm.

Raport ei muuda automaatselt prompt'e ega genereeri kursuse tõlkeid uuesti. Kursusele spetsiifilised parandused peaksid jääma kursuse repositooriumiga seotud. Ära eelda, et käsitsi tehtud redaktsioon säilib hilisema ümbertõlkimise korral; kinnita selle töövoo käitumine.

## Olemasolev näide: jaapani Markdowni lingid

The [jaapani juhisfail](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) ütleb mudelile, et tõlgiks lingiteksti, hoides alles Markdowni süntaksit ja lingisihtkohta. Näiteks lingi, mis on kirjutatud kujul `[text](URL)`, ei tohi muutuda `「text」（URL）`.

See on keskendunud näide keele reeglist, mida toetab õige ja vale väljundi illustratsioon. See ei tõesta, et ainult prompti juhised tagavad korrektse Markdowni.

The [Markdown prompti koostaja](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) laadib `templates/language/<language_code>.md` kasutades väiketähtedeks muudetud, kärbitud keelekoodi. Kui faili pole, kasutatakse üldjuhiseid. See kirjeldab Markdown-prompti teed; ära eelda, et iga pilt või muu tõlkerada kasutab samu juhiseid.

The [promptitestid](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) kontrollivad, et jaapani juhised on kaasatud. See kinnitab prompti kokkupanekut, mitte tõlke kvaliteeti.

## Mida peaks keele reegel sisaldama?

Esitage kitsas, korduv parandus koos lähte- näitega, eeldatava käitumise ja vastunäitega, mille puhul reegel ei tohiks kehtida. Säilitage tähendus, kohatäitjad, kood, URL-id ja dokumendi struktuur. Vältige ühe inimese stiilieelistuse või ühe kursuse terminoloogia muutmist universaalseks reegliks.

The current [sõnastiku rakendus](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) kaitseb termineid tõlkimise eest. See ei ole lähte- ja sihtkeele terminoloogia sõnastik. Arutage uut terminoloogia käitumist enne, kui lubate seda panustajatele.

## Kogukonna näide: jaapani tootenime raport

In [raportis #527](https://github.com/Azure/co-op-translator/issues/527), @hyoshioka0128 tuvastas jaapani tõlke, mis muutis tootenime `Co-op Translator` `Co-op 翻訳`-iks. Raportis oli lisatud link mõjutatud dokumendile ja ekraanipilt, mis tegi probleemi hõlpsasti leitavaks.

Panustaja lisas ka lingi [seotud kursuse PR](https://github.com/microsoft/AZD-for-beginners/pull/109). Teemas toimunud arutelus tunnustas haldaja raporti ja pakkus välja uurida, miks nimi muutus, sh terminoloogia kaitse, sõnastiku käitumine ja tõlkerada.

See näitab, kuidas väike raport võib toetada uurimist, mis läheb kaugemale üksikust sõnastuse parandusest. See ei ole kinnitatud enne/peale tulemus ega tõend, et ülaltoodud jaapani Markdowni lingijuhised lahendasid seda tootenime probleemi.

Saate sama moodi panustada: jagage algset teksti, praegust tõlget, soovitatud parandust ja miks see on oluline. Lisage vajadusel dokumendi link või ekraanipilt. Te ei pea diagnoosima põhjust ega kirjutama prompti enne raporti esitamist.

## Valideerimine enne reegli vastuvõtmist

Kasutage baas- ja kandidaatrunnides samu lähtevalimeid, tõlkija revisjoni, pakkujat/mudelit ja genereerimisseadeid, muutes ainult pakutud juhist. Salvestage tegelik prompti muutus ja väljundid; korrake näiteid, kui vaja, et eristada järjekindlat mõju väljundi varieeruvusest. Lisage raporteeritud rike, vastanduvad kontekstid ja näited, mis juba tõlgitakse õigesti.

| Näide | Lähte/kontekst | Algväljund | Kandidaadiväljund | Ülevaataja hinnang |
| --- | --- | --- | --- | --- |
| Raporteeritud rike | Koguda | Pole käivitatud | Pole käivitatud | Ootel |
| Vastunäide | Koguda | Pole käivitatud | Pole käivitatud | Ootel |
| Mõjutamata näide | Koguda | Pole käivitatud | Pole käivitatud | Ootel |

Kontrollige struktuurseid invariande eraldi keelelistest hinnangutest. Edukas prompti laadimise test ei ole kvaliteedi hindamine ja üks täpne oodatav lause ei ole ainus kehtiv tõlge. Kui kontekst, mudeli jooksud või keeleülevaade puuduvad, jätke ettepanek ootele, selle asemel et väita, et probleem on lahendatud.