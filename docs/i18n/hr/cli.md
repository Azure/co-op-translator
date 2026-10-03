# CLI referenca

Co-op Translator instalira ove ulazne točke naredbenog retka:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Naredbe `translate`, `evaluate`, `migrate-links` i `co-op-review` pozivaju se putem `co_op_translator.__main__`, koji odabire implementaciju naredbe na temelju imena pokrenutog skripta. MCP poslužitelj izravno koristi `co_op_translator.mcp.server`.

Ako odlučujete između CLI-ja, Python API-ja i MCP-a, započnite s [Odaberite svoj radni tok](workflows.md).

## Konzolni izlaz

Interaktivni terminali koriste Rich oblikovanje za zaglavlje naredbe, napredak i sažetke. CI i nein­teraktivni izlaz automatski prelaze na običan tekst.

Postavite `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` da prisilite običan izlaz, ili `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` da prisilite Rich izlaz. Postavite `CO_OP_TRANSLATOR_NO_PROGRESS=1` da zadržite sažetke uz onemogućene prikaze napretka uživo.

Koristite `translate --json-events progress.ndjson` kada drugi sustav treba
strojno čitljiv napredak. CLI nastavlja prikazivati izlaz namijenjen ljudima, dok
NDJSON datoteka prima verzionirane `co-op.translation.event.v1` događaje s
stabilnim poljima poput `type`, `stage_key`, `completed`, `total`, i
`current_path`.

## Početni tijek rada CLI-ja

Započnite ovdje ako koristite Co-op Translator iz terminala:

1. Konfigurirajte pružatelja LLM-a kako je opisano u [Konfiguracija](configuration.md).
2. Odaberite vrstu sadržaja koju želite prevesti.
3. Najprije pokrenite fokusiranu naredbu, na primjer prijevod samo Markdown datoteka.
4. Upotrijebite `--dry-run` prije velikih promjena u repozitoriju.
5. Nakon prijevoda upotrijebite `co-op-review` za provjeru strukture i svježine.

| Cilj | Naredba za početak |
| --- | --- |
| Prevedi Markdown dokumente | `translate -l "ko" -md` |
| Prevedi bilježnice | `translate -l "ko" -nb` |
| Prevedi tekst na slikama | `translate -l "ko" -img` |
| Pregledajte rad bez zapisivanja datoteka | `translate -l "ko" -md --dry-run` |
| Pregledajte postojeće prijevode | `co-op-review -l "ko"` |
| Ažurirajte poveznice u bilježnicama i Markdownu | `migrate-links -l "ko" --dry-run` |
| Omogućite alate MCP klijentu | Umjesto izravnog pokretanja CLI naredbi konfigurirajte [MCP poslužitelj](mcp.md). |

## translate

Prevodi Markdown datoteke, bilježnice i tekst na slikama na jedan ili više ciljanih jezika.

```bash
translate -l "ko ja fr"
```

### Uobičajeni primjeri

Prevedi samo Markdown:

```bash
translate -l "de" -md
```

Prevedi samo bilježnice:

```bash
translate -l "zh-CN" -nb
```

Prevedi Markdown i slike:

```bash
translate -l "pt-BR" -md -img
```

Ažuriraj postojeće prijevode brisanjem i ponovnim stvaranjem:

```bash
translate -l "ko" -u
```

Pokrenite bez interaktivnih upita:

```bash
translate -l "ko ja" -md -y
```

Spremi zapisnike:

```bash
translate -l "ko" -s
```

Zapišite strukturirane događaje napretka:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Opcije

