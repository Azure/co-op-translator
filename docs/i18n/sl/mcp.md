# MCP strežnik

Co-op Translator vključuje strežnik Model Context Protocol za agente, urejevalnike in odjemalce, združljive z MCP.

Pri privzeti lokalni konfiguraciji uporabniki ročno ne poganjajo ločenega strežnika. Konfigurirajo svoj MCP odjemalec, ta pa samodejno zažene `co-op-translator-mcp` preko `stdio`, ko potrebuje orodja Co-op Translator.

Če se odločate med CLI, Python API in MCP, začnite z [Izberite svoj potek dela](workflows.md).

Uporabite MCP, ko naj agent ali urejevalnik neposredno kliče Co-op Translator:

| Cilj uporabnika | MCP orodja |
| --- | --- |
| Prevesti en Markdown dokument, notebook ali sliko | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Prevesti vsebino Markdowna ali notebooka z modelom gostiteljskega agenta | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Prepisati prevedene povezave v Markdownu ali notebooku po izbiri izhodne poti | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prevesti celoten repozitorij, kot pri CLI | `run_translation`, `translate_project` |
| Pregledati prevedeno izhodno vsebino brez poverilnic LLM | `run_review` |
| Preveriti zmožnosti in stanje okolja | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP strežnik zavije enak javni Python API, dokumentiran v [Python API](api.md). Orodja s podporo ponudnika uporabljajo enake konfigurirane ponudnike kot CLI in Python API. Orodja s pomočjo agenta pripravijo kose za prevajanje s strani MCP gostiteljskega agenta, nato pa Co-op Translator uporabi za rekonstrukcijo končnega Markdowna ali notebooka.

## Korak 1: Namestitev in konfiguracija Co-op Translator

Namestite Co-op Translator v Python okolje, ki ga bo uporabljal vaš MCP odjemalec:

```bash
pip install co-op-translator
```

Za lokalni razvoj iz tega repozitorija namestite paket v urejevalnem načinu:

```bash
pip install -e .
```

Izberite način prevajanja, ki ga bo uporabljal vaš MCP odjemalec:

