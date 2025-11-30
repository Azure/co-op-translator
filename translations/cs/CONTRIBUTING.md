<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T03:50:45+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "cs"
}
-->
# Přispívání do Co-op Translator

Tento projekt vítá příspěvky a návrhy. Většina příspěvků vyžaduje, abyste souhlasili s Contributor License Agreement (CLA), kde prohlašujete, že máte právo nám poskytnout práva k použití vašeho příspěvku. Podrobnosti najdete na https://cla.opensource.microsoft.com.

Když odešlete pull request, CLA bot automaticky zjistí, zda musíte poskytnout CLA, a podle toho označí PR (např. status check, komentář). Stačí postupovat podle pokynů bota. Toto stačí udělat jen jednou pro všechny repozitáře využívající naši CLA.

## Nastavení vývojového prostředí

Pro nastavení vývojového prostředí tohoto projektu doporučujeme používat Poetry pro správu závislostí. Závislosti projektu spravujeme pomocí `pyproject.toml`, proto byste měli používat Poetry pro jejich instalaci.

### Vytvoření virtuálního prostředí

#### Pomocí pip

```bash
python -m venv .venv
```

#### Pomocí Poetry

```bash
poetry init
```

### Aktivace virtuálního prostředí

#### Pro pip i Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Pomocí Poetry

```bash
poetry shell
```

### Instalace balíčku a potřebných balíčků

#### Pomocí Poetry (z pyproject.toml)

```bash
poetry install
```

### Manuální testování

Před odesláním PR je důležité otestovat překladovou funkci na skutečné dokumentaci:

1. V kořenovém adresáři vytvořte testovací složku:
    ```bash
    mkdir test_docs
    ```

2. Zkopírujte do testovací složky nějakou markdown dokumentaci a obrázky, které chcete překládat. Například:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Nainstalujte balíček lokálně:
    ```bash
    pip install -e .
    ```

4. Spusťte Co-op Translator na vašich testovacích dokumentech:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Zkontrolujte přeložené soubory v `test_docs/translations` a `test_docs/translated_images` a ověřte:
   - Kvalitu překladu
   - Správnost metadat v komentářích
   - Zachování původní struktury markdownu
   - Funkčnost odkazů a obrázků

Toto manuální testování pomáhá zajistit, že vaše změny fungují dobře v reálných situacích.

### Proměnné prostředí

1. V kořenovém adresáři vytvořte soubor `.env` zkopírováním poskytnutého souboru `.env.template`.
1. Vyplňte proměnné prostředí podle pokynů.

