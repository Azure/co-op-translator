# Prispievanie jazykových vylepšení

Vaše jazykové znalosti môžu pomôcť zlepšiť Co-op Translator. Začnite príkladom, navrhovanou opravou a vysvetlením pomocou [formulára spätnej väzby k prekladom](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Nemusíte písať kód ani platiť za spustenie modelu.

## Od hlásenia k spoločnému vylepšeniu

1. Prispievateľ poskytne úryvok zdrojového textu, jeho preklad a kontext.
2. Jazykový recenzent skontroluje význam, prirodzenosť a či návrh závisí od konkrétnej lokality alebo kurzu.
3. Správca rozhodne, či oprava patrí do zdrojového kurzu, spoločného jazykového pokynu, konfigurácie terminológie alebo do kódu prekladu.
4. Pri spoločnom pravidle správca porovná výstupy pred zmenou a po zmene na nahlásenom príklade a na nesúvisiacich príkladoch. Prispievatelia môžu tieto výstupy skontrolovať bez toho, aby nástroj spúšťali sami.
5. Výsledný PR odkazuje na hlásenie a pripisuje uznanie ľuďom, ktorí poskytli príklady a recenziu. Nasadenie alebo opätovné generovanie v konzumných repozitároch je samostatný krok.

Hlásenie automaticky nezasiahne do promptov ani negeneruje preklady kurzu znova. Opravy špecifické pre kurz by mali zostať prepojené s repozitárom kurzu. Nepredpokladajte, že manuálna úprava prežije neskoršie prekládanie; overte správanie pre tento pracovný postup.

## Existujúci príklad: japonské odkazy v Markdown

The [japonský inštrukčný súbor](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) hovorí modelu, aby prekladal text odkazu pri zachovaní Markdown syntaxe a cieľu odkazu. Napríklad odkaz napísaný ako `[text](URL)` nesmie byť premenený na `「text」（URL）`.

Toto je zameraný príklad jazykového pravidla podložený ukážkou správneho a nesprávneho výstupu. Nie je to dôkaz, že samotné inštrukcie v prompte zaručujú správny Markdown.

The [tvorca Markdown promptov](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) načíta `templates/language/<language_code>.md` použitím malých písmen a orezaného kódu jazyka. Ak súbor neexistuje, použije spoločné inštrukcie. Toto popisuje cestu promptu pre Markdown; nepredpokladajte, že každý obrázok alebo iná prekladová cesta používa rovnaké inštrukcie.

The [testy promptov](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) kontrolujú, či sú japonské inštrukcie zahrnuté. To overuje zostavenie promptu, nie kvalitu prekladu.

## Čo patrí do jazykového pravidla?

Navrhnite úzku, opakovateľnú opravu s príkladom zdroja, očakávaným správaním a protípríkladom, kde pravidlo nesmie platiť. Zachovajte význam, zástupné symboly, kód, URL a štruktúru dokumentu. Vyhnite sa tomu, aby ste preferenciu štýlu jednej osoby alebo terminológiu jedného kurzu premenili na všeobecné pravidlo.

Aktuálna [implementácia glosára](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) chráni termíny pred prekladom. Nie je to slovník terminológie zo zdrojového do cieľového jazyka. Pred sľubovaním správania novej terminológie to prediskutujte s prispievateľmi.

## Príklad komunity: hlásenie o názve produktu v japončine

V [hlásení č. 527](https://github.com/Azure/co-op-translator/issues/527) identifikoval @hyoshioka0128 japonský preklad, ktorý zmenil názov produktu `Co-op Translator` na `Co-op 翻訳`. Hlásenie obsahovalo odkaz na dotknutý dokument a snímku obrazovky, čo uľahčilo lokalizovanie problému.

Prispievateľ tiež pripojil [súvisiaci PR kurzu](https://github.com/microsoft/AZD-for-beginners/pull/109). V diskusii k issue správca potvrdil prijatie hlásenia a navrhol preskúmať, prečo sa názov zmenil, vrátane ochrany terminológie, správania glosára a prekladovej cesty.

To ukazuje, ako malé hlásenie môže podporiť vyšetrovanie presahujúce opravu individuálneho znenia. Nie je to overený výsledok pred/po ani dôkaz, že vyššie uvedené japonské inštrukcie pre Markdown-odkazy vyriešili tento problém s názvom produktu.

Môžete prispieť rovnako: zdieľajte pôvodný text, aktuálny preklad, navrhovanú opravu a dôvod, prečo je to dôležité. Pridajte odkaz na dokument alebo snímku obrazovky, keď je to užitočné. Nemusíte diagnostikovať príčinu ani písať prompt pred jeho nahlásením.

## Validácia pred prijatím pravidla

Použite rovnaké zdrojové vzorky, revíziu prekladu, poskytovateľa/model a nastavenia generovania pre východiskové i kandidátne spustenia, pričom zmeňte iba navrhovanú inštrukciu. Zaznamenajte skutočnú zmenu promptu a výstupy; opakujte príklady podľa potreby, aby ste odlíšili konzistentný efekt od variability výstupov. Zahrňte nahlásené zlyhanie, kontrastné kontexty a príklady, ktoré sa už prekladajú správne.

| Vzorka | Zdroj/Kontext | Východiskový výstup | Kandidátny výstup | Posúdenie recenzenta |
| --- | --- | --- | --- | --- |
| Nahlásené zlyhanie | Na zozbieranie | Nepustené | Nepustené | Čaká sa |
| Protípríklad | Na zozbieranie | Nepustené | Nepustené | Čaká sa |
| Neovplyvnený príklad | Na zozbieranie | Nepustené | Nepustené | Čaká sa |

Skontrolujte štrukturálne invarianty oddelene od jazykových posudkov. Úspešný test načítania promptu nie je hodnotením kvality a jedna presne očakávaná veta nie je jediným platným prekladom. Ak chýba kontext, spustenia modelu alebo jazyková recenzia, ponechajte návrh v stave čakajúcom namiesto tvrdenia, že problém je vyriešený.