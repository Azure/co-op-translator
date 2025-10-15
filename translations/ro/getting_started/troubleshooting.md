<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:57:58+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "ro"
}
-->
# Ghid de depanare Microsoft Co-op Translator

## Prezentare generală
Microsoft Co-Op Translator este un instrument puternic pentru traducerea documentelor Markdown fără efort. Acest ghid te va ajuta să rezolvi problemele comune întâlnite la utilizarea acestui instrument.

## Probleme frecvente și soluții

### 1. Problemă cu eticheta Markdown
**Problemă:** Documentul Markdown tradus conține o etichetă `markdown` în partea de sus, ceea ce cauzează probleme de afișare.

**Soluție:** Pentru a rezolva această problemă, șterge pur și simplu eticheta `markdown` din partea de sus a fișierului. Astfel, fișierul Markdown va fi afișat corect.

**Pași:**
1. Deschide fișierul Markdown (`.md`) tradus.
2. Găsește eticheta `markdown` din partea de sus a documentului.
3. Șterge eticheta `markdown`.
4. Salvează modificările.
5. Redeschide fișierul pentru a verifica dacă se afișează corect.

### 2. Problemă cu URL-ul imaginilor integrate
**Problemă:** URL-urile imaginilor integrate nu corespund cu limba documentului, ceea ce duce la imagini greșite sau lipsă.

**Soluție:** Verifică URL-ul imaginilor integrate și asigură-te că se potrivește cu limba documentului. Toate imaginile se află în folderul `translated_images`, iar fiecare imagine are un tag de limbă în numele fișierului.

**Pași:**
1. Deschide documentul Markdown tradus.
2. Identifică imaginile integrate și URL-urile acestora.
3. Verifică dacă tag-ul de limbă din numele fișierului imaginii corespunde cu limba documentului.
4. Actualizează URL-urile dacă este necesar.
5. Salvează modificările și redeschide documentul pentru a verifica dacă imaginile se afișează corect.

### 3. Acuratețea traducerii
**Problemă:** Conținutul tradus nu este corect sau necesită editări suplimentare.

**Soluție:** Revizuiește documentul tradus și fă modificările necesare pentru a îmbunătăți acuratețea și lizibilitatea.

**Pași:**
1. Deschide documentul tradus.
2. Revizuiește cu atenție conținutul.
3. Fă modificările necesare pentru a îmbunătăți traducerea.
4. Salvează modificările.

## 4. Eroare de permisiune Redacted sau 404

Dacă imaginile sau textul nu sunt traduse corect și în modul -d debug apare eroarea 401, este o problemă clasică de autentificare—cheia este invalidă, expirată sau nu este asociată cu regiunea endpoint-ului.

Rulează co-op translator cu [opțiunea -d debug](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) pentru a înțelege cauza principală.

