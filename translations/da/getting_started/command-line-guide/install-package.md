<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:22:25+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "da"
}
-->
# Installer Co-op Translator-pakken

**Co-op Translator** er et kommandolinjeværktøj (CLI), der hjælper dig med at oversætte alle markdown-filer og billeder i dit projekt til flere sprog. Denne vejledning guider dig igennem, hvordan du konfigurerer oversætteren og bruger den til forskellige formål.

### Opret et virtuelt miljø

Du kan oprette et virtuelt miljø med enten `pip` eller `Poetry`. Skriv en af følgende kommandoer i din terminal.

#### Brug af pip

```bash
python -m venv .venv
```

#### Brug af Poetry

```bash
poetry init
```

### Aktiver det virtuelle miljø

Når du har oprettet det virtuelle miljø, skal du aktivere det. Fremgangsmåden afhænger af dit styresystem. Skriv følgende kommando i din terminal.

#### For både pip og Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Brug af Poetry

1. Hvis du har oprettet miljøet med Poetry, skal du skrive følgende kommando i din terminal for at aktivere det.

    ```bash
    poetry shell
    ```

### Installation af pakken og nødvendige pakker

Når dit virtuelle miljø er oprettet og aktiveret, er næste skridt at installere de nødvendige afhængigheder.

### Hurtig installation

Installer Co-Op Translator via pip

```
pip install co-op-translator
```
Eller

Installer via poetry
```
poetry add co-op-translator
```

#### Brug af pip (fra requirements.txt), hvis du kloner dette repo

> [!NOTE]
> Gør IKKE dette, hvis du installerer co-op translator via hurtig installation.

1. Hvis du bruger pip, skal du skrive følgende kommando i din terminal. Den installerer automatisk de nødvendige pakker, der er angivet i `requirements.txt`-filen:

    ```bash
    pip install -r requirements.txt
    ```

#### Brug af Poetry (fra pyproject.toml)

1. Hvis du bruger Poetry, skal du skrive følgende kommando i din terminal. Den installerer automatisk de nødvendige pakker, der er angivet i `pyproject.toml`-filen:

    ```bash
    poetry install
    ```

---

**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.