<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:27:54+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "it"
}
-->
# Riferimento comandi  
Il CLI **Co-op Translator** offre diverse opzioni per personalizzare il processo di traduzione:

Comando                                      | Descrizione  
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
translate -l "language_codes"                 | Traduce il tuo progetto nelle lingue specificate. Esempio: translate -l "es fr de" traduce in spagnolo, francese e tedesco. Usa translate -l "all" per tradurre in tutte le lingue supportate.  
translate -l "language_codes" -u              | Aggiorna le traduzioni cancellando quelle esistenti e ricreandole. Attenzione: questo eliminerà tutte le traduzioni attuali per le lingue specificate.  
translate -l "language_codes" -img            | Traduce solo i file immagine.  
translate -l "language_codes" -md             | Traduce solo i file Markdown.  
translate -l "language_codes" -chk            | Controlla i file tradotti per errori e riprova la traduzione se necessario.  
translate -l "language_codes" -d              | Attiva la modalità debug per un logging dettagliato.  
translate -l "language_codes" -r "root_dir"   | Specifica la directory radice del progetto.  
translate -l "language_codes" -f              | Usa la modalità veloce per la traduzione delle immagini (fino a 3 volte più veloce con un leggero compromesso su qualità e allineamento).  
translate -l "language_codes" -y              | Conferma automaticamente tutte le richieste (utile per pipeline CI/CD).  
translate -l "language_codes" --help          | Mostra i dettagli di aiuto all’interno del CLI con i comandi disponibili.  

### Esempi d’uso:  

  1. Comportamento predefinito (aggiunge nuove traduzioni senza cancellare quelle esistenti):   translate -l "ko"    translate -l "es fr de" -r "./my_project"  

  2. Aggiunge solo nuove traduzioni immagine in coreano (non vengono cancellate le traduzioni esistenti):    translate -l "ko" -img  

  3. Aggiorna tutte le traduzioni in coreano (Attenzione: questo cancella tutte le traduzioni coreane esistenti prima di ritradurre):    translate -l "ko" -u  

  4. Aggiorna solo le immagini coreane (Attenzione: questo cancella tutte le immagini coreane esistenti prima di ritradurre):    translate -l "ko" -img -u  

  5. Aggiunge nuove traduzioni markdown per il coreano senza influire sulle altre traduzioni:    translate -l "ko" -md  

  6. Controlla i file tradotti per errori e riprova la traduzione se necessario: translate -l "ko" -chk  

  7. Controlla i file tradotti per errori e riprova la traduzione (solo markdown): translate -l "ko" -chk -md  

  8. Controlla i file tradotti per errori e riprova la traduzione (solo immagini): translate -l "ko" -chk -img  

  9. Usa la modalità veloce per la traduzione delle immagini:    translate -l "ko" -img -f  

  10. Esempio modalità debug: - translate -l "ko" -d: Attiva il logging debug.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.