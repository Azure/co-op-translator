<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:29:39+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "fi"
}
-->
# Komenttiviite
**Co-op Translator** CLI tarjoaa useita vaihtoehtoja käännösprosessin mukauttamiseen:

Komento                                      | Kuvaus
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Kääntää projektisi määriteltyihin kieliin. Esimerkki: translate -l "es fr de" kääntää espanjaksi, ranskaksi ja saksaksi. Käytä translate -l "all" kääntääksesi kaikkiin tuettuihin kieliin.
translate -l "language_codes" -u              | Päivittää käännökset poistamalla olemassa olevat ja luomalla ne uudelleen. Varoitus: Tämä poistaa kaikki nykyiset käännökset määritellyille kielille.
translate -l "language_codes" -img            | Kääntää vain kuv tiedostot.
translate -l "language_codes" -md             | Kääntää vain Markdown-tiedostot.
translate -l "language_codes" -chk            | Tarkistaa käännetyt tiedostot virheiden varalta ja yrittää käännöstä uudelleen tarvittaessa.
translate -l "language_codes" -d              | Ota debug-tila käyttöön yksityiskohtaista lokitusta varten.
translate -l "language_codes" -r "root_dir"   | Määrittää projektin juurihakemiston
translate -l "language_codes" -f              | Käyttää nopeaa tilaa kuvien käännöksessä (jopa 3 kertaa nopeampi piirtäminen pienen laadun ja kohdistuksen heikkenemisen hinnalla).
translate -l "language_codes" -y              | Vahvistaa automaattisesti kaikki kehotteet (kätevää CI/CD-putkistoissa)
translate -l "language_codes" --help          | CLI:n ohje, joka näyttää käytettävissä olevat komennot

### Käyttöesimerkkejä:

  1. Oletuskäyttäytyminen (lisää uusia käännöksiä poistamatta olemassa olevia):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Lisää vain uudet koreankieliset kuvakäännökset (ei poista olemassa olevia käännöksiä):    translate -l "ko" -img

  3. Päivitä kaikki koreankieliset käännökset (Varoitus: Tämä poistaa kaikki olemassa olevat koreankieliset käännökset ennen uudelleenkääntämistä):    translate -l "ko" -u

  4. Päivitä vain koreankieliset kuvat (Varoitus: Tämä poistaa kaikki olemassa olevat koreankieliset kuvat ennen uudelleenkääntämistä):    translate -l "ko" -img -u

  5. Lisää uudet markdown-käännökset koreaksi vaikuttamatta muihin käännöksiin:    translate -l "ko" -md

  6. Tarkista käännetyt tiedostot virheiden varalta ja yritä käännöksiä uudelleen tarvittaessa: translate -l "ko" -chk

  7. Tarkista käännetyt tiedostot virheiden varalta ja yritä käännöksiä uudelleen (vain markdown): translate -l "ko" -chk -md

  8. Tarkista käännetyt tiedostot virheiden varalta ja yritä käännöksiä uudelleen (vain kuvat): translate -l "ko" -chk -img

  9. Käytä nopeaa tilaa kuvien käännöksessä:    translate -l "ko" -img -f

  10. Debug-tila esimerkki: - translate -l "ko" -d: Ota debug-lokit käyttöön.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja omalla kielellään on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai virhetulkinnoista.