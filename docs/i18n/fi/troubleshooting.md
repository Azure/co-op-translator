# Vianetsintä

Käytä tätä sivua, kun käännösajo onnistuu odottamattomasti, epäonnistuu asetusten määrittelyn aikana tai tuottaa tulosta, joka vaatii tarkistusta.

## Aloita tästä

1. Suorita ensin kohdistettu komento, esimerkiksi `translate -l "ko" -md`.
2. Lisää `-d` saadaksesi konsolin debug-lokit.
3. Lisää `-s` tallentaaksesi debug-lokit polkuun `<root-dir>/logs/`.
4. Suorita `co-op-review` käännöksen jälkeen tarkistaaksesi ajantasaisuuden, rakenteen ja paikalliset linkit.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Konfigurointivirheet

### Ei kielimallipalveluntarjoajaa

Virhe:

```text
No language model configuration found.
```

Korjaus:

- Määritä Azure OpenAI, OpenAI tai Anthropic.
- Varmista, että muuttujat ovat siinä ympäristössä, jossa komento suoritetaan.
- Paikalliseen käyttöön laita ne projektin juureen tiedostoon `.env`.

Katso [Asetukset](configuration.md).

### Kuvien kääntäminen ilman Azure AI Visionia

Virhe:

```text
Image translation requested but Azure AI Service is not configured.
```

Korjaus:

- Lisää `AZURE_AI_SERVICE_API_KEY`.
- Lisää `AZURE_AI_SERVICE_ENDPOINT`.
- Tai suorita vain tekstiä käsittelevä komento, kuten `translate -l "ko" -md`.

### Virheellinen avain tai päätepiste

Oireita voivat olla `401`-virheet, sensuroidut käyttöoikeusvirheet tai päätepisteen käyttöön liittyvät virheet.

Korjaus:

- Varmista, että avain kuuluu samaan Azure-resurssiin kuin päätepiste.
- Varmista, että resurssi tukee Visionia käytettäessä `-img`-valitsinta.
- Varmista, että Azure OpenAI -käyttöönoton nimi ja API-versio vastaavat sinun käyttöönottoasi.
- Suorita debug-lokeilla: `translate -l "ko" -md -d -s`.

## Tiedostoja ei käännetty

Yleisiä syitä:

- Valitut valitsimet eivät vastaa tiedostojasi.
- Käännettyjä tiedostoja on jo olemassa.
- Lähdetiedostot sijaitsevat poissuljetuissa hakemistoissa.
- Komento suoritetaan väärästä projektin juurihakemistosta.

Tarkistukset:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Käytä `--root-dir`-valitsinta, kun komento suoritetaan projektin juuren ulkopuolelta.

## Odottamaton linkkien käyttäytyminen

Linkkien uudelleenkirjoitus riippuu valituista sisältötyypeistä:

- `-nb` mukana: notebook-linkit voivat osoittaa käännettyihin notebookeihin.
- `-nb` pois: notebook-linkit voivat pysyä osoittamassa alkuperäisiin notebookeihin.
- `-img` mukana: kuvalinkit voivat osoittaa käännettyihin kuviin.
- `-img` pois: kuvalinkit voivat jäädä osoittamaan alkuperäisiin kuviin.

Suorita täydellinen sisällön käännös, kun kaikkien sisäisten linkkien tulisi suosia käännettyjä tiedostoja:

```bash
translate -l "ko" -md -nb -img
```

Suorita linkkitarkistus käännöksen jälkeen:

```bash
co-op-review -l "ko"
```

## Markdownin renderöinti-ongelmat

Jos käännetty Markdown renderöityy väärin:

- Tarkista, että frontmatter alkaa ja päättyy `---`.
- Tarkista, että koodiaitausten määrät vastaavat toisiaan lähde- ja käännetyissä tiedostoissa.
- Suorita `co-op-review` havaitaksesi yleiset rakenneongelmat.
- Käännä kyseinen tiedosto uudelleen, jos tulos oli korruptoitunut.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action suoritettiin mutta pull requestia ei luotu

Jos `peter-evans/create-pull-request` raportoi, että haara ei ole edellä basea, työnkulku ei löytänyt tiedostoja commitattavaksi.

Todennäköiset syyt:

- Käännösajo ei tuottanut muutoksia.
- `.gitignore` sulkee pois `translations/`, `translated_images/`, tai käännetyt notebookit.
- `add-paths` ei vastaa luotuja tulostuskansioita.
- Käännösvaihe keskeytyi aikaisin.

Korjaukset:

1. Varmista, että luodut tiedostot löytyvät hakemistoista `translations/` tai `translated_images/`.
2. Varmista, ettei `.gitignore` ohita luotuja tulosteita.
3. Käytä vastaavia `add-paths`-asetuksia:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Lisää väliaikaisesti debug-valitsimet translate-komentoon:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Varmista, että työnkulun oikeudet sisältävät:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Käännöksen laatu

Konekäännökset saattavat tarvita ihmisen tarkistusta. Käytä `evaluate`-komentoa vain, kun haluat kokeellista laadun pisteytystä ja matalan luottamuksen korjaustyönkulkuja.

!!! warning "Kokeellinen"
    `evaluate` voi käyttää sääntöpohjaisia ja LLM-pohjaisia tarkistuksia, ja sen pisteytysmalli sekä metadatan käytös saattavat muuttua. Pidä sitä poissa pakollisista CI-portaista, ellei työnkulkusi ole valmistautunut muutoksiin.

Deterministisiin CI-tarkastuksiin käytä sen sijaan `co-op-review`.