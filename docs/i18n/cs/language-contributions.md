# Přispívání k vylepšení jazyka

Vaše jazykové znalosti mohou pomoci vylepšit Co-op Translator. Začněte příkladem, navrhovanou opravou a vysvětlením pomocí [formuláře pro zpětnou vazbu k překladu](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Nemusíte psát kód ani platit za spuštění modelu.

## Od hlášení k společnému vylepšení

1. Přispěvatel poskytne výňatek ze zdroje, jeho překlad a kontext.
2. Jazykový recenzent zkontroluje význam, přirozenost a zda návrh závisí na konkrétní lokalitě nebo kurzu.
3. Správce projektu rozhodne, zda oprava patří do zdrojového kurzu, sdílené jazykové instrukce, konfigurace terminologie nebo překladového kódu.
4. U sdíleného pravidla správce porovná výstupy před a po změně na nahlášeném příkladu a na nepříbuzných příkladech. Přispěvatelé mohou tyto výstupy zkontrolovat bez toho, aby nástroj sami spouštěli.
5. Výsledný PR propojí hlášení a ocení lidi, kteří poskytli příklady a recenzi. Nasazení nebo regenerace v repozitářích, které je využívají, je samostatný krok.

Hlášení automaticky nemění prompty ani znovu negeneruje překlady kurzů. Opravy specifické pro kurz by měly zůstat propojené s repozitářem kurzu. Nepředpokládejte, že ruční úprava přežije pozdější opětovný překlad; ověřte chování pro tento pracovní postup.

## Existující příklad: japonské Markdown odkazy

[Japonský soubor s instrukcemi](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) říká modelu, aby překládal text odkazu při zachování Markdown syntaxe a cíle odkazu. Například odkaz zapsaný jako `[text](URL)` nesmí být převeden na `「text」（URL）`.

Toto je cílený příklad jazykového pravidla podpořený ilustrací správného a nesprávného výstupu. Není to důkaz, že samotné instrukce promptu garantují správný Markdown.

[Generátor Markdown promptů](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) načítá `templates/language/<language_code>.md` použitím zmenšeného a oříznutého kódu jazyka. Pokud soubor neexistuje, použije společné instrukce. To popisuje cestu k Markdown promptu; nepředpokládejte, že každý obrázek nebo jiná překladová cesta používá stejné instrukce.

[Testy promptu](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) ověřují, že japonské instrukce jsou zahrnuty. To ověřuje sestavení promptu, nikoli kvalitu překladu.

## Co patří do jazykového pravidla?

Navrhněte úzkou, opakovatelnou opravu s ukázkou zdroje, očekávaným chováním a kontrapříkladem, kde pravidlo nesmí platit. Zachovejte význam, zástupné symboly, kód, URL a strukturu dokumentu. Vyhněte se přeměně stylové preference jedné osoby nebo terminologie jednoho kurzu na univerzální pravidlo.

[Současná implementace glosáře](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) chrání termíny před překladem. Není to slovník terminologie ze zdroje do cíle. Diskutujte chování nové terminologie dříve, než to slíbíte přispěvatelům.

## Příklad od komunity: hlášení o japonském názvu produktu

V [hlášení č. 527](https://github.com/Azure/co-op-translator/issues/527) @hyoshioka0128 identifikoval japonský překlad, který změnil název produktu `Co-op Translator` na `Co-op 翻訳`. Hlášení obsahovalo odkaz na postižený dokument a snímek obrazovky, což usnadnilo nalezení problému.

Přispěvatel také připojil [související PR kurzu](https://github.com/microsoft/AZD-for-beginners/pull/109). V diskusi k problému správce uznal hlášení a navrhl prozkoumat, proč se název změnil, včetně ochrany terminologie, chování glosáře a překladové cesty.

To ukazuje, jak malé hlášení může podpořit vyšetřování za rámec individuální úpravy znění. Není to ověřený před/po výsledek ani důkaz, že výše uvedené japonské instrukce pro Markdown-odkazy opravily tento problém s názvem produktu.

Můžete přispět stejným způsobem: sdílejte původní text, aktuální překlad, navrhovanou opravu a proč na tom záleží. Přidejte odkaz na dokument nebo snímek obrazovky, když je to užitečné. Nemusíte diagnostikovat příčinu ani psát prompt předtím, než to nahlásíte.

## Validace před přijetím pravidla

Použijte stejné zdrojové ukázky, revizi překladače, poskytovatele/model a nastavení generování pro základní a kandidátní běhy, přičemž měňte pouze navrhovanou instrukci. Zaznamenejte skutečnou změnu promptu a výstupy; opakujte příklady podle potřeby, abyste odlišili konzistentní efekt od variability výstupů. Zahrňte nahlášené selhání, kontrastní kontexty a příklady, které se již překládají správně.

| Vzorek | Zdroj/kontext | Výstup základního běhu | Výstup kandidátního běhu | Hodnocení recenzenta |
| --- | --- | --- | --- | --- |
| Nahlášené selhání | K doplnění | Nespuštěno | Nespuštěno | Čeká |
| Kontrapříklad | K doplnění | Nespuštěno | Nespuštěno | Čeká |
| Nepovlivněný příklad | K doplnění | Nespuštěno | Nespuštěno | Čeká |

Kontrolujte strukturální invarianty samostatně od jazykových posudků. Úspěšný test načtení promptu není hodnocení kvality a jedna přesně očekávaná věta není jediný platný překlad. Pokud chybí kontext, běhy modelu nebo jazyková revize, ponechte návrh jako čekající, místo abyste tvrdili, že problém je vyřešen.