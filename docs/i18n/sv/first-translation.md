# Översätt, redigera och granska ett litet projekt

Börja med två korta Markdown-filer och ett målspråk. Du får se var översättningarna sparas, vad som händer när källan ändras och hur du kontrollerar resultatet.

## Registrerade resultat

Exemplet kördes den 19 september 2026 med Co-op Translator 0.21.0 och Azure OpenAI (`gpt-5-mini`). De oförändrade CLI-kommandona anropades genom Clicks `CliRunner` med det byggda wheel-paketet och befintliga Python-beroenden.

| Steg | Resultat |
| --- | --- |
| Förhandsgranskning | Avslut 0; ingen modellöversättning begärdes |
| Initial översättning | Avslut 0; 27.36 sekunder |
| Initial granskning | Avslut 0 |
| Redigera README och granska | Avslut 1; föråldrad översättning upptäcktes |
| Uppdatera översättning | Avslut 0; 22.17 sekunder |
| Granskning efter uppdatering | Avslut 0; inga fel eller varningar |
| Oförändrad guide | Identiska bytes före och efter README-uppdatering |
| Kör igen | Avslut 0; identiska hashvärden för alla översättningsfiler |

Detta är mätningar för enskilda körningar, inte prestandagarantier. Uppstartstid är exkluderad; leverantörsfakturering mättes inte. En oförändrad körning kan fortfarande utföra en leverantörshälsokontroll.

Granska [initial översättning](../../assets/demo/before.txt), [uppdaterad översättning](../../assets/demo/after.txt), [komplett översättningsdiff](../../assets/demo/update.diff), [föråldrad granskning](../../assets/demo/review-stale.txt), [slutlig granskning](../../assets/demo/review-after.txt) och [körningsdetaljer](../../assets/demo/results.json). Översättning av hela filen kan ändra andra formuleringar, som den fångade diffen visar. Båda textartefakterna behåller den genererade ansvarsfriskrivningen.

Mänsklig granskning spelar fortfarande roll: den fångade uppdateringen använder `[사용 가이드](guide.md)을`; den koreanska partikeln borde vara `[사용 가이드](guide.md)를`. Textartefakterna behåller denna utdata intakt istället för att visa en redigerad översättning som modelloutput. Den strukturella granskningen godkänns trots detta formuleringsproblem.

## 1. Förbered en liten mapp

Använd Python 3.11–3.14 och [inställning av virtuell miljö](configuration.md#local-runtime-setup). Installera den version som användes för detta exempel:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Ladda ner [README.txt](../../assets/demo/README.txt) och [guide.txt](../../assets/demo/guide.txt) till denna mapp och spara dem som `README.md` och `guide.md`. De är små fiktiva projektdokument; ingen installation av applikation krävs.

README innehåller ett kodblock och en länk till `guide.md`. Dess sista mening är:

```text
Notes are saved locally.
```

Behåll endast dessa två källdokument i den här mappen. Alla följande kommandon körs inuti `translation-demo` och fungerar i Bash och PowerShell.

## 2. Förhandsgranska utan autentiseringsuppgifter

```bash
translate -l "ko" -md --dry-run
```

Förhandsgranskningen uppskattar översättningsarbetet utan att anropa en modell eller skriva översättningar. Tokenuppskattningar är inte en faktureringsuppgift. Den första körningen bör identifiera båda Markdown-filerna som nytt arbete.

## 3. Välj en leverantör och översätt

Konfigurera en leverantör med hjälp av [konfigurationsguiden](configuration.md): Azure OpenAI, OpenAI eller Anthropic. OpenAI och Anthropic kräver inget Azure-konto för textöversättning. Bildtjänster behövs inte för detta exempel.

Om du använder en lokal `.env`-fil, lägg till `.env` i den här mappens `.gitignore`. Översättningsanrop använder ditt leverantörskonto och kan medföra avgifter.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Öppna `translations/ko/README.md` och `translations/ko/guide.md`. Kontrollera den koreanska ordalydelsen, kodblocket och länken från den översatta README-filen till den översatta guiden. Formuleringen i utdata varierar beroende på modell.

`co-op-review` kontrollerar aktualitet, struktur och lokala länkar. Ett godkänt resultat garanterar inte språklig korrekthet. Åtgärda eventuella rapporterade fel innan du fortsätter.

Registrera den lyckade baslinjen med Git (konfigurera först din Git-identitet om det behövs):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Ändra källan

I `README.md`, ersätt `Notes are saved locally.` med:

```text
Notes are saved locally as Markdown files.
```

Lämna `guide.md` oförändrad. Kör sedan:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Granskningen bör rapportera README-översättningen som föråldrad och avsluta med fel. Detta är det förväntade mellanläget. Förhandsgranskningen bör identifiera arbete för den ändrade README-filen.

## 5. Uppdatera och granska diffen

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Granska den faktiska diffen: standard-CLI:n översätter om den ändrade filen, så modellen kan också revidera annan formulering i den filen. Den oförändrade guiden bör inte ha någon diff. Granskningen bör inte längre rapportera README som föråldrad; undersök eventuella andra fynd istället för att ignorera dem.

Bevarande på blocknivå av mänskliga Markdown-redigeringar kräver en valfri translation state provider i [Python API](api.md). Den är inte aktiverad av dessa CLI-kommandon.

## 6. Kör igen utan ändringar

Commitera den uppdaterade källan och översättningen:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Med nuvarande översättningar och oförändrad konfiguration hoppar översättaren över filerna. Det sista Git-kommandot bör inte ge någon diff och avsluta framgångsrikt.

## Nästa steg

- [Översätt endast README och öppna en pull request](github-actions.md#your-first-readme-translation-pr).
- [Välj CLI, Python API eller MCP](workflows.md).
- [Rapportera ett översättningsproblem utan kodning](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).