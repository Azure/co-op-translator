# Oversett, rediger og gjennomgå et lite prosjekt

Start med to korte Markdown-filer og ett målspråk. Du vil se hvor oversettelsene skrives, hva som skjer når kilden endres, og hvordan du sjekker resultatet.

## Registrerte resultater

Eksemplet ble kjørt 19. september 2026 med Co-op Translator 0.21.0 og Azure OpenAI (`gpt-5-mini`). De uendrede CLI-kommandoene ble kjørt gjennom Clicks `CliRunner` ved hjelp av det bygde wheelet og eksisterende Python-avhengigheter.

| Trinn | Resultat |
| --- | --- |
| Forhåndsvisning | Exit 0; ingen modelloversettelse forespurt |
| Første oversettelse | Exit 0; 27.36 sekunder |
| Første gjennomgang | Exit 0 |
| Rediger README og gjennomgå | Exit 1; foreldet oversettelse oppdaget |
| Oppdater oversettelse | Exit 0; 22.17 sekunder |
| Gjennomgang etter oppdatering | Exit 0; ingen feil eller advarsler |
| Uendret guide | Identiske byte før og etter README-oppdatering |
| Kjør igjen | Exit 0; identiske hasher for alle oversettelsesfiler |

Dette er individuelle kjøretidsmålinger, ikke ytelsesgarantier. Oppsettstid er ekskludert; leverandørfakturering ble ikke målt. Et uendret kjør kan fortsatt utføre en helsesjekk av leverandøren.

Undersøk [opprinnelig oversettelse](../../assets/demo/before.txt), [oppdatert oversettelse](../../assets/demo/after.txt), [komplett oversettelsesdiff](../../assets/demo/update.diff), [utdatert gjennomgang](../../assets/demo/review-stale.txt), [endelig gjennomgang](../../assets/demo/review-after.txt), og [kjøringsdetaljer](../../assets/demo/results.json). Fullstendig filoversettelse kan endre annen ordlyd, som den innfangede diffen viser. Begge tekstartefaktene beholder den genererte ansvarsfraskrivelsen.

Menneskelig gjennomgang er fortsatt viktig: den innfangede oppdateringen bruker `[사용 가이드](guide.md)을`; den koreanske partikelen burde være `[사용 가이드](guide.md)를`. Tekstartifaktene beholder denne utdataen uendret i stedet for å vise en redigert oversettelse som modellens utdata. Den strukturelle gjennomgangen godkjennes til tross for dette ordlydsproblemet.

## 1. Forbered en liten mappe

Bruk Python 3.11–3.14 og [oppsett for virtuelt miljø](configuration.md#local-runtime-setup). Installer versjonen som ble brukt i dette eksemplet:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Last ned [README.txt](../../assets/demo/README.txt) og [guide.txt](../../assets/demo/guide.txt) til denne mappen, og lagre dem som `README.md` og `guide.md`. De er små fiktive prosjektdokumenter; ingen installasjon av applikasjonen er nødvendig.

README-en inneholder en kodeblokk og en lenke til `guide.md`. Den siste setningen er:

```text
Notes are saved locally.
```

Behold bare disse to kildefilene i denne mappen. Alle påfølgende kommandoer kjøres inne i `translation-demo` og fungerer i Bash og PowerShell.

## 2. Forhåndsvisning uten påloggingsinformasjon

```bash
translate -l "ko" -md --dry-run
```

Forhåndsvisningen estimerer oversettelsesarbeidet uten å kalle en modell eller skrive oversettelser. Token-estimater er ikke et faktureringsanslag. Første kjøring bør identifisere begge Markdown-filene som nytt arbeid.

## 3. Velg en leverandør og oversett

Konfigurer én leverandør ved hjelp av [konfigurasjonsveiledningen](configuration.md): Azure OpenAI, OpenAI eller Anthropic. OpenAI og Anthropic tekstoversettelse krever ikke en Azure-konto. Bildetjenester er ikke nødvendig for dette eksemplet.

Hvis du bruker en lokal `.env`-fil, legg `.env` til i denne mappens `.gitignore`. Oversettelseskall bruker leverandørkontoen din og kan medføre kostnader.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Åpne `translations/ko/README.md` og `translations/ko/guide.md`. Sjekk den koreanske ordlyden, kodeblokken, og lenken fra den oversatte README til den oversatte guiden. Utdataenes ordlyd varierer etter modell.

`co-op-review` sjekker ferskhet, struktur og lokale lenker. Et bestått resultat garanterer ikke språklig nøyaktighet. Løs eventuelle rapporterte feil før du fortsetter.

Registrer den vellykkede baseline med Git (konfigurer Git-identiteten din først om nødvendig):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Endre kilden

I `README.md`, erstatt `Notes are saved locally.` med:

```text
Notes are saved locally as Markdown files.
```

La `guide.md` være uendret. Kjør deretter:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Gjennomgangen bør rapportere at README-oversettelsen er foreldet og avslutte mislykket. Dette er den forventede mellomtilstanden. Forhåndsvisningen bør identifisere arbeid for den endrede README-filen.

## 5. Oppdater og undersøk diffen

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Undersøk den faktiske diffen: standard CLI oversetter på nytt den endrede filen, så modellen kan også revidere annen ordlyd i den filen. Den uendrede guiden bør ikke ha noen diff. Gjennomgangen bør ikke lenger rapportere README som foreldet; undersøk eventuelle andre funn i stedet for å ignorere dem.

Bevaring på blokknivå av menneskelige Markdown-redigeringer krever en valgfri leverandør for oversettelsestilstand i [Python-API](api.md). Den er ikke aktivert av disse CLI-kommandoene.

## 6. Kjør igjen uten endringer

Commit de oppdaterte kildene og oversettelsene:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Med nåværende oversettelser og uendret konfigurasjon, vil oversetteren hoppe over filene. Den siste Git-kommandoen bør gi ingen diff og avslutte vellykket.

## Neste steg

- [Oversett bare en README og åpne en pull request](github-actions.md#your-first-readme-translation-pr).
- [Velg CLI, Python-API eller MCP](workflows.md).
- [Rapporter et oversettelsesproblem uten koding](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).