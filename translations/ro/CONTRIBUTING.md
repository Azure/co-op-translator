<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:42:38+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ro"
}
-->
# Contribuția la Co-op Translator

Acest proiect primește cu plăcere contribuții și sugestii. Majoritatea contribuțiilor necesită să fiți de acord cu un Acord de Licență pentru Contribuitori (CLA) care declară că aveți dreptul și efectiv ne acordați drepturile de a folosi contribuția dumneavoastră. Pentru detalii, vizitați https://cla.opensource.microsoft.com.

Când trimiteți un pull request, un bot CLA va determina automat dacă trebuie să furnizați un CLA și va marca PR-ul corespunzător (de ex., verificare stare, comentariu). Urmați pur și simplu instrucțiunile oferite de bot. Trebuie să faceți acest lucru o singură dată pentru toate depozitele care folosesc CLA-ul nostru.

## Configurarea mediului de dezvoltare

Pentru a configura mediul de dezvoltare pentru acest proiect, recomandăm folosirea Poetry pentru gestionarea dependențelor. Folosim `pyproject.toml` pentru gestionarea dependențelor proiectului, așadar, pentru instalarea dependențelor, ar trebui să folosiți Poetry.

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

Înainte de a trimite un PR, este important să testați funcționalitatea traducerii cu documentație reală:

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

5. Verificați fișierele traduse în `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`.
1. Completați variabilele de mediu conform indicațiilor.

> [!TIP]
>
> ### Opțiuni suplimentare pentru mediul de dezvoltare
>
> Pe lângă rularea proiectului local, puteți folosi și GitHub Codespaces sau VS Code Dev Containers pentru o configurare alternativă a mediului de dezvoltare.
>
> #### GitHub Codespaces
>
> Puteți rula aceste exemple virtual folosind GitHub Codespaces fără setări sau configurări suplimentare.
>
> Butonul va deschide o instanță VS Code bazată pe web în browserul dvs.:
>
> 1. Deschideți șablonul (poate dura câteva minute):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Rulare locală folosind VS Code Dev Containers
>
> ⚠️ Această opțiune funcționează doar dacă Docker Desktop are alocați cel puțin 16 GB RAM. Dacă aveți mai puțin de 16 GB RAM, puteți încerca opțiunea [GitHub Codespaces](../..) sau [configurați local](../..).
>
> O opțiune asociată este VS Code Dev Containers, care va deschide proiectul în VS Code local folosind [extensia Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Porniți Docker Desktop (instalați-l dacă nu este deja instalat)
> 2. Deschideți proiectul:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Stilul codului

Folosim [Black](https://github.com/psf/black) ca formatter pentru codul Python pentru a menține un stil consistent pe tot proiectul. Black este un formatter strict care reformatează automat codul Python pentru a respecta stilul Black.

#### Configurare

Configurarea Black este specificată în `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Instalarea Black

Puteți instala Black folosind fie Poetry (recomandat), fie pip:

##### Folosind Poetry

Black se instalează automat când configurați mediul de dezvoltare:
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
> Recomandăm să configurați editorul pentru a formata automat codul cu Black la salvare. Majoritatea editorilor moderni suportă asta prin extensii sau pluginuri.

## Rularea Co-op Translator

Pentru a rula Co-op Translator folosind Poetry în mediul dvs., urmați acești pași:

1. Navigați la directorul unde doriți să efectuați testele de traducere sau creați un folder temporar pentru teste.

2. Executați comanda de mai jos. Flag-ul `-l ko` with the language code you wish to translate into. The `-d` indică modul debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Asigurați-vă că mediul Poetry este activat (poetry shell) înainte de a rula comanda.

## Maintainers

### Mesajul commit-ului și strategia de merge

Pentru a asigura consistența și claritatea în istoricul commit-urilor proiectului nostru, urmăm un format specific pentru mesajele de commit **pentru mesajul final de commit** când folosim strategia **Squash and Merge**.

Când un pull request (PR) este fuzionat, commit-urile individuale vor fi combinate într-un singur commit. Mesajul final de commit trebuie să urmeze formatul de mai jos pentru a menține un istoric curat și consistent.

#### Formatul mesajului de commit (pentru squash and merge)

Folosim următorul format pentru mesajele de commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Specifică categoria commit-ului. Folosim următoarele tipuri:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Actualizare instrucțiuni de instalare pentru claritate (#50)`
- `Core: Îmbunătățire manipulare traducere imagini (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `corectare typo`
- `actualizare README`
- `ajustare format`

They should be squashed into:
`Docs: Îmbunătățire claritate și format documentație (#65)`

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să țineți cont că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.