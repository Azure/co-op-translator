# Problemen oplossen

Gebruik deze pagina wanneer een vertaalactie onverwacht slaagt, faalt tijdens de configuratie, of output produceert die gecontroleerd moet worden.

## Begin hier

1. Voer eerst een gerichte opdracht uit, zoals `translate -l "ko" -md`.
2. Voeg `-d` toe voor console-debuglogs.
3. Voeg `-s` toe om debuglogs op te slaan onder `<root-dir>/logs/`.
4. Voer `co-op-review` uit na vertaling om versheid, structuur en lokale links te controleren.

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

- Configureer Azure OpenAI of OpenAI.
- Controleer of de variabelen in de omgeving aanwezig zijn waar de opdracht wordt uitgevoerd.
- Voor lokaal gebruik, zet ze in `.env` in de projectroot.

Zie [Configuratie](configuration.md).

### Afbeeldingsvertaling zonder Azure AI Vision

Fout:

```text
Image translation requested but Azure AI Service is not configured.
```

Oplossing:

- Voeg `AZURE_AI_SERVICE_API_KEY` toe.
- Voeg `AZURE_AI_SERVICE_ENDPOINT` toe.
- Of voer een tekst-only opdracht uit zoals `translate -l "ko" -md`.

### Ongeldige sleutel of endpoint

Symptomen kunnen `401`, geanonimiseerde machtigingsfouten of endpoint-toegangsproblemen zijn.

Oplossing:

- Bevestig dat de sleutel bij dezelfde Azure-resource hoort als het endpoint.
- Bevestig dat de resource Vision ondersteunt bij gebruik van `-img`.
- Bevestig dat de Azure OpenAI deploymentnaam en API-versie overeenkomen met je implementatie.
- Voer uit met debuglogs: `translate -l "ko" -md -d -s`.

## Er zijn geen bestanden vertaald

Veelvoorkomende oorzaken:

- De geselecteerde flags komen niet overeen met je bestanden.
- Bestaande vertaalde bestanden zijn al aanwezig.
- Bronbestanden bevinden zich in uitgesloten mappen.
- De opdracht wordt uitgevoerd vanaf de verkeerde projectroot.

Controles:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Gebruik `--root-dir` wanneer de opdracht buiten de projectroot wordt uitgevoerd.

## Onverwacht linkgedrag

Het herschrijven van links hangt af van de geselecteerde inhoudstypen:

- `-nb` ingeschakeld: notebooklinks kunnen verwijzen naar vertaalde notebooks.
- `-nb` uitgeschakeld: notebooklinks kunnen blijven verwijzen naar bron-notebooks.
- `-img` ingeschakeld: afbeeldingslinks kunnen verwijzen naar vertaalde afbeeldingen.
- `-img` uitgeschakeld: afbeeldingslinks kunnen blijven verwijzen naar bronafbeeldingen.

Voer een volledige inhoudsvertaling uit wanneer alle interne links de voorkeur moeten geven aan vertaalde uitvoer:

```bash
translate -l "ko" -md -nb -img
```

Voer een linkcontrole uit na vertaling:

```bash
co-op-review -l "ko"
```

## Problemen met Markdown-weergave

Als vertaalde Markdown onjuist wordt weergegeven:

- Controleer of frontmatter begint en eindigt met `---`.
- Controleer of het aantal code fences overeenkomt tussen bron- en vertaalde bestanden.
- Voer `co-op-review` uit om veelvoorkomende structurele problemen op te sporen.
- Vertaal het specifieke bestand opnieuw als de output beschadigd was.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action heeft gedraaid maar er is geen Pull Request aangemaakt

Als `peter-evans/create-pull-request` meldt dat de branch niet voorloopt op de base, vond de workflow geen bestanden om te committen.

Waarschijnlijke oorzaken:

- De vertaalrun produceerde geen wijzigingen.
- `.gitignore` sluit `translations/`, `translated_images/` of vertaalde notebooks uit.
- `add-paths` komt niet overeen met de gegenereerde outputmappen.
- De vertaalstap is vroegtijdig beëindigd.

Oplossingen:

1. Bevestig dat de gegenereerde bestanden bestaan in `translations/` of `translated_images/`.
2. Bevestig dat `.gitignore` gegenereerde outputs niet negeert.
3. Gebruik bijpassende `add-paths`:

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

5. Bevestig dat de workflowrechten het volgende omvatten:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Vertaalkwaliteit

Machinevertalingen kunnen menselijke controle nodig hebben. Gebruik `evaluate` alleen wanneer je experimentele kwaliteitsbeoordelingen en reparatieworkflows voor lage betrouwbaarheid wilt.

!!! warning "Experimenteel"
    `evaluate` kan regelgebaseerde en LLM-gebaseerde controles gebruiken, en het scoringsmodel en het metadata-gedrag kunnen veranderen. Houd het buiten verplichte CI-gates tenzij je workflow voorbereid is op wijzigingen.

Voor deterministische CI-controles, gebruik in plaats daarvan `co-op-review`.