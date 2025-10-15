<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:49:25+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "hu"
}
-->
# Telepítsd a Co-op Translator csomagot

A **Co-op Translator** egy parancssori eszköz (CLI), amely segít lefordítani a projekted összes markdown fájlját és képét több nyelvre. Ez az útmutató végigvezet a fordító beállításán és különböző felhasználási módokon.

### Hozz létre virtuális környezetet

Virtuális környezetet létrehozhatsz `pip` vagy `Poetry` segítségével. Írd be az alábbi parancsok egyikét a terminálodba.

#### Pip használata

```bash
python -m venv .venv
```

#### Poetry használata

```bash
poetry init
```

### A virtuális környezet aktiválása

Miután létrehoztad a virtuális környezetet, aktiválnod kell azt. A lépések eltérnek attól függően, hogy milyen operációs rendszert használsz. Írd be az alábbi parancsot a terminálodba.

#### Pip és Poetry esetén is

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry használata

1. Ha a környezetet Poetry-vel hoztad létre, írd be az alábbi parancsot a terminálodba az aktiváláshoz.

    ```bash
    poetry shell
    ```

### A csomag és szükséges csomagok telepítése

Miután a virtuális környezet elkészült és aktiváltad, a következő lépés a szükséges függőségek telepítése.

### Gyors telepítés

Telepítsd a Co-Op Translator-t pip segítségével

```
pip install co-op-translator
```
Vagy 

Telepítsd Poetry-vel
```
poetry add co-op-translator
```

#### Pip használata (requirements.txt-ből), ha klónozod ezt a repót

> [!NOTE]
> Ezt NE csináld, ha a Co-op Translator-t a gyors telepítéssel telepíted.

1. Ha pip-et használsz, írd be az alábbi parancsot a terminálodba. Ez automatikusan telepíti a szükséges csomagokat, amiket a `requirements.txt` fájlban megadtak:

    ```bash
    pip install -r requirements.txt
    ```

#### Poetry használata (pyproject.toml-ból)

1. Ha Poetry-t használsz, írd be az alábbi parancsot a terminálodba. Ez automatikusan telepíti a szükséges csomagokat, amiket a `pyproject.toml` fájlban megadtak:

    ```bash
    poetry install
    ```

---

**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasoljuk a professzionális, emberi fordítást. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.