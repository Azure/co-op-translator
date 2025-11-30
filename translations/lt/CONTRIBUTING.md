<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T12:50:47+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "lt"
}
-->
# Prisidėjimas prie Co-op Translator

Šis projektas laukia indėlių ir pasiūlymų. Daugumai indėlių reikia sutikti su
Indėlio Licencijos Sutartimi (CLA), kurioje patvirtinate, kad turite teisę ir iš tikrųjų suteikiate mums
teisę naudoti jūsų indėlį. Daugiau informacijos rasite https://cla.opensource.microsoft.com.

Kai pateikiate pull request, CLA robotas automatiškai nustatys, ar jums reikia pateikti
CLA ir tinkamai pažymės PR (pvz., statuso patikrinimas, komentaras). Tiesiog sekite roboto nurodymus.
Tai reikės padaryti tik vieną kartą visuose repozitorijuose, naudojančiuose mūsų CLA.

## Vystymo aplinkos nustatymas

Norėdami nustatyti šio projekto vystymo aplinką, rekomenduojame naudoti Poetry priklausomybių valdymui. Mes naudojame `pyproject.toml` projekto priklausomybėms valdyti, todėl priklausomybių diegimui turėtumėte naudoti Poetry.

### Sukurkite virtualią aplinką

#### Naudojant pip

```bash
python -m venv .venv
```

#### Naudojant Poetry

```bash
poetry init
```

### Aktyvuokite virtualią aplinką

#### Tiek pip, tiek Poetry atveju

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Naudojant Poetry

```bash
poetry shell
```

### Paketo ir reikalingų paketų diegimas

#### Naudojant Poetry (iš pyproject.toml)

```bash
poetry install
```

### Rankinis testavimas

Prieš pateikdami PR, svarbu išbandyti vertimo funkcionalumą su tikra dokumentacija:

1. Sukurkite testų katalogą pagrindiniame kataloge:
    ```bash
    mkdir test_docs
    ```

2. Nukopijuokite keletą markdown dokumentų ir paveikslėlių, kuriuos norite išversti, į testų katalogą. Pavyzdžiui:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Įdiekite paketą lokaliai:
    ```bash
    pip install -e .
    ```

4. Paleiskite Co-op Translator savo testiniams dokumentams:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Patikrinkite išverstus failus `test_docs/translations` ir `test_docs/translated_images`, kad įsitikintumėte:
   - Vertimo kokybe
   - Metaduomenų komentarai yra teisingi
   - Originali markdown struktūra išsaugota
   - Nuorodos ir paveikslėliai veikia tinkamai

Šis rankinis testavimas padeda užtikrinti, kad jūsų pakeitimai gerai veiktų realiomis sąlygomis.

### Aplinkos kintamieji

1. Sukurkite `.env` failą pagrindiniame kataloge nukopijuodami pateiktą `.env.template` failą.
1. Užpildykite aplinkos kintamuosius pagal nurodymus.

