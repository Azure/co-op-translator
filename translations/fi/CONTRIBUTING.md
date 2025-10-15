<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T03:26:01+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "fi"
}
-->
# Osallistuminen Co-op Translator -projektiin

Tähän projektiin ovat tervetulleita kaikki kontribuutiot ja ehdotukset. Useimmat kontribuutiot edellyttävät, että hyväksyt Contributor License Agreementin (CLA), jossa vakuutat, että sinulla on oikeus antaa meille oikeudet käyttää kontribuutiotasi. Lisätietoja: https://cla.opensource.microsoft.com.

Kun lähetät pull requestin, CLA-botti tarkistaa automaattisesti, tarvitsetko CLA:n, ja merkitsee PR:n sen mukaisesti (esim. tilatarkistus, kommentti). Seuraa vain botin antamia ohjeita. Tämä tarvitsee tehdä vain kerran kaikissa repositorioissa, jotka käyttävät CLA:ta.

## Kehitysympäristön asennus

Tämän projektin kehitysympäristön asennukseen suosittelemme Poetrya riippuvuuksien hallintaan. Käytämme `pyproject.toml`-tiedostoa projektin riippuvuuksien hallintaan, joten riippuvuudet kannattaa asentaa Poetrylla.

### Virtuaaliympäristön luominen

#### pipillä

```bash
python -m venv .venv
```

#### Poetrylla

```bash
poetry init
```

### Virtuaaliympäristön aktivointi

#### Sekä pipille että Poetrylle

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetrylla

```bash
poetry shell
```

### Paketin ja tarvittavien riippuvuuksien asennus

#### Poetrylla (pyproject.toml-tiedostosta)

```bash
poetry install
```

### Manuaalinen testaus

Ennen PR:n lähettämistä on tärkeää testata käännöstoiminnallisuutta oikealla dokumentaatiolla:

1. Luo testikansio projektin juureen:
    ```bash
    mkdir test_docs
    ```

2. Kopioi haluamasi markdown-dokumentaatio ja kuvat testikansioon. Esimerkiksi:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Asenna paketti paikallisesti:
    ```bash
    pip install -e .
    ```

4. Aja Co-op Translator testidokumenteillasi:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Tarkista käännetyt tiedostot kansioista `test_docs/translations` ja `test_docs/translated_images` varmistaaksesi:
   - Käännöksen laatu
   - Metatietokommentit ovat oikein
   - Alkuperäinen markdown-rakenne säilyy
   - Linkit ja kuvat toimivat oikein

Tämä manuaalinen testaus auttaa varmistamaan, että muutoksesi toimivat hyvin todellisissa tilanteissa.

### Ympäristömuuttujat

1. Luo `.env`-tiedosto projektin juureen kopioimalla mukana tuleva `.env.template`-tiedosto.
1. Täytä ympäristömuuttujat ohjeiden mukaisesti.

