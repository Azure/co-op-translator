# Referință CLI

Co-op Translator instalează aceste puncte de intrare în linia de comandă:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Comenzile `translate`, `evaluate`, `migrate-links` și `co-op-review` sunt direcționate prin `co_op_translator.__main__`, care selectează implementarea comenzii pe baza numelui scriptului apelat. Serverul MCP folosește direct `co_op_translator.mcp.server`.

Dacă trebuie să alegeți între CLI, API-ul Python și MCP, începeți cu [Alegeți-vă fluxul de lucru](workflows.md).

## Ieșire în consolă

Terminalele interactive folosesc formatare Rich pentru antetul comenzii, progres și rezumate. Ieșirea în CI și ieșirile non-interactive trec automat la text simplu.

Setați `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` pentru a forța ieșirea simplă, sau `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` pentru a forța ieșirea Rich. Setați `CO_OP_TRANSLATOR_NO_PROGRESS=1` pentru a păstra rezumatele în timp ce suprimați barele de progres live.

Folosiți `translate --json-events progress.ndjson` când un alt sistem are nevoie
de progres lizibil de către mașină. CLI continuă să afișeze ieșirea destinată utilizatorilor, în timp ce
fișierul NDJSON primește evenimente versiunate `co-op.translation.event.v1` cu
câmpuri stabile precum `type`, `stage_key`, `completed`, `total` și
`current_path`.

## Fluxul CLI la prima utilizare

Începeți aici dacă folosiți Co-op Translator dintr-un terminal:

1. Configurați un furnizor LLM așa cum este descris în [Configurație](configuration.md).
2. Alegeți tipul de conținut pe care doriți să îl traduceți.
3. Rulați mai întâi o comandă focalizată, de exemplu traducerea doar a Markdown-ului.
4. Folosiți `--dry-run` înainte de schimbări majore în repository.
5. Folosiți `co-op-review` după traducere pentru a verifica structura și actualitatea.

| Scop | Comanda de început |
| --- | --- |
| Traduceți documente Markdown | `translate -l "ko" -md` |
| Traduceți notebook-uri | `translate -l "ko" -nb` |
| Traduceți textul din imagini | `translate -l "ko" -img` |
| Previzualizați munca fără a scrie fișiere | `translate -l "ko" -md --dry-run` |
| Revizuiți traducerile existente | `co-op-review -l "ko"` |
| Actualizați legăturile notebook și Markdown | `migrate-links -l "ko" --dry-run` |
| Expuneți instrumentele către un client MCP | Configurați [Serverul MCP](mcp.md) în loc să rulați comenzile CLI direct. |

## translate

Traduceți fișiere Markdown, notebook-uri și text din imagini în una sau mai multe limbi țintă.

```bash
translate -l "ko ja fr"
```

### Exemple comune

Traduceți doar Markdown:

```bash
translate -l "de" -md
```

Traduceți doar notebook-uri:

```bash
translate -l "zh-CN" -nb
```

Traduceți Markdown și imagini:

```bash
translate -l "pt-BR" -md -img
```

Actualizați traducerile existente ștergându-le și recreându-le:

```bash
translate -l "ko" -u
```

Rulați fără solicitări interactive:

```bash
translate -l "ko ja" -md -y
```

Salvați jurnalele:

```bash
translate -l "ko" -s
```

Scrieți evenimente structurate de progres:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Opțiuni

