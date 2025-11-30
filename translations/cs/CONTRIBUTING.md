<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T12:08:07+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "cs"
}
-->
# Přispívání do Co-op Translator

Tento projekt vítá příspěvky a návrhy. Většina příspěvků vyžaduje, abyste souhlasili s licenční smlouvou přispěvatele (Contributor License Agreement, CLA), která potvrzuje, že máte právo a skutečně nám udělujete práva k použití vašeho příspěvku. Podrobnosti najdete na https://cla.opensource.microsoft.com.

Když odešlete pull request, bot CLA automaticky zjistí, zda je potřeba poskytnout CLA, a příslušně označí PR (např. kontrola stavu, komentář). Stačí postupovat podle pokynů bota. Toto je potřeba udělat pouze jednou pro všechny repozitáře používající naši CLA.

## Nastavení vývojového prostředí

Pro nastavení vývojového prostředí tohoto projektu doporučujeme používat Poetry pro správu závislostí. Používáme `pyproject.toml` pro správu závislostí projektu, proto byste měli k instalaci závislostí použít Poetry.

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

### Instalace balíčku a požadovaných balíčků

#### Pomocí Poetry (z pyproject.toml)

```bash
poetry install
```

### Manuální testování

Před odesláním PR je důležité otestovat funkčnost překladu na reálné dokumentaci:

1. Vytvořte testovací adresář v kořenovém adresáři:
    ```bash
    mkdir test_docs
    ```

2. Zkopírujte do testovacího adresáře nějakou markdown dokumentaci a obrázky, které chcete přeložit. Například:
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
   - Správnost metadatových komentářů
   - Zachování původní struktury markdownu
   - Funkčnost odkazů a obrázků

Toto manuální testování pomáhá zajistit, že vaše změny fungují dobře v reálných scénářích.

### Proměnné prostředí

1. Vytvořte soubor `.env` v kořenovém adresáři zkopírováním poskytnutého souboru `.env.template`.
1. Vyplňte proměnné prostředí podle pokynů.

