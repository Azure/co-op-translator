<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:24:59+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "no"
}
-->
# Installer Co-op Translator-pakken

**Co-op Translator** er et kommandolinjeverktøy (CLI) som hjelper deg å oversette alle markdown-filer og bilder i prosjektet ditt til flere språk. Denne veiledningen viser deg hvordan du konfigurerer oversetteren og bruker den til ulike formål.

### Opprett et virtuelt miljø

Du kan opprette et virtuelt miljø med enten `pip` eller `Poetry`. Skriv inn en av følgende kommandoer i terminalen din.

#### Med pip

```bash
python -m venv .venv
```

#### Med Poetry

```bash
poetry init
```

### Aktiver det virtuelle miljøet

Etter at du har opprettet det virtuelle miljøet, må du aktivere det. Fremgangsmåten varierer avhengig av operativsystem. Skriv inn følgende kommando i terminalen din.

#### For både pip og Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Med Poetry

1. Hvis du opprettet miljøet med Poetry, skriv inn følgende kommando i terminalen for å aktivere det.

    ```bash
    poetry shell
    ```

### Installere pakken og nødvendige pakker

Når det virtuelle miljøet er satt opp og aktivert, er neste steg å installere nødvendige avhengigheter.

### Rask installasjon

Installer Co-Op Translator via pip

```
pip install co-op-translator
```
Eller

Installer via poetry
```
poetry add co-op-translator
```

#### Med pip (fra requirements.txt) hvis du kloner dette repoet

> [!NOTE]
> Ikke gjør dette hvis du installerer co-op translator via rask installasjon.

1. Hvis du bruker pip, skriv inn følgende kommando i terminalen. Den vil automatisk installere nødvendige pakker som er spesifisert i `requirements.txt`-filen:

    ```bash
    pip install -r requirements.txt
    ```

#### Med Poetry (fra pyproject.toml)

1. Hvis du bruker Poetry, skriv inn følgende kommando i terminalen. Den vil automatisk installere nødvendige pakker som er spesifisert i `pyproject.toml`-filen:

    ```bash
    poetry install
    ```

---

**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, må du være oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.