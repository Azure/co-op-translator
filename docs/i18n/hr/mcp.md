# MCP poslužitelj

Co-op Translator uključuje Model Context Protocol poslužitelj za agente, uređivače i MCP-kompatibilne klijente.

Za zadano lokalno postavljanje, korisnici ne pokreću zaseban poslužitelj ručno. Konfiguriraju svoj MCP klijent, a klijent automatski pokreće `co-op-translator-mcp` preko `stdio` kada treba alate Co-op Translatora.

Ako birate između CLI-ja, Python API-ja i MCP-a, počnite s [Odaberite svoj radni tok](workflows.md).

Koristite MCP kada agent ili uređivač trebaju izravno pozvati Co-op Translator:

| Cilj korisnika | MCP alati |
| --- | --- |
| Prevesti jedan Markdown dokument, bilježnicu ili sliku | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Prevesti sadržaj Markdowna ili bilježnice koristeći model host agenta | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Prepisati prevedene Markdown ili bilježničke poveznice nakon odabira izlazne putanje | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prevesti cijelo spremište poput CLI-ja | `run_translation`, `translate_project` |
| Pregledati prevedeni izlaz bez LLM vjerodajnica | `run_review` |
| Ispitati mogućnosti i status okoline | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP poslužitelj uokviruje isti javni Python API dokumentiran u [Python API](api.md). Alati koji se oslanjaju na davatelja usluga koriste iste konfigurirane davatelje kao CLI i Python API. Alati uz podršku agenta pripremaju dijelove za MCP host agenta da prevede, a zatim koriste Co-op Translator za rekonstrukciju konačnog Markdowna ili bilježnice.

## Korak 1: Instalirajte i konfigurirajte Co-op Translator

Instalirajte Co-op Translator u Python okruženje koje će koristiti vaš MCP klijent:

```bash
pip install co-op-translator
```

Za lokalni razvoj iz ovog spremišta instalirajte paket u uređivom načinu:

```bash
pip install -e .
```

Odaberite način prevođenja koji će koristiti vaš MCP klijent:

| Način | Koristite za | Pristupni podaci |
| --- | --- | --- |
| Temeljen na davatelju | Co-op Translator poziva `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, ili `run_translation`. | Prevođenje Markdowna i bilježnica zahtijeva Azure OpenAI ili OpenAI. Prevođenje slika također zahtijeva Azure AI Vision. |
| Pomoć agenta | MCP host agent prevodi dijelove vraćene s `start_markdown_agent_translation` ili `start_notebook_agent_translation`. | Nisu potrebne Co-op Translator LLM vjerodajnice za Markdown ili dijelove bilježnica. Prevođenje slika još nije pokriveno načinom uz podršku agenta. |

Ako započinjete s prevođenjem Markdowna ili bilježnica unutar agenta kao što su Codex ili Claude Code, započnite s načinom uz podršku agenta. Koristite način temeljen na davatelju kada želite da Co-op Translator sam poziva vaše konfigurirane davatelje, kada prevodite slike ili kada pokrećete prijevod na razini spremišta poput CLI-ja.

Konfigurirajte vjerodajnice davatelja usluga samo za tijekove rada koji se oslanjaju na davatelja:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Prevođenje slika koje se oslanja na davatelja dodatno treba:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## Korak 2: Konfigurirajte svoj MCP klijent

Za uobičajeno lokalno `stdio` postavljanje, dodajte Co-op Translator u konfiguraciju vašeg MCP klijenta. Klijent će automatski pokrenuti i zaustaviti proces.

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

Konfiguracija izvornog spremišta na Windowsu:

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

Konfiguracija izvornog spremišta na macOS-u ili Linuxu:

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

Nakon promjene konfiguracije MCP klijenta, ponovno pokrenite ili učitajte klijenta kako bi otkrio novi poslužitelj.

## Korak 3: Provjerite poslužitelj u klijentu

Zatražite od MCP klijenta da navede dostupne alate, ili najprije pozovite jednog od pomoćnika samo za čitanje:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Korisne prve provjere:

| Alat | Što provjeriti |
| --- | --- |
| `get_api_overview` | Potvrđuje da je poslužitelj dostupan i prikazuje dostupne tijekove rada. |
| `list_supported_languages` | Potvrđuje da se jezični podaci iz paketa mogu učitati. |
| `get_configuration_status` | Potvrđuje dostupnost LLM i Vision davatelja bez otkrivanja tajnih vrijednosti. |

## Korak 4: Odaberite radni tok

### Prevođenje pojedinačnih datoteka ili dokumenata

Koristite alate temeljen na davatelju kada MCP klijent već ima sadržaj dokumenta ili putanju slike i kada Co-op Translator treba pozvati konfigurirane prevoditeljske davatelje.

Za Markdown:

1. Pozovite `translate_markdown_content` s `document`, `language_code` i opcionalno `source_path`.
2. Ako će prevedeni rezultat biti zapisan u Co-op Translator izlazni raspored, pozovite `rewrite_markdown_paths`.
3. Dopustite klijentu da zapisuje ili vraća konačni `content`.

Za bilježnice:

1. Pozovite `translate_notebook_content` s JSON-om bilježnice i `language_code`.
2. Pozovite `rewrite_notebook_paths` ako prevedene bilježničke poveznice trebaju prilagodbu za ciljnu putanju.
3. Zapišite ili vratite konačni notebook JSON.

Za slike:

1. Pozovite `translate_image_content` s `image_path`, `language_code`, i opcionalno `root_dir` ili `fast_mode`.
2. Pročitajte vraćeni `data_base64` i `mime_type`.
3. Ako je `output_path` naveden, prevedena slika se također sprema na tu putanju.

Alati za sadržaj ne obavljaju otkrivanje projekata, ažuriranja metapodataka, odricanja ili automatsko prepisivanje putanja. Ako želite da host agent prevede Markdown ili dijelove bilježnice bez Co-op Translator LLM vjerodajnica, upotrijebite dolje opisani tijek rada uz pomoć agenta.

### Prevođenje uz model host-agenta

Koristite alate uz podršku agenta kada želite da MCP host agent, poput pomoćnika za kodiranje, proizvede prevedeni tekst umjesto konfiguriranja Azure OpenAI ili OpenAI za Co-op Translator.

U chat-baziranom MCP klijentu obično ne trebate sami pisati JSON alata. Zamolite agenta da koristi tijek rada uz podršku agenta:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Za bilježnice primijenite isti obrazac:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Ako vaš MCP klijent podržava server promptove, upotrijebite `agent_assisted_markdown_translation_prompt` da klijent učita iste upute tijeka rada.

Za Markdown:

1. Pozovite `start_markdown_agent_translation` sa `document`, `language_code` i opcionalno `source_path`.
2. Prevedite svaki vraćeni dio u host agentu prateći `prompt` za dio.
3. Pozovite `finish_markdown_agent_translation` s izvornim `job` i prevedenim dijelovima koristeći `chunk_id` i `translated_text`.
4. Ako će se sadržaj zapisati na prevedenu ciljnu putanju, pozovite `rewrite_markdown_paths`.

Za bilježnice:

1. Pozovite `start_notebook_agent_translation` s JSON-om bilježnice i `language_code`.
2. Prevedite svaki vraćeni dio u host agentu.
3. Pozovite `finish_notebook_agent_translation` s izvornim `job` i prevedenim dijelovima.
4. Pozovite `rewrite_notebook_paths` ako prevedene bilježničke poveznice trebaju prilagodbu ciljnoj putanji.

Alati uz podršku agenta ne pozivaju Azure OpenAI ili OpenAI iz Co-op Translatora. Host agent odgovoran je za prevođenje vraćenih dijelova. Co-op Translator se brine za razdvajanje Markdowna na dijelove, očuvanje placeholdera, rekonstrukciju frontmattera, zamjenu ćelija u bilježnici i normalizaciju nakon prevođenja.

### Prevođenje cijelog spremišta

Upotrijebite `run_translation` kada korisnik želi da se Co-op Translator ponaša poput `translate` CLI-ja.

Prevođenje spremišta po zadanom koristi `dry_run=true` kako bi agent mogao pregledati opseg prije promjena datoteka:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Da biste omogućili zapise, pozivatelj mora postaviti i `dry_run=false` i `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` je izložen kao kompatibilna alias funkcija za `run_translation`.

### Pregled prevedenog izlaza

Upotrijebite `run_review` za determinističke provjere koje ne zahtijevaju LLM ili Vision vjerodajnice:

!!! note "Beta"
    MCP exposes the beta `run_review` API. It is safe for read-only review workflows, but review checks and issue schemas may evolve.

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

Ručna pokretanja su uglavnom za otklanjanje pogrešaka ili za transportne mehanizme koji se ponašaju poput dugotrajnog poslužitelja.

Otklonite pogreške zadanim stdio poslužiteljem:

```bash
co-op-translator-mcp
```

Pokrenite iz izvornog preuzimanja:

```bash
python -m co_op_translator.mcp.server
```

Pokrenite dugoživući HTTP ili SSE poslužitelj:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Za lokalne integracije uređivača i agenta, dajte prednost konfiguraciji `stdio` kojom upravlja klijent iz Koraka 2.

## Alati

| Alat | Svrha | Piše datoteke |
| --- | --- | --- |
| `translate_markdown_content` | Prevedi string Markdowna. | Ne |
| `translate_notebook_content` | Prevedi Markdown ćelije u JSON-u bilježnice. | Ne |
| `translate_image_content` | Prevedi tekst na jednoj slici i vrati base64 podatke slike. | Opcionalno, samo kada je `output_path` naveden |
| `start_markdown_agent_translation` | Pripremi Markdown dijelove da ih host agent prevede bez Co-op Translator LLM vjerodajnica. | Ne |
| `finish_markdown_agent_translation` | Rekonstruiraj Markdown iz dijelova prevedenih od strane host-agenta. | Ne |
| `start_notebook_agent_translation` | Pripremi dijelove Markdown ćelija bilježnice da ih host agent prevede. | Ne |
| `finish_notebook_agent_translation` | Rekonstruiraj notebook JSON iz dijelova prevedenih od strane host-agenta. | Ne |
| `rewrite_markdown_paths` | Prepiši putanje u tijelu Markdowna i frontmatteru za prevedeni cilj. | Ne |
| `rewrite_notebook_paths` | Prepiši putanje unutar Markdown ćelija bilježnice. | Ne |
| `run_translation` | Pokreni prijevod projekta poput CLI-ja. | Da kada su `dry_run=false` i `confirm_write=true` |
| `translate_project` | Kompatibilni alias za `run_translation`. | Da kada su `dry_run=false` i `confirm_write=true` |
| `run_review` | Pokreni determinističke provjere pregleda. | Ne |
| `get_configuration_status` | Prijavi konfigurirane LLM i Vision davatelje bez otkrivanja tajni. | Ne |
| `list_supported_languages` | Nabroji podržane ciljne kodove jezika. | Ne |
| `get_api_overview` | Opis dostupnih MCP tijekova rada i alata. | Ne |

## Resursi

| URI resursa | Svrha |
| --- | --- |
| `co-op://api` | JSON pregled tijekova rada i alata. |
| `co-op://supported-languages` | JSON popis podržanih kodova jezika. |
| `co-op://configuration` | JSON sažetak dostupnosti davatelja bez tajni. |

