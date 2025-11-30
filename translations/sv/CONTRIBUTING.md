<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T11:19:49+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sv"
}
-->
# Bidra till Co-op Translator

Det här projektet välkomnar bidrag och förslag. De flesta bidrag kräver att du godkänner ett Contributor License Agreement (CLA) som intygar att du har rätt att, och faktiskt gör det, ge oss rättigheter att använda ditt bidrag. För detaljer, besök https://cla.opensource.microsoft.com.

När du skickar in en pull request kommer en CLA-bot automatiskt avgöra om du behöver tillhandahålla en CLA och märka PR:n på lämpligt sätt (t.ex. statuskontroll, kommentar). Följ bara instruktionerna från boten. Du behöver bara göra detta en gång för alla repos som använder vår CLA.

## Uppställning av utvecklingsmiljö

För att sätta upp utvecklingsmiljön för detta projekt rekommenderar vi att använda Poetry för hantering av beroenden. Vi använder `pyproject.toml` för att hantera projektets beroenden, och därför bör du använda Poetry för att installera beroenden.

### Skapa en virtuell miljö

#### Med pip

```bash
python -m venv .venv
```

#### Med Poetry

```bash
poetry init
```

### Aktivera den virtuella miljön

#### För både pip och Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Med Poetry

```bash
poetry shell
```

### Installera paketet och nödvändiga paket

#### Med Poetry (från pyproject.toml)

```bash
poetry install
```

### Manuell testning

Innan du skickar in en PR är det viktigt att testa översättningsfunktionen med riktig dokumentation:

1. Skapa en testkatalog i rotkatalogen:
    ```bash
    mkdir test_docs
    ```

2. Kopiera några markdown-dokument och bilder du vill översätta till testkatalogen. Till exempel:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Installera paketet lokalt:
    ```bash
    pip install -e .
    ```

4. Kör Co-op Translator på dina testdokument:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Kontrollera de översatta filerna i `test_docs/translations` och `test_docs/translated_images` för att verifiera:
   - Översättningskvaliteten
   - Att metadata-kommentarerna är korrekta
   - Att den ursprungliga markdown-strukturen bevaras
   - Att länkar och bilder fungerar som de ska

Denna manuella testning hjälper till att säkerställa att dina ändringar fungerar bra i verkliga scenarier.

### Miljövariabler

1. Skapa en `.env`-fil i rotkatalogen genom att kopiera den medföljande `.env.template`-filen.
1. Fyll i miljövariablerna enligt instruktionerna.

