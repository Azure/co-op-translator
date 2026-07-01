# CLI Reference

Co-op Translator installib need käsurea algpunktid:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Käsud `translate`, `evaluate`, `migrate-links` ja `co-op-review` väljastavad juhtimise läbi `co_op_translator.__main__`, mis valib käsu teostuse lähtudes käivitatud skripti nimest. MCP server kasutab otse `co_op_translator.mcp.server`.

Kui otsustate CLI, Python API ja MCP vahel, alustage lehega [Choose Your Workflow](workflows.md).

## First-Time CLI Flow

Alustage siit, kui kasutate Co-op Translatorit terminalist:

1. Konfigureerige LLM-teenuse pakkuja vastavalt juhisele lehel [Configuration](configuration.md).
2. Valige sisu tüüp, mida soovite tõlkida.
3. Käivitage esmalt fookustatud käsk, näiteks ainult Markdowni tõlge.
4. Kasutage suurte repositooriumi muutuste puhul enne kirjutamist `--dry-run`.
5. Kasutage tõlke järel struktuuri ja värskuse kontrollimiseks `co-op-review`.

| Goal | Command to start with |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | Configure the [MCP Server](mcp.md) instead of running CLI commands directly. |

## translate

Tõlgib Markdown-faile, märkmikke ja pilditeksti ühte või mitmesse sihtkeelde.

```bash
translate -l "ko ja fr"
```

### Common examples

Tõlgi ainult Markdown:

```bash
translate -l "de" -md
```

Tõlgi ainult märkmikud:

```bash
translate -l "zh-CN" -nb
```

Tõlgi Markdown ja pildid:

```bash
translate -l "pt-BR" -md -img
```

Uuenda olemasolevaid tõlkeid, kustutades ja uuesti luues need:

```bash
translate -l "ko" -u
```

Käivita ilma interaktiivsete küsimusteta:

```bash
translate -l "ko ja" -md -y
```

Salvesta logid:

```bash
translate -l "ko" -s
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Tühikuga eraldatud keeltsüklid, näiteks `"es fr de"`, või `"all"`. |
| `-r`, `--root-dir` | No | Projekti juurkataloog. Vaikeväärtus on jooksva kataloog. |
| `-u`, `--update` | No | Kustuta valitud keelte olemasolevad tõlked ja loo need uuesti. |
| `-img`, `--images` | No | Tõlgi ainult pildifailid. |
| `-md`, `--markdown` | No | Tõlgi ainult Markdown-failid. |
| `-nb`, `--notebook` | No | Tõlgi ainult Jupyter märkmikufailid. |
| `-d`, `--debug` | No | Lülita konsoolis sisse silumise logimine. |
| `-s`, `--save-logs` | No | Salvesta DEBUG-taseme logid kataloogi `<root-dir>/logs/`. |
| `-x`, `--fix` | No | Tõlgi madala usaldusvõimalusega Markdown-failid ümber eelnevate hindamistulemuste põhjal. |
| `-c`, `--min-confidence` | No | Usalduskünnis `--fix` jaoks. Vaikeväärtus on `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Lisa või peata masina tõlketeatisi. CLI puhul vaikimisi lubatud. |
| `-f`, `--fast` | No | Aegunud kiire pildirežiim. |
| `-y`, `--yes` | No | Kinnita automaatselt promptid, kasulik CI puhul. |
| `--repo-url` | No | Repositooriumi URL, mida kasutatakse README keelte tabeli harva-sõelumisalas. |
| `--migrate-language-folders` | No | Nimeta ümber vananenud alias-kaustad, näiteks `cn` või `tw`, kanoniliste BCP 47 kaustadeks. |
| `--dry-run` | No | Eelvaade keelekaustade migratsioonist ja tõlkehinnangutest ilma failide kirjutamiseta. |

Kui tüübivlippi ei anta, töötleb `translate` Markdowni, märkmikke ja pilte. Piltide tõlge nõuab Azure AI Vision konfigureerimist.

## evaluate

Hindab tõlgitud Markdowni kvaliteeti ühe keele jaoks.

!!! warning "Eksperimentaalne"
    `evaluate` on eksperimentaalne. See võib kasutada reeglil põhinevaid ja LLM-põhiseid kvaliteedikontrolle, kirjutab hindamistulemused tõlke metaandmetesse ning selle skoorimudel ja metaandmete käitumine võivad muutuda.

```bash
evaluate -l "ko"
```

### Common examples

Kasuta rangemat madala usaldusväärtuse läve:

```bash
evaluate -l "es" -c 0.8
```

Käivita ainult reeglil põhinevad kontrollid:

```bash
evaluate -l "fr" -f
```

Käivita ainult LLM-põhised kontrollid:

```bash
evaluate -l "ja" -D
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Üksikulise keele kood, mida hinnata. Alias-koodid normaliseeritakse. |
| `-r`, `--root-dir` | No | Projekti juurkataloog. Vaikeväärtus on jooksva kataloog. |
| `-c`, `--min-confidence` | No | Künnis, mida kasutatakse madala usaldusväärtusega tõlgete loetlemisel. Vaikeväärtus on `0.7`. |
| `-d`, `--debug` | No | Lülita sisse silumislogimine. |
| `-s`, `--save-logs` | No | Salvesta DEBUG-taseme logid kataloogi `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Ainult reeglil põhinev hindamine. |
| `-D`, `--deep` | No | Ainult LLM-põhine hindamine. |