| Opcija | Obavezno | Opis |
| --- | --- | --- |
| `-l`, `--language-codes` | Da | Kodovi jezika odvojeni razmacima, kao što su `"es fr de"`, ili `"all"`. |
| `-r`, `--root-dir` | Ne | Korijen projekta. Zadano je trenutni direktorij. |
| `-u`, `--update` | Ne | Izbrišite postojeće prijevode za odabrane jezike i ponovno ih stvorite. |
| `-img`, `--images` | Ne | Prevedi samo datoteke sa slikama. |
| `-md`, `--markdown` | Ne | Prevedi samo Markdown datoteke. |
| `-nb`, `--notebook` | Ne | Prevedi samo Jupyter notebook datoteke. |
| `-d`, `--debug` | Ne | Omogući zapisivanje za otklanjanje pogrešaka u konzoli. |
| `-s`, `--save-logs` | Ne | Spremi zapise razine DEBUG u `<root-dir>/logs/`. |
| `--json-events` | Ne | Zabilježi strojno čitljive događaje napretka prijevoda kao NDJSON. |
| `-x`, `--fix` | Ne | Ponovno prevedi Markdown datoteke s niskim povjerenjem na temelju prethodnih rezultata procjene. |
| `-c`, `--min-confidence` | Ne | Prag povjerenja za `--fix`. Zadano je `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Ne | Dodaj ili suzbije odricanja od odgovornosti za strojno prevođenje. Zadano je omogućeno u CLI-ju. |
| `-f`, `--fast` | Ne | Zastarjeli brzi način rada za slike. |
| `-y`, `--yes` | Ne | Automatski potvrdi upite, korisno u CI. |
| `--repo-url` | Ne | URL repozitorija koji se koristi u savjetu sparse-checkout u README tablici jezika. |
| `--migrate-language-folders` | Ne | Preimenuj naslijeđene alias mape, poput `cn` ili `tw`, u kanonske BCP 47 mape. |
| `--dry-run` | Ne | Pregled migracije mapa jezika i procjene prijevoda bez zapisivanja datoteka. |

Ako nije naveden nijedan tip zastavice, `translate` obrađuje Markdown, bilježnice i slike. Prevođenje slika zahtijeva konfiguraciju Azure AI Vision.

## evaluate

Ocijeni kvalitetu prevedenog Markdowna za jedan jezik.

!!! warning "Eksperimentalno"
    `evaluate` je eksperimentalna. Može koristiti provjere kvalitete temeljene na pravilima i LLM-u, zapisuje rezultate ocjene u metapodatke prijevoda, a njegov model bodovanja i ponašanje s metapodacima mogu se promijeniti.

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
| `-l`, `--language-code` | Da | Jedan kod jezika za ocjenu. Alias kodovi se normaliziraju. |
| `-r`, `--root-dir` | Ne | Korijen projekta. Zadano je trenutni direktorij. |
| `-c`, `--min-confidence` | Ne | Prag koji se koristi prilikom popisivanja prijevoda s niskim povjerenjem. Zadano je `0.7`. |
| `-d`, `--debug` | Ne | Omogući zapisivanje za otklanjanje pogrešaka. |
| `-s`, `--save-logs` | Ne | Spremi zapise razine DEBUG u `<root-dir>/logs/`. |
| `-f`, `--fast` | Ne | Samo procjena temeljena na pravilima. |
| `-D`, `--deep` | Ne | Samo procjena temeljena na LLM-u. |

Po zadanoj postavci `evaluate` koristi i procjene temeljene na pravilima i na LLM-u. Rezultati se zapisuju u metapodatke prijevoda i sažimaju se u konzoli.

## co-op-review

Pokrenite determinističke provjere održavanja prijevoda bez API vjerodajnica.

!!! note "Beta"
    `co-op-review` je beta deterministička naredba za pregled. Ne poziva pružatelje modela niti zapisuje datoteke, ali njezine provjere i shema izvještavanja o problemima mogu se mijenjati.

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

Pregledajte samo README nakon prijevoda koji obuhvaća samo README:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` zanemaruje druge dokumente i ugniježđene README-ove. Ne uspijeva ako nedostaje korijenski
`README.md`. U kombinaciji s `--changed-from`, pregledava samo README
kad se ta izvorna datoteka promijenila. Prijevod samo README-a ostavlja izvorni README
nepromijenjenim, uključujući bilo koje oznake zajedničkih odjeljaka.

Pregledajte samo izvorne datoteke promijenjene u odnosu na baznu referencu:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Ispišite GitHub-flavored Markdown izlaz za CI sažetke:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Opcije

