# Marejeo ya CLI

Co-op Translator inasakinisha pointi hizi za kuingia kwenye mstari wa amri:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Amri `translate`, `evaluate`, `migrate-links`, na `co-op-review` zinapitishwa kupitia `co_op_translator.__main__`, ambayo inachagua utekelezaji wa amri kulingana na jina la skripti iliyoitwa. Seva ya MCP inatumia `co_op_translator.mcp.server` moja kwa moja.

Ikiwa unatafuta kati ya CLI, Python API, na MCP, anza na [Chagua Mtiririko wa Kazi](workflows.md).

## Mtiririko wa CLI kwa Mara ya Kwanza

Anza hapa ikiwa unatumia Co-op Translator kutoka kwa terminali:

1. Sanidi mtoa huduma wa LLM kama ilivyoelezwa kwenye [Usanidi](configuration.md).
2. Chagua aina ya maudhui unayotaka kutafsiri.
3. Kimbia amri yenye lengo maalum kwanza, kama tafsiri ya Markdown pekee.
4. Tumia `--dry-run` kabla ya mabadiliko makubwa kwenye hazina.
5. Tumia `co-op-review` baada ya kutafsiri ili kukagua muundo na usasisho.

| Lengo | Amri ya kuanza nayo |
| --- | --- |
| Tafsiri hati za Markdown | `translate -l "ko" -md` |
| Tafsiri daftari (notebooks) | `translate -l "ko" -nb` |
| Tafsiri maandishi ya picha | `translate -l "ko" -img` |
| Angalia kazi bila kuandika mafaili | `translate -l "ko" -md --dry-run` |
| Kagua tafsiri zilizopo | `co-op-review -l "ko"` |
| Sasisha viungo vya notebook na Markdown | `migrate-links -l "ko" --dry-run` |
| Weka zana kwa mteja wa MCP | Sanidi [Seva ya MCP](mcp.md) badala ya kukimbia amri za CLI moja kwa moja. |

## translate

Tafsiri mafaili ya Markdown, notebooks, na maandishi ya picha kwa lugha moja au zaidi za lugha lengwa.

```bash
translate -l "ko ja fr"
```

### Mifano ya kawaida

Tafsiri Markdown pekee:

```bash
translate -l "de" -md
```

Tafsiri notebooks pekee:

```bash
translate -l "zh-CN" -nb
```

Tafsiri Markdown na picha:

```bash
translate -l "pt-BR" -md -img
```

Sasisha tafsiri zilizopo kwa kuzifuta na kuzitengeneza upya:

```bash
translate -l "ko" -u
```

Kimbia bila maswali ya kuingiliana:

```bash
translate -l "ko ja" -md -y
```

Hifadhi kumbukumbu za logi:

```bash
translate -l "ko" -s
```

### Chaguzi

