# CLI Referenca

Co-op Translator instalira ove naredbene točke naredbenog retka:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Naredbe `translate`, `evaluate`, `migrate-links` i `co-op-review` prosljeđuju se preko `co_op_translator.__main__`, koji odabire implementaciju naredbe na temelju naziva pozvanog skripta. MCP poslužitelj koristi `co_op_translator.mcp.server` izravno.

Ako odlučujete između CLI-ja, Python API-ja i MCP-a, započnite s [Choose Your Workflow](workflows.md).

## Početni CLI tijek rada

Započnite ovdje ako koristite Co-op Translator iz terminala:

1. Konfigurirajte pružatelja LLM-a kao što je opisano u [Configuration](configuration.md).
2. Odaberite vrstu sadržaja koji želite prevesti.
3. Prvo pokrenite fokusiranu naredbu, kao primjerice prijevod samo Markdown-a.
4. Prije velikih promjena u repozitoriju koristite `--dry-run`.
5. Nakon prijevoda upotrijebite `co-op-review` za provjeru strukture i ažurnosti.

| Cilj | Naredba za početak |
| --- | --- |
| Prevesti Markdown dokumente | `translate -l "ko" -md` |
| Prevesti bilježnice | `translate -l "ko" -nb` |
| Prevesti tekst na slikama | `translate -l "ko" -img` |
| Pregled radova bez pisanja datoteka | `translate -l "ko" -md --dry-run` |
| Pregledati postojeće prijevode | `co-op-review -l "ko"` |
| Ažurirati veze u bilježnicama i Markdownu | `migrate-links -l "ko" --dry-run` |
| Izložiti alate MCP klijentu | Konfigurirajte [MCP Server](mcp.md) umjesto izravnog pokretanja CLI naredbi. |

## translate

Prevedite Markdown datoteke, bilježnice i tekst na slikama na jedan ili više ciljanih jezika.

```bash
translate -l "ko ja fr"
```

### Uobičajeni primjeri

Prevedite samo Markdown:

```bash
translate -l "de" -md
```

Prevedite samo bilježnice:

```bash
translate -l "zh-CN" -nb
```

Prevedite Markdown i slike:

```bash
translate -l "pt-BR" -md -img
```

Ažurirajte postojeće prijevode brišući i ponovo ih stvarajući:

```bash
translate -l "ko" -u
```

Pokrenite bez interaktivnih upita:

```bash
translate -l "ko ja" -md -y
```

Spremite zapisnike:

```bash
translate -l "ko" -s
```

### Opcije

