<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:27:41+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "fi"
}
-->
# Asenna Co-op Translator -paketti

**Co-op Translator** on komentorivikäyttöliittymä (CLI) -työkalu, jonka avulla voit kääntää kaikki projektisi markdown-tiedostot ja kuvat useille kielille. Tämä opas neuvoo, miten kääntäjä konfiguroidaan ja käytetään eri tilanteissa.

### Luo virtuaaliympäristö

Voit luoda virtuaaliympäristön joko `pip`- tai `Poetry`-työkalulla. Kirjoita jokin seuraavista komennoista terminaaliin.

#### Pipin käyttö

```bash
python -m venv .venv
```

#### Poetryn käyttö

```bash
poetry init
```

### Aktivoi virtuaaliympäristö

Kun virtuaaliympäristö on luotu, se täytyy aktivoida. Vaiheet riippuvat käyttöjärjestelmästäsi. Kirjoita seuraava komento terminaaliin.

#### Pipille ja Poetrylle

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetryn käyttö

1. Jos loit ympäristön Poetrylla, aktivoi se kirjoittamalla seuraava komento terminaaliin.

    ```bash
    poetry shell
    ```

### Paketin ja tarvittavien pakettien asennus

Kun virtuaaliympäristö on luotu ja aktivoitu, seuraava vaihe on tarvittavien riippuvuuksien asentaminen.

### Nopea asennus

Asenna Co-Op Translator pipin kautta

```
pip install co-op-translator
```
Tai 

Asenna Poetryn kautta
```
poetry add co-op-translator
```

#### Pipin käyttö (requirements.txt-tiedostosta), jos kloonaat tämän repopaketin

> [!NOTE]
> Älä tee tätä, jos asennat co-op translatorin nopean asennuksen kautta.

1. Jos käytät pipiä, kirjoita seuraava komento terminaaliin. Se asentaa automaattisesti kaikki `requirements.txt`-tiedostossa määritetyt paketit:

    ```bash
    pip install -r requirements.txt
    ```

#### Poetryn käyttö (pyproject.toml-tiedostosta)

1. Jos käytät Poetrya, kirjoita seuraava komento terminaaliin. Se asentaa automaattisesti kaikki `pyproject.toml`-tiedostossa määritetyt paketit:

    ```bash
    poetry install
    ```

---

**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisissä tapauksissa suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai tulkintavirheistä.