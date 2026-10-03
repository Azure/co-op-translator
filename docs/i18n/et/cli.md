# CLI viide

Co-op Translator paigaldab järgmised käsurea käivituspunktid:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

The `translate`, `evaluate`, `migrate-links`, and `co-op-review` käsud kutsutakse läbi `co_op_translator.__main__`, mis valib käsu implementeerimise vastavalt käivitatud skripti nimele. MCP server kasutab `co_op_translator.mcp.server` otse.

Kui otsustate CLI, Python API ja MCP vahel, alustage [Vali töövoog](workflows.md).

## Konsooli väljund

Interaktiivsed terminalid kasutavad Rich-vormindust käsu päise, edenemise ja kokkuvõtete jaoks. CI ja mitte-interaktiivne väljund langevad automaatselt tagasi tavalisele tekstile.

Määrake `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` tavalise väljundi sundimiseks või `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` Rich-väljundi sundimiseks. Määrake `CO_OP_TRANSLATOR_NO_PROGRESS=1`, et säilitada kokkuvõtted, kuid peita elavaid edenemisribasid.

Kasutage `translate --json-events progress.ndjson`, kui mõni teine süsteem vajab
masinloetavat edenemist. CLI jätkab inimeste jaoks mõeldud väljundi kuvamist, samal ajal
kui NDJSON-fail saab versioonitud sündmusi `co-op.translation.event.v1`, mis sisaldavad
stabiilseid välju nagu `type`, `stage_key`, `completed`, `total` ja
`current_path`.

## Esmakordne CLI-töövoog

Alustage siit, kui kasutate Co-op Translatort terminalist:

1. Seadistage LLM-teenuse pakkuja nagu on kirjeldatud [Konfiguratsioonis](configuration.md).
2. Valige sisutüüp, mida soovite tõlkida.
3. Käivitage esmalt fokuseeritud käsk, näiteks ainult Markdowni tõlge.
4. Kasutage enne suuri repositooriumi muudatusi `--dry-run`.
5. Pärast tõlkimist kasutage `co-op-review` struktuuri ja ajakohasuse kontrollimiseks.

| Eesmärk | Käsk alustamiseks |
| --- | --- |
| Markdowni dokumentide tõlkimine | `translate -l "ko" -md` |
| Märkmike tõlkimine | `translate -l "ko" -nb` |
| Pilditeksti tõlkimine | `translate -l "ko" -img` |
| Töö eelvaade ilma failide salvestamiseta | `translate -l "ko" -md --dry-run` |
| Olemasolevate tõlgete ülevaatus | `co-op-review -l "ko"` |
| Märkmike ja Markdowni linkide uuendamine | `migrate-links -l "ko" --dry-run` |
| Tööriistade pakkumine MCP kliendile | Konfigureerige [MCP-server](mcp.md) selle asemel, et CLI käske otse käivitada. |

## translate

Tõlgib Markdowni faile, märkmikke ja pilditeksti ühte või mitmesse sihtkeelde.

```bash
translate -l "ko ja fr"
```

### Tüüpilised näited

Tõlgi ainult Markdown:

```bash
translate -l "de" -md
```

Tõlgi ainult märkmikke:

```bash
translate -l "zh-CN" -nb
```

Tõlgi Markdowni ja pilte:

```bash
translate -l "pt-BR" -md -img
```

Uuenda olemasolevaid tõlkeid, kustutades ja luues need uuesti:

```bash
translate -l "ko" -u
```

Käivita ilma interaktiivsete kinnituseta:

```bash
translate -l "ko ja" -md -y
```

Salvesta logid:

```bash
translate -l "ko" -s
```

Kirjuta struktureeritud edenemissündmusi:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Valikud

