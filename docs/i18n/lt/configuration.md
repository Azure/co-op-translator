# Konfigūracija

Co-op Translator reikalauja vieno kalbos modelio tiekėjo. Vaizdų vertimui papildomai reikalinga Azure AI Vision.

Konfigūracija skaitoma iš aplinkos kintamųjų. Vietiniams projektams įdėkite juos į `.env` failą projekto šaknyje.

Dėl Azure išteklių parengimo žr. [Azure AI nustatymas](azure-ai-setup.md).

## Vietinės vykdymo aplinkos nustatymas

Prieš paleisdami CLI vietoje, naudokite virtualią aplinką. Co-op Translator palaiko Python 3.11–3.14.

Įprastam CLI naudojimui įdiekite paskelbtą paketą virtualioje aplinkoje:

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

### Repozitorijos vystymas

Vystant repozitoriją, vietoj to įdiekite priklausomybes iš projekto šaknies:

```bash
poetry install
poetry run translate --help
```

Kai CLI bus pasiekiamas, sukonfigūruokite vieną kalbos modelio tiekėją faile `.env`.

## Tiekėjo pasirinkimas

Įrankis automatiškai aptinka tiekėjus šia tvarka:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Vertimui reikalingos tiekėjo prieigos duomenys, išskyrus peržiūras, pvz. `translate -l "ko" -md --dry-run`. Komandos `migrate-links`, `co-op-review` ir `run_review` yra deterministinės priežiūros operacijos ir nepareikalauja tiekėjo prieigos duomenų.

## Modelio kliento backend

Nuo Co-op Translator 0.22.0, Azure OpenAI, OpenAI ir Anthropic pagal nutylėjimą naudoja Microsoft Agent Framework. Paprastam naudojimui backend nustatymas nėra reikalingas.

Semantic Kernel laikinai išlieka prieinamas dėl suderinamumo. Norėdami jį pasirinkti aiškiai, nustatykite:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Naudojant Semantic Kernel išmetamas pasenimo įspėjimas. Planuojama perkelti Semantic Kernel į pasirenkamą priklausomybę versijoje 0.23.0 ir pašalinti integraciją 0.24.0, priklausomai nuo suderinamumo rezultatų ir naudotojų atsiliepimų. Anthropic reikalauja `agent-framework`; aiškus `semantic-kernel` pasirinkimas su Anthropic baigiasi konfigūracijos klaida. Neteisingos reikšmės sužlugdys vertėjo inicializaciją, pagrįstą tiekėju, o ne tyliai persijungs. Sekite diegimą ir praneškite apie blokuojančias problemas [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Naudokite Azure OpenAI, kai jūsų modelis diegiamas Azure AI Foundry arba Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Prieš pradėdama vertimą, ryšio tikrinimas naudoja endpoint'ą, API raktą, API versiją ir diegimo pavadinimą.

## OpenAI

Naudokite OpenAI, kai kreipiatės į OpenAI API tiesiogiai.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` yra privalomas, nes vertėjui reikalingas aiškus pokalbių modelis API užklausoms.

Palikite `OPENAI_ORG_ID` ir `OPENAI_BASE_URL` nenustatytus numatytajam nustatymui. Pridėkite organizacijos ID tik jei jūsų paskyra jo reikalauja, arba bazinį URL tik naudojant pasirinktą endpoint'ą. Nesikopijuokite vietos užpildų reikšmių opcioniniams nustatymams.

## Anthropic Claude

Naudokite Anthropic, kai kreipiatės į Claude API tiesiogiai. Sukurkite [Anthropic API raktą](https://platform.claude.com/docs/en/get-started) ir pasirinkite palaikomą [Claude modelio ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` ir `ANTHROPIC_MODEL` yra privalomi. Nereikia nustatyti `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework yra numatytasis backend.

Palikite `ANTHROPIC_BASE_URL` nenustatytą Anthropic API. Nustatykite jį tik naudojant pasirinktą endpoint'ą.

`ANTHROPIC_MAX_TOKENS` numatytoji reikšmė yra `8192`, kas palieka vietos tokenų tankioms abėcėlėms, pvz., Meitei Mayek. Sumažinkite ją, jei jūsų modelis arba su Anthropic suderinamas endpoint'as riboja išvestį žemiau to.

## Azure AI Vision

Vaizdų vertimui reikalinga Azure AI Vision, kad įrankis galėtų išgauti tekstą iš vaizdų prieš tai, kai nustatytas kalbos modelis jį išvers. Anthropic gali išversti išgautą tekstą taip pat kaip Azure OpenAI ar OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Jei vaizdų vertimas pasirinktas su `-img`, `images=True` arba nėra content-type filtro, įrankis prieš pradėdamas vertimą patikrina Vision konfigūraciją.

## Keli kredencialų rinkiniai

Konfigūracijos sluoksnis palaiko kelis kredencialų rinkinius pridedant kintamiesiems tą patį sufiksą (indeksą):

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

Kiekvienas rinkinys turi būti pilnas. Būklės patikra parenka veikiančią rinkinį prieš pradedant vertimą.

OpenAI ir Anthropic palaiko tą pačią sufikso konvenciją. Laikykite kiekvieną kintamąjį kredencialų rinkinyje su tuo pačiu sufiksu, įskaitant opcionalias reikšmes, tokias kaip `OPENAI_BASE_URL_1` ar `ANTHROPIC_BASE_URL_1`.

## Komandų reikalavimai

| Komanda arba API | Reikia LLM | Reikia Vision | Pastabos |
| --- | --- | --- | --- |
| `translate -md` | Taip | Ne | Verčia tik Markdown. |
| `translate -nb` | Taip | Ne | Verčia tik užrašų knygutes. |
| `translate -img` | Taip | Taip | Verčia tik vaizdus. |
| `translate` su jokiomis tipo žymėmis | Taip | Taip | Numatytoji būsena apima Markdown, užrašų knygutes ir vaizdus. |
| `evaluate` | Taip | Ne | Naudoja LLM vertinimą, nebent pasirinktas `--fast`. |
| `migrate-links` | Ne | Ne | Atlieka vietinę nuorodų migraciją be tiekėjo užklausų. |
| `co-op-review` | Ne | Ne | Atlieka deterministinius vertimo struktūros, aktualumo, Markdown, užrašų knygutės ir vietinių nuorodų patikrinimus. |
| `run_translation(markdown=True)` | Taip | Ne | Programinis Markdown vertimas. |
| `run_translation(images=True)` | Taip | Taip | Programinis vaizdų vertimas. |
| `run_review(...)` | Ne | Ne | Programinė deterministinė peržiūra. |

## Išvesties katalogai

Numatytoji teksto vertimo išvestis:

```text
translations/<language-code>/<source-relative-path>
```

Numatytoji išverstų vaizdų išvestis:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API gali perrašyti šiuos katalogus su `translations_dir` ir `image_dir`.