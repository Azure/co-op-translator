<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:35:33+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "fi"
}
-->
# Asenna Co-op translator -paketti

**Co-op Translator** on komentorivityökalu (CLI), joka auttaa sinua kääntämään kaikki projektisi markdown-tiedostot ja kuvat useille kielille. Tämä opas ohjaa sinut läpi kääntäjän konfiguroinnin ja sen käyttämisen eri tilanteissa.

### Luo virtuaaliympäristö

Voit luoda virtuaaliympäristön käyttämällä joko `pip` tai `Poetry`. Kirjoita jompikumpi seuraavista komennoista terminaaliisi.

#### Pipin käyttäminen

```bash
python -m venv .venv
```

#### Poetryn käyttäminen

```bash
poetry init
```

### Aktivoi virtuaaliympäristö

Virtuaaliympäristön luomisen jälkeen sinun täytyy aktivoida se. Vaiheet riippuvat käyttöjärjestelmästäsi. Kirjoita seuraava komento terminaaliisi.

#### Sekä pipille että Poetrylle

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetryn käyttäminen

1. Jos loit ympäristön Poetrylla, kirjoita seuraava komento terminaaliisi aktivoidaksesi sen.

    ```bash
    poetry shell
    ```

### Paketin ja vaadittavien pakettien asentaminen

Kun virtuaaliympäristö on luotu ja aktivoitu, seuraava vaihe on asentaa tarvittavat riippuvuudet.

### Pikainen asennus

Asenna Co-Op Translator pipin kautta

```
pip install co-op-translator
```  
Tai  

Asenna Poetrylla  
```
poetry add co-op-translator
```

#### Pipin käyttäminen (requirements.txt-tiedostosta), jos kloonaat tämän repositorion

![NOTE] Älä tee tätä, jos asennat co-op translatorin pikaisen asennuksen kautta.

1. Jos käytät pipiä, kirjoita seuraava komento terminaaliisi. Se asentaa automaattisesti `requirements.txt`-tiedostossa määritellyt pakolliset paketit:

    ```bash
    pip install -r requirements.txt
    ```

#### Poetryn käyttäminen (pyproject.toml-tiedostosta)

1. Jos käytät Poetrya, kirjoita seuraava komento terminaaliisi. Se asentaa automaattisesti `pyproject.toml`-tiedostossa määritellyt pakolliset paketit:

    ```bash
    poetry install
    ```

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty tekoälypohjaisella käännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on katsottava auktoriteettiseksi lähteeksi. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai virhetulkinnoista.