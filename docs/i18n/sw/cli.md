# Marejeo ya CLI

Co-op Translator huweka viingilio vifuatavyo vya mstari wa amri:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Amri za `translate`, `evaluate`, `migrate-links`, na `co-op-review` zinapitishwa kupitia `co_op_translator.__main__`, ambayo inachagua utekelezaji wa amri kulingana na jina la skripti iliyotekelezwa. Server ya MCP inatumia `co_op_translator.mcp.server` moja kwa moja.

Ikiwa unatazama kati ya CLI, Python API, na MCP, anza na [Chagua Mtiririko Wako](workflows.md).

## Matokeo ya Konsoli

Terminali zenye uingiliano zinatumia uundaji wa Rich kwa kichwa cha amri, maendeleo, na muhtasari. Matokeo ya CI na yasiyo ya kuingiliana yanarejeshwa moja kwa moja kuwa maandishi ya kawaida.

Weka `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` kulazimisha matokeo ya maandishi, au `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` kulazimisha matokeo ya Rich. Weka `CO_OP_TRANSLATOR_NO_PROGRESS=1` ili kuweka muhtasari huku ukificha mabara ya maendeleo yanayoonyesha.

Tumia `translate --json-events progress.ndjson` wakati mfumo mwingine unahitaji maendeleo yanayosomwa na mashine. CLI itaendelea kuonyesha matokeo kwa wanadamu, wakati faili ya NDJSON itapokea matukio ya toleo `co-op.translation.event.v1` yenye nyanja thabiti kama `type`, `stage_key`, `completed`, `total`, na `current_path`.





## Mtiririko wa Mara ya Kwanza wa CLI

Anza hapa ikiwa unatumia Co-op Translator kutoka kwenye terminali:

1. Sanidi mtoa huduma wa LLM kama ilivyoelezwa katika [Usanidi](configuration.md).
2. Chagua aina ya maudhui unayotaka kutafsiri.
3. Endesha amri iliyoelekezwa kwanza, kama tafsiri ya Markdown pekee.
4. Tumia `--dry-run` kabla ya mabadiliko makubwa ya hazina (repository).
5. Tumia `co-op-review` baada ya tafsiri ili kukagua muundo na ikiwa tafsiri ni za hivi karibuni.

| Lengo | Amri ya kuanza nayo |
| --- | --- |
| Tafsiri nyaraka za Markdown | `translate -l "ko" -md` |
| Tafsiri daftari (notebooks) | `translate -l "ko" -nb` |
| Tafsiri maandishi ya picha | `translate -l "ko" -img` |
| Angalia kazi bila kuandika faili | `translate -l "ko" -md --dry-run` |
| Pitia tafsiri zilizopo | `co-op-review -l "ko"` |
| Sasisha viungo vya notebook na Markdown | `migrate-links -l "ko" --dry-run` |
| Fungua zana kwa mteja wa MCP | Sanidi [MCP Server](mcp.md) badala ya kuendesha amri za CLI moja kwa moja. |

## translate

Tafsiri faili za Markdown, notebooks, na maandishi ya picha katika lugha moja au zaidi za lengo.

```bash
translate -l "ko ja fr"
```

### Mifano ya kawaida

Tafsiri Markdown pekee:

```bash
translate -l "de" -md
```

Translate only notebooks:

```bash
translate -l "zh-CN" -nb
```

Translate Markdown and images:

```bash
translate -l "pt-BR" -md -img
```

Sasisha tafsiri zilizopo kwa kuzifuta na kuzizalisha upya:

```bash
translate -l "ko" -u
```

Run without interactive prompts:

```bash
translate -l "ko ja" -md -y
```

Save logs:

```bash
translate -l "ko" -s
```

Write structured progress events:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Chaguzi

