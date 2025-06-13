<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:36:36+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "tl"
}
-->
# I-install ang Co-op translator package

Ang **Co-op Translator** ay isang command-line interface (CLI) tool na dinisenyo para tulungan kang isalin ang lahat ng markdown files at mga larawan sa iyong proyekto sa iba't ibang wika. Gabay ka ng tutorial na ito sa pag-configure ng translator at paggamit nito para sa iba't ibang sitwasyon.

### Gumawa ng virtual environment

Maaari kang gumawa ng virtual environment gamit ang alinman sa `pip` o `Poetry`. I-type ang isa sa mga sumusunod na utos sa loob ng iyong terminal.

#### Gamit ang pip

```bash
python -m venv .venv
```

#### Gamit ang Poetry

```bash
poetry init
```

### I-activate ang virtual environment

Pagkatapos mong gumawa ng virtual environment, kailangan mo itong i-activate. Nagkakaiba ang mga hakbang depende sa iyong operating system. I-type ang sumusunod na utos sa loob ng iyong terminal.

#### Para sa parehong pip at Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Gamit ang Poetry

1. Kung ginawa mo ang environment gamit ang Poetry, i-type ang sumusunod na utos sa iyong terminal para i-activate ito.

    ```bash
    poetry shell
    ```

### Pag-install ng Package at mga kinakailangang Packages

Kapag na-setup at na-activate na ang iyong virtual environment, ang susunod na hakbang ay i-install ang mga kinakailangang dependencies.

### Mabilisang install

I-install ang Co-Op Translator gamit ang pip

```
pip install co-op-translator
```
O kaya 

I-install gamit ang poetry
```
poetry add co-op-translator
```

#### Gamit ang pip (mula sa requirements.txt) kung kinopya mo ang repo na ito

![NOTE] Huwag gawin ito kung nag-install ka ng co-op translator gamit ang mabilisang install.

1. Kung gumagamit ka ng pip, i-type ang sumusunod na utos sa iyong terminal. Awtomatikong i-install nito ang mga kinakailangang packages na nakasaad sa `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

#### Gamit ang Poetry (mula sa pyproject.toml)

1. Kung gumagamit ka ng Poetry, i-type ang sumusunod na utos sa iyong terminal. Awtomatikong i-install nito ang mga kinakailangang packages na nakasaad sa `pyproject.toml` file:

    ```bash
    poetry install
    ```

**Pahayag ng Pagsuway**:  
Ang dokumentong ito ay isinalin gamit ang serbisyong AI na pagsasalin [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.