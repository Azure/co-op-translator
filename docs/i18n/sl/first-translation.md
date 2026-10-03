# Prevedite, uredite in pregledajte majhen projekt

Začnite z dvema kratkima Markdown datotekama in enim ciljnim jezikom. Videli boste, kam se zapišejo prevodi, kaj se zgodi, ko se izvor spremeni, in kako preveriti rezultat.

## Zabeleženi rezultati

Primer je bil izveden 19. septembra 2026 s Co-op Translator 0.21.0 in Azure OpenAI (`gpt-5-mini`). Nespremenjeni ukazi CLI so bili poklicani prek Clickovega `CliRunner` z uporabo zgrajenega wheel paketa in obstoječih Python odvisnosti.

| Korak | Rezultat |
| --- | --- |
| Predogled | Izhod 0; prevod z modelom ni bil zahtevan |
| Začetni prevod | Izhod 0; 27.36 sekund |
| Začetni pregled | Izhod 0 |
| Uredi README in preglej | Izhod 1; zaznan zastarel prevod |
| Posodobi prevod | Izhod 0; 22.17 sekund |
| Pregled po posodobitvi | Izhod 0; brez napak ali opozoril |
| Nespremenjen vodnik | Identični bajti pred in po posodobitvi README |
| Zaženi znova | Izhod 0; identični hashi za vse datoteke prevodov |

To so meritve posameznih zaganjanj, ne garancija zmogljivosti. Čas nastavitev je izključen; obračunavanje s strani ponudnika ni bilo izmerjeno. Nespremenjen zagon lahko še vedno izvede preverjanje stanja ponudnika.

Preverite [začetni prevod](../../assets/demo/before.txt), [posodobljeni prevod](../../assets/demo/after.txt), [popolno razliko prevoda](../../assets/demo/update.diff), [zastarel pregled](../../assets/demo/review-stale.txt), [končni pregled](../../assets/demo/review-after.txt) in [podrobnosti zagona](../../assets/demo/results.json). Prevodi celotnih datotek lahko spremenijo drugo besedilo, kot kaže zajeta razlika. Oba besedilna artefakta ohranita generirano izjavo.

Človeški pregled je še vedno pomemben: zajeta posodobitev uporablja `[사용 가이드](guide.md)을`; korejska partikula bi morala biti `[사용 가이드](guide.md)를`. Besedilni artefakti ohranijo ta izhod nespremenjen, namesto da bi predstavili urejen prevod kot izhod modela. Strukturni pregled je opravljen kljub tej jezikovni težavi.

## 1. Pripravite majhno mapo

Uporabite Python 3.11–3.14 in [nastavitev virtualnega okolja](configuration.md#local-runtime-setup). Namestite različico uporabljeno za ta primer:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Prenesite [README.txt](../../assets/demo/README.txt) in [guide.txt](../../assets/demo/guide.txt) v to mapo in ju shranite kot `README.md` in `guide.md`. To so majhni izmišljeni projektni dokumenti; namestitev aplikacije ni potrebna.

README vsebuje blok kode in povezavo do `guide.md`. Njegov zadnji stavek je:

```text
Notes are saved locally.
```

V tej mapi ohranite samo ti dve izvorni datoteki. Vsi nadaljnji ukazi se izvajajo znotraj `translation-demo` in delujejo v Bash in PowerShell.

## 2. Predogled brez poverilnic

```bash
translate -l "ko" -md --dry-run
```

Predogled ocenjuje delo prevajanja brez klica modela ali pisanja prevodov. Ocenjene količine žetonov niso ponudba za obračun. Prvi zagon bi moral označiti obe Markdown datoteki kot novo delo.

## 3. Izberite ponudnika in prevedite

Konfigurirajte enega ponudnika s pomočjo [priročnika za konfiguracijo](configuration.md): Azure OpenAI, OpenAI ali Anthropic. Za prevajanje besedila z OpenAI in Anthropic ne potrebujete Azure računa. Storitve za slike v tem primeru niso potrebne.

Če uporabljate lokalno datoteko `.env`, dodajte `.env` v `.gitignore` te mape. Klici za prevajanje uporabljajo vaš račun pri ponudniku in lahko povzročijo stroške.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Odprite `translations/ko/README.md` in `translations/ko/guide.md`. Preverite korejsko besedišče, blok kode in povezavo iz prevedenega README na prevedeni vodnik. Besedilo izhoda se razlikuje glede na model.

`co-op-review` preveri svežino, strukturo in lokalne povezave. Uspešen rezultat ne potrjuje jezikovne točnosti. Pred nadaljevanjem odpravite vse poročane napake.

Zabeležite uspešno osnovno stanje z Gitom (po potrebi najprej nastavite svojo Git identiteto):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Spremenite izvor

V `README.md` zamenjajte `Notes are saved locally.` z:

```text
Notes are saved locally as Markdown files.
```

Pustite `guide.md` nespremenjen. Nato zaženite:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Pregled bi moral poročati, da je prevod README zastarel in končati z neuspehom. To je pričakovano vmesno stanje. Predogled bi moral zaznati delo za spremenjeni README.

## 5. Posodobite in preglejte razliko

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Preglejte dejansko razliko: privzeti CLI ponovno prevede spremenjeno datoteko, zato lahko model tudi spremeni drugo besedilo v tej datoteki. Nespremenjeni vodnik ne bi smel imeti razlike. Pregled ne bi smel več poročati, da je README zastarel; preučite morebitna druga ugotovljena vprašanja namesto da jih ignorirate.

Ohranjanje blokovne ravni človeških Markdown urejanj zahteva izbirnega ponudnika stanja prevoda v [Python API](api.md). To ni omogočeno s temi CLI ukazi.

## 6. Ponovno zaženite brez sprememb

Potrdite posodobljeni izvor in prevod:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

S trenutnimi prevodi in nespremenjeno konfiguracijo prevajalnik preskoči datoteke. Končni Git ukaz ne bi smel ustvariti razlike in bi moral uspešno zaključiti.

## Naslednji koraki

- [Prevedite samo README in odprite pull request](github-actions.md#your-first-readme-translation-pr).
- [Izberite CLI, Python API ali MCP](workflows.md).
- [Prijavite težavo s prevodom brez kodiranja](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).