| Chaguo | Inahitajika | Maelezo |
| --- | --- | --- |
| `-l`, `--language-codes` | Ndiyo | Msimbo wa lugha umewekwa kwa nafasi, kama `"es fr de"`, au `"all"`. |
| `-r`, `--root-dir` | Hapana | Mzizi wa mradi. Kwa kawaida ni saraka ya sasa. |
| `-u`, `--update` | Hapana | Futa tafsiri zilizopo kwa lugha zilizochaguliwa na uzitengeneze upya. |
| `-img`, `--images` | Hapana | Tafsiri faili za picha pekee. |
| `-md`, `--markdown` | Hapana | Tafsiri faili za Markdown pekee. |
| `-nb`, `--notebook` | Hapana | Tafsiri faili za Jupyter notebook pekee. |
| `-d`, `--debug` | Hapana | Washa uandishi wa kumbukumbu za uandaaji kwa konsoli. |
| `-s`, `--save-logs` | Hapana | Hifadhi logi za kiwango cha DEBUG chini ya `<root-dir>/logs/`. |
| `--json-events` | Hapana | Andika matukio ya maendeleo ya tafsiri yanayosomwa na mashine kama NDJSON. |
| `-x`, `--fix` | Hapana | Tafsiri upya faili za Markdown zenye imani ndogo kulingana na matokeo ya tathmini ya awali. |
| `-c`, `--min-confidence` | Hapana | Kizingiti cha uaminifu kwa `--fix`. Kiasi asilia ni `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Hapana | Ongeza au zima taarifa za kutaja tafsiri za mashine. Kwa chaguo asilia zimewezeshwa katika CLI. |
| `-f`, `--fast` | Hapana | Mode ya picha ya haraka ambayo imepitwa (deprecated). |
| `-y`, `--yes` | Hapana | Thibitisha maswali moja kwa moja, inafaa kwa CI. |
| `--repo-url` | Hapana | URL ya hazina inayotumika kwenye ushauri wa sparse-checkout wa jedwali la lugha la README. |
| `--migrate-language-folders` | Hapana | Badilisha majina ya folda za utangulizi, kama `cn` au `tw`, kwenda kwenye folda za BCP 47 rasmi. |
| `--dry-run` | Hapana | Angalia mwonekano wa uhamishaji wa folda za lugha na makadirio ya tafsiri bila kuandika faili. |

Ikiwa hakuna bendera ya aina iliyotolewa, `translate` itashughulikia Markdown, notebooks, na picha. Tafsiri ya picha inahitaji usanidi wa Azure AI Vision.

## evaluate

Tathmini ubora wa tafsiri za Markdown kwa lugha moja.

!!! warning "Jaribio"
    `evaluate` ni jaribio. Inaweza kutumia ukaguzi wa ubora unaotegemea sheria na ule unaotegemea LLM, inaandika matokeo ya tathmini ndani ya metadata ya tafsiri, na modeli yake ya upimaji na tabia ya metadata zinaweza kubadilika.

```bash
evaluate -l "ko"
```

### Mifano ya kawaida

Tumia kizingiti kali zaidi cha imani ndogo:

```bash
evaluate -l "es" -c 0.8
```

Run rule-based checks only:

```bash
evaluate -l "fr" -f
```

Run LLM-based checks only:

```bash
evaluate -l "ja" -D
```

### Chaguzi

| Chaguo | Inahitajika | Maelezo |
| --- | --- | --- |
| `-l`, `--language-code` | Ndiyo | Msimbo mmoja wa lugha wa kutathmini. Msimbo wa jina mbadala unasawazishwa. |
| `-r`, `--root-dir` | Hapana | Mzizi wa mradi. Kwa kawaida ni saraka ya sasa. |
| `-c`, `--min-confidence` | Hapana | Kizingiti kinachotumika wakati wa kuorodhesha tafsiri zenye imani ndogo. Kiasi asilia ni `0.7`. |
| `-d`, `--debug` | Hapana | Washa uandishi wa kumbukumbu za uandaaji. |
| `-s`, `--save-logs` | Hapana | Hifadhi logi za kiwango cha DEBUG chini ya `<root-dir>/logs/`. |
| `-f`, `--fast` | Hapana | Tathmini kwa msingi wa sheria pekee. |
| `-D`, `--deep` | Hapana | Tathmini kwa msingi wa LLM pekee. |

Kwa chaguo asilia, `evaluate` inatumia tathmini za msingi wa sheria na za msingi wa LLM. Matokeo yanaandikwa ndani ya metadata ya tafsiri na huhitimishwa kwenye konsoli.

## co-op-review

Endesha ukaguzi thabiti wa matengenezo ya tafsiri bila vyeti vya API.

!!! note "Beta"
    `co-op-review` ni amri ya mapitio thabiti katika awamu ya beta. Haipigi watoa huduma za modeli au haileti faili, lakini ukaguzi wake na muundo wa matokeo ya masuala yanaweza kubadilika.

```bash
co-op-review -l "ko"
```

### Mifano ya kawaida

Pitia tafsiri za Kikorea na Kijapani kutoka saraka ya sasa:

```bash
co-op-review -l "ko ja"
```

Pitia mzizi maalum wa mradi:

```bash
co-op-review -l "fr" -r ./my-course
```

Pitia README pekee baada ya tafsiri ya README pekee:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` haishiriki hati nyingine na README zilizoko ndani. Inashindwa ikiwa `README.md` ya mzizi haipo. Ikitumika pamoja na `--changed-from`, hupitia README pekee wakati faili hiyo ya chanzo imebadilika. Tafsiri ya README pekee inabaki isibadilishe README ya chanzo, ikijumuisha alama yoyote za sehemu zilizosambazwa.




Pitia faili za chanzo tu ambazo zimebadilika dhidi ya rejea ya msingi:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Chapisha matokeo ya Markdown ya mtindo wa GitHub kwa muhtasari wa CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Chaguzi

