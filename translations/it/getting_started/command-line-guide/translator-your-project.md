<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:05:48+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "it"
}
-->
# Traduci il tuo progetto con Co-op Translator

**Co-op Translator** è uno strumento da riga di comando (CLI) che ti aiuta a tradurre file markdown e immagini nel tuo progetto in più lingue. In questa sezione ti spieghiamo come usare lo strumento, le varie opzioni CLI disponibili e ti mostriamo esempi per diversi scenari d’uso.

> [!NOTE]
> Per l’elenco completo dei comandi e le relative descrizioni dettagliate, consulta la [Riferimento comandi](./command-reference.md).

---

## Esempi di scenari e comandi

Ecco alcuni casi d’uso comuni per **Co-op Translator**, insieme ai comandi da utilizzare.

### 1. Traduzione base (una sola lingua)

Per tradurre l’intero progetto (file markdown e immagini) in una sola lingua, ad esempio il coreano, usa questo comando:

```bash
translate -l "ko"
```

Questo comando tradurrà tutti i file markdown e le immagini in coreano, aggiungendo nuove traduzioni senza eliminare quelle già esistenti.

> [!TIP]
>
> Vuoi sapere quali codici lingua sono disponibili in **Co-op Translator**? Visita la sezione [Lingue supportate](https://github.com/Azure/co-op-translator#supported-languages) nel repository per maggiori dettagli.

#### Esempio su Phi-3 CookBook

Nel **Phi-3 CookBook**, ho usato questo metodo per aggiungere la traduzione coreana ai file markdown e alle immagini già presenti.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Traduzione in più lingue

Per tradurre il tuo progetto in più lingue (ad esempio spagnolo, francese e tedesco), usa questo comando:

```bash
translate -l "es fr de"
```

Questo comando tradurrà il progetto in spagnolo, francese e tedesco, aggiungendo nuove traduzioni senza sovrascrivere quelle esistenti.

#### Esempio su Phi-3 CookBook

Nel **Phi-3 CookBook**, dopo aver scaricato le ultime modifiche per riflettere i commit più recenti, ho usato questo metodo per tradurre i nuovi file markdown e immagini aggiunti.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Anche se di solito è consigliato tradurre una lingua alla volta, in situazioni come questa dove bisogna aggiungere modifiche specifiche, tradurre più lingue contemporaneamente può essere efficiente.

### 3. Aggiornare le traduzioni (elimina le traduzioni esistenti)

Per aggiornare le traduzioni esistenti (cioè eliminare le traduzioni attuali e sostituirle con quelle nuove), usa l’opzione `-u`. Questa eliminerà tutte le traduzioni esistenti per le lingue specificate e le tradurrà di nuovo.

```bash
translate -l "ko" -u
```

Attenzione: Questo comando ti chiederà conferma prima di procedere con l’eliminazione delle traduzioni esistenti.

#### Esempio su Phi-3 CookBook

Nel **Phi-3 CookBook**, ho usato questo metodo per aggiornare tutti i file tradotti in spagnolo. Consiglio di usare questo metodo quando ci sono cambiamenti importanti nei contenuti originali su più documenti markdown. Se invece devi aggiornare solo pochi file markdown tradotti, è più efficiente eliminarli manualmente e poi usare il metodo `-a` per aggiungere le traduzioni aggiornate.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Tradurre solo le immagini

Per tradurre solo i file immagine nel tuo progetto, usa l’opzione `-img`:

```bash
translate -l "ko" -img
```

Questo comando tradurrà solo le immagini in coreano, senza modificare i file markdown.

### 6. Tradurre solo i file markdown

Per tradurre solo i file markdown nel tuo progetto, usa l’opzione `-md`:

```bash
translate -l "ko" -md
```

#### Esempio su Phi-3 CookBook

Nel **Phi-3 CookBook**, ho usato questo metodo per controllare eventuali errori di traduzione nei file coreani e ritentare automaticamente la traduzione per i file con problemi rilevati.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Questa opzione controlla la presenza di errori di traduzione. Attualmente, se la differenza di interruzioni di riga tra il file originale e quello tradotto supera sei, il file viene segnalato come errato. Ho intenzione di migliorare questo criterio per renderlo più flessibile in futuro.

Ad esempio, questo metodo è utile per individuare parti mancanti o traduzioni corrotte, e ritenterà automaticamente la traduzione per quei file.

Tuttavia, se già sai quali file sono problematici, è più efficiente eliminarli manualmente e usare l’opzione `-a` per tradurli di nuovo.

### 8. Modalità debug

Per abilitare la registrazione dettagliata e facilitare la risoluzione dei problemi, usa l’opzione `-d`:

```bash
translate -l "ko" -d
```

Questo comando eseguirà la traduzione in modalità debug, fornendo informazioni di log aggiuntive che possono aiutarti a individuare eventuali problemi durante il processo di traduzione.

#### Esempio su Phi-3 CookBook

Nel **Phi-3 CookBook**, ho riscontrato un problema in cui le traduzioni con molti link nei file markdown causavano errori di formattazione, come traduzioni interrotte e salti di riga ignorati. Per diagnosticare il problema, ho usato l’opzione `-d` per vedere come funzionava il processo di traduzione.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Tradurre in tutte le lingue

Se vuoi tradurre il progetto in tutte le lingue supportate, usa la parola chiave all.

> [!WARNING]
> Tradurre tutte le lingue contemporaneamente può richiedere molto tempo a seconda delle dimensioni del progetto. Ad esempio, tradurre il **Phi-3 CookBook** in spagnolo ha richiesto circa 2 ore. Considerando la scala, non è pratico per una sola persona gestire 20 lingue. Si consiglia di suddividere il lavoro tra più collaboratori, ognuno responsabile di una o due lingue, e aggiornare le traduzioni gradualmente.

```bash
translate -l "all"
```

Questo comando tradurrà il progetto in tutte le lingue disponibili. Se procedi, la traduzione potrebbe richiedere molto tempo a seconda delle dimensioni del progetto.

> [!TIP]
>
> ### Eliminare manualmente i file tradotti (opzionale)
> Ora i file tradotti vengono rilevati e ripuliti automaticamente quando un file sorgente viene aggiornato.
>
> Tuttavia, se vuoi aggiornare manualmente una traduzione – ad esempio per rifare un file specifico o ignorare il comportamento automatico del sistema – puoi usare il seguente comando per eliminare tutte le versioni del file nelle cartelle delle lingue.
>
> ### Su Windows:
> 1. **Usando il Prompt dei comandi**:
>    - Apri il Prompt dei comandi.
>    - Vai nella cartella dove si trovano i file usando il comando `cd`.
>    - Usa questo comando per eliminare i file:
>      ```
>      del /s *filename*
>      ```
>      Sostituisci `filename` con la parte specifica del nome del file che cerchi. L’opzione `/s` cerca anche nelle sottocartelle.
>
> 2. **Usando PowerShell**:
>    - Apri PowerShell.
>    - Esegui questo comando:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Sostituisci `"C:\YourPath"` con il percorso della cartella e `filename` con il nome specifico.
>
> ### Su macOS/Linux:
> 1. **Usando il Terminale**:
>   - Apri il Terminale.
>   - Vai nella directory con `cd`.
>   - Usa il comando `find`:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Sostituisci `filename` con il nome specifico.
>
> Controlla sempre i file prima di eliminarli per evitare perdite accidentali.
>
> Una volta eliminati i file da sostituire, ti basta rieseguire il comando `translate -l` per aggiornare le modifiche più recenti ai file.

---

**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.