| Chaguo | Inahitajika | Maelezo |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Msimbo wa lugha uliotengwa kwa nafasi, kama `"es fr de"`, au `"all"`. |
| `-r`, `--root-dir` | No | Mizizi ya mradi. Kwa kawaida ni saraka ya sasa. |
| `-u`, `--update` | No | Futa tafsiri zilizopo kwa lugha zilizochaguliwa na uzizifanye upya. |
| `-img`, `--images` | No | Tafsiri tu mafaili ya picha. |
| `-md`, `--markdown` | No | Tafsiri tu mafaili ya Markdown. |
| `-nb`, `--notebook` | No | Tafsiri tu mafaili ya Jupyter notebook. |
| `-d`, `--debug` | No | Washa uandishi wa logi wa debug kwenye koni. |
| `-s`, `--save-logs` | No | Hifadhi logi za kiwango cha DEBUG chini ya `<root-dir>/logs/`. |
| `-x`, `--fix` | No | Tafsiri tena mafaili ya Markdown yenye uhakika mdogo kulingana na matokeo ya tathmini ya awali. |
| `-c`, `--min-confidence` | No | Kipimo cha uhakika kwa `--fix`. Kwa kawaida ni `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Ongeza au zima taarifa za kukanusha kuhusu tafsiri za mashine. Kwa kawaida zimewezeshwa kwenye CLI. |
| `-f`, `--fast` | No | Njia ya picha ya haraka (imepitwa na wakati). |
| `-y`, `--yes` | No | Thibitisha moja kwa moja maswali, ya msaada katika CI. |
| `--repo-url` | No | Repository URL used in the README languages table sparse-checkout advisory. |
| `--migrate-language-folders` | No | Badili majina ya saraka za nakala za zamani, kama `cn` au `tw`, kuwa saraka rasmi za BCP 47. |
| `--dry-run` | No | Onyesha awali uhamisho wa saraka za lugha na makisio ya tafsiri bila kuandika mafaili. |

If no type flag is provided, `translate` processes Markdown, notebooks, and images. Image translation requires Azure AI Vision configuration.

## evaluate

Tathmini ubora wa tafsiri za Markdown kwa lugha moja.

!!! warning "Experimental"
    `evaluate` ni jaribio. Inaweza kutumia ukaguzi wa ubora unaotegemea sheria na ukaguzi unaotegemea LLM, inaandika matokeo ya tathmini kwenye metadata ya tafsiri, na mfano wake wa upimaji na tabia ya metadata yanaweza kubadilika.

```bash
evaluate -l "ko"
```

### Mifano ya kawaida

Tumia kikomo kali zaidi cha uhakika mdogo:

```bash
evaluate -l "es" -c 0.8
```

Fanya ukaguzi unaotegemea sheria pekee:

```bash
evaluate -l "fr" -f
```

Fanya ukaguzi unaotegemea LLM pekee:

```bash
evaluate -l "ja" -D
```

### Chaguzi

| Chaguo | Inahitajika | Maelezo |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Msimbo mmoja wa lugha wa kutathmini. Mifupisho ya lugha (alias) inabadilishwa kuwa kawaida. |
| `-r`, `--root-dir` | No | Mizizi ya mradi. Kwa kawaida ni saraka ya sasa. |
| `-c`, `--min-confidence` | No | Kipimo kinachotumika wakati wa kuorodhesha tafsiri zenye uhakika mdogo. Kwa kawaida `0.7`. |
| `-d`, `--debug` | No | Washa uandishi wa logi za debug. |
| `-s`, `--save-logs` | No | Hifadhi logi za kiwango cha DEBUG chini ya `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Tathmini inayotegemea sheria pekee. |
| `-D`, `--deep` | No | Tathmini inayotegemea LLM pekee. |

Kwa chaguo la msingi, `evaluate` inatumia tathmini zote mbili: inayotegemea sheria na inayotegemea LLM. Matokeo yanaandikwa kwenye metadata ya tafsiri na yamefupishwa kwenye koni.

## co-op-review

Endesha ukaguzi thabiti wa matengenezo ya tafsiri bila cheti za API.

!!! note "Beta"
    `co-op-review` ni amri ya ukaguzi ya beta na thabiti. Haiitii watoa huduma za modeli au kuandika mafaili, lakini ukaguzi wake na muundo wa matokeo yanaweza kubadilika.

```bash
co-op-review -l "ko"
```

### Mifano ya kawaida

Kagua tafsiri za Kikorea na Kijapani kutoka saraka ya sasa:

```bash
co-op-review -l "ko ja"
```

Kagua mzizi maalum wa mradi:

```bash
co-op-review -l "fr" -r ./my-course
```

Kagua tu mafaili ya chanzo yaliyobadilika dhidi ya rejea ya msingi:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Chapisha matokeo ya Markdown yenye ladha ya GitHub kwa muhtasari za CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Chaguzi

| Chaguo | Inahitajika | Maelezo |
| --- | --- | --- |
| `-l`, `--language-code` | No | Msimbo wa lugha wa kukagua. Unaweza kupitishwa mara nyingi au kama thamani iliyoachwa kwa nafasi. Kwa kawaida ni lugha zote zilizogunduliwa za tafsiri. |
| `-r`, `--root-dir` | No | Mizizi ya mradi. Kwa kawaida ni saraka ya sasa. |
| `--changed-from` | No | Git ref used to limit review to changed source files. |
| `--format` | No | Muundo wa pato: `text` au `github`. Kwa kawaida `text`. |

