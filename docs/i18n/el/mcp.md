# Διακομιστής MCP

Το Co-op Translator περιλαμβάνει έναν διακομιστή Model Context Protocol για πράκτορες, συντάκτες και πελάτες συμβατούς με MCP.

Για την προεπιλεγμένη τοπική ρύθμιση, οι χρήστες δεν χρειάζεται να διατηρούν ξεχωριστό διακομιστή χειροκίνητα. Διαμορφώνουν τον πελάτη MCP τους, και ο πελάτης ξεκινά αυτόματα την `co-op-translator-mcp` μέσω `stdio` όταν χρειάζεται τα εργαλεία του Co-op Translator.

Αν αποφασίζετε ανάμεσα σε CLI, Python API και MCP, ξεκινήστε με [Επιλέξτε τη ροή εργασίας σας](workflows.md).

Χρησιμοποιήστε MCP όταν ένας πράκτορας ή συντάκτης πρέπει να καλεί απευθείας το Co-op Translator:

| Στόχος χρήστη | Εργαλεία MCP |
| --- | --- |
| Μεταφράστε ένα έγγραφο Markdown, σημειωματάριο, ή εικόνα | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Μεταφράστε περιεχόμενο Markdown ή notebook με το μοντέλο του host agent | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Επανεγγράψτε μεταφρασμένους συνδέσμους Markdown ή notebook αφού επιλέξετε τη διαδρομή εξόδου | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Μεταφράστε ολόκληρο αποθετήριο όπως το CLI | `run_translation`, `translate_project` |
| Επανεξέταση του μεταφρασμένου αποτελέσματος χωρίς διαπιστευτήρια LLM | `run_review` |
| Επιθεώρηση δυνατοτήτων και κατάστασης περιβάλλοντος | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Ο διακομιστής MCP τυλίγει την ίδια δημόσια Python API που τεκμηριώνεται στο [Python API](api.md). Τα εργαλεία που υποστηρίζονται από παρόχους χρησιμοποιούν τους ίδιους διαμορφωμένους παρόχους όπως το CLI και το Python API. Τα εργαλεία με βοήθεια πράκτορα προετοιμάζουν κομμάτια για τον host agent του MCP να τα μεταφράσει και έπειτα χρησιμοποιούν το Co-op Translator για να ανασυνθέσουν το τελικό Markdown ή notebook.

## Βήμα 1: Εγκαταστήστε και διαμορφώστε το Co-op Translator

Εγκαταστήστε το Co-op Translator στο περιβάλλον Python που θα χρησιμοποιήσει ο πελάτης MCP σας:

```bash
pip install co-op-translator
```

Για τοπική ανάπτυξη από αυτό το αποθετήριο, εγκαταστήστε το πακέτο σε editable mode:

```bash
pip install -e .
```

Επιλέξτε τη λειτουργία μετάφρασης που θα χρησιμοποιήσει ο πελάτης MCP σας:

| Λειτουργία | Χρησιμοποιείται για | Διαπιστευτήρια |
| --- | --- | --- |
| Provider-backed | Το Co-op Translator καλεί `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, ή `run_translation`. | Η μετάφραση απαιτεί Azure OpenAI, OpenAI, ή Anthropic. Η μετάφραση εικόνων απαιτεί επίσης Azure AI Vision. |
| Agent-assisted | Ο host agent του MCP μεταφράζει κομμάτια που επιστρέφονται από `start_markdown_agent_translation` ή `start_notebook_agent_translation`. | Δεν απαιτούνται διαπιστευτήρια παρόχου LLM του Co-op Translator για κομμάτια Markdown ή notebook. Η μετάφραση εικόνων δεν καλύπτεται ακόμη από τη λειτουργία agent-assisted. |

Εάν ξεκινάτε με μετάφραση Markdown ή notebook μέσα σε έναν agent όπως το Codex ή Claude Code, ξεκινήστε με τη λειτουργία agent-assisted. Χρησιμοποιήστε τη λειτουργία provider-backed όταν θέλετε το ίδιο το Co-op Translator να καλεί τους διαμορφωμένους παρόχους σας, όταν μεταφράζετε εικόνες, ή όταν εκτελείτε μετάφραση σε επίπεδο αποθετηρίου όπως το CLI.

Διαμορφώστε έναν πάροχο για ροές εργασίας provider-backed:

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

# Ή Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Επιπλέον, η μετάφραση εικόνων με provider-backed χρειάζεται:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Η λειτουργία agent-assisted αυτή τη στιγμή καλύπτει Markdown και τα Markdown κελιά των notebook. Η μετάφραση εικόνων εξακολουθεί να χρησιμοποιεί την pipeline εικόνων που βασίζεται σε παρόχους και απαιτεί Azure AI Vision για OCR και απόδοση με γνώση διάταξης.

## Βήμα 2: Διαμορφώστε τον πελάτη MCP σας

Για την κανονική τοπική ρύθμιση `stdio`, προσθέστε το Co-op Translator στη διαμόρφωση του πελάτη MCP σας. Ο πελάτης θα ξεκινά και θα σταματά τη διαδικασία αυτόματα.

Διαμόρφωση για εγκατεστημένο πακέτο:

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

Διαμόρφωση source checkout στα Windows:

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

Διαμόρφωση source checkout σε macOS ή Linux:

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

Μετά την αλλαγή της διαμόρφωσης του πελάτη MCP, επανεκκινήστε ή φορτώστε ξανά τον πελάτη ώστε να μπορεί να εντοπίσει τον νέο διακομιστή.

## Βήμα 3: Επαληθεύστε τον διακομιστή στον πελάτη

Ζητήστε από τον πελάτη MCP να απαριθμήσει τα διαθέσιμα εργαλεία, ή καλέστε πρώτα ένα από τα βοηθητικά εργαλεία μόνο για ανάγνωση:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Χρήσιμοι αρχικοί έλεγχοι:

| Εργαλείο | Τι να ελέγξετε |
| --- | --- |
| `get_api_overview` | Επιβεβαιώνει ότι ο διακομιστής είναι προσβάσιμος και δείχνει τις διαθέσιμες ροές εργασίας. |
| `list_supported_languages` | Επιβεβαιώνει ότι τα πακέτα γλωσσικών δεδομένων μπορούν να φορτωθούν. |
| `get_configuration_status` | Επιβεβαιώνει τη διαθεσιμότητα παρόχων LLM και Vision χωρίς την αποκάλυψη μυστικών. |

## Βήμα 4: Επιλέξτε μια ροή εργασίας

### Μεταφράστε μεμονωμένα αρχεία ή έγγραφα

Χρησιμοποιήστε εργαλεία content provider-backed όταν ο πελάτης MCP έχει ήδη το περιεχόμενο εγγράφου ή τη διαδρομή εικόνας και το Co-op Translator πρέπει να καλεί τους διαμορφωμένους παρόχους μετάφρασης.

Για Markdown:

1. Καλέστε `translate_markdown_content` με `document`, `language_code`, και προαιρετικά `source_path`.
2. Εάν το μεταφρασμένο αποτέλεσμα θα γραφτεί σε ένα layout εξόδου του Co-op Translator, καλέστε `rewrite_markdown_paths`.
3. Επιτρέψτε στον πελάτη να γράψει ή να επιστρέψει το τελικό `content`.

Για notebooks:

1. Καλέστε `translate_notebook_content` με το JSON του notebook και `language_code`.
2. Καλέστε `rewrite_notebook_paths` εάν οι μεταφρασμένοι σύνδεσμοι του notebook χρειάζεται να προσαρμοστούν για μια διαδρομή προορισμού.
3. Γράψτε ή επιστρέψτε το τελικό JSON του notebook.

Για εικόνες:

1. Καλέστε `translate_image_content` με `image_path`, `language_code`, και προαιρετικά `root_dir` ή `fast_mode`.
2. Διαβάστε τα επιστρεφόμενα `data_base64` και `mime_type`.
3. Εάν παρέχεται `output_path`, η μεταφρασμένη εικόνα αποθηκεύεται επίσης σε αυτή τη διαδρομή.

Τα εργαλεία περιεχομένου δεν εκτελούν ανακάλυψη έργου, ενημερώσεις μεταδεδομένων, δηλώσεις αποποίησης ή αυτόματη αναδιαγραφή διαδρομών. Εάν θέλετε ο host agent να μεταφράσει κομμάτια Markdown ή notebook χωρίς διαπιστευτήρια παρόχου LLM του Co-op Translator, χρησιμοποιήστε την agent-assisted ροή εργασίας παρακάτω.

### Μεταφράστε με το μοντέλο του host agent

Χρησιμοποιήστε εργαλεία agent-assisted όταν θέλετε ο host agent του MCP, όπως ένας βοηθός προγραμματισμού, να παράγει το μεταφρασμένο κείμενο αντί να διαμορφώσετε έναν πάροχο LLM για το Co-op Translator.

Σε έναν πελάτη MCP βασισμένο σε συνομιλία, συνήθως δεν χρειάζεται να γράψετε εσείς το JSON του εργαλείου. Ζητήστε από τον agent να χρησιμοποιήσει την agent-assisted ροή εργασίας:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Για notebooks, χρησιμοποιήστε το ίδιο μοτίβο:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Εάν ο πελάτης MCP σας υποστηρίζει server prompts, χρησιμοποιήστε `agent_assisted_markdown_translation_prompt` ώστε ο πελάτης να φορτώσει τις ίδιες οδηγίες ροής εργασίας.

Για Markdown:

1. Καλέστε `start_markdown_agent_translation` με `document`, `language_code`, και προαιρετικά `source_path`.
2. Μεταφράστε κάθε επιστρεφόμενο κομμάτι μέσα στον host agent ακολουθώντας το `prompt` του κομματιού.
3. Καλέστε `finish_markdown_agent_translation` με το αρχικό `job` και τα μεταφρασμένα κομμάτια χρησιμοποιώντας `chunk_id` και `translated_text`.
4. Εάν το περιεχόμενο θα γραφτεί σε μεταφρασμένη διαδρομή προορισμού, καλέστε `rewrite_markdown_paths`.

Για notebooks:

1. Καλέστε `start_notebook_agent_translation` με το JSON του notebook και `language_code`.
2. Μεταφράστε κάθε επιστρεφόμενο κομμάτι στον host agent.
3. Καλέστε `finish_notebook_agent_translation` με το αρχικό `job` και τα μεταφρασμένα κομμάτια.
4. Καλέστε `rewrite_notebook_paths` εάν οι μεταφρασμένοι σύνδεσμοι του notebook χρειάζονται προσαρμογή της διαδρομής προορισμού.

Τα εργαλεία agent-assisted δεν καλούν τον διαμορφωμένο πάροχο LLM από το Co-op Translator. Ο host agent είναι υπεύθυνος για τη μετάφραση των επιστρεφόμενων κομματιών. Το Co-op Translator χειρίζεται το σπάσιμο σε κομμάτια Markdown, τη διατήρηση των placeholder, την ανακατασκευή του frontmatter, την αντικατάσταση κελιών notebook και την κανονικοποίηση μετά τη μετάφραση.

### Μεταφράστε ολόκληρο αποθετήριο

Χρησιμοποιήστε `run_translation` όταν ο χρήστης θέλει το Co-op Translator να συμπεριφέρεται όπως το CLI `translate`.

Η μετάφραση αποθετηρίου έχει προεπιλεγμένη τιμή `dry_run=true` ώστε ένας agent να μπορεί να ελέγξει το εύρος πριν τις αλλαγές αρχείων:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Το αποτέλεσμα `run_translation` περιλαμβάνει έναν πίνακα `events` με εκδοσιοποιημένα
`co-op.translation.event.v1` γεγονότα προόδου. Οι πελάτες MCP θα πρέπει να χρησιμοποιούν πεδία όπως
όπως `type`, `stage_key`, `completed`, `total`, και `current_path` αντί να
αναλύουν το καταγεγραμμένο κείμενο της κονσόλας. Δώστε το `json_events_path` για να γράψετε επίσης αυτά τα γεγονότα
σε ένα αρχείο NDJSON.

Για να επιτραπεί η εγγραφή, ο καλών πρέπει να ρυθμίσει τόσο `dry_run=false` όσο και `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` παρέχεται ως alias συμβατότητας για το `run_translation`.

### Επανεξέταση του μεταφρασμένου αποτελέσματος

Χρησιμοποιήστε `run_review` για ντετερμινιστικούς ελέγχους που δεν απαιτούν διαπιστευτήρια LLM ή Vision:

!!! note "Beta"
    Το MCP εκθέτει το beta API `run_review`. Είναι ασφαλές για ροές εργασίας επανεξέτασης μόνο για ανάγνωση, αλλά οι έλεγχοι επανεξέτασης και τα σχήματα θεμάτων ενδέχεται να εξελιχθούν.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Το αποτέλεσμα περιλαμβάνει καταγεγραμμένο κείμενο εξόδου και μια δομημένη περίληψη επανεξέτασης όταν είναι διαθέσιμη.

## Χειροκίνητες Εκτελέσεις Διακομιστή

Οι χειροκίνητες εκτελέσεις προορίζονται κυρίως για αποσφαλμάτωση ή για μεταφορές που συμπεριφέρονται σαν μακροχρόνιοι διακομιστές.

Εντοπισμός σφαλμάτων του προεπιλεγμένου stdio διακομιστή:

```bash
co-op-translator-mcp
```

Εκτέλεση από source checkout:

```bash
python -m co_op_translator.mcp.server
```

Εκτέλεση μακροχρόνιου HTTP ή SSE διακομιστή:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Για τοπικές ενσωματώσεις editor και agent, προτιμήστε τη διαμόρφωση `stdio` που διαχειρίζεται ο πελάτης στο Βήμα 2.

## Εργαλεία

| Εργαλείο | Σκοπός | Γράφει αρχεία |
| --- | --- | --- |
| `translate_markdown_content` | Μεταφράζει μια συμβολοσειρά Markdown. | Όχι |
| `translate_notebook_content` | Μεταφράζει κελία Markdown στο JSON του notebook. | Όχι |
| `translate_image_content` | Μεταφράζει κείμενο σε μια εικόνα και επιστρέφει δεδομένα εικόνας σε base64. | Προαιρετικό, μόνο όταν παρέχεται `output_path` |
| `start_markdown_agent_translation` | Προετοιμάζει κομμάτια Markdown για να τα μεταφράσει ο host agent χωρίς διαπιστευτήρια παρόχου LLM του Co-op Translator. | Όχι |
| `finish_markdown_agent_translation` | Ανασυνθέτει Markdown από τα μεταφρασμένα κομμάτια του host agent. | Όχι |
| `start_notebook_agent_translation` | Προετοιμάζει κομμάτια markdown-κελιών notebook για να τα μεταφράσει ο host agent. | Όχι |
| `finish_notebook_agent_translation` | Ανασυνθέτει το JSON του notebook από τα μεταφρασμένα κομμάτια του host agent. | Όχι |
| `rewrite_markdown_paths` | Επανεγγράφει το σώμα Markdown και τις διαδρομές frontmatter για έναν μεταφρασμένο προορισμό. | Όχι |
| `rewrite_notebook_paths` | Επανεγγράφει διαδρομές μέσα σε κελία Markdown του notebook. | Όχι |
| `run_translation` | Εκτελεί μετάφραση σε επίπεδο έργου όπως το CLI. | Ναι όταν `dry_run=false` και `confirm_write=true` |
| `translate_project` | Alias συμβατότητας για το `run_translation`. | Ναι όταν `dry_run=false` και `confirm_write=true` |
| `run_review` | Εκτελεί ντετερμινιστικούς ελέγχους επανεξέτασης. | Όχι |
| `get_configuration_status` | Αναφέρει τους διαμορφωμένους παρόχους LLM και Vision χωρίς να αποκαλύπτει μυστικά. | Όχι |
| `list_supported_languages` | Λίστα με κωδικούς υποστηριζόμενων γλωσσών στόχου. | Όχι |
| `get_api_overview` | Περιγράφει τις διαθέσιμες ροές εργασίας και εργαλεία MCP. | Όχι |

## Πόροι

| URI Πόρου | Σκοπός |
| --- | --- |
| `co-op://api` | JSON επισκόπηση των ροών εργασίας και εργαλείων. |
| `co-op://supported-languages` | JSON λίστα με υποστηριζόμενους κωδικούς γλωσσών. |
| `co-op://configuration` | JSON περίληψη διαθεσιμότητας παρόχων χωρίς μυστικά. |

