<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:35:24+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "no"
}
-->
# Installer Co-op translator-pakken

**Co-op Translator** er et kommandolinjeverktøy (CLI) som hjelper deg med å oversette alle markdown-filene og bildene i prosjektet ditt til flere språk. Denne veiledningen tar deg gjennom hvordan du konfigurerer oversetteren og kjører den for ulike brukstilfeller.

### Opprett et virtuelt miljø

Du kan opprette et virtuelt miljø ved å bruke enten `pip` eller `Poetry`. Skriv en av følgende kommandoer i terminalen din.

#### Bruke pip

```bash
python -m venv .venv
```

#### Bruke Poetry

```bash
poetry init
```

### Aktiver det virtuelle miljøet

Etter at du har opprettet det virtuelle miljøet, må du aktivere det. Stegene varierer avhengig av operativsystemet ditt. Skriv følgende kommando i terminalen.

#### For både pip og Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Bruke Poetry

1. Hvis du opprettet miljøet med Poetry, skriv følgende kommando i terminalen for å aktivere det.

    ```bash
    poetry shell
    ```

### Installere pakken og nødvendige pakker

Når det virtuelle miljøet ditt er satt opp og aktivert, er neste steg å installere de nødvendige avhengighetene.

### Rask installasjon

Installer via Co-Op Translator med pip

```
pip install co-op-translator
```
Eller

Installer via Poetry
```
poetry add co-op-translator
```

#### Bruke pip (fra requirements.txt) hvis du kloner dette repoet

![NOTE] Vennligst IKKE gjør dette hvis du installerer co-op translator via rask installasjon.

1. Hvis du bruker pip, skriv følgende kommando i terminalen. Den vil automatisk installere de nødvendige pakkene spesifisert i `requirements.txt`-filen:

    ```bash
    pip install -r requirements.txt
    ```

#### Bruke Poetry (fra pyproject.toml)

1. Hvis du bruker Poetry, skriv følgende kommando i terminalen. Den vil automatisk installere de nødvendige pakkene spesifisert i `pyproject.toml`-filen:

    ```bash
    poetry install
    ```

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.