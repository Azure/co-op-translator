# Käännä, muokkaa ja tarkista pieni projekti

Aloita kahdella lyhyellä Markdown-tiedostolla ja yhdellä kohdekielellä. Näet, mihin käännökset kirjoitetaan, mitä tapahtuu kun lähdetiedosto muuttuu, ja miten tarkistaa tulos.

## Tallennetut tulokset

Esimerkki ajettiin 19. syyskuuta 2026 käyttäen Co-op Translator 0.21.0:aa ja Azure OpenAI:ta (`gpt-5-mini`). Muokkaamattomat CLI-komennot kutsuttiin Clickin `CliRunner`-luokan kautta käyttäen rakennettua wheel-pakettia ja olemassa olevia Python-riippuvuuksia.

| Vaihe | Tulos |
| --- | --- |
| Esikatselu | Poistumiskoodi 0; mallikäännöstä ei pyydetty |
| Alkuperäinen käännös | Poistumiskoodi 0; 27.36 sekuntia |
| Alkuperäinen tarkastus | Poistumiskoodi 0 |
| Muokkaa README:tä ja tarkasta | Poistumiskoodi 1; vanhentunut käännös havaittu |
| Päivitä käännös | Poistumiskoodi 0; 22.17 sekuntia |
| Tarkastus päivityksen jälkeen | Poistumiskoodi 0; ei virheitä tai varoituksia |
| Muuttumaton opas | Tavut ovat identtiset ennen ja jälkeen README-päivityksen |
| Aja uudelleen | Poistumiskoodi 0; identtiset tiivisteet kaikille käännöstiedostoille |

Nämä ovat yksittäisiä ajokertamittauksia, eivät suorituskykytakuita. Asetusaikaa ei ole otettu mukaan; palveluntarjoajan laskutusta ei mitattu. Muuttumaton ajo voi silti suorittaa palveluntarjoajan terveystarkistuksen.

Tarkastele [alkuperäistä käännöstä](../../assets/demo/before.txt), [päivitettyä käännöstä](../../assets/demo/after.txt), [kokonaisen käännöksen eroa](../../assets/demo/update.diff), [vanhentunutta tarkastusta](../../assets/demo/review-stale.txt), [lopullista tarkastusta](../../assets/demo/review-after.txt) ja [ajon yksityiskohtia](../../assets/demo/results.json). Kokonaisen tiedoston käännös voi muuttaa muita sanavalintoja, kuten tallennettu diff osoittaa. Molemmat tekstiaineistot säilyttävät generoidun vastuuvapauslausekkeen.

Ihmisen tarkastus on edelleen tärkeää: tallennettu päivitys käyttää `[사용 가이드](guide.md)을`; korealaisen partikkelin pitäisi olla `[사용 가이드](guide.md)를`. Tekstiaineistot säilyttävät tämän tulosteen sellaisenaan sen sijaan, että esittäisivät muokatun käännöksen mallin tuottamana. Rakenteellinen tarkastus läpäistään tämän sanamuotovirheen huolimatta.

## 1. Valmistele pieni kansio

Käytä Python 3.11–3.14 ja [virtuaaliympäristön asetusta](configuration.md#local-runtime-setup). Asenna esimerkissä käytetty versio:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Lataa [README.txt](../../assets/demo/README.txt) ja [guide.txt](../../assets/demo/guide.txt) tähän kansioon ja tallenna ne nimillä `README.md` ja `guide.md`. Ne ovat pieniä kuvitteellisia projektidokumentteja; sovelluksen asennusta ei tarvita.

README sisältää koodilohkon ja linkin `guide.md`-tiedostoon. Sen viimeinen lause on:

```text
Notes are saved locally.
```

Pidä tässä kansiossa vain nämä kaksi lähdetiedostoa. Kaikki seuraavat komennot ajetaan kansiosta `translation-demo` ja ne toimivat Bashissa ja PowerShellissä.

## 2. Esikatsele ilman tunnuksia

```bash
translate -l "ko" -md --dry-run
```

Esikatselu arvioi käännöstyön määrän ilman mallin kutsumista tai käännösten kirjoittamista. Token-arviot eivät ole laskutuslaskelma. Ensimmäisen ajon pitäisi tunnistaa molemmat Markdown-tiedostot uutena työnä.

## 3. Valitse palveluntarjoaja ja käännä

Konfiguroi yksi palveluntarjoaja käyttäen [konfigurointiohjetta](configuration.md): Azure OpenAI, OpenAI tai Anthropic. OpenAI:n ja Anthropicin tekstikäännöksiin ei tarvita Azure-tiliä. Kuvapalveluita ei tarvita tässä esimerkissä.

Jos käytät paikallista `.env`-tiedostoa, lisää `.env` tämän kansion `.gitignore`-tiedostoon. Käännöskutsut käyttävät palveluntarjoajatililtäsi resursseja ja saattavat aiheuttaa kuluja.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Avaa `translations/ko/README.md` ja `translations/ko/guide.md`. Tarkista korealainen sanamuoto, koodilohko ja linkki käännetystä README-tiedostosta käännettyyn opaseen. Tulosten sanavalinnat vaihtelevat mallista riippuen.

`co-op-review` tarkistaa tuoreuden, rakenteen ja paikalliset linkit. Läpäisevä tulos ei takaa kielellistä oikeellisuutta. Korjaa mahdolliset raportoidut virheet ennen jatkamista.

Tallenna onnistunut perusta Gitillä (konfiguroi Git-tunnuksesi ensin tarvittaessa):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Muuta lähdetiedostoa

Korvaa `README.md`-tiedostossa `Notes are saved locally.` seuraavalla:

```text
Notes are saved locally as Markdown files.
```

Jätä `guide.md` muuttumattomaksi. Sitten suorita:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Tarkastus ilmoittaa README-käännöksen vanhentuneeksi ja poistuu epäonnistuneesti. Tämä on odotettu välivaihe. Esikatselun pitäisi tunnistaa työksi muuttunut README.

## 5. Päivitä ja tarkista erot

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Tarkista todellinen diff: oletus-CLI kääntää muuttuneen tiedoston uudelleen, joten malli voi myös muokata muita sanavalintoja kyseisessä tiedostossa. Muuttumattomassa oppaassa ei pitäisi olla eroja. Tarkastuksen ei pitäisi enää ilmoittaa README:tä vanhentuneeksi; tutki kaikki muut löydökset sen sijaan, että sivuuttaisit ne.

Ihmisen tekemiä Markdown-muutoksia säilyttävä lohko-tason säilytys vaatii valinnaisen käännöstilan tarjoajan [Python API](api.md) -rajapinnassa. Se ei ole käytössä näillä CLI-komennoilla.

## 6. Aja uudelleen ilman muutoksia

Commitoi päivitetty lähde ja käännös:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Nykyisillä käännöksillä ja muuttumattomalla konfiguraatiolla kääntäjä ohittaa tiedostot. Viimeisen Git-komennon ei pitäisi tuottaa eroja ja sen pitäisi päättyä onnistuneesti.

## Seuraavat askeleet

- [Käännä vain README ja avaa pull-pyyntö](github-actions.md#your-first-readme-translation-pr).
- [Valitse CLI, Python API tai MCP](workflows.md).
- [Ilmoita käännösongelmasta ilman koodausta](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).