# Bijdragen aan taalverbeteringen

Uw taalkennis kan helpen Co-op Translator te verbeteren. Begin met een voorbeeld, een voorgestelde correctie en een uitleg via het [formulier voor vertaalfeedback](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). U hoeft geen code te schrijven of te betalen voor een modelrun.

## Van een rapport naar een gezamenlijke verbetering

1. Een bijdrager levert een brontekstfragment, de vertaling daarvan en context.
2. Een taalbeoordelaar controleert betekenis, natuurlijkheid en of de suggestie afhankelijk is van een specifieke locale of cursus.
3. Een beheerder beslist of de correctie thuishoort in de broncursus, een gedeelde taalinstructie, terminologieconfiguratie of vertaalcode.
4. Voor een gedeelde regel vergelijkt een beheerder de uitvoer vóór en na de wijziging voor het gerapporteerde voorbeeld en voor niet-verwante voorbeelden. Bijdragers kunnen deze uitvoer beoordelen zonder het hulpmiddel zelf te hoeven uitvoeren.
5. De resulterende PR koppelt het rapport en vermeldt de personen die voorbeelden en beoordeling hebben geleverd. Deployment of regeneratie in consumerende repositories is een aparte stap.

Een rapport verandert niet automatisch prompts of genereert cursusvertalingen opnieuw. Cursus-specifieke correcties moeten verbonden blijven met de cursusrepository. Ga er niet van uit dat een handmatige wijziging een latere hervertaling overleeft; bevestig het gedrag voor die workflow.

## Bestaand voorbeeld: Japanse Markdown-links

Het [Japans instructiebestand](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) vertelt het model om linktekst te vertalen terwijl de Markdown-syntaxis en de linkbestemming behouden blijven. Bijvoorbeeld, een link geschreven als `[text](URL)` mag niet `「text」（URL）` worden.

Dit is een gericht voorbeeld van een taalregel ondersteund door een illustratie van correcte en onjuiste uitvoer. Het is geen bewijs dat promptinstructies op zichzelf correcte Markdown garanderen.

De [Markdown prompt builder](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) laadt `templates/language/<language_code>.md` met een in kleine letters omgezette, getrimde taalcode. Als er geen bestand bestaat, gebruikt het de algemene instructies. Dit beschrijft het pad voor de Markdown-prompt; ga er niet van uit dat elk afbeeldings- of ander vertaalpad dezelfde instructies gebruikt.

De [prompt tests](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) controleren of de Japanse instructies zijn opgenomen. Dat verifieert de opbouw van de prompt, niet de vertaalkwaliteit.

## Wat hoort thuis in een taalregel?

Stel een nauwkeurige, herhaalbare correctie voor met een bronvoorbeeld, verwacht gedrag en een tegenvoorbeeld waar de regel niet van toepassing mag zijn. Behoud betekenis, placeholders, code, URL's en documentstructuur. Voorkom dat iemands stijlvoorkeur of de terminologie van één cursus een universele regel wordt.

De huidige [glossary-implementatie](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) beschermt termen tegen vertaling. Het is geen terminologiewoordenboek van bron naar doel. Bespreek nieuw terminologiegedrag voordat u het aan bijdragers belooft.

## Voorbeeld uit de community: een Japans rapport over een productnaam

In [rapport #527](https://github.com/Azure/co-op-translator/issues/527), @hyoshioka0128 identificeerde een Japanse vertaling die de productnaam `Co-op Translator` veranderde in `Co-op 翻訳`. Het rapport bevatte een link naar het getroffen document en een screenshot, waardoor het probleem gemakkelijk te lokaliseren was.

De bijdrager koppelde ook een [gerelateerde cursus-PR](https://github.com/microsoft/AZD-for-beginners/pull/109). In de discussie erkende de beheerder het rapport en stelde voor te onderzoeken waarom de naam veranderde, inclusief terminologiebescherming, glossariumgedrag en het vertaalpad.

Dit toont aan hoe een klein rapport onderzoek kan ondersteunen dat verder gaat dan een individuele woordkeuzecorrectie. Het is geen geverifieerd voor/na-resultaat of bewijs dat de hierboven genoemde Japanse instructies voor Markdown-links dit productnaamprobleem hebben opgelost.

U kunt op dezelfde manier bijdragen: deel de originele tekst, de huidige vertaling, de voorgestelde correctie en waarom het belangrijk is. Voeg indien nuttig een documentlink of screenshot toe. U hoeft niet de oorzaak te diagnosticeren of een prompt te schrijven voordat u het rapporteert.

## Validatie voordat een regel wordt aangenomen

Gebruik dezelfde bronvoorbeelden, vertalerrevisie, provider/model en generatie-instellingen voor baseline- en kandidaat-runs, waarbij alleen de voorgestelde instructie verandert. Leg de daadwerkelijke promptwijziging en uitvoer vast; herhaal voorbeelden indien nodig om een consistent effect te onderscheiden van uitvoervariabiliteit. Neem de gerapporteerde fout op, contrasterende contexten en voorbeelden die al correct vertalen.

| Voorbeeld | Bron/context | Baseline output | Candidate output | Reviewer assessment |
| --- | --- | --- | --- | --- |
| Gerapporteerde fout | Te verzamelen | Niet uitgevoerd | Niet uitgevoerd | In afwachting |
| Tegenvoorbeeld | Te verzamelen | Niet uitgevoerd | Niet uitgevoerd | In afwachting |
| Ongeïnvloed voorbeeld | Te verzamelen | Niet uitgevoerd | Niet uitgevoerd | In afwachting |

Controleer structurele invarianties los van taalkundige beoordelingen. Een geslaagde test voor het laden van prompts is geen kwaliteitsbeoordeling, en één exact verwachte zin is niet de enige geldige vertaling. Als context, modelruns of taalbeoordeling ontbreken, houd het voorstel in afwachting in plaats van te beweren dat het probleem is opgelost.