| Valik | Nõutav | Kirjeldus |
| --- | --- | --- |
| `-l`, `--language-codes` | Jah | Tühikuga eraldatud keelekoodid, näiteks "es fr de", või "all". |
| `-r`, `--root-dir` | Ei | Projekti juur. Vaikeväärtus on praegune kataloog. |
| `-u`, `--update` | Ei | Kustutab valitud keelte olemasolevad tõlked ja loob need uuesti. |
| `-img`, `--images` | Ei | Tõlgi ainult pildifaile. |
| `-md`, `--markdown` | Ei | Tõlgi ainult Markdown-faile. |
| `-nb`, `--notebook` | Ei | Tõlgi ainult Jupyteri märkmikke. |
| `-d`, `--debug` | Ei | Luba debug-tasemel logimine konsoolis. |
| `-s`, `--save-logs` | Ei | Salvesta DEBUG-taseme logid asukohta `<root-dir>/logs/`. |
| `--json-events` | Ei | Kirjuta masinloetavad tõlke edenemissündmused NDJSON-ina. |
| `-x`, `--fix` | Ei | Uuesti tõlgi madala usaldusega Markdown-failid varasemate hindamistulemite põhjal. |
| `-c`, `--min-confidence` | Ei | Usalduse lävi `--fix` jaoks. Vaikeväärtus on `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Ei | Lisa või peida masintõlke vastutusest teatamist. CLI-s on see vaikimisi lubatud. |
| `-f`, `--fast` | Ei | Aegunud kiire pildirežiim. |
| `-y`, `--yes` | Ei | Automaatne kinnitamine, kasulik CI puhul. |
| `--repo-url` | Ei | Repositooriumi URL, mida kasutatakse README keelte tabeli sparse-checkout soovituses. |
| `--migrate-language-folders` | Ei | Nimeta ümber pärandalias kaustad, nagu `cn` või `tw`, kanonilisteks BCP 47 kaustadeks. |
| `--dry-run` | Ei | Eelvaade keelekaustade migratsioonist ja tõlkemahust ilma failide kirjutamiseta. |

Kui tüübi lipik pole antud, töötleb `translate` Markdowni, märkmikke ja pilte. Pildi tõlkimine nõuab Azure AI Vision konfiguratsiooni.

## evaluate

Hinda tõlgitud Markdowni kvaliteeti ühe keele jaoks.

!!! warning "Eksperimentaalne"
    `evaluate` on eksperimentaalne. See võib kasutada reeglitel põhinevaid ja LLM-põhiseid kvaliteedikontrolle, kirjutab hindamistulemused tõlke metaandmetesse ning selle skoorimismudel ja metaandmete käitumine võivad muutuda.

```bash
evaluate -l "ko"
```

### Näited

Kasuta rangemat madala usalduse läve:

```bash
evaluate -l "es" -c 0.8
```

Käivita ainult reeglitel põhinevad kontrollid:

```bash
evaluate -l "fr" -f
```

Käivita ainult LLM-põhised kontrollid:

```bash
evaluate -l "ja" -D
```

### Valikud

| Valik | Nõutav | Kirjeldus |
| --- | --- | --- |
| `-l`, `--language-code` | Jah | Üksik keelekood hindamiseks. Aliase koodid normaliseeritakse. |
| `-r`, `--root-dir` | Ei | Projekti juur. Vaikeväärtus on praegune kataloog. |
| `-c`, `--min-confidence` | Ei | Lävi, mida kasutatakse madala usalduse tõlgete loetlemisel. Vaikeväärtus on `0.7`. |
| `-d`, `--debug` | Ei | Luba debug-logimine. |
| `-s`, `--save-logs` | Ei | Salvesta DEBUG-taseme logid asukohta `<root-dir>/logs/`. |
| `-f`, `--fast` | Ei | Ainult reeglitel põhinev hindamine. |
| `-D`, `--deep` | Ei | Ainult LLM-põhine hindamine. |

Vaikimisi kasutab `evaluate` nii reeglitel põhinevat kui ka LLM-põhist hindamist. Tulemused kirjutatakse tõlke metaandmetesse ja kokku võetakse konsoolis.

## co-op-review

Käivita deterministlikud tõlke hoolduse kontrollid ilma API volitusteta.

!!! note "Beeta"
    `co-op-review` on beeta deterministlik ülevaatekäsk. See ei kutsu mudelite pakkujaid ega kirjuta faile, kuid selle kontrollid ja probleemide väljundi skeem võivad areneda.

```bash
co-op-review -l "ko"
```

### Näited

Kontrolli Korea ja Jaapani tõlkeid praegusest kataloogist:

```bash
co-op-review -l "ko ja"
```

Kontrolli konkreetset projekti juurt:

```bash
co-op-review -l "fr" -r ./my-course
```

Kontrolli vaid README-d pärast ainult README tõlget:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` jätab muud dokumendid ja pesastatud README-d tähelepanuta. See ebaõnnestub, kui juurkataloogi
`README.md` puudub. Koos `--changed-from`-iga vaatleb see README-d ainult
siis, kui see lähtefail on muutunud. Ainult README tõlge jätab lähte-README
muutumatuks, kaasa arvatud kõik jagatud-sektsiooni märgendid.

Kontrolli ainult lähtefaile, mis on muutunud võrreldes baas-refiga:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Prindi GitHub-i stiilis Markdown-väljund CI kokkuvõtete jaoks:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Valikud

