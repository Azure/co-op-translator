# Bidra med språklige forbedringer

Din språkkompetanse kan hjelpe til med å forbedre Co-op Translator. Start med et eksempel, et forslag til rettelse og en forklaring ved å bruke [oversettelses-tilbakemeldingsskjemaet](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Du trenger ikke å skrive kode eller betale for en modellkjøring.

## Fra en rapport til en delt forbedring

1. En bidragsyter leverer et kildeutdrag, dets oversettelse og kontekst.
2. En språkansvarlig sjekker mening, naturlighet og om forslaget avhenger av en bestemt lokal variant eller kurs.
3. En vedlikeholder avgjør om fiksen hører hjemme i kildekursen, i felles språkinstruksjon, i terminologikonfigurasjonen eller i oversettelseskoden.
4. For en delt regel sammenligner en vedlikeholder utdata før og etter endringen på det rapporterte eksempelet og på ikke-relaterte eksempler. Bidragsytere kan gjennomgå disse utdataene uten å kjøre verktøyet selv.
5. Den resulterende PR-en lenker til rapporten og krediterer de som ga eksempler og gjennomgang. Distribusjon eller regenerering i de avhengige repositoriene er et eget steg.

En rapport endrer ikke automatisk promptene eller regenererer kursoversettelser. Kurs-spesifikke korreksjoner bør forbli knyttet til kurs-repositoriet. Ikke anta at en manuell redigering overlever senere retranslasjon; bekreft oppførselen for den arbeidsflyten.

## Eksisterende eksempel: japanske Markdown-lenker

Filen [Japanese instruction file](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) instruerer modellen til å oversette lenketekst samtidig som den bevarer Markdown-syntaks og lenkedestinasjon. For eksempel må en lenke skrevet som `[text](URL)` ikke bli `「text」（URL）`.

Dette er et fokusert eksempel på en språkregel støttet av en illustrasjon av korrekt og ukorrekt utdata. Det er ikke bevis for at prompt-instruksjoner alene garanterer korrekt Markdown.

[Markdown-promptbyggeren](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) laster `templates/language/<language_code>.md` ved å bruke en språkkode som er gjort med små bokstaver og trimmet. Hvis ingen fil finnes, bruker den de vanlige instruksjonene. Dette beskriver Markdown-promptens bane; ikke anta at hvert bilde eller annen oversettelsesbane bruker de samme instruksjonene.

[Prompt-testene](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) sjekker at de japanske instruksjonene er inkludert. Det verifiserer sammensetningen av prompten, ikke oversettelseskvaliteten.

## Hva hører hjemme i en språkregel?

Foreslå en smal, repeterbar korreksjon med et kildeeksempel, forventet oppførsel og et moteksempel hvor regelen ikke skal gjelde. Bevar mening, plassholdere, kode, URLer og dokumentstruktur. Unngå å gjøre en persons stilpreferanse eller terminologi fra ett kurs til en universell regel.

Den nåværende [glossarimplementeringen](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) beskytter termer mot oversettelse. Den er ikke en kilde-til-mål terminologidatabase. Diskuter ny terminologioppførsel før du lover det til bidragsytere.

## Fellesskapseksempel: en japansk rapport om produktnavn

I [rapport #527](https://github.com/Azure/co-op-translator/issues/527) identifiserte @hyoshioka0128 en japansk oversettelse som endret produktnavnet `Co-op Translator` til `Co-op 翻訳`. Rapporten inkluderte en lenke til det berørte dokumentet og et skjermbilde, noe som gjorde problemet lett å finne.

Bidragsyteren lenket også en [relatert kurs-PR](https://github.com/microsoft/AZD-for-beginners/pull/109). I diskusjonen anerkjente vedlikeholderen rapporten og foreslo å undersøke hvorfor navnet endret seg, inkludert terminologibeskyttelse, glossarens oppførsel og oversettelsesbanen.

Dette viser hvordan en liten rapport kan støtte undersøkelse utover en individuell ordvalgsrettelse. Det er ikke et verifisert før/etter-resultat eller bevis på at de japanske Markdown-lenkeinstruksjonene ovenfor løste dette produktnavnproblemet.

Du kan bidra på samme måte: del originalteksten, nåværende oversettelse, foreslått korreksjon og hvorfor det er viktig. Legg til en dokumentlenke eller skjermbilde når det er nyttig. Du trenger ikke å diagnostisere årsaken eller skrive en prompt før du rapporterer det.

## Validering før adopsjon av en regel

Bruk de samme kildesampelene, oversetterrevisjonen, leverandør/modellen og genereringsinnstillingene for baseline- og kandidatkjøringer, og endre kun den foreslåtte instruksjonen. Registrer den faktiske promptendringen og utdataene; gjenta eksempler når det er nødvendig for å skille en konsistent effekt fra variasjon i utdata. Inkluder den rapporterte feilen, kontrasterende kontekster og eksempler som allerede oversettes korrekt.

| Eksempel | Kilde/kontekst | Baseline-utdata | Kandidat-utdata | Gjennomlesers vurdering |
| --- | --- | --- | --- | --- |
| Rapportert feil | Skal samles | Ikke kjørt | Ikke kjørt | Avventer |
| Moteksempel | Skal samles | Ikke kjørt | Ikke kjørt | Avventer |
| Upåvirket eksempel | Skal samles | Ikke kjørt | Ikke kjørt | Avventer |

Sjekk strukturelle invariantene separat fra språklige vurderinger. En vellykket test av prompt-innlasting er ikke en kvalitetsvurdering, og én nøyaktig forventet setning er ikke den eneste gyldige oversettelsen. Hvis kontekst, modellkjøringer eller språkvurdering mangler, la forslaget forbli avventende i stedet for å hevde at problemet er løst.