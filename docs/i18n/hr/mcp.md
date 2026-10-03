# MCP poslužitelj

Co-op Translator uključuje MCP (Model Context Protocol) poslužitelj za agente, uređivače i MCP-kompatibilne klijente.

Za zadanu lokalnu postavku korisnici ne pokreću zaseban poslužitelj ručno. Oni konfiguriraju svoj MCP klijent, a klijent automatski pokreće `co-op-translator-mcp` preko `stdio` kada mu trebaju alati Co-op Translatora.

Ako odlučujete između CLI-ja, Python API-ja i MCP-a, započnite s [Odaberite svoj tijek rada](workflows.md).

Koristite MCP kada agent ili uređivač treba izravno pozvati Co-op Translator:

| Korisnički cilj | MCP alati |
| --- | --- |
| Prevesti jedan Markdown dokument, bilježnicu (notebook) ili sliku | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Prevesti sadržaj Markdowna ili bilježnice pomoću modela host-agenta | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Prepiši prevedene poveznice u Markdownu ili bilježnici nakon odabira izlazne putanje | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prevesti cijeli repozitorij kao CLI | `run_translation`, `translate_project` |
| Pregledati prevedeni izlaz bez LLM vjerodajnica | `run_review` |
| Pregledati mogućnosti i status okoline | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP poslužitelj obavija isti javni Python API dokumentiran u [Python API](api.md). Alati koji koriste dobavljače (provider-backed) koriste iste konfigurirane providere kao CLI i Python API. Alati uz pomoć agenta (agent-assisted) pripremaju dijelove za MCP host-agenta da ih prevede, a zatim koriste Co-op Translator za rekonstrukciju konačnog Markdowna ili bilježnice.

## Korak 1: Instalirajte i konfigurirajte Co-op Translator

Instalirajte Co-op Translator u Python okruženje koje će koristiti vaš MCP klijent:

```bash
pip install co-op-translator
```

Za lokalni razvoj iz ovog repozitorija, instalirajte paket u uređivom načinu (editable mode):

```bash
pip install -e .
```

Odaberite način prevođenja koji će vaš MCP klijent koristiti:

