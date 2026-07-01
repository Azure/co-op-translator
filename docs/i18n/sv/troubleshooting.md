# Felsökning

Använd den här sidan när en översättningskörning lyckas oväntat, misslyckas under konfiguration eller producerar utdata som behöver granskas.

## Börja här

1. Kör först ett fokuserat kommando, till exempel `translate -l "ko" -md`.
2. Lägg till `-d` för felsökningsloggar i konsolen.
3. Lägg till `-s` för att spara felsökningsloggar under `<root-dir>/logs/`.
4. Kör `co-op-review` efter översättning för att kontrollera färskhet, struktur och lokala länkar.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Konfigurationsfel

### Ingen leverantör av språkmodell

Fel:

```text
No language model configuration found.
```

Åtgärd:

- Konfigurera Azure OpenAI eller OpenAI.
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
- Eller kör ett textendast-kommando såsom `translate -l "ko" -md`.

### Ogiltig nyckel eller slutpunkt

Symptom kan inkludera `401`, dolda behörighetsfel eller åtkomstfel för slutpunkten.

Åtgärd:

- Bekräfta att nyckeln tillhör samma Azure-resurs som slutpunkten.
- Bekräfta att resursen stöder Vision när du använder `-img`.
- Bekräfta att Azure OpenAI-distributionsnamn och API-version matchar din distribution.
- Kör med felsökningsloggar: `translate -l "ko" -md -d -s`.

## Inga filer översattes

Vanliga orsaker:

- De valda flaggorna matchar inte dina filer.
- Befintliga översatta filer finns redan.
- Källfiler är under uteslutna kataloger.
- Kommandot körs från fel projektrot.

Kontroller:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Använd `--root-dir` när kommandot körs utanför projektets rot.

## Oväntat länkbeteende

Omlänkning beror på valda innehållstyper:

- `-nb` inkluderat: anteckningsboks-länkar kan peka på översatta anteckningsböcker.
- `-nb` exkluderat: anteckningsboks-länkar kan förbli pekande på källanteckningsböcker.
- `-img` inkluderat: bildlänkar kan peka på översatta bilder.
- `-img` exkluderat: bildlänkar kan förbli pekande på källbilder.

Kör en fullständig innehållsöversättning när alla interna länkar bör föredra översatta utdata:

```bash
translate -l "ko" -md -nb -img
```

Kör länkgranskning efter översättning:

```bash
co-op-review -l "ko"
```

## Problem med Markdown-rendering

Om översatt Markdown renderas felaktigt:

- Kontrollera att frontmatter börjar och slutar med `---`.
- Kontrollera att antalet kodavgränsare matchar mellan käll- och översatta filer.
- Kör `co-op-review` för att fånga vanliga strukturproblem.
- Översätt om den specifika filen om utdata var korrupt.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action kördes men ingen pull-begäran skapades

Om `peter-evans/create-pull-request` rapporterar att grenen inte är före basen, hittade arbetsflödet inga filer att committa.

Sannolika orsaker:

- Översättningskörningen producerade inga förändringar.
- `.gitignore` utesluter `translations/`, `translated_images/` eller översatta anteckningsböcker.
- `add-paths` matchar inte de genererade utgångskatalogerna.
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

4. Lägg till debugflaggor temporärt i translate-kommandot:

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

Maskinöversättningar kan behöva manuell granskning. Använd `evaluate` endast när du vill ha experimentell kvalitetsbedömning och reparationsarbetsflöden för lågt förtroende.

!!! warning "Experimentell"
    `evaluate` kan använda regelbaserade och LLM-baserade kontroller, och dess poängsättningsmodell och metadata-beteende kan ändras. Håll det utanför obligatoriska CI-gates om inte ditt arbetsflöde är förberett för förändringar.

För deterministiska CI-kontroller, använd `co-op-review` istället.