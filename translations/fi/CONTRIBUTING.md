<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T11:31:34+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "fi"
}
-->
# Osallistuminen Co-op Translator -projektiin

Tämä projekti ottaa mielellään vastaan panoksia ja ehdotuksia. Useimmat panokset edellyttävät, että hyväksyt
Contributor License Agreementin (CLA), jossa vahvistat, että sinulla on oikeus ja myönnät meille
oikeudet käyttää panostasi. Lisätietoja löytyy osoitteesta https://cla.opensource.microsoft.com.

Kun lähetät pull requestin, CLA-botti tarkistaa automaattisesti, tarvitsetko CLA:n ja merkitsee PR:n asianmukaisesti (esim. tilantarkistus, kommentti). Noudata vain botin antamia ohjeita. Tämä tarvitsee tehdä vain kerran kaikissa CLA:ta käyttävissä repositorioissa.

## Kehitysympäristön asennus

Tämän projektin kehitysympäristön asennukseen suosittelemme Poetrya riippuvuuksien hallintaan. Käytämme `pyproject.toml`-tiedostoa projektin riippuvuuksien hallintaan, joten riippuvuuksien asentamiseen tulee käyttää Poetrya.

### Virtuaaliympäristön luominen

#### Pipin avulla

```bash
python -m venv .venv
```

#### Poetryn avulla

```bash
poetry init
```

### Virtuaaliympäristön aktivointi

#### Sekä pipillä että Poetrylla

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetryn avulla

```bash
poetry shell
```

### Paketin ja vaadittujen pakettien asentaminen

#### Poetrylla (pyproject.toml:n perusteella)

```bash
poetry install
```

### Manuaalinen testaus

Ennen PR:n lähettämistä on tärkeää testata käännöstoiminnallisuus oikealla dokumentaatiolla:

1. Luo testihakemisto juurihakemistoon:
    ```bash
    mkdir test_docs
    ```

2. Kopioi testihakemistoon joitain käännettäviä markdown-dokumentteja ja kuvia. Esimerkiksi:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Asenna paketti paikallisesti:
    ```bash
    pip install -e .
    ```

4. Suorita Co-op Translator testidokumenteillasi:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Tarkista käännetyt tiedostot kansioista `test_docs/translations` ja `test_docs/translated_images` varmistaaksesi:
   - Käännöksen laatu
   - Metatietokommenttien oikeellisuus
   - Alkuperäisen markdown-rakenteen säilyminen
   - Linkkien ja kuvien toimivuus

Tämä manuaalinen testaus varmistaa, että muutoksesi toimivat hyvin todellisissa tilanteissa.

### Ympäristömuuttujat

1. Luo juurihakemistoon `.env`-tiedosto kopioimalla valmiiksi annettu `.env.template`-tiedosto.
1. Täytä ympäristömuuttujat ohjeiden mukaisesti.