Vaikimisi kasutab `evaluate` nii reeglipõhist kui ka LLM-põhist hindamist. Tulemused kirjutatakse tõlke metaandmetesse ja koondatakse konsoolis.

## co-op-review

Käivita deterministlikke tõlke hoolduskontrolle ilma API mandaatideta.

!!! note "Beeta"
    `co-op-review` on beetafaasis deterministlik ülevaatekäsk. See ei kutsu mudeleid ega kirjuta faile, kuid selle kontrollid ja leitud probleemide väljundiskeem võivad areneda.

```bash
co-op-review -l "ko"
```

### Common examples

Vaata üle korea ja jaapani tõlked jooksvast kataloogist:

```bash
co-op-review -l "ko ja"
```

Vaata üle konkreetne projekti juur:

```bash
co-op-review -l "fr" -r ./my-course
```

Vaata üle ainult lähtefaile, mis on muutunud võrreldes alusrefiga:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Trüki CI kokkuvõtete jaoks GitHub-vorminguline Markdown:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | No | Keel, mida üle vaadata. Võib esitada mitu korda või tühikuga eraldatuna. Vaikimisi kõik avastatud tõlke keeled. |
| `-r`, `--root-dir` | No | Projekti juurkataloog. Vaikeväärtus on jooksva kataloog. |
| `--changed-from` | No | Git-ref, mida kasutatakse ülevaate piiramiseks muutunud lähtefailidele. |
| `--format` | No | Väljundi formaat: `text` või `github`. Vaikeväärtus on `text`. |

`co-op-review` kontrollib hetkel puuduvaid tõlgitud faile, puuduvat või aegunud tõlke metaandmeid, Markdowni frontmatteri ja koodifensi terviklikkust, vigast tõlgitud märkmiku JSON-i ning puuduvaid kohalikke Markdown- või pildilingi sihtpunkte. Puuduvad lingid on vaikimisi hoiatused; struktuuri- ja värskusprobleemid peatavad käsu ebaõnnestununa.

## co-op-translator-mcp

Käivita Co-op Translatori MCP server agentide, redigeerijate ja MCP-ühilduvate klientide jaoks.

```bash
co-op-translator-mcp
```

Vaiketransport on `stdio`. Vaata kliendi konfigureerimise, tööriistade, ressursside ja ohutusmärkuste kohta juhendit [MCP Server](mcp.md).

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, või `sse`. Vaikeväärtus on `stdio`. |

## migrate-links

Töötle tõlgitud Markdown-faile uuesti ja uuenda märkmike linke nii, et need osutaksid tõlgitud märkmikele, kui need on saadaval.

```bash
migrate-links -l "ko ja"
```

### Common examples

Eelvaata lingi uuendusi:

```bash
migrate-links -l "ko" --dry-run
```

Töötle kõiki toetatud keeli ilma kinnitusteta:

```bash
migrate-links -l "all" -y
```

Kirjuta lingid ümber ainult siis, kui tõlgitud märkmikud olemas:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Tühikuga eraldatud keeltsüklid või `"all"`. |
| `-r`, `--root-dir` | No | Projekti juurkataloog. Vaikeväärtus on jooksva kataloog. |
| `--image-dir` | No | Tõlgitud piltide kataloog juure suhtes. Vaikeväärtus on `translated_images`. |
| `--dry-run` | No | Näita faile, mida muudetakse, kirjutamata muudatusi. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Kasuta algset märkmiku linki, kui tõlgitud märkmikuid pole. Vaikimisi lubatud. |
| `-d`, `--debug` | No | Lülita sisse silumislogimine. |
| `-s`, `--save-logs` | No | Salvesta DEBUG-taseme logid kataloogi `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Kinnita automaatselt promptid, kui töödeldakse kõiki keeli. |

## Environment

Kõik käsud nõuavad ühe konfigureeritud LLM-teenuse pakkuja:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Või OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Piltide tõlge nõuab lisaks Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Output layout

Tekstide tõlked kirjutatakse kataloogi:

```text
translations/<language-code>/<original-path>
```

Tõlgitud pildiväljund kirjutatakse kataloogi:

```text
translated_images/<language-code>/<original-path>
```

Näiteks, kui tõlkida `README.md` ja `docs/setup.md` korea keelde, tekib:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Copy-Paste CLI Examples

Tõlgi Markdown kolmeks keeleks:

```bash
translate -l "ko ja fr" -md
```

Tõlgi ainult märkmikud:

```bash
translate -l "zh-CN" -nb
```

Tõlgi ainult pildid:

```bash
translate -l "pt-BR" -img
```

Eelvaata Markdowni tõlget ilma failide kirjutamiseta:

```bash
translate -l "de es" -md --dry-run
```

Paranda madala usaldusväärtusega Markdown-tõlkeid:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Käivita CI-sõbralik Markdowni tõlge:

```bash
translate -l "ko ja" -md -y -s
```

Vaata üle tõlgitud väljund:

```bash
co-op-review -l "ko ja"
```

Eelvaata lingi migratsiooni:

```bash
migrate-links -l "ko" --dry-run
```