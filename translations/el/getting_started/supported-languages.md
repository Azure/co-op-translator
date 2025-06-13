<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4ed48f23ec418b31e90a02fe629fcde",
  "translation_date": "2025-06-12T12:10:58+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "el"
}
-->
# Υποστηριζόμενες γλώσσες

Ο παρακάτω πίνακας απαριθμεί τις γλώσσες που υποστηρίζονται αυτή τη στιγμή από το **Co-op Translator**. Περιλαμβάνει κωδικούς γλωσσών, ονόματα γλωσσών και τυχόν γνωστά προβλήματα που σχετίζονται με κάθε γλώσσα. Εάν θέλετε να προσθέσετε υποστήριξη για μια νέα γλώσσα, παρακαλώ προσθέστε τον αντίστοιχο κωδικό γλώσσας, το όνομα και την κατάλληλη γραμματοσειρά στο αρχείο `font_language_mappings.yml` που βρίσκεται στο `src/co_op_translator/fonts/` και υποβάλετε ένα pull request μετά από δοκιμές.

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | English              | NotoSans-Medium.ttf               | No          | No           |
| fr            | French               | NotoSans-Medium.ttf               | No          | No           |
| es            | Spanish              | NotoSans-Medium.ttf               | No          | No           |
| de            | German               | NotoSans-Medium.ttf               | No          | No           |
| ru            | Russian              | NotoSans-Medium.ttf               | No          | No           |
| ar            | Arabic               | NotoSansArabic-Medium.ttf         | Yes         | No           |
| fa            | Persian (Farsi)      | NotoSansArabic-Medium.ttf         | No          | No           |
| ur            | Urdu                 | NotoSansArabic-Medium.ttf         | No          | No           |
| zh            | Chinese (Simplified) | NotoSansCJK-Medium.ttc            | No          | No           |
| mo            | Chinese (Traditional, Macau) | NotoSansCJK-Medium.ttc    | No          | No           |
| hk            | Chinese (Traditional, Hong Kong) | NotoSansCJK-Medium.ttc| No          | No           |
| tw            | Chinese (Traditional, Taiwan) | NotoSansCJK-Medium.ttc   | No          | No           |
| ja            | Japanese             | NotoSansCJK-Medium.ttc            | No          | No           |
| ko            | Korean               | NotoSansCJK-Medium.ttc            | No          | No           |
| hi            | Hindi                | NotoSansDevanagari-Medium.ttf     | No          | No           |
| bn            | Bengali              | NotoSansBengali-Medium.ttf        | No          | No           |
| mr            | Marathi              | NotoSansDevanagari-Medium.ttf     | No          | No           |
| ne            | Nepali               | NotoSansDevanagari-Medium.ttf     | No          | No           |
| pa            | Punjabi (Gurmukhi)   | NotoSansGurmukhi-Medium.ttf       | No          | No           |
| pt            | Portuguese (Portugal)| NotoSans-Medium.ttf               | No          | No           |
| br            | Portuguese (Brazil)  | NotoSans-Medium.ttf               | No          | No           |
| it            | Italian              | NotoSans-Medium.ttf               | No          | No           |
| pl            | Polish               | NotoSans-Medium.ttf               | No          | No           |
| tr            | Turkish              | NotoSans-Medium.ttf               | No          | No           |
| el            | Greek                | NotoSans-Medium.ttf               | No          | No           |
| th            | Thai                 | NotoSansThai-Medium.ttf           | No          | No           |
| sv            | Swedish              | NotoSans-Medium.ttf               | No          | No           |
| da            | Danish               | NotoSans-Medium.ttf               | No          | No           |
| no            | Norwegian            | NotoSans-Medium.ttf               | No          | No           |
| fi            | Finnish              | NotoSans-Medium.ttf               | No          | No           |
| nl            | Dutch                | NotoSans-Medium.ttf               | No          | No           |
| he            | Hebrew               | NotoSansHebrew-Medium.ttf         | No          | No           |
| vi            | Vietnamese           | NotoSans-Medium.ttf               | No          | No           |
| id            | Indonesian           | NotoSans-Medium.ttf               | No          | No           |
| ms            | Malay                | NotoSans-Medium.ttf               | No          | No           |
| tl            | Tagalog (Filipino)   | NotoSans-Medium.ttf               | No          | No           |
| sw            | Swahili              | NotoSans-Medium.ttf               | No          | No           |
| hu            | Hungarian            | NotoSans-Medium.ttf               | No          | No           |
| cs            | Czech                | NotoSans-Medium.ttf               | No          | No           |
| sk            | Slovak               | NotoSans-Medium.ttf               | No          | No           |
| ro            | Romanian             | NotoSans-Medium.ttf               | No          | No           |
| bg            | Bulgarian            | NotoSans-Medium.ttf               | No          | No           |
| sr            | Serbian (Cyrillic)   | NotoSans-Medium.ttf               | No          | No           |
| hr            | Croatian             | NotoSans-Medium.ttf               | No          | No           |
| sl            | Slovenian            | NotoSans-Medium.ttf               | No          | No           |
| uk            | Ukrainian            | NotoSans-Medium.ttf               | No          | No           |
| my            | Burmese (Myanmar)    | NotoSans-Medium.ttf               | No          | No           |

## Προσθήκη νέας γλώσσας

Για να προσθέσετε υποστήριξη για μια νέα γλώσσα:

1. Μεταβείτε στο [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml).
2. Προσθέστε τον κωδικό γλώσσας, το όνομα και το κατάλληλο αρχείο γραμματοσειράς. Βεβαιωθείτε ότι έχετε συμπεριλάβει το `rtl` χαρακτηριστικό εάν η γλώσσα είναι από δεξιά προς τα αριστερά.
3. Εάν χρειαστεί να χρησιμοποιήσετε νέα γραμματοσειρά, βεβαιωθείτε ότι η γραμματοσειρά είναι ελεύθερη για χρήση σε έργα ανοιχτού κώδικα ελέγχοντας τους όρους άδειας και πνευματικών δικαιωμάτων. Μετά την επιβεβαίωση, προσθέστε το αρχείο γραμματοσειράς στον κατάλογο `src/co_op_translator/fonts/`.
4. Δοκιμάστε τις αλλαγές τοπικά για να βεβαιωθείτε ότι η νέα γλώσσα υποστηρίζεται σωστά.
5. Υποβάλετε ένα Pull Request με τις αλλαγές σας και αναφέρετε την προσθήκη της νέας γλώσσας στην περιγραφή του PR.

Παράδειγμα:

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική μετάφραση από άνθρωπο. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.