# Prevedi, uredi i pregledaj mali projekt

Počnite s dvije kratke Markdown datoteke i jednim ciljnim jezikom. Vidjet ćete gdje se pišu prijevodi, što se događa kada se izvor promijeni i kako provjeriti rezultat.

## Zabilježeni rezultati

Primjer je pokrenut 19. rujna 2026. s Co-op Translator 0.21.0 i Azure OpenAI (`gpt-5-mini`). Nepromijenjene CLI naredbe su pozvane putem Clickovog `CliRunner`a koristeći izgrađeni wheel i postojeće Python ovisnosti.

| Korak | Rezultat |
| --- | --- |
| Pretpregled | Izlaz 0; nije zatražen prijevod modelom |
| Početni prijevod | Izlaz 0; 27.36 sekundi |
| Početni pregled | Izlaz 0 |
| Uredi README i pregled | Izlaz 1; otkriven je zastarjeli prijevod |
| Ažuriraj prijevod | Izlaz 0; 22.17 sekundi |
| Pregled nakon ažuriranja | Izlaz 0; bez pogrešaka ili upozorenja |
| Neizmijenjeni vodič | Identični bajtovi prije i nakon ažuriranja README-a |
| Pokreni ponovno | Izlaz 0; identični hashovi za sve datoteke prijevoda |

Ovo su pojedinačna mjerenja pokretanja, a ne jamstva izvedbe. Vrijeme postavljanja je isključeno; naplata od strane davatelja nije mjerena. Nepromijenjeno pokretanje i dalje može izvršiti provjeru zdravlja davatelja usluge.

Pregledajte [početni prijevod](../../assets/demo/before.txt), [ažurirani prijevod](../../assets/demo/after.txt), [puni diff prijevoda](../../assets/demo/update.diff), [zastarjeli pregled](../../assets/demo/review-stale.txt), [završni pregled](../../assets/demo/review-after.txt) i [detalje pokretanja](../../assets/demo/results.json). Potpuni prijevod datoteke može promijeniti drugu formulaciju, kao što pokazuje snimljeni diff. Oba tekstualna artefakta zadržavaju generirani odricanje.

Ljudski pregled je i dalje važan: snimljeno ažuriranje koristi `[사용 가이드](guide.md)을`; korejska partikula bi trebala biti `[사용 가이드](guide.md)를`. Tekstualni artefakti ostavljaju ovaj izlaz netaknut umjesto da prikažu uređeni prijevod kao izlaz modela. Strukturni pregled prolazi unatoč tom problemu s formulacijom.

## 1. Pripremite malu mapu

Koristite Python 3.11–3.14 i [postavljanje virtualnog okruženja](configuration.md#local-runtime-setup). Instalirajte verziju korištenu za ovaj primjer:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Preuzmite [README.txt](../../assets/demo/README.txt) i [guide.txt](../../assets/demo/guide.txt) u ovu mapu, spremite ih kao `README.md` i `guide.md`. To su mali izmišljeni dokumenti projekta; nije potrebna instalacija aplikacije.

README uključuje blok koda i poveznicu na `guide.md`. Njegova završna rečenica je:

```text
Notes are saved locally.
```

Ostavite u ovoj mapi samo ova dva izvornika. Sve naredbe u nastavku pokreću se unutar `translation-demo` i rade u Bashu i PowerShellu.

## 2. Pregled bez vjerodajnica

```bash
translate -l "ko" -md --dry-run
```

Pregled procjenjuje rad prijevoda bez pozivanja modela ili zapisivanja prijevoda. Procjene tokena nisu ponuda za naplatu. Prvo pokretanje bi trebalo identificirati obje Markdown datoteke kao novi posao.

## 3. Odaberite pružatelja i prevedite

Konfigurirajte jednog pružatelja koristeći [upute za konfiguraciju](configuration.md): Azure OpenAI, OpenAI ili Anthropic. OpenAI i Anthropic za prijevod teksta ne zahtijevaju Azure račun. Usluge za slike nisu potrebne za ovaj primjer.

Ako koristite lokalnu `.env` datoteku, dodajte `.env` u `.gitignore` ove mape. Pozivi za prijevod koriste račun vašeg pružatelja i mogu uzrokovati troškove.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Otvorite `translations/ko/README.md` i `translations/ko/guide.md`. Provjerite korejsko izražavanje, blok koda i poveznicu iz prevedenog README-a na prevedeni vodič. Formulacija izlaza varira ovisno o modelu.

`co-op-review` provjerava svježinu, strukturu i lokalne poveznice. Uspješan rezultat ne jamči jezičnu točnost. Riješite sve prijavljene pogreške prije nastavka.

Zabilježite uspješnu početnu verziju s Gitom (ako je potrebno, prvo konfigurirajte svoj Git identitet):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Promijenite izvor

U `README.md`, zamijenite `Notes are saved locally.` s:

```text
Notes are saved locally as Markdown files.
```

Ostavite `guide.md` nepromijenjenim. Zatim pokrenite:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Pregled bi trebao prijaviti da je prijevod README-a zastario i izaći neuspješno. Ovo je očekivano međustanje. Pretpregled bi trebao identificirati rad za promijenjeni README.

## 5. Ažurirajte i pregledajte diff

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Pregledajte stvarni diff: zadani CLI ponovno prevodi promijenjenu datoteku, pa model može također izmijeniti drugu formulaciju u toj datoteci. Neizmijenjeni vodič ne bi trebao imati diff. Pregled više ne bi trebao prijavljivati README kao zastario; istražite sve ostale nalaze umjesto da ih ignorirate.

Očuvanje uređivanja Markdowna na razini blokova zahtijeva opcionalnog pružatelja stanja prijevoda u [Python API](api.md). To nije omogućeno ovim CLI naredbama.

## 6. Pokrenite ponovno bez promjena

Commitajte ažurirani izvor i prijevod:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

S trenutnim prijevodima i nepromijenjenom konfiguracijom, prevoditelj preskače datoteke. Konačna Git naredba ne bi trebala proizvesti diff i trebala bi završiti uspješno.

## Sljedeći koraci

- [Prevedite samo README i otvorite pull request](github-actions.md#your-first-readme-translation-pr).
- [Odaberite CLI, Python API ili MCP](workflows.md).
- [Prijavite problem s prijevodom bez kodiranja](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).