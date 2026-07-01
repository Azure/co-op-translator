# CLI-viite

Co-op Translator asentaa nämä komentorivipäätepisteet:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Komennot `translate`, `evaluate`, `migrate-links` ja `co-op-review` välitetään `co_op_translator.__main__`in kautta, joka valitsee komennon toteutuksen kutsutun skriptin nimen perusteella. MCP-palvelin käyttää `co_op_translator.mcp.server`ia suoraan.

Jos valitset CLI:n, Python-API:n ja MCP:n välillä, aloita [Valitse työnkulku](workflows.md).

## Ensimmäinen CLI-käyttökerta

Aloita täältä, jos käytät Co-op Translatoria terminaalista:

1. Määritä LLM-palveluntarjoaja kuten kuvattu [Konfigurointi](configuration.md).
2. Valitse sisällön tyyppi, jonka haluat kääntää.
3. Suorita ensin tarkennettu komento, esimerkiksi vain Markdownin käännös.
4. Käytä `--dry-run` ennen suuria arkistomuutoksia.
5. Käytä `co-op-review` käännösten jälkeen rakenteen ja ajantasaisuuden tarkistamiseen.

| Tavoite | Komento aloitukseen |
| --- | --- |
| Käännä Markdown-dokumentteja | `translate -l "ko" -md` |
| Käännä muistikirjoja | `translate -l "ko" -nb` |
| Käännä kuvan teksti | `translate -l "ko" -img` |
| Esikatsele muutoksia ilman tiedostojen kirjoittamista | `translate -l "ko" -md --dry-run` |
| Tarkista olemassa olevat käännökset | `co-op-review -l "ko"` |
| Päivitä muistikirja- ja Markdown-linkit | `migrate-links -l "ko" --dry-run` |
| Avaa työkalut MCP-asiakkaalle | Määritä [MCP-palvelin](mcp.md) sen sijaan, että suoritat CLI-komentoja suoraan. |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

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

Suorita ilman interaktiivisia kehotteita:

```bash
translate -l "ko ja" -md -y
```

Tallenna lokit:

```bash
translate -l "ko" -s
```

### Asetukset