> [!TIP]
>
> ### Ytterligare alternativ för utvecklingsmiljö
>
> Förutom att köra projektet lokalt kan du även använda GitHub Codespaces eller VS Code Dev Containers som alternativa utvecklingsmiljöer.
>
> #### GitHub Codespaces
>
> Du kan köra dessa exempel virtuellt med GitHub Codespaces utan några extra inställningar eller konfigurationer.
>
> Knappen öppnar en webbaserad VS Code-instans i din webbläsare:
>
> 1. Öppna mallen (det kan ta några minuter):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Köra lokalt med VS Code Dev Containers
>
> ⚠️ Detta alternativ fungerar endast om din Docker Desktop har tilldelats minst 16 GB RAM. Om du har mindre än 16 GB RAM kan du prova [GitHub Codespaces-alternativet](../..) eller [sätta upp det lokalt](../..).
>
> Ett relaterat alternativ är VS Code Dev Containers, som öppnar projektet i din lokala VS Code med hjälp av [Dev Containers-tillägget](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Starta Docker Desktop (installera det om det inte redan är installerat)
> 2. Öppna projektet:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Kodstil

Vi använder [Black](https://github.com/psf/black) som vår Python-kodformatterare för att upprätthålla en konsekvent kodstil i hela projektet. Black är en kompromisslös formatterare som automatiskt omformaterar Python-kod för att följa Blacks kodstil.

#### Konfiguration

Black-konfigurationen anges i vår `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installera Black

Du kan installera Black med antingen Poetry (rekommenderat) eller pip:

##### Med Poetry

Black installeras automatiskt när du sätter upp utvecklingsmiljön:
```bash
poetry install
```

##### Med pip

Om du använder pip kan du installera Black direkt:
```bash
pip install black
```

#### Använda Black

##### Med Poetry

1. Formatera alla Python-filer i projektet:
    ```bash
    poetry run black .
    ```

2. Formatera en specifik fil eller katalog:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Med pip

1. Formatera alla Python-filer i projektet:
    ```bash
    black .
    ```

2. Formatera en specifik fil eller katalog:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Vi rekommenderar att du ställer in din editor så att den automatiskt formaterar kod med Black vid sparande. De flesta moderna editors stödjer detta via tillägg eller plugins.

## Köra Co-op Translator

För att köra Co-op Translator med Poetry i din miljö, följ dessa steg:

1. Navigera till den katalog där du vill utföra översättningstester eller skapa en temporär mapp för teständamål.

2. Kör följande kommando. Byt ut `-l ko` mot språkkoden för det språk du vill översätta till. Flaggan `-d` anger debug-läge.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Se till att din Poetry-miljö är aktiverad (poetry shell) innan du kör kommandot.

## Bidra med ett nytt språk

Vi välkomnar bidrag som lägger till stöd för nya språk. Innan du öppnar en PR, vänligen genomför stegen nedan för att säkerställa en smidig granskning.

1. Lägg till språket i fontmappningen
   - Redigera `src/co_op_translator/fonts/font_language_mappings.yml`
   - Lägg till en post med:
     - `code`: ISO-liknande språkkod (t.ex. `vi`)
     - `name`: Ett användarvänligt visningsnamn
     - `font`: En font som levereras i `src/co_op_translator/fonts/` och som stödjer skriptet
     - `rtl`: `true` om språket skrivs höger-till-vänster, annars `false`

2. Inkludera nödvändiga fontfiler (om det behövs)
   - Om en ny font krävs, verifiera licenskompatibilitet för öppen källkodsdistribution
   - Lägg till fontfilen i `src/co_op_translator/fonts/`

3. Lokal verifiering
   - Kör översättningar för ett litet exempel (Markdown, bilder och notebooks efter behov)
   - Verifiera att utdata renderas korrekt, inklusive fonter och eventuellt RTL-layouter

4. Uppdatera dokumentationen
   - Säkerställ att språket finns med i `getting_started/supported-languages.md`
   - Inga ändringar behövs i `getting_started/README_languages_template.md`; den genereras från listan över stödjade språk

5. Öppna en PR
   - Beskriv det tillagda språket och eventuella font-/licensöverväganden
   - Bifoga skärmdumpar av renderade resultat om möjligt

Exempel på YAML-post:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Testa det nya språket

Du kan testa det nya språket genom att köra följande kommando:

```bash
# Skapa och aktivera en virtuell miljö
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Installera utvecklingspaketet
pip install -e .
# Kör översättningen
translate -l "new_lang"
```

## Underhållare

### Commit-meddelande och sammanslagningsstrategi

För att säkerställa konsekvens och tydlighet i projektets commit-historik följer vi ett specifikt format för commit-meddelanden **för det slutgiltiga commit-meddelandet** när vi använder **Squash and Merge**-strategin.

När en pull request (PR) slås ihop kommer de individuella commits att slås ihop till en enda commit. Det slutgiltiga commit-meddelandet ska följa formatet nedan för att bibehålla en ren och konsekvent historik.

#### Format för commit-meddelande (för squash and merge)

Vi använder följande format för commit-meddelanden:

```bash
<type>: <description> (#<PR-nummer>)
```

- **type**: Anger kategorin för commit. Vi använder följande typer:
  - `Docs`: För dokumentationsuppdateringar.
  - `Build`: För ändringar relaterade till byggsystem eller beroenden, inklusive uppdateringar av konfigurationsfiler, CI-flöden eller Dockerfile.
  - `Core`: För ändringar i projektets kärnfunktionalitet eller funktioner, särskilt de som involverar filer i `src/co_op_translator/core`-katalogen.

- **description**: En kortfattad sammanfattning av ändringen.
- **PR-nummer**: Numret på pull requesten som är kopplad till commiten.

**Exempel**:

- `Docs: Uppdatera installationsinstruktioner för tydlighet (#50)`
- `Core: Förbättra hantering av bildöversättning (#60)`

> [!NOTE]
> För närvarande läggs prefixen **`Docs`**, **`Core`** och **`Build`** automatiskt till PR-titlar baserat på etiketter som applicerats på den modifierade källkoden. Så länge rätt etikett är applicerad behöver du vanligtvis inte manuellt uppdatera PR-titeln. Du behöver bara verifiera att allt är korrekt och att prefixet har genererats på rätt sätt.

#### Sammanslagningsstrategi

Vi använder **Squash and Merge** som vår standardstrategi för pull requests. Denna strategi säkerställer att commit-meddelanden följer vårt format, även om individuella commits inte gör det.

**Anledningar**:

- En ren, linjär projekthistorik.
- Konsekvens i commit-meddelanden.
- Mindre brus från mindre commits (t.ex. "fixa stavfel").

När du slår ihop, se till att det slutgiltiga commit-meddelandet följer det commit-format som beskrivs ovan.

**Exempel på Squash and Merge**
Om en PR innehåller följande commits:

- `fixa stavfel`
- `uppdatera README`
- `justera formatering`

Ska de slås ihop till:
`Docs: Förbättra dokumentationens tydlighet och formatering (#65)`

### Release-process

Det här avsnittet beskriver det enklaste sättet för underhållare att publicera en ny version av Co-op Translator.

#### 1. Höj versionen i `pyproject.toml`

1. Bestäm nästa versionsnummer (vi följer semantisk versionering: `MAJOR.MINOR.PATCH`).
2. Redigera `pyproject.toml` och uppdatera fältet `version` under `[tool.poetry]`.
3. Öppna en dedikerad pull request som endast ändrar versionen (och eventuella automatiskt uppdaterade lås-/metadatafiler, om sådana finns).
4. Efter granskning, använd **Squash and Merge** och se till att det slutgiltiga commit-meddelandet följer formatet som beskrivs ovan.

#### 2. Skapa en GitHub Release

1. Gå till GitHub-repositoriets sida och öppna **Releases** → **Draft a new release**.
2. Skapa en ny tagg (t.ex. `v0.13.0`) från `main`-grenen.
3. Sätt releasetiteln till samma version (t.ex. `v0.13.0`).
4. Klicka på **Generate release notes** för att automatiskt fylla i changeloggen.
5. Redigera texten vid behov (t.ex. för att lyfta fram nyss stödjade språk eller viktiga ändringar).
6. Publicera releasen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->