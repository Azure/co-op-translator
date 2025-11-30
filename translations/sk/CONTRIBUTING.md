<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T12:12:23+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sk"
}
-->
# Prispievanie do Co-op Translator

Tento projekt vítá príspevky a návrhy. Väčšina príspevkov vyžaduje, aby ste súhlasili s Dohodou o licencii prispievateľa (CLA), ktorá potvrdzuje, že máte právo a skutočne nám udeľujete práva na použitie vášho príspevku. Pre podrobnosti navštívte https://cla.opensource.microsoft.com.

Keď odošlete pull request, bot CLA automaticky zistí, či je potrebné poskytnúť CLA, a príslušne označí PR (napr. kontrola stavu, komentár). Jednoducho postupujte podľa pokynov bota. Toto budete musieť urobiť iba raz pre všetky repozitáre používajúce našu CLA.

## Nastavenie vývojového prostredia

Pre nastavenie vývojového prostredia tohto projektu odporúčame používať Poetry na správu závislostí. Používame `pyproject.toml` na správu závislostí projektu, preto by ste mali na inštaláciu závislostí použiť Poetry.

### Vytvorenie virtuálneho prostredia

#### Pomocou pip

```bash
python -m venv .venv
```

#### Pomocou Poetry

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

#### Pomocou Poetry

```bash
poetry shell
```

### Inštalácia balíka a požadovaných balíkov

#### Pomocou Poetry (z pyproject.toml)

```bash
poetry install
```

### Manuálne testovanie

Pred odoslaním PR je dôležité otestovať funkčnosť prekladu na reálnej dokumentácii:

1. Vytvorte testovací adresár v koreňovom adresári:
    ```bash
    mkdir test_docs
    ```

2. Skopírujte nejakú markdown dokumentáciu a obrázky, ktoré chcete preložiť, do testovacieho adresára. Napríklad:
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

5. Skontrolujte preložené súbory v `test_docs/translations` a `test_docs/translated_images` a overte:
   - Kvalitu prekladu
   - Správnosť metadátových komentárov
   - Zachovanie pôvodnej štruktúry markdownu
   - Funkčnosť odkazov a obrázkov

Toto manuálne testovanie pomáha zabezpečiť, že vaše zmeny fungujú dobre v reálnych scenároch.

### Premenné prostredia

1. V koreňovom adresári vytvorte súbor `.env` skopírovaním poskytnutého súboru `.env.template`.
2. Vyplňte premenné prostredia podľa pokynov.