- **Mesaj de eroare**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Cauze posibile**:
  - Cheia de abonament a fost ascunsă sau incorectă în cerere.
  - Cheia AI Services sau Subscription Key aparține unei alte resurse Azure (de exemplu Translator sau OpenAI) în loc de **Azure AI Vision**.

 **Tipul resursei**
  - Accesează [Azure Portal](https://portal.azure.com) sau [Azure AI Foundry](https://ai.azure.com) și asigură-te că resursa este de tip `Azure AI services` → `Vision`.
  - Verifică cheile și asigură-te că folosești cheia corectă.

## 5. Erori de configurare (Gestionare erori nouă)

Odată cu noul sistem de traducere selectivă, Co-op Translator oferă acum mesaje de eroare explicite când serviciile necesare nu sunt configurate.

### 5.1. Serviciul Azure AI nu este configurat pentru traducerea imaginilor

**Problemă:** Ai solicitat traducerea imaginilor (flag-ul `-img`), dar serviciul Azure AI nu este configurat corect.

**Mesaj de eroare:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Soluție:**
1. **Opțiunea 1**: Configurează serviciul Azure AI
   - Adaugă `AZURE_AI_SERVICE_API_KEY` în fișierul `.env`
   - Adaugă `AZURE_AI_SERVICE_ENDPOINT` în fișierul `.env`
   - Verifică dacă serviciul este accesibil

2. **Opțiunea 2**: Elimină cererea de traducere a imaginilor
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Configurare lipsă

**Problemă:** Configurarea LLM esențială lipsește.

**Mesaj de eroare:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Soluție:**
1. Verifică dacă fișierul `.env` conține cel puțin una dintre următoarele configurații LLM:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` și `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Ai nevoie de Azure OpenAI SAU OpenAI configurat, nu ambele.

### 5.3. Confuzie la traducerea selectivă

**Problemă:** Nu s-a tradus niciun fișier, deși comanda a fost executată cu succes.

**Cauze posibile:**
- Flag-uri greșite pentru tipul de fișier (`-md`, `-img`, `-nb`)
- Nu există fișiere potrivite în proiect
- Structură de directoare incorectă

**Soluție:**
1. **Folosește modul debug** pentru a vedea ce se întâmplă:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Verifică tipurile de fișiere** din proiect:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Verifică combinațiile de flag-uri**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migrare de la sistemul vechi

### 6.1. Modul doar Markdown a fost eliminat

**Problemă:** Comenzile care se bazau pe fallback automat doar pentru markdown nu mai funcționează ca înainte.

**Comportament vechi:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Comportament nou:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Soluție:**
- **Fii explicit** cu privire la ce vrei să traduci:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Comportament neașteptat al link-urilor

**Problemă:** Link-urile din fișierele traduse duc către locații neașteptate.

**Cauză:** Procesarea dinamică a link-urilor se schimbă în funcție de tipurile de fișiere selectate.

**Soluție:**
1. **Înțelege noul comportament al link-urilor**:
   - Dacă folosești `-nb`: Link-urile către notebook-uri duc la versiunile traduse
   - Dacă nu folosești `-nb`: Link-urile către notebook-uri duc la fișierele originale
   - Dacă folosești `-img`: Link-urile către imagini duc la versiunile traduse
   - Dacă nu folosești `-img`: Link-urile către imagini duc la fișierele originale

2. **Alege combinația potrivită** pentru nevoile tale:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. Acțiunea GitHub a rulat, dar nu s-a creat Pull Request (PR)

**Simptom:** Logurile workflow-ului pentru `peter-evans/create-pull-request` arată:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Cauze probabile:**
- **Nu s-au detectat modificări:** Pasul de traducere nu a produs diferențe (repo-ul este deja actualizat).
- **Output-uri ignorate:** `.gitignore` exclude fișierele pe care vrei să le comiți (de exemplu, `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths nu se potrivește:** Căile furnizate acțiunii nu corespund cu locațiile reale ale output-urilor.
- **Logica/condițiile workflow-ului:** Pasul de traducere s-a oprit devreme sau a scris în directoare neașteptate.

**Cum să verifici / să rezolvi:**
1. **Confirmă existența output-urilor:** După traducere, verifică dacă workspace-ul conține fișiere noi/modificate în `translations/` și/sau `translated_images/`.
   - Dacă traduci notebook-uri, asigură-te că fișierele `.ipynb` sunt scrise sub `translations/<lang>/...`.
2. **Verifică `.gitignore`:** Nu ignora output-urile generate. Asigură-te că NU ignori:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (dacă traduci notebook-uri)
3. **Asigură-te că add-paths se potrivește cu output-urile:** Folosește o valoare pe mai multe linii și include ambele foldere dacă este cazul:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Forțează un PR pentru debugging:** Permite temporar commit-uri goale pentru a verifica dacă totul este conectat corect:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Rulează cu debug:** Adaugă `-d` la comanda de traducere pentru a vedea ce fișiere au fost descoperite și scrise.
6. **Permisiuni (GITHUB_TOKEN):** Asigură-te că workflow-ul are permisiuni de scriere pentru a crea commit-uri și PR-uri:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Listă rapidă de verificare pentru depanare

Când rezolvi probleme de traducere:

1. **Folosește modul debug**: Adaugă flag-ul `-d` pentru loguri detaliate
2. **Verifică flag-urile**: Asigură-te că `-md`, `-img`, `-nb` corespund intenției tale
3. **Verifică configurația**: Asigură-te că fișierul `.env` conține cheile necesare
4. **Testează incremental**: Începe cu doar `-md`, apoi adaugă celelalte tipuri
5. **Verifică structura fișierelor**: Asigură-te că fișierele sursă există și sunt accesibile

Pentru mai multe detalii despre comenzile și flag-urile disponibile, vezi [Command Reference](./command-reference.md).

---

**Declarație de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm răspunderea pentru orice neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.