<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T12:02:01+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "sw"
}
-->
# Marejeleo ya Amri

CLI ya **Co-op Translator** inatoa chaguzi kadhaa za kubinafsisha mchakato wa tafsiri:

Amri                                         | Maelezo
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Inatafsiri mradi wako kwa lugha zilizotajwa. Mfano: translate -l "es fr de" inatafsiri kwa Kihispania, Kifaransa, na Kijerumani. Tumia translate -l "all" kutafsiri kwa lugha zote zinazotegemewa.
translate -l "language_codes" -u              | Inasasisha tafsiri kwa kufuta zilizopo na kuziunda upya. Tahadhari: Hii itafuta tafsiri zote za sasa kwa lugha zilizotajwa.
translate -l "language_codes" -img            | Inatafsiri faili za picha pekee.
translate -l "language_codes" -md             | Inatafsiri faili za Markdown pekee.
translate -l "language_codes" -nb             | Inatafsiri faili za daftari la Jupyter (.ipynb) pekee.
translate -l "language_codes" --fix           | Inatafsiri upya faili zilizo na alama za kuaminika chini kulingana na matokeo ya tathmini ya awali.
translate -l "language_codes" -d              | Inawezesha hali ya ufuatiliaji wa makosa kwa kumbukumbu za kina.
translate -l "language_codes" --save-logs, -s | Hifadhi kumbukumbu za kiwango cha DEBUG kwenye faili chini ya <root_dir>/logs/ (konsoli bado inasimamiwa na -d)
translate -l "language_codes" -r "root_dir"   | Inabainisha saraka kuu ya mradi
translate -l "language_codes" -f              | Inatumia hali ya haraka kwa tafsiri ya picha (hadi mara 3 haraka zaidi kwa kuchora kwa gharama ndogo ya ubora na upangaji).
translate -l "language_codes" -y              | Thibitisha moja kwa moja maelekezo yote (inayofaa kwa mizunguko ya CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Weka au zima sehemu ya onyo la tafsiri ya mashine kwenye markdown na daftari zilizotafsiriwa (chaguo-msingi: imewezeshwa).
translate -l "language_codes" --help          | maelezo ya msaada ndani ya CLI yanaonyesha amri zinazopatikana
evaluate -l "language_code"                  | Inatathmini ubora wa tafsiri kwa lugha fulani na kutoa alama za kuaminika
evaluate -l "language_code" -c 0.8           | Inatathmini tafsiri kwa kiwango maalum cha kuaminika
evaluate -l "language_code" -f               | Hali ya tathmini ya haraka (kulingana na sheria pekee, bila LLM)
evaluate -l "language_code" -D               | Hali ya tathmini ya kina (inayotumia LLM pekee, kina zaidi lakini polepole)
evaluate -l "language_code" --save-logs, -s  | Hifadhi kumbukumbu za kiwango cha DEBUG kwenye faili chini ya <root_dir>/logs/
migrate-links -l "language_codes"             | Inachakata upya faili za Markdown zilizotafsiriwa kusasisha viungo vya daftari (.ipynb). Inapendelea daftari zilizotafsiriwa inapopatikana; vinginevyo inaweza kurudi kwenye daftari asilia.
migrate-links -l "language_codes" -r          | Bainisha saraka kuu ya mradi (chaguo-msingi: saraka ya sasa).
migrate-links -l "language_codes" --dry-run   | Onyesha faili gani zingebadilika bila kuandika mabadiliko.
migrate-links -l "language_codes" --no-fallback-to-original | Usibadilishe viungo vya daftari asilia wakati daftari zilizotafsiriwa hazipo (sasisha tu wakati tafsiri ipo).
migrate-links -l "language_codes" -d          | Wezesha hali ya ufuatiliaji wa makosa kwa kumbukumbu za kina.
migrate-links -l "language_codes" --save-logs, -s | Hifadhi kumbukumbu za kiwango cha DEBUG kwenye faili chini ya <root_dir>/logs/
migrate-links -l "all" -y                      | Chakata lugha zote na thibitisha onyo moja kwa moja.

## Mifano ya Matumizi

  1. Tabia ya kawaida (ongeza tafsiri mpya bila kufuta zilizopo):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Ongeza tafsiri mpya za picha za Kikorea pekee (hakuna tafsiri zilizopo zitaondolewa):    translate -l "ko" -img

  3. Sasisha tafsiri zote za Kikorea (Tahadhari: Hii inafuta tafsiri zote za Kikorea kabla ya kutafsiri upya):    translate -l "ko" -u

  4. Sasisha picha za Kikorea pekee (Tahadhari: Hii inafuta picha zote za Kikorea kabla ya kutafsiri upya):    translate -l "ko" -img -u

  5. Ongeza tafsiri mpya za markdown za Kikorea bila kuathiri tafsiri nyingine:    translate -l "ko" -md

  6. Rekebisha tafsiri zenye alama za kuaminika chini kulingana na matokeo ya tathmini ya awali: translate -l "ko" --fix

  7. Rekebisha tafsiri zenye alama za kuaminika chini kwa faili maalum pekee (markdown): translate -l "ko" --fix -md

  8. Rekebisha tafsiri zenye alama za kuaminika chini kwa faili maalum pekee (picha): translate -l "ko" --fix -img

  9. Tumia hali ya haraka kwa tafsiri ya picha:    translate -l "ko" -img -f

  10. Rekebisha tafsiri zenye alama za kuaminika chini kwa kiwango maalum: translate -l "ko" --fix -c 0.8

  11. Mfano wa hali ya ufuatiliaji wa makosa: - translate -l "ko" -d: Wezesha kumbukumbu za ufuatiliaji.
  12. Hifadhi kumbukumbu kwenye faili: translate -l "ko" -s
  13. DEBUG ya konsoli na DEBUG ya faili: translate -l "ko" -d -s
  14. Tafsiri bila kuongeza onyo la tafsiri ya mashine kwenye matokeo: translate -l "ko" --no-disclaimer

  15. Hamisha viungo vya daftari kwa tafsiri za Kikorea (sasisha viungo vya daftari zilizotafsiriwa inapopatikana):    migrate-links -l "ko"

  15. Hamisha viungo kwa dry-run (hakuna kuandika faili):    migrate-links -l "ko" --dry-run

  16. Sasisha viungo tu wakati daftari zilizotafsiriwa zipo (usirudi kwenye asilia):    migrate-links -l "ko" --no-fallback-to-original

  17. Chakata lugha zote na onyo la uthibitisho:    migrate-links -l "all"

  18. Chakata lugha zote na thibitisha moja kwa moja:    migrate-links -l "all" -y
  19. Hifadhi kumbukumbu kwenye faili kwa migrate-links:    migrate-links -l "ko ja" -s

### Mifano ya Tathmini

> [!WARNING]  
> **Sifa ya Beta**: Kazi ya tathmini kwa sasa iko katika awamu ya beta. Kipengele hiki kimetolewa kutathmini nyaraka zilizotafsiriwa, na mbinu za tathmini pamoja na utekelezaji wa kina bado ziko katika maendeleo na zinaweza kubadilika.

  1. Tathmini tafsiri za Kikorea: evaluate -l "ko"

  2. Tathmini kwa kiwango maalum cha kuaminika: evaluate -l "ko" -c 0.8

  3. Tathmini ya haraka (kulingana na sheria pekee): evaluate -l "ko" -f

  4. Tathmini ya kina (inayotumia LLM pekee): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiarifa cha Kukataa**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->