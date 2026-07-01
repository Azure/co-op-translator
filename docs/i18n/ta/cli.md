# CLI கையேடு

Co-op Translator இவை கட்டளை வரி நுழைவு புள்ளிகளை நிறுவுகிறது:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

The `translate`, `evaluate`, `migrate-links`, and `co-op-review` commands dispatch through `co_op_translator.__main__`, which selects the command implementation based on the invoked script name. The MCP server uses `co_op_translator.mcp.server` directly.

If you are deciding between CLI, Python API, and MCP, start with [உங்கள் பணித் நடைமுறையைத் தேர்ந்தெடுக்கவும்](workflows.md).

## முதன்முதலில் CLI பணிநடை

டெர்மினலில் Co-op Translator பயன்படுத்தினால் இங்கே தொடங்குங்கள்:

1. இடுக்கப்பட்டுள்ள [கட்டமைப்பு](configuration.md) வழிகாட்டுதலின் படி ஒரு LLM வழங்குநரை கட்டமைக்கவும்.
2. மாற்ற மொழி செய்ய விரும்பும் உள்ளடக்க வகையை தேர்வு செய்யுங்கள்.
3. முதலில் கவனம் மையமாக்கப்பட்ட கட்டளையை இயக்குங்கள்; உதாரணமாக Markdown மட்டும் மொழிபெயர்ப்பு.
4. பெரிய சேமகோப்புப் பரிமாற்றங்களுக்கு முன் `--dry-run` பயன்படுத்துங்கள்.
5. மொழிமாற்றத்திற்குப்பிறகு கட்டமைப்பு மற்றும் புதுமையைச் சோதிக்க `co-op-review` பயன்படுத்துங்கள்.

| நோக்கம் | தொடங்க உபயோகிக்க வேண்டிய கட்டளை |
| --- | --- |
| Markdown ஆவணங்களை மொழிபெயர்க்க | `translate -l "ko" -md` |
| நோட்புக் ஆவணங்களை மொழிபெயர்க்க | `translate -l "ko" -nb` |
| படத்தின் உரையை மொழிபெயர்க்க | `translate -l "ko" -img` |
| கோப்புகள் எழுதாமல் வேலைக்கு முன்னோட்டம் காண்பிக்க | `translate -l "ko" -md --dry-run` |
| நிலைத்து உள்ள மொழிபெயர்ப்புகளை மதிப்பாய்வு செய்ய | `co-op-review -l "ko"` |
| நோட்புக் மற்றும் Markdown லிங்குகளை புதுப்பிக்க | `migrate-links -l "ko" --dry-run` |
| MCP கிளையண்டிற்கு கருவிகளை வழங்க | CLI கட்டளைகள் நேரடியாக இயக்குவதைவிட [MCP சர்வர்](mcp.md) ஐ கட்டமைக்கவும். |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

```bash
translate -l "ko ja fr"
```

### பொதுவான உதாரணங்கள்

Markdown மட்டும் மொழிபெயரிக்க:

```bash
translate -l "de" -md
```

நோட்புக் மட்டும் மொழிபெயரிக்க:

```bash
translate -l "zh-CN" -nb
```

Markdown மற்றும் படங்களை மொழிபெயரிக்க:

```bash
translate -l "pt-BR" -md -img
```

இருந்து மொழிபெயர்ப்புகளை நீக்கி மறுபடியும் உருவாக்கி புதுப்பிக்க:

```bash
translate -l "ko" -u
```

இணையத் தூண்டுதல்களின்றி இயக்க:

```bash
translate -l "ko ja" -md -y
```

லாக்குகளை சேமிக்க:

```bash
translate -l "ko" -s
```

### விருப்பங்கள்

