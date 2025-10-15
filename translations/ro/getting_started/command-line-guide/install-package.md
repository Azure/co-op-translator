<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:58:17+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "ro"
}
-->
# Instalează pachetul Co-op Translator

**Co-op Translator** este un instrument de tip linie de comandă (CLI) creat pentru a te ajuta să traduci toate fișierele markdown și imaginile din proiectul tău în mai multe limbi. Acest tutorial te va ghida prin configurarea translatorului și rularea lui pentru diverse scenarii.

### Creează un mediu virtual

Poți crea un mediu virtual folosind fie `pip`, fie `Poetry`. Tastează una dintre comenzile de mai jos în terminal.

#### Folosind pip

```bash
python -m venv .venv
```

#### Folosind Poetry

```bash
poetry init
```

### Activează mediul virtual

După ce ai creat mediul virtual, va trebui să-l activezi. Pașii diferă în funcție de sistemul de operare. Tastează următoarea comandă în terminal.

#### Pentru pip și Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Folosind Poetry

1. Dacă ai creat mediul cu Poetry, tastează următoarea comandă în terminal pentru a-l activa.

    ```bash
    poetry shell
    ```

### Instalarea pachetului și a pachetelor necesare

După ce mediul virtual este creat și activat, următorul pas este să instalezi dependențele necesare.

### Instalare rapidă

Instalează Co-Op Translator cu pip

```
pip install co-op-translator
```
Sau 

Instalează cu poetry
```
poetry add co-op-translator
```

#### Folosind pip (din requirements.txt) dacă clonezi acest repo

> [!NOTE]
> Te rugăm să NU faci acest lucru dacă instalezi co-op translator prin instalarea rapidă.

1. Dacă folosești pip, tastează următoarea comandă în terminal. Va instala automat pachetele necesare specificate în fișierul `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Folosind Poetry (din pyproject.toml)

1. Dacă folosești Poetry, tastează următoarea comandă în terminal. Va instala automat pachetele necesare specificate în fișierul `pyproject.toml`:

    ```bash
    poetry install
    ```

---

**Declarație de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm răspunderea pentru orice neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.