# Αναφορά CLI

Co-op Translator εγκαθιστά αυτές τις εντολές γραμμής εντολών:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Οι εντολές `translate`, `evaluate`, `migrate-links` και `co-op-review` προωθούνται μέσω `co_op_translator.__main__`, το οποίο επιλέγει την υλοποίηση της εντολής με βάση το όνομα του καλούμενου script. Ο MCP διακομιστής χρησιμοποιεί απευθείας το `co_op_translator.mcp.server`.

Εάν αποφασίζετε ανάμεσα σε CLI, Python API και MCP, ξεκινήστε με το [Επιλέξτε τη ροή εργασίας σας](workflows.md).

## Διαδικασία Πρώτης Χρήσης CLI

Ξεκινήστε εδώ εάν χρησιμοποιείτε το Co-op Translator από ένα τερματικό:

1. Διαμορφώστε έναν πάροχο LLM όπως περιγράφεται στο [Ρυθμίσεις](configuration.md).
2. Επιλέξτε τον τύπο περιεχομένου που θέλετε να μεταφράσετε.
3. Εκτελέστε πρώτα μια στοχευμένη εντολή, όπως μεταφράσεις μόνο για Markdown.
4. Χρησιμοποιήστε `--dry-run` πριν από μεγάλες αλλαγές στο αποθετήριο.
5. Χρησιμοποιήστε `co-op-review` μετά τη μετάφραση για έλεγχο της δομής και της επικαιρότητας.

| Στόχος | Εντολή για να ξεκινήσετε με |
| --- | --- |
| Μετάφραση εγγράφων Markdown | `translate -l "ko" -md` |
| Μετάφραση σημειωματάριων | `translate -l "ko" -nb` |
| Μετάφραση κειμένου εικόνων | `translate -l "ko" -img` |
| Προεπισκόπηση εργασίας χωρίς εγγραφή αρχείων | `translate -l "ko" -md --dry-run` |
| Ανασκόπηση υπαρχουσών μεταφράσεων | `co-op-review -l "ko"` |
| Ενημέρωση συνδέσμων σημειωματάριων και Markdown | `migrate-links -l "ko" --dry-run` |
| Εκθέστε εργαλεία σε πελάτη MCP | Διαμορφώστε τον [Διακομιστή MCP](mcp.md) αντί να εκτελείτε εντολές CLI απευθείας. |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

```bash
translate -l "ko ja fr"
```

### Συνήθη παραδείγματα

Translate only Markdown:

```bash
translate -l "de" -md
```

Translate only notebooks:

```bash
translate -l "zh-CN" -nb
```

Translate Markdown and images:

```bash
translate -l "pt-BR" -md -img
```

Update existing translations by deleting and recreating them:

```bash
translate -l "ko" -u
```

Run without interactive prompts:

```bash
translate -l "ko ja" -md -y
```

Save logs:

```bash
translate -l "ko" -s
```

### Επιλογές

| Επιλογή | Απαραίτητο | Περιγραφή |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Κώδικες γλωσσών διαχωρισμένοι με κενό, όπως `"es fr de"`, ή `"all"`. |
| `-r`, `--root-dir` | No | Ρίζα έργου. Από προεπιλογή ο τρέχων κατάλογος. |
| `-u`, `--update` | No | Διαγραφή υπάρχουσων μεταφράσεων για τις επιλεγμένες γλώσσες και δημιουργία τους ξανά. |
| `-img`, `--images` | No | Μετάφραση μόνο αρχείων εικόνων. |
| `-md`, `--markdown` | No | Μετάφραση μόνο αρχείων Markdown. |
| `-nb`, `--notebook` | No | Μετάφραση μόνο αρχείων σημειωματάριων Jupyter. |
| `-d`, `--debug` | No | Ενεργοποίηση καταγραφής εντοπισμού σφαλμάτων στην κονσόλα. |
| `-s`, `--save-logs` | No | Αποθήκευση αρχείων καταγραφής επιπέδου DEBUG στο `<root-dir>/logs/`. |
| `-x`, `--fix` | No | Επαναμετάφραση αρχείων Markdown με χαμηλή εμπιστοσύνη βάσει προηγούμενων αποτελεσμάτων αξιολόγησης. |
| `-c`, `--min-confidence` | No | Όριο εμπιστοσύνης για το `--fix`. Προεπιλογή `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Προσθέτει ή καταστέλλει δηλώσεις αποποίησης ευθυνών για μηχανική μετάφραση. Προεπιλογή: ενεργοποιημένο στο CLI. |
| `-f`, `--fast` | No | Αποσυρμένη γρήγορη λειτουργία εικόνας. |
| `-y`, `--yes` | No | Αυτόματη επιβεβαίωση προτροπών, χρήσιμο σε CI. |
| `--repo-url` | No | Το URL του αποθετηρίου που χρησιμοποιείται στη συμβουλή sparse-checkout στον πίνακα γλωσσών του README. |
| `--migrate-language-folders` | No | Μετονομασία παλαιών φακέλων ψευδωνύμων, όπως `cn` ή `tw`, σε κανονικούς φακέλους BCP 47. |
| `--dry-run` | No | Προεπισκόπηση μετανάστευσης φακέλων γλωσσών και εκτιμήσεων μετάφρασης χωρίς εγγραφή αρχείων. |

If no type flag is provided, `translate` processes Markdown, notebooks, and images. Image translation requires Azure AI Vision configuration.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "Πειραματικό"
    `evaluate` is experimental. It can use rule-based and LLM-based quality checks, writes evaluation results into translation metadata, and its scoring model and metadata behavior may change.

```bash
evaluate -l "ko"
```

### Συνήθη παραδείγματα

Use a stricter low-confidence threshold:

```bash
evaluate -l "es" -c 0.8
```

Run rule-based checks only:

```bash
evaluate -l "fr" -f
```

Run LLM-based checks only:

```bash
evaluate -l "ja" -D
```

### Επιλογές

| Επιλογή | Απαραίτητο | Περιγραφή |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Μοναδικός κωδικός γλώσσας προς αξιολόγηση. Οι κωδικοί ψευδωνύμων κανονικοποιούνται. |
| `-r`, `--root-dir` | No | Ρίζα έργου. Από προεπιλογή ο τρέχων κατάλογος. |
| `-c`, `--min-confidence` | No | Όριο που χρησιμοποιείται κατά τη λίστα μεταφράσεων με χαμηλή εμπιστοσύνη. Προεπιλογή `0.7`. |
| `-d`, `--debug` | No | Ενεργοποίηση καταγραφής εντοπισμού σφαλμάτων. |
| `-s`, `--save-logs` | No | Αποθήκευση αρχείων καταγραφής επιπέδου DEBUG στο `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Μόνο αξιολόγηση με κανόνες. |
| `-D`, `--deep` | No | Μόνο αξιολόγηση με LLM. |