> [!TIP]
>
> ### Papildomos vystymo aplinkos galimybės
>
> Be projekto paleidimo lokaliai, galite naudoti GitHub Codespaces arba VS Code Dev Containers kaip alternatyvią vystymo aplinką.
>
> #### GitHub Codespaces
>
> Šiuos pavyzdžius galite paleisti virtualiai naudodami GitHub Codespaces, nereikia jokių papildomų nustatymų ar konfigūracijų.
>
> Mygtukas atvers naršyklėje veikiantį VS Code langą:
>
> 1. Atidarykite šabloną (tai gali užtrukti kelias minutes):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Paleidimas lokaliai naudojant VS Code Dev Containers
>
> ⚠️ Ši parinktis veiks tik jei jūsų Docker Desktop turi bent 16 GB RAM. Jei turite mažiau nei 16 GB RAM, galite išbandyti [GitHub Codespaces parinktį](../..) arba [nustatyti lokaliai](../..).
>
> Susijusi parinktis yra VS Code Dev Containers, kuri atvers projektą jūsų vietiniame VS Code naudodama [Dev Containers plėtinį](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Paleiskite Docker Desktop (įdiekite, jei dar neįdiegta)
> 2. Atidarykite projektą:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Kodo stilius

Naudojame [Black](https://github.com/psf/black) kaip Python kodo formatavimo įrankį, kad palaikytume nuoseklų kodo stilių projekte. Black yra griežtas kodo formatuotojas, kuris automatiškai pertvarko Python kodą pagal Black stiliaus taisykles.

#### Konfigūracija

Black konfigūracija nurodyta mūsų `pyproject.toml` faile:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black diegimas

Galite įdiegti Black naudodami Poetry (rekomenduojama) arba pip:

##### Naudojant Poetry

Black automatiškai įdiegiama nustatant vystymo aplinką:
```bash
poetry install
```

##### Naudojant pip

Jei naudojate pip, Black galite įdiegti tiesiogiai:
```bash
pip install black
```

#### Black naudojimas

##### Su Poetry

1. Suformatuokite visus Python failus projekte:
    ```bash
    poetry run black .
    ```

2. Suformatuokite konkretų failą arba katalogą:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Su pip

1. Suformatuokite visus Python failus projekte:
    ```bash
    black .
    ```

2. Suformatuokite konkretų failą arba katalogą:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Rekomenduojame nustatyti savo redaktorių automatiškai formatuoti kodą su Black įrašant. Dauguma šiuolaikinių redaktorių tai palaiko per plėtinius ar papildinius.

## Co-op Translator paleidimas

Norėdami paleisti Co-op Translator naudodami Poetry savo aplinkoje, atlikite šiuos veiksmus:

1. Eikite į katalogą, kuriame norite atlikti vertimo testus, arba sukurkite laikiną aplanką testavimui.

2. Vykdykite šią komandą. Pakeiskite `-l ko` į norimos kalbos kodą, į kurią norite versti. `-d` žymi derinimo režimą.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Įsitikinkite, kad jūsų Poetry aplinka yra aktyvuota (poetry shell) prieš vykdant komandą.

## Prisidėkite naują kalbą

Laukiame indėlių, kurie prideda naujų kalbų palaikymą. Prieš atidarydami PR, atlikite žemiau nurodytus veiksmus, kad užtikrintumėte sklandų peržiūrėjimą.

1. Pridėkite kalbą prie šrifto žemėlapio
   - Redaguokite `src/co_op_translator/fonts/font_language_mappings.yml`
   - Pridėkite įrašą su:
     - `code`: ISO tipo kalbos kodas (pvz., `vi`)
     - `name`: Žmogiškai suprantamas pavadinimas
     - `font`: Šriftas, esantis `src/co_op_translator/fonts/`, palaikantis tą raštą
     - `rtl`: `true`, jei rašoma iš dešinės į kairę, kitu atveju `false`

2. Įtraukite reikalingus šrifto failus (jei reikia)
   - Jei reikalingas naujas šriftas, patikrinkite licencijos suderinamumą su atviro kodo platinimu
   - Pridėkite šrifto failą į `src/co_op_translator/fonts/`

3. Vietinis patikrinimas
   - Paleiskite vertimus mažam pavyzdžiui (Markdown, paveikslėliai ir užrašų knygelės pagal poreikį)
   - Patikrinkite, ar išvestis atvaizduojama teisingai, įskaitant šriftus ir, jei taikoma, RTL išdėstymą

4. Atnaujinkite dokumentaciją
   - Įsitikinkite, kad kalba yra `getting_started/supported-languages.md` faile
   - Nereikia keisti `getting_started/README_languages_template.md`; jis generuojamas iš palaikomų kalbų sąrašo

5. Atidarykite PR
   - Aprašykite pridėtą kalbą ir bet kokius šrifto/licencijos aspektus
   - Jei įmanoma, pridėkite ekrano nuotraukas su atvaizduotais rezultatais

Pavyzdinis YAML įrašas:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Naujos kalbos testavimas

Naują kalbą galite išbandyti paleisdami šią komandą:

```bash
# Sukurkite ir aktyvuokite virtualią aplinką
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Įdiekite kūrimo paketą
pip install -e .
# Vykdykite vertimą
translate -l "new_lang"
```

## Prižiūrėtojai

### Įsipareigojimo žinutės ir sujungimo strategija

Siekiant užtikrinti nuoseklumą ir aiškumą mūsų projekto įsipareigojimų istorijoje, naudojame specifinį įsipareigojimo žinutės formatą **galutinei įsipareigojimo žinutei** naudojant **Squash and Merge** strategiją.

Kai pull request (PR) yra sujungiamas, atskiri įsipareigojimai bus sujungti į vieną. Galutinė įsipareigojimo žinutė turėtų atitikti žemiau pateiktą formatą, kad būtų palaikoma švari ir nuosekli istorija.

#### Įsipareigojimo žinutės formatas (squash and merge atveju)

Naudojame šį formatą įsipareigojimų žinutėms:

```bash
<type>: <description> (#<PR numeris>)
```

- **type**: Nurodo įsipareigojimo kategoriją. Naudojame šiuos tipus:
  - `Docs`: Dokumentacijos atnaujinimams.
  - `Build`: Pakeitimams, susijusiems su statybos sistema ar priklausomybėmis, įskaitant konfigūracijos failų, CI darbo eigų ar Dockerfile atnaujinimus.
  - `Core`: Projekto pagrindinės funkcijos ar savybių pakeitimams, ypač tiems, kurie susiję su failais `src/co_op_translator/core` kataloge.

- **description**: Trumpas pakeitimo aprašymas.
- **PR numeris**: Susijusio pull request numeris.

**Pavyzdžiai**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Šiuo metu **`Docs`**, **`Core`** ir **`Build`** prefiksai automatiškai pridedami prie PR pavadinimų pagal modifikuoto kodo etiketes. Jei tinkama etikete pritaikyta, paprastai nereikia rankiniu būdu keisti PR pavadinimo. Tiesiog patikrinkite, ar viskas teisinga ir prefiksas sugeneruotas tinkamai.

#### Sujungimo strategija

Naudojame **Squash and Merge** kaip numatytąją strategiją pull requestams. Ši strategija užtikrina, kad įsipareigojimų žinutės atitiktų mūsų formatą, net jei atskiri įsipareigojimai to nedaro.

**Priežastys**:

- Švari, linijinė projekto istorija.
- Nuoseklumas įsipareigojimų žinutėse.
- Mažiau triukšmo dėl smulkių įsipareigojimų (pvz., „fix typo“).

Sujungiant, įsitikinkite, kad galutinė įsipareigojimo žinutė atitinka aukščiau aprašytą formatą.

**Squash and Merge pavyzdys**
Jei PR turi šiuos įsipareigojimus:

- `fix typo`
- `update README`
- `adjust formatting`

Jie turėtų būti sujungti į:
`Docs: Improve documentation clarity and formatting (#65)`

### Leidimo procesas

Šiame skyriuje aprašomas paprasčiausias būdas prižiūrėtojams paskelbti naują Co-op Translator leidimą.

#### 1. Padidinkite versiją `pyproject.toml`

1. Nuspręskite kitą versijos numerį (naudojame semantinį versijavimą: `MAJOR.MINOR.PATCH`).
2. Redaguokite `pyproject.toml` ir atnaujinkite `version` lauką po `[tool.poetry]`.
3. Atidarykite specialų pull request, kuriame keičiate tik versiją (ir bet kokius automatiškai atnaujinamus užrakinimo/metaduomenų failus, jei yra).
4. Po peržiūros naudokite **Squash and Merge** ir įsitikinkite, kad galutinė įsipareigojimo žinutė atitinka aukščiau aprašytą formatą.

#### 2. Sukurkite GitHub leidimą

1. Eikite į GitHub repozitorijos puslapį ir atidarykite **Releases** → **Draft a new release**.
2. Sukurkite naują žymę (pvz., `v0.13.0`) iš `main` šakos.
3. Nustatykite leidimo pavadinimą tokiu pačiu numeriu (pvz., `v0.13.0`).
4. Spustelėkite **Generate release notes**, kad automatiškai užpildytumėte pakeitimų žurnalą.
5. Pasirinktinai redaguokite tekstą (pvz., pabrėžkite naujai palaikomas kalbas ar svarbius pakeitimus).
6. Paskelbkite leidimą.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->