<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:37:16+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "sk"
}
-->
# Inštalácia balíka Co-op translator

**Co-op Translator** je nástroj s príkazovým riadkom (CLI), ktorý vám pomôže preložiť všetky markdown súbory a obrázky vo vašom projekte do viacerých jazykov. Tento návod vás prevedie konfiguráciou prekladača a jeho spustením pre rôzne prípady použitia.

### Vytvorenie virtuálneho prostredia

Virtuálne prostredie môžete vytvoriť pomocou `pip` alebo `Poetry`. Zadajte jeden z nasledujúcich príkazov v termináli.

#### Použitie pip

```bash
python -m venv .venv
```

#### Použitie Poetry

```bash
poetry init
```

### Aktivácia virtuálneho prostredia

Po vytvorení virtuálneho prostredia ho musíte aktivovať. Postup sa líši podľa operačného systému. Zadajte nasledujúci príkaz v termináli.

#### Pre pip aj Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Použitie Poetry

1. Ak ste prostredie vytvorili pomocou Poetry, zadajte v termináli nasledujúci príkaz na jeho aktiváciu.

    ```bash
    poetry shell
    ```

### Inštalácia balíka a potrebných závislostí

Keď máte virtuálne prostredie nastavené a aktivované, ďalším krokom je inštalácia potrebných závislostí.

### Rýchla inštalácia

Nainštalujte Co-Op Translator cez pip

```
pip install co-op-translator
```
Alebo

Nainštalujte cez Poetry
```
poetry add co-op-translator
```

#### Použitie pip (z requirements.txt), ak ste naklonovali tento repozitár

![NOTE] Prosím, nerobte to, ak inštalujete co-op translator cez rýchlu inštaláciu.

1. Ak používate pip, zadajte v termináli nasledujúci príkaz. Automaticky nainštaluje potrebné balíky uvedené v súbore `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Použitie Poetry (z pyproject.toml)

1. Ak používate Poetry, zadajte v termináli nasledujúci príkaz. Automaticky nainštaluje potrebné balíky uvedené v súbore `pyproject.toml`:

    ```bash
    poetry install
    ```

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.