| Način | Koristi se za | Vjerodajnice |
| --- | --- | --- |
| Podržano od strane providera | Co-op Translator poziva `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, ili `run_translation`. | Prevođenje zahtijeva Azure OpenAI, OpenAI ili Anthropic. Prevođenje slika također zahtijeva Azure AI Vision. |
| Uz pomoć agenta | MCP host-agent prevodi dijelove koje vraćaju `start_markdown_agent_translation` ili `start_notebook_agent_translation`. | Za Markdown ili dijelove bilježnice nisu potrebne LLM vjerodajnice Co-op Translatora. Prevođenje slika još nije pokriveno u načinu rada uz pomoć agenta. |

Ako započinjete s prevođenjem Markdowna ili bilježnice unutar agenta kao što su Codex ili Claude Code, počnite s načinom rada uz pomoć agenta. Koristite način podržan od providera kada želite da sam Co-op Translator poziva vaše konfigurirane providere, kada prevodite slike ili kada pokrećete prevođenje na razini repozitorija poput CLI-ja.

Konfigurirajte jednog providera za radne tokove podržane od providera:

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

Prevođenje slika u načinu rada podržanom od providera dodatno zahtijeva:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Način rada uz pomoć agenta trenutno pokriva Markdown i Markdown ćelije u bilježnicama. Prevođenje slika i dalje koristi pipeline za slike podržan od providera i zahtijeva Azure AI Vision za OCR i renderiranje prilagođeno rasporedu.

## Korak 2: Konfigurirajte svoj MCP klijent

Za uobičajenu lokalnu `stdio` postavku, dodajte Co-op Translator u konfiguraciju vašeg MCP klijenta. Klijent će automatski pokretati i zaustavljati proces.

Konfiguracija instaliranog paketa:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

Konfiguracija izvornog checkouta na Windowsu:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

Konfiguracija izvornog checkouta na macOS-u ili Linuxu:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

Nakon promjene konfiguracije MCP klijenta, ponovno pokrenite ili osvježite klijenta kako bi mogao otkriti novi poslužitelj.

## Korak 3: Provjerite poslužitelj u klijentu

Naredite MCP klijentu da navede dostupne alate ili najprije pozovite jednog od pomoćnika samo za čitanje:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Korisne početne provjere:

| Alat | Što provjeriti |
| --- | --- |
| `get_api_overview` | Potvrđuje da je poslužitelj dostupan i prikazuje dostupne radne tokove. |
| `list_supported_languages` | Potvrđuje da se pakirani podaci o jezicima mogu učitati. |
| `get_configuration_status` | Potvrđuje dostupnost LLM i Vision providera bez izlaganja tajnih vrijednosti. |

## Korak 4: Odaberite tijek rada

### Prevođenje pojedinačnih datoteka ili dokumenata

Koristite alate podržane od providera kada MCP klijent već ima sadržaj dokumenta ili putanju slike i kada Co-op Translator treba pozvati konfigurirane providere za prevođenje.

Za Markdown:

1. Pozovite `translate_markdown_content` s `document`, `language_code` i po želji `source_path`.
2. Ako će prevedeni rezultat biti zapisan u izlazni raspored Co-op Translatora, pozovite `rewrite_markdown_paths`.
3. Neka klijent upiše ili vrati konačni `content`.

Za bilježnice:

1. Pozovite `translate_notebook_content` s JSON-om bilježnice i `language_code`.
2. Pozovite `rewrite_notebook_paths` ako prevedene poveznice u bilježnici trebaju biti prilagođene za ciljnu putanju.
3. Zapišite ili vratite konačni JSON bilježnice.

Za slike:

1. Pozovite `translate_image_content` s `image_path`, `language_code` i opcionalno `root_dir` ili `fast_mode`.
2. Pročitajte vraćeni `data_base64` i `mime_type`.
3. Ako je `output_path` naveden, prevedena slika će biti spremljena i na tu putanju.

Alati za sadržaj ne obavljaju otkrivanje projekta, ažuriranja metapodataka, odricanja ili automatsko prepisivanje putanja. Ako želite da host-agent prevede dijelove Markdowna ili bilježnica bez LLM vjerodajnica Co-op Translatora, upotrijebite dolje opisani tijek rada uz pomoć agenta.

### Prevođenje pomoću modela host-agenta

Koristite alate uz pomoć agenta kada želite da MCP host-agent, poput asistenta za kodiranje, generira prevedeni tekst umjesto da konfigurirate LLM providera za Co-op Translator.

U chat-baziranom MCP klijentu obično ne trebate sami pisati JSON alata. Zamolite agenta da koristi tijek rada uz pomoć agenta:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Za bilježnice, koristite isti obrazac:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Ako vaš MCP klijent podržava server promptove, upotrijebite `agent_assisted_markdown_translation_prompt` kako bi klijent učitao iste upute tijeka rada.

Za Markdown:

1. Pozovite `start_markdown_agent_translation` s `document`, `language_code` i po želji `source_path`.
2. Prevedite svaki vraćeni dio u host-agentu slijedeći `prompt` za dio.
3. Pozovite `finish_markdown_agent_translation` s originalnim `job` i prevedenim dijelovima koristeći `chunk_id` i `translated_text`.
4. Ako će se sadržaj zapisati na prevedenu ciljnu putanju, pozovite `rewrite_markdown_paths`.

Za bilježnice:

1. Pozovite `start_notebook_agent_translation` s JSON-om bilježnice i `language_code`.
2. Prevedite svaki vraćeni dio u host-agentu.
3. Pozovite `finish_notebook_agent_translation` s originalnim `job` i prevedenim dijelovima.
4. Pozovite `rewrite_notebook_paths` ako prevedene poveznice u bilježnici trebaju prilagodbu ciljnih putanja.

Alati uz pomoć agenta ne pozivaju konfigurirani LLM provider iz Co-op Translatora. Host-agent je odgovoran za prevođenje vraćenih dijelova. Co-op Translator se brine o razdvajanju Markdowna na dijelove, očuvanju rezerviranih mjesta (placeholdera), rekonstrukciji frontmattera, zamjeni ćelija bilježnice i normalizaciji nakon prevođenja.

### Prevođenje cijelog repozitorija

Upotrijebite `run_translation` kada korisnik želi da se Co-op Translator ponaša poput `translate` CLI-ja.

Prevođenje repozitorija prema zadanim postavkama ima `dry_run=true` kako bi agent mogao pregledati opseg prije promjena datoteka:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Rezultat `run_translation` uključuje polje `events` s verzioniranim
`co-op.translation.event.v1` događajima napretka. MCP klijenti bi trebali koristiti polja poput
`type`, `stage_key`, `completed`, `total` i `current_path` umjesto
parsiranja uhvaćenog konzolnog teksta. Proslijedite `json_events_path` da također zapišete te događaje
u NDJSON datoteku.

Da bi se omogućila pisanja, pozivatelj mora postaviti i `dry_run=false` i `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` je izložen kao alias radi kompatibilnosti za `run_translation`.

### Pregled prevedenog izlaza

Upotrijebite `run_review` za determinističke provjere koje ne zahtijevaju LLM ili Vision vjerodajnice:

!!! note "Beta"
    MCP izlaže beta API `run_review`. Siguran je za tijekove rada samo za pregled, ali provjere pregleda i sheme problema mogu se razvijati.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Rezultat uključuje snimljeni tekstualni izlaz i strukturirani sažetak pregleda kada je dostupan.

## Ručno pokretanje poslužitelja

Ručna pokretanja uglavnom su za otklanjanje pogrešaka ili za transportere koji se ponašaju poput dugotrajnih poslužitelja.

Otklonite pogreške na zadanim stdio poslužitelju:

```bash
co-op-translator-mcp
```

Pokrenite iz izvornog checkouta:

```bash
python -m co_op_translator.mcp.server
```

Pokrenite dugotrajni HTTP ili SSE poslužitelj:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Za lokalne integracije uređivača i agenata, preferirajte konfiguraciju `stdio` kojom upravlja klijent u Koraku 2.

## Alati

| Alat | Svrha | Piše datoteke |
| --- | --- | --- |
| `translate_markdown_content` | Prevede Markdown niz. | Ne |
| `translate_notebook_content` | Prevede Markdown ćelije u JSON-u bilježnice. | Ne |
| `translate_image_content` | Prevede tekst na jednoj slici i vraća base64 podatke slike. | Opcionalno, samo kada je `output_path` naveden |
| `start_markdown_agent_translation` | Pripremi dijelove Markdowna da ih host-agent prevede bez LLM vjerodajnica Co-op Translatora. | Ne |
| `finish_markdown_agent_translation` | Rekonstruira Markdown iz host-agentom prevedenih dijelova. | Ne |
| `start_notebook_agent_translation` | Pripremi dijelove Markdown ćelija bilježnice za prevođenje od strane host-agenta. | Ne |
| `finish_notebook_agent_translation` | Rekonstruira JSON bilježnice iz host-agentom prevedenih dijelova. | Ne |
| `rewrite_markdown_paths` | Prepiše tijelo Markdowna i putanje u frontmatteru za prevedenu ciljnu lokaciju. | Ne |
| `rewrite_notebook_paths` | Prepiše putanje unutar Markdown ćelija bilježnice. | Ne |
| `run_translation` | Pokreće prevođenje na razini projekta poput CLI-ja. | Da kada su `dry_run=false` i `confirm_write=true` |
| `translate_project` | Alias za kompatibilnost za `run_translation`. | Da kada su `dry_run=false` i `confirm_write=true` |
| `run_review` | Pokreće determinističke provjere pregleda. | Ne |
| `get_configuration_status` | Izvještava o konfiguriranim LLM i Vision providerima bez izlaganja tajni. | Ne |
| `list_supported_languages` | Navodi podržane kodove ciljanih jezika. | Ne |
| `get_api_overview` | Opisuje dostupne MCP radne tokove i alate. | Ne |

## Resursi

| URI resursa | Svrha |
| --- | --- |
| `co-op://api` | JSON pregled radnih tokova i alata. |
| `co-op://supported-languages` | JSON popis podržanih kodova jezika. |
| `co-op://configuration` | JSON sažetak dostupnosti providera bez tajnih podataka. |

