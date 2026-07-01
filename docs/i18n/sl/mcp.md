# MCP strežnik

Co-op Translator vključuje strežnik Model Context Protocol (MCP) za agente, urejevalnike in odjemalce, združljive z MCP.

Za privzeto lokalno nastavitev uporabniki ne poganjajo ločenega strežnika ročno. Konfigurirajo svoj MCP odjemalec, in odjemalec samodejno zažene `co-op-translator-mcp` prek `stdio`, ko potrebuje orodja Co-op Translator.

Če se odločate med vmesnikom CLI, Python API in MCP, začnite z [Izberite svoj potek dela](workflows.md).

Uporabite MCP, kadar mora agent ali urejevalnik neposredno klicati Co-op Translator:

| Cilj uporabnika | Orodja MCP |
| --- | --- |
| Prevesti en Markdown dokument, zvezek (notebook) ali sliko | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Prevesti vsebino Markdowna ali zvezka z modelom gostiteljskega agenta | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Prepišite prevedene povezave v Markdownu ali zvezku po izbiri izhodne poti | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prevesti celoten repozitorij, podobno kot CLI | `run_translation`, `translate_project` |
| Pregledati prevedeno izhodno vsebino brez poverilnic LLM | `run_review` |
| Pregledati zmožnosti in stanje okolja | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP strežnik ovija isti javni Python API, kot je dokumentiran v [Python API](api.md). Orodja, podprta s strani ponudnikov, uporabljajo iste konfigurirane ponudnike kot CLI in Python API. Orodja z asistenco agenta pripravijo koščke za prevod s strani gostiteljskega MCP agenta, nato pa Co-op Translator uporabi za rekonstruiranje končnega Markdowna ali zvezka.

## Korak 1: Namestite in konfigurirajte Co-op Translator

Namestite Co-op Translator v Python okolju, ki ga bo uporabljal vaš MCP odjemalec:

```bash
pip install co-op-translator
```

Za lokalni razvoj iz tega repozitorija namestite paket v urejevalnem načinu:

```bash
pip install -e .
```

Izberite način prevajanja, ki ga bo uporabljal vaš MCP odjemalec:

| Način | Uporabite za | Poverilnice |
| --- | --- | --- |
| Podprto s ponudniki | Co-op Translator kliče `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, ali `run_translation`. | Prevajanje Markdowna in zvezkov zahteva Azure OpenAI ali OpenAI. Prevajanje slik zahteva tudi Azure AI Vision. |
| Asistirano z agentom | Gostiteljski MCP agent prevede koščke, ki jih vrne `start_markdown_agent_translation` ali `start_notebook_agent_translation`. | Za koščke Markdowna ali zvezka niso potrebna poverilnica ponudnikov LLM za Co-op Translator. Prevajanje slik še ni podprto v načinu asistence agenta. |

Če začnete s prevajanjem Markdowna ali zvezkov znotraj agenta, kot sta Codex ali Claude Code, začnite z načinom z asistenco agenta. Uporabite način z voljo ponudnikov, ko želite, da Co-op Translator sam kliče vaše konfigurirane ponudnike, ko prevajate slike ali ko izvajate prevajanje na ravni repozitorija, kot pri CLI.

Konfigurirajte poverilnice ponudnikov samo za delovne tokove z podporo ponudnikov:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Za prevajanje slik z podporo ponudnikov je dodatno potrebno:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Način z asistenco agenta trenutno pokriva Markdown in Markdown celice v zvezkih. Prevajanje slik še vedno uporablja cevovod slik, podprt s ponudniki, in zahteva Azure AI Vision za OCR in upoštevanje postavitve.

## Korak 2: Konfigurirajte vaš MCP odjemalec

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

Konfiguracija izvorne kopije v sistemu Windows:

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

Konfiguracija izvorne kopije na macOS ali Linuxu:

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

Po spremembi konfiguracije MCP odjemalca ga ponovno zaženite ali naložite, da lahko odkrije nov strežnik.

## Korak 3: Preverite strežnik v odjemalcu

Prosite MCP odjemalca, naj izpiše razpoložljiva orodja, ali pa najprej pokličite enega od pomočnikov samo za branje:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Koristni začetni pregledi:

| Orodje | Kaj preveriti |
| --- | --- |
| `get_api_overview` | Potrdi, da je strežnik dosegljiv in prikaže razpoložljive delovne tokove. |
| `list_supported_languages` | Potrdi, da je mogoče naložiti pakirane podatke o jezikih. |
| `get_configuration_status` | Potrdi razpoložljivost ponudnikov LLM in Vision, ne da bi razkrival skrivne vrednosti. |

## Korak 4: Izberite potek dela

### Prevajanje posameznih datotek ali dokumentov

Uporabite orodja z podporo ponudnikov, kadar ima MCP odjemalec že vsebino dokumenta ali pot do slike in naj Co-op Translator pokliče konfigurirane ponudnike za prevajanje.

Za Markdown:

1. Pokličite `translate_markdown_content` z `document`, `language_code` in po potrebi `source_path`.
2. Če bo prevedeni rezultat zapisan v izhodno postavitev Co-op Translator, pokličite `rewrite_markdown_paths`.
3. Naj odjemalec zapiše ali vrne končno `content`.

Za zvezke:

1. Pokličite `translate_notebook_content` z JSON zvezka in `language_code`.
2. Pokličite `rewrite_notebook_paths`, če je treba prevedene povezave v zvezku prilagoditi ciljni poti.
3. Zapišite ali vrnite končni JSON zvezka.

Za slike:

1. Pokličite `translate_image_content` z `image_path`, `language_code` in izbirno `root_dir` ali `fast_mode`.
2. Preberite vrnjeni `data_base64` in `mime_type`.
3. Če je podan `output_path`, je prevedena slika tudi shranjena na to pot.

Orodja za vsebino ne izvajajo odkrivanja projektov, posodobitev metapodatkov, opozoril ali samodejnega prepisovanja poti. Če želite, da gostiteljski agent prevede koščke Markdowna ali zvezka brez poverilnic ponudnika LLM Co-op Translator, uporabite spodnji potek dela z asistenco agenta.

### Prevajanje z modelom gostiteljskega agenta

Uporabite orodja z asistenco agenta, kadar želite, da gostiteljski MCP agent, na primer pomočnik za programiranje, ustvari prevedeno besedilo namesto konfiguriranja Azure OpenAI ali OpenAI za Co-op Translator.

V klepetalnem MCP odjemalcu običajno ne potrebujete sami pisati orodijskega JSON-a. Prosite agenta, naj uporabi potek dela z asistenco agenta:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Za zvezke uporabite isti vzorec:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Če vaš MCP odjemalec podpira strežniške pozive, uporabite `agent_assisted_markdown_translation_prompt`, da odjemalec naloži ista navodila poteka dela.

Za Markdown:

1. Pokličite `start_markdown_agent_translation` z `document`, `language_code` in po potrebi `source_path`.
2. Prevedite vsak vrnjen košček v gostiteljskem agentu tako, da sledite `prompt` koščka.
3. Pokličite `finish_markdown_agent_translation` z izvirnim `job` in prevedenimi koščki z uporabo `chunk_id` in `translated_text`.
4. Če bo vsebina zapisana na prevedeno ciljno pot, pokličite `rewrite_markdown_paths`.

Za zvezke:

1. Pokličite `start_notebook_agent_translation` z JSON zvezka in `language_code`.
2. Prevedite vsak vrnjen košček v gostiteljskem agentu.
3. Pokličite `finish_notebook_agent_translation` z izvirnim `job` in prevedenimi koščki.
4. Pokličite `rewrite_notebook_paths`, če je treba prevedene povezave v zvezku prilagoditi ciljni poti.

Orodja z asistenco agenta ne kličejo Azure OpenAI ali OpenAI iz Co-op Translator. Gostiteljski agent je odgovoren za prevajanje vrnjenih koščkov. Co-op Translator obvladuje razbijanje Markdowna na koščke, ohranjanje nadomestnih mest, rekonstrukcijo frontmatter, zamenjavo celic v zvezku in normalizacijo po prevajanju.

### Prevajanje celotnega repozitorija

Uporabite `run_translation`, ko uporabnik želi, da se Co-op Translator obnaša kot `translate` CLI.

Prevajanje repozitorija privzeto uporablja `dry_run=true`, tako da lahko agent pregleda obseg pred spremembami datotek:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Da se dovolijo zapisi, mora kličujoči nastaviti `dry_run=false` in `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` je izpostavljen kot skladen vzdevek (alias) za `run_translation`.

### Pregled prevedenega izhoda

Uporabite `run_review` za deterministične preglede, ki ne zahtevajo poverilnic LLM ali Vision:

!!! note "Beta"
    MCP izpostavlja beta API `run_review`. Je varen za delovne tokove pregleda samo za branje, vendar se lahko preverjanja pregleda in sheme težav razvijajo.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Rezultat vključuje zajet izhod besedila in strukturiran povzetek pregleda, če je na voljo.

## Ročno zaganjanje strežnika

Ročni zagoni so namenjeni predvsem razhroščevanju ali transportom, ki se obnašajo kot dolgotrajni strežniki.

Razhroščite privzeti stdio strežnik:

```bash
co-op-translator-mcp
```

Zaženite iz izvorne kopije:

```bash
python -m co_op_translator.mcp.server
```

Zaženite dolgotrajni HTTP ali SSE strežnik:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Za lokalne integracije urejevalnikov in agentov raje uporabite konfiguracijo `stdio`, ki jo upravlja odjemalec, iz Koraka 2.

## Orodja

| Orodje | Namen | Zapisuje datoteke |
| --- | --- | --- |
| `translate_markdown_content` | Prevede niz Markdown. | Ne |
| `translate_notebook_content` | Prevede Markdown celice v JSON zvezku. | Ne |
| `translate_image_content` | Prevede besedilo na eni sliki in vrne base64 podatke slike. | Izbirno, samo ko je podan `output_path` |
| `start_markdown_agent_translation` | Pripravi koščke Markdowna, da jih gostiteljski agent prevede brez LLM poverilnic Co-op Translator. | Ne |
| `finish_markdown_agent_translation` | Rekonstruira Markdown iz koščkov, prevedenih s strani gostiteljskega agenta. | Ne |
| `start_notebook_agent_translation` | Pripravi koščke Markdown celic zvezka za prevod s strani gostiteljskega agenta. | Ne |
| `finish_notebook_agent_translation` | Rekonstruira JSON zvezka iz koščkov, prevedenih s strani gostiteljskega agenta. | Ne |
| `rewrite_markdown_paths` | Prepiše poti v telesu Markdowna in frontmatter za prevedeni cilj. | Ne |
| `rewrite_notebook_paths` | Prepiše poti znotraj Markdown celic zvezka. | Ne |
| `run_translation` | Zažene prevajanje na ravni projekta, podobno kot CLI. | Da, ko `dry_run=false` in `confirm_write=true` |
| `translate_project` | Združljivostni vzdevek za `run_translation`. | Da, ko `dry_run=false` in `confirm_write=true` |
| `run_review` | Izvede deterministične preglede. | Ne |
| `get_configuration_status` | Poročilo o konfiguriranih ponudnikih LLM in Vision, ne da bi razkrival skrivnosti. | Ne |
| `list_supported_languages` | Navedite podprte ciljne jezikovne kode. | Ne |
| `get_api_overview` | Opisati razpoložljive MCP poteke dela in orodja. | Ne |

## Viri

| URI vira | Namen |
| --- | --- |
| `co-op://api` | JSON pregled potekov dela in orodij. |
| `co-op://supported-languages` | JSON seznam podprtih jezikovnih kod. |
| `co-op://configuration` | JSON povzetek razpoložljivosti ponudnikov brez skrivnosti. |