| Način | Uporabno za | Poverilnice |
| --- | --- | --- |
| S podporo ponudnika | Co-op Translator kliče `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, ali `run_translation`. | Prevajanje zahteva Azure OpenAI, OpenAI ali Anthropic. Prevodi slik prav tako zahtevajo Azure AI Vision. |
| S asistenco agenta | MCP gostiteljski agent prevede kose, ki jih vrne `start_markdown_agent_translation` ali `start_notebook_agent_translation`. | Za kose Markdown ali notebook ni potrebnih poverilnic ponudnika LLM za Co-op Translator. Prevajanje slik še ni zajeto v načinu s pomočjo agenta. |

Če začnete s prevajanjem Markdowna ali notebooka znotraj agenta, kot sta Codex ali Claude Code, začnite z načinom s pomočjo agenta. Uporabite način s podporo ponudnika, ko želite, da Co-op Translator sam kliče vaše konfigurirane ponudnike, ko prevajate slike ali ko izvajate prevajanje na ravni repozitorija, kot pri CLI.

Konfigurirajte enega ponudnika za delovne postopke s podporo ponudnika:

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

Prevajanje slik s podporo ponudnika dodatno zahteva:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Način s pomočjo agenta trenutno pokriva Markdown in Markdown celice v notebookih. Prevodi slik še vedno uporabljajo pipeline slik s podporo ponudnika in zahtevajo Azure AI Vision za OCR in upoštevanje postavitve.

## Korak 2: Konfigurirajte svoj MCP odjemalec

Za običajno lokalno nastavitev `stdio` dodajte Co-op Translator v konfiguracijo vašega MCP odjemalca. Odjemalec bo proces samodejno zagnal in ustavil.

Konfiguracija nameščenega paketa:

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

Konfiguracija preverjanja izvora v sistemu Windows:

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

Konfiguracija preverjanja izvora na macOS ali Linux:

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

Po spremembi konfiguracije MCP odjemalca znova zaženite ali osvežite odjemalca, da lahko odkrije nov strežnik.

## Korak 3: Preverite strežnik v odjemalcu

Prosite MCP odjemalca, naj izpiše razpoložljiva orodja, ali najprej pokličite enega izmed pomočnikov samo za branje:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Uporabni začetni pregledi:

| Orodje | Kaj preveriti |
| --- | --- |
| `get_api_overview` | Potrdi, da je strežnik dosegljiv in prikaže razpoložljive poteke dela. |
| `list_supported_languages` | Potrdi, da je mogoče naložiti vključene podatke o jezikih. |
| `get_configuration_status` | Potrdi razpoložljivost ponudnikov LLM in Vision, ne da bi razkril skrivne vrednosti. |

## Korak 4: Izberite potek dela

### Prevajanje posameznih datotek ali dokumentov

Uporabite orodja s podporo ponudnika, kadar ima MCP odjemalec že vsebino dokumenta ali pot do slike in naj Co-op Translator kliče konfigurirane ponudnike prevajanja.

Za Markdown:

1. Pokličite `translate_markdown_content` z `document`, `language_code`, in po želji `source_path`.
2. Če bo prevedeni rezultat zapisan v izhodno postavitev Co-op Translator, pokličite `rewrite_markdown_paths`.
3. Naj odjemalec zapiše ali vrne končno `content`.

Za notebooke:

1. Pokličite `translate_notebook_content` z JSON-om notebooka in `language_code`.
2. Pokličite `rewrite_notebook_paths`, če je treba prilagoditi prevedene povezave v notebooku za ciljno pot.
3. Zapišite ali vrnite končni JSON notebooka.

Za slike:

1. Pokličite `translate_image_content` z `image_path`, `language_code` in po želji `root_dir` ali `fast_mode`.
2. Preberite vrnjeni `data_base64` in `mime_type`.
3. Če je podan `output_path`, je prevedena slika prav tako shranjena na to pot.

Orodja za vsebine ne izvajajo odkrivanja projektov, posodobitev metapodatkov, opozoril ali samodejnega prepisovanja poti. Če želite, da gostiteljski agent prevede kose Markdowna ali notebooka brez poverilnic ponudnika LLM za Co-op Translator, uporabite spodnji potek dela s pomočjo agenta.

### Prevajanje z modelom gostiteljskega agenta

Uporabite orodja s pomočjo agenta, kadar želite, da MCP gostiteljski agent, na primer programerski pomočnik, proizvede prevedeno besedilo namesto konfiguriranja ponudnika LLM za Co-op Translator.

V klepetalnem MCP odjemalcu običajno ne potrebujete sami pisati JSON orodja. Prosite agenta, naj uporabi potek dela s pomočjo agenta:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Za notebooke uporabite enak vzorec:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Če vaš MCP odjemalec podpira strežniške pozive, uporabite `agent_assisted_markdown_translation_prompt`, da odjemalec naloži enaka navodila poteka dela.

Za Markdown:

1. Pokličite `start_markdown_agent_translation` z `document`, `language_code` in po želji `source_path`.
2. V gostiteljskem agentu prevedite vsak vrnjen kos tako, da sledite `prompt`-u kosa.
3. Pokličite `finish_markdown_agent_translation` z originalnim `job` in prevedenimi kosi, ki uporabljajo `chunk_id` in `translated_text`.
4. Če bo vsebina zapisana na prevedeno ciljno pot, pokličite `rewrite_markdown_paths`.

Za notebooke:

1. Pokličite `start_notebook_agent_translation` z JSON-om notebooka in `language_code`.
2. V gostiteljskem agentu prevedite vsak vrnjen kos.
3. Pokličite `finish_notebook_agent_translation` z izvirnim `job` in prevedenimi deli.
4. Pokličite `rewrite_notebook_paths`, če je treba prilagoditi ciljne poti prevedenih povezav v zvezku.

Agentom podprta orodja ne kličejo nastavljenega ponudnika LLM iz Co-op Translatorja. Gostiteljski agent je odgovoren za prevajanje vrnjenih delov. Co-op Translator skrbi za razbijanje Markdowna na kose, ohranjanje nadomestkov, rekonstrukcijo frontmatterja, zamenjavo celic zvezka in normalizacijo po prevodu.

### Prevajanje celotnega repozitorija

Uporabite `run_translation`, kadar želi uporabnik, da se Co-op Translator obnaša kot ukaz `translate` v CLI.

Prevajanje repozitorija je privzeto nastavljeno na `dry_run=true`, tako da lahko agent pregleda obseg pred spremembami datotek:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Rezultat `run_translation` vključuje polje `events` z verzioniranimi
`co-op.translation.event.v1` dogodki napredka. MCP odjemalci naj uporabljajo polja, kot
so `type`, `stage_key`, `completed`, `total` in `current_path`, namesto da bi
analizirali zajeto besedilo konzole. Podajte `json_events_path`, da se ti dogodki
tudi zapišejo v NDJSON datoteko.

Za omogočanje zapisov mora klicatelj nastaviti `dry_run=false` in `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` je na voljo kot združljivostni alias za `run_translation`.

### Pregled prevedene vsebine

Uporabite `run_review` za deterministične preveritve, ki ne zahtevajo poverilnic za LLM ali Vision:

!!! note "Beta"
    MCP ponuja beta API `run_review`. Primeren je za postopke pregleda samo za branje, vendar se lahko preverjanja pregleda in sheme težav razvijajo.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Rezultat vključuje zajeti besedilni izhod in strukturiran povzetek pregleda, če je na voljo.

## Ročni zagon strežnika

Ročni zagoni so namenjeni predvsem razhroščevanju ali za transporte, ki se obnašajo kot dolgotrajni strežniki.

Odpravljanje napak privzetega stdio strežnika:

```bash
co-op-translator-mcp
```

Zaženite iz izvoda izvorne kode:

```bash
python -m co_op_translator.mcp.server
```

Zaženite dolgotrajen HTTP ali SSE strežnik:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Za integracije lokalnih urejevalnikov in agentov raje izberite konfiguracijo `stdio`, ki jo upravlja odjemalec, v koraku 2.

## Orodja

| Orodje | Namen | Zapisuje datoteke |
| --- | --- | --- |
| `translate_markdown_content` | Prevede Markdown niz. | Ne |
| `translate_notebook_content` | Prevede Markdown celice v JSON zapisu zvezka. | Ne |
| `translate_image_content` | Prevede besedilo na eni sliki in vrne base64 podatke slike. | Neobvezno, le kadar je podan `output_path` |
| `start_markdown_agent_translation` | Pripravi Markdown kose, da jih gostiteljski agent prevede brez poverilnic ponudnika LLM Co-op Translatorja. | Ne |
| `finish_markdown_agent_translation` | Obnovi Markdown iz prevedenih kosov gostiteljskega agenta. | Ne |
| `start_notebook_agent_translation` | Pripravi kose Markdown-celic v zvezku za prevajanje s strani gostiteljskega agenta. | Ne |
| `finish_notebook_agent_translation` | Obnovi JSON zvezka iz prevedenih kosov gostiteljskega agenta. | Ne |
| `rewrite_markdown_paths` | Prepiše poti v telesu Markdowna in frontmatterju za prevedeno ciljno mesto. | Ne |
| `rewrite_notebook_paths` | Prepiše poti znotraj Markdown celic v zvezku. | Ne |
| `run_translation` | Izvede prevajanje na ravni projekta, podobno kot CLI. | Da, ko sta `dry_run=false` in `confirm_write=true` |
| `translate_project` | Združljivostni alias za `run_translation`. | Da, ko sta `dry_run=false` in `confirm_write=true` |
| `run_review` | Izvede deterministične preglede. | Ne |
| `get_configuration_status` | Poroča o konfiguriranih ponudnikih LLM in Vision brez razkrivanja skrivnosti. | Ne |
| `list_supported_languages` | Navedite podprte kode ciljnih jezikov. | Ne |
| `get_api_overview` | Opiše razpoložljive MCP delovne tokove in orodja. | Ne |

## Viri

| URI vira | Namen |
| --- | --- |
| `co-op://api` | JSON pregled delovnih tokov in orodij. |
| `co-op://supported-languages` | JSON seznam podprtih kod jezikov. |
| `co-op://configuration` | JSON povzetek razpoložljivosti ponudnikov brez skrivnosti. |

