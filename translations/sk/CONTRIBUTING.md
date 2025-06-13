<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:42:15+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sk"
}
-->
# Prispievanie do Co-op Translator

Tento projekt víta príspevky a návrhy. Väčšina príspevkov vyžaduje, aby ste súhlasili s Contributor License Agreement (CLA), ktorý potvrdzuje, že máte právo a skutočne nám poskytujete práva na použitie vášho príspevku. Pre podrobnosti navštívte https://cla.opensource.microsoft.com.

Keď odošlete pull request, CLA bot automaticky zistí, či je potrebné poskytnúť CLA, a označí PR vhodne (napr. kontrola stavu, komentár). Jednoducho postupujte podľa pokynov bota. Toto budete musieť urobiť iba raz pre všetky repozitáre používajúce náš CLA.

## Nastavenie vývojového prostredia

Pre nastavenie vývojového prostredia tohto projektu odporúčame používať Poetry na správu závislostí. Používame `pyproject.toml` na správu závislostí projektu, a preto by ste mali na inštaláciu závislostí používať Poetry.

### Vytvorenie virtuálneho prostredia

#### Použitie pip

```bash
python -m venv .venv
```

#### Použitie Poetry

```bash
poetry init
```

### Aktivácia virtuálneho prostredia

#### Pre pip aj Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Použitie Poetry

```bash
poetry shell
```

### Inštalácia balíka a potrebných balíkov

#### Použitie Poetry (z pyproject.toml)

```bash
poetry install
```

### Manuálne testovanie

Pred odoslaním PR je dôležité otestovať funkčnosť prekladu na reálnej dokumentácii:

1. Vytvorte testovací adresár v koreňovom adresári:
    ```bash
    mkdir test_docs
    ```

2. Skopírujte niektorú markdown dokumentáciu a obrázky, ktoré chcete preložiť, do testovacieho adresára. Napríklad:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Nainštalujte balík lokálne:
    ```bash
    pip install -e .
    ```

4. Spustite Co-op Translator na vašich testovacích dokumentoch:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Skontrolujte preložené súbory v súbore `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`.
1. Vyplňte premenné prostredia podľa pokynov.

> [!TIP]
>
> ### Ďalšie možnosti nastavenia vývojového prostredia
>
> Okrem lokálneho spustenia projektu môžete použiť aj GitHub Codespaces alebo VS Code Dev Containers ako alternatívne nastavenie vývojového prostredia.
>
> #### GitHub Codespaces
>
> Tento príklad môžete spustiť virtuálne pomocou GitHub Codespaces bez nutnosti ďalších nastavení.
>
> Tlačidlo otvorí webovú VS Code inštanciu vo vašom prehliadači:
>
> 1. Otvorte šablónu (môže to trvať niekoľko minút):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Lokálne spustenie pomocou VS Code Dev Containers
>
> ⚠️ Táto možnosť funguje len ak má váš Docker Desktop pridelených aspoň 16 GB RAM. Ak máte menej ako 16 GB RAM, môžete skúsiť [GitHub Codespaces](../..) alebo [nastaviť to lokálne](../..).
>
> Súvisiaca možnosť sú VS Code Dev Containers, ktoré otvoria projekt vo vašom lokálnom VS Code pomocou [Dev Containers rozšírenia](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Spustite Docker Desktop (ak ho ešte nemáte, nainštalujte)
> 2. Otvorte projekt:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Štýl kódu

Používame [Black](https://github.com/psf/black) ako formátovač Python kódu, aby sme udržali jednotný štýl kódu v celom projekte. Black je nekompromisný formátovač kódu, ktorý automaticky preformátuje Python kód podľa štýlu Black.

#### Konfigurácia

Konfigurácia Black je definovaná v našom `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Inštalácia Black

Black môžete nainštalovať buď cez Poetry (odporúčané) alebo pip:

##### Použitie Poetry

Black sa automaticky nainštaluje pri nastavení vývojového prostredia:
```bash
poetry install
```

##### Použitie pip

Ak používate pip, môžete Black nainštalovať priamo:
```bash
pip install black
```

#### Použitie Black

##### S Poetry

1. Naformátujte všetky Python súbory v projekte:
    ```bash
    poetry run black .
    ```

2. Naformátujte konkrétny súbor alebo adresár:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### S pip

1. Naformátujte všetky Python súbory v projekte:
    ```bash
    black .
    ```

2. Naformátujte konkrétny súbor alebo adresár:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Odporúčame nastaviť si editor tak, aby automaticky formátoval kód pomocou Black pri ukladaní. Väčšina moderných editorov to podporuje cez rozšírenia alebo pluginy.

## Spustenie Co-op Translator

Ak chcete spustiť Co-op Translator pomocou Poetry vo vašom prostredí, postupujte podľa týchto krokov:

1. Prejdite do adresára, kde chcete vykonať testy prekladu, alebo si vytvorte dočasný priečinok na testovanie.

2. Spustite nasledujúci príkaz. Flag `-l ko` with the language code you wish to translate into. The `-d` znamená režim ladenia (debug).

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Uistite sa, že máte aktivované prostredie Poetry (poetry shell) pred spustením príkazu.

## Správcovia

### Formát správy o commite a stratégia zlúčenia

Pre zabezpečenie konzistentnosti a prehľadnosti histórie commitov v našom projekte používame špecifický formát správy o commite **pre finálnu správu commitu** pri použití stratégie **Squash and Merge**.

Keď sa pull request (PR) zlúči, jednotlivé commity sa spoja do jedného. Finálna správa o commite by mala mať nasledujúci formát, aby sa zachovala čistá a konzistentná história.

#### Formát správy o commite (pre squash and merge)

Používame nasledujúci formát správ o commitoch:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Určuje kategóriu commitu. Používame tieto typy:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `fix typo`
- `update README`
- `adjust formatting`

They should be squashed into:
`Docs: Improve documentation clarity and formatting (#65)`

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.