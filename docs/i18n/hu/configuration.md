# Konfiguráció

A Co-op Translatorhez egy nyelvi modell szolgáltató szükséges. A képfordításhoz emellett az Azure AI Vision is szükséges.

A konfiguráció környezeti változókból olvasható. Helyi projektekhez helyezze őket a projekt gyökerében található `.env` fájlba.

Az Azure erőforrás beállításához lásd a [Azure AI beállítása](azure-ai-setup.md).

## Helyi futtatási környezet beállítása

Használjon virtuális környezetet, mielőtt helyben futtatja a CLI-t. A Co-op Translator a Python 3.11–3.14 verziókat támogatja.

A CLI normál használatához telepítse a publikált csomagot a virtuális környezetbe:

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

### Tároló fejlesztése

A tároló fejlesztéséhez ehelyett telepítse a függőségeket a projekt gyökeréből:

```bash
poetry install
poetry run translate --help
```

Miután a CLI elérhetővé vált, konfiguráljon egy nyelvi modell szolgáltatót a `.env` fájlban.

## Szolgáltató kiválasztása

Az eszköz az alábbi sorrendben automatikusan észleli a szolgáltatókat:

1. Azure OpenAI
2. OpenAI
3. Anthropic

A fordításhoz szolgáltatói hitelesítési adatok szükségesek, kivéve az olyan előnézeteket, mint `translate -l "ko" -md --dry-run`. A `migrate-links`, `co-op-review` és `run_review` determinisztikus karbantartási műveletek, és nem igényelnek szolgáltatói hitelesítést.

## Modell kliens backend

A Co-op Translator 0.22.0 verziótól kezdve az Azure OpenAI, OpenAI és Anthropic alapértelmezés szerint a Microsoft Agent Framework-öt használják. Normál használathoz nincs szükség backend beállításra.

A Semantic Kernel ideiglenesen továbbra is elérhető kompatibilitás céljából. Ha kifejezetten ezt szeretné kiválasztani, állítsa be:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

A Semantic Kernel használata elavulásra figyelmeztet. A csomag tervezett módosítása szerint a Semantic Kernel opcionális függőséggé kerül a 0.23.0 verzióban, és az integráció eltávolításra kerül a 0.24.0 verzióban, a kompatibilitási eredmények és a felhasználói visszajelzések függvényében. Az Anthropic megköveteli az `agent-framework`-öt; az `semantic-kernel` kifejezett kiválasztása Anthropic esetén konfigurációs hibát eredményez. Érvénytelen értékek hibát okoznak a szolgáltató által támogatott fordító inicializálása során ahelyett, hogy csendben visszaesnének. Kövesse a bevezetést, és jelentse a blokkoló problémákat a [GitHub hibajegy #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Használja az Azure OpenAI-t, ha modellje az Azure AI Foundry-ban vagy az Azure OpenAI Service-ben van telepítve.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

A kapcsolódási ellenőrzés a végpontot, az API-kulcsot, az API-verziót és a telepítés nevét használja a fordítás megkezdése előtt.

## OpenAI

Használja az OpenAI-t, ha közvetlenül az OpenAI API-t hívja.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` kötelező, mert a fordítónak explicit chat modellre van szüksége az API-hívásokhoz.

Hagyja üresen az `OPENAI_ORG_ID` és `OPENAI_BASE_URL` értékét az alapértelmezett beállításhoz. Adjon meg szervezeti azonosítót csak akkor, ha a fiókjának szüksége van rá, vagy egy alap URL-t csak akkor, ha egyedi végpontot használ. Ne másolja az opcionális beállításokhoz adott helyőrző értékeket.

## Anthropic Claude

Használja az Anthropic-ot, ha közvetlenül a Claude API-t hívja. Hozzon létre egy [Anthropic API kulcsot](https://platform.claude.com/docs/en/get-started), és válasszon egy támogatott [Claude modellazonosítót](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` és `ANTHROPIC_MODEL` kötelezőek. Nem szükséges beállítani a `CO_OP_TRANSLATOR_MODEL_CLIENT`-et; az Agent Framework az alapértelmezett backend.

Az Anthropic API esetén hagyja üresen az `ANTHROPIC_BASE_URL`-t. Állítsa be csak akkor, ha egyedi végpontot használ.

`ANTHROPIC_MAX_TOKENS` alapértelmezett értéke `8192`, ami teret biztosít a token-sűrű írásrendszereknek, például a Meitei Mayeknek. Csökkentse, ha a modellje vagy az Anthropic-kompatibilis végpont ennél alacsonyabbra korlátozza a kimenetet.

## Azure AI Vision

A képfordításhoz Azure AI Vision szükséges, hogy az eszköz kinyerhesse a képekből a szöveget, mielőtt a konfigurált nyelvi modell lefordítaná. Az Anthropic ugyanúgy le tudja fordítani a kinyert szöveget, mint az Azure OpenAI vagy az OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Ha a képfordítást a `-img`, `images=True` opcióval választják, vagy nincs tartalomtípus-szűrő beállítva, az eszköz a fordítás megkezdése előtt érvényesíti a Vision konfigurációt.

## Több hitelesítési készlet

A konfigurációs réteg több hitelesítési készletet támogat úgy, hogy a változókhoz azonos indexű utótagokat fűz:

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

Minden készletnek teljesnek kell lennie. Az egészségügyi ellenőrzés kiválaszt egy működő készletet, mielőtt a fordítás folytatódik.

Az OpenAI és az Anthropic ugyanazt az utótag konvenciót támogatja. Tartsa a hitelesítési készlet minden változóját azonos utótagon, beleértve az olyan opcionális értékeket is, mint az `OPENAI_BASE_URL_1` vagy `ANTHROPIC_BASE_URL_1`.

## Parancsok követelményei

| Parancs vagy API | LLM szükséges | Vision szükséges | Megjegyzések |
| --- | --- | --- | --- |
| `translate -md` | Igen | Nem | Csak Markdown fordítása. |
| `translate -nb` | Igen | Nem | Csak notebookok fordítása. |
| `translate -img` | Igen | Igen | Csak képek fordítása. |
| `translate` típusjelzők nélkül | Igen | Igen | Az alapértelmezett mód tartalmazza a Markdown-t, notebookokat és képeket. |
| `evaluate` | Igen | Nem | LLM alapú értékelést használ, hacsak nincs kiválasztva a `--fast`. |
| `migrate-links` | Nem | Nem | Helyi link migrációt végez szolgáltató hívások nélkül. |
| `co-op-review` | Nem | Nem | Determinisztikus fordítási szerkezet, frissesség, Markdown, notebook és helyi link ellenőrzéseket futtat. |
| `run_translation(markdown=True)` | Igen | Nem | Programozott Markdown fordítás. |
| `run_translation(images=True)` | Igen | Igen | Programozott képfordítás. |
| `run_review(...)` | Nem | Nem | Programozott determinisztikus ellenőrzés. |

## Kimeneti könyvtárak

Alapértelmezett szövegfordítási kimenet:

```text
translations/<language-code>/<source-relative-path>
```

Alapértelmezett lefordított képek kimenete:

```text
translated_images/<language-code>/<source-relative-path>
```

A Python API felülírhatja ezeket a könyvtárakat a `translations_dir` és `image_dir` használatával.