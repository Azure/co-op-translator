<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:39:43+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "it"
}
-->
# Modalità Solo Markdown

## Introduzione
La modalità solo Markdown è progettata per tradurre esclusivamente il contenuto Markdown del tuo progetto. Questa modalità bypassa il processo di traduzione delle immagini e si concentra solo sul contenuto testuale, risultando ideale in scenari in cui la traduzione delle immagini non è necessaria o le variabili d'ambiente richieste per Computer Vision non sono configurate.

## Quando Usarla
- Quando le variabili d'ambiente relative a Computer Vision non sono configurate.
- Quando vuoi tradurre solo il contenuto testuale senza aggiornare i link delle immagini.
- Quando specificato esplicitamente dall'utente tramite l'opzione da riga di comando `-md`.

## Come Attivarla
Per attivare la modalità solo Markdown, usa l'opzione `-md` nel tuo comando. Per esempio:
```
translate -l "ko" -md
```

Oppure, se le variabili d'ambiente relative a Computer Vision non sono configurate, eseguendo `translate -l "ko"` si passerà automaticamente alla modalità solo Markdown.

```
translate -l "ko"
```

Questo comando traduce il contenuto Markdown in coreano e mantiene i link delle immagini ai loro percorsi originali, invece di modificarli in percorsi di immagini tradotte.

## Comportamento
In modalità solo Markdown:
- Il processo di traduzione salta la fase di traduzione delle immagini.
- I link delle immagini nel Markdown restano invariati, puntando ai loro percorsi originali.

## Esempi
### Prima
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.it.png)
```
### Dopo aver usato la modalità solo Markdown
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.it.png)
```

## Risoluzione dei Problemi
- Assicurati che l'opzione `-md` sia specificata correttamente nel comando.
- Verifica che nessuna variabile d'ambiente di Computer Vision interferisca con il processo.

## Conclusione
La modalità solo Markdown offre un modo semplice per tradurre il contenuto testuale senza modificare i link delle immagini. È particolarmente utile quando la traduzione delle immagini non è necessaria o si lavora in ambienti privi della configurazione di Computer Vision.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.