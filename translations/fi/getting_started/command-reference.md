<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:26:54+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "fi"
}
-->
# Komentoviite

**Co-op Translator** CLI tarjoaa useita vaihtoehtoja käännösprosessin räätälöintiin:

Komento                                       | Kuvaus
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Kääntää projektisi valituille kielille. Esimerkki: translate -l "es fr de" kääntää espanjaksi, ranskaksi ja saksaksi. Käytä translate -l "all" kääntääksesi kaikille tuetuille kielille.
translate -l "language_codes" -u              | Päivittää käännökset poistamalla olemassa olevat ja luomalla ne uudelleen. Varoitus: Tämä poistaa kaikki nykyiset käännökset valituille kielille.
translate -l "language_codes" -img            | Kääntää vain kuvatiedostot.
translate -l "language_codes" -md             | Kääntää vain Markdown-tiedostot.
translate -l "language_codes" -nb             | Kääntää vain Jupyter notebook -tiedostot (.ipynb).
translate -l "language_codes" --fix           | Kääntää uudelleen tiedostot, joiden luottamuspisteet ovat matalat aiempien arviointitulosten perusteella.
translate -l "language_codes" -d              | Ottaa käyttöön debug-tilan yksityiskohtaista lokitusta varten.
translate -l "language_codes" --save-logs, -s | Tallentaa DEBUG-tason lokitiedostot hakemistoon <root_dir>/logs/ (konsoli pysyy -d:n ohjaamana)
translate -l "language_codes" -r "root_dir"   | Määrittää projektin juurihakemiston
translate -l "language_codes" -f              | Käyttää nopeaa tilaa kuvakäännöksissä (jopa 3x nopeampi piirto, mutta hieman heikompi laatu ja kohdistus).
translate -l "language_codes" -y              | Vahvistaa kaikki kehotteet automaattisesti (hyödyllinen CI/CD-putkissa)
translate -l "language_codes" --help          | Näyttää CLI:n ohjeet ja käytettävissä olevat komennot
evaluate -l "language_code"                  | Arvioi käännösten laatua tietylle kielelle ja antaa luottamuspisteet
evaluate -l "language_code" -c 0.8           | Arvioi käännökset mukautetulla luottamuskynnyksellä
evaluate -l "language_code" -f               | Nopea arviointitila (vain sääntöihin perustuva, ei LLM:ää)
evaluate -l "language_code" -D               | Syvä arviointitila (vain LLM-pohjainen, perusteellisempi mutta hitaampi)
evaluate -l "language_code" --save-logs, -s  | Tallentaa DEBUG-tason lokitiedostot hakemistoon <root_dir>/logs/
migrate-links -l "language_codes"             | Käsittelee uudelleen käännetyt Markdown-tiedostot ja päivittää linkit notebookeihin (.ipynb). Käyttää mieluiten käännettyjä notebookeja, muuten voi käyttää alkuperäisiä.
migrate-links -l "language_codes" -r          | Määritä projektin juurihakemisto (oletus: nykyinen hakemisto).
migrate-links -l "language_codes" --dry-run   | Näyttää, mitkä tiedostot muuttuisivat ilman muutosten tallentamista.
migrate-links -l "language_codes" --no-fallback-to-original | Älä päivitä linkkejä alkuperäisiin notebookeihin, jos käännettyjä ei ole (päivitä vain, kun käännetty löytyy).
migrate-links -l "language_codes" -d          | Ota debug-tila käyttöön yksityiskohtaista lokitusta varten.
migrate-links -l "language_codes" --save-logs, -s | Tallentaa DEBUG-tason lokitiedostot hakemistoon <root_dir>/logs/
migrate-links -l "all" -y                      | Käsittele kaikki kielet ja vahvista varoitus automaattisesti.

## Käyttöesimerkkejä

  1. Oletuskäyttäytyminen (lisää uusia käännöksiä poistamatta olemassa olevia):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Lisää vain uusia koreankielisiä kuvakäännöksiä (olemassa olevia ei poisteta):    translate -l "ko" -img

  3. Päivitä kaikki koreankieliset käännökset (Varoitus: Poistaa kaikki olemassa olevat koreankieliset käännökset ennen uudelleenkääntämistä):    translate -l "ko" -u

  4. Päivitä vain koreankieliset kuvat (Varoitus: Poistaa kaikki olemassa olevat koreankieliset kuvat ennen uudelleenkääntämistä):    translate -l "ko" -img -u

  5. Lisää uusia markdown-käännöksiä koreaksi vaikuttamatta muihin käännöksiin:    translate -l "ko" -md

  6. Korjaa matalan luottamuksen käännökset aiempien arviointitulosten perusteella: translate -l "ko" --fix

  7. Korjaa matalan luottamuksen käännökset vain tietyille tiedostoille (markdown): translate -l "ko" --fix -md

  8. Korjaa matalan luottamuksen käännökset vain tietyille tiedostoille (kuvat): translate -l "ko" --fix -img

  9. Käytä nopeaa tilaa kuvakäännöksissä:    translate -l "ko" -img -f

  10. Korjaa matalan luottamuksen käännökset mukautetulla kynnyksellä: translate -l "ko" --fix -c 0.8

  11. Debug-tilan esimerkki: - translate -l "ko" -d: Ota debug-lokitus käyttöön.
  12. Tallenna lokitiedostot: translate -l "ko" -s
  13. Konsolin DEBUG ja tiedoston DEBUG: translate -l "ko" -d -s

  14. Siirrä notebook-linkit koreankielisille käännöksille (päivitä linkit käännettyihin notebookeihin, kun saatavilla):    migrate-links -l "ko"

  15. Siirrä linkit dry-run-tilassa (ei tiedostojen kirjoitusta):    migrate-links -l "ko" --dry-run

  16. Päivitä linkit vain, kun käännetty notebook on olemassa (älä käytä alkuperäistä varana):    migrate-links -l "ko" --no-fallback-to-original

  17. Käsittele kaikki kielet vahvistuskehotteella:    migrate-links -l "all"

  18. Käsittele kaikki kielet ja vahvista automaattisesti:    migrate-links -l "all" -y
  19. Tallenna lokitiedostot migrate-linksille:    migrate-links -l "ko ja" -s

### Arviointiesimerkkejä

> [!WARNING]  
> **Beta-ominaisuus**: Arviointitoiminnallisuus on tällä hetkellä beta-vaiheessa. Tämä ominaisuus julkaistiin käännettyjen dokumenttien arviointiin, ja arviointimenetelmät sekä toteutus ovat vielä kehitteillä ja voivat muuttua.

  1. Arvioi koreankieliset käännökset: evaluate -l "ko"

  2. Arvioi mukautetulla luottamuskynnyksellä: evaluate -l "ko" -c 0.8

  3. Nopea arviointi (vain sääntöihin perustuva): evaluate -l "ko" -f

  4. Syvä arviointi (vain LLM-pohjainen): evaluate -l "ko" -D

---

**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisissä tapauksissa suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa tämän käännöksen käytöstä mahdollisesti aiheutuvista väärinkäsityksistä tai tulkintavirheistä.