> [!TIP]
>
> ### Další možnosti vývojového prostředí
>
> Kromě lokálního spuštění projektu můžete také využít GitHub Codespaces nebo VS Code Dev Containers jako alternativní nastavení vývojového prostředí.
>
> #### GitHub Codespaces
>
> Tento vzorek můžete spustit virtuálně pomocí GitHub Codespaces bez nutnosti dalších nastavení.
>
> Tlačítko otevře webovou instanci VS Code ve vašem prohlížeči:
>
> 1. Otevřete šablonu (může to trvat několik minut):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Lokální spuštění pomocí VS Code Dev Containers
>
> ⚠️ Tato možnost funguje pouze, pokud má váš Docker Desktop přiděleno alespoň 16 GB RAM. Pokud máte méně než 16 GB RAM, můžete zkusit [GitHub Codespaces](../..) nebo [nastavit prostředí lokálně](../..).
>
> Související možností jsou VS Code Dev Containers, které otevřou projekt ve vašem lokálním VS Code pomocí [rozšíření Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Spusťte Docker Desktop (pokud není nainstalován, nainstalujte ho)
> 2. Otevřete projekt:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Styl kódu

Používáme [Black](https://github.com/psf/black) jako formátovač Python kódu, abychom udrželi konzistentní styl kódu v celém projektu. Black je nekompromisní formátovač, který automaticky přeformátuje Python kód podle stylu Black.

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

Black se automaticky nainstaluje při nastavení vývojového prostředí:
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

2. Naformátujte konkrétní soubor nebo adresář:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### S pip

1. Naformátujte všechny Python soubory v projektu:
    ```bash
    black .
    ```

2. Naformátujte konkrétní soubor nebo adresář:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Doporučujeme nastavit editor tak, aby automaticky formátoval kód pomocí Black při ukládání. Většina moderních editorů toto podporuje přes rozšíření nebo pluginy.

## Spuštění Co-op Translator

Pro spuštění Co-op Translator pomocí Poetry ve vašem prostředí postupujte takto:

1. Přejděte do adresáře, kde chcete provádět testy překladu, nebo si vytvořte dočasnou složku pro testování.

2. Spusťte následující příkaz. Nahraďte `-l ko` kódem jazyka, do kterého chcete překládat. Přepínač `-d` znamená režim ladění.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Před spuštěním příkazu se ujistěte, že máte aktivované prostředí Poetry (poetry shell).

## Přispění nového jazyka

Vítáme příspěvky, které přidávají podporu nových jazyků. Před otevřením PR prosím dokončete následující kroky, aby byl proces revize hladký.

1. Přidejte jazyk do mapování fontů
   - Upravte `src/co_op_translator/fonts/font_language_mappings.yml`
   - Přidejte položku s:
     - `code`: ISO-podobný kód jazyka (např. `vi`)
     - `name`: Čitelný název jazyka
     - `font`: Font dodávaný v `src/co_op_translator/fonts/`, který podporuje daný skript
     - `rtl`: `true`, pokud je jazyk psán zprava doleva, jinak `false`

2. Přidejte potřebné fontové soubory (pokud je to nutné)
   - Pokud je potřeba nový font, ověřte kompatibilitu licence pro open source distribuci
   - Přidejte fontový soubor do `src/co_op_translator/fonts/`

3. Lokální ověření
   - Proveďte překlady na malém vzorku (Markdown, obrázky a notebooky podle potřeby)
   - Ověřte, že výstup se správně zobrazuje, včetně fontů a případného RTL rozložení

4. Aktualizujte dokumentaci
   - Ujistěte se, že jazyk je uveden v `getting_started/supported-languages.md`
   - Není potřeba měnit `getting_started/README_languages_template.md`, ten se generuje ze seznamu podporovaných jazyků

5. Otevřete PR
   - Popište přidaný jazyk a případné poznámky k fontům/licencím
   - Přiložte screenshoty vykreslených výstupů, pokud je to možné

Příklad položky v YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Testování nového jazyka

Nový jazyk můžete otestovat spuštěním následujícího příkazu:

```bash
# Vytvořte a aktivujte virtuální prostředí
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Nainstalujte vývojový balíček
pip install -e .
# Spusťte překlad
translate -l "new_lang"
```

## Správci projektu

### Formát zprávy commitu a strategie slučování

Pro zajištění konzistence a přehlednosti historie commitu v našem projektu používáme specifický formát zprávy commitu **pro finální zprávu commitu** při použití strategie **Squash and Merge**.

Když je pull request (PR) sloučen, jednotlivé commity se sloučí do jednoho. Finální zpráva commitu by měla mít následující formát, aby byla historie čistá a konzistentní.

#### Formát zprávy commitu (pro squash and merge)

Používáme tento formát zpráv commitu:

```bash
<type>: <description> (#<Číslo PR>)
```

- **type**: Určuje kategorii commitu. Používáme tyto typy:
  - `Docs`: Pro aktualizace dokumentace.
  - `Build`: Pro změny související se sestavovacím systémem nebo závislostmi, včetně aktualizací konfiguračních souborů, CI workflow nebo Dockerfile.
  - `Core`: Pro úpravy jádra projektu nebo funkcí, zejména soubory v adresáři `src/co_op_translator/core`.

- **description**: Stručný popis změny.
- **PR number**: Číslo pull requestu, ke kterému commit patří.

**Příklady**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Aktuálně jsou prefixy **`Docs`**, **`Core`** a **`Build`** automaticky přidávány k názvům PR na základě štítků aplikovaných na upravený zdrojový kód. Pokud je správný štítek aplikován, obvykle není potřeba ručně upravovat název PR. Stačí ověřit, že je vše správně a prefix byl vygenerován.

#### Strategie slučování

Jako výchozí strategii slučování pull requestů používáme **Squash and Merge**. Tato strategie zajistí, že zprávy commitů budou odpovídat našemu formátu, i když jednotlivé commity ne.

**Důvody**:

- Čistá, lineární historie projektu.
- Konzistence ve zprávách commitů.
- Méně šumu z drobných commitů (např. "fix typo").

Při slučování se ujistěte, že finální zpráva commitu odpovídá výše popsanému formátu.

**Příklad Squash and Merge**
Pokud PR obsahuje tyto commity:

- `fix typo`
- `update README`
- `adjust formatting`

měly by být sloučeny do:
`Docs: Improve documentation clarity and formatting (#65)`

### Proces vydání

Tato sekce popisuje nejjednodušší způsob, jak správci projektu mohou vydat novou verzi Co-op Translator.

#### 1. Zvýšení verze v `pyproject.toml`

1. Rozhodněte o dalším čísle verze (dodržujeme semver: `MAJOR.MINOR.PATCH`).
2. Upravte `pyproject.toml` a aktualizujte pole `version` v sekci `[tool.poetry]`.
3. Otevřete samostatný pull request, který mění pouze verzi (a případné automaticky aktualizované lock/metadata soubory).
4. Po schválení použijte **Squash and Merge** a ujistěte se, že finální zpráva commitu odpovídá výše popsanému formátu.

#### 2. Vytvoření GitHub Release

1. Přejděte na stránku repozitáře na GitHubu a otevřete **Releases** → **Draft a new release**.
2. Vytvořte nový tag (např. `v0.13.0`) z větve `main`.
3. Nastavte název vydání na stejnou verzi (např. `v0.13.0`).
4. Klikněte na **Generate release notes** pro automatické vyplnění changelogu.
5. Volitelně upravte text (např. zdůrazněte nově podporované jazyky nebo důležité změny).
6. Publikujte vydání.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->