`co-op-review` kwa sasa hukagua faili za tafsiri zilizokosekana, metadata ya tafsiri iliyokosekana au iliyokuwa ya zamani, ukamilifu wa frontmatter ya Markdown na mizingiro ya code fence, JSON ya notebook iliyotafsiriwa isiyo sahihi, na malengo ya viungo vya ndani vya Markdown au picha vinavyokosekana. Viungo vinavyokosekana ni onyo kwa kawaida; matatizo ya muundo na usasisho hupelekea amri kushindwa.

## co-op-translator-mcp

Endesha seva ya Co-op Translator MCP kwa maajenti, wahariri, na wateja wanaolingana na MCP.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [Seva ya MCP](mcp.md) guide for client configuration, tools, resources, and safety notes.

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

Fanyia tena kazi mafaili ya Markdown yaliyotafsiriwa na sasisha viungo vya notebook ili viweze kuelekeza kwa notebooks zilizotafsiriwa inapopatikana.

```bash
migrate-links -l "ko ja"
```

### Mifano ya kawaida

Angalia awali masasisho ya viungo:

```bash
migrate-links -l "ko" --dry-run
```

Fanyia kazi lugha zote zinazoungwa mkono bila uthibitisho:

```bash
migrate-links -l "all" -y
```

Rekebisha viungo tu wakati notebooks zilizotafsiriwa zipo:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Chaguzi

| Chaguo | Inahitajika | Maelezo |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Msimbo za lugha zilizoachwa kwa nafasi, au `"all"`. |
| `-r`, `--root-dir` | No | Mizizi ya mradi. Kwa kawaida ni saraka ya sasa. |
| `--image-dir` | No | Saraka ya picha zilizotafsiriwa kuhusiana na mizizi. Kwa kawaida `translated_images`. |
| `--dry-run` | No | Onyesha mafaili yangepobadilika bila kuandika masasisho. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Tumia viungo vya notebook vya awali wakati notebooks zilizotafsiriwa hazipo. Imewezeshwa kwa kawaida. |
| `-d`, `--debug` | No | Washa uandishi wa logi za debug. |
| `-s`, `--save-logs` | No | Hifadhi logi za kiwango cha DEBUG chini ya `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Thibitisha moja kwa moja maswali wakati ukisindika lugha zote. |

## Mazingira

Amri zote zinahitaji mtoa huduma wa LLM mmoja aliyesanidiwa:

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
```

Tafsiri ya picha pia inahitaji Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Muundo wa pato

Tafsiri za maandishi zinaandikwa chini ya:

```text
translations/<language-code>/<original-path>
```

Pato la picha zilizotafsiriwa linaandikwa chini ya:

```text
translated_images/<language-code>/<original-path>
```

Kwa mfano, kutafsiri `README.md` na `docs/setup.md` kwa Kikorea kunazalisha:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Mifano za Nakili-na-Bandika za CLI

Tafsiri Markdown kwa lugha tatu:

```bash
translate -l "ko ja fr" -md
```

Tafsiri notebooks pekee:

```bash
translate -l "zh-CN" -nb
```

Tafsiri picha pekee:

```bash
translate -l "pt-BR" -img
```

Angalia awali tafsiri ya Markdown bila kuandika mafaili:

```bash
translate -l "de es" -md --dry-run
```

Rekebisha tafsiri za Markdown zenye uhakika mdogo:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Endesha tafsiri ya Markdown inayofaa kwa CI:

```bash
translate -l "ko ja" -md -y -s
```

Kagua matokeo yaliyotafsiriwa:

```bash
co-op-review -l "ko ja"
```

Angalia awali uhamisho wa viungo:

```bash
migrate-links -l "ko" --dry-run
```