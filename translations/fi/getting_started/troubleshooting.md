<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:28:07+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "fi"
}
-->
# Microsoft Co-op Translatorin Vianmääritysohje


## Yleiskatsaus
Microsoft Co-Op Translator on tehokas työkalu Markdown-dokumenttien sujuvaan kääntämiseen. Tämä ohje auttaa sinua ratkaisemaan yleisimpiä työkalun käytössä esiintyviä ongelmia.

## Yleiset ongelmat ja ratkaisut

### 1. Markdown-tägiongelma
**Ongelma:** Käännettyyn Markdown-dokumenttiin ilmestyy `markdown`-tägi tiedoston alkuun, mikä aiheuttaa renderöintiongelmia.

**Ratkaisu:** Poista tiedoston alusta `markdown`-tägi. Tämä mahdollistaa Markdown-tiedoston oikean renderöinnin.

**Vaiheet:**
1. Avaa käännetty Markdown (`.md`) -tiedosto.
2. Etsi dokumentin alussa oleva `markdown`-tägi.
3. Poista `markdown`-tägi.
4. Tallenna tiedosto.
5. Avaa tiedosto uudelleen varmistaaksesi, että se renderöityy oikein.

### 2. Upotettujen kuvien URL-ongelma
**Ongelma:** Upotettujen kuvien URL-osoitteet eivät vastaa kieliversiota, mikä johtaa virheellisiin tai puuttuviin kuviin.

**Ratkaisu:** Tarkista upotettujen kuvien URL-osoitteet ja varmista, että ne vastaavat kieliversiota. Kaikki kuvat sijaitsevat `translated_images`-kansiossa, ja jokaisessa kuvatiedoston nimessä on kieliversiotunniste.

**Vaiheet:**
1. Avaa käännetty Markdown-dokumentti.
2. Tunnista upotetut kuvat ja niiden URL-osoitteet.
3. Varmista, että kuvatiedoston nimen kieliversiotunniste vastaa dokumentin kieltä.
4. Päivitä URL-osoitteet tarvittaessa.
5. Tallenna muutokset ja avaa dokumentti uudelleen varmistaaksesi kuvien oikean renderöinnin.

### 3. Käännöksen tarkkuus
**Ongelma:** Käännetty sisältö ei ole tarkkaa tai vaatii lisämuokkauksia.

**Ratkaisu:** Tarkista käännetty dokumentti ja tee tarvittavat muokkaukset käännöksen tarkkuuden ja luettavuuden parantamiseksi.

**Vaiheet:**
1. Avaa käännetty dokumentti.
2. Tarkista sisältö huolellisesti.
3. Tee tarvittavat muokkaukset käännöksen parantamiseksi.
4. Tallenna muutokset.

### 4. Tiedoston muotoiluongelmat
**Ongelma:** Käännetyn dokumentin muotoilu on virheellinen. Tämä voi ilmetä esimerkiksi taulukoissa, joihin liittyvät ongelmat ratkaistaan lisätyllä ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ```:lla.

**Vaiheet:**
1. Avaa käännetty dokumentti.
2. Vertaa sitä alkuperäiseen dokumenttiin muotoiluvirheiden löytämiseksi.
3. Korjaa muotoilu vastaamaan alkuperäistä dokumenttia.
4. Tallenna muutokset.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.