By default, `evaluate` uses both rule-based and LLM-based evaluation. Results are written into translation metadata and summarized in the console.

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "Beta"
    `co-op-review` is a beta deterministic review command. It does not call model providers or write files, but its checks and issue output schema may evolve.

```bash
co-op-review -l "ko"
```

### Συνήθη παραδείγματα

Review Korean and Japanese translations from the current directory:

```bash
co-op-review -l "ko ja"
```

Review a specific project root:

```bash
co-op-review -l "fr" -r ./my-course
```

Review only source files changed against a base ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Print GitHub-flavored Markdown output for CI summaries:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Επιλογές

| Επιλογή | Απαραίτητο | Περιγραφή |
| --- | --- | --- |
| `-l`, `--language-code` | No | Κωδικός γλώσσας προς ανασκόπηση. Μπορεί να περαστεί πολλές φορές ή ως τιμή διαχωρισμένη με κενά. Προεπιλογή: όλες οι εντοπισμένες γλώσσες μετάφρασης. |
| `-r`, `--root-dir` | No | Ρίζα έργου. Από προεπιλογή ο τρέχων κατάλογος. |
| `--changed-from` | No | Git ref που χρησιμοποιείται για τον περιορισμό της ανασκόπησης σε αλλάζοντα αρχεία πηγής. |
| `--format` | No | Μορφή εξόδου: `text` ή `github`. Προεπιλογή `text`. |

`co-op-review` currently checks for missing translated files, missing or stale translation metadata, Markdown frontmatter and code fence integrity, invalid translated notebook JSON, and missing local Markdown or image link targets. Missing links are warnings by default; structural and freshness problems fail the command.

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [Διακομιστής MCP](mcp.md) guide for client configuration, tools, resources, and safety notes.

### Επιλογές

| Επιλογή | Απαραίτητο | Περιγραφή |
| --- | --- | --- |
| `--transport` | No | MCP μεταφορικό μέσο: `stdio`, `streamable-http`, ή `sse`. Προεπιλογή `stdio`. |

## migrate-links

Reprocess translated Markdown files and update notebook links so they point to translated notebooks when available.

```bash
migrate-links -l "ko ja"
```

### Συνήθη παραδείγματα

Preview link updates:

```bash
migrate-links -l "ko" --dry-run
```

Process all supported languages without confirmation:

```bash
migrate-links -l "all" -y
```

Only rewrite links when translated notebooks exist:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Επιλογές

| Επιλογή | Απαραίτητο | Περιγραφή |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Κώδικες γλωσσών διαχωρισμένοι με κενό, ή `"all"`. |
| `-r`, `--root-dir` | No | Ρίζα έργου. Από προεπιλογή ο τρέχων κατάλογος. |
| `--image-dir` | No | Κατάλογος μεταφρασμένων εικόνων σχετικός με τη ρίζα. Προεπιλογή `translated_images`. |
| `--dry-run` | No | Εμφάνιση αρχείων που θα άλλαζαν χωρίς να γίνουν ενημερώσεις. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Χρήση αρχικών συνδέσμων notebook όταν λείπουν μεταφρασμένα notebooks. Ενεργό από προεπιλογή. |
| `-d`, `--debug` | No | Ενεργοποίηση καταγραφής εντοπισμού σφαλμάτων. |
| `-s`, `--save-logs` | No | Αποθήκευση αρχείων καταγραφής επιπέδου DEBUG στο `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Αυτόματη επιβεβαίωση προτροπών κατά την επεξεργασία όλων των γλωσσών. |

## Περιβάλλον

All commands require one configured LLM provider:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Ή OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Image translation additionally requires Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Διάταξη εξόδου

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

Translated image output is written under:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Παραδείγματα CLI για Αντιγραφή-Επικόλληση

Translate Markdown into three languages:

```bash
translate -l "ko ja fr" -md
```

Translate notebooks only:

```bash
translate -l "zh-CN" -nb
```

Translate images only:

```bash
translate -l "pt-BR" -img
```

Preview Markdown translation without writing files:

```bash
translate -l "de es" -md --dry-run
```

Repair low-confidence Markdown translations:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Run CI-friendly Markdown translation:

```bash
translate -l "ko ja" -md -y -s
```

Review translated output:

```bash
co-op-review -l "ko ja"
```

Preview link migration:

```bash
migrate-links -l "ko" --dry-run
```