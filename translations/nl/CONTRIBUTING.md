<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:37:42+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "nl"
}
-->
# Bijdragen aan Co-op Translator

Dit project verwelkomt bijdragen en suggesties. De meeste bijdragen vereisen dat je akkoord gaat met een Contributor License Agreement (CLA) waarin je verklaart dat je het recht hebt om, en daadwerkelijk, ons de rechten verleent om je bijdrage te gebruiken. Voor meer details, bezoek https://cla.opensource.microsoft.com.

Wanneer je een pull request indient, zal een CLA-bot automatisch bepalen of je een CLA moet aanleveren en het PR dienovereenkomstig markeren (bijvoorbeeld statuscontrole, commentaar). Volg gewoon de instructies van de bot. Dit hoef je slechts één keer te doen voor alle repositories die onze CLA gebruiken.

## Ontwikkelomgeving opzetten

Voor het opzetten van de ontwikkelomgeving voor dit project raden we aan Poetry te gebruiken voor het beheren van afhankelijkheden. We gebruiken `pyproject.toml` om projectafhankelijkheden te beheren, en daarom moet je Poetry gebruiken om afhankelijkheden te installeren.

### Een virtuele omgeving aanmaken

#### Met pip

```bash
python -m venv .venv
```

#### Met Poetry

```bash
poetry init
```

### De virtuele omgeving activeren

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

### Het pakket en vereiste pakketten installeren

#### Met Poetry (uit pyproject.toml)

```bash
poetry install
```

### Handmatig testen

Voordat je een PR indient, is het belangrijk om de vertaalfunctionaliteit te testen met echte documentatie:

1. Maak een testmap aan in de hoofdmap:
    ```bash
    mkdir test_docs
    ```

2. Kopieer enkele markdown-documenten en afbeeldingen die je wilt vertalen naar de testmap. Bijvoorbeeld:
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

5. Controleer de vertaalde bestanden in `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` bestand.
1. Vul de omgevingsvariabelen in zoals aangegeven.

> [!TIP]
>
> ### Extra opties voor de ontwikkelomgeving
>
> Naast het lokaal draaien van het project, kun je ook GitHub Codespaces of VS Code Dev Containers gebruiken voor een alternatieve ontwikkelomgeving.
>
> #### GitHub Codespaces
>
> Je kunt deze voorbeelden virtueel draaien met GitHub Codespaces, zonder extra instellingen of configuratie.
>
> De knop opent een webgebaseerde VS Code in je browser:
>
> 1. Open de template (dit kan enkele minuten duren):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Lokaal draaien met VS Code Dev Containers
>
> ⚠️ Deze optie werkt alleen als Docker Desktop minimaal 16 GB RAM toegewezen heeft. Heb je minder dan 16 GB RAM, probeer dan de [GitHub Codespaces optie](../..) of [zet het lokaal op](../..).
>
> Een gerelateerde optie is VS Code Dev Containers, die het project opent in je lokale VS Code met de [Dev Containers extensie](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Start Docker Desktop (installeer het als het nog niet geïnstalleerd is)
> 2. Open het project:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Code stijl

We gebruiken [Black](https://github.com/psf/black) als onze Python code formatter om een consistente code stijl in het project te behouden. Black is een compromisloze code formatter die Python code automatisch aanpast aan de Black code stijl.

#### Configuratie

De Black configuratie staat in onze `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black installeren

Je kunt Black installeren via Poetry (aanbevolen) of pip:

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

1. Formatteer alle Python bestanden in het project:
    ```bash
    poetry run black .
    ```

2. Formatteer een specifiek bestand of map:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Met pip

1. Formatteer alle Python bestanden in het project:
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

Om Co-op Translator met Poetry in je omgeving uit te voeren, volg je deze stappen:

1. Navigeer naar de map waarin je vertaaltests wilt uitvoeren of maak een tijdelijke map aan voor testdoeleinden.

2. Voer het volgende commando uit. De `-l ko` with the language code you wish to translate into. The `-d` vlag geeft aan dat debugmodus aanstaat.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Zorg dat je Poetry omgeving geactiveerd is (poetry shell) voordat je het commando uitvoert.

## Beheerders

### Commitbericht en Merge strategie

Om consistentie en duidelijkheid in de commitgeschiedenis van ons project te waarborgen, volgen we een specifiek commitberichtformaat **voor het uiteindelijke commitbericht** bij het gebruik van de **Squash and Merge** strategie.

Wanneer een pull request (PR) wordt gemerged, worden de individuele commits samengevoegd tot één commit. Het uiteindelijke commitbericht moet het onderstaande formaat volgen om een schone en consistente geschiedenis te behouden.

#### Commitberichtformaat (voor squash en merge)

We gebruiken het volgende formaat voor commitberichten:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Specificeert de categorie van de commit. We gebruiken de volgende types:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Update installatie-instructies voor duidelijkheid (#50)`
- `Core: Verbeter afhandeling van afbeeldingsvertaling (#60)`

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

- `fix typefout`
- `update README`
- `pas opmaak aan`

They should be squashed into:
`Docs: Verbeter documentatie duidelijkheid en opmaak (#65)`

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal geldt als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.