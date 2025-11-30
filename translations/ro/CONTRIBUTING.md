<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T12:16:42+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ro"
}
-->
# Contribuții la Co-op Translator

Acest proiect primește cu plăcere contribuții și sugestii. Majoritatea contribuțiilor necesită să fiți de acord cu un Acord de Licență pentru Contribuitori (CLA) prin care declarați că aveți dreptul și efectiv ne acordați drepturile de a folosi contribuția dvs. Pentru detalii, vizitați https://cla.opensource.microsoft.com.

Când trimiteți un pull request, un bot CLA va determina automat dacă trebuie să furnizați un CLA și va marca PR-ul corespunzător (de exemplu, verificare de stare, comentariu). Urmați pur și simplu instrucțiunile oferite de bot. Va trebui să faceți acest lucru o singură dată pentru toate repo-urile care folosesc CLA-ul nostru.

## Configurarea mediului de dezvoltare

Pentru a configura mediul de dezvoltare pentru acest proiect, recomandăm folosirea Poetry pentru gestionarea dependențelor. Folosim `pyproject.toml` pentru gestionarea dependențelor proiectului, așadar pentru instalarea dependențelor ar trebui să folosiți Poetry.

### Crearea unui mediu virtual

#### Folosind pip

```bash
python -m venv .venv
```

#### Folosind Poetry

```bash
poetry init
```

### Activarea mediului virtual

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

Înainte de a trimite un PR, este important să testați funcționalitatea de traducere cu documentație reală:

1. Creați un director de test în directorul rădăcină:
    ```bash
    mkdir test_docs
    ```

2. Copiați în directorul de test documentația markdown și imaginile pe care doriți să le traduceți. De exemplu:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Instalați pachetul local:
    ```bash
    pip install -e .
    ```

4. Rulați Co-op Translator pe documentele de test:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Verificați fișierele traduse din `test_docs/translations` și `test_docs/translated_images` pentru a confirma:
   - Calitatea traducerii
   - Comentariile de metadate sunt corecte
   - Structura originală markdown este păstrată
   - Linkurile și imaginile funcționează corect

Această testare manuală ajută să vă asigurați că modificările dvs. funcționează bine în scenarii reale.

### Variabile de mediu

1. Creați un fișier `.env` în directorul rădăcină copiat din fișierul `.env.template` furnizat.
1. Completați variabilele de mediu conform indicațiilor.

