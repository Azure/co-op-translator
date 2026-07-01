# Referenca CLI

Co-op Translator namesti naslednje vstopne točke ukazne vrstice:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Ukazi `translate`, `evaluate`, `migrate-links` in `co-op-review` se pošiljajo prek `co_op_translator.__main__`, ki izbere implementacijo ukaza glede na ime poklicanega skripta. MCP strežnik uporablja `co_op_translator.mcp.server` neposredno.

Če se odločate med CLI, Python API in MCP, začnite z [Izberite svoj potek dela](workflows.md).

## Postopek pri prvi uporabi CLI

Začnite tukaj, če uporabljate Co-op Translator iz terminala:

1. Konfigurirajte ponudnika LLM, kot je opisano v [Configuration](configuration.md).
2. Izberite vrsto vsebine, ki jo želite prevesti.
3. Najprej zaženite osredotočen ukaz, na primer prevod samo Markdowna.
4. Pred večjimi spremembami v repozitoriju uporabite `--dry-run`.
5. Po prevajanju uporabite `co-op-review` za preverjanje strukture in ažurnosti.

| Cilj | Ukaz za začetek |
| --- | --- |
| Prevedi Markdown dokumente | `translate -l "ko" -md` |
| Prevedi zvezke | `translate -l "ko" -nb` |
| Prevedi besedilo na slikah | `translate -l "ko" -img` |
| Predogled dela brez zapisovanja datotek | `translate -l "ko" -md --dry-run` |
| Preglej obstoječe prevode | `co-op-review -l "ko"` |
| Posodobi povezave v zvezkih in Markdownu | `migrate-links -l "ko" --dry-run` |
| Omogoči orodja MCP odjemalcu | Konfigurirajte [MCP strežnik](mcp.md) namesto neposrednega zagona CLI ukazov. |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

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

Posodobi obstoječe prevode z izbrisom in ponovnim ustvarjanjem:

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

### Možnosti

