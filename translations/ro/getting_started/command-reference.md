<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T12:19:11+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "ro"
}
-->
# Referință comenzi

CLI-ul **Co-op Translator** oferă mai multe opțiuni pentru personalizarea procesului de traducere:

Comandă                                      | Descriere
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Traduce proiectul în limbile specificate. Exemplu: translate -l "es fr de" traduce în spaniolă, franceză și germană. Folosește translate -l "all" pentru a traduce în toate limbile suportate.
translate -l "language_codes" -u              | Actualizează traducerile prin ștergerea celor existente și recrearea lor. Atenție: Aceasta va șterge toate traducerile curente pentru limbile specificate.
translate -l "language_codes" -img            | Traduce doar fișierele imagine.
translate -l "language_codes" -md             | Traduce doar fișierele Markdown.
translate -l "language_codes" -nb             | Traduce doar fișierele Jupyter notebook (.ipynb).
translate -l "language_codes" --fix           | Retraduce fișierele cu scoruri de încredere scăzute, pe baza rezultatelor evaluărilor anterioare.
translate -l "language_codes" -d              | Activează modul debug pentru logare detaliată.
translate -l "language_codes" --save-logs, -s | Salvează logurile de nivel DEBUG în fișiere sub <root_dir>/logs/ (consola rămâne controlată de -d)
translate -l "language_codes" -r "root_dir"   | Specifică directorul rădăcină al proiectului
translate -l "language_codes" -f              | Folosește modul rapid pentru traducerea imaginilor (până la de 3 ori mai rapid, cu o ușoară scădere a calității și aliniamentului).
translate -l "language_codes" -y              | Confirmă automat toate prompturile (util pentru pipeline-uri CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Activează sau dezactivează adăugarea unei secțiuni de avertisment privind traducerea automată în markdown și notebook-uri traduse (implicit: activat).
translate -l "language_codes" --help          | afișează detalii de ajutor în CLI cu comenzile disponibile
evaluate -l "language_code"                  | Evaluează calitatea traducerii pentru o limbă specifică și oferă scoruri de încredere
evaluate -l "language_code" -c 0.8           | Evaluează traducerile cu un prag personalizat de încredere
evaluate -l "language_code" -f               | Mod de evaluare rapidă (doar bazat pe reguli, fără LLM)
evaluate -l "language_code" -D               | Mod de evaluare aprofundată (doar bazat pe LLM, mai detaliat dar mai lent)
evaluate -l "language_code" --save-logs, -s  | Salvează logurile de nivel DEBUG în fișiere sub <root_dir>/logs/
migrate-links -l "language_codes"             | Reprocesează fișierele Markdown traduse pentru a actualiza linkurile către notebook-uri (.ipynb). Preferă notebook-urile traduse când sunt disponibile; altfel poate reveni la notebook-urile originale.
migrate-links -l "language_codes" -r          | Specifică directorul rădăcină al proiectului (implicit: directorul curent).
migrate-links -l "language_codes" --dry-run   | Afișează ce fișiere s-ar modifica fără a scrie efectiv modificările.
migrate-links -l "language_codes" --no-fallback-to-original | Nu rescrie linkurile către notebook-urile originale când cele traduse lipsesc (actualizează doar când există traducerea).
migrate-links -l "language_codes" -d          | Activează modul debug pentru logare detaliată.
migrate-links -l "language_codes" --save-logs, -s | Salvează logurile de nivel DEBUG în fișiere sub <root_dir>/logs/
migrate-links -l "all" -y                      | Procesează toate limbile și confirmă automat promptul de avertizare.

## Exemple de utilizare

  1. Comportament implicit (adaugă traduceri noi fără a șterge pe cele existente):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Adaugă doar traduceri noi pentru imagini în coreeană (nu se șterg traducerile existente):    translate -l "ko" -img

  3. Actualizează toate traducerile în coreeană (Atenție: Șterge toate traducerile coreene existente înainte de retraducere):    translate -l "ko" -u

  4. Actualizează doar imaginile în coreeană (Atenție: Șterge toate imaginile coreene existente înainte de retraducere):    translate -l "ko" -img -u

  5. Adaugă traduceri noi pentru markdown în coreeană fără a afecta alte traduceri:    translate -l "ko" -md

  6. Corectează traducerile cu încredere scăzută pe baza rezultatelor evaluărilor anterioare: translate -l "ko" --fix

  7. Corectează traducerile cu încredere scăzută doar pentru anumite fișiere (markdown): translate -l "ko" --fix -md

  8. Corectează traducerile cu încredere scăzută doar pentru anumite fișiere (imagini): translate -l "ko" --fix -img

  9. Folosește modul rapid pentru traducerea imaginilor:    translate -l "ko" -img -f

  10. Corectează traducerile cu încredere scăzută folosind un prag personalizat: translate -l "ko" --fix -c 0.8

  11. Exemplu modul debug: - translate -l "ko" -d: Activează logarea debug.
  12. Salvează logurile în fișiere: translate -l "ko" -s
  13. DEBUG în consolă și în fișiere: translate -l "ko" -d -s
  14. Traduce fără a adăuga avertismente privind traducerea automată în output: translate -l "ko" --no-disclaimer

  15. Migrează linkurile notebook-urilor pentru traducerile în coreeană (actualizează linkurile către notebook-urile traduse când sunt disponibile):    migrate-links -l "ko"

  15. Migrează linkurile cu dry-run (fără scriere în fișiere):    migrate-links -l "ko" --dry-run

  16. Actualizează linkurile doar când există notebook-uri traduse (nu revine la cele originale):    migrate-links -l "ko" --no-fallback-to-original

  17. Procesează toate limbile cu prompt de confirmare:    migrate-links -l "all"

  18. Procesează toate limbile și confirmă automat:    migrate-links -l "all" -y
  19. Salvează logurile în fișiere pentru migrate-links:    migrate-links -l "ko ja" -s

### Exemple de evaluare

> [!WARNING]  
> **Funcționalitate Beta**: Funcționalitatea de evaluare este momentan în beta. Această caracteristică a fost lansată pentru a evalua documentele traduse, iar metodele de evaluare și implementarea detaliată sunt încă în dezvoltare și pot suferi modificări.

  1. Evaluează traducerile în coreeană: evaluate -l "ko"

  2. Evaluează cu prag personalizat de încredere: evaluate -l "ko" -c 0.8

  3. Evaluare rapidă (doar bazată pe reguli): evaluate -l "ko" -f

  4. Evaluare aprofundată (doar bazată pe LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->