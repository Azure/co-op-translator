<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:38:16+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "sl"
}
-->
# Namestitev paketa Co-op translator

**Co-op Translator** je orodje z ukazno vrstico (CLI), ki vam pomaga prevesti vse markdown datoteke in slike v vašem projektu v več jezikov. Ta vodič vas bo popeljal skozi nastavitev prevajalnika in njegovo uporabo za različne primere.

### Ustvarjanje virtualnega okolja

Virtualno okolje lahko ustvarite z uporabo `pip` ali `Poetry`. V terminal vnesite eno od naslednjih ukazov.

#### Uporaba pip

```bash
python -m venv .venv
```

#### Uporaba Poetry

```bash
poetry init
```

### Aktivacija virtualnega okolja

Ko ustvarite virtualno okolje, ga morate aktivirati. Postopek je odvisen od vašega operacijskega sistema. V terminal vnesite naslednji ukaz.

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

Ko je virtualno okolje pripravljeno in aktivirano, je naslednji korak namestitev potrebnih paketov.

### Hitro nameščanje

Namestite Co-Op Translator preko pip

```
pip install co-op-translator
```
Ali

Namestite preko Poetry
```
poetry add co-op-translator
```

#### Uporaba pip (iz requirements.txt), če ste klonirali ta repozitorij

![NOTE] Prosimo, tega ne počnite, če ste Co-op translator namestili preko hitre namestitve.

1. Če uporabljate pip, v terminal vnesite naslednji ukaz. Samodejno bo namestil potrebne pakete, določene v datoteki `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Uporaba Poetry (iz pyproject.toml)

1. Če uporabljate Poetry, v terminal vnesite naslednji ukaz. Samodejno bo namestil potrebne pakete, določene v datoteki `pyproject.toml`:

    ```bash
    poetry install
    ```

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.