## Promptovi

| Prompt | Svrha |
| --- | --- |
| `translate_markdown_document_prompt` | Vodite MCP klijenta kroz prevođenje sadržaja plus opcionalno prepisivanje putanja. |
| `agent_assisted_markdown_translation_prompt` | Vodite MCP klijenta kroz prevođenje Markdowna uz pomoć host-agenta bez LLM vjerodajnica Co-op Translatora. |
| `translate_repository_prompt` | Vodite MCP klijenta kroz prevođenje repozitorija s najprije dry-run opcijom. |

## Primjeri za kopiranje i lijepljenje

Prevedi sadržaj Markdowna:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Prepiši prevedene Markdown poveznice:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

Prevedi Markdown pomoću modela host-agenta:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Nakon što host-agent prevede svaki vraćeni dio, dovršite posao s kompletnim objektom `job` koji vraća `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Pregledaj prevođenje repozitorija:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## Rješavanje problema

| Problem | Što pokušati |
| --- | --- |
| MCP klijent ne može pronaći `co-op-translator-mcp`. | Koristite apsolutnu putanju do Python izvršne datoteke i konfiguraciju izvornog checkouta `["-m", "co_op_translator.mcp.server"]`. |
| Poslužitelj je naveden, ali prevođenje ne uspijeva. | Pozovite `get_configuration_status` i potvrdite da je LLM provider dostupan. |
| Želite prevođenje Markdowna ili bilježnica bez vjerodajnica providera. | Koristite `start_markdown_agent_translation` / `finish_markdown_agent_translation` ili ekvivalente za bilježnice tako da host-agent prevede dijelove. |
| Prevođenje slike ne uspijeva. | Potvrdite da su varijable za Azure AI Vision postavljene i pozovite `get_configuration_status`. |
| Prevođenje repozitorija ne zapisuje datoteke. | Postavite `dry_run=false` i `confirm_write=true` tek nakon izričitog odobrenja korisnika. |
| Promjene u konfiguraciji klijenta se ne pojavljuju. | Ponovno pokrenite ili osvježite MCP klijenta. |

## Napomene o sigurnosti

- Pozivi MCP alata kontrolira model host-aplikacije, stoga je prevođenje repozitorija prema zadanim postavkama u dry-run načinu.
- Potpuno prevođenje repozitorija može stvoriti, ažurirati ili ukloniti mnoge datoteke. Zahtijevajte izričito odobrenje korisnika prije postavljanja `confirm_write=true`.
- Alat za status konfiguracije nikada ne vraća API ključeve, krajnje točke (endpoints) ili druge tajne vrijednosti.
- Prevođenje slika vraća base64 podatke slike. Velike slike mogu proizvesti velike odgovore alata.
- Alati uz pomoć agenta vraćaju izvorne dijelove i promptove MCP hostu. Koristite ih samo s sadržajem koji je korisnik spreman poslati tom modelu host-agenta.