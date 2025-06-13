<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:35:42+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "nl"
}
-->
# Installeer het Co-op translator pakket

De **Co-op Translator** is een command-line interface (CLI) tool die je helpt om alle markdown-bestanden en afbeeldingen in je project naar meerdere talen te vertalen. Deze handleiding leidt je door het configureren van de translator en het uitvoeren ervan voor verschillende toepassingen.

### Maak een virtuele omgeving aan

Je kunt een virtuele omgeving aanmaken met `pip` of `Poetry`. Typ een van de volgende commando’s in je terminal.

#### Gebruik van pip

```bash
python -m venv .venv
```

#### Gebruik van Poetry

```bash
poetry init
```

### Activeer de virtuele omgeving

Nadat je de virtuele omgeving hebt aangemaakt, moet je deze activeren. De stappen verschillen per besturingssysteem. Typ het volgende commando in je terminal.

#### Voor zowel pip als Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Gebruik van Poetry

1. Als je de omgeving met Poetry hebt aangemaakt, typ dan het volgende commando in je terminal om deze te activeren.

    ```bash
    poetry shell
    ```

### Installeren van het pakket en benodigde pakketten

Zodra je virtuele omgeving is ingesteld en geactiveerd, is de volgende stap het installeren van de benodigde dependencies.

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

#### Gebruik van pip (via requirements.txt) als je deze repo clonet

![NOTE] Doe dit NIET als je co-op translator via de snelle installatie installeert.

1. Als je pip gebruikt, typ dan het volgende commando in je terminal. Dit installeert automatisch de benodigde pakketten die zijn gespecificeerd in het `requirements.txt` bestand:

    ```bash
    pip install -r requirements.txt
    ```

#### Gebruik van Poetry (via pyproject.toml)

1. Als je Poetry gebruikt, typ dan het volgende commando in je terminal. Dit installeert automatisch de benodigde pakketten die zijn gespecificeerd in het `pyproject.toml` bestand:

    ```bash
    poetry install
    ```

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal geldt als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.