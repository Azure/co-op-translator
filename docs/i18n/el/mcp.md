# MCP Server

Co-op Translator περιλαμβάνει έναν server Model Context Protocol για agents, επεξεργαστές και πελάτες συμβατούς με MCP.

Για την προεπιλεγμένη τοπική ρύθμιση, οι χρήστες δεν διατηρούν ξεχωριστό server χειροκίνητα. Διαμορφώνουν τον MCP client τους και ο client ξεκινάει το `co-op-translator-mcp` αυτόματα μέσω `stdio` όταν χρειαστεί εργαλεία του Co-op Translator.

Εάν αποφασίζετε ανάμεσα σε CLI, Python API και MCP, ξεκινήστε με το [Choose Your Workflow](workflows.md).

Χρησιμοποιήστε MCP όταν ένας agent ή επεξεργαστής πρέπει να καλέσει απευθείας το Co-op Translator:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Ο MCP server τυλίγει το ίδιο δημόσιο Python API που τεκμηριώνεται στο [Python API](api.md). Τα εργαλεία που βασίζονται σε providers χρησιμοποιούν τους ίδιους ρυθμισμένους providers με το CLI και το Python API. Τα εργαζόμενα από agent εργαλεία προετοιμάζουν κομμάτια για τον MCP host agent για μετάφραση και μετά χρησιμοποιούν το Co-op Translator για να ανασυνθέσουν το τελικό Markdown ή notebook.

## Step 1: Install and Configure Co-op Translator

Εγκαταστήστε το Co-op Translator στο Python περιβάλλον που θα χρησιμοποιήσει ο MCP client σας:

```bash
pip install co-op-translator
```

Για τοπική ανάπτυξη από αυτό το repository, εγκαταστήστε το πακέτο σε editable mode:

```bash
pip install -e .
```

