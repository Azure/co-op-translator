# Vianetsintä

Käytä tätä sivua, kun käännöskierros onnistuu odottamattomasti, epäonnistuu konfiguroinnin aikana tai tuottaa tarkistettavaa sisältöä.

## Aloita tästä

1. Suorita ensin kohdennettu komento, esimerkiksi `translate -l "ko" -md`.
2. Lisää `-d` debug-lokeja varten.
3. Lisää `-s` tallentaaksesi debug-lokit hakemistoon `<root-dir>/logs/`.
4. Suorita `co-op-review` käännöksen jälkeen tarkistaaksesi tuoreuden, rakenteen ja paikalliset linkit.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Konfigurointivirheet

### Ei kielimallin tarjoajaa

Virhe:

```text
No language model configuration found.
```

Korjaus:

- Määritä Azure OpenAI tai OpenAI.
- Varmista, että muuttujat ovat ympäristössä, jossa komento suoritetaan.
- Paikalliseen käyttöön laita ne `.env`-tiedostoon projektin juureen.

Katso [Konfigurointi](configuration.md).

### Kuvakäännökset ilman Azure AI Visionia

Virhe:

```text
Image translation requested but Azure AI Service is not configured.
```

Korjaus:

- Lisää `AZURE_AI_SERVICE_API_KEY`.
- Lisää `AZURE_AI_SERVICE_ENDPOINT`.
- Tai suorita vain tekstiä käsittelevä komento, kuten `translate -l "ko" -md`.

### Virheellinen avain tai päätepiste

Oireisiin voi kuulua `401`, sensuroidut käyttöoikeusvirheet tai päätepisteen käyttöön liittyvät virheet.

Korjaus:

- Varmista, että avain kuuluu samaan Azure-resurssiin kuin päätepiste.
- Varmista, että resurssi tukee Visionia, kun käytät `-img`.
- Varmista, että Azure OpenAI -käyttöönoton nimi ja API-versio vastaavat käyttöönottoasi.
- Suorita debug-lokeilla: `translate -l "ko" -md -d -s`.

## Tiedostoja ei käännetty

Yleisiä syitä:

- Valitut liput eivät vastaa tiedostojasi.
- Käännettyjä tiedostoja on jo olemassa.
- Lähdetiedostot ovat suljettujen hakemistojen alla.
- Kommentoa ajetaan väärästä projektin juurihakemistosta.

Tarkistukset:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Käytä `--root-dir` kun komento ajetaan projektin juuren ulkopuolelta.

## Odottamaton linkkikäyttäytyminen

Linkkien uudelleenkirjoitus riippuu valituista sisältötyypeistä:

- `-nb` mukana: muistikirjalinkit voivat osoittaa käännettyihin muistikirjoihin.
- `-nb` poissa: muistikirjalinkit voivat jäädä osoittamaan lähde-muistikirjoihin.
- `-img` mukana: kuvien linkit voivat osoittaa käännettyihin kuviin.
- `-img` poissa: kuvien linkit voivat jäädä osoittamaan lähdekuviin.

Suorita täydellinen sisällönkäännös, kun kaikkien sisäisten linkkien tulisi suosia käännettyjä versioita:

```bash
translate -l "ko" -md -nb -img
```

Suorita linkkitarkistus käännöksen jälkeen:

```bash
co-op-review -l "ko"
```

## Markdownin renderöintiongelmat

Jos käännetty Markdown renderöityy väärin:

- Tarkista, että frontmatter alkaa ja päättyy `---`.
- Tarkista, että koodiaitausten määrät vastaavat lähde- ja käännettyjen tiedostojen välillä.
- Suorita `co-op-review` yleisten rakenneongelmien havaitsemiseksi.
- Käännä kyseinen tiedosto uudelleen, jos tulos oli vioittunut.

```bash
co-op-review -l "ko" --format github
```

## GitHub-aktion suoritus mutta vetopyyntöä ei luotu

Jos `peter-evans/create-pull-request` ilmoittaa, että haara ei ole edellä basea, työnkulku ei löytänyt sitoutettavia tiedostoja.

Todennäköiset syyt:

- Käännösajo ei tuottanut muutoksia.
- `.gitignore` sulkee pois `translations/`, `translated_images/` tai käännetyt muistikirjat.
- `add-paths` ei vastaa tuotettuja tuloshakemistoja.
- Käännösvaihe keskeytyi aikaisin.

Korjaukset:

1. Varmista, että tuotetut tiedostot löytyvät hakemistoista `translations/` tai `translated_images/`.
2. Varmista, että `.gitignore` ei ohita tuotettuja tuloksia.
3. Käytä vastaavia `add-paths`-asetuksia:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Lisää tilapäisesti debug-lippuja translate-komentoon:

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

Konekäännökset saattavat vaatia ihmistarkistusta. Käytä `evaluate`-komentoa vain, kun haluat kokeellista laadun pisteytystä ja alhaisen luottamuksen korjaustyönkulkuja.

!!! warning "Kokeellinen"
    `evaluate` voi käyttää sääntöpohjaisia ja LLM-pohjaisia tarkistuksia, ja sen pisteytysmalli sekä metadatankäsittely voivat muuttua. Älä ota sitä osaksi pakollisia CI-portteja ellei työnkulkusi ole valmistautunut muutoksiin.

For deterministic CI checks, use `co-op-review` instead.