| விருப்பம் | தேவையா | விளக்கம் |
| --- | --- | --- |
| `-l`, `--language-codes` | ஆம் | இடைவெளியால் பிரிக்கப்பட்ட மொழி குறியீடுகள், உதாரணத்திற்கு `"es fr de"`, அல்லது `"all"`. |
| `-r`, `--root-dir` | இல்லை | திட்ட முதன்மை அடைவு. இயல்புநிலை தற்போதைய அடைவு. |
| `-u`, `--update` | இல்லை | தேர்ந்தெடுக்கப்பட்ட மொழிகளுக்கான உள்ளூர் மொழிபெயர்ப்புகளை நீக்கி மீண்டும் உருவாக்கும். |
| `-img`, `--images` | இல்லை | படக் கோப்புகளை மட்டுமே மொழிபெயர்க்க. |
| `-md`, `--markdown` | இல்லை | Markdown கோப்புகளை மட்டுமே மொழிபெயர்க்க. |
| `-nb`, `--notebook` | இல்லை | Jupyter நோட்புக் கோப்புகளை மொழிபெயர்க்க. |
| `-d`, `--debug` | இல்லை | கான்சோலில் டீபக் பதிவு செயல்படுத்தவும். |
| `-s`, `--save-logs` | இல்லை | DEBUG நிலை பதிவுகளை `<root-dir>/logs/` கீழாக சேமிக்கவும். |
| `-x`, `--fix` | இல்லை | முந்தைய மதிப்பீட்டு முடிவுகளின் அடிப்படையில் குறைந்த நம்பகத்தன்மையுள்ள Markdown கோப்புகளை மீண்டும் மொழிபெயர்க்க. |
| `-c`, `--min-confidence` | இல்லை | `--fix` இற்கு நம்பகத்தன்மை வரம்பு. இயல்புநிலை `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | இல்லை | யந்திர மொழிபெயர்ப்பு அறிவிப்புகளை சேர்க்க அல்லது கைவிட. CLI இல் இயல்பாக சேர்க்கப்பட்டுள்ளது. |
| `-f`, `--fast` | இல்லை | பழமடைந்த வேகமான பட முறை. |
| `-y`, `--yes` | இல்லை | தானாக கேள்விகளை ஒப்புக்கொள்ள, CI இல் பயன்படும். |
| `--repo-url` | இல்லை | README மொழி அட்டவணையில் sparse-checkout அறிவுரையில் பயன்படும் களஞ்சிய URL. |
| `--migrate-language-folders` | இல்லை | பழைய மாற்று பெயர் கோப்புறைகள் (`cn`, `tw` போன்றவை) ஐ canonical BCP 47 கோப்புறைகளாக பெயரிடு. |
| `--dry-run` | இல்லை | மொழி அடைவு மாற்றம் மற்றும் மொழிபெயர்ப்பு மதிப்பீடுகளை கோப்புகள் எழுதாமலேயே முன்னோட்டம் காண. |

If no type flag is provided, `translate` processes Markdown, notebooks, and images. Image translation requires Azure AI Vision configuration.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "சோதனை நிலை"
    `evaluate` சோதனை நிலை ஆகும். இது விதிமுறை அடிப்படையிலான மற்றும் LLM அடிப்படையிலான தரச் சோதனைகளை பயன்படுத்தக்கூடும், மதிப்பீட்டு முடிவுகளை மொழிபெயர்ப்பு மेटாடேட்டாவில் எழுதுகிறது, மேலும் அதன் மதிப்பீட்டு மாதிரி மற்றும் மெட்டாடேட்டா நடத்தை மாறலாம்.

```bash
evaluate -l "ko"
```

### பொதுவான உதாரணங்கள்

கடுமையான குறைந்த நம்பகத்தன்மை எல்லையைப் பயன்படுத்தவும்:

```bash
evaluate -l "es" -c 0.8
```

விதி-அடிப்படையிலான சோதனைகளை மட்டும் இயக்கவும்:

```bash
evaluate -l "fr" -f
```

LLM-அடிப்படையிலான சோதனைகளை மட்டும் இயக்கவும்:

```bash
evaluate -l "ja" -D
```

### விருப்பங்கள்

| விருப்பம் | தேவையா | விளக்கம் |
| --- | --- | --- |
| `-l`, `--language-code` | ஆம் | மதிப்பீடு செய்ய ஒரு தனி மொழி குறியீடு. மாற்று குறியீடுகள் சீரமைக்கப்படுகின்றன. |
| `-r`, `--root-dir` | இல்லை | திட்ட முதன்மை அடைவு. இயல்புநிலை தற்போதைய அடைவு. |
| `-c`, `--min-confidence` | இல்லை | குறைந்த நம்பகத்தன்மையைக் கொண்ட மொழிபெயர்ப்புகளை பட்டியலிடும் போது பயன்படுத்தப்படும் எல்லை. இயல்புநிலை `0.7`. |
| `-d`, `--debug` | இல்லை | டீபக் பதிவை இயக்கு. |
| `-s`, `--save-logs` | இல்லை | DEBUG நிலை பதிவுகளை `<root-dir>/logs/` கீழாக சேமிக்கவும். |
| `-f`, `--fast` | இல்லை | விதி-அடிப்படை மதிப்பீடு மட்டுமே. |
| `-D`, `--deep` | இல்லை | LLM-அடிப்படை மதிப்பீடு மட்டும். |

இயல்பாக, `evaluate` விதி-அடிப்படையிலும் LLM-அடிப்படையிலும் இரண்டையும் பயன்படுத்துகிறது. முடிவுகள் மொழிபெயர்ப்பு மेटாடேட்டாவில் எழுதி, கான்சோலில் சுருக்கமாக காட்டப்படும்.

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "பீட்டா"
    `co-op-review` ஒரு பீட்டா தீர்மானமான மதிப்பாய்வு கட்டளையாகும். இது மாடல் வழங்குநர்களை அழைக்காது அல்லது கோப்புகளை எழுதாது, ஆனால் அதன் சோதனைகள் மற்றும் பிரச்சினை வெளியீட்டு திட்டம் மாறக்கூடும்.

```bash
co-op-review -l "ko"
```

### பொதுவான உதாரணங்கள்

தற்போதய அடைவிலிருந்து கொரிய மற்றும் ஜப்பானிய மொழிபெயர்ப்புகளை மதிப்பாய்வு செய்ய:

```bash
co-op-review -l "ko ja"
```

குறிப்பிட்ட திட்ட ரூட் மதிப்பாய்வு செய்ய:

```bash
co-op-review -l "fr" -r ./my-course
```

ஒரு அடிப்படை குறிக்கோளுடன் மாறிய மூல கோப்புகளை மட்டும் மதிப்பாய்வு செய்ய:

```bash
co-op-review -l "ko" --changed-from origin/main
```

CI சுருக்கங்களுக்கு GitHub-ஸ்வாதீனமான Markdown வெளியீட்டை அச்சிடுங்கள்:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### விருப்பங்கள்

| விருப்பம் | தேவையா | விளக்கம் |
| --- | --- | --- |
| `-l`, `--language-code` | இல்லை | மதிப்பாய்வு செய்ய மொழி குறியீடு. பலமுறை வழங்கலாம் அல்லது இடைவெளியால் பிரிக்கப்பட்ட மதிப்பாக கொடுக்கலாம். இயல்பாக கண்டுபிடிக்கப்பட்ட அனைத்து மொழிபெயர்ப்புகளுக்கும். |
| `-r`, `--root-dir` | இல்லை | திட்ட முதன்மை அடைவு. இயல்புநிலை தற்போதைய அடைவு. |
| `--changed-from` | இல்லை | மதிப்பாய்வை மாற்றப்பட்ட மூல கோப்புகளுக்கு மட்டுப்படுத்த பயன்படுத்தப்படும் Git ref. |
| `--format` | இல்லை | வெளியீட்டு வடிவம்: `text` அல்லது `github`. இயல்புநிலை `text`. |

`co-op-review` தற்போது காணாமல் இருக்கும் மொழிபெயர்ப்புப் கோப்புகள், காணாமற் அல்லது பழுதடைந்த மொழிபெயர்ப்பு மेटாடேட்டா, Markdown frontmatter மற்றும் code fence ஒருங்கிணைப்பு, தவறான மொழிபெயர்க்கப்பட்ட நோட்புக் JSON, மற்றும் உள்ளூர் Markdown அல்லது பட இணைப்பு இலக்குகள் காணாமல் இருப்பதைச் சரிபார்க்கிறது. இணைப்புகள் காணாமல் இருப்பது இயல்பில் எச்சரிக்கை; கட்டமைப்பு மற்றும் புதுமை பிரச்சினைகள் கட்டளையை தோற்கடிக்க செய்கின்றன.

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [MCP சர்வர்](mcp.md) guide for client configuration, tools, resources, and safety notes.

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

Reprocess translated Markdown files and update notebook links so they point to translated notebooks when available.

```bash
migrate-links -l "ko ja"
```

### பொதுவான உதாரணங்கள்

இணைப்பு புதுப்பிப்புகளின் முன்னோட்டம்:

```bash
migrate-links -l "ko" --dry-run
```

உறுதிப்படுத்தலின்றி ஆதரிக்கப்படுகின்ற அனைத்து மொழிகளையும் செயலாக்கு:

```bash
migrate-links -l "all" -y
```

மொழிபெயர்க்கப்பட்ட நோட்புக் கிடைத்தால் மட்டுமே இணைப்புகளை புதுப்பிக்க:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### விருப்பங்கள்

| விருப்பம் | தேவையா | விளக்கம் |
| --- | --- | --- |
| `-l`, `--language-codes` | ஆம் | இடைவெளி பிரிக்கப்பட்ட மொழி குறியீடுகள், அல்லது `"all"`. |
| `-r`, `--root-dir` | இல்லை | திட்ட முதன்மை அடைவு. இயல்புநிலை தற்போதைய அடைவு. |
| `--image-dir` | இல்லை | மூலத்தை சார்ந்த மொழிபெயர்க்கப்பட்ட படம் அடைவு. இயல்புநிலை `translated_images`. |
| `--dry-run` | இல்லை | மேம்படுத்தல்களை எழுதாமல் எந்த கோப்புகள் மாறுமோ அவைகளை காட்டும். |
| `--fallback-to-original`, `--no-fallback-to-original` | இல்லை | மொழிபெயர்க்கப்பட்ட நோட்புக் கிடையாமல் இருப்பின் மூல நோட்புக் இணைப்புகளைப் பயன்படுத்தவும். இயல்பாக இயலுமைப்படுத்தப்பட்டுள்ளது. |
| `-d`, `--debug` | இல்லை | டீபக் பதிவை இயக்கு. |
| `-s`, `--save-logs` | இல்லை | DEBUG நிலை பதிவுகளை `<root-dir>/logs/` கீழாக சேமிக்கவும். |
| `-y`, `--yes` | இல்லை | அனைத்து மொழிகளையும் செயலாக்கும்போது தானாக ஒப்புதல். |

## சூழ்நிலை

அனைத்து கட்டளைகளுக்கும் ஒரு கட்டமைக்கப்பட்ட LLM வழங்குநர் தேவையாகும்:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# அல்லது OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

பட மொழிபெயர்ப்பு மேலாக Azure AI Vision ஐ தேவைப்படுத்துகிறது:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## வெளியீட்டு அமைப்பு

உரை மொழிபெயர்ப்புகள் கீழே எழுதப்படுகின்றன:

```text
translations/<language-code>/<original-path>
```

மொழிபெயர்க்கப்பட்ட பட வெளியீடு கீழே எழுதப்படுகிறது:

```text
translated_images/<language-code>/<original-path>
```

உதாரணமாக, `README.md` மற்றும் `docs/setup.md` ஐ கொரிய மொழிக்கு மொழிமாற்றம் செய்தால் உருவாகும்:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## நகலெடு-ஒட்ட CLI உதாரணங்கள்

Markdown ஐ மூன்று மொழிகளுக்கு மொழிபெயர்க்க:

```bash
translate -l "ko ja fr" -md
```

நோட்புக் கோப்புகளை மட்டுமே மொழிபெயர்க்க:

```bash
translate -l "zh-CN" -nb
```

படங்களை மட்டுமே மொழிபெயர்க்க:

```bash
translate -l "pt-BR" -img
```

கோப்புகளை எழுதாமல் Markdown மொழிபெயர்ப்பை முன்னோட்டமாக பார்க்க:

```bash
translate -l "de es" -md --dry-run
```

குறைந்த நம்பகத்தன்மையுள்ள Markdown மொழிபெயர்ப்புகளை சரிசெய்:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

CI-க்கு உகந்த Markdown மொழிபெயர்ப்பை இயக்க:

```bash
translate -l "ko ja" -md -y -s
```

மொழிபெயர்க்கப்பட்ட வெளியீட்டை மதிப்பாய்வு செய்ய:

```bash
co-op-review -l "ko ja"
```

இணைப்பு இடமாற்றத்தை முன்னோட்டம் காண:

```bash
migrate-links -l "ko" --dry-run
```