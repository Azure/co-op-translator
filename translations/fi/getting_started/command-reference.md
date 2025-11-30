<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T11:33:53+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "fi"
}
-->
# Komenttiviite

**Co-op Translator** CLI tarjoaa useita vaihtoehtoja käännösprosessin mukauttamiseen:

Komentorivi                                  | Kuvaus
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Kääntää projektisi määriteltyihin kieliin. Esimerkki: translate -l "es fr de" kääntää espanjaksi, ranskaksi ja saksaksi. Käytä translate -l "all" kääntääksesi kaikkiin tuettuihin kieliin.
translate -l "language_codes" -u              | Päivittää käännökset poistamalla olemassa olevat ja luomalla ne uudelleen. Varoitus: Tämä poistaa kaikki nykyiset käännökset määritellyille kielille.
translate -l "language_codes" -img            | Kääntää vain kuvatiedostot.
translate -l "language_codes" -md             | Kääntää vain Markdown-tiedostot.
translate -l "language_codes" -nb             | Kääntää vain Jupyter-muistikirjatiedostot (.ipynb).
translate -l "language_codes" --fix           | Kääntää uudelleen tiedostot, joilla on matala luottamuspiste aiempien arviointitulosten perusteella.
translate -l "language_codes" -d              | Ottaa käyttöön debug-tilan yksityiskohtaista lokitusta varten.
translate -l "language_codes" --save-logs, -s | Tallentaa DEBUG-tason lokitiedostot hakemistoon <root_dir>/logs/ (konsolin lokitus pysyy -d-vaihtoehdon ohjaamana)
translate -l "language_codes" -r "root_dir"   | Määrittää projektin juurihakemiston
translate -l "language_codes" -f              | Käyttää nopeaa tilaa kuvakäännöksissä (jopa 3 kertaa nopeampi piirtäminen hieman laadun ja kohdistuksen kustannuksella).
translate -l "language_codes" -y              | Vahvistaa automaattisesti kaikki kehotteet (kätevää CI/CD-putkistoissa)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Ota käyttöön tai poista käytöstä konekäännöksen vastuuvapauslauseke käännetyissä markdown- ja muistikirjatiedostoissa (oletus: käytössä).
translate -l "language_codes" --help          | Näyttää CLI:n käytettävissä olevat komennot ja ohjeet
evaluate -l "language_code"                  | Arvioi tietyn kielen käännösten laatua ja antaa luottamuspisteet
evaluate -l "language_code" -c 0.8           | Arvioi käännökset mukautetulla luottamuskynnyksellä
evaluate -l "language_code" -f               | Nopea arviointitila (vain sääntöpohjainen, ei LLM)
evaluate -l "language_code" -D               | Syväarviointitila (vain LLM-pohjainen, perusteellisempi mutta hitaampi)
evaluate -l "language_code" --save-logs, -s  | Tallentaa DEBUG-tason lokitiedostot hakemistoon <root_dir>/logs/
migrate-links -l "language_codes"             | Käsittelee uudelleen käännetyt Markdown-tiedostot päivittääkseen linkit muistikirjoihin (.ipynb). Käyttää mieluummin käännettyjä muistikirjoja, jos saatavilla; muuten voi käyttää alkuperäisiä.
migrate-links -l "language_codes" -r          | Määrittää projektin juurihakemiston (oletus: nykyinen hakemisto).
migrate-links -l "language_codes" --dry-run   | Näyttää, mitkä tiedostot muuttuisivat ilman, että muutoksia kirjoitetaan.
migrate-links -l "language_codes" --no-fallback-to-original | Älä korvaa linkkejä alkuperäisiin muistikirjoihin, jos käännettyjä versioita ei ole (päivitä vain, kun käännetty versio on olemassa).
migrate-links -l "language_codes" -d          | Ota käyttöön debug-tila yksityiskohtaista lokitusta varten.
migrate-links -l "language_codes" --save-logs, -s | Tallenna DEBUG-tason lokitiedostot hakemistoon <root_dir>/logs/
migrate-links -l "all" -y                      | Käsittele kaikki kielet ja vahvista varoituskehotteet automaattisesti.

## Käyttöesimerkit

  1. Oletuskäyttäytyminen (lisää uusia käännöksiä poistamatta olemassa olevia):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Lisää vain uudet koreankieliset kuvakäännökset (ei poista olemassa olevia käännöksiä):    translate -l "ko" -img

  3. Päivitä kaikki koreankieliset käännökset (Varoitus: Tämä poistaa kaikki olemassa olevat koreankieliset käännökset ennen uudelleenkääntämistä):    translate -l "ko" -u

  4. Päivitä vain koreankieliset kuvat (Varoitus: Tämä poistaa kaikki olemassa olevat koreankieliset kuvat ennen uudelleenkääntämistä):    translate -l "ko" -img -u

  5. Lisää uudet markdown-käännökset koreaksi vaikuttamatta muihin käännöksiin:    translate -l "ko" -md

  6. Korjaa matalan luottamuksen käännökset aiempien arviointitulosten perusteella: translate -l "ko" --fix

  7. Korjaa matalan luottamuksen käännökset vain tietyille tiedostoille (markdown): translate -l "ko" --fix -md

  8. Korjaa matalan luottamuksen käännökset vain tietyille tiedostoille (kuvat): translate -l "ko" --fix -img

  9. Käytä nopeaa tilaa kuvakäännöksissä:    translate -l "ko" -img -f

  10. Korjaa matalan luottamuksen käännökset mukautetulla kynnyksellä: translate -l "ko" --fix -c 0.8

  11. Debug-tila esimerkki: - translate -l "ko" -d: Ota debug-lokitus käyttöön.
  12. Tallenna lokitiedostot: translate -l "ko" -s
  13. Konsolin DEBUG ja tiedoston DEBUG: translate -l "ko" -d -s
  14. Käännä ilman konekäännöksen vastuuvapauslausekkeita: translate -l "ko" --no-disclaimer

  15. Siirrä muistikirjalinkit koreankielisille käännöksille (päivitä linkit käännettyihin muistikirjoihin, jos saatavilla):    migrate-links -l "ko"

  15. Siirrä linkit kuivaharjoituksella (ei tiedostojen kirjoitusta):    migrate-links -l "ko" --dry-run

  16. Päivitä linkit vain, kun käännetyt muistikirjat ovat olemassa (älä palaa alkuperäisiin):    migrate-links -l "ko" --no-fallback-to-original

  17. Käsittele kaikki kielet vahvistuskehotteella:    migrate-links -l "all"

  18. Käsittele kaikki kielet ja vahvista automaattisesti:    migrate-links -l "all" -y
  19. Tallenna lokitiedostot migrate-links-komennolle:    migrate-links -l "ko ja" -s

### Arviointiesimerkit

> [!WARNING]  
> **Beta-ominaisuus**: Arviointitoiminto on tällä hetkellä beta-vaiheessa. Tämä ominaisuus julkaistiin käännettyjen dokumenttien arviointiin, ja arviointimenetelmät sekä yksityiskohtainen toteutus ovat vielä kehitysvaiheessa ja voivat muuttua.

  1. Arvioi koreankieliset käännökset: evaluate -l "ko"

  2. Arvioi mukautetulla luottamuskynnyksellä: evaluate -l "ko" -c 0.8

  3. Nopea arviointi (vain sääntöpohjainen): evaluate -l "ko" -f

  4. Syväarviointi (vain LLM-pohjainen): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->