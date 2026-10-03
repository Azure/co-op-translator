# Depanare

Folosiți această pagină când o rulare de traducere reușește neașteptat, eșuează în timpul configurării sau produce rezultate care necesită revizuire.

## Începeți aici

1. Rulați mai întâi o comandă focalizată, de exemplu `translate -l "ko" -md`.
2. Adăugați `-d` pentru jurnale de depanare în consolă.
3. Adăugați `-s` pentru a salva jurnalele de depanare sub `<root-dir>/logs/`.
4. Rulați `co-op-review` după traducere pentru a verifica actualitatea, structura și link-urile locale.

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

- Configurați Azure OpenAI, OpenAI sau Anthropic.
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
- Sau rulați o comandă doar text, de exemplu `translate -l "ko" -md`.

### Cheie sau endpoint invalid

Simptomele pot include `401`, erori de permisiuni redactate sau erori de acces la endpoint.

Remediere:

- Confirmați că cheia aparține aceleiași resurse Azure ca endpoint-ul.
- Confirmați că resursa suportă Vision când folosiți `-img`.
- Confirmați că numele deployment-ului Azure OpenAI și versiunea API corespund implementării dvs.
- Rulați cu jurnale de depanare: `translate -l "ko" -md -d -s`.

## Niciun fișier nu a fost tradus

Cauze comune:

- Flag-urile selectate nu se potrivesc cu fișierele dvs.
- Există deja fișiere traduse.
- Fișierele sursă sunt în directoare excluse.
- Comanda rulează din rădăcina de proiect greșită.

Verificări:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Folosiți `--root-dir` când comanda este rulată în afara rădăcinii proiectului.

## Comportament neașteptat al link-urilor

Rescrierea link-urilor depinde de tipurile de conținut selectate:

- `-nb` inclus: link-urile către notebook-uri pot indica notebook-urile traduse.
- `-nb` exclus: link-urile către notebook-uri pot rămâne îndreptate către notebook-urile sursă.
- `-img` inclus: link-urile către imagini pot indica imaginile traduse.
- `-img` exclus: link-urile către imagini pot rămâne îndreptate către imaginile sursă.

Rulați o traducere completă a conținutului atunci când toate link-urile interne ar trebui să prefere rezultatele traduse:

```bash
translate -l "ko" -md -nb -img
```

Rulați revizuirea link-urilor după traducere:

```bash
co-op-review -l "ko"
```

## Probleme la redarea Markdown

Dacă Markdown-ul tradus se redă incorect:

- Verificați că frontmatter începe și se termină cu `---`.
- Verificați că numărul gardurilor de cod se potrivește între fișierele sursă și cele traduse.
- Rulați `co-op-review` pentru a detecta probleme structurale comune.
- Retraduceți fișierul specific dacă ieșirea a fost coruptă.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action a rulat, dar nu a fost creat niciun Pull Request

Dacă `peter-evans/create-pull-request` raportează că branch-ul nu este în fața bazei, workflow-ul nu a găsit fișiere de comis.

Cauze probabile:

- Rularea de traducere nu a produs modificări.
- `.gitignore` exclude `translations/`, `translated_images/` sau notebook-urile traduse.
- `add-paths` nu se potrivește cu directoarele de output generate.
- Pasul de traducere s-a oprit prematur.

Remedieri:

1. Confirmați că fișierele generate există în `translations/` sau `translated_images/`.
2. Confirmați că `.gitignore` nu ignoră output-urile generate.
3. Folosiți `add-paths` care se potrivesc:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Adăugați temporar flag-uri de depanare la comanda de traducere:

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

Traducerile automate pot necesita revizuire umană. Folosiți `evaluate` doar când doriți evaluări experimentale ale calității și fluxuri de lucru de reparare pentru încredere scăzută.

!!! warning "Experimental"
    `evaluate` poate utiliza verificări bazate pe reguli și pe LLM, iar modelul său de scor și comportamentul metadatelor se pot modifica. Nu îl includeți în gate-urile CI obligatorii decât dacă fluxul dvs. de lucru este pregătit pentru schimbări.

Pentru verificări CI deterministe, folosiți în schimb `co-op-review`.