| Opcija | Obavezno | Opis |
| --- | --- | --- |
| `-l`, `--language-codes` | Da | Jezici odvojeni razmacima, npr. `"es fr de"`, ili `"all"`. |
| `-r`, `--root-dir` | Ne | Korijen projekta. Zadano je trenutačni direktorij. |
| `-u`, `--update` | Ne | Izbriši postojeće prijevode za odabrane jezike i ponovno ih stvori. |
| `-img`, `--images` | Ne | Prevedi samo slikovne datoteke. |
| `-md`, `--markdown` | Ne | Prevedi samo Markdown datoteke. |
| `-nb`, `--notebook` | Ne | Prevedi samo Jupyter bilježnice. |
| `-d`, `--debug` | Ne | Omogući debug zapisivanje u konzoli. |
| `-s`, `--save-logs` | Ne | Spremi DEBUG-nivo zapisnika ispod `<root-dir>/logs/`. |
| `-x`, `--fix` | Ne | Ponovno prevedi Markdown datoteke niskog povjerenja na temelju prethodnih rezultata evaluacije. |
| `-c`, `--min-confidence` | Ne | Prag povjerenja za `--fix`. Zadano je `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Ne | Dodaj ili suzbij izjavu o strojnom prijevodu. Prema zadanim postavkama omogućeno u CLI-ju. |
| `-f`, `--fast` | Ne | Zastarjeli brzi način za slike. |
| `-y`, `--yes` | Ne | Automatski potvrdi upite, korisno u CI. |
| `--repo-url` | Ne | URL repozitorija koji se koristi u README tablici jezika za sparse-checkout savjet. |
| `--migrate-language-folders` | Ne | Preimenuj naslijeđene alias mape, poput `cn` ili `tw`, u kanonske BCP 47 mape. |
| `--dry-run` | Ne | Pregled migracije mapa jezika i procjena prijevoda bez pisanja datoteka. |

Ako nije naveden nijedan tip zastavice, `translate` obrađuje Markdown, bilježnice i slike. Za prijevod slika potrebna je konfiguracija Azure AI Vision.

## evaluate

Evaluirajte kvalitetu prevedenog Markdown-a za jedan jezik.

!!! warning "Experimental"
    `evaluate` je eksperimentalan. Može koristiti provjere kvalitete temeljene na pravilima i na LLM-u, zapisuje rezultate evaluacije u metapodatke prijevoda, i njegov model bodovanja i ponašanje metapodataka mogu se promijeniti.

```bash
evaluate -l "ko"
```

### Uobičajeni primjeri

Koristite stroži prag za nisko povjerenje:

```bash
evaluate -l "es" -c 0.8
```

Pokrenite samo provjere temeljene na pravilima:

```bash
evaluate -l "fr" -f
```

Pokrenite samo provjere temeljene na LLM-u:

```bash
evaluate -l "ja" -D
```

### Opcije

| Opcija | Obavezno | Opis |
| --- | --- | --- |
| `-l`, `--language-code` | Da | Jedan jezični kod za evaluaciju. Alias kodovi se normaliziraju. |
| `-r`, `--root-dir` | Ne | Korijen projekta. Zadano je trenutačni direktorij. |
| `-c`, `--min-confidence` | Ne | Prag koji se koristi pri nabrajaju prijevoda niskog povjerenja. Zadano `0.7`. |
| `-d`, `--debug` | Ne | Omogući debug zapisivanje. |
| `-s`, `--save-logs` | Ne | Spremi DEBUG-nivo zapisnika ispod `<root-dir>/logs/`. |
| `-f`, `--fast` | Ne | Samo evaluacija temeljena na pravilima. |
| `-D`, `--deep` | Ne | Samo evaluacija temeljena na LLM-u. |

Prema zadanim postavkama, `evaluate` koristi i evaluaciju temeljenu na pravilima i na LLM-u. Rezultati se zapisuju u metapodatke prijevoda i sažimaju u konzoli.

## co-op-review

Pokrenite determinističke provjere održavanja prijevoda bez API vjerodajnica.

!!! note "Beta"
    `co-op-review` je beta deterministička naredba za pregled. Ne poziva pružatelje modela niti ne zapisuje datoteke, ali njegove provjere i shema izlaza problema mogu se mijenjati.

```bash
co-op-review -l "ko"
```

### Uobičajeni primjeri

Pregledajte korejske i japanske prijevode iz trenutnog direktorija:

```bash
co-op-review -l "ko ja"
```

Pregledajte određeni korijen projekta:

```bash
co-op-review -l "fr" -r ./my-course
```

Pregledajte samo izvorne datoteke promijenjene u odnosu na osnovni ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Ispišite GitHub-flavored Markdown izlaz za sažetke u CI-u:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Opcije

| Opcija | Obavezno | Opis |
| --- | --- | --- |
| `-l`, `--language-code` | Ne | Jezični kod za pregled. Može se proslijediti više puta ili kao vrijednost odvojenih razmacima. Zadano je za sve otkrivene jezike prijevoda. |
| `-r`, `--root-dir` | Ne | Korijen projekta. Zadano je trenutačni direktorij. |
| `--changed-from` | Ne | Git ref koji se koristi za ograničavanje pregleda na promijenjene izvorne datoteke. |
| `--format` | Ne | Izlazni format: `text` ili `github`. Zadano `text`. |

`co-op-review` trenutačno provjerava nedostajuće prevedene datoteke, nedostajuće ili zastarjele metapodatke prijevoda, integritet Markdown frontmatter-a i ograda koda, neispravan JSON prevedenih bilježnica i nedostajuće lokalne Markdown ili slikovne ciljeve veza. Nedostajuće veze su upozorenja prema zadanim postavkama; problemi strukture i svježine uzrokuju neuspjeh naredbe.

## co-op-translator-mcp

Pokrenite Co-op Translator MCP poslužitelj za agente, urednike i MCP-kompatibilne klijente.

```bash
co-op-translator-mcp
```

Zadani transport je `stdio`. Pogledajte vodič [MCP Server](mcp.md) za konfiguraciju klijenta, alate, resurse i sigurnosne napomene.

### Opcije

| Opcija | Obavezno | Opis |
| --- | --- | --- |
| `--transport` | Ne | MCP transport: `stdio`, `streamable-http`, ili `sse`. Zadano `stdio`. |

## migrate-links

Ponovno obradite prevedene Markdown datoteke i ažurirajte veze u bilježnicama tako da upućuju na prevedene bilježnice kada su dostupne.

```bash
migrate-links -l "ko ja"
```

### Uobičajeni primjeri

Pregled ažuriranja veza:

```bash
migrate-links -l "ko" --dry-run
```

Obradite sve podržane jezike bez potvrde:

```bash
migrate-links -l "all" -y
```

Prepišite veze samo kada postoje prevedene bilježnice:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Opcije

| Opcija | Obavezno | Opis |
| --- | --- | --- |
| `-l`, `--language-codes` | Da | Jezici odvojeni razmacima, ili `"all"`. |
| `-r`, `--root-dir` | Ne | Korijen projekta. Zadano je trenutačni direktorij. |
| `--image-dir` | Ne | Direktorij prevedenih slika relativno prema korijenu. Zadano `translated_images`. |
| `--dry-run` | Ne | Prikaži datoteke koje bi se promijenile bez zapisivanja ažuriranja. |
| `--fallback-to-original`, `--no-fallback-to-original` | Ne | Koristi originalne veze na bilježnice kada prevedene bilježnice nedostaju. Prema zadanim postavkama omogućeno. |
| `-d`, `--debug` | Ne | Omogući debug zapisivanje. |
| `-s`, `--save-logs` | Ne | Spremi DEBUG-nivo zapisnika ispod `<root-dir>/logs/`. |
| `-y`, `--yes` | Ne | Automatski potvrdi upite pri obradi svih jezika. |

## Okoliš

Sve naredbe zahtijevaju jednog konfiguriranog pružatelja LLM-a:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Ili OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Prijevod slika dodatno zahtijeva Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Izgled izlaza

Tekstualni prijevodi zapisuju se pod:

```text
translations/<language-code>/<original-path>
```

Izlaz prevedenih slika zapisuje se pod:

```text
translated_images/<language-code>/<original-path>
```

Na primjer, prevođenje `README.md` i `docs/setup.md` na korejski proizvodi:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Primjeri za copy-paste CLI

Prevedi Markdown na tri jezika:

```bash
translate -l "ko ja fr" -md
```

Prevedi samo bilježnice:

```bash
translate -l "zh-CN" -nb
```

Prevedi samo slike:

```bash
translate -l "pt-BR" -img
```

Pregled prijevoda Markdown-a bez pisanja datoteka:

```bash
translate -l "de es" -md --dry-run
```

Popravi prijevode Markdown-a s niskim povjerenjem:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Pokreni CI-prijateljski prijevod Markdown-a:

```bash
translate -l "ko ja" -md -y -s
```

Pregled prevedenog izlaza:

```bash
co-op-review -l "ko ja"
```

Pregled migracije veza:

```bash
migrate-links -l "ko" --dry-run
```