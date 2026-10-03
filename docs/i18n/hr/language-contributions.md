# Doprinos poboljšanjima jezika

Vaše znanje jezika može pomoći u poboljšanju Co-op Translatora. Počnite s primjerom, predloženom ispravkom i objašnjenjem koristeći [obrazac za povratne informacije o prijevodu](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Ne morate pisati kod niti plaćati za pokretanje modela.

## Od izvještaja do zajedničkog poboljšanja

1. Suradnik dostavi izvadak izvornog teksta, njegov prijevod i kontekst.
2. Recenzent jezika provjerava značenje, prirodnost i ovisi li prijedlog o određenoj lokalizaciji ili tečaju.
3. Održavatelj odlučuje pripada li ispravak izvornom tečaju, zajedničkoj jezičnoj uputi, konfiguraciji terminologije ili kodu za prijevod.
4. Za zajedničko pravilo, održavatelj uspoređuje izlaze prije i nakon promjene na prijavljenom primjeru i na nevezanim primjerima. Suradnici mogu pregledati te izlaze bez samostalnog pokretanja alata.
5. Rezultirajući PR povezuje izvještaj i navodi osobe koje su pružile primjere i pregled. Implementacija ili ponovno generiranje u repozitorijima koji koriste promjenu je zaseban korak.

Izvještaj automatski ne mijenja upute (prompts) niti ne regenerira prijevode tečaja. Ispravci specifični za tečaj trebaju ostati povezani s repozitorijem tečaja. Nemojte pretpostavljati da će ručna izmjena preživjeti kasniji ponovni prijevod; provjerite ponašanje za taj tijek rada.

## Postojeći primjer: japanske Markdown poveznice

[Datoteka s uputama za japanski](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) govori modelu da prevede tekst poveznice pritom zadržavajući Markdown sintaksu i odredište poveznice. Na primjer, poveznica zapisana kao `[text](URL)` ne smije postati `「text」（URL）`.

Ovo je usmjereni primjer jezičnog pravila potkrijepljen ilustracijom ispravnog i neispravnog izlaza. To nije dokaz da same upute (prompts) jamče ispravan Markdown.

[Graditelj Markdown prompta](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) učitava `templates/language/<language_code>.md` koristeći jezični kod malim slovima i bez razmaka na početku i kraju. Ako datoteka ne postoji, koristi zajedničke upute. Ovo opisuje putanju Markdown prompta; nemojte pretpostavljati da svaka slika ili neki drugi put prijevoda koristi iste upute.

[Testovi prompta](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) provjeravaju da su japanske upute uključene. To potvrđuje sastavljanje prompta, ne kvalitetu prijevoda.

## Što treba biti u jezičnom pravilu?

Predložite usku, ponovljivu ispravku s izvornim primjerom, očekivanim ponašanjem i kontraprimjerom u kojem pravilo ne smije vrijediti. Sačuvajte značenje, zamjenske oznake, kod, URL-ove i strukturu dokumenta. Izbjegavajte pretvaranje tuđe stilske preference ili terminologije jednog tečaja u univerzalno pravilo.

Trenutna [implementacija rječnika](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) štiti pojmove od prevođenja. To nije rječnik terminologije iz izvornog u ciljni jezik. Raspravite novo ponašanje terminologije prije nego što ga obećate suradnicima.

## Primjer iz zajednice: izvještaj o japanskom nazivu proizvoda

U [izvještaju #527](https://github.com/Azure/co-op-translator/issues/527), @hyoshioka0128 je identificirao japanski prijevod koji je promijenio ime proizvoda `Co-op Translator` u `Co-op 翻訳`. Izvještaj je uključivao poveznicu na pogođeni dokument i snimku zaslona, što je olakšalo pronalaženje problema.

Suradnik je također povezao [povezani PR tečaja](https://github.com/microsoft/AZD-for-beginners/pull/109). U raspravi o problemu, održavatelj je potvrdio izvještaj i predložio ispitivanje zašto je ime promijenjeno, uključujući zaštitu terminologije, ponašanje rječnika i put prijevoda.

Ovo pokazuje kako mali izvještaj može podržati istragu širu od pojedinačne ispravke formulacije. To nije provjeren rezultat prije/nakon niti dokaz da su gore navedene japanske upute za Markdown-poveznice riješile ovaj problem s imenom proizvoda.

Možete doprinijeti na isti način: podijelite izvorni tekst, trenutni prijevod, predloženu ispravku i zašto je to važno. Dodajte poveznicu na dokument ili snimku zaslona kad je korisno. Ne morate dijagnosticirati uzrok ili napisati uputu (prompt) prije prijave.

## Provjera prije prihvaćanja pravila

Koristite iste uzorke izvora, reviziju prevoditelja, pružatelja/model i postavke generiranja za osnovne i kandidatne pokuse, mijenjajući samo predloženu uputu. Zabilježite stvarnu promjenu prompta i izlaze; ponovite primjere kad je potrebno kako biste razlikovali konzistentan efekt od varijabilnosti izlaza. Uključite prijavljeni neuspjeh, kontrastne kontekste i primjere koji se već pravilno prevode.

| Primjer | Izvor/kontekst | Izlaz referentni | Izlaz kandidata | Procjena recenzenta |
| --- | --- | --- | --- | --- |
| Prijavljeni neuspjeh | Treba prikupiti | Nije pokrenuto | Nije pokrenuto | Na čekanju |
| Kontraprimjer | Treba prikupiti | Nije pokrenuto | Nije pokrenuto | Na čekanju |
| Nepogođeni primjer | Treba prikupiti | Nije pokrenuto | Nije pokrenuto | Na čekanju |

Provjerite strukturne invarijante zasebno od jezičnih procjena. Uspješan test učitavanja prompta nije evaluacija kvalitete, i jedna točno očekivana rečenica nije jedini valjani prijevod. Ako nedostaju kontekst, pokusi modela ili jezična recenzija, zadržite prijedlog na čekanju umjesto da tvrdite da je problem riješen.