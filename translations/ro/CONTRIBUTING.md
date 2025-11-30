<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T03:56:38+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ro"
}
-->
# Contribuie la Co-op Translator

Acest proiect acceptă contribuții și sugestii. Majoritatea contribuțiilor necesită să fii de acord cu un
Acord de Licență pentru Contribuitori (CLA) care declară că ai dreptul și chiar acorzi drepturile
de a folosi contribuția ta. Pentru detalii, vizitează https://cla.opensource.microsoft.com.

Când trimiți un pull request, un bot CLA va determina automat dacă trebuie să furnizezi
un CLA și va marca PR-ul corespunzător (de exemplu, status check, comentariu). Urmează pur și simplu instrucțiunile
oferite de bot. Trebuie să faci acest lucru o singură dată pentru toate repo-urile care folosesc CLA-ul nostru.

## Configurarea mediului de dezvoltare

Pentru a configura mediul de dezvoltare pentru acest proiect, recomandăm folosirea Poetry pentru gestionarea dependențelor. Folosim `pyproject.toml` pentru a gestiona dependențele proiectului, așa că pentru instalarea dependențelor ar trebui să folosești Poetry.

### Creează un mediu virtual

#### Folosind pip

```bash
python -m venv .venv
```

#### Folosind Poetry

```bash
poetry init
```

### Activează mediul virtual

#### Pentru pip și Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Folosind Poetry

```bash
poetry shell
```

### Instalarea pachetului și a pachetelor necesare

#### Folosind Poetry (din pyproject.toml)

```bash
poetry install
```

### Testare manuală

Înainte de a trimite un PR, este important să testezi funcționalitatea de traducere cu documentație reală:

1. Creează un director de test în directorul rădăcină:
    ```bash
    mkdir test_docs
    ```

2. Copiază câteva fișiere markdown și imagini pe care vrei să le traduci în directorul de test. De exemplu:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Instalează pachetul local:
    ```bash
    pip install -e .
    ```

4. Rulează Co-op Translator pe documentele tale de test:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Verifică fișierele traduse din `test_docs/translations` și `test_docs/translated_images` pentru a te asigura că:
   - Calitatea traducerii este bună
   - Comentariile de metadate sunt corecte
   - Structura originală a markdown-ului este păstrată
   - Link-urile și imaginile funcționează corect

Această testare manuală te ajută să te asiguri că modificările tale funcționează bine în scenarii reale.

### Variabile de mediu

1. Creează un fișier `.env` în directorul rădăcină, copiind fișierul `.env.template` furnizat.
1. Completează variabilele de mediu conform instrucțiunilor.

