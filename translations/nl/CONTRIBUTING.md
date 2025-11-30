<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T11:35:29+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "nl"
}
-->
# Bijdragen aan Co-op Translator

Dit project verwelkomt bijdragen en suggesties. De meeste bijdragen vereisen dat je akkoord gaat met een Contributor License Agreement (CLA) waarin je verklaart dat je het recht hebt om, en daadwerkelijk, ons de rechten verleent om jouw bijdrage te gebruiken. Voor details, bezoek https://cla.opensource.microsoft.com.

Wanneer je een pull request indient, bepaalt een CLA-bot automatisch of je een CLA moet aanleveren en voorziet het PR van de juiste aanduidingen (bijv. statuscontrole, commentaar). Volg gewoon de instructies van de bot. Dit hoef je maar één keer te doen voor alle repositories die onze CLA gebruiken.

## Ontwikkelomgeving instellen

Voor het opzetten van de ontwikkelomgeving voor dit project raden we aan Poetry te gebruiken voor het beheren van afhankelijkheden. We gebruiken `pyproject.toml` om projectafhankelijkheden te beheren, dus om afhankelijkheden te installeren, moet je Poetry gebruiken.

### Maak een virtuele omgeving aan

#### Met pip

```bash
python -m venv .venv
```

#### Met Poetry

```bash
poetry init
```

### Activeer de virtuele omgeving

#### Voor zowel pip als Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Met Poetry

```bash
poetry shell
```

### Installeren van het pakket en benodigde pakketten

#### Met Poetry (vanuit pyproject.toml)

```bash
poetry install
```

### Handmatig testen

Voordat je een PR indient, is het belangrijk om de vertaalfunctionaliteit te testen met echte documentatie:

1. Maak een testmap aan in de hoofdmap:
    ```bash
    mkdir test_docs
    ```

2. Kopieer wat markdown-documentatie en afbeeldingen die je wilt vertalen naar de testmap. Bijvoorbeeld:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Installeer het pakket lokaal:
    ```bash
    pip install -e .
    ```

4. Voer Co-op Translator uit op je testdocumenten:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Controleer de vertaalde bestanden in `test_docs/translations` en `test_docs/translated_images` om te verifiëren:
   - De kwaliteit van de vertaling
   - De metadata-commentaren zijn correct
   - De originele markdown-structuur is behouden
   - Links en afbeeldingen werken correct

Deze handmatige test helpt ervoor te zorgen dat je wijzigingen goed functioneren in realistische situaties.

### Omgevingsvariabelen

1. Maak een `.env`-bestand aan in de hoofdmap door het meegeleverde `.env.template`-bestand te kopiëren.
1. Vul de omgevingsvariabelen in zoals aangegeven.

