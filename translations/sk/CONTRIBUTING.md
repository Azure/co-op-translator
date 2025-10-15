<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T03:53:38+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sk"
}
-->
# Prispievanie do Co-op Translator

Tento projekt víta príspevky a návrhy. Väčšina príspevkov vyžaduje, aby ste súhlasili s Contributor License Agreement (CLA), čím potvrdíte, že máte právo a skutočne udeľujete práva na použitie vášho príspevku. Viac informácií nájdete na https://cla.opensource.microsoft.com.

Keď odošlete pull request, CLA bot automaticky zistí, či musíte poskytnúť CLA, a podľa toho označí PR (napr. status check, komentár). Stačí postupovať podľa pokynov bota. Tento proces stačí absolvovať len raz pre všetky repozitáre využívajúce našu CLA.

## Nastavenie vývojového prostredia

Na nastavenie vývojového prostredia pre tento projekt odporúčame používať Poetry na správu závislostí. Závislosti projektu spravujeme cez `pyproject.toml`, preto na ich inštaláciu používajte Poetry.

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

### Inštalácia balíka a potrebných balíkov

#### Pomocou Poetry (z pyproject.toml)

```bash
poetry install
```

### Manuálne testovanie

Pred odoslaním PR je dôležité otestovať funkčnosť prekladu na reálnej dokumentácii:

1. V koreňovom adresári vytvorte testovací adresár:
    ```bash
    mkdir test_docs
    ```

2. Skopírujte do testovacieho adresára nejakú markdown dokumentáciu a obrázky, ktoré chcete preložiť. Napríklad:
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
   - Správnosť komentárov s metadátami
   - Zachovanie pôvodnej štruktúry markdownu
   - Funkčnosť odkazov a obrázkov

Toto manuálne testovanie pomáha zabezpečiť, že vaše zmeny fungujú aj v reálnych podmienkach.

### Premenné prostredia

1. V koreňovom adresári vytvorte súbor `.env` skopírovaním poskytnutého súboru `.env.template`.
1. Vyplňte premenné prostredia podľa pokynov.

