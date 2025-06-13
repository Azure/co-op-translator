<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:47:43+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "it"
}
-->
# Traduci il tuo progetto usando Co-op Translator

Il **Co-op Translator** è uno strumento da linea di comando (CLI) che ti aiuta a tradurre file markdown e immagini nel tuo progetto in più lingue. Questa sezione spiega come usare lo strumento, illustra le varie opzioni CLI e fornisce esempi per diversi casi d’uso.

> [!NOTE]
> Per un elenco completo dei comandi e delle loro descrizioni dettagliate, consulta la [Riferimento comandi](./command-reference.md).

---

## Scenari ed Esempi di Comandi

Ecco alcuni casi d’uso comuni per il **Co-op Translator**, insieme ai comandi appropriati da eseguire.

### 1. Traduzione Base (Singola Lingua)

Per tradurre l’intero progetto (file markdown e immagini) in una singola lingua, come il coreano, usa il comando seguente:

```bash
translate -l "ko"
```

Questo comando tradurrà tutti i file markdown e immagini in coreano, aggiungendo nuove traduzioni senza cancellare quelle esistenti.

> [!TIP]
>
> Vuoi sapere quali codici lingua sono disponibili in **Co-op Translator**? Visita la sezione [Lingue Supportate](https://github.com/Azure/co-op-translator#supported-languages) nel repository per maggiori dettagli.

#### Esempio su Phi-3 CookBook

Nel **Phi-3 CookBook**, ho usato il seguente metodo per aggiungere la traduzione in coreano ai file markdown e immagini esistenti.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Tradurre in Più Lingue

Per tradurre il tuo progetto in più lingue (ad esempio spagnolo, francese e tedesco), usa questo comando:

```bash
translate -l "es fr de"
```

Questo comando tradurrà il progetto in spagnolo, francese e tedesco, aggiungendo nuove traduzioni senza sovrascrivere quelle esistenti.

#### Esempio su Phi-3 CookBook

Nel **Phi-3 CookBook**, dopo aver scaricato le ultime modifiche per riflettere i commit più recenti, ho usato il seguente metodo per tradurre i nuovi file markdown e immagini aggiunti.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Sebbene generalmente sia consigliato tradurre una lingua alla volta, in situazioni come questa, dove è necessario aggiungere modifiche specifiche, tradurre più lingue contemporaneamente può essere efficiente.

### 3. Aggiornare le Traduzioni (Cancella quelle Esistenti)

Per aggiornare le traduzioni esistenti (cioè cancellare le traduzioni attuali e sostituirle con nuove), usa l’opzione `-u`. Questo eliminerà tutte le traduzioni esistenti per le lingue specificate e le ritradurrà.

```bash
translate -l "ko" -u
```

Attenzione: questo comando ti chiederà conferma prima di procedere con la cancellazione delle traduzioni esistenti.

#### Esempio su Phi-3 CookBook

Nel **Phi-3 CookBook**, ho usato il seguente metodo per aggiornare tutti i file tradotti in spagnolo. Consiglio questo metodo quando ci sono cambiamenti significativi nel contenuto originale in più documenti markdown. Se invece ci sono pochi file markdown tradotti da aggiornare, è più efficiente cancellare manualmente quei file specifici e poi usare il metodo `-a` per aggiungere le traduzioni aggiornate.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Tradurre Solo le Immagini

Per tradurre solo i file immagine nel tuo progetto, usa l’opzione `-img`:

```bash
translate -l "ko" -img
```

Questo comando tradurrà solo le immagini in coreano, senza modificare i file markdown.

### 6. Tradurre Solo i File Markdown

Per tradurre solo i file markdown nel tuo progetto, usa l’opzione `-md`:

```bash
translate -l "ko" -md
```

### 7. Controllare Errori nei File Tradotti

Se vuoi controllare la presenza di errori nei file tradotti e ritentare la traduzione se necessario, usa l’opzione `-chk`:

```bash
translate -l "ko" -chk
```

Questo comando eseguirà la scansione dei file markdown tradotti e ritenterà la traduzione per qualsiasi file con errori.

#### Esempio su Phi-3 CookBook

Nel **Phi-3 CookBook**, ho usato il seguente metodo per controllare errori di traduzione nei file coreani e ritentare automaticamente la traduzione per i file con problemi rilevati.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Questa opzione verifica errori di traduzione. Attualmente, se la differenza nelle interruzioni di linea tra il file originale e quello tradotto supera sei, il file viene segnalato come contenente un errore di traduzione. Ho in programma di migliorare questo criterio per una maggiore flessibilità in futuro.

Ad esempio, questo metodo è utile per rilevare parti mancanti o traduzioni corrotte, e ritenterà automaticamente la traduzione per quei file.

Tuttavia, se sai già quali file sono problematici, è più efficiente cancellarli manualmente e usare l’opzione `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`:

```bash
translate -l "ko" -d
```

Questo comando eseguirà la traduzione in modalità debug, fornendo informazioni di log aggiuntive che possono aiutarti a identificare problemi durante il processo di traduzione.

#### Esempio su Phi-3 CookBook

Nel **Phi-3 CookBook**, ho incontrato un problema in cui traduzioni con molti link nei file markdown causavano errori di formattazione, come traduzioni interrotte e interruzioni di linea ignorate. Per diagnosticare questo problema, ho usato l’opzione `-d` per vedere come funziona il processo di traduzione.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Tradurre Tutte le Lingue

Se vuoi tradurre il progetto in tutte le lingue supportate, usa la parola chiave all.

> [!WARNING]
> Tradurre tutte le lingue contemporaneamente può richiedere molto tempo a seconda della dimensione del progetto. Ad esempio, tradurre il **Phi-3 CookBook** in spagnolo ha richiesto circa 2 ore. Data la mole di lavoro, non è pratico per una sola persona gestire 20 lingue. È consigliabile dividere il lavoro tra più collaboratori, ognuno responsabile di una o due lingue, aggiornando le traduzioni gradualmente.

```bash
translate -l "all"
```

Questo comando tradurrà il progetto in tutte le lingue disponibili. Se procedi, la traduzione potrebbe richiedere molto tempo a seconda della dimensione del progetto.

> [!TIP]
>
> ### Cancellare Manualmente i File Tradotti (Opzionale)
> I file tradotti ora vengono rilevati e puliti automaticamente quando un file sorgente viene aggiornato.
>
> Tuttavia, se vuoi aggiornare manualmente una traduzione — ad esempio per rifare un file specifico o sovrascrivere il comportamento del sistema — puoi usare il comando seguente per cancellare tutte le versioni del file nelle cartelle delle lingue.
>
> ### Su Windows:
> 1. **Usando il Prompt dei Comandi**:
>    - Apri il Prompt dei Comandi.
>    - Naviga nella cartella dove si trovano i file usando il comando `cd`.
>    - Usa il comando seguente per cancellare i file:
>      ```
>      del /s *filename*
>      ```
>      L’opzione `/s` cerca anche nelle sottocartelle.
>
> 2. **Usando PowerShell**:
>    - Apri PowerShell.
>    - Esegui questo comando:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Sostituisci `"C:\YourPath"` con il percorso corretto.
>
>     Il comando `cd` serve per cambiare directory, mentre `find` aiuta a individuare i file.
>
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>
>     Sostituisci `filename` con il nome del file e usa il comando `translate -l` per aggiornare le modifiche più recenti ai file.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre deve essere considerato la fonte autorevole. Per informazioni critiche si raccomanda la traduzione professionale effettuata da un traduttore umano. Non ci assumiamo responsabilità per eventuali incomprensioni o interpretazioni errate derivanti dall’uso di questa traduzione.