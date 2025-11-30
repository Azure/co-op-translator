<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:57:29+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "ro"
}
-->
# Referință comenzi

CLI-ul **Co-op Translator** oferă mai multe opțiuni pentru a personaliza procesul de traducere:

Comandă                                       | Descriere
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "coduri_limbă"                   | Traduce proiectul în limbile specificate. Exemplu: translate -l "es fr de" traduce în spaniolă, franceză și germană. Folosește translate -l "all" pentru a traduce în toate limbile suportate.
translate -l "coduri_limbă" -u                | Actualizează traducerile prin ștergerea celor existente și recrearea lor. Atenție: Aceasta va șterge toate traducerile curente pentru limbile specificate.
translate -l "coduri_limbă" -img              | Traduce doar fișierele imagine.
translate -l "coduri_limbă" -md               | Traduce doar fișierele Markdown.
translate -l "coduri_limbă" -nb               | Traduce doar fișierele Jupyter notebook (.ipynb).
translate -l "coduri_limbă" --fix             | Retraduce fișierele cu scoruri de încredere scăzute pe baza rezultatelor evaluărilor anterioare.
translate -l "coduri_limbă" -d                | Activează modul de depanare pentru logare detaliată.
translate -l "coduri_limbă" --save-logs, -s   | Salvează logurile de nivel DEBUG în fișiere sub <root_dir>/logs/ (consola rămâne controlată de -d)
translate -l "coduri_limbă" -r "root_dir"     | Specifică directorul rădăcină al proiectului
translate -l "coduri_limbă" -f                | Folosește modul rapid pentru traducerea imaginilor (până la 3x mai rapid, cu un mic compromis la calitate și aliniere).
translate -l "coduri_limbă" -y                | Confirmă automat toate solicitările (util pentru pipeline-uri CI/CD)
translate -l "coduri_limbă" --help            | Detalii de ajutor în CLI cu comenzile disponibile
evaluate -l "cod_limbă"                       | Evaluează calitatea traducerii pentru o limbă specifică și oferă scoruri de încredere
evaluate -l "cod_limbă" -c 0.8                | Evaluează traducerile cu un prag de încredere personalizat
evaluate -l "cod_limbă" -f                    | Mod de evaluare rapidă (doar pe reguli, fără LLM)
evaluate -l "cod_limbă" -D                    | Mod de evaluare profundă (doar pe bază de LLM, mai amănunțit dar mai lent)
evaluate -l "cod_limbă" --save-logs, -s       | Salvează logurile de nivel DEBUG în fișiere sub <root_dir>/logs/
migrate-links -l "coduri_limbă"               | Reprocesează fișierele Markdown traduse pentru a actualiza linkurile către notebook-uri (.ipynb). Preferă notebook-urile traduse când sunt disponibile; altfel poate folosi notebook-urile originale.
migrate-links -l "coduri_limbă" -r            | Specifică directorul rădăcină al proiectului (implicit: directorul curent).
migrate-links -l "coduri_limbă" --dry-run     | Afișează ce fișiere s-ar schimba fără a scrie modificările.
migrate-links -l "coduri_limbă" --no-fallback-to-original | Nu rescrie linkurile către notebook-urile originale când lipsesc cele traduse (actualizează doar când există traducere).
migrate-links -l "coduri_limbă" -d            | Activează modul de depanare pentru logare detaliată.
migrate-links -l "coduri_limbă" --save-logs, -s | Salvează logurile de nivel DEBUG în fișiere sub <root_dir>/logs/
migrate-links -l "all" -y                      | Procesează toate limbile și confirmă automat avertismentul.

## Exemple de utilizare

  1. Comportament implicit (adaugă traduceri noi fără a le șterge pe cele existente):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Adaugă doar traduceri noi pentru imagini în coreeană (fără a șterge traducerile existente):    translate -l "ko" -img

  3. Actualizează toate traducerile în coreeană (Atenție: Aceasta șterge toate traducerile coreene existente înainte de retraducere):    translate -l "ko" -u

  4. Actualizează doar imaginile în coreeană (Atenție: Aceasta șterge toate imaginile coreene existente înainte de retraducere):    translate -l "ko" -img -u

  5. Adaugă traduceri noi pentru fișiere Markdown în coreeană fără a afecta alte traduceri:    translate -l "ko" -md

  6. Repară traducerile cu scor de încredere scăzut pe baza rezultatelor evaluărilor anterioare: translate -l "ko" --fix

  7. Repară traducerile cu scor de încredere scăzut doar pentru anumite fișiere (markdown): translate -l "ko" --fix -md

  8. Repară traducerile cu scor de încredere scăzut doar pentru anumite fișiere (imagini): translate -l "ko" --fix -img

  9. Folosește modul rapid pentru traducerea imaginilor:    translate -l "ko" -img -f

  10. Repară traducerile cu scor de încredere scăzut cu un prag personalizat: translate -l "ko" --fix -c 0.8

  11. Exemplu mod debug: - translate -l "ko" -d: Activează logarea de depanare.
  12. Salvează logurile în fișiere: translate -l "ko" -s
  13. DEBUG în consolă și fișier: translate -l "ko" -d -s

  14. Migrează linkurile către notebook-uri pentru traducerile coreene (actualizează linkurile către notebook-urile traduse când sunt disponibile):    migrate-links -l "ko"

  15. Migrează linkurile cu dry-run (fără scrierea fișierelor):    migrate-links -l "ko" --dry-run

  16. Actualizează linkurile doar când există notebook-uri traduse (nu folosi originalele):    migrate-links -l "ko" --no-fallback-to-original

  17. Procesează toate limbile cu confirmare:    migrate-links -l "all"

  18. Procesează toate limbile și confirmă automat:    migrate-links -l "all" -y
  19. Salvează logurile în fișiere pentru migrate-links:    migrate-links -l "ko ja" -s

### Exemple de evaluare

> [!WARNING]  
> **Funcționalitate Beta**: Funcția de evaluare este momentan în stadiu beta. Această funcție a fost lansată pentru a evalua documentele traduse, iar metodele de evaluare și implementarea detaliată sunt încă în dezvoltare și pot suferi modificări.

  1. Evaluează traducerile în coreeană: evaluate -l "ko"

  2. Evaluează cu un prag de încredere personalizat: evaluate -l "ko" -c 0.8

  3. Evaluare rapidă (doar pe reguli): evaluate -l "ko" -f

  4. Evaluare profundă (doar pe bază de LLM): evaluate -l "ko" -D

---

**Declarație de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională umană. Nu ne asumăm răspunderea pentru orice neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.