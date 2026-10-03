# Bidrag til sproglige forbedringer

Din sprogkundskab kan hjælpe med at forbedre Co-op Translator. Start med et eksempel, en foreslået rettelse og en forklaring ved hjælp af [oversættelsesfeedbackformularen](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Du behøver ikke skrive kode eller betale for en modelkørsel.

## Fra en rapport til en fælles forbedring

1. En bidragsyder leverer et kildeuddrag, dets oversættelse og kontekst.
2. En sprogansvarlig tjekker betydning, naturlighed og om forslaget afhænger af en bestemt lokalitet eller kursus.
3. En vedligeholder beslutter, om rettelsen hører hjemme i kildekurset, i en delt sprogvejledning, i terminologikonfigurationen eller i oversættelseskoden.
4. For en delt regel sammenligner en vedligeholder output før og efter ændringen på det rapporterede eksempel og på ikke-relaterede eksempler. Bidragsydere kan gennemse disse output uden selv at køre værktøjet.
5. Den resulterende PR linker til rapporten og krediterer de personer, der leverede eksempler og review. Udrulning eller regenerering i de forbrugende repositories er et separat trin.

En rapport ændrer ikke automatisk prompts eller regenererer kursusoversættelser. Kursusspecifikke rettelser bør forblive forbundet med kursusrepositoryet. Antag ikke, at en manuel redigering overlever senere genoversættelse; bekræft adfærden for den arbejdsgang.

## Eksisterende eksempel: Japanske Markdown-links

The [japansk instruktionsfil](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) fortæller modellen at oversætte linktekst samtidig med at bevare Markdown-syntaks og linkdestinationen. For eksempel må et link skrevet som `[text](URL)` ikke blive til `「text」（URL）`.

Dette er et fokuseret eksempel på en sprogregel bakket op af en illustration af korrekt og ukorrekt output. Det er ikke bevis for, at promptinstruktioner alene garanterer korrekt Markdown.

The [Markdown-promptbyggeren](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) indlæser `templates/language/<language_code>.md` ved at bruge en sprogkode, som er gjort med små bogstaver og trimmet. Hvis der ikke findes en fil, bruger den de fælles instruktioner. Dette beskriver Markdown-promptstien; antag ikke, at hvert billede eller anden oversættelsessti bruger de samme instruktioner.

The [prompttestene](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) sikrer, at de japanske instruktioner er inkluderet. Det bekræfter promptsamlingen, ikke oversættelseskvaliteten.

## Hvad hører hjemme i en sprogregel?

Foreslå en snæver, gentagelig rettelse med et kildeeksempel, forventet adfærd og et modeksempel, hvor reglen ikke må gælde. Bevar betydning, pladsholdere, kode, URL'er og dokumentstruktur. Undgå at gøre én persons stilpræference eller et enkelt kursus' terminologi til en universel regel.

The current [glossarimplementeringen](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) beskytter termer mod oversættelse. Det er ikke en kilde-til-mål terminologidatabase. Diskutér ny terminologiadfærd, inden du lover det til bidragsydere.

## Fællesskabseksempel: en japansk rapport om produktnavn

I [rapport #527](https://github.com/Azure/co-op-translator/issues/527) identificerede @hyoshioka0128 en japansk oversættelse, der ændrede produktnavnet `Co-op Translator` til `Co-op 翻訳`. Rapporten inkluderede et link til det berørte dokument og et screenshot, hvilket gjorde problemet nemt at lokalisere.

Bidragsyderen linkede også til en [relateret kursus-PR](https://github.com/microsoft/AZD-for-beginners/pull/109). I issues-diskussionen anerkendte vedligeholderen rapporten og foreslog at undersøge, hvorfor navnet ændredes, inklusiv terminologibeskyttelse, glossaradfærd og oversættelsesstien.

Dette viser, hvordan en lille rapport kan understøtte en undersøgelse ud over en individuel ordlydsrettelse. Det er ikke et verificeret før/efter-resultat eller bevis for, at de japanske Markdown-linkinstruktioner ovenfor løste dette produktnavneproblem.

Du kan bidrage på samme måde: del den originale tekst, den nuværende oversættelse, den foreslåede rettelse og hvorfor det betyder noget. Tilføj et dokumentlink eller screenshot, når det er nyttigt. Du behøver ikke diagnosticere årsagen eller skrive en prompt før du rapporterer det.

## Validering før vedtagelse af en regel

Brug de samme kildeprøver, oversætterrevision, udbyder/model og genereringsindstillinger for baseline- og kandidatkørsler, og ændr kun den foreslåede instruktion. Registrer den faktiske promptændring og output; gentag eksempler efter behov for at skelne en konsekvent effekt fra outputvariabilitet. Inkluder den rapporterede fejl, kontrasterende kontekster og eksempler, der allerede oversætter korrekt.

| Prøve | Kilde/kontekst | Baseline-output | Kandidat-output | Anmelders vurdering |
| --- | --- | --- | --- | --- |
| Rapportet fejl | Til indsamling | Ikke kørt | Ikke kørt | Afventer |
| Modeksempel | Til indsamling | Ikke kørt | Ikke kørt | Afventer |
| Upåvirket eksempel | Til indsamling | Ikke kørt | Ikke kørt | Afventer |

Kontroller strukturelle invarianter separat fra sproglige vurderinger. En vellykket promptindlæsningstest er ikke en kvalitetsvurdering, og én nøjagtig forventet sætning er ikke den eneste gyldige oversættelse. Hvis kontekst, modelkørsler eller sprogvurdering mangler, behold forslaget afventende i stedet for at påstå, at problemet er løst.