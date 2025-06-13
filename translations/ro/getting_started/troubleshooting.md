<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:30:40+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "ro"
}
-->
# Microsoft Co-op Translator Troubleshooting Guide


## Prezentare generală
Microsoft Co-Op Translator este un instrument puternic pentru traducerea fără probleme a documentelor Markdown. Acest ghid te va ajuta să rezolvi problemele frecvente întâlnite în utilizarea acestui instrument.

## Probleme comune și soluții

### 1. Problemă cu etichetele Markdown
**Problemă:** Documentul Markdown tradus include o etichetă `markdown` în partea de sus, cauzând probleme la redare.

**Soluție:** Pentru a rezolva acest lucru, pur și simplu șterge eticheta `markdown` din partea de sus a fișierului. Astfel, fișierul Markdown va fi redat corect.

**Pași:**
1. Deschide fișierul Markdown tradus (`.md`).
2. Găsește eticheta `markdown` din partea de sus a documentului.
3. Șterge eticheta `markdown`.
4. Salvează modificările făcute în fișier.
5. Redeschide fișierul pentru a verifica dacă se redă corect.

### 2. Problemă cu URL-urile imaginilor încorporate
**Problemă:** URL-urile imaginilor încorporate nu corespund cu localizarea limbii, ceea ce duce la imagini incorecte sau lipsă.

**Soluție:** Verifică URL-urile imaginilor încorporate și asigură-te că acestea corespund cu localizarea limbii. Toate imaginile sunt în folderul `translated_images`, fiecare imagine având o etichetă de localizare a limbii în numele fișierului.

**Pași:**
1. Deschide documentul Markdown tradus.
2. Identifică imaginile încorporate și URL-urile acestora.
3. Verifică dacă localizarea limbii din numele fișierului imaginii corespunde cu limba documentului.
4. Actualizează URL-urile dacă este necesar.
5. Salvează modificările și redeschide documentul pentru a confirma că imaginile se afișează corect.

### 3. Acuratețea traducerii
**Problemă:** Conținutul tradus nu este precis sau necesită editări suplimentare.

**Soluție:** Revizuiește documentul tradus și fă modificările necesare pentru a îmbunătăți acuratețea și lizibilitatea.

**Pași:**
1. Deschide documentul tradus.
2. Revizuiește conținutul cu atenție.
3. Fă modificările necesare pentru a îmbunătăți acuratețea traducerii.
4. Salvează modificările.

### 4. Probleme de formatare a fișierului
**Problemă:** Formatarea documentului tradus este incorectă. Aceasta poate apărea în tabele; aici un ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` suplimentar va rezolva problemele legate de tabele.

**Pași:**
1. Deschide documentul tradus.
2. Compară-l cu documentul original pentru a identifica problemele de formatare.
3. Ajustează formatarea pentru a corespunde documentului original.
4. Salvează modificările.

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere automată AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să țineți cont că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea în urma utilizării acestei traduceri.