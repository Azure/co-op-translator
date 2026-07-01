# Depanare

Folosiți această pagină când o rulare de traducere reușește neașteptat, eșuează în timpul configurării sau generează un rezultat care necesită revizuire.

## Începeți aici

1. Rulați mai întâi o comandă focalizată, de exemplu `translate -l "ko" -md`.
2. Adăugați `-d` pentru jurnalele de depanare în consolă.
3. Adăugați `-s` pentru a salva jurnalele de depanare în `<root-dir>/logs/`.
4. Rulați `co-op-review` după traducere pentru a verifica actualitatea, structura și linkurile locale.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Erori de configurare

### Niciun furnizor de model lingvistic

Eroare:

```text
No language model configuration found.
```

Remediere:

- Configurați Azure OpenAI sau OpenAI.
- Verificați că variabilele sunt în mediul în care rulează comanda.
- Pentru utilizare locală, puneți-le în `.env` la rădăcina proiectului.

Consultați [Configurare](configuration.md).

### Traducerea imaginilor fără Azure AI Vision

Eroare:

```text
Image translation requested but Azure AI Service is not configured.
```

Remediere:

- Adăugați `AZURE_AI_SERVICE_API_KEY`.
- Adăugați `AZURE_AI_SERVICE_ENDPOINT`.
- Sau rulați o comandă doar pentru text, cum ar fi `translate -l "ko" -md`.

### Cheie sau endpoint invalid

Simptomele pot include `401`, erori de permisiuni redactate sau erori de acces la endpoint.

Remediere:

- Confirmați că cheia aparține aceleiași resurse Azure ca și endpointul.
- Confirmați că resursa suportă Vision atunci când folosiți `-img`.
- Confirmați că numele implementării Azure OpenAI și versiunea API se potrivesc cu implementarea dvs.
- Rulați cu jurnale de depanare: `translate -l "ko" -md -d -s`.

## Nu s-au tradus fișiere

Cauze comune:

- Flag-urile selectate nu corespund fișierelor dvs.
- Există deja fișiere traduse.
- Fișierele sursă sunt în directoare excluse.
- Comanda rulează din directorul rădăcină greșit al proiectului.

Verificări:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Folosiți `--root-dir` când comanda este rulată în afara rădăcinii proiectului.

## Comportament neașteptat al linkurilor

Rescrierea linkurilor depinde de tipurile de conținut selectate:

- `-nb` inclus: linkurile către notebook pot indica către notebook-urile traduse.
- `-nb` exclus: linkurile către notebook pot rămâne îndreptate către notebook-urile sursă.
- `-img` inclus: linkurile către imagini pot indica către imaginile traduse.
- `-img` exclus: linkurile către imagini pot rămâne îndreptate către imaginile sursă.

Rulați o traducere completă a conținutului când toate linkurile interne ar trebui să prefere rezultatele traduse:

```bash
translate -l "ko" -md -nb -img
```

Rulați revizuirea linkurilor după traducere:

```bash
co-op-review -l "ko"
```

## Probleme de redare Markdown

Dacă Markdown-ul tradus se redă incorect:

- Verificați că frontmatter-ul începe și se termină cu `---`.
- Verificați că numărul delimitatorilor pentru blocurile de cod se potrivește între fișierele sursă și cele traduse.
- Rulați `co-op-review` pentru a detecta problemele comune de structură.
- Retraduceți fișierul specific dacă ieșirea a fost coruptă.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action a rulat, dar nu a fost creat niciun Pull Request

Dacă `peter-evans/create-pull-request` raportează că ramura nu este înaintea bazei, workflow-ul nu a găsit fișiere de comis.

Cauze probabile:

- Rularea de traducere nu a produs modificări.
- `.gitignore` exclude `translations/`, `translated_images/` sau notebook-urile traduse.
- `add-paths` nu corespunde directoarelor de ieșire generate.
- Pasul de traducere s-a încheiat prematur.

Soluții:

1. Confirmați că fișierele generate există în `translations/` sau `translated_images/`.
2. Confirmați că `.gitignore` nu ignoră ieșirile generate.
3. Folosiți `add-paths` care se potrivesc:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Adăugați temporar flag-urile de depanare la comanda de traducere:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Confirmați că permisiunile workflow-ului includ:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Calitatea traducerii

Traducerile automate pot necesita revizuire umană. Folosiți `evaluate` doar când doriți evaluări de calitate experimentale și fluxuri de lucru de reparare pentru cazuri cu încredere scăzută.

!!! warning "Experimental"
    `evaluate` poate folosi verificări bazate pe reguli și verificări bazate pe LLM, iar modelul său de scoring și comportamentul metadatelor se pot schimba. Nu îl includeți în porțile CI obligatorii decât dacă fluxul dvs. de lucru este pregătit pentru schimbări.

Pentru verificări CI deterministe, folosiți în schimb `co-op-review`.