> [!TIP]
>
> ### Ďalšie možnosti vývojového prostredia
>
> Okrem lokálneho spustenia projektu môžete využiť aj GitHub Codespaces alebo VS Code Dev Containers ako alternatívne vývojové prostredie.
>
> #### GitHub Codespaces
>
> Ukážky môžete spustiť virtuálne pomocou GitHub Codespaces bez ďalších nastavení.
>
> Tlačidlo otvorí webovú verziu VS Code vo vašom prehliadači:
>
> 1. Otvorte šablónu (môže to trvať niekoľko minút):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### Lokálne spustenie cez VS Code Dev Containers
>
> ⚠️ Táto možnosť funguje len ak máte v Docker Desktop pridelených aspoň 16 GB RAM. Ak máte menej, skúste [GitHub Codespaces](../..) alebo [nastavte lokálne](../..).
>
> Alternatívou sú VS Code Dev Containers, ktoré otvoria projekt vo vašom lokálnom VS Code pomocou [Dev Containers rozšírenia](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Spustite Docker Desktop (nainštalujte, ak ešte nemáte)
> 2. Otvorte projekt:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### Štýl kódu

Používame [Black](https://github.com/psf/black) ako formátovač Python kódu, aby sme udržali jednotný štýl v celom projekte. Black je nekompromisný formátovač, ktorý automaticky upravuje Python kód podľa svojich pravidiel.

#### Konfigurácia

Konfigurácia Black je uvedená v našom `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Inštalácia Black

Black môžete nainštalovať buď cez Poetry (odporúčané) alebo pip:

##### Pomocou Poetry

Black sa nainštaluje automaticky pri nastavovaní vývojového prostredia:
```bash
poetry install
```

##### Pomocou pip

Ak používate pip, Black nainštalujete priamo:
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
> Odporúčame nastaviť editor tak, aby automaticky formátoval kód pomocou Black pri ukladaní. Väčšina moderných editorov to podporuje cez rozšírenia alebo pluginy.

## Spustenie Co-op Translator

Na spustenie Co-op Translator pomocou Poetry vo vašom prostredí postupujte takto:

1. Prejdite do adresára, kde chcete vykonávať prekladové testy, alebo si vytvorte dočasný priečinok na testovanie.

2. Spustite nasledujúci príkaz. Nahraďte `-l ko` kódom jazyka, do ktorého chcete prekladať. Prepínač `-d` aktivuje debug mód.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Pred spustením príkazu sa uistite, že máte aktivované Poetry prostredie (poetry shell).

## Pridanie nového jazyka

Radi privítame príspevky, ktoré pridávajú podporu pre nové jazyky. Pred otvorením PR prosím splňte nasledujúce kroky, aby bola kontrola plynulá.

1. Pridajte jazyk do mapovania fontov
   - Upraviť `src/co_op_translator/fonts/font_language_mappings.yml`
   - Pridať položku s:
     - `code`: ISO-like kód jazyka (napr. `vi`)
     - `name`: Zrozumiteľný názov jazyka
     - `font`: Font dostupný v `src/co_op_translator/fonts/`, ktorý podporuje dané písmo
     - `rtl`: `true` ak je jazyk písaný sprava doľava, inak `false`

2. Pridajte potrebné fonty (ak treba)
   - Ak je potrebný nový font, overte licenčnú kompatibilitu pre open source distribúciu
   - Pridajte font do `src/co_op_translator/fonts/`

3. Lokálne overenie
   - Spustite preklad na malej vzorke (Markdown, obrázky, notebooky podľa potreby)
   - Overte, že výstup sa správne zobrazuje, vrátane fontov a prípadného RTL rozloženia

4. Aktualizujte dokumentáciu
   - Uistite sa, že jazyk je uvedený v `getting_started/supported-languages.md`
   - Nie je potrebné meniť `README_languages_template.md`; generuje sa zo zoznamu podporovaných jazykov

5. Otvorte PR
   - Popíšte pridaný jazyk a prípadné font/licenčné otázky
   - Priložte screenshoty zobrazených výstupov, ak je to možné

Príklad YAML položky:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Správcovia

### Formát správy o commite a stratégia zlúčenia

Aby sme udržali konzistentnú a prehľadnú históriu commitov, používame špecifický formát správy o commite **pre finálnu správu** pri použití stratégie **Squash and Merge**.

Pri zlúčení pull requestu (PR) sa jednotlivé commity spoja do jedného. Finálna správa o commite by mala nasledovať formát nižšie, aby bola história čistá a jednotná.

#### Formát správy o commite (pre squash and merge)

Používame nasledujúci formát:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Určuje kategóriu commitu. Používame tieto typy:
  - `Docs`: Aktualizácie dokumentácie.
  - `Build`: Zmeny týkajúce sa build systému alebo závislostí, vrátane úprav konfiguračných súborov, CI workflow alebo Dockerfile.
  - `Core`: Úpravy hlavnej funkcionality projektu, najmä súborov v `src/co_op_translator/core`.

- **description**: Stručné zhrnutie zmeny.
- **PR number**: Číslo pull requestu, s ktorým commit súvisí.

**Príklady**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Prefixy **`Docs`**, **`Core`** a **`Build`** sa aktuálne automaticky pridávajú do názvu PR podľa priradených štítkov k upravenému zdrojovému kódu. Ak je správny štítok priradený, zvyčajne netreba názov PR manuálne upravovať. Stačí overiť, že je všetko správne a prefix bol vygenerovaný správne.

#### Stratégia zlúčenia

Používame **Squash and Merge** ako predvolenú stratégiu pre pull requesty. Táto stratégia zabezpečuje, že správy o commite budú podľa nášho formátu, aj keď jednotlivé commity nie sú.

**Dôvody**:

- Čistá, lineárna história projektu.
- Konzistentné správy o commite.
- Menej zbytočných commitov (napr. "fix typo").

Pri zlúčení sa uistite, že finálna správa o commite je podľa vyššie uvedeného formátu.

**Príklad Squash and Merge**
Ak PR obsahuje tieto commity:

- `fix typo`
- `update README`
- `adjust formatting`

Mali by byť zlúčené do:
`Docs: Improve documentation clarity and formatting (#65)`

---

**Vyhlásenie o vylúčení zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladovej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Za autoritatívny zdroj sa považuje pôvodný dokument v jeho pôvodnom jazyku. Pre kritické informácie odporúčame profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vzniknuté použitím tohto prekladu.