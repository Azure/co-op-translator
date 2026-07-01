# Konfiguracija

Co-op Translator zahtijeva jednog pružatelja modela jezika. Prevođenje slika dodatno zahtijeva Azure AI Vision.

Konfiguracija se čita iz varijabli okoline. Za lokalne projekte, stavite ih u datoteku `.env` u korijenu projekta.

Za postavljanje Azure resursa, pogledajte [Postavljanje Azure AI](azure-ai-setup.md).

## Lokalno postavljanje runtimea

Prije pokretanja CLI alata lokalno koristite virtualno okruženje. Co-op Translator podržava Python 3.10 do 3.12.

Za uobičajenu upotrebu CLI-a, instalirajte objavljeni paket unutar virtualnog okruženja:

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

Za razvoj repozitorija, umjesto toga instalirajte ovisnosti iz korijena projekta:

```bash
poetry install
poetry run translate --help
```

Nakon što je CLI dostupan, konfigurirajte jednog pružatelja modela jezika u `.env`.

## Odabir pružatelja

Alat automatski otkriva pružatelje u ovom redoslijedu:

1. Azure OpenAI
2. OpenAI

Ako nijedan pružatelj nije konfiguriran, `translate`, `evaluate`, `migrate-links`, i `run_translation` ne uspijevaju tijekom provjera konfiguracije. `co-op-review` i `run_review` su determinističke provjere održavanja i ne zahtijevaju vjerodajnice pružatelja.

## Azure OpenAI

Koristite Azure OpenAI kada je vaš model postavljen u Azure AI Foundry ili Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provjera povezanosti koristi endpoint, API ključ, verziju API-ja i naziv implementacije prije početka prijevoda.

## OpenAI

Koristite OpenAI kada izravno pozivate OpenAI API.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # neobavezno
OPENAI_BASE_URL="..."        # neobavezno
```

`OPENAI_CHAT_MODEL_ID` je obavezan jer prevoditelj treba eksplicitan chat model za pozive API-ja.

## Azure AI Vision

Prevođenje slika zahtijeva Azure AI Vision kako bi alat mogao izdvojiti tekst iz slika prije nego što ga prevede.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Ako je prevođenje slika odabrano s `-img`, `images=True` ili bez filtera tipa sadržaja, alat provjerava konfiguraciju Vision prije nego prijevod započne.

## Višestruki skupovi vjerodajnica

Sloj konfiguracije podržava višestruke skupove vjerodajnica dodavanjem sufiksa s istim indeksom varijablama:

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

Svaki skup mora biti kompletan. Provjera ispravnosti odabire radni skup prije nego prijevod nastavi.

## Zahtjevi naredbi

| Naredba ili API | Potreban LLM | Potreban Vision | Napomene |
| --- | --- | --- | --- |
| `translate -md` | Da | Ne | Prevodi samo Markdown. |
| `translate -nb` | Da | Ne | Prevodi samo bilježnice. |
| `translate -img` | Da | Da | Prevodi samo slike. |
| `translate` bez tipova zastavica | Da | Da | Zadani način uključuje Markdown, bilježnice i slike. |
| `evaluate` | Da | Ne | Koristi evaluaciju LLM-a osim ako nije odabran `--fast`. |
| `migrate-links` | Da | Ne | Izvodi migraciju poveznica, ali i dalje pokreće zajedničke provjere konfiguracije. |
| `co-op-review` | Ne | Ne | Pokreće determinističke provjere strukture prijevoda, svježine, Markdowna, bilježnica i lokalnih poveznica. |
| `run_translation(markdown=True)` | Da | Ne | Programatski prijevod Markdowna. |
| `run_translation(images=True)` | Da | Da | Programatsko prevođenje slika. |
| `run_review(...)` | Ne | Ne | Programatski deterministički pregled. |

## Izlazni direktoriji

Zadani izlaz za tekstualne prijevode:

```text
translations/<language-code>/<source-relative-path>
```

Zadani izlaz prevedenih slika:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API može nadjačati ove direktorije pomoću `translations_dir` i `image_dir`.