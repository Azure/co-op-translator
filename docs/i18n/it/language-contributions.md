# Contribuire ai miglioramenti linguistici

Le tue conoscenze linguistiche possono aiutare a migliorare Co-op Translator. Inizia con un esempio, una correzione suggerita e una spiegazione usando il [modulo di feedback per le traduzioni](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Non è necessario scrivere codice o pagare per l'esecuzione di un modello.

## Da un rapporto a un miglioramento condiviso

1. Un contributore fornisce un estratto della sorgente, la sua traduzione e il contesto.
2. Un revisore linguistico verifica il significato, la naturalezza e se il suggerimento dipende da un particolare locale o corso.
3. Un manutentore decide se la correzione appartiene al corso sorgente, a un'istruzione linguistica condivisa, alla configurazione della terminologia o al codice di traduzione.
4. Per una regola condivisa, un manutentore confronta gli output prima e dopo la modifica sull'esempio segnalato e su esempi non correlati. I contributori possono esaminare questi output senza eseguire lo strumento da soli.
5. La PR risultante collega il rapporto e accredita le persone che hanno fornito esempi e revisioni. Il deployment o la rigenerazione nei repository che consumano è un passaggio separato.

Una segnalazione non modifica automaticamente i prompt né rigenera le traduzioni del corso. Le correzioni specifiche del corso dovrebbero rimanere collegate al repository del corso. Non presumere che una modifica manuale sopravviva a una successiva retraduzione; conferma il comportamento per quel flusso di lavoro.

## Esempio esistente: link Markdown giapponesi

Il [file di istruzioni giapponese](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) dice al modello di tradurre il testo del link preservando la sintassi Markdown e la destinazione del link. Ad esempio, un link scritto come `[text](URL)` non deve diventare `「text」（URL）`.

Questo è un esempio mirato di una regola linguistica supportata da un'illustrazione di output corretto e scorretto. Non è una prova che le istruzioni del prompt da sole garantiscano un Markdown corretto.

Il [Markdown prompt builder](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) carica `templates/language/<language_code>.md` usando un codice lingua in minuscolo e senza spazi iniziali/finali. Se non esiste un file, usa le istruzioni comuni. Questo descrive il percorso del prompt Markdown; non presumere che ogni immagine o altro percorso di traduzione usi le stesse istruzioni.

I [test dei prompt](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) verificano che le istruzioni giapponesi siano incluse. Questo verifica l'assemblaggio del prompt, non la qualità della traduzione.

## Cosa dovrebbe includere una regola linguistica?

Proponi una correzione mirata e ripetibile con un esempio sorgente, il comportamento atteso e un controesempio in cui la regola non deve applicarsi. Preserva il significato, i segnaposto, il codice, le URL e la struttura del documento. Evita di trasformare la preferenza stilistica di una persona o la terminologia di un singolo corso in una regola universale.

L'attuale [implementazione del glossario](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) protegge i termini dalla traduzione. Non è un dizionario di terminologia da sorgente a destinazione. Discuti il nuovo comportamento della terminologia prima di prometterlo ai contributori.

## Esempio della comunità: un report sul nome del prodotto giapponese

In [report #527](https://github.com/Azure/co-op-translator/issues/527), @hyoshioka0128 ha individuato una traduzione giapponese che ha cambiato il nome del prodotto `Co-op Translator` in `Co-op 翻訳`. Il report includeva un link al documento interessato e uno screenshot, rendendo facile localizzare il problema.

Il contributore ha anche collegato una [PR del corso correlata](https://github.com/microsoft/AZD-for-beginners/pull/109). Nella discussione dell'issue, il manutentore ha riconosciuto il report e ha proposto di indagare perché il nome è cambiato, inclusa la protezione della terminologia, il comportamento del glossario e il percorso di traduzione.

Questo mostra come una piccola segnalazione possa supportare un'indagine oltre la correzione di una singola formulazione. Non è un risultato verificato prima/dopo né una prova che le istruzioni giapponesi sui link Markdown sopra abbiano risolto questo problema del nome del prodotto.

Puoi contribuire allo stesso modo: condividi il testo originale, la traduzione corrente, la correzione suggerita e perché è importante. Aggiungi un link al documento o uno screenshot quando utile. Non è necessario diagnosticare la causa o scrivere un prompt prima di segnalarlo.

## Validazione prima di adottare una regola

Usa gli stessi campioni di origine, la revisione del traduttore, il provider/modello e le impostazioni di generazione per le esecuzioni baseline e candidate, cambiando solo l'istruzione proposta. Registra la modifica effettiva del prompt e gli output; ripeti gli esempi quando necessario per distinguere un effetto coerente dalla variabilità dell'output. Includi il fallimento segnalato, i contesti contrastanti e gli esempi che già traducono correttamente.

| Campione | Sorgente/contesto | Output baseline | Output candidato | Valutazione del revisore |
| --- | --- | --- | --- | --- |
| Fallimento segnalato | Da raccogliere | Non eseguito | Non eseguito | In sospeso |
| Controesempio | Da raccogliere | Non eseguito | Non eseguito | In sospeso |
| Esempio non interessato | Da raccogliere | Non eseguito | Non eseguito | In sospeso |

Controlla gli invarianti strutturali separatamente dai giudizi linguistici. Un test di caricamento del prompt riuscito non è una valutazione di qualità, e una singola frase esatta prevista non è l'unica traduzione valida. Se mancano contesto, esecuzioni del modello o revisione linguistica, mantieni la proposta in sospeso piuttosto che affermare che il problema è risolto.