| Valik | Nõutav | Kirjeldus |
| --- | --- | --- |
| `-l`, `--language-code` | Ei | Keelekood, mida üle vaadata. Võib edastada mitu korda või tühikuga eraldatud väärtusena. Vaikimisi kõik leitud tõlkekeeled. |
| `-r`, `--root-dir` | Ei | Projekti juur. Vaikeväärtus on praegune kataloog. |
| `--changed-from` | Ei | Git ref, mida kasutatakse ülevaate piiramiseks muudetud lähtefailidele. |
| `--readme-only` | Ei | Vaata ainult juurkataloogi `README.md` tõlget. |
| `--format` | Ei | Väljundi formaat: `text` või `github`. Vaikeväärtus on `text`. |

`co-op-review` kontrollib praegu puuduvate tõlgitud failide, puuduvate või aegunut tõlke metaandmete, Markdowni frontmatteri ja koodiaia terviklikkuse, vigase tõlgitud märkmiku JSON-i ning puuduvaid kohalikke Markdowni või pildilinke. Puuduvad lingid on vaikimisi hoiatused; struktuuri- ja ajakohasuse probleemid põhjustavad käsu nurjumise.

## co-op-translator-mcp

Käivitage Co-op Translator MCP-server agentidele, redaktoritele ja MCP-ühilduvatele klientidele.

```bash
co-op-translator-mcp
```

Vaiketransport on `stdio`. Kliendi konfiguratsiooni, tööriistade, ressursside ja turvanõuete kohta vaadake juhendit [MCP-server](mcp.md).

### Valikud

| Valik | Nõutav | Kirjeldus |
| --- | --- | --- |
| `--transport` | Ei | MCP-transport: `stdio`, `streamable-http`, or `sse`. Vaikeväärtus on `stdio`. |

## migrate-links

Töödelda uuesti tõlgitud Markdown-faile ja uuendada märkmike linke nii, et need osutaksid tõlgitud märkmikele, kui need on olemas.

```bash
migrate-links -l "ko ja"
```

### Näited

Eelvaade lingi uuendustest:

```bash
migrate-links -l "ko" --dry-run
```

Töötle kõiki toetatud keeli ilma kinnitamiseta:

```bash
migrate-links -l "all" -y
```

Kirjuta lingid ümber ainult siis, kui tõlgitud märkmikud on olemas:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Valikud

| Valik | Nõutav | Kirjeldus |
| --- | --- | --- |
| `-l`, `--language-codes` | Jah | Tühikuga eraldatud keelekoodid või "all". |
| `-r`, `--root-dir` | Ei | Projekti juur. Vaikeväärtus on praegune kataloog. |
| `--image-dir` | Ei | Tõlgitud piltide kaust suhtelise tee suhtes juurest. Vaikeväärtus `translated_images`. |
| `--dry-run` | Ei | Näita faile, mida muudetaks, ilma et muudatusi kirjutataks. |
| `--fallback-to-original`, `--no-fallback-to-original` | Ei | Kasuta originaalseid märkmiku linke, kui tõlgitud märkmikud puuduvad. Vaikimisi lubatud. |
| `-d`, `--debug` | Ei | Luba debug-logimine. |
| `-s`, `--save-logs` | Ei | Salvesta DEBUG-taseme logid asukohta `<root-dir>/logs/`. |
| `-y`, `--yes` | Ei | Automaatne kinnitamine, kui töödeldakse kõiki keeli. |

## Keskkond

Kui käsu käivitamiseks on vaja pakkuja volitusi, seadistage üks neist pakkujakomplektidest. `translate --dry-run` ja `co-op-review` ei vaja pakkuja volitusi:

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

# Või Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Pilditõlkimiseks on lisaks vaja Azure AI Vision'i:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Väljundi paigutus

Tekstilised tõlked kirjutatakse siia:

```text
translations/<language-code>/<original-path>
```

Tõlgitud piltide väljund kirjutatakse siia:

```text
translated_images/<language-code>/<original-path>
```

Näiteks `README.md` ja `docs/setup.md` koreakeelde tõlkimine toodab:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Kopeeri-kleebi CLI näited

Tõlgi Markdown kolmele keelele:

```bash
translate -l "ko ja fr" -md
```

Tõlgi ainult märkmikke:

```bash
translate -l "zh-CN" -nb
```

Tõlgi ainult pilte:

```bash
translate -l "pt-BR" -img
```

Eelvaata Markdowni tõlget ilma failide kirjutamiseta:

```bash
translate -l "de es" -md --dry-run
```

Paranda madala usaldusega Markdowni tõlkeid:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Käivita CI-sõbralik Markdowni tõlge:

```bash
translate -l "ko ja" -md -y -s
```

Kontrolli tõlgitud väljundit:

```bash
co-op-review -l "ko ja"
```

Eelvaata linkide migratsiooni:

```bash
migrate-links -l "ko" --dry-run
```