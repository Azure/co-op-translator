# Probleemoplossing

Gebruik deze pagina wanneer een vertaalrun onverwacht slaagt, faalt tijdens de configuratie, of output produceert die beoordeeld moet worden.

## Begin hier

1. Voer eerst een gerichte opdracht uit, zoals `translate -l "ko" -md`.
2. Voeg `-d` toe voor console-debuglogs.
3. Voeg `-s` toe om debuglogs op te slaan onder `<root-dir>/logs/`.
4. Voer `co-op-review` uit na vertaling om actualiteit, structuur en lokale links te controleren.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Configuratiefouten

### Geen taalmodelprovider

Fout:

```text
No language model configuration found.
```

Oplossing:

- Configureer Azure OpenAI, OpenAI of Anthropic.
- Controleer of de variabelen aanwezig zijn in de omgeving waarin de opdracht wordt uitgevoerd.
- Voor lokaal gebruik zet ze in `.env` in de projectroot.

Zie [Configuratie](configuration.md).

### Afbeeldingsvertaling zonder Azure AI Vision

Fout:

```text
Image translation requested but Azure AI Service is not configured.
```

Oplossing:

- Voeg `AZURE_AI_SERVICE_API_KEY` toe.
- Voeg `AZURE_AI_SERVICE_ENDPOINT` toe.
- Of voer een alleen-tekstopdracht uit zoals `translate -l "ko" -md`.

### Ongeldige sleutel of endpoint

Symptomen kunnen `401`-fouten, geanonimiseerde machtigingsfouten of problemen met endpoint-toegang omvatten.

Oplossing:

- Bevestig dat de sleutel bij dezelfde Azure-resource hoort als het endpoint.
- Bevestig dat de resource Vision ondersteunt wanneer `-img` wordt gebruikt.
- Bevestig dat de naam van de Azure OpenAI-implementatie en de API-versie overeenkomen met jouw implementatie.
- Voer uit met debuglogs: `translate -l "ko" -md -d -s`.

## Er zijn geen bestanden vertaald

Veelvoorkomende oorzaken:

- De geselecteerde flags komen niet overeen met je bestanden.
- Er zijn al bestaande vertaalde bestanden aanwezig.
- Bronbestanden bevinden zich in uitgesloten mappen.
- De opdracht wordt uitgevoerd vanuit de verkeerde projectroot.

Controlepunten:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Gebruik `--root-dir` wanneer de opdracht buiten de projectroot wordt uitgevoerd.

## Onverwacht linkgedrag

Het herschrijven van links hangt af van de geselecteerde inhoudstypen:

- `-nb` ingesloten: notebook-links kunnen naar vertaalde notebooks verwijzen.
- `-nb` uitgesloten: notebook-links kunnen blijven verwijzen naar bron-notebooks.
- `-img` ingesloten: afbeeldingslinks kunnen naar vertaalde afbeeldingen verwijzen.
- `-img` uitgesloten: afbeeldingslinks kunnen blijven verwijzen naar bronafbeeldingen.

Voer een volledige inhoudsvertaling uit wanneer alle interne links de voorkeur aan vertaalde outputs moeten geven:

```bash
translate -l "ko" -md -nb -img
```

Voer na vertaling een linkreview uit:

```bash
co-op-review -l "ko"
```

## Problemen met Markdown-rendering

Als vertaald Markdown onjuist wordt weergegeven:

- Controleer dat frontmatter begint en eindigt met `---`.
- Controleer dat het aantal code-fences overeenkomt tussen bron- en vertaalde bestanden.
- Voer `co-op-review` uit om veelvoorkomende structurele problemen te vinden.
- Vertaal het specifieke bestand opnieuw als de output beschadigd was.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action draaide maar er werd geen Pull Request aangemaakt

Als `peter-evans/create-pull-request` meldt dat de branch niet voorloopt op de base, heeft de workflow geen bestanden gevonden om te committen.

Waarschijnlijke oorzaken:

- De vertaalrun leverde geen wijzigingen op.
- `.gitignore` sluit `translations/`, `translated_images/` of vertaalde notebooks uit.
- `add-paths` komt niet overeen met de gegenereerde outputmappen.
- De vertaalstap werd voortijdig beëindigd.

Oplossingen:

1. Controleer of gegenereerde bestanden bestaan in `translations/` of `translated_images/`.
2. Controleer of `.gitignore` de gegenereerde output niet uitsluit.
3. Gebruik overeenkomende `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Voeg tijdelijk debugflags toe aan de translate-opdracht:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Controleer of workflow-rechten het volgende omvatten:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Vertaalkwaliteit

Machinevertalingen kunnen menselijke controle nodig hebben. Gebruik `evaluate` alleen wanneer je experimentele kwaliteitsbeoordeling en lage-zekerheid reparatieworkflows wilt.

!!! warning "Experimenteel"
    `evaluate` kan regelgebaseerde en LLM-gebaseerde controles gebruiken, en het scoremodel en metadata-gedrag kunnen veranderen. Houd het buiten vereiste CI-gates tenzij je workflow is voorbereid op wijzigingen.

Voor deterministische CI-controles, gebruik in plaats daarvan `co-op-review`.