> [!TIP]
>
> ### Vaihtoehtoisia kehitysympäristöjä
>
> Projektia voi ajaa paikallisesti, mutta vaihtoehtoisesti voit käyttää GitHub Codespacesia tai VS Code Dev Containers -ympäristöä.
>
> #### GitHub Codespaces
>
> Voit ajaa näitä esimerkkejä virtuaalisesti GitHub Codespacesin avulla ilman lisäasetuksia.
>
> Painike avaa selaimessa web-pohjaisen VS Code -instanssin:
>
> 1. Avaa malli (voi kestää muutaman minuutin):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Paikallinen ajo VS Code Dev Containersilla
>
> ⚠️ Tämä vaihtoehto toimii vain, jos Docker Desktopilla on varattu vähintään 16 GB RAM-muistia. Jos muistia on vähemmän, voit kokeilla [GitHub Codespaces -vaihtoehtoa](../..) tai [asentaa paikallisesti](../..).
>
> Vaihtoehtona on VS Code Dev Containers, joka avaa projektin paikallisessa VS Codessa käyttäen [Dev Containers -laajennusta](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Käynnistä Docker Desktop (asennus tarvittaessa)
> 2. Avaa projekti:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Koodityyli

Käytämme [Black](https://github.com/psf/black) -työkalua Python-koodin muotoiluun, jotta koodityyli pysyy yhtenäisenä projektissa. Black on tinkimätön koodinmuotoilija, joka muotoilee Python-koodin automaattisesti Blackin tyylin mukaiseksi.

#### Konfiguraatio

Blackin asetukset on määritelty `pyproject.toml`-tiedostossamme:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Blackin asentaminen

Blackin voi asentaa joko Poetrylla (suositus) tai pipillä:

##### Poetrylla

Black asennetaan automaattisesti kehitysympäristön asennuksen yhteydessä:
```bash
poetry install
```

##### Pipillä

Jos käytät pipiä, voit asentaa Blackin suoraan:
```bash
pip install black
```

#### Blackin käyttö

##### Poetrylla

1. Muotoile kaikki projektin Python-tiedostot:
    ```bash
    poetry run black .
    ```

2. Muotoile tietty tiedosto tai hakemisto:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Pipillä

1. Muotoile kaikki projektin Python-tiedostot:
    ```bash
    black .
    ```

2. Muotoile tietty tiedosto tai hakemisto:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Suosittelemme konfiguroimaan editorisi muotoilemaan koodin automaattisesti Blackilla tallennuksen yhteydessä. Useimmat nykyaikaiset editorit tukevat tätä laajennusten tai lisäosien kautta.

## Co-op Translatorin ajaminen

Ajaaksesi Co-op Translatoria Poetryn avulla ympäristössäsi, toimi seuraavasti:

1. Siirry hakemistoon, jossa haluat tehdä käännösten testauksen, tai luo väliaikainen kansio testejä varten.

2. Suorita seuraava komento. Korvaa `-l ko` haluamallasi kielikoodilla. `-d`-valitsin tarkoittaa debug-tilaa.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Varmista, että Poetry-ympäristö on aktivoitu (poetry shell) ennen komennon suorittamista.

## Uuden kielen lisääminen

Otamme mielellämme vastaan panoksia, jotka lisäävät tukea uusille kielille. Ennen PR:n avaamista suorita alla olevat vaiheet sujuvan tarkastelun varmistamiseksi.

1. Lisää kieli fonttikarttaan
   - Muokkaa tiedostoa `src/co_op_translator/fonts/font_language_mappings.yml`
   - Lisää merkintä, jossa on:
     - `code`: ISO-tyylinen kielikoodi (esim. `vi`)
     - `name`: Käyttäjäystävällinen näyttönimi
     - `font`: Fontti, joka toimitetaan kansiossa `src/co_op_translator/fonts/` ja tukee kyseistä kirjoitusjärjestelmää
     - `rtl`: `true`, jos kieli on oikealta vasemmalle, muuten `false`

2. Lisää tarvittavat fonttitiedostot (tarvittaessa)
   - Jos uusi fontti tarvitaan, varmista lisenssin yhteensopivuus avoimen lähdekoodin jakeluun
   - Lisää fonttitiedosto kansioon `src/co_op_translator/fonts/`

3. Paikallinen tarkistus
   - Suorita käännökset pienelle näytteelle (Markdown, kuvat ja notebookit tarpeen mukaan)
   - Varmista, että tuloste näkyy oikein, mukaan lukien fontit ja mahdollinen RTL-asettelu

4. Päivitä dokumentaatio
   - Varmista, että kieli näkyy tiedostossa `getting_started/supported-languages.md`
   - Tiedostoa `getting_started/README_languages_template.md` ei tarvitse muuttaa, sillä se generoidaan tuetun listan perusteella

5. Avaa PR
   - Kuvaile lisätty kieli ja mahdolliset fontti- tai lisenssiasiat
   - Liitä mukaan kuvakaappauksia renderöidyistä tuloksista, jos mahdollista

Esimerkkimerkintä YAML-muodossa:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Uuden kielen testaus

Voit testata uutta kieltä suorittamalla seuraavan komennon:

```bash
# Luo ja aktivoi virtuaaliympäristö
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Asenna kehityspaketti
pip install -e .
# Suorita käännös
translate -l "new_lang"
```

## Ylläpitäjät

### Commit-viesti ja yhdistämisstrategia

Projektin commit-historian johdonmukaisuuden ja selkeyden varmistamiseksi noudatamme tiettyä commit-viestien muotoa **lopullisessa commit-viestissä** käyttäessämme **Squash and Merge** -strategiaa.

Kun pull request yhdistetään, yksittäiset commitit yhdistetään yhdeksi commitiksi. Lopullisen commit-viestin tulee noudattaa alla olevaa muotoa, jotta historia pysyy siistinä ja yhtenäisenä.

#### Commit-viestin muoto (squash and merge)

Käytämme seuraavaa muotoa commit-viesteissä:

```bash
<type>: <description> (#<PR numero>)
```

- **type**: Määrittää commitin kategorian. Käytämme seuraavia tyyppejä:
  - `Docs`: Dokumentaatiopäivitykset.
  - `Build`: Muutokset build-järjestelmään tai riippuvuuksiin, mukaan lukien konfiguraatiotiedostot, CI-työnkulut tai Dockerfile.
  - `Core`: Muutokset projektin ydintoiminnallisuuteen tai ominaisuuksiin, erityisesti tiedostoissa `src/co_op_translator/core`.

- **description**: Tiivis yhteenveto muutoksesta.
- **PR-numero**: Pull requestin numero, johon commit liittyy.

**Esimerkkejä**:

- `Docs: Päivitä asennusohjeet selkeyden vuoksi (#50)`
- `Core: Paranna kuvan käännöksen käsittelyä (#60)`

> [!NOTE]
> Tällä hetkellä **`Docs`**, **`Core`** ja **`Build`** -etuliitteet lisätään automaattisesti PR-otsikoihin muokattujen lähdekooditiedostojen tunnisteiden perusteella. Kun oikea tunniste on käytössä, sinun ei yleensä tarvitse muokata PR-otsikkoa manuaalisesti. Tarkista vain, että kaikki on oikein ja etuliite on generoitu oikein.

#### Yhdistämisstrategia

Käytämme oletuksena **Squash and Merge** -strategiaa pull requesteille. Tämä varmistaa, että commit-viestit noudattavat muotoamme, vaikka yksittäiset commitit eivät sitä tekisikään.

**Syitä**:

- Selkeä, lineaarinen projektihistoria.
- Johdonmukaisuus commit-viesteissä.
- Vähemmän hälyä pienistä commiteista (esim. "korjaa kirjoitusvirhe").

Yhdistämisen yhteydessä varmista, että lopullinen commit-viesti noudattaa yllä kuvattua muotoa.

**Esimerkki Squash and Merge -yhdistämisestä**
Jos PR sisältää seuraavat commitit:

- `korjaa kirjoitusvirhe`
- `päivitä README`
- `säädä muotoilua`

Ne yhdistetään muotoon:
`Docs: Paranna dokumentaation selkeyttä ja muotoilua (#65)`

### Julkaisuprosessi

Tässä osiossa kuvataan helpoin tapa ylläpitäjille julkaista uusi versio Co-op Translatorista.

#### 1. Versiotunnuksen päivitys `pyproject.toml`-tiedostossa

1. Päätä seuraava versiotunnus (käytämme semanttista versionhallintaa: `MAJOR.MINOR.PATCH`).
2. Muokkaa `pyproject.toml`-tiedostoa ja päivitä `version`-kenttä `[tool.poetry]`-osion alla.
3. Avaa oma pull request, joka muuttaa vain version (ja mahdolliset automaattisesti päivittyvät lukko- tai metatiedostot).
4. Tarkastuksen jälkeen käytä **Squash and Merge** -yhdistämistä ja varmista, että lopullinen commit-viesti noudattaa yllä kuvattua muotoa.

#### 2. GitHub Release -julkaisun luominen

1. Mene GitHub-repositorion sivulle ja avaa **Releases** → **Draft a new release**.
2. Luo uusi tagi (esim. `v0.13.0`) `main`-haaran pohjalta.
3. Aseta julkaisun otsikoksi sama versio (esim. `v0.13.0`).
4. Klikkaa **Generate release notes** täyttääksesi automaattisesti muutosten lokin.
5. Muokkaa tekstiä halutessasi (esim. korosta uusia kieliä tai tärkeitä muutoksia).
6. Julkaise release.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->