> [!TIP]
>
> ### Lisävaihtoehtoja kehitysympäristölle
>
> Voit ajaa projektia paikallisesti, mutta vaihtoehtoisesti voit käyttää myös GitHub Codespacesia tai VS Code Dev Containersia kehitysympäristön pystyttämiseen.
>
> #### GitHub Codespaces
>
> Voit ajaa näitä esimerkkejä virtuaalisesti GitHub Codespacesilla ilman lisäasetuksia.
>
> Painike avaa selainpohjaisen VS Code -instanssin:
>
> 1. Avaa pohja (tämä voi kestää muutaman minuutin):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Paikallinen ajo VS Code Dev Containersilla
>
> ⚠️ Tämä vaihtoehto toimii vain, jos Docker Desktopille on varattu vähintään 16 GB RAM-muistia. Jos muistia on vähemmän, kokeile [GitHub Codespaces -vaihtoehtoa](../..) tai [asennusta paikallisesti](../..).
>
> Toinen vaihtoehto on VS Code Dev Containers, joka avaa projektin paikallisessa VS Codessa [Dev Containers -laajennuksella](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Käynnistä Docker Desktop (asenna, jos ei ole jo asennettu)
> 2. Avaa projekti:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Koodityyli

Käytämme [Blackia](https://github.com/psf/black) Python-koodin muotoiluun, jotta koodityyli pysyy yhtenäisenä koko projektissa. Black on automaattinen koodinmuotoilija, joka muotoilee Python-koodin Blackin tyyliin.

#### Konfiguraatio

Blackin asetukset löytyvät `pyproject.toml`-tiedostosta:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Blackin asennus

Voit asentaa Blackin joko Poetrylla (suositeltavaa) tai pipillä:

##### Poetrylla

Black asentuu automaattisesti kehitysympäristön asennuksen yhteydessä:
```bash
poetry install
```

##### pipillä

Jos käytät pipiä, voit asentaa Blackin suoraan:
```bash
pip install black
```

#### Blackin käyttö

##### Poetrylla

1. Muotoile kaikki Python-tiedostot projektissa:
    ```bash
    poetry run black .
    ```

2. Muotoile tietty tiedosto tai kansio:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pipillä

1. Muotoile kaikki Python-tiedostot projektissa:
    ```bash
    black .
    ```

2. Muotoile tietty tiedosto tai kansio:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Suosittelemme asettamaan editorisi muotoilemaan koodin automaattisesti Blackilla tallennuksen yhteydessä. Useimmat modernit editorit tukevat tätä laajennusten tai lisäosien avulla.

## Co-op Translatorin ajaminen

Voit ajaa Co-op Translatoria Poetrylla seuraavasti:

1. Siirry kansioon, jossa haluat tehdä käännöstestejä, tai luo väliaikainen kansio testausta varten.

2. Suorita seuraava komento. Korvaa `-l ko` haluamallasi kielikoodilla. `-d`-lippu käynnistää debug-tilan.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Varmista, että Poetry-ympäristö on aktivoitu (poetry shell) ennen komennon suorittamista.

## Uuden kielen lisääminen

Otamme mielellämme vastaan kontribuutioita, jotka lisäävät tuen uusille kielille. Ennen PR:n avaamista tee seuraavat vaiheet, jotta tarkistus sujuu sujuvasti.

1. Lisää kieli fonttikarttaan
   - Muokkaa tiedostoa `src/co_op_translator/fonts/font_language_mappings.yml`
   - Lisää rivi, jossa on:
     - `code`: ISO-tyyppinen kielikoodi (esim. `vi`)
     - `name`: Ihmisläheinen nimi
     - `font`: Fontti, joka löytyy kansiosta `src/co_op_translator/fonts/` ja tukee kyseistä kirjoitusjärjestelmää
     - `rtl`: `true`, jos oikealta vasemmalle, muuten `false`

2. Lisää tarvittavat fonttitiedostot (tarvittaessa)
   - Jos uusi fontti tarvitaan, varmista, että sen lisenssi sallii avoimen lähdekoodin jakelun
   - Lisää fonttitiedosto kansioon `src/co_op_translator/fonts/`

3. Paikallinen testaus
   - Aja käännös pienellä esimerkillä (Markdown, kuvat ja notebookit tarpeen mukaan)
   - Varmista, että tuloste näkyy oikein, mukaan lukien fontit ja mahdollinen RTL-asettelu

4. Päivitä dokumentaatio
   - Varmista, että kieli näkyy tiedostossa `getting_started/supported-languages.md`
   - Tiedostoon `README_languages_template.md` ei tarvitse tehdä muutoksia; se generoidaan tuetun listan perusteella

5. Avaa PR
   - Kuvaile lisätty kieli ja mahdolliset fontti/lisenssihuomiot
   - Liitä mukaan kuvakaappauksia renderöidyistä tulosteista, jos mahdollista

Esimerkki YAML-rivistä:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Ylläpitäjille

### Commit-viestit ja yhdistämisstrategia

Jotta projektin commit-historia pysyy selkeänä ja johdonmukaisena, noudatamme tiettyä commit-viestien muotoa **lopullisessa commit-viestissä** käytettäessä **Squash and Merge** -strategiaa.

Kun pull request (PR) yhdistetään, yksittäiset commitit yhdistetään yhdeksi commitiksi. Lopullisen commit-viestin tulee noudattaa alla olevaa muotoa, jotta historia pysyy siistinä ja yhtenäisenä.

#### Commit-viestin muoto (squash and merge)

Käytämme seuraavaa muotoa commit-viesteissä:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Määrittää commitin kategorian. Käytämme seuraavia tyyppejä:
  - `Docs`: Dokumentaatiopäivitykset.
  - `Build`: Muutokset build-järjestelmään tai riippuvuuksiin, mukaan lukien konfiguraatiotiedostot, CI-työnkulut tai Dockerfile.
  - `Core`: Projektin ydintoiminnallisuuden tai ominaisuuksien muutokset, erityisesti `src/co_op_translator/core`-kansiossa.

- **description**: Tiivis yhteenveto muutoksesta.
- **PR number**: Pull requestin numero.

**Esimerkkejä**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Tällä hetkellä **`Docs`**, **`Core`** ja **`Build`** -etuliitteet lisätään automaattisesti PR-otsikoihin muokattujen lähdekooditiedostojen perusteella. Kunhan oikea label on lisätty, sinun ei yleensä tarvitse muokata PR-otsikkoa käsin. Tarkista vain, että kaikki on oikein ja etuliite on muodostettu oikein.

#### Yhdistämisstrategia

Käytämme oletuksena **Squash and Merge** -strategiaa pull requesteille. Tämä varmistaa, että commit-viestit noudattavat muotoamme, vaikka yksittäiset commitit eivät sitä tekisikään.

**Perustelut**:

- Selkeä, lineaarinen projektihistoria.
- Johdonmukaiset commit-viestit.
- Vähemmän hälyä pienistä commiteista (esim. "fix typo").

Yhdistettäessä varmista, että lopullinen commit-viesti noudattaa yllä kuvattua muotoa.

**Esimerkki Squash and Merge -yhdistämisestä**
Jos PR sisältää seuraavat commitit:

- `fix typo`
- `update README`
- `adjust formatting`

Ne yhdistetään muotoon:
`Docs: Improve documentation clarity and formatting (#65)`

---

**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisissä tapauksissa suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa tämän käännöksen käytöstä mahdollisesti aiheutuvista väärinkäsityksistä tai tulkintavirheistä.