<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:12:46+00:00",
  "source_file": "README.md",
  "language_code": "el"
}
-->
# Co-op Translator

_Αυτοματοποιήστε εύκολα τη μετάφραση του εκπαιδευτικού σας περιεχομένου στο GitHub σε πολλές γλώσσες για να προσεγγίσετε ένα παγκόσμιο κοινό._

### 🌐 Υποστήριξη Πολλών Γλωσσών

#### Υποστηρίζεται από το [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Αραβικά](../ar/README.md) | [Βεγγαλικά](../bn/README.md) | [Βουλγαρικά](../bg/README.md) | [Βιρμανικά (Μιανμάρ)](../my/README.md) | [Κινέζικα (Απλοποιημένα)](../zh/README.md) | [Κινέζικα (Παραδοσιακά, Χονγκ Κονγκ)](../hk/README.md) | [Κινέζικα (Παραδοσιακά, Μακάο)](../mo/README.md) | [Κινέζικα (Παραδοσιακά, Ταϊβάν)](../tw/README.md) | [Κροατικά](../hr/README.md) | [Τσέχικα](../cs/README.md) | [Δανέζικα](../da/README.md) | [Ολλανδικά](../nl/README.md) | [Εσθονικά](../et/README.md) | [Φινλανδικά](../fi/README.md) | [Γαλλικά](../fr/README.md) | [Γερμανικά](../de/README.md) | [Ελληνικά](./README.md) | [Εβραϊκά](../he/README.md) | [Χίντι](../hi/README.md) | [Ουγγρικά](../hu/README.md) | [Ινδονησιακά](../id/README.md) | [Ιταλικά](../it/README.md) | [Ιαπωνικά](../ja/README.md) | [Κορεατικά](../ko/README.md) | [Λιθουανικά](../lt/README.md) | [Μαλαισιανά](../ms/README.md) | [Μαραθικά](../mr/README.md) | [Νεπαλέζικα](../ne/README.md) | [Νορβηγικά](../no/README.md) | [Περσικά (Φαρσί)](../fa/README.md) | [Πολωνικά](../pl/README.md) | [Πορτογαλικά (Βραζιλία)](../br/README.md) | [Πορτογαλικά (Πορτογαλία)](../pt/README.md) | [Πουντζάμπι (Γκουρμούκι)](../pa/README.md) | [Ρουμανικά](../ro/README.md) | [Ρωσικά](../ru/README.md) | [Σερβικά (Κυριλλικά)](../sr/README.md) | [Σλοβακικά](../sk/README.md) | [Σλοβενικά](../sl/README.md) | [Ισπανικά](../es/README.md) | [Σουαχίλι](../sw/README.md) | [Σουηδικά](../sv/README.md) | [Ταγκάλογκ (Φιλιππίνες)](../tl/README.md) | [Ταμίλ](../ta/README.md) | [Ταϊλανδικά](../th/README.md) | [Τουρκικά](../tr/README.md) | [Ουκρανικά](../uk/README.md) | [Ουρντού](../ur/README.md) | [Βιετναμέζικα](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Επισκόπηση

Το **Co-op Translator** σας επιτρέπει να μεταφράζετε γρήγορα το εκπαιδευτικό σας περιεχόμενο στο GitHub σε πολλές γλώσσες, ώστε να προσεγγίζετε εύκολα ένα παγκόσμιο κοινό. Όταν ενημερώνετε τα αρχεία Markdown, τις εικόνες ή τα Jupyter notebooks σας, οι μεταφράσεις συγχρονίζονται αυτόματα ώστε το εκπαιδευτικό σας περιεχόμενο να παραμένει επίκαιρο και σχετικό για διεθνείς χρήστες.

Δείτε πώς το Co-op Translator οργανώνει το μεταφρασμένο εκπαιδευτικό περιεχόμενο στο GitHub:

![Παράδειγμα](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.el.png)

## Γρήγορη εκκίνηση

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

Docker:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Ελάχιστη ρύθμιση

- Δημιουργήστε ένα `.env` χρησιμοποιώντας το πρότυπο: [.env.template](../../.env.template)
- Ρυθμίστε έναν πάροχο LLM (Azure OpenAI ή OpenAI)
- Για μετάφραση εικόνων (`-img`), ρυθμίστε επίσης το Azure AI Vision
- Προτείνεται: Αν έχετε μεταφράσεις που δημιουργήθηκαν από άλλα εργαλεία, καθαρίστε τις πρώτα για να αποφύγετε διενέξεις (π.χ. `translations/`).
- Προτείνεται: Προσθέστε μια ενότητα μεταφράσεων στο README σας χρησιμοποιώντας το [πρότυπο γλωσσών README](./README_languages_template.md)
- Δείτε: [Ρύθμιση Azure AI](./getting_started/set-up-azure-ai.md)

