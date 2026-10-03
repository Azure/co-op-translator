# CLI-viite

Co-op Translator asentaa nämä komentorivitoiminnot:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Komennot `translate`, `evaluate`, `migrate-links` ja `co-op-review` välitetään `co_op_translator.__main__`-moduulin kautta, joka valitsee komennon toteutuksen kutsutun skriptin nimen perusteella. MCP-palvelin käyttää suoraan `co_op_translator.mcp.server`-moduulia.

Jos valitset CLI:n, Python-API:n ja MCP:n välillä, aloita luvusta [Valitse työnkulku](workflows.md).

## Konsoliulostus

Interaktiiviset päätelaitteet käyttävät Rich-muotoilua komennon otsikkoon, edistymiseen ja yhteenvetoihin. CI ja ei-interaktiivinen tulostus palautuvat automaattisesti tavalliseen tekstiin.

Aseta `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` pakottaaksesi tavallisen tulostuksen, tai `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` pakottaaksesi Rich-tulostuksen. Aseta `CO_OP_TRANSLATOR_NO_PROGRESS=1` pitääksesi yhteenvedot mutta estääksesi live-tilapalkit.

Käytä `translate --json-events progress.ndjson`, kun toinen järjestelmä tarvitsee koneellisesti luettavaa edistymistä. CLI jatkaa ihmiskäyttäjälle tarkoitetun tulostuksen renderöintiä, kun taas NDJSON-tiedosto vastaanottaa versioituja `co-op.translation.event.v1`-tapahtumia, joissa on vakaita kenttiä kuten `type`, `stage_key`, `completed`, `total` ja `current_path`.





## Ensimmäinen CLI-käyttö

Aloita tästä, jos käytät Co-op Translatoria päätelaitteesta:

1. Määritä LLM-palveluntarjoaja kuten kuvataan kohdassa [Asetukset](configuration.md).
2. Valitse sisältötyyppi, jonka haluat kääntää.
3. Suorita ensin kohdennettu komento, esimerkiksi vain Markdownin käännös.
4. Käytä `--dry-run` ennen suuren repoon tehtäviä muutoksia.
5. Käytä `co-op-review` käännöksen jälkeen rakenteen ja ajantasaisuuden tarkistukseen.

| Goal | Command to start with |
| --- | --- |
| Käännä Markdown-dokumentit | `translate -l "ko" -md` |
| Käännä muistikirjat | `translate -l "ko" -nb` |
| Käännä kuvan teksti | `translate -l "ko" -img` |
| Esikatsele muutoksia ilman tiedostojen kirjoittamista | `translate -l "ko" -md --dry-run` |
| Tarkista olemassa olevat käännökset | `co-op-review -l "ko"` |
| Päivitä muistikirja- ja Markdown-linkit | `migrate-links -l "ko" --dry-run` |
| Tarjoa työkalut MCP-asiakkaalle | Konfiguroi [MCP-palvelin](mcp.md) sen sijaan, että suoritat CLI-komentoja suoraan. |

## translate

Käännä Markdown-tiedostoja, muistikirjoja ja kuvien tekstiä yhteen tai useampaan kohdekieleen.

```bash
translate -l "ko ja fr"
```

### Yleisiä esimerkkejä

Käännä vain Markdown:

```bash
translate -l "de" -md
```

Käännä vain muistikirjat:

```bash
translate -l "zh-CN" -nb
```

Käännä Markdown ja kuvat:

```bash
translate -l "pt-BR" -md -img
```

Päivitä olemassa olevat käännökset poistamalla ja luomalla ne uudelleen:

```bash
translate -l "ko" -u
```

Suorita ilman vuorovaikutteisia kehotteita:

```bash
translate -l "ko ja" -md -y
```

Tallenna lokit:

```bash
translate -l "ko" -s
```

Kirjoita jäsenneltyjä edistymistapahtumia:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Asetukset