## Pozivi

| Poziv | Namen |
| --- | --- |
| `translate_markdown_document_prompt` | Vodnik za MCP odjemalca pri prevajanju vsebine in po potrebi prepisovanju poti. |
| `agent_assisted_markdown_translation_prompt` | Vodnik za MCP odjemalca pri prevajanju Markdowna s strani gostiteljskega agenta brez poverilnic ponudnika LLM Co-op Translator. |
| `translate_repository_prompt` | Vodnik za MCP odjemalca pri prevajanju repozitorija z najprej poskusnim zagonom (dry-run). |

## Primeri za prilepanje

Prevajanje vsebine Markdown:

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

Prevedi Markdown z modelom gostiteljskega agenta:

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

Ko gostiteljski agent prevede vsak vrnjen košček, dokončajte nalogo s celotnim objektom `job`, ki ga vrne `start_markdown_agent_translation`:

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
| MCP odjemalec ne najde `co-op-translator-mcp`. | Uporabite absolutno pot do Python izvršljive datoteke in konfiguracijo izvorne kopije `["-m", "co_op_translator.mcp.server"]`. |
| Strežnik je na seznamu, vendar prevajanje ne uspe. | Pokličite `get_configuration_status` in potrdite, da je ponudnik LLM na voljo. |
| Želite prevajanje Markdowna ali zvezka brez ključev Azure OpenAI/OpenAI. | Uporabite `start_markdown_agent_translation` / `finish_markdown_agent_translation` ali ustreznike za zvezke, da gostiteljski agent prevede koščke. |
| Prevajanje slik ne uspe. | Potrdite, da so nastavljene spremenljivke Azure AI Vision in pokličite `get_configuration_status`. |
| Prevajanje repozitorija ne zapisuje datotek. | Nastavite `dry_run=false` in `confirm_write=true` šele po izrecnem odobrenju uporabnika. |
| Spremembe v konfiguraciji odjemalca se ne prikažejo. | Ponovno zaženite ali znova naložite MCP odjemalca. |

## Varnostne opombe

- Klici orodij MCP so nadzorovani z modelom gostiteljske aplikacije, zato je prevajanje repozitorija privzeto v načinu dry-run.
- Celovito prevajanje repozitorija lahko ustvari, posodobi ali odstrani veliko datotek. Pred nastavljenjem `confirm_write=true` zahtevajte izrecno odobritev uporabnika.
- Orodje za stanje konfiguracije nikoli ne vrača API ključev, končnih točk ali drugih skrivnih vrednosti.
- Prevajanje slik vrača base64 podatke slike. Velike slike lahko povzročijo velike odzive orodij.
- Orodja z asistenco agenta vračajo izvorne koščke in pozive gostitelju MCP. Uporabljajte jih le z vsebino, za katero je uporabnik pripravljen, da jo pošlje temu modelu gostiteljskega agenta.