> [!TIP]
>
> ### Extra opties voor de ontwikkelomgeving
>
> Naast het lokaal draaien van het project, kun je ook GitHub Codespaces of VS Code Dev Containers gebruiken als alternatieve ontwikkelomgeving.
>
> #### GitHub Codespaces
>
> Je kunt deze voorbeelden virtueel draaien met GitHub Codespaces, zonder extra instellingen of configuratie.
>
> De knop opent een webgebaseerde VS Code-instantie in je browser:
>
> 1. Open de template (dit kan enkele minuten duren):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Lokaal draaien met VS Code Dev Containers
>
> ⚠️ Deze optie werkt alleen als je Docker Desktop minimaal 16 GB RAM heeft toegewezen. Heb je minder dan 16 GB RAM, dan kun je de [GitHub Codespaces optie](../..) proberen of [de lokale setup](../..) gebruiken.
>
> Een gerelateerde optie is VS Code Dev Containers, waarmee je het project opent in je lokale VS Code met de [Dev Containers-extensie](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Start Docker Desktop (installeer het indien nog niet gedaan)
> 2. Open het project:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Code stijl

We gebruiken [Black](https://github.com/psf/black) als onze Python code formatter om een consistente code stijl in het project te behouden. Black is een compromisloze formatter die Python code automatisch herformatteert volgens de Black code stijl.

#### Configuratie

De Black-configuratie staat in onze `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black installeren

Je kunt Black installeren met Poetry (aanbevolen) of pip:

##### Met Poetry

Black wordt automatisch geïnstalleerd bij het opzetten van de ontwikkelomgeving:
```bash
poetry install
```

##### Met pip

Als je pip gebruikt, kun je Black direct installeren:
```bash
pip install black
```

#### Black gebruiken

##### Met Poetry

1. Formatteer alle Python-bestanden in het project:
    ```bash
    poetry run black .
    ```

2. Formatteer een specifiek bestand of map:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Met pip

1. Formatteer alle Python-bestanden in het project:
    ```bash
    black .
    ```

2. Formatteer een specifiek bestand of map:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> We raden aan je editor zo in te stellen dat code automatisch met Black wordt geformatteerd bij het opslaan. De meeste moderne editors ondersteunen dit via extensies of plugins.

## Co-op Translator uitvoeren

Om Co-op Translator te draaien met Poetry in jouw omgeving, volg je deze stappen:

1. Navigeer naar de map waar je vertaaltests wilt uitvoeren of maak een tijdelijke map aan voor testdoeleinden.

2. Voer het volgende commando uit. Vervang `-l ko` door de taalcode waarin je wilt vertalen. De `-d` vlag geeft debugmodus aan.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Zorg dat je Poetry-omgeving is geactiveerd (poetry shell) voordat je het commando uitvoert.

## Een nieuwe taal toevoegen

We verwelkomen bijdragen die ondersteuning voor nieuwe talen toevoegen. Voltooi voor het openen van een PR de onderstaande stappen om een soepele beoordeling te garanderen.

1. Voeg de taal toe aan de font mapping
   - Bewerk `src/co_op_translator/fonts/font_language_mappings.yml`
   - Voeg een item toe met:
     - `code`: ISO-achtige taalcode (bijv. `vi`)
     - `name`: Mensvriendelijke weergavenaam
     - `font`: Een lettertype dat wordt meegeleverd in `src/co_op_translator/fonts/` en het schrift ondersteunt
     - `rtl`: `true` als het een rechts-naar-links taal is, anders `false`

2. Voeg benodigde lettertypebestanden toe (indien nodig)
   - Controleer licentiecompatibiliteit voor open source distributie als een nieuw lettertype vereist is
   - Voeg het lettertypebestand toe aan `src/co_op_translator/fonts/`

3. Lokale verificatie
   - Voer vertalingen uit voor een kleine sample (Markdown, afbeeldingen en notebooks indien van toepassing)
   - Controleer of de output correct wordt weergegeven, inclusief lettertypen en eventuele RTL-layout

4. Documentatie bijwerken
   - Zorg dat de taal voorkomt in `getting_started/supported-languages.md`
   - Er zijn geen aanpassingen nodig in `getting_started/README_languages_template.md`; dit wordt gegenereerd vanuit de ondersteunde lijst

5. Open een PR
   - Beschrijf de toegevoegde taal en eventuele font/licentie-overwegingen
   - Voeg indien mogelijk screenshots toe van de gerenderde output

Voorbeeld YAML-item:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Test de nieuwe taal

Je kunt de nieuwe taal testen door het volgende commando uit te voeren:

```bash
# Maak en activeer een virtuele omgeving
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Installeer het ontwikkelpakket
pip install -e .
# Voer de vertaling uit
translate -l "new_lang"
```

## Beheerders

### Commitbericht en Merge-strategie

Om consistentie en duidelijkheid in de commitgeschiedenis van ons project te waarborgen, hanteren we een specifiek commitberichtformaat **voor het uiteindelijke commitbericht** bij gebruik van de **Squash and Merge** strategie.

Wanneer een pull request (PR) wordt gemerged, worden de individuele commits samengevoegd tot één commit. Het uiteindelijke commitbericht moet het onderstaande formaat volgen om een schone en consistente geschiedenis te behouden.

#### Commitberichtformaat (voor squash and merge)

We gebruiken het volgende formaat voor commitberichten:

```bash
<type>: <description> (#<PR nummer>)
```

- **type**: Geeft de categorie van de commit aan. We gebruiken de volgende types:
  - `Docs`: Voor documentatie-updates.
  - `Build`: Voor wijzigingen gerelateerd aan het build-systeem of afhankelijkheden, inclusief updates aan configuratiebestanden, CI-workflows of de Dockerfile.
  - `Core`: Voor aanpassingen aan de kernfunctionaliteit of features van het project, vooral die in de `src/co_op_translator/core` map.

- **description**: Een beknopte samenvatting van de wijziging.
- **PR nummer**: Het nummer van de pull request die bij de commit hoort.

**Voorbeelden**:

- `Docs: Update installatie-instructies voor duidelijkheid (#50)`
- `Core: Verbeter afhandeling van afbeeldingvertaling (#60)`

> [!NOTE]
> Momenteel worden de prefixen **`Docs`**, **`Core`** en **`Build`** automatisch toegevoegd aan PR-titels op basis van de labels die op de gewijzigde broncode zijn toegepast. Zolang het juiste label is toegepast, hoef je de PR-titel meestal niet handmatig aan te passen. Controleer alleen of alles correct is en het prefix correct is gegenereerd.

#### Merge-strategie

We gebruiken **Squash and Merge** als standaardstrategie voor pull requests. Deze strategie zorgt ervoor dat commitberichten ons formaat volgen, ook als individuele commits dat niet doen.

**Redenen**:

- Een schone, lineaire projectgeschiedenis.
- Consistentie in commitberichten.
- Minder ruis door kleine commits (bijv. "fix typo").

Zorg bij het mergen dat het uiteindelijke commitbericht het hierboven beschreven commitberichtformaat volgt.

**Voorbeeld van Squash and Merge**
Als een PR de volgende commits bevat:

- `fix typo`
- `update README`
- `adjust formatting`

Dan worden deze samengevoegd tot:
`Docs: Improve documentation clarity and formatting (#65)`

### Releaseproces

Deze sectie beschrijft de eenvoudigste manier voor beheerders om een nieuwe release van Co-op Translator uit te brengen.

#### 1. Verhoog de versie in `pyproject.toml`

1. Bepaal het volgende versienummer (we volgen semantische versiebeheer: `MAJOR.MINOR.PATCH`).
2. Bewerk `pyproject.toml` en werk het `version` veld bij onder `[tool.poetry]`.
3. Open een dedicated pull request die alleen de versie (en eventuele automatisch bijgewerkte lock-/metadata-bestanden, indien aanwezig) wijzigt.
4. Na review, gebruik **Squash and Merge** en zorg dat het uiteindelijke commitbericht het hierboven beschreven formaat volgt.

#### 2. Maak een GitHub Release aan

1. Ga naar de GitHub repository pagina en open **Releases** → **Draft a new release**.
2. Maak een nieuwe tag aan (bijvoorbeeld `v0.13.0`) vanaf de `main` branch.
3. Stel de release titel in op dezelfde versie (bijvoorbeeld `v0.13.0`).
4. Klik op **Generate release notes** om de changelog automatisch te vullen.
5. Bewerk de tekst eventueel (bijvoorbeeld om nieuw ondersteunde talen of belangrijke wijzigingen te benadrukken).
6. Publiceer de release.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->