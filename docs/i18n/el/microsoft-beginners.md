# Αποθετήρια Microsoft για Αρχάριους

Αυτή η σελίδα είναι για τους συντηρητές των αποθετηρίων "For Beginners" της Microsoft που χρησιμοποιούν την κοινόχρηστη ενότητα README "Other Courses".

Οι περισσότεροι χρήστες του Co-op Translator δεν χρειάζονται αυτή τη σελίδα.

## Αυτόματος Συγχρονισμός της Ενότητας "Other Courses"

Προσθέστε αυτούς τους δείκτες γύρω από την ενότητα "Other Courses" στο README σας:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Κάθε φορά που το Co-op Translator εκτελείται μέσω της CLI ή του GitHub Actions, αντικαθιστά το περιεχόμενο μεταξύ των δεικτών με το συσκευασμένο πρότυπο.

## Ενημέρωση του Κοινόχρηστου Προτύπου

Η πηγή του προτύπου βρίσκεται στο:

```text
src/co_op_translator/templates/other_courses.md
```

Για να ενημερώσετε το κοινόχρηστο περιεχόμενο:

1. Επεξεργαστείτε το πρότυπο.
2. Ανοίξτε ένα pull request στο Co-op Translator.
3. Αφού κυκλοφορήσει η αλλαγή, εκτελέστε το Co-op Translator στο στοχευόμενο αποθετήριο.

## Συμβουλή για Sparse Checkout

Τα μεγάλα αποθετήρια μαθημάτων μπορεί να γίνουν δαπανηρά για κλωνοποίηση όταν περιλαμβάνουν πολλές μεταφρασμένες εξόδους. Μπορείτε να συμπεριλάβετε αυτή τη σύσταση στις παραγόμενες ενότητες γλωσσών:

```markdown
> **Prefer to Clone Locally?**
>
> This repository includes many language translations, which can significantly increase download size. To clone without translations, use sparse checkout:
>
> ```bash
> git clone --filter=blob:none --sparse https://github.com/org/repo.git
> cd repo
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
```