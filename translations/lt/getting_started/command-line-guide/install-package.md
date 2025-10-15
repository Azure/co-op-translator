<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T04:59:47+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "lt"
}
-->
# Įdiekite Co-op vertėjo paketą

**Co-op Translator** yra komandinės eilutės (CLI) įrankis, skirtas padėti išversti visus jūsų projekto markdown failus ir paveikslėlius į kelias kalbas. Šiame vadove sužinosite, kaip sukonfigūruoti vertėją ir paleisti jį įvairiais atvejais.

### Sukurkite virtualią aplinką

Virtualią aplinką galite sukurti naudodami `pip` arba `Poetry`. Įveskite vieną iš šių komandų savo terminale.

#### Naudojant pip

```bash
python -m venv .venv
```

#### Naudojant Poetry

```bash
poetry init
```

### Aktyvuokite virtualią aplinką

Sukūrę virtualią aplinką, ją reikės aktyvuoti. Veiksmai priklauso nuo jūsų operacinės sistemos. Įveskite šią komandą savo terminale.

#### Tinka tiek pip, tiek Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Naudojant Poetry

1. Jei aplinką sukūrėte su Poetry, įveskite šią komandą savo terminale, kad ją aktyvuotumėte.

    ```bash
    poetry shell
    ```

### Paketo ir reikiamų paketų diegimas

Kai virtuali aplinka jau sukurta ir aktyvuota, kitas žingsnis – įdiegti reikalingas priklausomybes.

### Greitas diegimas

Įdiekite Co-Op Translator per pip

```
pip install co-op-translator
```
Arba 

Įdiekite per poetry
```
poetry add co-op-translator
```

#### Naudojant pip (iš requirements.txt), jei klonuojate šį repozitoriją

> [!NOTE]
> Prašome to nedaryti, jei Co-op translator diegiate per greitą diegimą.

1. Jei naudojate pip, įveskite šią komandą savo terminale. Ji automatiškai įdiegs reikiamus paketus, nurodytus `requirements.txt` faile:

    ```bash
    pip install -r requirements.txt
    ```

#### Naudojant Poetry (iš pyproject.toml)

1. Jei naudojate Poetry, įveskite šią komandą savo terminale. Ji automatiškai įdiegs reikiamus paketus, nurodytus `pyproject.toml` faile:

    ```bash
    poetry install
    ```

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbios informacijos atveju rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretavimą, kilusį naudojantis šiuo vertimu.