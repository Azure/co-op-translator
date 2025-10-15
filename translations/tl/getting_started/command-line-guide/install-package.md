<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:43:28+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "tl"
}
-->
# I-install ang Co-op translator package

Ang **Co-op Translator** ay isang command-line interface (CLI) tool na ginawa para tulungan kang isalin ang lahat ng markdown files at mga larawan sa iyong proyekto sa iba't ibang wika. Ang tutorial na ito ay gagabay sa iyo sa pag-configure ng translator at paggamit nito para sa iba't ibang sitwasyon.

### Gumawa ng virtual environment

Maaari kang gumawa ng virtual environment gamit ang `pip` o `Poetry`. I-type ang isa sa mga sumusunod na command sa iyong terminal.

#### Gamit ang pip

```bash
python -m venv .venv
```

#### Gamit ang Poetry

```bash
poetry init
```

### I-activate ang virtual environment

Pagkatapos mong gumawa ng virtual environment, kailangan mo itong i-activate. Magkakaiba ang steps depende sa iyong operating system. I-type ang sumusunod na command sa iyong terminal.

#### Para sa pip at Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Gamit ang Poetry

1. Kung ginawa mo ang environment gamit ang Poetry, i-type ang sumusunod na command sa iyong terminal para i-activate ito.

    ```bash
    poetry shell
    ```

### Pag-install ng Package at mga kinakailangang Package

Kapag na-setup at na-activate mo na ang iyong virtual environment, ang susunod na hakbang ay i-install ang mga kinakailangang dependencies.

### Mabilisang pag-install

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

> [!NOTE]
> Huwag mo itong gawin kung nag-install ka ng co-op translator gamit ang mabilisang pag-install.

1. Kung pip ang gamit mo, i-type ang sumusunod na command sa iyong terminal. Awtomatikong i-install nito ang mga kinakailangang package na nakalista sa `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

#### Gamit ang Poetry (mula sa pyproject.toml)

1. Kung Poetry ang gamit mo, i-type ang sumusunod na command sa iyong terminal. Awtomatikong i-install nito ang mga kinakailangang package na nakalista sa `pyproject.toml` file:

    ```bash
    poetry install
    ```

---

**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi eksaktong salin. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring lumitaw mula sa paggamit ng pagsasaling ito.