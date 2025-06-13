<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:35:15+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "da"
}
-->
# Installer Co-op translator-pakken

**Co-op Translator** er et kommandolinjeværktøj (CLI), der hjælper dig med at oversætte alle markdown-filer og billeder i dit projekt til flere sprog. Denne vejledning guider dig gennem opsætning af translatoren og hvordan du kører den til forskellige formål.

### Opret et virtuelt miljø

Du kan oprette et virtuelt miljø ved hjælp af enten `pip` eller `Poetry`. Skriv en af følgende kommandoer i din terminal.

#### Brug af pip

```bash
python -m venv .venv
```

#### Brug af Poetry

```bash
poetry init
```

### Aktiver det virtuelle miljø

Når det virtuelle miljø er oprettet, skal du aktivere det. Trinnene varierer afhængigt af dit operativsystem. Skriv følgende kommando i din terminal.

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

1. Hvis du har oprettet miljøet med Poetry, skal du skrive følgende kommando i terminalen for at aktivere det.

    ```bash
    poetry shell
    ```

### Installation af pakken og nødvendige pakker

Når dit virtuelle miljø er sat op og aktiveret, er næste skridt at installere de nødvendige afhængigheder.

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

![NOTE] Gør venligst IKKE dette, hvis du installerer co-op translator via hurtiginstallationen.

1. Hvis du bruger pip, skal du skrive følgende kommando i din terminal. Den installerer automatisk de nødvendige pakker, som er angivet i `requirements.txt`-filen:

    ```bash
    pip install -r requirements.txt
    ```

#### Brug af Poetry (fra pyproject.toml)

1. Hvis du bruger Poetry, skal du skrive følgende kommando i din terminal. Den installerer automatisk de nødvendige pakker, som er angivet i `pyproject.toml`-filen:

    ```bash
    poetry install
    ```

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.