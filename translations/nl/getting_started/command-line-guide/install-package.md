<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:30:26+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "nl"
}
-->
# Installeer het Co-op Translator pakket

De **Co-op Translator** is een command-line interface (CLI) tool die je helpt om alle markdown-bestanden en afbeeldingen in je project naar meerdere talen te vertalen. Deze handleiding laat zien hoe je de vertaler configureert en gebruikt voor verschillende scenario's.

### Maak een virtuele omgeving aan

Je kunt een virtuele omgeving aanmaken met `pip` of `Poetry`. Typ een van de volgende commando's in je terminal.

#### Met pip

```bash
python -m venv .venv
```

#### Met Poetry

```bash
poetry init
```

### Activeer de virtuele omgeving

Na het aanmaken van de virtuele omgeving moet je deze activeren. De stappen verschillen per besturingssysteem. Typ het volgende commando in je terminal.

#### Voor zowel pip als Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Met Poetry

1. Als je de omgeving met Poetry hebt aangemaakt, typ dan het volgende commando in je terminal om deze te activeren.

    ```bash
    poetry shell
    ```

### Het pakket en benodigde pakketten installeren

Zodra je virtuele omgeving is opgezet en geactiveerd, is de volgende stap het installeren van de benodigde afhankelijkheden.

### Snelle installatie

Installeer Co-Op Translator via pip

```
pip install co-op-translator
```
Of 

Installeer via poetry
```
poetry add co-op-translator
```

#### Met pip (vanuit requirements.txt) als je deze repo kloont

> [!NOTE]
> Doe dit NIET als je co-op translator via de snelle installatie hebt geïnstalleerd.

1. Als je pip gebruikt, typ dan het volgende commando in je terminal. Hiermee worden automatisch de benodigde pakketten geïnstalleerd die in het bestand `requirements.txt` staan:

    ```bash
    pip install -r requirements.txt
    ```

#### Met Poetry (vanuit pyproject.toml)

1. Als je Poetry gebruikt, typ dan het volgende commando in je terminal. Hiermee worden automatisch de benodigde pakketten geïnstalleerd die in het bestand `pyproject.toml` staan:

    ```bash
    poetry install
    ```

---

**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.