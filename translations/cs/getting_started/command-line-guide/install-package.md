<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:52:33+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "cs"
}
-->
# Instalace balíčku Co-op Translator

**Co-op Translator** je nástroj pro příkazovou řádku (CLI), který vám pomůže přeložit všechny markdown soubory a obrázky ve vašem projektu do více jazyků. Tento návod vás provede nastavením překladače a jeho spuštěním pro různé případy použití.

### Vytvoření virtuálního prostředí

Virtuální prostředí můžete vytvořit pomocí `pip` nebo `Poetry`. Zadejte jeden z následujících příkazů do svého terminálu.

#### Pomocí pip

```bash
python -m venv .venv
```

#### Pomocí Poetry

```bash
poetry init
```

### Aktivace virtuálního prostředí

Po vytvoření virtuálního prostředí je potřeba ho aktivovat. Postup se liší podle vašeho operačního systému. Zadejte následující příkaz do svého terminálu.

#### Pro pip i Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Pomocí Poetry

1. Pokud jste prostředí vytvořili pomocí Poetry, zadejte do terminálu následující příkaz pro jeho aktivaci.

    ```bash
    poetry shell
    ```

### Instalace balíčku a potřebných závislostí

Jakmile máte virtuální prostředí připravené a aktivované, dalším krokem je instalace potřebných závislostí.

### Rychlá instalace

Nainstalujte Co-Op Translator pomocí pip

```
pip install co-op-translator
```
Nebo 

Nainstalujte pomocí poetry
```
poetry add co-op-translator
```

#### Pomocí pip (ze souboru requirements.txt), pokud klonujete toto repo

> [!NOTE]
> Toto prosím NEDĚLEJTE, pokud instalujete co-op translator pomocí rychlé instalace.

1. Pokud používáte pip, zadejte do terminálu následující příkaz. Automaticky nainstaluje požadované balíčky uvedené v souboru `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Pomocí Poetry (ze souboru pyproject.toml)

1. Pokud používáte Poetry, zadejte do terminálu následující příkaz. Automaticky nainstaluje požadované balíčky uvedené v souboru `pyproject.toml`:

    ```bash
    poetry install
    ```

---

**Prohlášení**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho rodném jazyce. Pro kritické informace doporučujeme profesionální lidský překlad. Nenese odpovědnost za jakékoli nedorozumění nebo nesprávné výklady vzniklé v důsledku použití tohoto překladu.