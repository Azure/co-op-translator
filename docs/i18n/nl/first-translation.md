# Vertaal, bewerk en beoordeel een klein project

Begin met twee korte Markdown-bestanden en één doeltaal. Je ziet waar vertalingen worden geschreven, wat er gebeurt als de bron verandert en hoe je het resultaat controleert.

## Opgenomen resultaten

Het voorbeeld werd uitgevoerd op 19 september 2026 met Co-op Translator 0.21.0 en Azure OpenAI (`gpt-5-mini`). De ongemodificeerde CLI-commando's werden aangeroepen via Click's `CliRunner` met het gebouwde wheel en de bestaande Python-afhankelijkheden.

| Stap | Resultaat |
| --- | --- |
| Voorbeeldweergave | Exit 0; geen modelvertaling opgevraagd |
| Initiële vertaling | Exit 0; 27.36 seconden |
| Initiële beoordeling | Exit 0 |
| README bewerken en beoordelen | Exit 1; verouderde vertaling gedetecteerd |
| Vertaling bijwerken | Exit 0; 22.17 seconden |
| Beoordeling na update | Exit 0; geen fouten of waarschuwingen |
| Ongeraakte gids | Identieke bytes vóór en na README-update |
| Opnieuw uitvoeren | Exit 0; identieke hashes voor alle vertaalbestanden |

Dit zijn metingen van individuele runs, geen prestatiegaranties. Opstarttijd is uitgesloten; facturering door de provider is niet gemeten. Een ongewijzigde run kan nog steeds een gezondheidscontrole van de provider uitvoeren.

Inspecteer de [initiële vertaling](../../assets/demo/before.txt), [bijgewerkte vertaling](../../assets/demo/after.txt), [volledige vertaaldiff](../../assets/demo/update.diff), [verouderde beoordeling](../../assets/demo/review-stale.txt), [definitieve beoordeling](../../assets/demo/review-after.txt), en [uitvoeringsdetails](../../assets/demo/results.json). Een volledige bestandvertaling kan andere bewoordingen wijzigen, zoals de vastgelegde diff aantoont. Beide tekstartefacten behouden de gegenereerde disclaimer.

Menselijke beoordeling blijft belangrijk: de vastgelegde update gebruikt `[사용 가이드](guide.md)을`; het Koreaanse deeltje zou `[사용 가이드](guide.md)를` moeten zijn. De tekstartefacten laten deze output onaangeroerd in plaats van een bewerkte vertaling als modeluitvoer te tonen. De structurele beoordeling slaagt ondanks dit formuleringprobleem.

## 1. Bereid een kleine map voor

Gebruik Python 3.11–3.14 en de [opzet van de virtuele omgeving](configuration.md#local-runtime-setup). Installeer de versie die voor dit voorbeeld is gebruikt:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Download [README.txt](../../assets/demo/README.txt) en [guide.txt](../../assets/demo/guide.txt) in deze map en sla ze op als `README.md` en `guide.md`. Het zijn kleine fictieve projectdocumenten; er is geen installatie van een applicatie nodig.

De README bevat een codeblok en een link naar `guide.md`. De laatste zin ervan is:

```text
Notes are saved locally.
```

Houd alleen deze twee brondocumenten in deze map. Alle volgende opdrachten worden uitgevoerd binnen `translation-demo` en werken in Bash en PowerShell.

## 2. Voorvertoning zonder inloggegevens

```bash
translate -l "ko" -md --dry-run
```

De voorvertoning schat het vertaalwerk zonder een model aan te roepen of vertalingen te schrijven. Tokenramingen zijn geen factuurofferte. De eerste run zou beide Markdown-bestanden als nieuw werk moeten identificeren.

## 3. Kies een provider en vertaal

Configureer één provider met behulp van de [configuratiehandleiding](configuration.md): Azure OpenAI, OpenAI of Anthropic. Tekstvertaling met OpenAI en Anthropic vereist geen Azure-account. Beeldservices zijn voor dit voorbeeld niet nodig.

Als je een lokaal `.env`-bestand gebruikt, voeg dan `.env` toe aan de `.gitignore` van deze map. Vertaaloproepen gebruiken je provideraccount en kunnen kosten met zich meebrengen.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Open `translations/ko/README.md` en `translations/ko/guide.md`. Controleer de Koreaanse bewoording, het codeblok en de link van de vertaalde README naar de vertaalde gids. De uiteindelijke formulering varieert per model.

`co-op-review` controleert actualiteit, structuur en lokale links. Een geslaagde uitslag certificeert geen taalkundige nauwkeurigheid. Los eventuele gerapporteerde fouten op voordat je verdergaat.

Leg de succesvolle basislijn vast met Git (configureer eerst je Git-identiteit indien nodig):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Wijzig de bron

Vervang in `README.md` `Notes are saved locally.` door:

```text
Notes are saved locally as Markdown files.
```

Laat `guide.md` ongewijzigd. Voer daarna uit:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

De beoordeling zou moeten rapporteren dat de README-vertaling verouderd is en met een foutcode moeten beëindigen. Dit is de verwachte tussenstatus. De voorvertoning zou werk moeten identificeren voor de gewijzigde README.

## 5. Werk bij en inspecteer de diff

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Inspecteer de werkelijke diff: de standaard-CLI vertaalt het gewijzigde bestand opnieuw, zodat het model ook andere bewoordingen in dat bestand kan herzien. De ongewijzigde gids zou geen diff moeten hebben. De beoordeling mag README niet langer als verouderd rapporteren; onderzoek andere bevindingen in plaats van ze te negeren.

Behoud op blokniveau van menselijke Markdown-bewerkingen vereist een optionele vertaalstatusprovider in de [Python API](api.md). Deze is niet ingeschakeld door deze CLI-commando's.

## 6. Draai opnieuw zonder wijzigingen

Commit de bijgewerkte bron en vertaling:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Met de huidige vertalingen en ongewijzigde configuratie slaat de vertaler de bestanden over. Het laatste Git-commando zou geen diff moeten opleveren en succesvol moeten afsluiten.

## Volgende stappen

- [Vertaal alleen een README en open een pull request](github-actions.md#your-first-readme-translation-pr).
- [Kies CLI, Python API of MCP](workflows.md).
- [Meld een vertaalprobleem zonder te programmeren](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).