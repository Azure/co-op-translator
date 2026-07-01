# Referință CLI

Co-op Translator instalează următoarele puncte de intrare în linia de comandă:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Comenzile `translate`, `evaluate`, `migrate-links` și `co-op-review` sunt direcționate prin `co_op_translator.__main__`, care selectează implementarea comenzii în funcție de numele scriptului apelat. Serverul MCP folosește direct `co_op_translator.mcp.server`.

Dacă decideți între CLI, API Python și MCP, începeți cu [Alegeți fluxul de lucru](workflows.md).

## Fluxul CLI pentru prima utilizare

Porniți de aici dacă folosiți Co-op Translator dintr-un terminal:

1. Configurați un furnizor LLM așa cum este descris în [Configuration](configuration.md).
2. Alegeți tipul de conținut pe care doriți să îl traduceți.
3. Rulați mai întâi o comandă focalizată, cum ar fi traducerea doar a Markdown-ului.
4. Folosiți `--dry-run` înainte de modificări mari ale depozitului.
5. Folosiți `co-op-review` după traducere pentru a verifica structura și actualitatea.

| Scop | Comanda pentru a începe |
| --- | --- |
| Traduce documente Markdown | `translate -l "ko" -md` |
| Traduce notebook-uri | `translate -l "ko" -nb` |
| Traduce text din imagini | `translate -l "ko" -img` |
| Previzualizați lucrările fără a scrie fișiere | `translate -l "ko" -md --dry-run` |
| Revizuiți traducerile existente | `co-op-review -l "ko"` |
| Actualizați link-urile din notebook-uri și Markdown | `migrate-links -l "ko" --dry-run` |
| Expuneți instrumentele către un client MCP | Configurați [Serverul MCP](mcp.md) în loc să rulați comenzile CLI direct. |

## translate

Traduce fișiere Markdown, notebook-uri și text din imagini în una sau mai multe limbi țintă.

```bash
translate -l "ko ja fr"
```

### Exemple comune

Traduce doar Markdown:

```bash
translate -l "de" -md
```

Traduce doar notebook-uri:

```bash
translate -l "zh-CN" -nb
```

Traduce Markdown și imagini:

```bash
translate -l "pt-BR" -md -img
```

Actualizează traducerile existente prin ștergerea și recrearea lor:

```bash
translate -l "ko" -u
```

Rulează fără prompturi interactive:

```bash
translate -l "ko ja" -md -y
```

Salvează jurnalele:

```bash
translate -l "ko" -s
```

