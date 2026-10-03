# Πρότυπο README για Γλώσσες

Ο Co-op Translator μπορεί να διατηρεί έναν πίνακα γλωσσών README για αποθετήρια που δημοσιεύουν μεταφρασμένο περιεχόμενο.

Χρησιμοποιήστε τους παρακάτω δείκτες όταν θέλετε ο Co-op Translator να αντικαθιστά ολόκληρο το τμήμα κάθε φορά που εκτελείται η μετάφραση. Αφαιρέστε τους δείκτες αν προτιμάτε να διατηρείτε χειροκίνητα ένα προσαρμοσμένο υποσύνολο.

Η ένδειξη απόδοσης και ο σύνδεσμος ξεκινήματος πάνω από τους δείκτες είναι προαιρετικοί. Βοηθούν τους αναγνώστες να ανακαλύψουν πώς διατηρούνται οι μεταφράσεις και πώς να μεταφράσουν τα δικά τους αποθετήρια. Κρατήστε τα έξω από τους δείκτες ώστε οι ενημερώσεις του πίνακα γλωσσών να τα διατηρούν. Όταν ενημερώνετε άλλο αποθετήριο, ακολουθήστε τις οδηγίες συνεισφοράς του και αφήστε τους συντηρητές να αποφασίσουν αν θα συμπεριλάβουν αυτό το κείμενο.

````markdown
### Multi-Language Support

#### Supported by [Co-op Translator](https://github.com/Azure/co-op-translator)

Maintain your own documentation? [Start with one README and one language](https://github.com/Azure/co-op-translator/blob/main/docs/github-actions.md#your-first-readme-translation-pr).

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](./translations/ar/README.md) | [Bengali](./translations/bn/README.md) | [Bulgarian](./translations/bg/README.md) | [Burmese (Myanmar)](./translations/my/README.md) | [Chinese (Simplified)](./translations/zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](./translations/zh-HK/README.md) | [Chinese (Traditional, Macau)](./translations/zh-MO/README.md) | [Chinese (Traditional, Taiwan)](./translations/zh-TW/README.md) | [Croatian](./translations/hr/README.md) | [Czech](./translations/cs/README.md) | [Danish](./translations/da/README.md) | [Dutch](./translations/nl/README.md) | [Estonian](./translations/et/README.md) | [Finnish](./translations/fi/README.md) | [French](./translations/fr/README.md) | [German](./translations/de/README.md) | [Greek](./translations/el/README.md) | [Hebrew](./translations/he/README.md) | [Hindi](./translations/hi/README.md) | [Hungarian](./translations/hu/README.md) | [Indonesian](./translations/id/README.md) | [Italian](./translations/it/README.md) | [Japanese](./translations/ja/README.md) | [Kannada](./translations/kn/README.md) | [Khmer](./translations/km/README.md) | [Korean](./translations/ko/README.md) | [Lithuanian](./translations/lt/README.md) | [Malay](./translations/ms/README.md) | [Malayalam](./translations/ml/README.md) | [Manipuri (Meitei Mayek)](./translations/mni/README.md) | [Marathi](./translations/mr/README.md) | [Nepali](./translations/ne/README.md) | [Nigerian Pidgin](./translations/pcm/README.md) | [Norwegian](./translations/no/README.md) | [Persian (Farsi)](./translations/fa/README.md) | [Polish](./translations/pl/README.md) | [Portuguese (Brazil)](./translations/pt-BR/README.md) | [Portuguese (Portugal)](./translations/pt-PT/README.md) | [Punjabi (Gurmukhi)](./translations/pa/README.md) | [Romanian](./translations/ro/README.md) | [Russian](./translations/ru/README.md) | [Serbian (Cyrillic)](./translations/sr/README.md) | [Slovak](./translations/sk/README.md) | [Slovenian](./translations/sl/README.md) | [Spanish](./translations/es/README.md) | [Swahili](./translations/sw/README.md) | [Swedish](./translations/sv/README.md) | [Tagalog (Filipino)](./translations/tl/README.md) | [Tamil](./translations/ta/README.md) | [Telugu](./translations/te/README.md) | [Thai](./translations/th/README.md) | [Turkish](./translations/tr/README.md) | [Ukrainian](./translations/uk/README.md) | [Urdu](./translations/ur/README.md) | [Vietnamese](./translations/vi/README.md)

> **Prefer to Clone Locally?**
>
> This repository includes many language translations, which can significantly increase download size. To clone without translations, use sparse checkout:
>
> ```bash
> git clone --filter=blob:none --sparse https://github.com/org/repo.git
> cd repo
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```

<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->
````

Εξατομικεύστε το URL του αποθετηρίου sparse-checkout κατά τη διάρκεια της μετάφρασης:

```bash
translate -l "ko" --repo-url "https://github.com/org/repo.git"
```

Εάν οι δείκτες υπάρχουν, ο Co-op Translator μπορεί να ενημερώσει τον δημιουργημένο πίνακα όταν προστίθενται ή αλλάζουν γλώσσες.

Για ένα υπάρχον README, μπορείτε να προσθέσετε την προαιρετική ένδειξη απόδοσης και τον σύνδεσμο για να ξεκινήσετε πάνω από τους δείκτες του πίνακα γλωσσών χωρίς να αντικαταστήσετε τους συνδέσμους γλώσσας ή άλλο περιεχόμενο. Διευθύνετε τους συνδέσμους των υποστηριζόμενων γλωσσών προς τον [οδηγό της τρέχουσας γλώσσας](https://github.com/Azure/co-op-translator/blob/main/docs/supported-languages.md).