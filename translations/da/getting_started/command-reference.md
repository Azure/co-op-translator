<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:29:12+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "da"
}
-->
# Command reference
**Co-op Translator** CLI tilbyder flere muligheder for at tilpasse oversættelsesprocessen:

Command                                       | Beskrivelse
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Oversætter dit projekt til de angivne sprog. Eksempel: translate -l "es fr de" oversætter til spansk, fransk og tysk. Brug translate -l "all" for at oversætte til alle understøttede sprog.
translate -l "language_codes" -u              | Opdaterer oversættelser ved at slette eksisterende og oprette dem igen. Advarsel: Dette sletter alle nuværende oversættelser for de angivne sprog.
translate -l "language_codes" -img            | Oversætter kun billedfiler.
translate -l "language_codes" -md             | Oversætter kun Markdown-filer.
translate -l "language_codes" -chk            | Tjekker oversatte filer for fejl og prøver at oversætte igen, hvis det er nødvendigt.
translate -l "language_codes" -d              | Aktiverer fejlsøgningsfunktion for detaljeret logning.
translate -l "language_codes" -r "root_dir"   | Angiver projektets rodmappe.
translate -l "language_codes" -f              | Bruger hurtig tilstand til billedoversættelse (op til 3x hurtigere gengivelse med en lille kompromis på kvalitet og justering).
translate -l "language_codes" -y              | Bekræfter automatisk alle prompts (nyttigt til CI/CD pipelines).
translate -l "language_codes" --help          | Hjælpedetaljer i CLI med tilgængelige kommandoer.

### Eksempler på brug:

  1. Standardadfærd (tilføjer nye oversættelser uden at slette eksisterende):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Tilføj kun nye koreanske billedoversættelser (ingen eksisterende oversættelser slettes):    translate -l "ko" -img

  3. Opdater alle koreanske oversættelser (Advarsel: Dette sletter alle eksisterende koreanske oversættelser før genoversættelse):    translate -l "ko" -u

  4. Opdater kun koreanske billeder (Advarsel: Dette sletter alle eksisterende koreanske billeder før genoversættelse):    translate -l "ko" -img -u

  5. Tilføj nye markdown-oversættelser for koreansk uden at påvirke andre oversættelser:    translate -l "ko" -md

  6. Tjek oversatte filer for fejl og prøv at oversætte igen, hvis nødvendigt: translate -l "ko" -chk

  7. Tjek oversatte filer for fejl og prøv igen (kun markdown): translate -l "ko" -chk -md

  8. Tjek oversatte filer for fejl og prøv igen (kun billeder): translate -l "ko" -chk -img

  9. Brug hurtig tilstand til billedoversættelse:    translate -l "ko" -img -f

  10. Eksempel på fejlsøgningsfunktion: - translate -l "ko" -d: Aktiver fejlsøgningslogning.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.