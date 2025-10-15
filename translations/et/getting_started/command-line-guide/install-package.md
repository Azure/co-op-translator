<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T05:00:05+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "et"
}
-->
# Paigalda Co-op Translator pakett

**Co-op Translator** on käsurea tööriist (CLI), mis aitab sul tõlkida kõik oma projekti markdown-failid ja pildid mitmesse keelde. See juhend aitab sul tõlkijat seadistada ja kasutada erinevateks otstarveteks.

### Loo virtuaalne keskkond

Virtuaalse keskkonna saad luua kas `pip` või `Poetry` abil. Sisesta üks järgmistest käskudest oma terminali.

#### Kasutades pip-i

```bash
python -m venv .venv
```

#### Kasutades Poetry-t

```bash
poetry init
```

### Aktiveeri virtuaalne keskkond

Pärast virtuaalse keskkonna loomist tuleb see aktiveerida. Sammud sõltuvad sinu operatsioonisüsteemist. Sisesta järgmine käsk oma terminali.

#### Pip-i ja Poetry jaoks

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Kasutades Poetry-t

1. Kui lõid keskkonna Poetry-ga, sisesta järgmine käsk oma terminali, et see aktiveerida.

    ```bash
    poetry shell
    ```

### Paketi ja vajalike pakettide paigaldamine

Kui virtuaalne keskkond on loodud ja aktiveeritud, tuleb paigaldada vajalikud sõltuvused.

### Kiire paigaldus

Paigalda Co-Op Translator pip-i abil

```
pip install co-op-translator
```
Või 

Paigalda Poetry abil
```
poetry add co-op-translator
```

#### Kasutades pip-i (requirements.txt kaudu), kui kloonid selle repo

> [!NOTE]
> Palun ÄRA tee seda, kui paigaldad co-op translatori kiire paigaldusega.

1. Kui kasutad pip-i, sisesta järgmine käsk oma terminali. See paigaldab automaatselt kõik vajalikud paketid, mis on kirjas failis `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Kasutades Poetry-t (pyproject.toml kaudu)

1. Kui kasutad Poetry-t, sisesta järgmine käsk oma terminali. See paigaldab automaatselt kõik vajalikud paketid, mis on kirjas failis `pyproject.toml`:

    ```bash
    poetry install
    ```

---

**Vastutusest loobumine**:  
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, tuleb arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokumenti selle algses keeles tuleks pidada autoriteetseks allikaks. Kriitilise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgendamise eest.