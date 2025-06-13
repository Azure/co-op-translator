<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:37:27+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "ro"
}
-->
# Instalează pachetul Co-op translator

**Co-op Translator** este un instrument de linie de comandă (CLI) creat pentru a te ajuta să traduci toate fișierele markdown și imaginile din proiectul tău în mai multe limbi. Acest tutorial te va ghida prin configurarea traducătorului și rularea acestuia pentru diverse cazuri de utilizare.

### Creează un mediu virtual

Poți crea un mediu virtual folosind fie `pip`, fie `Poetry`. Tastează una dintre comenzile de mai jos în terminalul tău.

#### Folosind pip

```bash
python -m venv .venv
```

#### Folosind Poetry

```bash
poetry init
```

### Activează mediul virtual

După ce ai creat mediul virtual, va trebui să îl activezi. Pașii diferă în funcție de sistemul tău de operare. Tastează comanda corespunzătoare în terminal.

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

### Instalarea pachetului și a dependențelor necesare

După ce mediul virtual este configurat și activat, următorul pas este să instalezi dependențele necesare.

### Instalare rapidă

Instalează Co-Op Translator folosind pip

```
pip install co-op-translator
```  
Sau  

Instalează folosind poetry  
```
poetry add co-op-translator
```

#### Folosind pip (din requirements.txt) dacă ai clonat acest repo

![NOTE] Te rugăm să NU faci asta dacă instalezi co-op translator prin instalarea rapidă.

1. Dacă folosești pip, tastează următoarea comandă în terminal. Aceasta va instala automat pachetele necesare specificate în fișierul `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Folosind Poetry (din pyproject.toml)

1. Dacă folosești Poetry, tastează următoarea comandă în terminal. Aceasta va instala automat pachetele necesare specificate în fișierul `pyproject.toml`:

    ```bash
    poetry install
    ```

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.