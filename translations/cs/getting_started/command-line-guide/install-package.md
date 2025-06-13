<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:37:07+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "cs"
}
-->
# Instalace balíčku Co-op translator

**Co-op Translator** je nástroj příkazového řádku (CLI), který vám pomůže přeložit všechny markdown soubory a obrázky ve vašem projektu do více jazyků. Tento návod vás provede nastavením překladače a jeho spuštěním pro různé scénáře použití.

### Vytvoření virtuálního prostředí

Virtuální prostředí můžete vytvořit pomocí `pip` nebo `Poetry`. Zadejte jeden z následujících příkazů do terminálu.

#### Použití pip

```bash
python -m venv .venv
```

#### Použití Poetry

```bash
poetry init
```

### Aktivace virtuálního prostředí

Po vytvoření virtuálního prostředí je potřeba ho aktivovat. Postup se liší podle operačního systému. Zadejte následující příkaz do terminálu.

#### Pro pip i Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Použití Poetry

1. Pokud jste prostředí vytvořili pomocí Poetry, aktivujte ho tímto příkazem v terminálu.

    ```bash
    poetry shell
    ```

### Instalace balíčku a požadovaných knihoven

Jakmile máte virtuální prostředí nastavené a aktivované, dalším krokem je instalace potřebných závislostí.

### Rychlá instalace

Instalace Co-Op Translator přes pip

```
pip install co-op-translator
```  
Nebo

Instalace přes Poetry  
```
poetry add co-op-translator
```

#### Použití pip (z requirements.txt), pokud klonujete tento repozitář

![NOTE] Pokud instalujete co-op translator přes rychlou instalaci, tuto metodu NEPOUŽÍVEJTE.

1. Pokud používáte pip, zadejte do terminálu následující příkaz. Automaticky se nainstalují všechny požadované balíčky uvedené v souboru `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Použití Poetry (z pyproject.toml)

1. Pokud používáte Poetry, zadejte do terminálu následující příkaz. Automaticky se nainstalují všechny požadované balíčky uvedené v souboru `pyproject.toml`:

    ```bash
    poetry install
    ```

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje využít profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.