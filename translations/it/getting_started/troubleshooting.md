<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:26:10+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "it"
}
-->
# Guida alla risoluzione dei problemi del traduttore Microsoft Co-op


## Panoramica
Il traduttore Microsoft Co-Op è uno strumento potente per tradurre documenti Markdown senza intoppi. Questa guida ti aiuterà a risolvere i problemi comuni riscontrati durante l'uso dello strumento.

## Problemi comuni e soluzioni

### 1. Problema con il tag Markdown
**Problema:** Il documento Markdown tradotto include un tag `markdown` in cima, causando problemi di visualizzazione.

**Soluzione:** Per risolvere, basta eliminare il tag `markdown` presente in cima al file. Questo permetterà al file Markdown di essere visualizzato correttamente.

**Passaggi:**
1. Apri il file Markdown tradotto (`.md`).
2. Individua il tag `markdown` in cima al documento.
3. Elimina il tag `markdown`.
4. Salva le modifiche al file.
5. Riapri il file per assicurarti che venga visualizzato correttamente.

### 2. Problema con l'URL delle immagini incorporate
**Problema:** Gli URL delle immagini incorporate non corrispondono alla lingua locale, causando immagini errate o mancanti.

**Soluzione:** Controlla l'URL delle immagini incorporate e assicurati che corrispondano alla lingua locale. Tutte le immagini si trovano nella cartella `translated_images` e ogni immagine ha un tag della lingua nel nome del file.

**Passaggi:**
1. Apri il documento Markdown tradotto.
2. Identifica le immagini incorporate e i loro URL.
3. Verifica che la lingua nel nome del file immagine corrisponda a quella del documento.
4. Aggiorna gli URL se necessario.
5. Salva le modifiche e riapri il documento per confermare che le immagini vengano visualizzate correttamente.

### 3. Precisione della traduzione
**Problema:** Il contenuto tradotto non è accurato o necessita di ulteriori modifiche.

**Soluzione:** Rivedi il documento tradotto e apporta le modifiche necessarie per migliorare accuratezza e leggibilità.

**Passaggi:**
1. Apri il documento tradotto.
2. Esamina attentamente il contenuto.
3. Apporta le modifiche necessarie per migliorare la precisione della traduzione.
4. Salva le modifiche.

### 4. Problemi di formattazione del file
**Problema:** La formattazione del documento tradotto è errata. Questo può accadere nelle tabelle; qui un ulteriore ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` risolverà i problemi delle tabelle.

**Passaggi:**
1. Apri il documento tradotto.
2. Confrontalo con il documento originale per individuare problemi di formattazione.
3. Regola la formattazione per farla corrispondere a quella originale.
4. Salva le modifiche.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale effettuata da un esperto umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.