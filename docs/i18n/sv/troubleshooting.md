# Felsökning

Använd den här sidan när en översättningskörning lyckas oväntat, misslyckas under konfiguration eller ger resultat som behöver granskas.

## Börja här

1. Kör först ett fokuserat kommando, till exempel `translate -l "ko" -md`.
2. Lägg till `-d` för felsökningsloggar i konsolen.
3. Lägg till `-s` för att spara felsökningsloggar under `<root-dir>/logs/`.
4. Kör `co-op-review` efter översättningen för att kontrollera aktualitet, struktur och lokala länkar.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Konfigurationsfel

### Ingen språkmodellleverantör

Fel:

```text
No language model configuration found.
```

Åtgärd:

- Konfigurera Azure OpenAI, OpenAI eller Anthropic.
- Verifiera att variablerna finns i miljön där kommandot körs.
- För lokal användning, lägg dem i `.env` i projektets rot.

Se [Konfiguration](configuration.md).

### Bildöversättning utan Azure AI Vision

Fel:

```text
Image translation requested but Azure AI Service is not configured.
```

Åtgärd:

- Lägg till `AZURE_AI_SERVICE_API_KEY`.
- Lägg till `AZURE_AI_SERVICE_ENDPOINT`.
- Eller kör ett textbaserat kommando, till exempel `translate -l "ko" -md`.

### Ogiltig nyckel eller slutpunkt

Symptom kan inkludera `401`, maskerade behörighetsfel eller åtkomstfel för slutpunkten.

Åtgärd:

- Bekräfta att nyckeln tillhör samma Azure-resurs som slutpunkten.
- Bekräfta att resursen stöder Vision när du använder `-img`.
- Bekräfta att Azure OpenAI-distributionens namn och API-version stämmer överens med din distribution.
- Kör med felsökningsloggar: `translate -l "ko" -md -d -s`.

## Inga filer översattes

Vanliga orsaker:

- De valda flaggorna stämmer inte överens med dina filer.
- Befintliga översatta filer finns redan.
- Källfiler finns i exkluderade kataloger.
- Kommandot körs från fel projektrot.

Kontroller:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Använd `--root-dir` när kommandot körs utanför projektroten.

## Oväntat länkbeteende

Omskrivning av länkar beror på valda innehållstyper:

- `-nb` inkluderat: länkar till notebooks kan peka på översatta notebooks.
- `-nb` exkluderat: länkar till notebooks kan fortsätta peka på källnotebooks.
- `-img` inkluderat: bildlänkar kan peka på översatta bilder.
- `-img` exkluderat: bildlänkar kan fortsätta peka på källbilder.

Kör en fullständig innehållsöversättning när alla interna länkar ska föredra översatta resultat:

```bash
translate -l "ko" -md -nb -img
```

Kör länkgranskning efter översättningen:

```bash
co-op-review -l "ko"
```

## Problem med Markdown-rendering

Om översatt Markdown renderas felaktigt:

- Kontrollera att frontmatter börjar och slutar med `---`.
- Kontrollera att antalet kodavgränsare stämmer överens mellan käll- och översatta filer.
- Kör `co-op-review` för att fånga vanliga strukturproblem.
- Översätt om den specifika filen om utdata blev korrupt.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action kördes men ingen pullbegäran skapades

Om `peter-evans/create-pull-request` rapporterar att grenen inte ligger före basen, hittade arbetsflödet inga filer att committa.

Troliga orsaker:

- Översättningskörningen genererade inga ändringar.
- `.gitignore` exkluderar `translations/`, `translated_images/` eller översatta notebooks.
- `add-paths` matchar inte de genererade utmatningskatalogerna.
- Översättningssteget avslutades tidigt.

Åtgärder:

1. Bekräfta att genererade filer finns i `translations/` eller `translated_images/`.
2. Bekräfta att `.gitignore` inte ignorerar genererade utdata.
3. Använd matchande `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Lägg till tillfälligt felsökningsflaggor i translate-kommandot:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Bekräfta att arbetsflödets behörigheter inkluderar:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Översättningskvalitet

Maskinöversättningar kan behöva manuell granskning. Använd `evaluate` endast när du vill ha experimentell kvalitetsbedömning och arbetsflöden för reparation av resultat med låg tillförlitlighet.

!!! warning "Experimentell"
    `evaluate` kan använda regelbaserade och LLM-baserade kontroller, och dess poängsättningsmodell och metadata-beteende kan förändras. Håll det utanför obligatoriska CI-gates om inte ditt arbetsflöde är förberett på förändringar.

För deterministiska CI-kontroller, använd `co-op-review` istället.