| Opțiune | Obligatoriu | Descriere |
| --- | --- | --- |
| `-l`, `--language-codes` | Da | Coduri de limbă separate prin spațiu, cum ar fi `"es fr de"`, sau `"all"`. |
| `-r`, `--root-dir` | Nu | Rădăcina proiectului. Implicit, directorul curent. |
| `-u`, `--update` | Nu | Șterge traducerile existente pentru limbile selectate și le recreează. |
| `-img`, `--images` | Nu | Traduce numai fișiere imagine. |
| `-md`, `--markdown` | Nu | Traduce numai fișiere Markdown. |
| `-nb`, `--notebook` | Nu | Traduce numai fișiere Jupyter notebook. |
| `-d`, `--debug` | Nu | Activează logarea de depanare în consolă. |
| `-s`, `--save-logs` | Nu | Salvează jurnale de nivel DEBUG în `<root-dir>/logs/`. |
| `--json-events` | Nu | Scrie evenimente de progres ale traducerii lizibile de mașină ca NDJSON. |
| `-x`, `--fix` | Nu | Retraduce fișiere Markdown cu încredere scăzută pe baza rezultatelor evaluărilor anterioare. |
| `-c`, `--min-confidence` | Nu | Prag de încredere pentru `--fix`. Implicit `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Nu | Adaugă sau suprimă avertismentele privind traducerea automată. În CLI este activat implicit. |
| `-f`, `--fast` | Nu | Modul rapid pentru imagini, depreciat. |
| `-y`, `--yes` | Nu | Confirmă automat solicitările, util în CI. |
| `--repo-url` | Nu | URL-ul repository folosit în recomandarea privind sparse-checkout din tabelul limbilor din README. |
| `--migrate-language-folders` | Nu | Redenumește foldere alias învechite, precum `cn` sau `tw`, în foldere canonice BCP 47. |
| `--dry-run` | Nu | Previzualizează migrarea folderelor de limbă și estimările traducerii fără a scrie fișiere. |

Dacă nu este furnizat niciun flag de tip, `translate` procesează Markdown, notebook-uri și imagini. Traducerea imaginilor necesită configurare Azure AI Vision.

## evaluate

Evaluează calitatea traducerii Markdown pentru o limbă.

!!! warning "Experimental"
    `evaluate` este experimental. Poate folosi verificări ale calității bazate pe reguli și pe LLM, scrie rezultatele evaluării în metadatele traducerii, iar modelul de scor și comportamentul metadatelor se pot schimba.

```bash
evaluate -l "ko"
```

### Exemple comune

Folosiți un prag mai strict pentru încrederea scăzută:

```bash
evaluate -l "es" -c 0.8
```

Rulați doar verificări bazate pe reguli:

```bash
evaluate -l "fr" -f
```

Rulați doar verificări bazate pe LLM:

```bash
evaluate -l "ja" -D
```

### Opțiuni

| Opțiune | Obligatoriu | Descriere |
| --- | --- | --- |
| `-l`, `--language-code` | Da | Un singur cod de limbă de evaluat. Codurile alias sunt normalizate. |
| `-r`, `--root-dir` | Nu | Rădăcina proiectului. Implicit, directorul curent. |
| `-c`, `--min-confidence` | Nu | Prag folosit când se listează traducerile cu încredere scăzută. Implicit `0.7`. |
| `-d`, `--debug` | Nu | Activează logarea de debug. |
| `-s`, `--save-logs` | Nu | Salvează jurnale de nivel DEBUG în `<root-dir>/logs/`. |
| `-f`, `--fast` | Nu | Numai evaluare bazată pe reguli. |
| `-D`, `--deep` | Nu | Numai evaluare bazată pe LLM. |

Implicit, `evaluate` folosește atât evaluare bazată pe reguli, cât și pe LLM. Rezultatele sunt scrise în metadatele traducerii și rezumate în consolă.

## co-op-review

Rulați verificări deterministe de întreținere a traducerii fără credențiale API.

!!! note "Beta"
    `co-op-review` este o comandă beta de revizuire deterministă. Nu apelează furnizori de modele și nu scrie fișiere, dar verificările și schema de ieșire a problemelor se pot modifica.

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

Revizuiți doar README după o traducere efectuată doar asupra README-ului:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` ignoră alte documente și README-urile imbricate. Eșuează dacă rădăcina
`README.md` lipsește. Combinat cu `--changed-from`, revizuiește doar README-ul
când fișierul sursă s-a schimbat. Traducerea doar a README lasă README-ul sursă
neschimbat, inclusiv orice marcatoare de secțiune partajată.

Revizuiți doar fișierele sursă care s-au schimbat față de o referință de bază:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Tipăriți ieșire Markdown în stil GitHub pentru rezumatele CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Opțiuni

