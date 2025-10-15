<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T04:09:54+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "sl"
}
-->
# Namestitev paketa Co-op Translator

**Co-op Translator** je orodje za ukazno vrstico (CLI), namenjeno prevajanju vseh markdown datotek in slik v vašem projektu v več jezikov. Ta vodič vas bo popeljal skozi nastavitev prevajalnika in njegovo uporabo v različnih primerih.

### Ustvarite virtualno okolje

Virtualno okolje lahko ustvarite z uporabo `pip` ali `Poetry`. V terminal vnesite enega od naslednjih ukazov.

#### Uporaba pip

```bash
python -m venv .venv
```

#### Uporaba Poetry

```bash
poetry init
```

### Aktivirajte virtualno okolje

Ko ustvarite virtualno okolje, ga morate aktivirati. Koraki se razlikujejo glede na vaš operacijski sistem. V terminal vnesite naslednji ukaz.

#### Za pip in Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Uporaba Poetry

1. Če ste okolje ustvarili s Poetry, v terminal vnesite naslednji ukaz za aktivacijo.

    ```bash
    poetry shell
    ```

### Namestitev paketa in potrebnih odvisnosti

Ko je vaše virtualno okolje pripravljeno in aktivirano, je naslednji korak namestitev potrebnih odvisnosti.

### Hitra namestitev

Namestite Co-Op Translator prek pip

```
pip install co-op-translator
```
Ali 

Namestite prek poetry
```
poetry add co-op-translator
```

#### Uporaba pip (iz requirements.txt), če klonirate ta repozitorij

> [!NOTE]
> Tega NE počnite, če nameščate co-op translator prek hitre namestitve.

1. Če uporabljate pip, v terminal vnesite naslednji ukaz. Samodejno bo namestil potrebne pakete, ki so navedeni v datoteki `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Uporaba Poetry (iz pyproject.toml)

1. Če uporabljate Poetry, v terminal vnesite naslednji ukaz. Samodejno bo namestil potrebne pakete, ki so navedeni v datoteki `pyproject.toml`:

    ```bash
    poetry install
    ```

---

**Izjava o omejitvi odgovornosti**:
Ta dokument je bil preveden s pomočjo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem maternem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokoven človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi izhajale iz uporabe tega prevoda.