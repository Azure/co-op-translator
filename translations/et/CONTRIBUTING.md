<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T13:00:19+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "et"
}
-->
# Panustamine Co-op Translatori

See projekt ootab panuseid ja ettepanekuid. Enamik panustest nõuab, et nõustuksite
panustaja litsentsilepinguga (CLA), mis kinnitab, et teil on õigus ja te annate meile
õiguse kasutada teie panust. Lisateabe saamiseks külastage https://cla.opensource.microsoft.com.

Kui esitate pull requesti, määrab CLA bot automaatselt, kas peate esitama
CLA ja märgistab PR-i vastavalt (nt olekukontroll, kommentaar). Järgige lihtsalt boti juhiseid.
Seda tuleb teha ainult üks kord kõigis meie CLA-d kasutavates hoidlates.

## Arenduskeskkonna seadistamine

Selle projekti arenduskeskkonna seadistamiseks soovitame kasutada Poetryt sõltuvuste haldamiseks. Me kasutame `pyproject.toml` projekti sõltuvuste haldamiseks, seega tuleks sõltuvuste paigaldamiseks kasutada Poetryt.

### Virtuaalkeskkonna loomine

#### Pipiga

```bash
python -m venv .venv
```

#### Poetryga

```bash
poetry init
```

### Virtuaalkeskkonna aktiveerimine

#### Pipiga ja Poetryga

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetryga

```bash
poetry shell
```

### Paketi ja vajalike pakettide paigaldamine

#### Poetryga (pyproject.toml-ist)

```bash
poetry install
```

### Käsitsi testimine

Enne PR-i esitamist on oluline testida tõlke funktsionaalsust reaalse dokumentatsiooniga:

1. Loo juurkataloogi testkaust:
    ```bash
    mkdir test_docs
    ```

2. Kopeeri testkausta mõned tõlgitavad markdown-dokumendid ja pildid. Näiteks:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Paigalda pakett lokaalselt:
    ```bash
    pip install -e .
    ```

4. Käivita Co-op Translator oma testdokumentidel:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Kontrolli tõlgitud faile kaustades `test_docs/translations` ja `test_docs/translated_images`, et veenduda:
   - Tõlke kvaliteedis
   - Metaandmete kommentaaride õigsuses
   - Originaalse markdowni struktuuri säilimises
   - Linkide ja piltide korrektses toimimises

See käsitsi testimine aitab tagada, et teie muudatused töötavad hästi reaalses kasutuses.

### Keskkonnamuutujad

1. Loo juurkataloogi `.env` fail, kopeerides olemasoleva `.env.template` faili.
1. Täida keskkonnamuutujad vastavalt juhistele.

> [!TIP]
>
> ### Täiendavad arenduskeskkonna valikud
>
> Lisaks projekti lokaalsele käivitamisele võite kasutada ka GitHub Codespaces või VS Code Dev Containers alternatiivse arenduskeskkonna seadistamiseks.
>
> #### GitHub Codespaces
>
> Seda näidist saab käivitada virtuaalselt GitHub Codespaces abil, ilma täiendavate seadistusteta.
>
> Nupp avab veebipõhise VS Code'i brauseris:
>
> 1. Ava mall (see võib võtta mitu minutit):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Lokaalne käivitamine VS Code Dev Containers abil
>
> ⚠️ See valik töötab ainult siis, kui teie Docker Desktopil on vähemalt 16 GB RAM-i. Kui teil on vähem kui 16 GB RAM-i, võite proovida [GitHub Codespaces valikut](../..) või [seadistada lokaalselt](../..).
>
> Seotud valik on VS Code Dev Containers, mis avab projekti teie lokaalses VS Code'is, kasutades [Dev Containers laiendust](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Käivita Docker Desktop (paigalda, kui pole veel paigaldatud)
> 2. Ava projekt:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Koodistiil

