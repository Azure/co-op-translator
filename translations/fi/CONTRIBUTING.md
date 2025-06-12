<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:37:18+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "fi"
}
-->
# Osallistuminen Co-op Translator -projektiin

Tämä projekti toivottaa tervetulleiksi kontribuutiot ja ehdotukset. Useimmat kontribuutiot edellyttävät, että hyväksyt Contributor License Agreementin (CLA), jossa vahvistat, että sinulla on oikeus myöntää meille oikeudet käyttää panostustasi. Lisätietoja löytyy osoitteesta https://cla.opensource.microsoft.com.

Kun lähetät pull requestin, CLA-botti tarkistaa automaattisesti, tarvitseeko sinun toimittaa CLA ja merkitsee PR:n asianmukaisesti (esim. tilantarkistus, kommentti). Noudata vain botin antamia ohjeita. Tätä tarvitsee tehdä vain kerran kaikissa CLA:ta käyttävissä repositorioissa.

## Kehitysympäristön asennus

Tämän projektin kehitysympäristön pystyttämiseen suosittelemme Poetrya riippuvuuksien hallintaan. Käytämme `pyproject.toml` projektin riippuvuuksien hallintaan, joten riippuvuuksien asentamiseen tulee käyttää Poetrya.

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

#### Sekä pipille että Poetrylle

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

#### Poetryn avulla (pyproject.toml -tiedostosta)

```bash
poetry install
```

### Manuaalinen testaus

Ennen PR:n lähettämistä on tärkeää testata käännöstoiminnallisuus oikealla dokumentaatiolla:

1. Luo testihakemisto juurihakemistoon:
    ```bash
    mkdir test_docs
    ```

2. Kopioi testihakemistoon markdown-dokumentaatiota ja kuvia, jotka haluat kääntää. Esimerkiksi:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Asenna paketti paikallisesti:
    ```bash
    pip install -e .
    ```

4. Suorita Co-op Translator testiasiakirjoillasi:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Tarkista käännetyt tiedostot hakemistosta `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`.
1. Täytä ympäristömuuttujat ohjeiden mukaisesti.

> [!TIP]
>
> ### Lisävaihtoehtoja kehitysympäristölle
>
> Projektin ajamisen lisäksi paikallisesti voit käyttää myös GitHub Codespacesia tai VS Code Dev Containersia vaihtoehtoisena kehitysympäristönä.
>
> #### GitHub Codespaces
>
> Voit ajaa tämän esimerkin virtuaalisesti GitHub Codespacesin avulla ilman lisäasetuksia tai -asennuksia.
>
> Painike avaa selaimessasi web-pohjaisen VS Code -instanssin:
>
> 1. Avaa template (avaaminen voi kestää muutaman minuutin):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Paikallinen ajaminen VS Code Dev Containersilla
>
> ⚠️ Tämä vaihtoehto toimii vain, jos Docker Desktopilla on varattu vähintään 16 GB RAM-muistia. Jos RAM-muistia on alle 16 GB, voit kokeilla [GitHub Codespaces -vaihtoehtoa](../..) tai [pystyttää ympäristön paikallisesti](../..).
>
> Vaihtoehtona on VS Code Dev Containers, joka avaa projektin paikallisessa VS Codessa käyttäen [Dev Containers -laajennusta](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Käynnistä Docker Desktop (asennus tarvittaessa)
> 2. Avaa projekti:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Koodityyli

Käytämme [Black](https://github.com/psf/black) -työkalua Python-koodin muotoiluun, jotta koodityyli pysyy yhtenäisenä projektissa. Black on tinkimätön koodinmuotoilija, joka muokkaa Python-koodin automaattisesti noudattamaan Blackin koodityyliohjeita.

#### Konfigurointi

Blackin asetukset on määritelty `pyproject.toml`-tiedostossamme:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Blackin asentaminen

Blackin voi asentaa joko Poetrylla (suositeltu) tai pipillä:

##### Poetryn avulla

Black asennetaan automaattisesti, kun pystytät kehitysympäristön:
```bash
poetry install
```

##### Pipin avulla

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

2. Muotoile tietty tiedosto tai hakemisto:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Pipillä

1. Muotoile kaikki Python-tiedostot projektissa:
    ```bash
    black .
    ```

2. Muotoile tietty tiedosto tai hakemisto:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Suosittelemme konfiguroimaan editorisi muotoilemaan koodin automaattisesti Blackilla tallennuksen yhteydessä. Useimmat nykyaikaiset editorit tukevat tätä laajennusten tai pluginien kautta.

## Co-op Translatorin ajaminen

Co-op Translatorin ajamiseksi Poetrylla omassa ympäristössäsi, toimi seuraavasti:

1. Siirry hakemistoon, jossa haluat tehdä käännöstestauksen, tai luo väliaikainen kansio testausta varten.

2. Suorita seuraava komento. Korvaa `-l ko` with the language code you wish to translate into. The `-d` -valitsin tarkoittaa debug-tilaa.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Varmista, että Poetry-ympäristö on aktivoitu (poetry shell) ennen komennon suorittamista.

## Ylläpitäjät

### Commit-viesti ja yhdistämisstrategia

Projektimme commit-historian johdonmukaisuuden ja selkeyden varmistamiseksi noudatamme tiettyä commit-viestin formaattia **viimeisessä commit-viestissä** käytettäessä **Squash and Merge** -strategiaa.

Kun pull request yhdistetään, yksittäiset commitit yhdistetään yhdeksi commitiksi. Lopullisen commit-viestin tulee noudattaa alla olevaa formaattia, jotta historia pysyy siistinä ja yhtenäisenä.

#### Commit-viestin formaatti (squash and merge)

Käytämme seuraavaa formaattia commit-viesteissä:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Määrittää commitin kategorian. Käytämme seuraavia tyyppejä:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Päivitä asennusohjeet selkeyden vuoksi (#50)`
- `Core: Paranna kuvakäännöksen käsittelyä (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `korjaa kirjoitusvirhe`
- `päivitä README`
- `säädä muotoilua`

They should be squashed into:
`Docs: Paranna dokumentaation selkeyttä ja muotoilua (#65)`

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää auktoritatiivisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai tulkinnoista.