| Vaihtoehto | Pakollinen | Kuvaus |
| --- | --- | --- |
| `-l`, `--language-codes` | Kyllä | Välilyönnillä erotetut kielikoodit, kuten `"es fr de"`, tai `"all"`. |
| `-r`, `--root-dir` | Ei | Projektin juurihakemisto. Oletuksena nykyinen hakemisto. |
| `-u`, `--update` | Ei | Poista olemassa olevat käännökset valituille kielille ja luo ne uudelleen. |
| `-img`, `--images` | Ei | Käännä vain kuvatiedostot. |
| `-md`, `--markdown` | Ei | Käännä vain Markdown-tiedostoja. |
| `-nb`, `--notebook` | Ei | Käännä vain Jupyter-muistikirjatiedostoja. |
| `-d`, `--debug` | Ei | Ota debug-lokin tulostus käyttöön konsolissa. |
| `-s`, `--save-logs` | Ei | Tallenna DEBUG-tason lokit polkuun `<root-dir>/logs/`. |
| `--json-events` | Ei | Kirjoita koneellisesti luettavat käännöksen edistymistapahtumat NDJSON-muotoon. |
| `-x`, `--fix` | Ei | Uudelleenkäännä matalan luottamuksen Markdown-tiedostot aiempien arviointitulosten perusteella. |
| `-c`, `--min-confidence` | Ei | Luottamuskynnys `--fix`-optiolle. Oletus `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Ei | Lisää tai poista konekäännösvaroitukset. Oletuksena CLI:ssä käytössä. |
| `-f`, `--fast` | Ei | Vanhentunut nopea kuva-tila. |
| `-y`, `--yes` | Ei | Vahvista kehotteet automaattisesti, hyödyllinen CI:ssä. |
| `--repo-url` | Ei | Arkiston URL, jota käytetään README-kielten taulukon sparse-checkout-ohjeessa. |
| `--migrate-language-folders` | Ei | Nimeä vanhat alias-kansiot, kuten `cn` tai `tw`, uudelleen kanonisiin BCP 47 -kansioihin. |
| `--dry-run` | Ei | Esikatsele kielikansioiden migraatiota ja käännösarvioita ilman tiedostojen kirjoittamista. |

Jos tyyppilippua ei anneta, `translate` käsittelee Markdown-tiedostot, muistikirjat ja kuvat. Kuvien kääntäminen vaatii Azure AI Vision -määrityksen.

## evaluate

Arvioi käännettyjen Markdown-tiedostojen laatu yhdelle kielelle.

!!! warning "Kokeellinen"
    `evaluate` on kokeellinen. Se voi käyttää sääntöpohjaisia ja LLM-pohjaisia laatutarkistuksia, kirjoittaa arviointitulokset käännösmetatietoihin, ja sen pisteytysmalli sekä metatietokäytös saattavat muuttua.

```bash
evaluate -l "ko"
```

### Yleisiä esimerkkejä

Käytä tiukempaa matalan luottamuksen kynnystä:

```bash
evaluate -l "es" -c 0.8
```

Suorita vain sääntöpohjaiset tarkistukset:

```bash
evaluate -l "fr" -f
```

Suorita vain LLM-pohjaiset tarkistukset:

```bash
evaluate -l "ja" -D
```

### Asetukset

| Vaihtoehto | Pakollinen | Kuvaus |
| --- | --- | --- |
| `-l`, `--language-code` | Kyllä | Arvioitava yksittäinen kielikoodi. Alias-koodit normalisoidaan. |
| `-r`, `--root-dir` | Ei | Projektin juurihakemisto. Oletuksena nykyinen hakemisto. |
| `-c`, `--min-confidence` | Ei | Kynnys käytettäväksi listattaessa matalan luottamuksen käännöksiä. Oletus `0.7`. |
| `-d`, `--debug` | Ei | Ota debug-lokin tulostus käyttöön. |
| `-s`, `--save-logs` | Ei | Tallenna DEBUG-tason lokit polkuun `<root-dir>/logs/`. |
| `-f`, `--fast` | Ei | Vain sääntöpohjainen arviointi. |
| `-D`, `--deep` | Ei | Vain LLM-pohjainen arviointi. |

Oletuksena `evaluate` käyttää sekä sääntöpohjaista että LLM-pohjaista arviointia. Tulokset kirjoitetaan käännösmetatietoihin ja tiivistetään konsoliin.

## co-op-review

Suorita deterministisiä käännösten ylläpitotarkistuksia ilman API-tunnuksia.

!!! note "Beeta"
    `co-op-review` on beeta-vaiheessa oleva deterministinen tarkistuskomento. Se ei kutsu malli­palveluntarjoajia eikä kirjoita tiedostoja, mutta sen tarkistukset ja virheilmoitusten tulostemuoto voivat kehittyä.

```bash
co-op-review -l "ko"
```

### Yleisiä esimerkkejä

Tarkista korealaiset ja japanilaiset käännökset nykyisestä hakemistosta:

```bash
co-op-review -l "ko ja"
```

Tarkista tietty projektin juurihakemisto:

```bash
co-op-review -l "fr" -r ./my-course
```

Tarkista vain README, README:lle tehdyn käännöksen jälkeen:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` ohittaa muut asiakirjat ja sisäkkäiset READMEt. Se epäonnistuu, jos juurihakemiston
`README.md` puuttuu. Yhdistettynä `--changed-from`-valintaan se tarkistaa README:n vain
kun kyseinen lähdetiedosto on muuttunut. README-ainoa käännös jättää alkuperäisen README:n
muuttumattomaksi, mukaan lukien kaikki jaetut osiomerkinnät.

Tarkista vain lähdetiedostot, jotka ovat muuttuneet verrattuna perusrefiin:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Tulosta GitHub-tyylinen Markdown-tulostus CI-yhteenvetoja varten:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Asetukset

