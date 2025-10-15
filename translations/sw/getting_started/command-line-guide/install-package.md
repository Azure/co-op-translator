<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:46:15+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "sw"
}
-->
# Sakinisha kifurushi cha Co-op Translator

**Co-op Translator** ni zana ya mstari wa amri (CLI) iliyoundwa kukusaidia kutafsiri faili zote za markdown na picha kwenye mradi wako kwenda katika lugha mbalimbali. Mafunzo haya yatakuongoza jinsi ya kusanidi translator na kuiendesha kwa matumizi tofauti.

### Tengeneza mazingira ya virtual

Unaweza kutengeneza mazingira ya virtual kwa kutumia `pip` au `Poetry`. Andika mojawapo ya amri zifuatazo kwenye terminal yako.

#### Kutumia pip

```bash
python -m venv .venv
```

#### Kutumia Poetry

```bash
poetry init
```

### Washa mazingira ya virtual

Baada ya kutengeneza mazingira ya virtual, utahitaji kuyaamsha. Hatua zinatofautiana kulingana na mfumo wa uendeshaji unaotumia. Andika amri ifuatayo kwenye terminal yako.

#### Kwa pip na Poetry zote

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Kutumia Poetry

1. Kama umetengeneza mazingira kwa Poetry, andika amri ifuatayo kwenye terminal yako ili kuyaamsha.

    ```bash
    poetry shell
    ```

### Kusakinisha Kifurushi na Vifurushi vinavyohitajika

Mara mazingira yako ya virtual yakishatengenezwa na kuwashwa, hatua inayofuata ni kusakinisha utegemezi unaohitajika.

### Usakinishaji wa haraka

Sakinisha Co-Op Translator kupitia pip

```
pip install co-op-translator
```
Au 

Sakinisha kupitia poetry
```
poetry add co-op-translator
```

#### Kutumia pip (kutoka requirements.txt) kama umeclone repo hii 

> [!NOTE]
> Tafadhali USIFANYE hivi kama umesakinisha co-op translator kupitia usakinishaji wa haraka.

1. Kama unatumia pip, andika amri ifuatayo kwenye terminal yako. Itaweka moja kwa moja vifurushi vinavyohitajika vilivyoainishwa kwenye faili `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Kutumia Poetry (kutoka pyproject.toml)

1. Kama unatumia Poetry, andika amri ifuatayo kwenye terminal yako. Itaweka moja kwa moja vifurushi vinavyohitajika vilivyoainishwa kwenye faili `pyproject.toml`:

    ```bash
    poetry install
    ```

---

**Kanusho**:
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo rasmi. Kwa taarifa muhimu, inashauriwa kutumia huduma ya mtaalamu wa kutafsiri binadamu. Hatutawajibika kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.