Επιλέξτε τη λειτουργία μετάφρασης που θα χρησιμοποιήσει ο MCP client σας:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Το Co-op Translator καλεί `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, ή `run_translation`. | Η μετάφραση Markdown και notebook απαιτεί Azure OpenAI ή OpenAI. Η μετάφραση εικόνων απαιτεί επίσης Azure AI Vision. |
| Agent-assisted | Ο MCP host agent μεταφράζει τα κομμάτια που επιστρέφονται από `start_markdown_agent_translation` ή `start_notebook_agent_translation`. | Δεν απαιτούνται διαπιστευτήρια παρόχου LLM του Co-op Translator για κομμάτια Markdown ή notebook. Η μετάφραση εικόνων δεν καλύπτεται ακόμη από το agent-assisted mode. |

Εάν ξεκινάτε με μετάφραση Markdown ή notebook μέσα σε έναν agent όπως Codex ή Claude Code, ξεκινήστε με το agent-assisted mode. Χρησιμοποιήστε το provider-backed mode όταν θέλετε το ίδιο το Co-op Translator να καλεί τους ρυθμισμένους providers σας, όταν μεταφράζετε εικόνες, ή όταν εκτελείτε μετάφραση επιπέδου repository όπως το CLI.

Διαμορφώστε τα διαπιστευτήρια των providers μόνο για workflows που είναι provider-backed:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Η provider-backed μετάφραση εικόνων χρειάζεται επιπλέον:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Το agent-assisted mode καλύπτει επί του παρόντος τα Markdown και τα Markdown κελιά notebook. Η μετάφραση εικόνων εξακολουθεί να χρησιμοποιεί τον provider-backed pipeline εικόνων και απαιτεί Azure AI Vision για OCR και αποκατάσταση διάταξης.

## Step 2: Configure Your MCP Client

Για τη συνηθισμένη τοπική ρύθμιση `stdio`, προσθέστε το Co-op Translator στη ρύθμιση του MCP client σας. Ο client θα ξεκινάει και θα σταματάει τη διεργασία αυτόματα.

Εγκατεστημένη ρύθμιση πακέτου:

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

Ρύθμιση από source checkout στα Windows:

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

Ρύθμιση από source checkout σε macOS ή Linux:

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

Μετά την αλλαγή της ρύθμισης του MCP client, επανεκκινήστε ή φορτώστε ξανά τον client ώστε να ανακαλύψει τον νέο server.

## Step 3: Verify the Server in the Client

Ζητήστε από τον MCP client να απαριθμήσει τα διαθέσιμα εργαλεία, ή καλέστε έναν από τους βοηθητικούς μη-επεμβατικούς χειρισμούς πρώτα:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Χρήσιμοι αρχικοί έλεγχοι:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Επιβεβαιώνει ότι ο server είναι προσβάσιμος και εμφανίζει τα διαθέσιμα workflows. |
| `list_supported_languages` | Επιβεβαιώνει ότι μπορούν να φορτωθούν τα πακεταρισμένα δεδομένα γλωσσών. |
| `get_configuration_status` | Επιβεβαιώνει τη διαθεσιμότητα παρόχων LLM και Vision χωρίς να αποκαλύπτει μυστικές τιμές. |

## Step 4: Choose a Workflow

### Translate Individual Files or Documents

Χρησιμοποιήστε εργαλεία provider-backed περιεχομένου όταν ο MCP client ήδη έχει το περιεχόμενο του εγγράφου ή τη διαδρομή εικόνας και το Co-op Translator πρέπει να καλέσει τους ρυθμισμένους providers.

Για Markdown:

1. Καλέστε `translate_markdown_content` με `document`, `language_code`, και προαιρετικά `source_path`.
2. Εάν το μεταφρασμένο αποτέλεσμα θα εγγραφεί σε ένα output layout του Co-op Translator, καλέστε `rewrite_markdown_paths`.
3. Αφήστε τον client να γράψει ή να επιστρέψει το τελικό `content`.

Για notebooks:

1. Καλέστε `translate_notebook_content` με το JSON του notebook και `language_code`.
2. Καλέστε `rewrite_notebook_paths` εάν οι μεταφρασμένοι σύνδεσμοι του notebook χρειάζονται προσαρμογή για έναν στόχο διαδρομής.
3. Γράψτε ή επιστρέψτε το τελικό notebook JSON.

Για εικόνες:

1. Καλέστε `translate_image_content` με `image_path`, `language_code`, και προαιρετικά `root_dir` ή `fast_mode`.
2. Διαβάστε τα επιστρεφόμενα `data_base64` και `mime_type`.
3. Εάν παρέχεται `output_path`, η μεταφρασμένη εικόνα αποθηκεύεται επίσης σε αυτήν τη διαδρομή.

Τα εργαλεία περιεχομένου δεν εκτελούν ανακάλυψη έργου, ενημερώσεις metadata, αποποιήσεις ευθύνης ή αυτόματη επανεγγραφή διαδρομών. Εάν θέλετε ο host agent να μεταφράσει κομμάτια Markdown ή notebook χωρίς διαπιστευτήρια LLM του Co-op Translator, χρησιμοποιήστε το agent-assisted workflow πιο κάτω.

### Translate with the Host Agent Model

Χρησιμοποιήστε εργαλεία agent-assisted όταν θέλετε ο MCP host agent, όπως ένας βοηθός κωδικοποίησης, να παράγει το μεταφρασμένο κείμενο αντί να διαμορφώσετε Azure OpenAI ή OpenAI για το Co-op Translator.

Σε έναν chat-based MCP client, συνήθως δεν χρειάζεται να γράφετε εσείς JSON εργαλείων. Ζητήστε από τον agent να χρησιμοποιήσει το agent-assisted workflow:

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

Εάν ο MCP client σας υποστηρίζει server prompts, χρησιμοποιήστε το `agent_assisted_markdown_translation_prompt` για να φορτώσει ο client τις ίδιες οδηγίες workflow.

Για Markdown:

1. Καλέστε `start_markdown_agent_translation` με `document`, `language_code`, και προαιρετικά `source_path`.
2. Μεταφράστε κάθε επιστρεφόμενο κομμάτι στον host agent ακολουθώντας το `prompt` του κομματιού.
3. Καλέστε `finish_markdown_agent_translation` με το αρχικό `job` και τα μεταφρασμένα κομμάτια χρησιμοποιώντας `chunk_id` και `translated_text`.
4. Εάν το περιεχόμενο θα γραφτεί σε μεταφρασμένο στοχευμένο μονοπάτι, καλέστε `rewrite_markdown_paths`.

Για notebooks:

1. Καλέστε `start_notebook_agent_translation` με το JSON του notebook και `language_code`.
2. Μεταφράστε κάθε επιστρεφόμενο κομμάτι στον host agent.
3. Καλέστε `finish_notebook_agent_translation` με το αρχικό `job` και τα μεταφρασμένα κομμάτια.
4. Καλέστε `rewrite_notebook_paths` εάν οι μεταφρασμένοι σύνδεσμοι του notebook χρειάζονται προσαρμογή στόχου.

Τα εργαλεία agent-assisted δεν καλούν Azure OpenAI ή OpenAI από το Co-op Translator. Ο host agent είναι υπεύθυνος για τη μετάφραση των επιστρεφόμενων κομματιών. Το Co-op Translator αναλαμβάνει το chunking του Markdown, τη διατήρηση των placeholders, την ανασύνθεση frontmatter, την αντικατάσταση κελιών notebook και την κανονικοποίηση μετά τη μετάφραση.

### Translate an Entire Repository

Χρησιμοποιήστε `run_translation` όταν ο χρήστης θέλει το Co-op Translator να συμπεριφερθεί όπως το CLI `translate`.

Η μετάφραση repository έχει ως προεπιλογή `dry_run=true` ώστε ένας agent να μπορεί να εξετάσει το εύρος πριν τις αλλαγές αρχείων:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Για να επιτρέψετε εγγραφές, ο καλών πρέπει να ορίσει και τα `dry_run=false` και `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

