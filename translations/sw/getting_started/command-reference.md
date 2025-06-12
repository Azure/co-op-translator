<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:31:54+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "sw"
}
-->
# Marejeo ya Amri
CLI ya **Co-op Translator** inatoa chaguzi kadhaa za kubinafsisha mchakato wa tafsiri:

Amri                                        | Maelezo
--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"               | Hufasiri mradi wako kwa lugha zilizobainishwa. Mfano: translate -l "es fr de" hufasiri kwa Kihispania, Kifaransa, na Kijerumani. Tumia translate -l "all" kutafsiri kwa lugha zote zinazotegemewa.
translate -l "language_codes" -u            | Husasisha tafsiri kwa kufuta zilizopo na kuziunda upya. Warning: Hii itafuta tafsiri zote za sasa za lugha zilizobainishwa.
translate -l "language_codes" -img          | Hufasiri faili za picha pekee.
translate -l "language_codes" -md           | Hufasiri faili za Markdown pekee.
translate -l "language_codes" -chk          | Hukagua faili zilizotafsiriwa kwa makosa na kujaribu tena tafsiri ikiwa inahitajika.
translate -l "language_codes" -d            | Huamsha hali ya debug kwa uandishi wa maelezo ya kina.
translate -l "language_codes" -r "root_dir" | Huainisha saraka kuu ya mradi
translate -l "language_codes" -f            | Hutumia hali ya haraka kwa tafsiri ya picha (hadi mara 3 haraka zaidi kwa kuchora kwa gharama ndogo ya ubora na muafaka).
translate -l "language_codes" -y            | Huthibitisha moja kwa moja maelekezo yote (inayofaa kwa CI/CD pipelines)
translate -l "language_codes" --help        | maelezo ya msaada ndani ya CLI yanaonyesha amri zinazopatikana

### Mifano ya Matumizi:

  1. Tabia ya kawaida (ongeza tafsiri mpya bila kufuta zilizopo):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Ongeza tafsiri mpya za picha za Kikorea pekee (hakuna tafsiri zilizopo zifutwe):    translate -l "ko" -img

  3. Sasisha tafsiri zote za Kikorea (Warning: Hii hufuta tafsiri zote za Kikorea zilizopo kabla ya kutafsiri tena):    translate -l "ko" -u

  4. Sasisha picha za Kikorea pekee (Warning: Hii hufuta picha zote za Kikorea zilizopo kabla ya kutafsiri tena):    translate -l "ko" -img -u

  5. Ongeza tafsiri mpya za Markdown za Kikorea bila kuathiri tafsiri nyingine:    translate -l "ko" -md

  6. Kagua faili zilizotafsiriwa kwa makosa na jaribu tena tafsiri ikiwa inahitajika: translate -l "ko" -chk

  7. Kagua faili zilizotafsiriwa kwa makosa na jaribu tena tafsiri (Markdown pekee): translate -l "ko" -chk -md

  8. Kagua faili zilizotafsiriwa kwa makosa na jaribu tena tafsiri (picha pekee): translate -l "ko" -chk -img

  9. Tumia hali ya haraka kwa tafsiri ya picha:    translate -l "ko" -img -f

  10. Mfano wa hali ya debug: - translate -l "ko" -d: Huamsha uandishi wa maelezo ya debug.

**Kasi ya Maelezo**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za moja kwa moja zinaweza kuwa na makosa au kasoro. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha kuaminika. Kwa taarifa muhimu, tafsiri ya kitaalamu na ya binadamu inashauriwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.