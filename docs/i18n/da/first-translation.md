# Oversæt, rediger og gennemse et lille projekt

Start med to korte Markdown-filer og ét målsprog. Du vil se, hvor oversættelserne skrives, hvad der sker, når kilden ændres, og hvordan du kontrollerer resultatet.

## Optagede resultater

Eksemplet blev kørt den 19. september 2026 med Co-op Translator 0.21.0 og Azure OpenAI (`gpt-5-mini`). De uændrede CLI-kommandoer blev påkaldt via Clicks `CliRunner` ved hjælp af den byggede wheel og eksisterende Python-afhængigheder.

| Trin | Resultat |
| --- | --- |
| Forhåndsvisning | Exit 0; ingen modeloversættelse anmodet |
| Indledende oversættelse | Exit 0; 27,36 sekunder |
| Indledende gennemgang | Exit 0 |
| Rediger README og gennemse | Exit 1; forældet oversættelse opdaget |
| Opdater oversættelse | Exit 0; 22,17 sekunder |
| Gennemgang efter opdatering | Exit 0; ingen fejl eller advarsler |
| Uændret vejledning | Identiske bytes før og efter README-opdatering |
| Kør igen | Exit 0; identiske hashes for alle oversættelsesfiler |

Dette er individuelle kørselsmålinger, ikke ydelsesgarantier. Opsætningstid er ekskluderet; udbyderfakturering blev ikke målt. En uændret kørsel kan stadig udføre en sundhedskontrol hos udbyderen.

Undersøg [indledende oversættelse](../../assets/demo/before.txt), [opdateret oversættelse](../../assets/demo/after.txt), [komplet oversættelsesdiff](../../assets/demo/update.diff), [forældet gennemgang](../../assets/demo/review-stale.txt), [endelig gennemgang](../../assets/demo/review-after.txt), og [kørselsdetaljer](../../assets/demo/results.json). Oversættelse af hele filen kan ændre anden formulering, som det fangede diff viser. Begge tekstartefakter bevarer den genererede ansvarsfraskrivelse.

Menneskelig gennemgang er stadig vigtig: den indfangede opdatering bruger `[사용 가이드](guide.md)을`; den koreanske partikel burde være `[사용 가이드](guide.md)를`. Tekstartifakterne beholder denne output uændret i stedet for at præsentere en redigeret oversættelse som modeloutput. Den strukturelle gennemgang bestås på trods af dette ordlydsproblem.

## 1. Forbered en lille mappe

Brug Python 3.11–3.14 og [opsætning af virtuelt miljø](configuration.md#local-runtime-setup). Installer den version, der blev brugt til dette eksempel:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Download [README.txt](../../assets/demo/README.txt) og [guide.txt](../../assets/demo/guide.txt) til denne mappe, og gem dem som `README.md` og `guide.md`. De er små fiktive projektfiler; ingen installation af applikation er nødvendig.

README'en indeholder en kodeblok og et link til `guide.md`. Dens sidste sætning er:

```text
Notes are saved locally.
```

Hold kun disse to kildefiler i denne mappe. Alle følgende kommandoer køres inde i `translation-demo` og virker i både Bash og PowerShell.

## 2. Forhåndsvis uden legitimationsoplysninger

```bash
translate -l "ko" -md --dry-run
```

Forhåndsvisningen estimerer oversættelsesarbejdet uden at kalde en model eller skrive oversættelser. Token-estimater er ikke et faktureringsoverslag. Den første kørsel bør identificere begge Markdown-filer som nyt arbejde.

## 3. Vælg en udbyder og oversæt

Konfigurer en udbyder ved hjælp af [konfigurationsguiden](configuration.md): Azure OpenAI, OpenAI eller Anthropic. OpenAI og Anthropic tekstoversættelse kræver ikke en Azure-konto. Billedtjenester er ikke nødvendige til dette eksempel.

Hvis du bruger en lokal `.env`-fil, tilføj `.env` til denne mappes `.gitignore`. Oversættelseskald bruger din udbyderkonto og kan medføre omkostninger.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Åbn `translations/ko/README.md` og `translations/ko/guide.md`. Kontroller den koreanske ordlyd, kodeblokken og linket fra den oversatte README til den oversatte guide. Formuleringen i output varierer efter model.

`co-op-review` kontrollerer friskhed, struktur og lokale links. Et bestået resultat garanterer ikke sproglig nøjagtighed. Løs eventuelle rapporterede fejl, før du fortsætter.

Registrer det succesfulde baseline med Git (konfigurer først din Git-identitet, hvis nødvendigt):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Ændr kilden

I `README.md` skal du erstatte `Notes are saved locally.` med:

```text
Notes are saved locally as Markdown files.
```

Lad `guide.md` være uændret. Kør derefter:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Gennemgangen bør rapportere README-oversættelsen som forældet og afslutte uden succes. Dette er den forventede mellemliggende tilstand. Forhåndsvisningen bør identificere arbejde for den ændrede README.

## 5. Opdater og inspicer diffen

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Undersøg det egentlige diff: den standard CLI genskriver den ændrede fil, så modellen også kan revidere anden formulering i den fil. Den uændrede guide bør ikke have noget diff. Gennemgangen bør ikke længere rapportere README som forældet; undersøg andre fund i stedet for at ignorere dem.

Bevarelse på blokniveau af menneskelige Markdown-redigeringer kræver en valgfri leverandør af oversættelsestilstand i [Python API](api.md). Den er ikke aktiveret af disse CLI-kommandoer.

## 6. Kør igen uden ændringer

Commit de opdaterede kildefiler og oversættelsen:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Med de nuværende oversættelser og uændret konfiguration springer oversætterprogrammet filerne over. Den afsluttende Git-kommando bør ikke give noget diff og afslutte med succes.

## Næste skridt

- [Oversæt kun en README og åbn en pull request](github-actions.md#your-first-readme-translation-pr).
- [Vælg CLI, Python API eller MCP](workflows.md).
- [Rapporter et oversættelsesproblem uden at kode](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).