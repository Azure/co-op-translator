<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:36:57+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "hu"
}
-->
# Telepítsd a Co-op fordító csomagot

A **Co-op Translator** egy parancssori eszköz (CLI), amely segít lefordítani a projekted összes markdown fájlját és képét több nyelvre. Ez az útmutató végigvezet a fordító beállításán és különböző használati esetek futtatásán.

### Virtuális környezet létrehozása

Virtuális környezetet létrehozhatsz `pip` vagy `Poetry` használatával. Írd be a következő parancsok egyikét a terminálodba.

#### Pip használata

```bash
python -m venv .venv
```

#### Poetry használata

```bash
poetry init
```

### A virtuális környezet aktiválása

A virtuális környezet létrehozása után aktiválnod kell azt. A lépések az operációs rendszertől függően eltérnek. Írd be a következő parancsot a terminálodba.

#### Mind pip, mind Poetry esetén

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry használata

1. Ha Poetry-val hoztad létre a környezetet, írd be a következő parancsot a terminálba az aktiváláshoz.

    ```bash
    poetry shell
    ```

### A csomag és a szükséges csomagok telepítése

Miután a virtuális környezet be van állítva és aktiválva, a következő lépés a szükséges függőségek telepítése.

### Gyors telepítés

Telepítés Co-Op Translator segítségével pip-pel

```
pip install co-op-translator
```
Vagy

Telepítés Poetry-val
```
poetry add co-op-translator
```

#### Pip használata (requirements.txt alapján), ha klónozod ezt a repót

![NOTE] Kérjük, ezt NE tedd, ha a gyors telepítéssel telepíted a co-op fordítót.

1. Ha pip-et használsz, írd be a következő parancsot a terminálodba. Ez automatikusan telepíti a `requirements.txt` fájlban megadott szükséges csomagokat:

    ```bash
    pip install -r requirements.txt
    ```

#### Poetry használata (pyproject.toml alapján)

1. Ha Poetry-t használsz, írd be a következő parancsot a terminálodba. Ez automatikusan telepíti a `pyproject.toml` fájlban megadott szükséges csomagokat:

    ```bash
    poetry install
    ```

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget az ezen fordítás használatából eredő félreértésekért vagy félreértelmezésekért.