> [!TIP]
>
> ### Další možnosti vývojového prostředí
>
> Kromě lokálního spuštění projektu můžete využít také GitHub Codespaces nebo VS Code Dev Containers jako alternativní vývojové prostředí.
>
> #### GitHub Codespaces
>
> Ukázky můžete spustit virtuálně pomocí GitHub Codespaces bez dalších nastavení.
>
> Tlačítko otevře webovou verzi VS Code ve vašem prohlížeči:
>
> 1. Otevřete šablonu (může to trvat několik minut):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### Lokální spuštění pomocí VS Code Dev Containers
>
> ⚠️ Tato možnost funguje pouze, pokud máte v Docker Desktopu přiděleno alespoň 16 GB RAM. Pokud máte méně než 16 GB RAM, zkuste [možnost GitHub Codespaces](../..) nebo [nastavte lokálně](../..).
>
> Další možností jsou VS Code Dev Containers, které otevřou projekt ve vašem lokálním VS Code pomocí [rozšíření Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Spusťte Docker Desktop (nainstalujte, pokud ještě nemáte)
> 2. Otevřete projekt:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### Styl kódu

Používáme [Black](https://github.com/psf/black) jako formátovač Python kódu pro udržení jednotného stylu v celém projektu. Black je nekompromisní formátovač, který automaticky upravuje Python kód podle stylu Black.

#### Konfigurace

Konfigurace Black je uvedena v našem `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Instalace Black

Black můžete nainstalovat buď pomocí Poetry (doporučeno), nebo pip:

##### Pomocí Poetry

Black se nainstaluje automaticky při nastavení vývojového prostředí:
```bash
poetry install
```

##### Pomocí pip

Pokud používáte pip, můžete Black nainstalovat přímo:
```bash
pip install black
```

#### Použití Black

##### S Poetry

1. Naformátujte všechny Python soubory v projektu:
    ```bash
    poetry run black .
    ```

2. Naformátujte konkrétní soubor nebo složku:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### S pip

1. Naformátujte všechny Python soubory v projektu:
    ```bash
    black .
    ```

2. Naformátujte konkrétní soubor nebo složku:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Doporučujeme nastavit editor tak, aby automaticky formátoval kód pomocí Black při ukládání. Většina moderních editorů to podporuje pomocí rozšíření nebo pluginů.

## Spuštění Co-op Translator

Pro spuštění Co-op Translator pomocí Poetry ve vašem prostředí postupujte takto:

1. Přejděte do složky, kde chcete provádět překladové testy, nebo si vytvořte dočasnou složku pro testování.

2. Spusťte následující příkaz. Nahraďte `-l ko` kódem jazyka, do kterého chcete překládat. Přepínač `-d` aktivuje debug mód.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Před spuštěním příkazu se ujistěte, že máte aktivované prostředí Poetry (poetry shell).

## Přidání nového jazyka

Uvítáme příspěvky, které přidávají podporu nových jazyků. Před otevřením PR prosím dokončete níže uvedené kroky pro hladkou kontrolu.

1. Přidejte jazyk do mapování fontů
   - Upravte `src/co_op_translator/fonts/font_language_mappings.yml`
   - Přidejte položku s:
     - `code`: ISO-like kód jazyka (např. `vi`)
     - `name`: Srozumitelný název jazyka
     - `font`: Font dostupný v `src/co_op_translator/fonts/`, který podporuje dané písmo
     - `rtl`: `true` pokud je jazyk psán zprava doleva, jinak `false`

2. Přidejte potřebné fonty (pokud je třeba)
   - Pokud je potřeba nový font, ověřte kompatibilitu licence pro open source distribuci
   - Přidejte soubor fontu do `src/co_op_translator/fonts/`

3. Lokální ověření
   - Proveďte překlad na malém vzorku (Markdown, obrázky, případně notebooky)
   - Ověřte, že výstup se správně zobrazuje, včetně fontů a případného RTL rozložení

4. Aktualizujte dokumentaci
   - Ujistěte se, že jazyk je uveden v `getting_started/supported-languages.md`
   - Žádné změny v `README_languages_template.md` nejsou potřeba; generuje se ze seznamu podporovaných jazyků

5. Otevřete PR
   - Popište přidaný jazyk a případné font/licenční aspekty
   - Přiložte screenshoty vykreslených výstupů, pokud je to možné

Ukázka YAML položky:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Správci

### Formát zprávy o commitu a strategie slučování

Pro zajištění konzistence a přehlednosti v historii commitů projektu dodržujeme specifický formát zpráv o commitu **pro finální commit** při použití strategie **Squash and Merge**.

Když se pull request (PR) sloučí, jednotlivé commity se spojí do jednoho. Finální zpráva o commitu by měla dodržet níže uvedený formát pro čistou a jednotnou historii.

#### Formát zprávy o commitu (pro squash and merge)

Používáme následující formát zpráv o commitu:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Určuje kategorii commitu. Používáme tyto typy:
  - `Docs`: Pro aktualizace dokumentace.
  - `Build`: Pro změny týkající se build systému nebo závislostí, včetně aktualizací konfiguračních souborů, CI workflow nebo Dockerfile.
  - `Core`: Pro úpravy hlavní funkcionality projektu, zejména souborů ve složce `src/co_op_translator/core`.

- **description**: Stručné shrnutí změny.
- **PR number**: Číslo pull requestu spojeného s commitem.

**Příklady**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Prefixy **`Docs`**, **`Core`** a **`Build`** se aktuálně automaticky přidávají do názvů PR podle štítků aplikovaných na upravený zdrojový kód. Pokud je správný štítek aplikován, obvykle není potřeba název PR ručně upravovat. Stačí ověřit, že je vše správně a prefix byl vygenerován.

#### Strategie slučování

Používáme **Squash and Merge** jako výchozí strategii pro pull requesty. Tato strategie zajišťuje, že zprávy o commitu dodržují náš formát, i když jednotlivé commity ne.

**Důvody**:

- Čistá, lineární historie projektu.
- Konzistence zpráv o commitu.
- Méně rušivých drobných commitů (např. "fix typo").

Při slučování se ujistěte, že finální zpráva o commitu odpovídá výše popsanému formátu.

**Příklad Squash and Merge**
Pokud PR obsahuje následující commity:

- `fix typo`
- `update README`
- `adjust formatting`

Měly by být sloučeny do:
`Docs: Improve documentation clarity and formatting (#65)`

---

**Prohlášení**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho rodném jazyce. Pro kritické informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné výklady vzniklé v důsledku použití tohoto překladu.