## Χρήση

Μεταφράστε όλους τους υποστηριζόμενους τύπους:

```bash
translate -l "ko ja"
```

Μόνο Markdown:

```bash
translate -l "de" -md
```

Markdown + εικόνες:

```bash
translate -l "pt" -md -img
```

Μόνο notebooks:

```bash
translate -l "zh" -nb
```

Περισσότερες επιλογές: [Αναφορά εντολών](./getting_started/command-reference.md)

## Δυνατότητες

- Αυτοματοποιημένη μετάφραση για Markdown, notebooks και εικόνες
- Διατηρεί τις μεταφράσεις συγχρονισμένες με τις αλλαγές της πηγής
- Λειτουργεί τοπικά (CLI) ή σε CI (GitHub Actions)
- Υποστηρίζει Azure OpenAI ή OpenAI· προαιρετικά Azure AI Vision για εικόνες
- Διατηρεί τη μορφοποίηση και τη δομή του Markdown

## Τεκμηρίωση

- [Οδηγός γραμμής εντολών](./getting_started/command-line-guide/command-line-guide.md)
- [Οδηγός GitHub Actions (Δημόσια αποθετήρια & τυπικά secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Οδηγός GitHub Actions (Αποθετήρια οργανισμού Microsoft & ρυθμίσεις σε επίπεδο οργανισμού)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Υποστηριζόμενες γλώσσες](./getting_started/supported-languages.md)
- [Αντιμετώπιση προβλημάτων](./getting_started/troubleshooting.md)

## Υποστηρίξτε μας και ενισχύστε τη μάθηση παγκοσμίως

Γίνετε μέρος της αλλαγής στον τρόπο που διαμοιράζεται το εκπαιδευτικό περιεχόμενο παγκοσμίως! Δώστε ένα ⭐ στο [Co-op Translator](https://github.com/azure/co-op-translator) στο GitHub και στηρίξτε την αποστολή μας να καταργήσουμε τα γλωσσικά εμπόδια στη μάθηση και την τεχνολογία. Το ενδιαφέρον και η συνεισφορά σας έχουν πραγματικό αντίκτυπο! Κάθε συνεισφορά σε κώδικα ή ιδέα για νέα χαρακτηριστικά είναι ευπρόσδεκτη.

### Εξερευνήστε εκπαιδευτικό περιεχόμενο της Microsoft στη γλώσσα σας

- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Βίντεο Παρουσιάσεις

Μάθετε περισσότερα για το Co-op Translator μέσα από τις παρουσιάσεις μας _(Κάντε κλικ στην εικόνα παρακάτω για να δείτε στο YouTube.)_:

- **Open at Microsoft**: Μια σύντομη εισαγωγή 18 λεπτών και γρήγορος οδηγός για το πώς να χρησιμοποιήσετε το Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.el.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Συνεισφορά

Αυτό το έργο καλωσορίζει συνεισφορές και προτάσεις. Θέλετε να συνεισφέρετε στο Azure Co-op Translator; Δείτε το [CONTRIBUTING.md](./CONTRIBUTING.md) για οδηγίες σχετικά με το πώς μπορείτε να βοηθήσετε να γίνει το Co-op Translator πιο προσβάσιμο.

## Συντελεστές

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Κώδικας Δεοντολογίας

Αυτό το έργο έχει υιοθετήσει τον [Κώδικα Δεοντολογίας Ανοιχτού Κώδικα της Microsoft](https://opensource.microsoft.com/codeofconduct/).
Για περισσότερες πληροφορίες δείτε το [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ή
επικοινωνήστε με το [opencode@microsoft.com](mailto:opencode@microsoft.com) για επιπλέον ερωτήσεις ή σχόλια.

## Υπεύθυνη Τεχνητή Νοημοσύνη

Η Microsoft δεσμεύεται να βοηθά τους πελάτες της να χρησιμοποιούν υπεύθυνα τα προϊόντα AI, να μοιράζεται τις γνώσεις της και να χτίζει σχέσεις εμπιστοσύνης μέσω εργαλείων όπως τα Transparency Notes και Impact Assessments. Πολλοί από αυτούς τους πόρους βρίσκονται στο [https://aka.ms/RAI](https://aka.ms/RAI).
Η προσέγγιση της Microsoft για υπεύθυνη AI βασίζεται στις αρχές της δικαιοσύνης, αξιοπιστίας και ασφάλειας, ιδιωτικότητας και ασφάλειας, συμπερίληψης, διαφάνειας και λογοδοσίας.

Μεγάλης κλίμακας μοντέλα φυσικής γλώσσας, εικόνας και ομιλίας - όπως αυτά που χρησιμοποιούνται σε αυτό το δείγμα - ενδέχεται να συμπεριφέρονται με τρόπους που είναι άδικοι, αναξιόπιστοι ή προσβλητικοί, προκαλώντας βλάβες. Παρακαλούμε συμβουλευτείτε το [Transparency note της υπηρεσίας Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) για να ενημερωθείτε για τους κινδύνους και τους περιορισμούς.

Η προτεινόμενη προσέγγιση για τον μετριασμό αυτών των κινδύνων είναι να συμπεριλάβετε ένα σύστημα ασφάλειας στην αρχιτεκτονική σας που μπορεί να ανιχνεύει και να αποτρέπει επιβλαβή συμπεριφορά. Το [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) παρέχει ένα ανεξάρτητο επίπεδο προστασίας, ικανό να ανιχνεύει επιβλαβές περιεχόμενο που δημιουργείται από χρήστες ή AI σε εφαρμογές και υπηρεσίες. Το Azure AI Content Safety περιλαμβάνει APIs για κείμενο και εικόνα που σας επιτρέπουν να ανιχνεύετε επιβλαβές υλικό. Διαθέτουμε επίσης το διαδραστικό Content Safety Studio που σας επιτρέπει να δείτε, να εξερευνήσετε και να δοκιμάσετε δείγματα κώδικα για την ανίχνευση επιβλαβούς περιεχομένου σε διάφορες μορφές. Η παρακάτω [τεκμηρίωση γρήγορης εκκίνησης](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) σας καθοδηγεί στη χρήση της υπηρεσίας.
Ένα ακόμα στοιχείο που πρέπει να λάβετε υπόψη είναι η συνολική απόδοση της εφαρμογής. Σε εφαρμογές με πολλαπλές λειτουργίες και μοντέλα, η απόδοση σημαίνει ότι το σύστημα λειτουργεί όπως εσείς και οι χρήστες σας περιμένετε, συμπεριλαμβανομένου του να μην παράγει επιβλαβή αποτελέσματα. Είναι σημαντικό να αξιολογείτε την απόδοση της συνολικής εφαρμογής σας χρησιμοποιώντας [μετρικές ποιότητας παραγωγής και κινδύνου και ασφάλειας](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Μπορείτε να αξιολογήσετε την εφαρμογή AI σας στο περιβάλλον ανάπτυξης χρησιμοποιώντας το [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Δίνοντας είτε ένα σύνολο δοκιμαστικών δεδομένων είτε έναν στόχο, οι γεννήσεις της εφαρμογής σας με γενετική AI μετρώνται ποσοτικά με ενσωματωμένους αξιολογητές ή προσαρμοσμένους αξιολογητές της επιλογής σας. Για να ξεκινήσετε με το prompt flow sdk για να αξιολογήσετε το σύστημά σας, μπορείτε να ακολουθήσετε τον [οδηγό γρήγορης εκκίνησης](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Μόλις εκτελέσετε μια αξιολόγηση, μπορείτε να [οραματιστείτε τα αποτελέσματα στο Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Εμπορικά Σήματα

Αυτό το έργο μπορεί να περιέχει εμπορικά σήματα ή λογότυπα για έργα, προϊόντα ή υπηρεσίες. Η εξουσιοδοτημένη χρήση εμπορικών σημάτων ή λογοτύπων της Microsoft υπόκειται και πρέπει να ακολουθεί τις [Οδηγίες Εμπορικών Σημάτων & Επωνυμίας της Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Η χρήση εμπορικών σημάτων ή λογοτύπων της Microsoft σε τροποποιημένες εκδόσεις αυτού του έργου δεν πρέπει να προκαλεί σύγχυση ή να υπονοεί χορηγία από τη Microsoft. Κάθε χρήση εμπορικών σημάτων ή λογοτύπων τρίτων υπόκειται στις πολιτικές των αντίστοιχων τρίτων.

## Λήψη Βοήθειας

Αν κολλήσετε ή έχετε απορίες σχετικά με την ανάπτυξη εφαρμογών AI, μπείτε:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Αν έχετε σχόλια για το προϊόν ή συναντήσετε σφάλματα κατά την ανάπτυξη, επισκεφθείτε:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Αποποίηση Ευθύνης**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρότι καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρανοήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.