## Προτροπές

| Προτροπή | Σκοπός |
| --- | --- |
| `translate_markdown_document_prompt` | Καθοδηγεί έναν πελάτη MCP στη μετάφραση περιεχομένου καθώς και στην προαιρετική επανεγγραφή διαδρομών. |
| `agent_assisted_markdown_translation_prompt` | Καθοδηγεί έναν πελάτη MCP στη μετάφραση Markdown με host-agent χωρίς διαπιστευτήρια παρόχου LLM του Co-op Translator. |
| `translate_repository_prompt` | Καθοδηγεί έναν πελάτη MCP στη μετάφραση αποθετηρίου με πρώτη προεπισκόπηση (dry-run). |

## Παραδείγματα Αντιγραφής-Επικόλλησης

Μεταφράστε περιεχόμενο Markdown:

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

Επανεγγράψτε μεταφρασμένους συνδέσμους Markdown:

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

Μεταφράστε Markdown με το μοντέλο host agent:

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

Αφού ο host agent μεταφράσει κάθε επιστρεφόμενο κομμάτι, ολοκληρώστε τη δουλειά με το πλήρες αντικείμενο `job` που επιστρέφεται από το `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Προεπισκόπηση μετάφρασης αποθετηρίου:

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

## Αντιμετώπιση προβλημάτων

| Πρόβλημα | Τι να δοκιμάσετε |
| --- | --- |
| Ο πελάτης MCP δεν μπορεί να βρει `co-op-translator-mcp`. | Χρησιμοποιήστε την απόλυτη διαδρομή εκτελέσιμου Python και τη διαμόρφωση source checkout `["-m", "co_op_translator.mcp.server"]`. |
| Ο διακομιστής εμφανίζεται αλλά η μετάφραση αποτυγχάνει. | Καλέστε `get_configuration_status` και επιβεβαιώστε ότι υπάρχει διαθέσιμος πάροχος LLM. |
| Θέλετε μετάφραση Markdown ή notebook χωρίς διαπιστευτήρια παρόχου. | Χρησιμοποιήστε `start_markdown_agent_translation` / `finish_markdown_agent_translation` ή τα αντίστοιχα για notebook ώστε ο host agent να μεταφράσει τα κομμάτια. |
| Η μετάφραση εικόνας αποτυγχάνει. | Επιβεβαιώστε ότι οι μεταβλητές Azure AI Vision έχουν οριστεί και καλέστε `get_configuration_status`. |
| Η μετάφραση αποθετηρίου δεν γράφει αρχεία. | Ορίστε `dry_run=false` και `confirm_write=true` μόνο μετά από ρητή έγκριση του χρήστη. |
| Οι αλλαγές στη διαμόρφωση του πελάτη δεν εμφανίζονται. | Επανεκκινήστε ή φορτώστε ξανά τον πελάτη MCP. |

## Σημειώσεις Ασφαλείας

- Οι κλήσεις εργαλείων MCP ελέγχονται από το μοντέλο της εφαρμογής υποδοχής, επομένως η μετάφραση αποθετηρίου είναι από προεπιλογή dry-run.
- Η πλήρης μετάφραση αποθετηρίου μπορεί να δημιουργήσει, ενημερώσει ή καταργήσει πολλά αρχεία. Απαιτήστε ρητή έγκριση χρήστη πριν ορίσετε `confirm_write=true`.
- Το εργαλείο κατάστασης διαμόρφωσης δεν επιστρέφει ποτέ κλειδιά API, endpoints ή άλλες μυστικές τιμές.
- Η μετάφραση εικόνας επιστρέφει δεδομένα εικόνας σε base64. Οι μεγάλες εικόνες μπορεί να παράγουν μεγάλες αποκρίσεις εργαλείων.
- Τα εργαλεία agent-assisted επιστρέφουν πηγές κομματιών και prompts στον host MCP. Χρησιμοποιήστε τα μόνο με περιεχόμενο που ο χρήστης αισθάνεται άνετα να στείλει στο μοντέλο του host agent.