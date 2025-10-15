<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:19:49+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "sv"
}
-->
# Installera Co-op Translator-paketet

**Co-op Translator** är ett kommandoradsverktyg (CLI) som hjälper dig att översätta alla markdown-filer och bilder i ditt projekt till flera språk. Den här guiden visar hur du konfigurerar översättaren och använder den för olika behov.

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

När du har skapat den virtuella miljön behöver du aktivera den. Stegen skiljer sig beroende på operativsystem. Skriv följande kommando i din terminal.

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

1. Om du skapade miljön med Poetry, skriv följande kommando i din terminal för att aktivera den.

    ```bash
    poetry shell
    ```

### Installera paketet och nödvändiga paket

När din virtuella miljö är klar och aktiverad är nästa steg att installera de nödvändiga beroenden.

### Snabbinstallation

Installera Co-Op Translator med pip

```
pip install co-op-translator
```
Eller 

Installera med poetry
```
poetry add co-op-translator
```

#### Med pip (från requirements.txt) om du klonar detta repo 

> [!NOTE]
> Gör INTE detta om du installerar co-op translator via snabbinstallationen.

1. Om du använder pip, skriv följande kommando i din terminal. Det installerar automatiskt de paket som anges i filen `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Med Poetry (från pyproject.toml)

1. Om du använder Poetry, skriv följande kommando i din terminal. Det installerar automatiskt de paket som anges i filen `pyproject.toml`:

    ```bash
    poetry install
    ```

---

**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.