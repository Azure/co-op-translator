# Konfiguracija

Co-op Translator zahtijeva jednog pružatelja modela jezika. Za prevođenje slika dodatno je potreban Azure AI Vision.

Konfiguracija se čita iz varijabli okruženja. Za lokalne projekte, smjestite ih u datoteku `.env` u korijenu projekta.

Za postavljanje Azure resursa, pogledajte [Postavljanje Azure AI](azure-ai-setup.md).

## Lokalno postavljanje runtimea

Prije pokretanja CLI-a lokalno koristite virtualno okruženje. Co-op Translator podržava Python 3.11 do 3.14.

Za normalnu upotrebu CLI-a instalirajte objavljeni paket unutar virtualnog okruženja:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### Razvoj repozitorija

Za razvoj repozitorija, umjesto toga instalirajte ovisnosti iz korijena projekta:

```bash
poetry install
poetry run translate --help
```

Nakon što je CLI dostupan, konfigurirajte jednog pružatelja modela jezika u `.env`.

## Odabir pružatelja

Alat automatski otkriva pružatelje u sljedećem redoslijedu:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Za prevođenje su potrebne vjerodajnice pružatelja, osim za preglede kao što je `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review`, i `run_review` su determinističke operacije održavanja i ne zahtijevaju vjerodajnice pružatelja.

## Back-end klijenta modela

Počevši s Co-op Translator 0.22.0, Azure OpenAI, OpenAI i Anthropic zadano koriste Microsoft Agent Framework. Nije potrebno postaviti backend za normalnu upotrebu.

Semantic Kernel ostaje privremeno dostupan radi kompatibilnosti. Da biste ga izričito odabrali, postavite:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Korištenje Semantic Kernel-a generira upozorenje o zastarijevanju. Planirano je da paket premjesti Semantic Kernel u opcionalnu ovisnost u 0.23.0 i ukloni integraciju u 0.24.0, ovisno o rezultatima kompatibilnosti i povratnim informacijama korisnika. Anthropic zahtijeva `agent-framework`; izričito odabiranje `semantic-kernel` s Anthropicom rezultira pogreškom u konfiguraciji. Neispravne vrijednosti izazvat će pogrešku tijekom inicijalizacije prevoditelja koji se oslanja na pružatelja umjesto da se tiho prebace na zadanu opciju. Pratite uvođenje i prijavite blokade u [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Koristite Azure OpenAI kada je vaš model raspoređen u Azure AI Foundry ili Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provjera povezanosti koristi endpoint, API ključ, verziju API-ja i ime deploymenta prije nego što prijevod započne.

## OpenAI

Koristite OpenAI kada pozivate OpenAI API izravno.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` je obavezan jer prevoditelj zahtijeva eksplicitni chat model za pozive API-ja.

Ostavite `OPENAI_ORG_ID` i `OPENAI_BASE_URL` nepostavljenima za zadano postavljanje. Dodajte ID organizacije samo ako vaš račun to zahtijeva, ili osnovni URL samo kada koristite prilagođeni endpoint. Ne kopirajte zamjenske (placeholder) vrijednosti za opcionalne postavke.

## Anthropic Claude

Koristite Anthropic kada pozivate Claude API izravno. Kreirajte [Anthropic API ključ](https://platform.claude.com/docs/en/get-started) i odaberite podržani [ID Claude modela](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` i `ANTHROPIC_MODEL` su obavezni. Ne morate postaviti `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework je zadani backend.

Ostavite `ANTHROPIC_BASE_URL` nepostavljen za Anthropic API. Postavite ga samo kada koristite prilagođeni endpoint.

`ANTHROPIC_MAX_TOKENS` ima zadanu vrijednost `8192`, što ostavlja prostora za jezike bogate tokenima poput Meitei Mayek. Smanjite ga ako vaš model ili Anthropic-kompatibilni endpoint ograničava izlaz ispod toga.

## Azure AI Vision

Prevođenje slika zahtijeva Azure AI Vision kako bi alat mogao izdvojiti tekst iz slika prije nego što ga konfigurirani model jezika prevede. Anthropic može prevesti izdvojeni tekst isto kao Azure OpenAI ili OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Ako je prevođenje slika odabrano s `-img`, `images=True` ili bez filtra tipa sadržaja, alat provjerava konfiguraciju Vision prije početka prijevoda.

## Višestruki skupovi vjerodajnica

Sloj konfiguracije podržava više skupova vjerodajnica dodavanjem sufiksa istog indeksa varijablama:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

Svaki skup mora biti potpun. Provjera zdravlja (health check) odabire radni skup prije nego što prijevod nastavi.

OpenAI i Anthropic podržavaju istu konvenciju sufiksa. Držite svaku varijablu u skupu vjerodajnica na istom sufiksu, uključujući opcionalne vrijednosti poput `OPENAI_BASE_URL_1` ili `ANTHROPIC_BASE_URL_1`.

## Zahtjevi naredbi

| Naredba ili API | Potreban LLM | Potreban Vision | Napomene |
| --- | --- | --- | --- |
| `translate -md` | Da | Ne | Prevodi samo Markdown. |
| `translate -nb` | Da | Ne | Prevodi samo bilježnice. |
| `translate -img` | Da | Da | Prevodi samo slike. |
| `translate` bez zastavica tipa | Da | Da | Zadani način uključuje Markdown, bilježnice i slike. |
| `evaluate` | Da | Ne | Koristi LLM evaluaciju osim ako nije odabrano `--fast`. |
| `migrate-links` | Ne | Ne | Izvodi lokalnu migraciju linkova bez poziva pružatelja. |
| `co-op-review` | Ne | Ne | Pokreće determinističke provjere strukture prijevoda, svježine, Markdowna, bilježnica i lokalnih poveznica. |
| `run_translation(markdown=True)` | Da | Ne | Programski prijevod Markdowna. |
| `run_translation(images=True)` | Da | Da | Programsko prevođenje slika. |
| `run_review(...)` | Ne | Ne | Programska deterministička revizija. |

## Izlazni direktoriji

Zadani izlaz za tekstualne prijevode:

```text
translations/<language-code>/<source-relative-path>
```

Zadani izlaz za prevedene slike:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API može nadjačati ove direktorije pomoću `translations_dir` i `image_dir`.