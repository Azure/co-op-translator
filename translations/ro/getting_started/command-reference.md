<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:33:12+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "ro"
}
-->
# Referință comenzi  
CLI-ul **Co-op Translator** oferă mai multe opțiuni pentru personalizarea procesului de traducere:

Comandă                                      | Descriere  
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
translate -l "language_codes"                 | Traduce proiectul în limbile specificate. Exemplu: translate -l "es fr de" traduce în spaniolă, franceză și germană. Folosește translate -l "all" pentru a traduce în toate limbile suportate.  
translate -l "language_codes" -u              | Actualizează traducerile prin ștergerea celor existente și refacerea lor. Atenție: Aceasta va șterge toate traducerile curente pentru limbile specificate.  
translate -l "language_codes" -img            | Traduce doar fișierele imagine.  
translate -l "language_codes" -md             | Traduce doar fișierele Markdown.  
translate -l "language_codes" -chk            | Verifică fișierele traduse pentru erori și reîncearcă traducerea dacă este necesar.  
translate -l "language_codes" -d              | Activează modul debug pentru logare detaliată.  
translate -l "language_codes" -r "root_dir"   | Specifică directorul rădăcină al proiectului.  
translate -l "language_codes" -f              | Folosește modul rapid pentru traducerea imaginilor (până la de 3 ori mai rapid, cu o ușoară scădere a calității și aliniamentului).  
translate -l "language_codes" -y              | Confirmă automat toate solicitările (util pentru pipeline-uri CI/CD).  
translate -l "language_codes" --help          | Afișează detalii de ajutor în CLI cu comenzile disponibile.  

### Exemple de utilizare:

  1. Comportament implicit (adaugă traduceri noi fără a șterge pe cele existente):   translate -l "ko"    translate -l "es fr de" -r "./my_project"  

  2. Adaugă doar traduceri noi pentru imagini în coreeană (nu se șterg traducerile existente):    translate -l "ko" -img  

  3. Actualizează toate traducerile în coreeană (Atenție: Șterge toate traducerile coreene existente înainte de a retraduce):    translate -l "ko" -u  

  4. Actualizează doar imaginile în coreeană (Atenție: Șterge toate imaginile coreene existente înainte de a retraduce):    translate -l "ko" -img -u  

  5. Adaugă traduceri noi pentru Markdown în coreeană fără a afecta alte traduceri:    translate -l "ko" -md  

  6. Verifică fișierele traduse pentru erori și reîncearcă traducerile dacă este necesar: translate -l "ko" -chk  

  7. Verifică fișierele traduse pentru erori și reîncearcă traducerile (doar Markdown): translate -l "ko" -chk -md  

  8. Verifică fișierele traduse pentru erori și reîncearcă traducerile (doar imagini): translate -l "ko" -chk -img  

  9. Folosește modul rapid pentru traducerea imaginilor:    translate -l "ko" -img -f  

  10. Exemplu modul debug: - translate -l "ko" -d: Activează logarea debug.

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea în urma utilizării acestei traduceri.