## Upute

| Prompt | Svrha |
| --- | --- |
| `translate_markdown_document_prompt` | Vodi MCP klijenta kroz prevođenje sadržaja uz opcionalno prepisivanje putanja. |
| `agent_assisted_markdown_translation_prompt` | Vodi MCP klijenta kroz prevođenje Markdowna pomoću host-agenta bez Co-op Translator LLM vjerodajnica. |
| `translate_repository_prompt` | Vodi MCP klijenta kroz prijevod spremišta koji prvo radi dry-run. |

## Primjeri za kopiranje i lijepljenje

Prevedite Markdown sadržaj:

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

Prepišite prevedene Markdown poveznice:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

Prevedite Markdown uz model host-agenta:

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

Nakon što host agent prevede svaki vraćeni dio, završite posao s kompletnim `job` objektom vraćenim od `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Pregled prevođenja spremišta:

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
| MCP klijent ne može pronaći `co-op-translator-mcp`. | Upotrijebite apsolutnu putanju do Python izvršne datoteke i `["-m", "co_op_translator.mcp.server"]` source checkout konfiguraciju. |
| Poslužitelj je naveden, ali prijevod ne uspijeva. | Pozovite `get_configuration_status` i potvrdite da je LLM davatelj dostupan. |
| Želite prevođenje Markdowna ili bilježnica bez Azure OpenAI/OpenAI ključeva. | Upotrijebite `start_markdown_agent_translation` / `finish_markdown_agent_translation` ili ekvivalente za bilježnice kako bi host agent preveo dijelove. |
| Prevođenje slika ne uspijeva. | Potvrdite da su postavljene varijable Azure AI Vision i pozovite `get_configuration_status`. |
| Prevođenje spremišta ne zapisuje datoteke. | Postavite `dry_run=false` i `confirm_write=true` tek nakon izričitog odobrenja korisnika. |
| Promjene u konfiguraciji klijenta se ne pojavljuju. | Ponovno pokrenite ili ponovno učitajte MCP klijenta. |

## Sigurnosne napomene

- Pozivi MCP alata kontrolira model u host aplikaciji, stoga je prevođenje spremišta po zadanoj postavci dry-run.
- Potpuno prevođenje spremišta može stvoriti, ažurirati ili ukloniti mnogo datoteka. Zahtijevajte izričito odobrenje korisnika prije postavljanja `confirm_write=true`.
- Alat za status konfiguracije nikada ne vraća API ključeve, krajnje točke ili druge tajne vrijednosti.
- Prevođenje slika vraća base64 podatke slike. Velike slike mogu proizvesti velike odgovore alata.
- Alati uz podršku agenta vraćaju izvorne dijelove i promptove hostu MCP. Koristite ih samo sa sadržajem koji je korisniku ugodno poslati tom modelu host-agenta.