| Valinta | Pakollinen | Kuvaus |
| --- | --- | --- |
| `-l`, `--language-codes` | Kyllä | Välilyönnillä erotetut kielikoodit, esimerkiksi `"es fr de"`, tai `"all"`. |
| `-r`, `--root-dir` | Ei | Projektin juurihakemisto. Oletuksena nykyinen hakemisto. |
| `-u`, `--update` | Ei | Poista valittujen kielten olemassa olevat käännökset ja luo ne uudelleen. |
| `-img`, `--images` | Ei | Käännä vain kuvatiedostoja. |
| `-md`, `--markdown` | Ei | Käännä vain Markdown-tiedostoja. |
| `-nb`, `--notebook` | Ei | Käännä vain Jupyter-muistikirjoja. |
| `-d`, `--debug` | Ei | Ota debug-lokin tulostus konsoliin käyttöön. |
| `-s`, `--save-logs` | Ei | Tallenna DEBUG-tason lokit polkuun `<root-dir>/logs/`. |
| `-x`, `--fix` | Ei | Käännä uudelleen alhaisen luottamuksen Markdown-tiedostot aiempien arviointitulosten perusteella. |
| `-c`, `--min-confidence` | Ei | Luottamuskynnys `--fix`-vaihtoehdolle. Oletuksena `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Ei | Lisää tai poista konekäännöksiä koskevat vastuuvapauslausekkeet. Oletuksena käytössä CLI:ssä. |
| `-f`, `--fast` | Ei | Poistettu käytöstä oleva nopea kuvatila. |
| `-y`, `--yes` | Ei | Hyväksy kehotteet automaattisesti, hyödyllinen CI:ssä. |
| `--repo-url` | Ei | Arkiston URL, jota käytetään README:n kielitaulukon sparse-checkout-ohjeessa. |
| `--migrate-language-folders` | Ei | Nimeä uudelleen perinteiset alias-kansiot, kuten `cn` tai `tw`, kanonisiin BCP 47 -kansioihin. |
| `--dry-run` | Ei | Esikatsele kielikansioiden uudelleennimeämiset ja käännösarviot ilman tiedostojen kirjoittamista. |

If no type flag is provided, `translate` processes Markdown, notebooks, and images. Image translation requires Azure AI Vision configuration.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "Kokeellinen"
    `evaluate` on kokeellinen. Se voi käyttää sääntöperusteisia ja LLM-pohjaisia laatutarkistuksia, kirjoittaa arviointitulokset käännösmetatietoihin, ja sen pisteytysmalli sekä metatietojen käyttäytyminen voivat muuttua.

```bash
evaluate -l "ko"
```

### Yleisiä esimerkkejä

Käytä tiukempaa alhaisen luottamuksen kynnystä:

```bash
evaluate -l "es" -c 0.8
```

Suorita vain sääntöperusteiset tarkistukset:

```bash
evaluate -l "fr" -f
```

Suorita vain LLM-perusteiset tarkistukset:

```bash
evaluate -l "ja" -D
```

### Asetukset

| Valinta | Pakollinen | Kuvaus |
| --- | --- | --- |
| `-l`, `--language-code` | Kyllä | Yksi kielikoodi arvioitavaksi. Alias-koodit normalisoidaan. |
| `-r`, `--root-dir` | Ei | Projektin juurihakemisto. Oletuksena nykyinen hakemisto. |
| `-c`, `--min-confidence` | Ei | Kynnys, jota käytetään luetteloitaessa alhaisen luottamuksen käännöksiä. Oletuksena `0.7`. |
| `-d`, `--debug` | Ei | Ota debug-lokin tulostus käyttöön. |
| `-s`, `--save-logs` | Ei | Tallenna DEBUG-tason lokit polkuun `<root-dir>/logs/`. |
| `-f`, `--fast` | Ei | Vain sääntöperusteinen arviointi. |
| `-D`, `--deep` | Ei | Vain LLM-pohjainen arviointi. |

Oletuksena `evaluate` käyttää sekä sääntöperusteista että LLM-pohjaista arviointia. Tulokset kirjoitetaan käännösmetatietoihin ja esitetään yhteenvedossa konsolissa.

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "Beta"
    `co-op-review` on beta-vaiheessa oleva deterministinen tarkistuskomento. Se ei kutsu mallipalveluntarjoajia eikä kirjoita tiedostoja, mutta sen tarkistukset ja ongelmaulostulon skeema saattavat kehittyä.

```bash
co-op-review -l "ko"
```

### Yleisiä esimerkkejä

Tarkista korea- ja japani-käännökset nykyisestä hakemistosta:

```bash
co-op-review -l "ko ja"
```

Tarkista tietty projektin juuri:

```bash
co-op-review -l "fr" -r ./my-course
```

Tarkista vain lähdetiedostot, jotka ovat muuttuneet verrattuna base-refiin:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Tulosta GitHub-tyyppinen Markdown-ulostulo CI-yhteenvedoille:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Asetukset

| Valinta | Pakollinen | Kuvaus |
| --- | --- | --- |
| `-l`, `--language-code` | Ei | Tarkistettava kielikoodi. Voidaan antaa useita kertoja tai välilyönnillä eroteltuna. Oletuksena kaikki löydetyt käännöskielet. |
| `-r`, `--root-dir` | Ei | Projektin juurihakemisto. Oletuksena nykyinen hakemisto. |
| `--changed-from` | Ei | Git-ref, jota käytetään rajoittamaan tarkistus muutettuihin lähdetiedostoihin. |
| `--format` | Ei | Tulosteen muoto: `text` tai `github`. Oletuksena `text`. |

`co-op-review` tarkistaa tällä hetkellä puuttuvat käännetyt tiedostot, puuttuvat tai vanhentuneet käännösmetatiedot, Markdown-frontmatterin ja koodiaitausten eheystarkistuksen, virheellisen käännetyn notebook JSONin sekä puuttuvat paikalliset Markdown- tai kuvalinkkien kohteet. Puuttuvat linkit ovat oletuksena varoituksia; rakenteelliset ja ajantasaisuuteen liittyvät ongelmat aiheuttavat komennon epäonnistumisen.

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [MCP-palvelin](mcp.md) guide for client configuration, tools, resources, and safety notes.

### Asetukset

| Valinta | Pakollinen | Kuvaus |
| --- | --- | --- |
| `--transport` | Ei | MCP-yhteys: `stdio`, `streamable-http` tai `sse`. Oletuksena `stdio`. |

## migrate-links

Reprocess translated Markdown files and update notebook links so they point to translated notebooks when available.

```bash
migrate-links -l "ko ja"
```

### Yleisiä esimerkkejä

Esikatsele linkkimuutokset:

```bash
migrate-links -l "ko" --dry-run
```

Käsittele kaikki tuetut kielet ilman vahvistusta:

```bash
migrate-links -l "all" -y
```

Kirjoita linkkejä uudelleen vain, kun käännettyjä muistikirjoja on olemassa:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Asetukset

| Valinta | Pakollinen | Kuvaus |
| --- | --- | --- |
| `-l`, `--language-codes` | Kyllä | Välilyönnillä erotetut kielikoodit, tai `"all"`. |
| `-r`, `--root-dir` | Ei | Projektin juurihakemisto. Oletuksena nykyinen hakemisto. |
| `--image-dir` | Ei | Käännettyjen kuvien hakemisto suhteessa juureen. Oletuksena `translated_images`. |
| `--dry-run` | Ei | Näytä tiedostot, jotka muuttuivat ilman kirjoitusta. |
| `--fallback-to-original`, `--no-fallback-to-original` | Ei | Käytä alkuperäisiä muistikirjalinkkejä, kun käännettyjä muistikirjoja puuttuu. Oletuksena käytössä. |
| `-d`, `--debug` | Ei | Ota debug-lokin tulostus käyttöön. |
| `-s`, `--save-logs` | Ei | Tallenna DEBUG-tason lokit polkuun `<root-dir>/logs/`. |
| `-y`, `--yes` | Ei | Hyväksy kehotteet automaattisesti käsiteltäessä kaikkia kieliä. |

## Ympäristö

Kaikki komennot vaativat yhden määritetyn LLM-palveluntarjoajan:

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
```

Kuvien käännös vaatii lisäksi Azure AI Visionin:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Tulosteiden rakenne

Tekstikäännökset kirjoitetaan sijainteihin:

```text
translations/<language-code>/<original-path>
```

Käännetyt kuvat kirjoitetaan sijainteihin:

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

Korjaa alhaisen luottamuksen Markdown-käännökset:

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

Esikatsele linkkisiirto:

```bash
migrate-links -l "ko" --dry-run
```