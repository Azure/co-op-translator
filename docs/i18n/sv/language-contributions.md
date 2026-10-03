# Bidra till språkförbättringar

Din språkkunskap kan hjälpa till att förbättra Co-op Translator. Börja med ett exempel, en föreslagen rättelse och en förklaring via [översättningsfeedbackformuläret](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Du behöver inte skriva kod eller betala för en modellkörning.

## Från en rapport till en gemensam förbättring

1. En bidragsgivare lämnar ett källutdrag, dess översättning och kontext.
2. En språkgranskare kontrollerar betydelse, naturlighet och om förslaget är beroende av en särskild lokal eller kurs.
3. En underhållare avgör om åtgärden hör hemma i källkursen, en gemensam språkinstruktion, terminologikonfiguration eller översättningskod.
4. För en gemensam regel jämför en underhållare utdata före och efter ändringen på det rapporterade exemplet och på orelaterade exempel. Bidragsgivare kan granska dessa utdata utan att själva köra verktyget.
5. Den resulterande PR:en länkar till rapporten och ger erkännande åt de som bidrog med exempel och granskning. Distribution eller regenerering i konsumerande repositories är ett separat steg.

En rapport ändrar inte automatiskt prompts eller regenererar kursöversättningar. Kurs-specifika korrigeringar bör förbli kopplade till kursens repository. Förutsätt inte att en manuell redigering överlever en senare återöversättning; kontrollera hur det fungerar för det arbetsflödet.

## Existerande exempel: japanska Markdown-länkar

Den [japanska instruktionsfilen](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) talar om för modellen att översätta länktexten samtidigt som Markdown-syntaxen och länkdestinationen bevaras. Till exempel får en länk skriven som `[text](URL)` inte bli `「text」（URL）`.

Detta är ett fokuserat exempel på en språkregel som stöds av en illustration av korrekt och felaktigt utdata. Det är inte bevis för att promptinstruktioner ensamma garanterar korrekt Markdown.

Den [Markdown prompt builder](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) laddar `templates/language/<language_code>.md` med en språkkod som är gemener och trimmad. Om ingen fil finns använder den de gemensamma instruktionerna. Detta beskriver Markdown-promptens sökväg; anta inte att varje bild eller annan översättningsväg använder samma instruktioner.

De [prompt tester](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) kontrollerar att de japanska instruktionerna ingår. Det verifierar promptens sammansättning, inte översättningskvaliteten.

## Vad hör hemma i en språkregel?

Föreslå en snäv, upprepbar korrigering med ett källexempel, förväntat beteende och ett motexempel där regeln inte ska tillämpas. Bevara betydelse, platshållare, kod, URL:er och dokumentstruktur. Undvik att göra en persons stilpreferens eller terminologi i en enskild kurs till en universell regel.

Den nuvarande [glossary implementation](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) skyddar termer från översättning. Den är inte en käll-till-mål-terminologidatabas. Diskutera nytt terminologibeteende innan ni lovar det till bidragsgivare.

## Exempel från communityn: en japansk rapport om produktnamn

I [rapport #527](https://github.com/Azure/co-op-translator/issues/527) identifierade @hyoshioka0128 en japansk översättning som ändrade produktnamnet `Co-op Translator` till `Co-op 翻訳`. Rapporten innehöll en länk till det påverkade dokumentet och en skärmbild, vilket gjorde problemet lätt att lokalisera.

Bidragsgivaren länkade också en [relaterad kurs-PR](https://github.com/microsoft/AZD-for-beginners/pull/109). I diskussionen i ärendet erkände underhållaren rapporten och föreslog att undersöka varför namnet ändrades, inklusive skydd av terminologi, glossarens beteende och översättningsvägen.

Detta visar hur en liten rapport kan stödja utredning bortom en enskild ordalydelsekorrigering. Det är inte ett verifierat före/efter-resultat eller bevis för att de japanska Markdown-länkinstruktionerna ovan åtgärdade detta produktnamnsproblem.

Du kan bidra på samma sätt: dela originaltexten, den aktuella översättningen, föreslagen rättelse och varför det spelar roll. Lägg till en dokumentslänk eller skärmbild när det är användbart. Du behöver inte diagnostisera orsaken eller skriva en prompt innan du rapporterar det.

## Validering innan en regel antas

Använd samma källprover, översättarrevision, leverantör/modell och genereringsinställningar för baseline- och kandidatkörningar, ändra endast den föreslagna instruktionen. Dokumentera den faktiska promptändringen och utdata; upprepa exempel vid behov för att skilja en konsekvent effekt från variationsbrus i utdata. Inkludera det rapporterade felet, kontrasterande kontexter och exempel som redan översätts korrekt.

| Exempel | Källa/kontext | Baseline output | Candidate output | Reviewer assessment |
| --- | --- | --- | --- | --- |
| Rapporterat fel | Att samla in | Ej körd | Ej körd | Avvaktar |
| Motexempel | Att samla in | Ej körd | Ej körd | Avvaktar |
| Opåverkat exempel | Att samla in | Ej körd | Ej körd | Avvaktar |

Kontrollera strukturella invarianta egenskaper separat från språkliga bedömningar. Ett lyckat test för inläsning av prompt är inte en kvalitetsutvärdering, och en exakt förväntad mening är inte den enda giltiga översättningen. Om kontext, modellkörningar eller språkgranskning saknas, håll förslaget avvaktande istället för att hävda att problemet är åtgärdat.