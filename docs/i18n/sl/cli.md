# CLI Referenca

Co-op Translator namesti te vstopne točke ukazne vrstice:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Ukazi `translate`, `evaluate`, `migrate-links` in `co-op-review` se pošiljajo skozi `co_op_translator.__main__`, ki izbere implementacijo ukaza glede na ime priklicanega skripta. MCP strežnik uporablja `co_op_translator.mcp.server` neposredno.

Če se odločate med CLI, Python API in MCP, začnite s [Izberite svoj delovni potek](workflows.md).

## Izhod konzole

Interaktivni terminali uporabljajo oblikovanje Rich za glavo ukaza, prikaz napredka in povzetke. CI in neinteraktivni izhod se samodejno vrneta na navadno besedilo.

Nastavite `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` za prisilni navadni izhod, ali `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` za prisilni Rich izhod. Nastavite `CO_OP_TRANSLATOR_NO_PROGRESS=1` za ohranjanje povzetkov ob zatiranju živih vrstic napredka.

Uporabite `translate --json-events progress.ndjson`, kadar drugo sistem potrebuje strojno berljiv napredek. CLI še vedno prikazuje izhod za ljudi, medtem ko datoteka NDJSON prejme verzionirane dogodke `co-op.translation.event.v1` z stabilnimi polji, kot so `type`, `stage_key`, `completed`, `total` in `current_path`.





## Prvi postopek uporabe CLI

Začnite tukaj, če uporabljate Co-op Translator iz terminala:

1. Konfigurirajte ponudnika LLM, kot je opisano v [Konfiguracija](configuration.md).
2. Izberite vrsto vsebine, ki jo želite prevesti.
3. Najprej zaženite osredotočen ukaz, na primer prevod samo Markdown datotek.
4. Pred večjimi spremembami repozitorija uporabite `--dry-run`.
5. Po prevajanju uporabite `co-op-review` za preverjanje strukture in ažurnosti.

| Cilj | Ukaz za začetek |
| --- | --- |
| Prevajanje Markdown dokumentov | `translate -l "ko" -md` |
| Prevajanje zvezkov | `translate -l "ko" -nb` |
| Prevajanje besedila na slikah | `translate -l "ko" -img` |
| Predogled dela brez zapisovanja datotek | `translate -l "ko" -md --dry-run` |
| Pregled obstoječih prevodov | `co-op-review -l "ko"` |
| Posodobitev povezav zvezkov in Markdowna | `migrate-links -l "ko" --dry-run` |
| Omogočanje orodij za MCP odjemalca | Namesto neposrednega zagona CLI ukazov konfigurirajte [MCP strežnik](mcp.md). |

## translate

Prevajajte Markdown datoteke, zvezke in besedilo na slikah v enega ali več ciljnih jezikov.

```bash
translate -l "ko ja fr"
```

### Pogosti primeri

Prevedi samo Markdown:

```bash
translate -l "de" -md
```

Prevedi samo zvezke:

```bash
translate -l "zh-CN" -nb
```

Prevedi Markdown in slike:

```bash
translate -l "pt-BR" -md -img
```

Posodobite obstoječe prevode z njihovim brisanjem in ponovnim ustvarjanjem:

```bash
translate -l "ko" -u
```

Zaženi brez interaktivnih pozivov:

```bash
translate -l "ko ja" -md -y
```

Shrani dnevnike:

```bash
translate -l "ko" -s
```

Zapiši strukturirane dogodke napredka:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Možnosti