### Opțiuni

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Da | Coduri de limbă separate prin spațiu, de exemplu `"es fr de"`, sau `"all"`. |
| `-r`, `--root-dir` | Nu | Rădăcina proiectului. Implicit este directorul curent. |
| `-u`, `--update` | Nu | Șterge traducerile existente pentru limbile selectate și le recreează. |
| `-img`, `--images` | Nu | Traduce doar fișierele de imagine. |
| `-md`, `--markdown` | Nu | Traduce doar fișierele Markdown. |
| `-nb`, `--notebook` | Nu | Traduce doar fișierele Jupyter notebook. |
| `-d`, `--debug` | Nu | Activează logarea de debug în consolă. |
| `-s`, `--save-logs` | Nu | Salvează jurnalele la nivel DEBUG sub `<root-dir>/logs/`. |
| `-x`, `--fix` | Nu | Retraduce fișiere Markdown cu încredere scăzută pe baza rezultatelor anterioare de evaluare. |
| `-c`, `--min-confidence` | Nu | Prag de încredere pentru `--fix`. Implicit `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Nu | Adaugă sau suprimă avertismentele privind traducerea automată. Implicit activate în CLI. |
| `-f`, `--fast` | Nu | Mod rapid pentru imagini, depreciat. |
| `-y`, `--yes` | Nu | Confirmă automat prompturile, util în CI. |
| `--repo-url` | Nu | URL-ul depozitului folosit în consilierea de sparse-checkout din tabelul limbilor din README. |
| `--migrate-language-folders` | Nu | Redenumește folderele alias vechi, cum ar fi `cn` sau `tw`, în foldere canonice BCP 47. |
| `--dry-run` | Nu | Previziualizează migrarea folderelor de limbă și estimările de traducere fără a scrie fișiere. |

Dacă nu este furnizat niciun flag de tip, `translate` procesează Markdown, notebook-uri și imagini. Traducerea imaginilor necesită configurarea Azure AI Vision.

## evaluate

Evaluează calitatea traducerilor Markdown pentru o limbă.

!!! warning "Experimental"
    `evaluate` este experimental. Poate folosi verificări bazate pe reguli și pe LLM, scrie rezultatele evaluării în metadatele traducerii, iar modelul său de scor și comportamentul metadata se pot schimba.

```bash
evaluate -l "ko"
```

### Exemple comune

Folosește un prag de încredere mai strict pentru conținut cu încredere scăzută:

```bash
evaluate -l "es" -c 0.8
```

Rulează doar verificări bazate pe reguli:

```bash
evaluate -l "fr" -f
```

Rulează doar verificări bazate pe LLM:

```bash
evaluate -l "ja" -D
```

### Opțiuni

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Da | Un singur cod de limbă de evaluat. Codurile alias sunt normalizate. |
| `-r`, `--root-dir` | Nu | Rădăcina proiectului. Implicit este directorul curent. |
| `-c`, `--min-confidence` | Nu | Prag folosit la listarea traducerilor cu încredere scăzută. Implicit `0.7`. |
| `-d`, `--debug` | Nu | Activează logarea de debug. |
| `-s`, `--save-logs` | Nu | Salvează jurnalele la nivel DEBUG sub `<root-dir>/logs/`. |
| `-f`, `--fast` | Nu | Doar evaluare bazată pe reguli. |
| `-D`, `--deep` | Nu | Doar evaluare bazată pe LLM. |

Implicit, `evaluate` folosește atât evaluarea bazată pe reguli, cât și pe LLM. Rezultatele sunt scrise în metadatele traducerii și rezumate în consolă.

## co-op-review

Rulează verificări deterministe de întreținere a traducerilor fără credențiale API.

!!! note "Beta"
    `co-op-review` este o comandă de revizuire deterministă în stadiu beta. Nu apelează furnizori de modele și nu scrie fișiere, dar verificările și schema de ieșire a problemelor pot evolua.

```bash
co-op-review -l "ko"
```

### Exemple comune

Revizuiți traducerile în coreeană și japoneză din directorul curent:

```bash
co-op-review -l "ko ja"
```

Revizuiți o rădăcină de proiect specifică:

```bash
co-op-review -l "fr" -r ./my-course
```

Revizuiți doar fișierele sursă modificate față de un ref de bază:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Printați ieșire în Markdown cu stil GitHub pentru rezumate CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Opțiuni

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Nu | Cod de limbă de revizuit. Poate fi trecut de mai multe ori sau ca o valoare separată prin spațiu. Implicit, toate limbile de traducere descoperite. |
| `-r`, `--root-dir` | Nu | Rădăcina proiectului. Implicit este directorul curent. |
| `--changed-from` | Nu | Ref Git folosit pentru a limita revizuirea la fișierele sursă modificate. |
| `--format` | Nu | Formatul de ieșire: `text` sau `github`. Implicit `text`. |

`co-op-review` verifică în prezent fișiere traduse lipsă, metadate de traducere lipsă sau depășite, integritatea frontmatter-ului Markdown și a blocurilor de cod, JSON invalid în notebook-urile traduse și ținte locale lipsă pentru linkuri Markdown sau imagini. Linkurile lipsă sunt avertismente implicit; problemele de structură și actualitate fac ca comanda să eșueze.

## co-op-translator-mcp

Rulează serverul MCP Co-op Translator pentru agenți, editori și clienți compatibili MCP.

```bash
co-op-translator-mcp
```

Transportul implicit este `stdio`. Consultați ghidul [Serverul MCP](mcp.md) pentru configurarea clientului, instrumente, resurse și note de securitate.

### Opțiuni

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | Nu | Transport MCP: `stdio`, `streamable-http`, sau `sse`. Implicit `stdio`. |

## migrate-links

Reprocesează fișierele Markdown traduse și actualizează link-urile din notebook-uri astfel încât să indice către notebook-urile traduse atunci când sunt disponibile.

```bash
migrate-links -l "ko ja"
```

### Exemple comune

Previzualizați actualizările de linkuri:

```bash
migrate-links -l "ko" --dry-run
```

Procesează toate limbile suportate fără confirmare:

```bash
migrate-links -l "all" -y
```

Rescrie link-urile doar atunci când există notebook-uri traduse:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Opțiuni

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Da | Coduri de limbă separate prin spațiu, sau `"all"`. |
| `-r`, `--root-dir` | Nu | Rădăcina proiectului. Implicit este directorul curent. |
| `--image-dir` | Nu | Directorul imaginilor traduse relativ la root. Implicit `translated_images`. |
| `--dry-run` | Nu | Afișează fișierele care s-ar schimba fără a scrie actualizări. |
| `--fallback-to-original`, `--no-fallback-to-original` | Nu | Folosește link-urile notebook originale când lipsesc notebook-urile traduse. Activat implicit. |
| `-d`, `--debug` | Nu | Activează logarea de debug. |
| `-s`, `--save-logs` | Nu | Salvează jurnalele la nivel DEBUG sub `<root-dir>/logs/`. |
| `-y`, `--yes` | Nu | Confirmă automat prompturile când se procesează toate limbile. |

## Mediu

Toate comenzile necesită un furnizor LLM configurat:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Sau OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Traducerea imaginilor necesită suplimentar Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Structura ieșirii

Traducerile text sunt scrise sub:

```text
translations/<language-code>/<original-path>
```

Ieșirea imaginilor traduse este scrisă sub:

```text
translated_images/<language-code>/<original-path>
```

De exemplu, traducerea fișierelor `README.md` și `docs/setup.md` în coreeană produce:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Exemple CLI de copiere și lipire

Traduce Markdown în trei limbi:

```bash
translate -l "ko ja fr" -md
```

Traduce doar notebook-uri:

```bash
translate -l "zh-CN" -nb
```

Traduce doar imagini:

```bash
translate -l "pt-BR" -img
```

Previzualizează traducerea Markdown fără a scrie fișiere:

```bash
translate -l "de es" -md --dry-run
```

Repară traducerile Markdown cu încredere scăzută:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Rulează traducerea Markdown potrivită pentru CI:

```bash
translate -l "ko ja" -md -y -s
```

Revizuiți rezultatul tradus:

```bash
co-op-review -l "ko ja"
```

Previzualizați migrarea linkurilor:

```bash
migrate-links -l "ko" --dry-run
```