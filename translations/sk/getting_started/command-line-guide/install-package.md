<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:55:30+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "sk"
}
-->
# Inštalácia balíka Co-op Translator

**Co-op Translator** je nástroj príkazového riadku (CLI), ktorý vám pomôže preložiť všetky markdown súbory a obrázky vo vašom projekte do viacerých jazykov. Tento návod vás prevedie nastavením prekladača a jeho používaním v rôznych situáciách.

### Vytvorenie virtuálneho prostredia

Virtuálne prostredie môžete vytvoriť pomocou `pip` alebo `Poetry`. Zadajte jeden z nasledujúcich príkazov do svojho terminálu.

#### Pomocou pip

```bash
python -m venv .venv
```

#### Pomocou Poetry

```bash
poetry init
```

### Aktivácia virtuálneho prostredia

Po vytvorení virtuálneho prostredia ho musíte aktivovať. Postup sa líši podľa operačného systému. Zadajte nasledujúci príkaz do svojho terminálu.

#### Pre pip aj Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Pomocou Poetry

1. Ak ste prostredie vytvorili pomocou Poetry, zadajte nasledujúci príkaz do svojho terminálu na jeho aktiváciu.

    ```bash
    poetry shell
    ```

### Inštalácia balíka a potrebných závislostí

Keď máte virtuálne prostredie nastavené a aktivované, ďalším krokom je inštalácia potrebných závislostí.

### Rýchla inštalácia

Inštalujte Co-Op Translator cez pip

```
pip install co-op-translator
```
Alebo 

Inštalujte cez poetry
```
poetry add co-op-translator
```

#### Pomocou pip (zo súboru requirements.txt) ak ste klonovali tento repozitár 

> [!NOTE]
> Toto nerobte, ak ste nainštalovali co-op translator cez rýchlu inštaláciu.

1. Ak používate pip, zadajte nasledujúci príkaz do svojho terminálu. Automaticky nainštaluje požadované balíky uvedené v súbore `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Pomocou Poetry (zo súboru pyproject.toml)

1. Ak používate Poetry, zadajte nasledujúci príkaz do svojho terminálu. Automaticky nainštaluje požadované balíky uvedené v súbore `pyproject.toml`:

    ```bash
    poetry install
    ```

---

**Vyhlásenie o vylúčení zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladovej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Za autoritatívny zdroj by sa mal považovať pôvodný dokument v jeho pôvodnom jazyku. Pre kritické informácie odporúčame profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vzniknuté použitím tohto prekladu.