| Možnost | Zahtevano | Opis |
| --- | --- | --- |
| `-l`, `--language-codes` | Da | Kode jezikov ločene s presledkom, na primer `"es fr de"`, ali `"all"`. |
| `-r`, `--root-dir` | Ne | Koren projekta. Privzeto trenutni imenik. |
| `-u`, `--update` | Ne | Izbriše obstoječe prevode za izbrane jezike in jih ponovno ustvari. |
| `-img`, `--images` | Ne | Prevedi samo slikovne datoteke. |
| `-md`, `--markdown` | Ne | Prevedi samo Markdown datoteke. |
| `-nb`, `--notebook` | Ne | Prevedi samo Jupyter zvezke. |
| `-d`, `--debug` | Ne | Omogoči debug beleženje v konzoli. |
| `-s`, `--save-logs` | Ne | Shrani dnevnik na ravni DEBUG v `<root-dir>/logs/`. |
| `--json-events` | Ne | Zapiše strojno berljive dogodke napredka prevajanja kot NDJSON. |
| `-x`, `--fix` | Ne | Ponovno prevede Markdown datoteke z nizko zanesljivostjo na podlagi prejšnjih rezultatov ocenjevanja. |
| `-c`, `--min-confidence` | Ne | Prag zanesljivosti za `--fix`. Privzeto `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Ne | Dodaj ali potlači izjavo o strojno prevedenem besedilu. Privzeto omogočeno v CLI. |
| `-f`, `--fast` | Ne | Zastareli hiter način za slike. |
| `-y`, `--yes` | Ne | Samodejno potrdi pozive, uporabno v CI. |
| `--repo-url` | Ne | URL repozitorija, uporabljen v tabeli jezikov README za nasvet sparse-checkout. |
| `--migrate-language-folders` | Ne | Preimenuje zastarele alias mape, kot sta `cn` ali `tw`, v kanonične BCP 47 mape. |
| `--dry-run` | Ne | Predogled migracije jezikovnih map in ocen prevajanja brez zapisovanja datotek. |

Če ni podan noben tip zastavice, `translate` obdela Markdown, zvezke in slike. Prevajanje slik zahteva konfiguracijo Azure AI Vision.

## evaluate

Ocenjevanje kakovosti prevedenega Markdowna za en jezik.

!!! warning "Eksperimentalno"
    `evaluate` je eksperimentalno. Lahko uporablja preverjanja kakovosti, ki temeljijo na pravilih in na LLM, zapisuje rezultate ocenjevanja v prevodne metapodatke in se lahko spremenita njegov model točkovanja in obnašanje metapodatkov.

```bash
evaluate -l "ko"
```

### Pogosti primeri

Uporabite strožji prag za nizko zaupanje:

```bash
evaluate -l "es" -c 0.8
```

Zaženi samo preverjanja, ki temeljijo na pravilih:

```bash
evaluate -l "fr" -f
```

Zaženi samo preverjanja, ki temeljijo na LLM:

```bash
evaluate -l "ja" -D
```

### Možnosti

| Možnost | Zahtevano | Opis |
| --- | --- | --- |
| `-l`, `--language-code` | Da | Ena koda jezika za ocenjevanje. Alias kode se normalizirajo. |
| `-r`, `--root-dir` | Ne | Koren projekta. Privzeto trenutni imenik. |
| `-c`, `--min-confidence` | Ne | Prag, uporabljen pri izpisu prevodov z nizko zanesljivostjo. Privzeto `0.7`. |
| `-d`, `--debug` | Ne | Omogoči debug beleženje. |
| `-s`, `--save-logs` | Ne | Shrani dnevnik na ravni DEBUG v `<root-dir>/logs/`. |
| `-f`, `--fast` | Ne | Samo ocenjevanje na osnovi pravil. |
| `-D`, `--deep` | Ne | Samo ocenjevanje na osnovi LLM. |

Privzeto `evaluate` uporablja tako ocenjevanje na osnovi pravil kot tudi na osnovi LLM. Rezultati se zapišejo v prevodne metapodatke in povzemejo v konzoli.

## co-op-review

Zaženite deterministične preglede vzdrževanja prevodov brez API poverilnic.

!!! note "Beta"
    `co-op-review` je beta determinističen ukaz za pregled. Ne kliče ponudnikov modelov niti ne zapisuje datotek, vendar se lahko spreminjajo njegovi preverjalni postopki in shema izhoda težav.

```bash
co-op-review -l "ko"
```

### Pogosti primeri

Preglejte korejske in japonske prevode iz trenutnega imenika:

```bash
co-op-review -l "ko ja"
```

Preglejte določen koren projekta:

```bash
co-op-review -l "fr" -r ./my-course
```

Preglejte le README po prevodu, izvedenem samo za README:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` zanemari druge dokumente in vgrajene README datoteke. Ne uspe, če manjka korenski `README.md`. V kombinaciji z `--changed-from` pregleda README le, ko se ta izvorna datoteka spremeni. Prevod le README pusti izvorni README nespremenjen, vključno z morebitnimi oznakami deljenih odsekov.




Preglejte samo izvorne datoteke, ki so se spremenile glede na osnovno referenco:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Izpiše Markdown v GitHub obliki za povzetke CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Možnosti

