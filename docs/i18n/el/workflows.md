# Επιλέξτε τη ροή εργασίας σας

Το Co-op Translator μπορεί να χρησιμοποιηθεί με τρεις τρόπους: η CLI, το Python API, και ο MCP διακομιστής. Μοιράζονται τις ίδιες δυνατότητες μετάφρασης, αλλά το καθένα ταιριάζει σε διαφορετική ροή εργασίας.

Χρησιμοποιήστε αυτή τη σελίδα όταν αποφασίζετε από πού να ξεκινήσετε.

## Γρήγορη Απόφαση

| If you want to... | Use | Start here |
| --- | --- | --- |
| Μεταφράστε ή αναθεωρήστε ένα αποθετήριο από το τερματικό | CLI | [Αναφορά CLI](cli.md) |
| Προσθέσετε μετάφραση σε ένα σενάριο Python, υπηρεσία, σημειωματάριο, ή εργασία CI | Python API | [Python API](api.md) |
| Επιτρέψετε σε έναν agent, editor, ή πελάτη συμβατό με MCP να μεταφράσει περιεχόμενο για εσάς | MCP Server | [Διακομιστής MCP](mcp.md) |
| Μεταφράστε ένα έγγραφο Markdown, σημειωματάριο, ή εικόνα που η εφαρμογή σας έχει ήδη φορτώσει | Python API or MCP Server | [Python API](api.md) ή [Διακομιστής MCP](mcp.md) |
| Μεταφράστε ολόκληρο αποθετήριο με τυπικούς φακέλους εξόδου και μεταδεδομένα | CLI or `run_translation` | [Αναφορά CLI](cli.md) ή [Python API](api.md) |

## Χρησιμοποιήστε το CLI όταν

Επιλέξτε το CLI όταν ένα άτομο ή μια εργασία CI εκτελεί τη μετάφραση του αποθετηρίου από ένα κέλυφος.

Το CLI είναι ο πιο άμεσος δρόμος όταν θέλετε το Co-op Translator να εντοπίσει αρχεία έργου, να δημιουργήσει μεταφρασμένα αποτελέσματα, να διατηρήσει τη διάταξη του έργου, να ενημερώσει τα μεταδεδομένα και να εκτελέσει εντολές αναθεώρησης.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Κατάλληλα σενάρια:

- Μεταφράζετε ένα αποθετήριο από το τερματικό σας.
- Θέλετε μια επαναλήψιμη εντολή για ροές εργασίας CI ή κυκλοφορίας.
- Θέλετε ενσωματωμένη ανακάλυψη έργου, διαδρομές εξόδου, μεταδεδομένα, καθαρισμό και αναθεώρηση.
- Προτιμάτε μια διεπαφή εντολών αντί για τη συγγραφή κώδικα Python.

## Χρησιμοποιήστε το Python API όταν

Επιλέξτε το Python API όταν ο δικός σας κώδικας πρέπει να ελέγχει τη ροή εργασίας.

Το API είναι χρήσιμο για εφαρμογές, αυτοματοποιημένα σενάρια, σημειωματάρια, υπηρεσίες και προσαρμοσμένους αγωγούς. Σας επιτρέπει να καλείτε χαμηλού επιπέδου APIs μετάφρασης περιεχομένου για μεμονωμένα αρχεία, ή να εκτελείτε την ίδια ορχήστρωση σε επίπεδο αποθετηρίου που χρησιμοποιεί το CLI.

Μεταφράστε ένα έγγραφο Markdown και αποφασίστε πού θα το αποθηκεύσετε:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Εκτελέστε μια μετάφραση αποθετηρίου από Python:

```python
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

Κατάλληλα σενάρια:

- Η εφαρμογή σας ήδη διαβάζει αρχεία, buffers, σημειωματάρια ή bytes εικόνων.
- Χρειάζεστε προσαρμοσμένη επικύρωση, αποθήκευση, καταγραφή, επαναπροσπάθειες ή ροές έγκρισης.
- Θέλετε να μεταφράσετε ένα έγγραφο, σημειωματάριο ή εικόνα χωρίς να επεξεργαστείτε ολόκληρο αποθετήριο.
- Θέλετε μετάφραση αποθετηρίου, αλλά μέσω αυτοματοποίησης Python αντί για εντολή κελύφους.

## Χρησιμοποιήστε τον MCP διακομιστή όταν

Επιλέξτε τον MCP διακομιστή όταν ένας agent, editor, ή πελάτης συμβατός με MCP θα πρέπει να καλεί τα εργαλεία του Co-op Translator.

Σε μια κανονική τοπική ρύθμιση, ο χρήστης δεν διατηρεί χειροκίνητα έναν διακομιστή σε λειτουργία. Ο πελάτης MCP ξεκινάει το `co-op-translator-mcp` μέσω του `stdio` όταν χρειάζεται τα εργαλεία.

Παραδείγματα αιτημάτων χρήστη που θα μπορούσε να χειριστεί ένας agent:

- "Μεταφράστε αυτό το αρχείο Markdown στα Κορεακά και διατηρήστε τους συνδέσμους σωστούς."
- "Μεταφράστε αυτό το αρχείο Markdown στα Κορεακά με τη ροή εργασίας MCP με βοήθεια agent, χρησιμοποιώντας το δικό σας μοντέλο για τα μεταφρασμένα κομμάτια."
- "Μεταφράστε αυτό το σημειωματάριο στα Κορεακά, διατηρήστε τα κελιά κώδικα και χρησιμοποιήστε το Co-op Translator MCP για να αναδομήσετε το σημειωματάριο."
- "Μεταφράστε το κείμενο στην εικόνα αυτή στα Ιαπωνικά και αποθηκεύστε το αποτέλεσμα."
- "Κάντε δοκιμαστική εκτέλεση μετάφρασης αποθετηρίου στα Ισπανικά και πείτε μου τι θα άλλαζε."
- "Ελέγξτε αν η έξοδος μετάφρασης στα Κορεακά είναι ενημερωμένη."

Για Markdown και σημειωματάρια, ο MCP μπορεί να λειτουργήσει σε δύο λειτουργίες:

| Mode | Use when | Main tools |
| --- | --- | --- |
| Agent-assisted | Ο host agent του MCP θα μεταφράζει κομμάτια με το δικό του μοντέλο, χωρίς διαπιστευτήρια παρόχου LLM του Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Το Co-op Translator θα πρέπει να καλεί απευθείας Azure OpenAI ή OpenAI. | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-backed Markdown tool call shape:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

MCP image tool call shape:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

Η μετάφραση αποθετηρίου είναι δοκιμαστική (dry-run) από προεπιλογή μέσω MCP:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

Κατάλληλα σενάρια:

- Θέλετε ροές εργασίας μετάφρασης σε φυσική γλώσσα μέσα σε έναν agent ή έναν editor.
- Θέλετε μετάφραση Markdown ή σημειωματαρίου όπου το μοντέλο του host agent μεταφράζει προετοιμασμένα κομμάτια.
- Θέλετε ο agent να μεταφράσει επιλεγμένο περιεχόμενο αντί ολόκληρου του αποθετηρίου.
- Θέλετε ένα βήμα έγκρισης πριν τις εγγραφές σε ολόκληρο το αποθετήριο.
- Θέλετε μια διεπαφή που εκθέτει εργαλεία Markdown, σημειωματαρίου, εικόνας, αναθεώρησης και επαναγραφή διαδρομών.

## Πώς Συνδέονται

Το CLI είναι η καλύτερη προεπιλογή για ανθρώπους που μεταφράζουν αποθετήρια. Το Python API είναι καλύτερο όταν ο κώδικάς σας ελέγχει τη ροή εργασίας. Ο MCP διακομιστής είναι καλύτερος όταν ένας agent ή editor έχει την ευθύνη της ροής εργασίας.

Και οι τρεις διαδρομές χρησιμοποιούν το ίδιο δημόσιο Co-op Translator API, οπότε μπορείτε να ξεκινήσετε με το CLI, να αυτοματοποιήσετε με Python αργότερα, και να εκθέσετε τις ίδιες δυνατότητες σε πελάτες MCP όταν χρειάζεστε ροές εργασίας που καθοδηγούνται από agents.