| Opțiune | Obligatoriu | Descriere |
| --- | --- | --- |
| `-l`, `--language-code` | Nu | Codul de limbă de revizuit. Poate fi trecut de mai multe ori sau ca o valoare separată prin spațiu. Implicit, toate limbile de traducere descoperite. |
| `-r`, `--root-dir` | Nu | Rădăcina proiectului. Implicit, directorul curent. |
| `--changed-from` | Nu | Ref Git folosit pentru a limita revizuirea la fișierele sursă modificate. |
| `--readme-only` | Nu | Revizuiește doar traducerea fișierului `README.md` din rădăcină. |
| `--format` | Nu | Formatul de ieșire: `text` sau `github`. Implicit `text`. |

`co-op-review` în prezent verifică fișierele traduse lipsă, metadatele traducerii lipsă sau învechite, integritatea frontmatter-ului Markdown și a delimitatorilor de cod, JSON-ul notebook tradus invalid și țintele de legături locale Markdown sau imagine lipsă. Legăturile lipsă sunt avertismente implicit; problemele de structură și de actualitate fac comanda să eșueze.

## co-op-translator-mcp

Rulați serverul MCP Co-op Translator pentru agenți, editori și clienți compatibili MCP.

```bash
co-op-translator-mcp
```

Transportul implicit este `stdio`. Consultați ghidul [Serverul MCP](mcp.md) pentru configurarea clientului, unelte, resurse și note de siguranță.

### Opțiuni

| Opțiune | Obligatoriu | Descriere |
| --- | --- | --- |
| `--transport` | Nu | Transport MCP: `stdio`, `streamable-http` sau `sse`. Implicit `stdio`. |

## migrate-links

Reprocesează fișierele Markdown traduse și actualizează legăturile către notebook-uri astfel încât să indice notebook-urile traduse când sunt disponibile.

```bash
migrate-links -l "ko ja"
```

### Exemple comune

Previzualizați actualizările legăturilor:

```bash
migrate-links -l "ko" --dry-run
```

Procesează toate limbile suportate fără confirmare:

```bash
migrate-links -l "all" -y
```

Rescrie legăturile doar când există notebook-uri traduse:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Opțiuni

| Opțiune | Obligatoriu | Descriere |
| --- | --- | --- |
| `-l`, `--language-codes` | Da | Coduri de limbă separate prin spațiu, sau `"all"`. |
| `-r`, `--root-dir` | Nu | Rădăcina proiectului. Implicit, directorul curent. |
| `--image-dir` | Nu | Directorul imaginilor traduse relativ la rădăcină. Implicit `translated_images`. |
| `--dry-run` | Nu | Afișează fișierele care s-ar schimba fără a scrie actualizări. |
| `--fallback-to-original`, `--no-fallback-to-original` | Nu | Folosește legăturile originale către notebook atunci când notebook-urile traduse lipsesc. Activat implicit. |
| `-d`, `--debug` | Nu | Activează logarea de debug. |
| `-s`, `--save-logs` | Nu | Salvează jurnale de nivel DEBUG în `<root-dir>/logs/`. |
| `-y`, `--yes` | Nu | Confirmă automat solicitările când se procesează toate limbile. |

## Mediu

Când o comandă necesită credențiale de furnizor, configurați unul dintre aceste seturi de furnizori. `translate --dry-run` și `co-op-review` nu necesită credențiale de furnizor:

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

# Sau Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Traducerea imaginilor necesită, în plus, Azure AI Vision:

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

De exemplu, traducerea lui `README.md` și `docs/setup.md` în coreeană produce:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Exemple CLI de copiat și lipit

Traduceți Markdown în trei limbi:

```bash
translate -l "ko ja fr" -md
```

Traduceți doar notebook-uri:

```bash
translate -l "zh-CN" -nb
```

Traduceți doar imagini:

```bash
translate -l "pt-BR" -img
```

Previzualizați traducerea Markdown fără a scrie fișiere:

```bash
translate -l "de es" -md --dry-run
```

Remediați traducerile Markdown cu încredere scăzută:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Rulați traducerea Markdown compatibilă cu CI:

```bash
translate -l "ko ja" -md -y -s
```

Revizuiți ieșirea tradusă:

```bash
co-op-review -l "ko ja"
```

Previzualizați migrarea legăturilor:

```bash
migrate-links -l "ko" --dry-run
```