| Možnost | Obvezno | Opis |
| --- | --- | --- |
| `-l`, `--language-codes` | Da | Jezikovne kode, ločene s presledki, na primer `"es fr de"`, ali `"all"`. |
| `-r`, `--root-dir` | Ne | Koren projekta. Privzeto trenutni imenik. |
| `-u`, `--update` | Ne | Izbriše obstoječe prevode za izbrane jezike in jih ponovno ustvari. |
| `-img`, `--images` | Ne | Prevede samo datoteke s slikami. |
| `-md`, `--markdown` | Ne | Prevede samo Markdown datoteke. |
| `-nb`, `--notebook` | Ne | Prevede samo Jupyter notebook datoteke. |
| `-d`, `--debug` | Ne | Omogoči debug beleženje v konzoli. |
| `-s`, `--save-logs` | Ne | Shrani dnevnike na ravni DEBUG v `<root-dir>/logs/`. |
| `-x`, `--fix` | Ne | Ponovno prevede Markdown datoteke z nizko zanesljivostjo na podlagi prejšnjih rezultatov ocenjevanja. |
| `-c`, `--min-confidence` | Ne | Prag zanesljivosti za `--fix`. Privzeto `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Ne | Dodaj ali onemogoči izjavo o strojnih prevodih. Privzeto omogočeno v CLI. |
| `-f`, `--fast` | Ne | Zastarel hiter način za slike. |
| `-y`, `--yes` | Ne | Samodejno potrdi pozive, uporabno v CI. |
| `--repo-url` | Ne | URL repozitorija, uporabljen v nasvetu za sparse-checkout v tabeli jezikov v README. |
| `--migrate-language-folders` | Ne | Preimenuje zastarele alias mape, kot so `cn` ali `tw`, v kanonične mape BCP 47. |
| `--dry-run` | Ne | Predogled migracije map jezikov in ocen prevajanja brez pisanja datotek. |

Če ni naveden noben tip zastavice, `translate` obdela Markdown, zvezke in slike. Prevod slik zahteva konfiguracijo Azure AI Vision.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "Eksperimentalno"
    `evaluate` je eksperimentalna. Lahko uporablja preverjanja kakovosti na osnovi pravil in na osnovi LLM, zapisuje rezultate ocenjevanja v prevodne metapodatke, in njen model ocenjevanja ter obnašanje metapodatkov se lahko spremenita.

```bash
evaluate -l "ko"
```

### Pogosti primeri

Uporabite strožji prag nizke zanesljivosti:

```bash
evaluate -l "es" -c 0.8
```

Zaženite samo preverjanja na osnovi pravil:

```bash
evaluate -l "fr" -f
```

Zaženite samo preverjanja na osnovi LLM:

```bash
evaluate -l "ja" -D
```

### Možnosti

| Možnost | Obvezno | Opis |
| --- | --- | --- |
| `-l`, `--language-code` | Da | Ena jezikovna koda za ocenjevanje. Alias kode se normalizirajo. |
| `-r`, `--root-dir` | Ne | Koren projekta. Privzeto trenutni imenik. |
| `-c`, `--min-confidence` | Ne | Prag, uporabljen pri navajanju prevodov z nizko zanesljivostjo. Privzeto `0.7`. |
| `-d`, `--debug` | Ne | Omogoči debug beleženje. |
| `-s`, `--save-logs` | Ne | Shrani dnevnike na ravni DEBUG v `<root-dir>/logs/`. |
| `-f`, `--fast` | Ne | Samo ocenjevanje na osnovi pravil. |
| `-D`, `--deep` | Ne | Samo ocenjevanje na osnovi LLM. |

Privzeto `evaluate` uporablja tako preverjanja na osnovi pravil kot na osnovi LLM. Rezultati se zapišejo v prevodne metapodatke in so povzeti v konzoli.

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "Beta"
    `co-op-review` je beta determinističen ukaz za pregled. Ne kliče ponudnikov modelov niti ne zapisuje datotek, vendar se lahko njegovi preverjalni postopki in shema izhoda zadev spremenijo.

```bash
co-op-review -l "ko"
```

### Pogosti primeri

Preglej korejske in japonske prevode iz trenutnega imenika:

```bash
co-op-review -l "ko ja"
```

Preglej določen koren projekta:

```bash
co-op-review -l "fr" -r ./my-course
```

Preglej samo izvorne datoteke, spremenjene glede na osnovni ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Natisni izhod v formatu GitHub-ovega Markdown za povzetke v CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Možnosti

| Možnost | Obvezno | Opis |
| --- | --- | --- |
| `-l`, `--language-code` | Ne | Jezikovna koda za pregled. Lahko se poda večkrat ali kot vrednost, ločena s presledkom. Privzeto vsi odkrijeni prevodni jeziki. |
| `-r`, `--root-dir` | Ne | Koren projekta. Privzeto trenutni imenik. |
| `--changed-from` | Ne | Git ref, uporabljen za omejitev pregleda na spremenjene izvorne datoteke. |
| `--format` | Ne | Izhodni format: `text` ali `github`. Privzeto `text`. |

`co-op-review` trenutno preverja manjkajoče prevedene datoteke, manjkajoče ali zastarele prevodne metapodatke, integriteto Markdown frontmatter in ograj kode, nepravilno preveden JSON zvezkov in manjkajoče lokalne cilje povezav v Markdownu ali slikah. Manjkajoče povezave so privzeto opozorila; strukturalne in problematične zastarelosti povzročijo neuspeh ukaza.

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

Privzeti transport je `stdio`. Oglejte si vodnik [MCP strežnik](mcp.md) za konfiguracijo odjemalcev, orodij, virov in varnostne opombe.

### Možnosti

| Možnost | Obvezno | Opis |
| --- | --- | --- |
| `--transport` | Ne | MCP transport: `stdio`, `streamable-http`, ali `sse`. Privzeto `stdio`. |

## migrate-links

Ponovno obdela prevedene Markdown datoteke in posodobi povezave v zvezkih, tako da kažejo na prevedene zvezke, kadar so na voljo.

```bash
migrate-links -l "ko ja"
```

### Pogosti primeri

Predogled posodobitev povezav:

```bash
migrate-links -l "ko" --dry-run
```

Obdelaj vse podprte jezike brez potrditve:

```bash
migrate-links -l "all" -y
```

Prepiši povezave le, ko prevedeni zvezki obstajajo:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Možnosti

| Možnost | Obvezno | Opis |
| --- | --- | --- |
| `-l`, `--language-codes` | Da | Jezikovne kode, ločene s presledki, ali `"all"`. |
| `-r`, `--root-dir` | Ne | Koren projekta. Privzeto trenutni imenik. |
| `--image-dir` | Ne | Mapa prevedenih slik glede na koren. Privzeto `translated_images`. |
| `--dry-run` | Ne | Prikaži datoteke, ki bi se spremenile, brez zapisovanja posodobitev. |
| `--fallback-to-original`, `--no-fallback-to-original` | Ne | Uporabi izvirne povezave na zvezke, ko prevedeni zvezki manjkajo. Privzeto omogočeno. |
| `-d`, `--debug` | Ne | Omogoči debug beleženje. |
| `-s`, `--save-logs` | Ne | Shrani dnevnike na ravni DEBUG v `<root-dir>/logs/`. |
| `-y`, `--yes` | Ne | Samodejno potrdi pozive pri obdelavi vseh jezikov. |

## Okolje

Vsi ukazi zahtevajo en konfiguriran ponudnik LLM:

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
```

Prevod slik dodatno zahteva Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Struktura izhoda

Besedilni prevodi se zapišejo v:

```text
translations/<language-code>/<original-path>
```

Prevedena slikovna izhodna vsebina se zapiše v:

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

Predogled prevoda Markdown brez pisanja datotek:

```bash
translate -l "de es" -md --dry-run
```

Popravi prevode Markdown z nizko zanesljivostjo:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Zaženi CI-prijazen prevod Markdown:

```bash
translate -l "ko ja" -md -y -s
```

Preglej prevedeno vsebino:

```bash
co-op-review -l "ko ja"
```

Predogled migracije povezav:

```bash
migrate-links -l "ko" --dry-run
```