> [!TIP]
>
> ### Opțiuni suplimentare pentru mediul de dezvoltare
>
> Pe lângă rularea proiectului local, poți folosi și GitHub Codespaces sau VS Code Dev Containers ca alternativă pentru configurarea mediului de dezvoltare.
>
> #### GitHub Codespaces
>
> Poți rula aceste exemple virtual folosind GitHub Codespaces, fără setări sau configurări suplimentare.
>
> Butonul va deschide o instanță VS Code bazată pe web direct în browserul tău:
>
> 1. Deschide template-ul (poate dura câteva minute):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Rulare locală folosind VS Code Dev Containers
>
> ⚠️ Această opțiune funcționează doar dacă Docker Desktop are alocat cel puțin 16 GB RAM. Dacă ai mai puțin de 16 GB RAM, poți încerca opțiunea [GitHub Codespaces](../..) sau [să configurezi local](../..).
>
> O opțiune similară este VS Code Dev Containers, care va deschide proiectul în VS Code local folosind [extensia Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Pornește Docker Desktop (instalează-l dacă nu este deja instalat)
> 2. Deschide proiectul:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Stilul codului

Folosim [Black](https://github.com/psf/black) ca formatter pentru codul Python, pentru a menține un stil consistent în tot proiectul. Black este un formatter strict care reformatează automat codul Python conform stilului Black.

#### Configurare

Configurația Black este specificată în `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Instalarea Black

Poți instala Black fie cu Poetry (recomandat), fie cu pip:

##### Folosind Poetry

Black se instalează automat când configurezi mediul de dezvoltare:
```bash
poetry install
```

##### Folosind pip

Dacă folosești pip, poți instala Black direct:
```bash
pip install black
```

#### Folosirea Black

##### Cu Poetry

1. Formatează toate fișierele Python din proiect:
    ```bash
    poetry run black .
    ```

2. Formatează un fișier sau director specific:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Cu pip

1. Formatează toate fișierele Python din proiect:
    ```bash
    black .
    ```

2. Formatează un fișier sau director specific:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Îți recomandăm să configurezi editorul să formateze automat codul cu Black la salvare. Majoritatea editorilor moderne suportă acest lucru prin extensii sau plugin-uri.

## Rularea Co-op Translator

Pentru a rula Co-op Translator folosind Poetry în mediul tău, urmează pașii de mai jos:

1. Navighează în directorul unde vrei să faci teste de traducere sau creează un folder temporar pentru testare.

2. Execută următoarea comandă. Înlocuiește `-l ko` cu codul limbii în care vrei să traduci. Flag-ul `-d` activează modul debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Asigură-te că mediul Poetry este activat (poetry shell) înainte de a rula comanda.

## Contribuie cu o limbă nouă

Acceptăm contribuții care adaugă suport pentru limbi noi. Înainte de a deschide un PR, te rugăm să parcurgi pașii de mai jos pentru a facilita procesul de review.

1. Adaugă limba în maparea fonturilor
   - Editează `src/co_op_translator/fonts/font_language_mappings.yml`
   - Adaugă o intrare cu:
     - `code`: cod de limbă tip ISO (ex: `vi`)
     - `name`: denumire afișată prietenoasă
     - `font`: un font inclus în `src/co_op_translator/fonts/` care suportă scrierea respectivă
     - `rtl`: `true` dacă limba se scrie de la dreapta la stânga, altfel `false`

2. Include fișierele de font necesare (dacă este cazul)
   - Dacă este nevoie de un font nou, verifică compatibilitatea licenței pentru distribuție open source
   - Adaugă fișierul de font în `src/co_op_translator/fonts/`

3. Verificare locală
   - Rulează traduceri pentru un eșantion mic (Markdown, imagini și notebook-uri, după caz)
   - Verifică dacă rezultatul se afișează corect, inclusiv fonturile și layout-ul RTL dacă este relevant

4. Actualizează documentația
   - Asigură-te că limba apare în `getting_started/supported-languages.md`
   - Nu sunt necesare modificări la `README_languages_template.md`; acesta se generează automat din lista de limbi suportate

5. Deschide un PR
   - Descrie limba adăugată și orice detalii despre font/licență
   - Atașează capturi de ecran cu rezultatele afișate, dacă este posibil

Exemplu de intrare YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Maintaineri

### Formatul mesajului de commit și strategia de îmbinare

Pentru a asigura consistența și claritatea istoricului de commit-uri al proiectului, urmăm un format specific **pentru mesajul final de commit** când folosim strategia **Squash and Merge**.

Când un pull request (PR) este îmbinat, commit-urile individuale vor fi unite într-un singur commit. Mesajul final de commit trebuie să urmeze formatul de mai jos pentru a menține un istoric curat și consistent.

#### Formatul mesajului de commit (pentru squash and merge)

Folosim următorul format pentru mesajele de commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Specifică categoria commit-ului. Folosim următoarele tipuri:
  - `Docs`: Pentru actualizări de documentație.
  - `Build`: Pentru modificări legate de sistemul de build sau dependențe, inclusiv actualizări la fișiere de configurare, workflow-uri CI sau Dockerfile.
  - `Core`: Pentru modificări ale funcționalității de bază a proiectului, în special cele care implică fișiere din directorul `src/co_op_translator/core`.

- **description**: Un rezumat concis al modificării.
- **PR number**: Numărul pull request-ului asociat commit-ului.

**Exemple**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> În prezent, prefixurile **`Docs`**, **`Core`** și **`Build`** sunt adăugate automat la titlurile PR-urilor pe baza etichetelor aplicate codului sursă modificat. Atât timp cât eticheta corectă este aplicată, de obicei nu trebuie să actualizezi manual titlul PR-ului. Trebuie doar să verifici că totul este corect și prefixul a fost generat corespunzător.

#### Strategia de îmbinare

Folosim **Squash and Merge** ca strategie implicită pentru pull request-uri. Această strategie asigură că mesajele de commit respectă formatul nostru, chiar dacă commit-urile individuale nu o fac.

**Motive**:

- Istoric de proiect curat și liniar.
- Consistență în mesajele de commit.
- Mai puțin zgomot din commit-uri minore (ex: "fix typo").

La îmbinare, asigură-te că mesajul final de commit respectă formatul descris mai sus.

**Exemplu de Squash and Merge**
Dacă un PR conține următoarele commit-uri:

- `fix typo`
- `update README`
- `adjust formatting`

Acestea trebuie unite într-un singur commit:
`Docs: Improve documentation clarity and formatting (#65)`

---

**Declarație de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm răspunderea pentru orice neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.