# Kielen parannuksiin osallistuminen

Kielen osaamisesi voi auttaa parantamaan Co-op Translatoria. Aloita esimerkillä, ehdotetulla korjauksella ja selityksellä käyttäen [käännöspalautelomake](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Sinun ei tarvitse kirjoittaa koodia tai maksaa mallin ajosta.

## Raportista yhteiseen parannukseen

1. Avustaja toimittaa lähdetekstin katkelman, sen käännöksen ja kontekstin.
2. Kielentarkastaja arvioi merkityksen, luonnollisuuden ja sen, riippuuko ehdotus tietystä alueesta (locale) tai kurssista.
3. Ylläpitäjä päättää, kuuluuko korjaus lähdekurssiin, jaettuun kieliohjeeseen, terminologian määritykseen tai käännöskoodiin.
4. Jaetun säännön kohdalla ylläpitäjä vertaa tuotoksia ennen ja jälkeen muutoksen sekä raportoidulla esimerkillä että siihen kuulumattomilla esimerkeillä. Avustajat voivat tarkistaa nämä tuotokset ilman, että heidän tarvitsee ajaa työkalua itse.
5. Tuloksena oleva PR linkittää raportin ja mainitsee henkilöt, jotka toimittivat esimerkit ja tarkistuksen. Julkaisu tai uudengenerointi käyttävissä repositorioissa on erillinen vaihe.

Raportti ei automaattisesti muuta promptteja tai uusi kurssikäännöksiä. Kurssikohtaiset korjaukset tulisi pitää kytkettyinä kurssin repositorioon. Älä oleta, että manuaalinen muutos säilyy myöhemmässä uudelleenkäännössä; varmista työprosessin käyttäytyminen.

## Olemassa oleva esimerkki: Japanilaiset Markdown-linkit

[Japanilainen ohjetiedosto](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) kertoo mallille, että sen tulee kääntää linkin tekstiä säilyttäen Markdown-syntaksin ja linkin kohteen. Esimerkiksi linkki, joka on kirjoitettu muodossa `[text](URL)`, ei saa muuttua muotoon `「text」（URL）`.

Tämä on tarkennettu esimerkki kielisäännöstä, jota tukee oikean ja väärän tulosteen kuvaus. Se ei todista, että pelkät prompt-ohjeet takaavat oikean Markdownin.

[Markdown-promptin rakentaja](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) lataa `templates/language/<language_code>.md` käyttäen pienaakkosiksi muunnettua ja ympäröivistä välilyönneistä siivottua kielikoodia. Jos tiedostoa ei ole, se käyttää yleisiä ohjeita. Tämä kuvaa Markdown-kehotepolkua; älä oleta, että jokainen kuva tai muu käännöspolku käyttää samoja ohjeita.

[Prompt-testit](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) tarkistavat, että japanilaiset ohjeet sisältyvät. Ne varmistavat kehotteen kokoamisen, eivät käännöksen laatua.

## Mitä tulisi sisällyttää kielisääntöön?

Ehdota kapea-alaista, toistettavissa olevaa korjausta lähde-esimerkin, odotetun käyttäytymisen ja vastiesimerkin kera, jossa sääntöä ei saa soveltaa. Säilytä merkitys, paikkamerkit, koodi, URLit ja asiakirjarakenne. Vältä yhden henkilön tyylivalinnan tai yhden kurssin terminologian muuttamista yleiseksi säännöksi.

Nykyinen [glossaarin toteutus](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) suojaa termejä kääntämiseltä. Se ei ole lähde‑kohde-terminologiasanasto. Keskustele uudesta terminologiakäytännöstä ennen kuin lupaat sitä avustajille.

## Yhteisön esimerkki: raportti japanilaisesta tuotteen nimestä

Raportissa [raportti #527](https://github.com/Azure/co-op-translator/issues/527) @hyoshioka0128 tunnisti japanilaisen käännöksen, joka muutti tuotteen nimen `Co-op Translator` muotoon `Co-op 翻訳`. Raportti sisälsi linkin vaikuttavaan asiakirjaan ja kuvakaappauksen, mikä teki ongelman helposti paikannettavaksi.

Avustaja liitti myös [aiheeseen liittyvän kurssin PR:n](https://github.com/microsoft/AZD-for-beginners/pull/109). Keskustelussa ylläpitäjä tunnisti raportin ja ehdotti tutkimusta, miksi nimi muuttui, mukaan lukien terminologian suojaus, glossaarin käyttäytyminen ja käännöspolku.

Tämä osoittaa, kuinka pieni raportti voi tukea tutkimusta yksittäisen sanamuutoksen korjauksen ulkopuolella. Se ei ole todistettu ennen/jälkeen-tulos eikä todiste siitä, että yllä olevat japanilaiset Markdown-linkkiohjeet korjasivat tämän tuotteen nimen ongelman.

Voit osallistua samalla tavalla: jaa alkuperäinen teksti, nykyinen käännös, ehdotettu korjaus ja miksi se on tärkeää. Lisää asiakirjalinkki tai kuvakaappaus, kun se on hyödyllistä. Sinun ei tarvitse diagnosoida syytä tai kirjoittaa prompttia ennen raportointia.

## Vahvistus ennen säännön käyttöönottoa

Käytä samoja lähteitä, kääntäjän tarkistuksia, tarjoajaa/mallia ja generointiasetuksia perus- ja ehdokaskierroksilla, muuttaen vain ehdotettua ohjetta. Tallenna varsinainen prompt-muutos ja tuotokset; toista esimerkkejä tarvittaessa erottaaksesi yhdenmukaisen vaikutuksen tuotosten vaihtelusta. Sisällytä raportoitua epäonnistumista, vastakkaisia konteksteja ja esimerkkejä, jotka jo kääntyvät oikein.

| Näyte | Lähde/konteksti | Perustulos | Ehdokastuotos | Tarkastajan arvio |
| --- | --- | --- | --- | --- |
| Raportoitu epäonnistuminen | Kerättävänä | Ei ajettu | Ei ajettu | Odottaa |
| Vastiesimerkki | Kerättävänä | Ei ajettu | Ei ajettu | Odottaa |
| Vaikuttamaton esimerkki | Kerättävänä | Ei ajettu | Ei ajettu | Odottaa |

Tarkista rakenteelliset invariantit erikseen kielellisistä arvioista. Onnistunut promptin lataustesti ei ole laatuarviointi, eikä yksi tarkka odotettu lause ole ainoa pätevä käännös. Jos konteksti, mallinajot tai kielitarkistus puuttuvat, pidä ehdotus vireillä sen sijaan, että väittäisit ongelman korjatuksi.