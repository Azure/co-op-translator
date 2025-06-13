<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:35:06+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "sv"
}
-->
# Installera Co-op translator-paketet

**Co-op Translator** är ett kommandoradsverktyg (CLI) som hjälper dig att översätta alla markdown-filer och bilder i ditt projekt till flera språk. Den här guiden visar hur du konfigurerar översättaren och kör den för olika användningsområden.

### Skapa en virtuell miljö

Du kan skapa en virtuell miljö med antingen `pip` eller `Poetry`. Skriv ett av följande kommandon i din terminal.

#### Med pip

```bash
python -m venv .venv
```

#### Med Poetry

```bash
poetry init
```

### Aktivera den virtuella miljön

När du har skapat den virtuella miljön måste du aktivera den. Stegen skiljer sig beroende på operativsystem. Skriv följande kommando i din terminal.

#### För både pip och Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Med Poetry

1. Om du skapade miljön med Poetry, skriv följande kommando i terminalen för att aktivera den.

    ```bash
    poetry shell
    ```

### Installera paketet och nödvändiga beroenden

När din virtuella miljö är upprättad och aktiverad är nästa steg att installera de nödvändiga beroendena.

### Snabbinstallation

Installera Co-Op Translator via pip

```
pip install co-op-translator
```  
Eller

Installera via Poetry  
```
poetry add co-op-translator
```

#### Med pip (från requirements.txt) om du klonar detta repo

![NOTE] Gör INTE detta om du installerar co-op translator via snabbinstallationen.

1. Om du använder pip, skriv följande kommando i terminalen. Det installerar automatiskt de paket som krävs enligt `requirements.txt`-filen:

    ```bash
    pip install -r requirements.txt
    ```

#### Med Poetry (från pyproject.toml)

1. Om du använder Poetry, skriv följande kommando i terminalen. Det installerar automatiskt de paket som krävs enligt `pyproject.toml`-filen:

    ```bash
    poetry install
    ```

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.