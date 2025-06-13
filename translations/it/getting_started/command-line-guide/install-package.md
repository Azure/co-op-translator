<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:34:03+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "it"
}
-->
# Installare il pacchetto Co-op translator

Il **Co-op Translator** è uno strumento a riga di comando (CLI) progettato per aiutarti a tradurre tutti i file markdown e le immagini del tuo progetto in più lingue. Questo tutorial ti guiderà nella configurazione del traduttore e nel suo utilizzo per vari casi d’uso.

### Creare un ambiente virtuale

Puoi creare un ambiente virtuale usando `pip` oppure `Poetry`. Digita uno dei seguenti comandi nel terminale.

#### Usando pip

```bash
python -m venv .venv
```

#### Usando Poetry

```bash
poetry init
```

### Attivare l’ambiente virtuale

Dopo aver creato l’ambiente virtuale, dovrai attivarlo. I passaggi variano a seconda del sistema operativo. Digita il seguente comando nel terminale.

#### Per pip e Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Usando Poetry

1. Se hai creato l’ambiente con Poetry, digita il seguente comando nel terminale per attivarlo.

    ```bash
    poetry shell
    ```

### Installazione del pacchetto e delle dipendenze necessarie

Una volta configurato e attivato l’ambiente virtuale, il passo successivo è installare le dipendenze necessarie.

### Installazione rapida

Installa Co-Op Translator tramite pip

```
pip install co-op-translator
```
Oppure

Installa tramite Poetry
```
poetry add co-op-translator
```

#### Usando pip (da requirements.txt) se cloni questo repo

![NOTE] Ti preghiamo di NON farlo se installi co-op translator tramite l’installazione rapida.

1. Se usi pip, digita il seguente comando nel terminale. Installerà automaticamente i pacchetti richiesti specificati nel file `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Usando Poetry (da pyproject.toml)

1. Se usi Poetry, digita il seguente comando nel terminale. Installerà automaticamente i pacchetti richiesti specificati nel file `pyproject.toml`:

    ```bash
    poetry install
    ```

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.