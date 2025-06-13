<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:36:46+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "sw"
}
-->
# Sakinisha kifurushi cha Co-op translator

**Co-op Translator** ni zana ya kiolesura cha amri (CLI) iliyoundwa kusaidia kutafsiri faili zote za markdown na picha katika mradi wako kwa lugha nyingi. Mafunzo haya yatakuongoza jinsi ya kusanidi translator na kuiendesha kwa matumizi mbalimbali.

### Unda mazingira ya virtual

Unaweza kuunda mazingira ya virtual ukitumia ama `pip` au `Poetry`. Andika moja ya amri zifuatazo ndani ya terminal yako.

#### Kutumia pip

```bash
python -m venv .venv
```

#### Kutumia Poetry

```bash
poetry init
```

### Washa mazingira ya virtual

Baada ya kuunda mazingira ya virtual, utahitaji kuyawezesha. Hatua hutofautiana kulingana na mfumo wako wa uendeshaji. Andika amri ifuatayo ndani ya terminal yako.

#### Kwa pip na Poetry zote mbili

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Kutumia Poetry

1. Ikiwa umeunda mazingira na Poetry, andika amri ifuatayo ndani ya terminal yako kuyawezesha.

    ```bash
    poetry shell
    ```

### Kusakinisha Kifurushi na vifurushi vinavyohitajika

Mara mazingira yako ya virtual yatakapowekwa na kuyawezesha, hatua inayofuata ni kusakinisha utegemezi unaohitajika.

### Usakinishaji wa haraka

Sakinisha kupitia Co-Op Translator kwa pip

```
pip install co-op-translator
```
Au 

Sakinisha kupitia poetry
```
poetry add co-op-translator
```

#### Kutumia pip (kutoka requirements.txt) ikiwa unakopa repo hii

![NOTE] Tafadhali USIFANYE hivi ikiwa unasakinisha co-op translator kupitia usakinishaji wa haraka.

1. Ikiwa unatumia pip, andika amri ifuatayo ndani ya terminal yako. Itasakinisha moja kwa moja vifurushi vinavyohitajika vilivyoainishwa katika faili la `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Kutumia Poetry (kutoka pyproject.toml)

1. Ikiwa unatumia Poetry, andika amri ifuatayo ndani ya terminal yako. Itasakinisha moja kwa moja vifurushi vinavyohitajika vilivyoainishwa katika faili la `pyproject.toml`:

    ```bash
    poetry install
    ```

**Angalizo**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za moja kwa moja zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei wajibu wowote kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.