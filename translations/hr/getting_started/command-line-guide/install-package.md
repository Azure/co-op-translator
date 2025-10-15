<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T04:06:55+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "hr"
}
-->
# Instalirajte Co-op Translator paket

**Co-op Translator** je alat za komandnu liniju (CLI) koji vam pomaže prevesti sve markdown datoteke i slike u vašem projektu na više jezika. Ovaj vodič će vas provesti kroz konfiguraciju prevoditelja i njegovo pokretanje za različite scenarije.

### Kreirajte virtualno okruženje

Virtualno okruženje možete kreirati pomoću `pip` ili `Poetry`. Upišite jednu od sljedećih naredbi u svoj terminal.

#### Korištenje pip-a

```bash
python -m venv .venv
```

#### Korištenje Poetry-a

```bash
poetry init
```

### Aktivirajte virtualno okruženje

Nakon što ste kreirali virtualno okruženje, potrebno ga je aktivirati. Koraci se razlikuju ovisno o operativnom sustavu. Upišite sljedeću naredbu u svoj terminal.

#### Za pip i Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Korištenje Poetry-a

1. Ako ste okruženje kreirali pomoću Poetry-a, upišite sljedeću naredbu u terminal za aktivaciju.

    ```bash
    poetry shell
    ```

### Instalacija paketa i potrebnih ovisnosti

Kada je vaše virtualno okruženje spremno i aktivirano, sljedeći korak je instalacija potrebnih ovisnosti.

### Brza instalacija

Instalirajte Co-Op Translator putem pip-a

```
pip install co-op-translator
```
Ili

Instalirajte putem Poetry-a
```
poetry add co-op-translator
```

#### Korištenje pip-a (iz requirements.txt) ako ste klonirali ovaj repozitorij

> [!NOTE]
> Nemojte ovo raditi ako instalirate co-op translator putem brze instalacije.

1. Ako koristite pip, upišite sljedeću naredbu u terminal. Ona će automatski instalirati potrebne pakete navedene u datoteci `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Korištenje Poetry-a (iz pyproject.toml)

1. Ako koristite Poetry, upišite sljedeću naredbu u terminal. Ona će automatski instalirati potrebne pakete navedene u datoteci `pyproject.toml`:

    ```bash
    poetry install
    ```

---

**Odricanje od odgovornosti**:
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na svom izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne preuzimamo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.