> [!TIP]
>
> ### Opțiuni suplimentare pentru mediul de dezvoltare
>
> Pe lângă rularea proiectului local, puteți folosi și GitHub Codespaces sau VS Code Dev Containers pentru o configurare alternativă a mediului de dezvoltare.
>
> #### GitHub Codespaces
>
> Puteți rula aceste exemple virtual folosind GitHub Codespaces, fără setări sau configurări suplimentare.
>
> Butonul va deschide o instanță VS Code bazată pe web în browserul dvs.:
>
> 1. Deschideți șablonul (poate dura câteva minute):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Rulare locală folosind VS Code Dev Containers
>
> ⚠️ Această opțiune funcționează doar dacă Docker Desktop are alocați cel puțin 16 GB RAM. Dacă aveți mai puțin de 16 GB RAM, puteți încerca opțiunea [GitHub Codespaces](../..) sau [configurarea locală](../..).
>
> O opțiune conexă este VS Code Dev Containers, care va deschide proiectul în VS Code local folosind [extensia Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Porniți Docker Desktop (instalați-l dacă nu este deja instalat)
> 2. Deschideți proiectul:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Stilul codului

Folosim [Black](https://github.com/psf/black) ca formatter pentru cod Python pentru a menține un stil consistent în tot proiectul. Black este un formatter strict care reformatează automat codul Python pentru a respecta stilul Black.

#### Configurare

Configurația Black este specificată în `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Instalarea Black

Puteți instala Black folosind fie Poetry (recomandat), fie pip:

##### Folosind Poetry

Black este instalat automat când configurați mediul de dezvoltare:
```bash
poetry install
```

##### Folosind pip

Dacă folosiți pip, puteți instala Black direct:
```bash
pip install black
```

#### Folosirea Black

##### Cu Poetry

1. Formatați toate fișierele Python din proiect:
    ```bash
    poetry run black .
    ```

2. Formatați un fișier sau director specific:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Cu pip

1. Formatați toate fișierele Python din proiect:
    ```bash
    black .
    ```

2. Formatați un fișier sau director specific:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Vă recomandăm să configurați editorul să formateze automat codul cu Black la salvare. Majoritatea editorilor moderni suportă asta prin extensii sau pluginuri.

## Rularea Co-op Translator

Pentru a rula Co-op Translator folosind Poetry în mediul dvs., urmați pașii:

1. Navigați în directorul unde doriți să faceți teste de traducere sau creați un folder temporar pentru testare.

2. Executați comanda următoare. Înlocuiți `-l ko` cu codul limbii în care doriți să traduceți. Flag-ul `-d` indică modul debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Asigurați-vă că mediul Poetry este activat (poetry shell) înainte de a rula comanda.

## Contribuiți cu o limbă nouă

Primim cu plăcere contribuții care adaugă suport pentru limbi noi. Înainte de a deschide un PR, vă rugăm să parcurgeți pașii de mai jos pentru a asigura o revizuire fără probleme.

1. Adăugați limba în maparea fonturilor
   - Editați `src/co_op_translator/fonts/font_language_mappings.yml`
   - Adăugați o intrare cu:
     - `code`: codul limbii în stil ISO (ex: `vi`)
     - `name`: numele afișat prietenos
     - `font`: un font livrat în `src/co_op_translator/fonts/` care suportă scriptul
     - `rtl`: `true` dacă este scris de la dreapta la stânga, altfel `false`

2. Includeți fișierele de font necesare (dacă este cazul)
   - Dacă este nevoie de un font nou, verificați compatibilitatea licenței pentru distribuție open source
   - Adăugați fișierul font în `src/co_op_translator/fonts/`

3. Verificare locală
   - Rulați traduceri pentru un eșantion mic (Markdown, imagini și notebook-uri după caz)
   - Verificați dacă rezultatul se afișează corect, inclusiv fonturile și orice layout RTL dacă este cazul

4. Actualizați documentația
   - Asigurați-vă că limba apare în `getting_started/supported-languages.md`
   - Nu sunt necesare modificări în `getting_started/README_languages_template.md`; acesta este generat din lista de limbi suportate

5. Deschideți un PR
   - Descrieți limba adăugată și orice considerente legate de font/licență
   - Atașați capturi de ecran cu rezultatele afișate, dacă este posibil

Exemplu de intrare YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Testați limba nouă

Puteți testa limba nouă rulând comanda următoare:

```bash
# Creează și activează un mediu virtual
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Instalează pachetul de dezvoltare
pip install -e .
# Rulează traducerea
translate -l "new_lang"
```

## Menținători

### Mesajul commit-ului și strategia de merge

Pentru a asigura consistență și claritate în istoricul commit-urilor proiectului, urmăm un format specific pentru mesajul commit-ului **pentru mesajul final** când folosim strategia **Squash and Merge**.

Când un pull request (PR) este integrat, commit-urile individuale vor fi combinate într-un singur commit. Mesajul final al commit-ului trebuie să urmeze formatul de mai jos pentru a menține un istoric curat și consistent.

#### Formatul mesajului commit (pentru squash and merge)

Folosim următorul format pentru mesajele commit-urilor:

```bash
<type>: <description> (#<număr PR>)
```

- **type**: Specifică categoria commit-ului. Folosim următoarele tipuri:
  - `Docs`: pentru actualizări de documentație.
  - `Build`: pentru modificări legate de sistemul de build sau dependențe, inclusiv actualizări ale fișierelor de configurare, workflow-uri CI sau Dockerfile.
  - `Core`: pentru modificări ale funcționalității sau caracteristicilor de bază ale proiectului, în special cele care implică fișiere din directorul `src/co_op_translator/core`.

- **description**: Un rezumat concis al modificării.
- **PR number**: Numărul pull request-ului asociat commit-ului.

**Exemple**:

- `Docs: Actualizare instrucțiuni de instalare pentru claritate (#50)`
- `Core: Îmbunătățire gestionare traducere imagini (#60)`

> [!NOTE]
> În prezent, prefixele **`Docs`**, **`Core`** și **`Build`** sunt adăugate automat la titlurile PR-urilor pe baza etichetelor aplicate codului sursă modificat. Atâta timp cât eticheta corectă este aplicată, de obicei nu trebuie să modificați manual titlul PR-ului. Trebuie doar să verificați că totul este corect și prefixul a fost generat corespunzător.

#### Strategia de merge

Folosim **Squash and Merge** ca strategie implicită pentru pull request-uri. Această strategie asigură că mesajele commit-urilor respectă formatul nostru, chiar dacă commit-urile individuale nu o fac.

**Motive**:

- Istoric curat și liniar al proiectului.
- Consistență în mesajele commit-urilor.
- Reducerea zgomotului cauzat de commit-uri minore (ex: „fix typo”).

La integrare, asigurați-vă că mesajul final al commit-ului respectă formatul descris mai sus.

**Exemplu de Squash and Merge**
Dacă un PR conține următoarele commit-uri:

- `fix typo`
- `update README`
- `adjust formatting`

Acestea trebuie combinate în:
`Docs: Îmbunătățire claritate și formatare documentație (#65)`

### Procesul de lansare

Această secțiune descrie cea mai simplă metodă pentru menținători de a publica o nouă versiune a Co-op Translator.

#### 1. Actualizați versiunea în `pyproject.toml`

1. Decideți următorul număr de versiune (urmăm semantic versioning: `MAJOR.MINOR.PATCH`).
2. Editați `pyproject.toml` și actualizați câmpul `version` din `[tool.poetry]`.
3. Deschideți un pull request dedicat care modifică doar versiunea (și orice fișiere de lock/metadate actualizate automat, dacă există).
4. După revizuire, folosiți **Squash and Merge** și asigurați-vă că mesajul final al commit-ului respectă formatul descris mai sus.

#### 2. Creați o lansare pe GitHub

1. Accesați pagina repository-ului pe GitHub și deschideți **Releases** → **Draft a new release**.
2. Creați un nou tag (de exemplu, `v0.13.0`) din ramura `main`.
3. Setați titlul lansării la aceeași versiune (de exemplu, `v0.13.0`).
4. Apăsați **Generate release notes** pentru a popula automat changelog-ul.
5. Opțional, editați textul (de exemplu, pentru a evidenția limbile noi suportate sau schimbări importante).
6. Publicați lansarea.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->