<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:38:05+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "hr"
}
-->
# Instalirajte Co-op translator paket

**Co-op Translator** je alat za naredbeni redak (CLI) dizajniran da vam pomogne prevesti sve markdown datoteke i slike u vašem projektu na više jezika. Ovaj vodič će vas provesti kroz konfiguraciju prevoditelja i njegovo pokretanje za različite slučajeve upotrebe.

### Kreirajte virtualno okruženje

Virtualno okruženje možete kreirati koristeći ili `pip` ili `Poetry`. Upišite jednu od sljedećih naredbi u vaš terminal.

#### Korištenje pip-a

```bash
python -m venv .venv
```

#### Korištenje Poetry-ja

```bash
poetry init
```

### Aktivirajte virtualno okruženje

Nakon što ste kreirali virtualno okruženje, potrebno ga je aktivirati. Koraci se razlikuju ovisno o vašem operativnom sustavu. Upišite sljedeću naredbu u terminal.

#### Za pip i Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Korištenje Poetry-ja

1. Ako ste kreirali okruženje pomoću Poetry-ja, upišite sljedeću naredbu u terminal da ga aktivirate.

    ```bash
    poetry shell
    ```

### Instalacija paketa i potrebnih ovisnosti

Nakon što ste postavili i aktivirali virtualno okruženje, sljedeći korak je instalirati potrebne ovisnosti.

### Brza instalacija

Instalirajte Co-Op Translator putem pip-a

```
pip install co-op-translator
```  
Ili  

Instalirajte putem Poetry-ja  
```
poetry add co-op-translator
```

#### Korištenje pip-a (iz requirements.txt) ako ste klonirali ovaj repozitorij

![NOTE] Molimo vas da ovo NE radite ako instalirate co-op translator putem brze instalacije.

1. Ako koristite pip, upišite sljedeću naredbu u terminal. Automatski će instalirati potrebne pakete navedene u datoteci `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Korištenje Poetry-ja (iz pyproject.toml)

1. Ako koristite Poetry, upišite sljedeću naredbu u terminal. Automatski će instalirati potrebne pakete navedene u datoteci `pyproject.toml`:

    ```bash
    poetry install
    ```

**Odricanje od odgovornosti**:  
Ovaj je dokument preveden pomoću AI usluge za prijevod [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.