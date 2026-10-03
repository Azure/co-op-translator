# Traduci, modifica e revisiona un piccolo progetto

Inizia con due brevi file Markdown e una lingua di destinazione. Vedrai dove vengono scritte le traduzioni, cosa succede quando la sorgente cambia e come controllare il risultato.

## Risultati registrati

L'esempio è stato eseguito il 19 settembre 2026 con Co-op Translator 0.21.0 e Azure OpenAI (`gpt-5-mini`). I comandi CLI non modificati sono stati invocati tramite Click's `CliRunner` usando la wheel costruita e le dipendenze Python esistenti.

| Step | Result |
| --- | --- |
| Preview | Exit 0; nessuna richiesta di traduzione al modello |
| Initial translation | Exit 0; 27.36 secondi |
| Initial review | Exit 0 |
| Edit README and review | Exit 1; traduzione obsoleta rilevata |
| Update translation | Exit 0; 22.17 secondi |
| Review after update | Exit 0; nessun errore o avviso |
| Unchanged guide | Identici byte prima e dopo l'aggiornamento di README |
| Run again | Exit 0; hash identici per tutti i file di traduzione |

Queste sono misurazioni di esecuzioni individuali, non garanzie di prestazioni. Il tempo di configurazione è escluso; la fatturazione del provider non è stata misurata. Una esecuzione senza cambiamenti può comunque eseguire un controllo di integrità del provider.

Ispeziona la [traduzione iniziale](../../assets/demo/before.txt), la [traduzione aggiornata](../../assets/demo/after.txt), il [diff completo della traduzione](../../assets/demo/update.diff), la [revisione obsoleta](../../assets/demo/review-stale.txt), la [revisione finale](../../assets/demo/review-after.txt) e i [dettagli dell'esecuzione](../../assets/demo/results.json). La traduzione dell'intero file può modificare altre formulazioni, come mostra il diff catturato. Entrambi gli artefatti testuali mantengono il disclaimer generato.

La revisione umana è ancora importante: l'aggiornamento catturato usa `[사용 가이드](guide.md)을`; la particella coreana dovrebbe essere `[사용 가이드](guide.md)를`. Gli artefatti testuali mantengono questo output intatto invece di presentare una traduzione modificata come output del modello. La revisione strutturale supera il controllo nonostante questo problema di formulazione.

## 1. Prepara una piccola cartella

Usa Python 3.11–3.14 e la [configurazione dell'ambiente virtuale](configuration.md#local-runtime-setup). Installa la versione usata per questo esempio:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Scarica [README.txt](../../assets/demo/README.txt) e [guide.txt](../../assets/demo/guide.txt) in questa cartella, salvandoli come `README.md` e `guide.md`. Sono piccoli documenti di progetto fittizi; non è necessaria l'installazione di applicazioni.

Il README include un blocco di codice e un link a `guide.md`. La sua frase finale è:

```text
Notes are saved locally.
```

Mantieni solo questi due documenti sorgente in questa cartella. Tutti i comandi seguenti vengono eseguiti all'interno di `translation-demo` e funzionano in Bash e PowerShell.

## 2. Anteprima senza credenziali

```bash
translate -l "ko" -md --dry-run
```

L'anteprima stima il lavoro di traduzione senza chiamare un modello o scrivere traduzioni. Le stime di token non sono un preventivo di fatturazione. La prima esecuzione dovrebbe identificare entrambi i file Markdown come nuovo lavoro.

## 3. Scegli un provider e traduci

Configura un provider utilizzando la [guida alla configurazione](configuration.md): Azure OpenAI, OpenAI o Anthropic. La traduzione di testo con OpenAI e Anthropic non richiede un account Azure. I servizi per immagini non sono necessari per questo esempio.

Se usi un file `.env` locale, aggiungi `.env` al `.gitignore` di questa cartella. Le chiamate di traduzione usano il tuo account provider e possono comportare addebiti.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Apri `translations/ko/README.md` e `translations/ko/guide.md`. Controlla la formulazione in coreano, il blocco di codice e il link dal README tradotto alla guida tradotta. La formulazione dell'output varia in base al modello.

`co-op-review` verifica la freschezza, la struttura e i link locali. Un risultato positivo non certifica l'accuratezza linguistica. Risolvi eventuali errori segnalati prima di proseguire.

Registra la baseline di successo con Git (configura prima la tua identità Git se necessario):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Modifica la sorgente

In `README.md`, sostituisci `Notes are saved locally.` con:

```text
Notes are saved locally as Markdown files.
```

Lascia `guide.md` invariato. Poi esegui:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

La revisione dovrebbe segnalare la traduzione del README come obsoleta e terminare con errore. Questo è lo stato intermedio previsto. L'anteprima dovrebbe identificare lavoro per il README modificato.

## 5. Aggiorna e ispeziona il diff

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Ispeziona il diff reale: la CLI predefinita re-traduce il file modificato, quindi il modello può anche rivedere altre formulazioni in quel file. La guida non modificata non dovrebbe avere diff. La revisione non dovrebbe più segnalare il README come obsoleto; indaga su qualsiasi altro riscontro invece di ignorarlo.

La conservazione a livello di blocco delle modifiche Markdown umane richiede un provider opzionale di stato di traduzione nell'[API Python](api.md). Non è abilitato da questi comandi CLI.

## 6. Esegui di nuovo senza modifiche

Esegui il commit del sorgente aggiornato e della traduzione:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Con le traduzioni correnti e la configurazione invariata, il traduttore salta i file. Il comando Git finale non dovrebbe produrre diff e dovrebbe terminare con successo.

## Prossimi passi

- [Traduci solo il README e apri una pull request](github-actions.md#your-first-readme-translation-pr).
- [Scegli CLI, Python API o MCP](workflows.md).
- [Segnala un problema di traduzione senza scrivere codice](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).