Το `translate_project` εκτίθεται ως alias συμβατότητας για το `run_translation`.

### Review Translated Output

Χρησιμοποιήστε `run_review` για ντετερμινιστικούς ελέγχους που δεν απαιτούν διαπιστευτήρια LLM ή Vision:

!!! note "Beta"
    Ο MCP εκθέτει το beta API `run_review`. Είναι ασφαλές για read-only workflows ανασκόπησης, αλλά οι έλεγχοι ανασκόπησης και τα σχήματα προβλημάτων μπορεί να εξελιχθούν.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Το αποτέλεσμα περιλαμβάνει καταγεγραμμένο κείμενο εξόδου και μια δομημένη περίληψη ανασκόπησης όταν είναι διαθέσιμη.

## Manual Server Runs

Οι χειροκίνητες εκτελέσεις είναι κυρίως για αποσφαλμάτωση ή για μεταφορές που συμπεριφέρονται σαν μακροχρόνιοι servers.

Αποσφαλματώστε τον προεπιλεγμένο stdio server:

```bash
co-op-translator-mcp
```

Εκτελέστε από ένα source checkout:

```bash
python -m co_op_translator.mcp.server
```

Εκτελέστε έναν μακροχρόνιο HTTP ή SSE server:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Για τοπικές ενσωματώσεις editor και agent, προτιμήστε τη ρύθμιση `stdio` που διαχειρίζεται ο client στο Βήμα 2.

## Tools

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Translate a Markdown string. | No |
| `translate_notebook_content` | Translate Markdown cells in notebook JSON. | No |
| `translate_image_content` | Translate text in one image and return base64 image data. | Optional, only when `output_path` is provided |
| `start_markdown_agent_translation` | Prepare Markdown chunks for the host agent to translate without Co-op Translator LLM credentials. | No |
| `finish_markdown_agent_translation` | Reconstruct Markdown from host-agent translated chunks. | No |
| `start_notebook_agent_translation` | Prepare notebook Markdown-cell chunks for the host agent to translate. | No |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON from host-agent translated chunks. | No |
| `rewrite_markdown_paths` | Rewrite Markdown body and frontmatter paths for a translated target. | No |
| `rewrite_notebook_paths` | Rewrite paths inside notebook Markdown cells. | No |
| `run_translation` | Run project-level translation like the CLI. | Yes when `dry_run=false` and `confirm_write=true` |
| `translate_project` | Compatibility alias for `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | Run deterministic review checks. | No |
| `get_configuration_status` | Report configured LLM and Vision providers without exposing secrets. | No |
| `list_supported_languages` | List supported target language codes. | No |
| `get_api_overview` | Describe available MCP workflows and tools. | No |

## Resources

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON overview of workflows and tools. |
| `co-op://supported-languages` | JSON list of supported language codes. |
| `co-op://configuration` | JSON provider availability summary without secrets. |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Guide an MCP client through content translation plus optional path rewriting. |
| `agent_assisted_markdown_translation_prompt` | Guide an MCP client through host-agent Markdown translation without Co-op Translator LLM provider credentials. |
| `translate_repository_prompt` | Guide an MCP client through dry-run-first repository translation. |

## Copy-Paste Examples

Translate Markdown content:

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

Rewrite translated Markdown links:

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

Translate Markdown with the host agent model:

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

After the host agent translates each returned chunk, finish the job with the complete `job` object returned by `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Preview repository translation:

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

## Troubleshooting

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Use the absolute Python executable path and `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| The server is listed but translation fails. | Call `get_configuration_status` and confirm an LLM provider is available. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` or the notebook equivalents so the host agent translates the chunks. |
| Image translation fails. | Confirm Azure AI Vision variables are set and call `get_configuration_status`. |
| Repository translation does not write files. | Set `dry_run=false` and `confirm_write=true` only after explicit user approval. |
| Changes to client config do not appear. | Restart or reload the MCP client. |

## Safety Notes

- Οι κλήσεις εργαλείων MCP ελέγχονται από το μοντέλο της εφαρμογής host, επομένως η μετάφραση repository είναι από προεπιλογή dry-run.
- Η πλήρης μετάφραση repository μπορεί να δημιουργήσει, ενημερώσει ή αφαιρέσει πολλά αρχεία. Απαιτήστε ρητή έγκριση χρήστη πριν ορίσετε `confirm_write=true`.
- Το εργαλείο κατάστασης διαμόρφωσης δεν επιστρέφει ποτέ API keys, endpoints ή άλλες μυστικές τιμές.
- Η μετάφραση εικόνων επιστρέφει base64 δεδομένα εικόνας. Οι μεγάλες εικόνες μπορούν να παράγουν μεγάλες αποκρίσεις εργαλείων.
- Τα εργαλεία agent-assisted επιστρέφουν πηγές κομματιών και prompts στον MCP host. Χρησιμοποιήστε τα μόνο με περιεχόμενο που ο χρήστης συμφωνεί να στείλει σε εκείνο το μοντέλο host agent.