| Opcija | Obavezno | Opis |
| --- | --- | --- |
| `-l`, `--language-code` | Ne | Kod jezika za pregled. Može se proslijediti više puta ili kao vrijednost odvojena razmacima. Zadano: svi otkriveni jezici prijevoda. |
| `-r`, `--root-dir` | Ne | Korijen projekta. Zadano je trenutni direktorij. |
| `--changed-from` | Ne | Git ref koji se koristi za ograničavanje pregleda na promijenjene izvorne datoteke. |
| `--readme-only` | Ne | Pregledaj samo prevod korijenskog `README.md`. |
| `--format` | Ne | Format izlaza: `text` ili `github`. Zadano: `text`. |

`co-op-review` trenutno provjerava nedostajuće prevedene datoteke, nedostajuće ili zastarjele metapodatke prijevoda, integritet Markdown frontmattera i ograda koda, nevažeći prevedeni notebook JSON i nedostajuće lokalne ciljeve poveznica u Markdownu ili za slike. Nedostajuće poveznice su po zadanoj postavci upozorenja; strukturni i problemi sa svježinom rezultiraju neuspjehom naredbe.

## co-op-translator-mcp

Pokrenite MCP poslužitelj Co-op Translatora za agente, uređivače i MCP-kompatibilne klijente.

```bash
co-op-translator-mcp
```

Zadani transport je `stdio`. Pogledajte vodič [MCP poslužitelj](mcp.md) za konfiguraciju klijenta, alate, resurse i napomene o sigurnosti.

### Opcije

| Opcija | Obavezno | Opis |
| --- | --- | --- |
| `--transport` | Ne | MCP transport: `stdio`, `streamable-http` ili `sse`. Zadano: `stdio`. |

## migrate-links

Ponovno obradi prevedene Markdown datoteke i ažuriraj poveznice u bilježnicama tako da upućuju na prevedene bilježnice kad su dostupne.

```bash
migrate-links -l "ko ja"
```

### Uobičajeni primjeri

Pregledajte ažuriranja poveznica:

```bash
migrate-links -l "ko" --dry-run
```

Obradite sve podržane jezike bez potvrde:

```bash
migrate-links -l "all" -y
```

Prepišite poveznice samo kad postoje prevedene bilježnice:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Opcije

| Opcija | Obavezno | Opis |
| --- | --- | --- |
| `-l`, `--language-codes` | Da | Kodovi jezika odvojeni razmacima, ili `"all"`. |
| `-r`, `--root-dir` | Ne | Korijen projekta. Zadano je trenutni direktorij. |
| `--image-dir` | Ne | Direktorij prevedenih slika u odnosu na korijen. Zadano: `translated_images`. |
| `--dry-run` | Ne | Prikaži datoteke koje bi se promijenile bez zapisivanja ažuriranja. |
| `--fallback-to-original`, `--no-fallback-to-original` | Ne | Koristi izvorne poveznice bilježnica kad prevedene bilježnice nedostaju. Omogućeno prema zadanim postavkama. |
| `-d`, `--debug` | Ne | Omogući zapisivanje za otklanjanje pogrešaka. |
| `-s`, `--save-logs` | Ne | Spremi zapise razine DEBUG u `<root-dir>/logs/`. |
| `-y`, `--yes` | Ne | Automatski potvrdi upite pri obradi svih jezika. |

## Okruženje

Kad naredba zahtijeva vjerodajnice pružatelja, konfigurirajte jedan od ovih skupova pružatelja. `translate --dry-run` i `co-op-review` ne zahtijevaju vjerodajnice pružatelja:

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

# Ili Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Prevođenje slika dodatno zahtijeva Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Izlazna struktura

Tekstualni prijevodi zapisuju se pod:

```text
translations/<language-code>/<original-path>
```

Izlaz prevedenih slika zapisuje se pod:

```text
translated_images/<language-code>/<original-path>
```

Na primjer, prevođenje `README.md` i `docs/setup.md` na korejski rezultira:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Primjeri za kopiranje i lijepljenje CLI naredbi

Prevedite Markdown na tri jezika:

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

Pregledajte prijevod Markdowna bez zapisivanja datoteka:

```bash
translate -l "de es" -md --dry-run
```

Popravi prijevode Markdowna s niskim povjerenjem:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Pokrenite Markdown prijevod prilagođen CI-u:

```bash
translate -l "ko ja" -md -y -s
```

Pregledajte prevedeni izlaz:

```bash
co-op-review -l "ko ja"
```

Pregledajte migraciju poveznica:

```bash
migrate-links -l "ko" --dry-run
```