| Vaihtoehto | Pakollinen | Kuvaus |
| --- | --- | --- |
| `-l`, `--language-code` | Ei | Tarkistettava kielikoodi. Voidaan antaa useita kertoja tai välilyönnillä erotettuna arvona. Oletuksena kaikki löydetyt käännöskielet. |
| `-r`, `--root-dir` | Ei | Projektin juurihakemisto. Oletuksena nykyinen hakemisto. |
| `--changed-from` | Ei | Git-ref, jota käytetään rajaamaan tarkistus muuttuneisiin lähdetiedostoihin. |
| `--readme-only` | Ei | Tarkista vain juuren `README.md`-käännös. |
| `--format` | Ei | Tulostusmuoto: `text` tai `github`. Oletus `text`. |

`co-op-review` tarkistaa tällä hetkellä puuttuvat käännetyt tiedostot, puuttuvat tai vanhentuneet käännösmetatiedot, Markdownin frontmatterin ja koodilohkojen eheyden, virheellisen käännetyn muistikirjan JSONin sekä puuttuvat paikalliset Markdown- tai kuva-linkkien kohteet. Puuttuvat linkit ovat oletuksena varoituksia; rakenne- ja ajantasaisuusongelmat johtavat komennon epäonnistumiseen.

## co-op-translator-mcp

Aja Co-op Translator MCP -palvelin agenteille, muokkaajille ja MCP-yhteensopiville asiakkaille.

```bash
co-op-translator-mcp
```

Oletussiirto on `stdio`. Katso [MCP-palvelin](mcp.md) -opas asiakasasetuksista, työkaluista, resursseista ja turvallisuusmuistiinpanoista.

### Asetukset

| Vaihtoehto | Pakollinen | Kuvaus |
| --- | --- | --- |
| `--transport` | Ei | MCP-siirto: `stdio`, `streamable-http`, tai `sse`. Oletus `stdio`. |

## migrate-links

Käsittele käännetyt Markdown-tiedostot uudelleen ja päivitä muistikirjalinkit niin, että ne osoittavat käännettyihin muistikirjoihin, kun niitä on saatavilla.

```bash
migrate-links -l "ko ja"
```

### Yleisiä esimerkkejä

Esikatsele linkkipäivitykset:

```bash
migrate-links -l "ko" --dry-run
```

Käsittele kaikki tuetut kielet ilman vahvistusta:

```bash
migrate-links -l "all" -y
```

Kirjoita linkit uudelleen vain, kun käännettyjä muistikirjoja on olemassa:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Asetukset

| Vaihtoehto | Pakollinen | Kuvaus |
| --- | --- | --- |
| `-l`, `--language-codes` | Kyllä | Välilyönnillä erotetut kielikoodit, tai `"all"`. |
| `-r`, `--root-dir` | Ei | Projektin juurihakemisto. Oletuksena nykyinen hakemisto. |
| `--image-dir` | Ei | Käännettyjen kuvien hakemisto suhteessa juureen. Oletus `translated_images`. |
| `--dry-run` | Ei | Näytä tiedostot, jotka muuttuisivat ilman päivitysten kirjoittamista. |
| `--fallback-to-original`, `--no-fallback-to-original` | Ei | Käytä alkuperäisiä muistikirjalinkkejä, kun käännetty muistikirja puuttuu. Oletuksena käytössä. |
| `-d`, `--debug` | Ei | Ota debug-lokin tulostus käyttöön. |
| `-s`, `--save-logs` | Ei | Tallenna DEBUG-tason lokit polkuun `<root-dir>/logs/`. |
| `-y`, `--yes` | Ei | Vahvista kehotteet automaattisesti käsiteltäessä kaikkia kieliä. |

## Ympäristö

Kun komento vaatii palveluntarjoajan tunnuksia, konfiguroi jokin näistä palveluntarjoajaryhmistä. `translate --dry-run` ja `co-op-review` eivät vaadi palveluntarjoajatunnuksia:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Tai OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Tai Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Kuvien kääntäminen vaatii lisäksi Azure AI Visionin:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Tulosteiden rakenne

Tekstikäännökset kirjoitetaan hakemistoon:

```text
translations/<language-code>/<original-path>
```

Käännettyjen kuvien tulosteet kirjoitetaan hakemistoon:

```text
translated_images/<language-code>/<original-path>
```

Esimerkiksi `README.md`- ja `docs/setup.md`-tiedostojen kääntäminen koreaksi tuottaa:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Kopioi-liitä CLI-esimerkit

Käännä Markdown kolmelle kielelle:

```bash
translate -l "ko ja fr" -md
```

Käännä vain muistikirjat:

```bash
translate -l "zh-CN" -nb
```

Käännä vain kuvat:

```bash
translate -l "pt-BR" -img
```

Esikatsele Markdown-käännös ilman tiedostojen kirjoittamista:

```bash
translate -l "de es" -md --dry-run
```

Korjaa matalan luottamuksen Markdown-käännökset:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Suorita CI-ystävällinen Markdown-käännös:

```bash
translate -l "ko ja" -md -y -s
```

Tarkista käännetty tulos:

```bash
co-op-review -l "ko ja"
```

Esikatsele linkkimigraatio:

```bash
migrate-links -l "ko" --dry-run
```