Kasutame [Black](https://github.com/psf/black) Python-koodi vormindajana, et hoida kogu projektis ühtset stiili. Black on kompromissitu vormindaja, mis automaatselt vormindab Python-koodi vastavalt Black stiilile.

#### Konfiguratsioon

Black konfiguratsioon on määratud meie `pyproject.toml` failis:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Blacki paigaldamine

Blacki saab paigaldada kas Poetry (soovitatav) või pip abil:

##### Poetryga

Black paigaldatakse automaatselt arenduskeskkonna seadistamisel:
```bash
poetry install
```

##### Pipiga

Kui kasutate pipi, saate Blacki otse paigaldada:
```bash
pip install black
```

#### Blacki kasutamine

##### Poetryga

1. Vorminda kõik projekti Python-failid:
    ```bash
    poetry run black .
    ```

2. Vorminda konkreetne fail või kataloog:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Pipiga

1. Vorminda kõik projekti Python-failid:
    ```bash
    black .
    ```

2. Vorminda konkreetne fail või kataloog:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Soovitame seadistada oma koodiredaktori automaatselt vormindama koodi Blackiga salvestamisel. Enamik kaasaegseid redaktoreid toetab seda laienduste või pluginatega.

## Co-op Translatori käivitamine

Co-op Translatori käivitamiseks Poetry abil oma keskkonnas toimige järgmiselt:

1. Liikuge kataloogi, kus soovite tõlketeste teha, või looge ajutine kaust testimiseks.

2. Käivitage järgmine käsk. Asendage `-l ko` soovitud sihtkeele koodiga. Lipp `-d` tähendab silumisrežiimi.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Veenduge, et teie Poetry keskkond on aktiveeritud (poetry shell) enne käsu käivitamist.

## Uue keele lisamine

Ootame panuseid, mis lisavad tuge uutele keeltele. Enne PR-i avamist järgige alltoodud samme sujuvaks ülevaatuseks.

1. Lisage keel fontide kaardistusse
   - Muutke faili `src/co_op_translator/fonts/font_language_mappings.yml`
   - Lisage kirje, mis sisaldab:
     - `code`: ISO-laadne keelekood (nt `vi`)
     - `name`: Inimloetav kuvatav nimi
     - `font`: Font, mis on kaasas kaustas `src/co_op_translator/fonts/` ja toetab skripti
     - `rtl`: `true`, kui keel on paremalt vasakule, muul juhul `false`

2. Lisage vajalikud fontfailid (kui vaja)
   - Kui on vaja uut fonti, kontrollige litsentsi ühilduvust avatud lähtekoodi levitamiseks
   - Lisage fontfail kausta `src/co_op_translator/fonts/`

3. Kohalik kontroll
   - Käivitage tõlked väikese näidisega (Markdown, pildid ja märkmikud vastavalt vajadusele)
   - Kontrollige, et väljund kuvatakse õigesti, sealhulgas fondid ja vajadusel RTL paigutus

4. Uuendage dokumentatsiooni
   - Veenduge, et keel on kirjas failis `getting_started/supported-languages.md`
   - Faili `getting_started/README_languages_template.md` muutma ei pea; see genereeritakse toetatud keelte nimekirjast

5. Avage PR
   - Kirjeldage lisatud keelt ja kõiki fontide/litsentsi eripärasid
   - Lisage võimalusel kuvatõmmised renderdatud väljunditest

Näidis YAML kirje:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Uue keele testimine

Uue keele testimiseks käivitage järgmine käsk:

```bash
# Loo ja aktiveeri virtuaalne keskkond
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Paigalda arenduspakett
pip install -e .
# Käivita tõlge
translate -l "new_lang"
```

## Hooldajad

### Commit-sõnum ja ühendamise strateegia

Selleks, et tagada meie projekti commit-ajaloos järjepidevus ja selgus, järgime kindlat commit-sõnumi vormingut **lõpliku commit-sõnumi** puhul, kui kasutame **Squash and Merge** strateegiat.

Kui pull request (PR) ühendatakse, surutakse kõik commitid üheks kokku. Lõplik commit-sõnum peaks järgima alltoodud vormingut, et hoida ajalugu puhtana ja ühtsena.

#### Commit-sõnumi vorming (squash and merge jaoks)

Kasutame commit-sõnumite jaoks järgmist vormingut:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Määrab commit'i kategooria. Kasutame järgmisi tüüpe:
  - `Docs`: Dokumentatsiooni uuendused.
  - `Build`: Muudatused build-süsteemis või sõltuvustes, sh konfiguratsioonifailide, CI töövoogude või Dockerfile uuendused.
  - `Core`: Muudatused projekti põhifunktsionaalsuses või -omadustes, eriti failides `src/co_op_translator/core` kataloogis.

- **description**: Lühike muudatuse kokkuvõte.
- **PR number**: Pull requesti number, millega commit on seotud.

**Näited**:

- `Docs: Täpsusta paigaldusjuhiseid (#50)`
- `Core: Paranda piltide tõlkimise käsitlemist (#60)`

> [!NOTE]
> Praegu lisatakse **`Docs`**, **`Core`** ja **`Build`** eesliited automaatselt PR pealkirjale vastavalt muudetud lähtekoodi siltidele. Kui õige silt on olemas, ei pea te tavaliselt PR pealkirja käsitsi muutma. Piisab, kui kontrollite, et kõik on õige ja eesliide on korrektselt genereeritud.

#### Ühendamise strateegia

Kasutame vaikimisi pull requestide ühendamiseks **Squash and Merge** strateegiat. See tagab, et commit-sõnumid järgivad meie vormingut, isegi kui üksikud commitid seda ei tee.

**Põhjused**:

- Puhtam, lineaarne projekti ajalugu.
- Järjepidevus commit-sõnumites.
- Vähem müra väikestest commitidest (nt "paranda kirjaviga").

Ühendamisel veenduge, et lõplik commit-sõnum järgib eespool kirjeldatud vormingut.

**Näide Squash and Merge'ist**
Kui PR sisaldab järgmisi commit'e:

- `fix typo`
- `update README`
- `adjust formatting`

Siis surutakse need kokku kujule:
`Docs: Paranda dokumentatsiooni selgust ja vormindust (#65)`

### Väljalaske protsess

See jaotis kirjeldab lihtsaimat viisi, kuidas hooldajad saavad avaldada Co-op Translatori uue versiooni.

#### 1. Versiooni tõstmine `pyproject.toml` failis

1. Otsustage järgmise versiooni number (järgime semantilist versioonimist: `MAJOR.MINOR.PATCH`).
2. Muutke `pyproject.toml` faili ja uuendage `[tool.poetry]` all olevat `version` välja.
3. Avage spetsiaalne pull request, mis muudab ainult versiooni (ja automaatselt uuendatud lukustus-/metaandmefaile, kui neid on).
4. Pärast ülevaatust kasutage **Squash and Merge** ja veenduge, et lõplik commit-sõnum järgib eelnevalt kirjeldatud vormingut.

#### 2. GitHub Release'i loomine

1. Minge GitHubi hoidla lehele ja avage **Releases** → **Draft a new release**.
2. Looge uus silt (näiteks `v0.13.0`) harust `main`.
3. Määrake väljalaske pealkirjaks sama versioon (näiteks `v0.13.0`).
4. Klõpsake **Generate release notes**, et automaatselt täita muudatuste logi.
5. Soovi korral muutke teksti (nt rõhutamaks uusi toetatud keeli või olulisi muudatusi).
6. Avaldage väljalase.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->