## Pozivi

| Poziv | Namen |
| --- | --- |
| `translate_markdown_document_prompt` | Vodi MCP odjemalca skozi prevajanje vsebine in po potrebi prepis poti. |
| `agent_assisted_markdown_translation_prompt` | Vodi MCP odjemalca skozi prevajanje Markdowna s pomočjo gostiteljskega agenta brez poverilnic ponudnika LLM Co-op Translatorja. |
| `translate_repository_prompt` | Vodi MCP odjemalca skozi prevajanje repozitorija z najprej izvajanjem dry-run. |

## Primeri kopiranja in lepljenja

Prevedite vsebino Markdowna:

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

Prepišite prevedene povezave v Markdownu:

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

Prevedite Markdown z modelom gostiteljskega agenta:

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

Po tem, ko gostiteljski agent prevede vsak vrnjen kos, dokončajte opravilo s celotnim objektom `job`, ki ga vrne `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Predogled prevajanja repozitorija:

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

## Odpravljanje težav

| Težava | Kaj poskusiti |
| --- | --- |
| MCP odjemalec ne najde `co-op-translator-mcp`. | Uporabite absolutno pot do Python izvršljive datoteke in konfiguracijo source checkout `["-m", "co_op_translator.mcp.server"]`. |
| Strežnik je naveden, vendar prevajanje ne uspe. | Pokličite `get_configuration_status` in potrdite, da je ponudnik LLM na voljo. |
| Želite prevajanje Markdowna ali zvezka brez poverilnic ponudnika. | Uporabite `start_markdown_agent_translation` / `finish_markdown_agent_translation` ali ustreznike za zvezke, tako da gostiteljski agent prevede kose. |
| Prevajanje slike ne uspe. | Preverite, ali so nastavljene spremenljivke Azure AI Vision in pokličite `get_configuration_status`. |
| Prevajanje repozitorija ne zapisuje datotek. | Nastavite `dry_run=false` in `confirm_write=true` šele po izrecnem odobrenju uporabnika. |
| Spremembe v konfiguraciji odjemalca se ne prikažejo. | Ponovno zaženite ali znova naložite MCP odjemalca. |

## Varnostne opombe

- Klice orodij MCP nadzoruje model gostiteljske aplikacije, zato je prevajanje repozitorija privzeto v dry-run načinu.
- Celotno prevajanje repozitorija lahko ustvari, posodobi ali odstrani veliko datotek. Pred nastavitvijo `confirm_write=true` zahtevajte izrecno odobritev uporabnika.
- Orodje za preverjanje stanja konfiguracije nikoli ne vrača API ključev, končnih točk ali drugih skrivnih vrednosti.
- Prevajanje slik vrne base64 podatke slike. Velike slike lahko ustvarijo obsežne odzive orodja.
- Orodja s pomočjo agenta vračajo izvorne kose in pozive gostitelju MCP. Uporabljajte jih le za vsebino, ki jo je uporabnik pripravljen poslati modelu gostiteljskega agenta.