| Možnost | Zahtevano | Opis |
| --- | --- | --- |
| `-l`, `--language-code` | Ne | Koda jezika za pregled. Lahko jo podate večkrat ali kot vrednost ločeno s presledki. Privzeto vsi najdeni prevodni jeziki. |
| `-r`, `--root-dir` | Ne | Koren projekta. Privzeto trenutni imenik. |
| `--changed-from` | Ne | Git referenca, uporabljena za omejitev pregleda na spremenjene izvorne datoteke. |
| `--readme-only` | Ne | Preglej samo prevod korenskega `README.md`. |
| `--format` | Ne | Format izhoda: `text` ali `github`. Privzeto `text`. |

`co-op-review` trenutno preverja manjkajoče prevedene datoteke, manjkajoče ali zastarele prevodne metapodatke, integriteto Markdown frontmatter in code fence-ov, neveljaven preveden JSON zvezka ter manjkajoče lokalne cilje povezav v Markdownu ali slikah. Manjkajoče povezave so privzeto opozorila; strukturne in ažurnostne težave povzročijo, da ukaz ne uspe.

## co-op-translator-mcp

Zaženite MCP strežnik Co-op Translator za agente, urednike in odjemalce združljive z MCP.

```bash
co-op-translator-mcp
```

Privzeti transport je `stdio`. Oglejte si vodnik [MCP strežnik](mcp.md) za konfiguracijo odjemalca, orodja, vire in varnostne opombe.

### Možnosti

| Možnost | Zahtevano | Opis |
| --- | --- | --- |
| `--transport` | Ne | MCP transport: `stdio`, `streamable-http`, ali `sse`. Privzeto `stdio`. |

## migrate-links

Ponovno obdela prevedene Markdown datoteke in posodobi povezave zvezkov, tako da kažejo na prevedene zvezke, kadar so na voljo.

```bash
migrate-links -l "ko ja"
```

### Pogosti primeri

Predogled posodobitev povezav:

```bash
migrate-links -l "ko" --dry-run
```

Obdelajte vse podprte jezike brez potrditve:

```bash
migrate-links -l "all" -y
```

Prepiši povezave le, ko prevodi zvezkov obstajajo:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Možnosti

| Možnost | Zahtevano | Opis |
| --- | --- | --- |
| `-l`, `--language-codes` | Da | Kode jezikov ločene s presledkom, ali `"all"`. |
| `-r`, `--root-dir` | Ne | Koren projekta. Privzeto trenutni imenik. |
| `--image-dir` | Ne | Mapo prevedenih slik relativno na koren. Privzeto `translated_images`. |
| `--dry-run` | Ne | Pokaže datoteke, ki bi se spremenile, brez zapisa posodobitev. |
| `--fallback-to-original`, `--no-fallback-to-original` | Ne | Uporabi izvirne povezave do zvezkov, ko prevodi manjkajo. Privzeto omogočeno. |
| `-d`, `--debug` | Ne | Omogoči debug beleženje. |
| `-s`, `--save-logs` | Ne | Shrani dnevnik na ravni DEBUG v `<root-dir>/logs/`. |
| `-y`, `--yes` | Ne | Samodejno potrdi pozive pri obdelavi vseh jezikov. |

## Okolje

Ko ukaz zahteva poverilnice ponudnika, konfigurirajte enega od teh kompletov ponudnikov. `translate --dry-run` in `co-op-review` ne zahtevata poverilnic ponudnikov:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Ali OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Ali Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Za prevajanje slik je dodatno potrebna Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Razpored izhoda

Besedilni prevodi se zapišejo pod:

```text
translations/<language-code>/<original-path>
```

Izhod prevedenih slik se zapiše pod:

```text
translated_images/<language-code>/<original-path>
```

Na primer, prevajanje `README.md` in `docs/setup.md` v korejščino ustvari:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Primeri CLI za kopiranje in lepljenje

Prevedi Markdown v tri jezike:

```bash
translate -l "ko ja fr" -md
```

Prevedi samo zvezke:

```bash
translate -l "zh-CN" -nb
```

Prevedi samo slike:

```bash
translate -l "pt-BR" -img
```

Predogled prevoda Markdown brez zapisovanja datotek:

```bash
translate -l "de es" -md --dry-run
```

Popravi prevode Markdown z nizko zanesljivostjo:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Zaženi CI-prijazen prevod Markdowna:

```bash
translate -l "ko ja" -md -y -s
```

Preglej prevedeni izhod:

```bash
co-op-review -l "ko ja"
```

Predogled migracije povezav:

```bash
migrate-links -l "ko" --dry-run
```