| Chaguo | Inahitajika | Maelezo |
| --- | --- | --- |
| `-l`, `--language-code` | Hapana | Msimbo wa lugha wa kupitia. Unaweza kupitishwa mara nyingi au kama thamani iliyotenganishwa kwa nafasi. Kwa chaguo asilia ni lugha zote zilizogunduliwa za tafsiri. |
| `-r`, `--root-dir` | Hapana | Mzizi wa mradi. Kwa kawaida ni saraka ya sasa. |
| `--changed-from` | Hapana | Rejea ya Git inayotumika kupunguza mapitio kwa faili za chanzo zilizobadilika. |
| `--readme-only` | Hapana | Pitia tu tafsiri ya `README.md` ya mzizi. |
| `--format` | Hapana | Muundo wa pato: `text` au `github`. Kawaida ni `text`. |

`co-op-review` kwa sasa inakagua faili za tafsiri zilizokosekana, metadata ya tafsiri iliyokosekana au iliyostaafu, frontmatter ya Markdown na uadilifu wa fence za nambari (code fence), JSON isiyo sahihi ya notebook iliyotafsiriwa, na malengo ya viungo vya ndani vya Markdown au picha vinavyokosekana. Viungo vinavyokosekana ni onyo kwa chaguo asilia; matatizo ya muundo na ya ukuaji wa uhalisi yanasababisha amri kushindwa.

## co-op-translator-mcp

Endesha server ya MCP ya Co-op Translator kwa maajenti, wahariri, na wateja wanaolingana na MCP.

```bash
co-op-translator-mcp
```

Usafirishaji wa msingi ni `stdio`. Angalia mwongozo wa [MCP Server](mcp.md) kwa usanidi wa mteja, zana, rasilimali, na vidokezo vya usalama.

### Chaguzi

| Chaguo | Inahitajika | Maelezo |
| --- | --- | --- |
| `--transport` | Hapana | Usafirishaji wa MCP: `stdio`, `streamable-http`, au `sse`. Kawaida ni `stdio`. |

## migrate-links

Fanyazindua upya faili za Markdown zilizotafsiriwa na sasisha viungo vya notebook ili vitumie notebooks zilizotafsiriwa pale zinapopatikana.

```bash
migrate-links -l "ko ja"
```

### Mifano ya kawaida

Angalia mapitisho ya viungo:

```bash
migrate-links -l "ko" --dry-run
```

Shughulikia lugha zote zinazoungwa mkono bila uthibitisho:

```bash
migrate-links -l "all" -y
```

Badilisha viungo tu wakati notebooks zilizotafsiriwa zinapatikana:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Chaguzi

| Chaguo | Inahitajika | Maelezo |
| --- | --- | --- |
| `-l`, `--language-codes` | Ndiyo | Msimbo wa lugha umewekwa kwa nafasi, au `"all"`. |
| `-r`, `--root-dir` | Hapana | Mzizi wa mradi. Kwa kawaida ni saraka ya sasa. |
| `--image-dir` | Hapana | Saraka ya picha zilizotafsiriwa kulingana na mzizi. Kawaida ni `translated_images`. |
| `--dry-run` | Hapana | Onyesha faili ambazo zingekuwa zimebadilika bila kuandika masasisho. |
| `--fallback-to-original`, `--no-fallback-to-original` | Hapana | Tumia viungo vya notebook vya awali wakati notebooks zilizotafsiriwa hazipo. Zimewezeshwa kwa chaguo asilia. |
| `-d`, `--debug` | Hapana | Washa uandishi wa kumbukumbu za uandaaji. |
| `-s`, `--save-logs` | Hapana | Hifadhi logi za kiwango cha DEBUG chini ya `<root-dir>/logs/`. |
| `-y`, `--yes` | Hapana | Thibitisha maswali moja kwa moja unapoendelea na lugha zote. |

## Mazingira

Wakati amri inahitaji nyaraka za mtoa huduma, sanidi mojawapo ya seti hizi za watoa huduma. `translate --dry-run` na `co-op-review` hazihitaji nyaraka za mtoa huduma:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Au OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Au Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Tafsiri ya picha pia inahitaji Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Mpangilio wa pato

Tafsiri za maandishi zinaandikwa chini ya:

```text
translations/<language-code>/<original-path>
```

Pato la picha zilizotafsiriwa linaandikwa chini ya:

```text
translated_images/<language-code>/<original-path>
```

Kwa mfano, kutafsiri `README.md` na `docs/setup.md` kwenda Kikorea kunazalisha:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Mifano ya CLI ya Nakili na Bandika

Tafsiri Markdown katika lugha tatu:

```bash
translate -l "ko ja fr" -md
```

Translate notebooks only:

```bash
translate -l "zh-CN" -nb
```

Tafsiri picha pekee:

```bash
translate -l "pt-BR" -img
```

Angalia tafsiri ya Markdown bila kuandika faili:

```bash
translate -l "de es" -md --dry-run
```

Rekebisha tafsiri za Markdown zenye imani ndogo:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Endesha tafsiri ya Markdown inayofaa kwa CI:

```bash
translate -l "ko ja" -md -y -s
```

Pitia matokeo yaliyotafsiriwa:

```bash
co-op-review -l "ko ja"
```

Angalia uhamisho wa viungo:

```bash
migrate-links -l "ko" --dry-run
```