> [!TIP]
>
> ### Ďalšie možnosti nastavenia vývojového prostredia
>
> Okrem spustenia projektu lokálne môžete použiť aj GitHub Codespaces alebo VS Code Dev Containers ako alternatívne prostredie pre vývoj.
>
> #### GitHub Codespaces
>
> Tento príklad môžete spustiť virtuálne pomocou GitHub Codespaces bez potreby ďalších nastavení.
>
> Tlačidlo otvorí webovú inštanciu VS Code vo vašom prehliadači:
>
> 1. Otvorte šablónu (môže to trvať niekoľko minút):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Lokálne spustenie pomocou VS Code Dev Containers
>
> ⚠️ Táto možnosť funguje len ak má váš Docker Desktop pridelených aspoň 16 GB RAM. Ak máte menej ako 16 GB RAM, môžete skúsiť [GitHub Codespaces](../..) alebo [nastaviť prostredie lokálne](../..).
>
> Súvisiaca možnosť je VS Code Dev Containers, ktorý otvorí projekt vo vašom lokálnom VS Code pomocou [rozšírenia Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Spustite Docker Desktop (ak ho ešte nemáte, nainštalujte ho)
> 2. Otvorte projekt:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Štýl kódu

Používame [Black](https://github.com/psf/black) ako formátovač Python kódu, aby sme udržali jednotný štýl kódu v celom projekte. Black je nekompromisný formátovač, ktorý automaticky preformátuje Python kód podľa štýlu Black.

#### Konfigurácia

Konfigurácia Black je uvedená v našom `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Inštalácia Black

Black môžete nainštalovať buď pomocou Poetry (odporúčané), alebo pip:

##### Pomocou Poetry

Black sa automaticky nainštaluje pri nastavení vývojového prostredia:
```bash
poetry install
```

##### Pomocou pip

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

2. Spustite nasledujúci príkaz. Nahraďte `-l ko` kódom jazyka, do ktorého chcete prekladať. Prepínač `-d` znamená režim ladenia.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Pred spustením príkazu sa uistite, že máte aktivované prostredie Poetry (poetry shell).

## Pridanie nového jazyka

Vítame príspevky, ktoré pridávajú podporu nových jazykov. Pred otvorením PR prosím dokončite nasledujúce kroky, aby bol proces recenzie hladký.

1. Pridajte jazyk do mapovania fontov
   - Upravte `src/co_op_translator/fonts/font_language_mappings.yml`
   - Pridajte záznam s:
     - `code`: ISO-podobný kód jazyka (napr. `vi`)
     - `name`: Čitateľný názov jazyka
     - `font`: Font dodávaný v `src/co_op_translator/fonts/`, ktorý podporuje daný skript
     - `rtl`: `true`, ak je jazyk sprava doľava, inak `false`

2. Pridajte potrebné fonty (ak je to potrebné)
   - Ak je potrebný nový font, overte licenčnú kompatibilitu pre open source distribúciu
   - Pridajte fontový súbor do `src/co_op_translator/fonts/`

3. Lokálna kontrola
   - Spustite preklady na malom vzorku (Markdown, obrázky a notebooky podľa potreby)
   - Overte, že výstup sa správne zobrazuje vrátane fontov a prípadného RTL rozloženia

4. Aktualizujte dokumentáciu
   - Uistite sa, že jazyk je uvedený v `getting_started/supported-languages.md`
   - Zmeny v `getting_started/README_languages_template.md` nie sú potrebné; tento súbor sa generuje zo zoznamu podporovaných jazykov

5. Otvorte PR
   - Popíšte pridaný jazyk a prípadné licenčné alebo fontové poznámky
   - Priložte screenshoty zobrazených výstupov, ak je to možné

Príklad YAML záznamu:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Testovanie nového jazyka

Nový jazyk môžete otestovať spustením nasledujúceho príkazu:

```bash
# Vytvorte a aktivujte virtuálne prostredie
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Nainštalujte vývojový balík
pip install -e .
# Spustite preklad
translate -l "new_lang"
```

## Správcovia projektu

### Formát správy commitov a stratégia zlúčenia

Pre zabezpečenie konzistentnosti a prehľadnosti histórie commitov v projekte používame špecifický formát správy commitov **pre finálnu správu** pri použití stratégie **Squash and Merge**.

Keď sa pull request (PR) zlúči, jednotlivé commity sa spoja do jedného. Finálna správa commitu by mala mať nasledujúci formát, aby sme udržali čistú a konzistentnú históriu.

#### Formát správy commitov (pre squash and merge)

Používame nasledujúci formát správ commitov:

```bash
<type>: <description> (#<Číslo PR>)
```

- **type**: Určuje kategóriu commitu. Používame tieto typy:
  - `Docs`: Pre aktualizácie dokumentácie.
  - `Build`: Pre zmeny súvisiace so systémom zostavenia alebo závislosťami, vrátane aktualizácií konfiguračných súborov, CI workflow alebo Dockerfile.
  - `Core`: Pre úpravy jadra projektu alebo funkcií, najmä súbory v adresári `src/co_op_translator/core`.

- **description**: Stručný popis zmeny.
- **PR number**: Číslo pull requestu, ku ktorému sa commit viaže.

**Príklady**:

- `Docs: Aktualizácia inštrukcií na inštaláciu pre lepšiu zrozumiteľnosť (#50)`
- `Core: Vylepšenie spracovania prekladu obrázkov (#60)`

> [!NOTE]
> Momentálne sa prefixy **`Docs`**, **`Core`** a **`Build`** automaticky pridávajú k názvom PR na základe štítkov aplikovaných na upravený zdrojový kód. Pokiaľ je správny štítok priradený, zvyčajne nie je potrebné manuálne upravovať názov PR. Stačí overiť, že je všetko správne a prefix bol vygenerovaný.

#### Stratégia zlúčenia

Ako predvolenú stratégiu pre pull requesty používame **Squash and Merge**. Táto stratégia zabezpečuje, že správy commitov budú mať náš formát, aj keď jednotlivé commity nie.

**Dôvody**:

- Čistá, lineárna história projektu.
- Konzistentnosť správ commitov.
- Menej šumu z drobných commitov (napr. "oprava preklepu").

Pri zlúčení sa uistite, že finálna správa commitu dodržiava vyššie uvedený formát.

**Príklad Squash and Merge**
Ak PR obsahuje tieto commity:

- `oprava preklepu`
- `aktualizácia README`
- `úprava formátovania`

Mali by byť zlúčené do:
`Docs: Vylepšenie dokumentácie a formátovania (#65)`

### Proces vydávania verzie

Táto sekcia popisuje najjednoduchší spôsob, ako správcovia môžu publikovať novú verziu Co-op Translator.

#### 1. Zvýšenie verzie v `pyproject.toml`

1. Rozhodnite sa o ďalšom čísle verzie (používame semver: `MAJOR.MINOR.PATCH`).
2. Upravte `pyproject.toml` a aktualizujte pole `version` v sekcii `[tool.poetry]`.
3. Otvorte samostatný pull request, ktorý mení iba verziu (a prípadné automaticky aktualizované lock/metadata súbory).
4. Po schválení použite **Squash and Merge** a uistite sa, že finálna správa commitu dodržiava vyššie uvedený formát.

#### 2. Vytvorenie GitHub Release

1. Prejdite na stránku repozitára na GitHub a otvorte **Releases** → **Draft a new release**.
2. Vytvorte nový tag (napr. `v0.13.0`) z vetvy `main`.
3. Nastavte názov vydania na rovnakú verziu (napr. `v0.13.0`).
4. Kliknite na **Generate release notes** pre automatické vyplnenie changelogu.
5. Voliteľne upravte text (napr. zvýraznite novo podporované jazyky alebo dôležité zmeny).
6. Publikujte vydanie.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->