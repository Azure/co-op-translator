<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:45:23+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "sw"
}
-->
# Rejea ya Amri

CLI ya **Co-op Translator** inatoa chaguzi kadhaa za kubadilisha mchakato wa tafsiri:

Amri                                         | Maelezo
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Inatafsiri mradi wako kwa lugha ulizochagua. Mfano: translate -l "es fr de" inatafsiri kwa Kihispania, Kifaransa, na Kijerumani. Tumia translate -l "all" kutafsiri kwa lugha zote zinazoungwa mkono.
translate -l "language_codes" -u              | Inasasisha tafsiri kwa kufuta zilizopo na kuziunda upya. Onyo: Hii itafuta tafsiri zote za sasa kwa lugha ulizochagua.
translate -l "language_codes" -img            | Inatafsiri faili za picha pekee.
translate -l "language_codes" -md             | Inatafsiri faili za Markdown pekee.
translate -l "language_codes" -nb             | Inatafsiri faili za Jupyter notebook (.ipynb) pekee.
translate -l "language_codes" --fix           | Inatafsiri tena faili zenye alama ya ujasiri wa chini kulingana na matokeo ya tathmini ya awali.
translate -l "language_codes" -d              | Inawasha hali ya uchunguzi kwa kuandika logi za kina.
translate -l "language_codes" --save-logs, -s | Hifadhi logi za DEBUG kwenye faili chini ya <root_dir>/logs/ (console inaendelea kudhibitiwa na -d)
translate -l "language_codes" -r "root_dir"   | Inaweka mahali pa mizizi ya mradi
translate -l "language_codes" -f              | Inatumia hali ya haraka kwa tafsiri ya picha (inaweza kuchora haraka mara 3 kwa gharama ndogo ya ubora na mpangilio).
translate -l "language_codes" -y              | Inathibitisha moja kwa moja maswali yote (inasaidia kwa CI/CD pipelines)
translate -l "language_codes" --help          | Maelezo ya msaada ndani ya CLI yanayoonyesha amri zinazopatikana
evaluate -l "language_code"                  | Inatathmini ubora wa tafsiri kwa lugha maalum na kutoa alama za ujasiri
evaluate -l "language_code" -c 0.8           | Inatathmini tafsiri kwa kizingiti cha ujasiri ulichobinafsisha
evaluate -l "language_code" -f               | Hali ya tathmini ya haraka (kanuni pekee, bila LLM)
evaluate -l "language_code" -D               | Hali ya tathmini ya kina (LLM pekee, ni ya kina zaidi lakini polepole)
evaluate -l "language_code" --save-logs, -s  | Hifadhi logi za DEBUG kwenye faili chini ya <root_dir>/logs/
migrate-links -l "language_codes"             | Inachakata upya faili za Markdown zilizotafsiriwa ili kusasisha viungo vya notebooks (.ipynb). Inapendelea notebooks zilizotafsiriwa zinapopatikana; vinginevyo inaweza kutumia notebooks asili.
migrate-links -l "language_codes" -r          | Weka mahali pa mizizi ya mradi (chaguo-msingi: saraka ya sasa).
migrate-links -l "language_codes" --dry-run   | Onyesha ni faili zipi zingebadilika bila kuandika mabadiliko.
migrate-links -l "language_codes" --no-fallback-to-original | Usibadilishe viungo kwenda kwenye notebooks asili pale ambapo tafsiri haipo (badilisha tu pale tafsiri ipo).
migrate-links -l "language_codes" -d          | Washa hali ya uchunguzi kwa logi za kina.
migrate-links -l "language_codes" --save-logs, -s | Hifadhi logi za DEBUG kwenye faili chini ya <root_dir>/logs/
migrate-links -l "all" -y                      | Chakata lugha zote na thibitisha onyo moja kwa moja.

## Mifano ya Matumizi

  1. Tabia ya kawaida (ongeza tafsiri mpya bila kufuta zilizopo):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Ongeza tafsiri mpya za picha za Kikorea pekee (hakuna tafsiri zilizopo zitafutwa):    translate -l "ko" -img

  3. Sasisha tafsiri zote za Kikorea (Onyo: Hii itafuta tafsiri zote za Kikorea kabla ya kutafsiri tena):    translate -l "ko" -u

  4. Sasisha picha za Kikorea pekee (Onyo: Hii itafuta picha zote za Kikorea kabla ya kutafsiri tena):    translate -l "ko" -img -u

  5. Ongeza tafsiri mpya za markdown kwa Kikorea bila kuathiri tafsiri nyingine:    translate -l "ko" -md

  6. Rekebisha tafsiri zenye ujasiri wa chini kulingana na matokeo ya tathmini ya awali: translate -l "ko" --fix

  7. Rekebisha tafsiri zenye ujasiri wa chini kwa faili maalum pekee (markdown): translate -l "ko" --fix -md

  8. Rekebisha tafsiri zenye ujasiri wa chini kwa faili maalum pekee (picha): translate -l "ko" --fix -img

  9. Tumia hali ya haraka kwa tafsiri ya picha:    translate -l "ko" -img -f

  10. Rekebisha tafsiri zenye ujasiri wa chini kwa kizingiti ulichobinafsisha: translate -l "ko" --fix -c 0.8

  11. Mfano wa hali ya uchunguzi: - translate -l "ko" -d: Washa logi za uchunguzi.
  12. Hifadhi logi kwenye faili: translate -l "ko" -s
  13. Console DEBUG na file DEBUG: translate -l "ko" -d -s

  14. Hamisha viungo vya notebook kwa tafsiri za Kikorea (sasisha viungo kwenda kwenye notebooks zilizotafsiriwa zinapopatikana):    migrate-links -l "ko"

  15. Hamisha viungo kwa dry-run (hakuna faili zitakazoandikwa):    migrate-links -l "ko" --dry-run

  16. Sasisha viungo tu pale ambapo notebooks zilizotafsiriwa zipo (usirudi kwenye asili):    migrate-links -l "ko" --no-fallback-to-original

  17. Chakata lugha zote na swali la uthibitisho:    migrate-links -l "all"

  18. Chakata lugha zote na thibitisho moja kwa moja:    migrate-links -l "all" -y
  19. Hifadhi logi kwenye faili kwa migrate-links:    migrate-links -l "ko ja" -s

### Mifano ya Tathmini

> [!WARNING]  
> **Kipengele cha Beta**: Uwezo wa tathmini bado uko kwenye beta. Kipengele hiki kimetolewa ili kutathmini hati zilizotafsiriwa, na mbinu za tathmini na utekelezaji wa kina bado vinaendelea kuboreshwa na vinaweza kubadilika.

  1. Tathmini tafsiri za Kikorea: evaluate -l "ko"

  2. Tathmini kwa kizingiti cha ujasiri ulichobinafsisha: evaluate -l "ko" -c 0.8

  3. Tathmini ya haraka (kanuni pekee): evaluate -l "ko" -f

  4. Tathmini ya kina (LLM pekee): evaluate -l "ko" -D

---

**Kanusho**:
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya mtafsiri wa kibinadamu mwenye ujuzi. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zitakazotokana na matumizi ya tafsiri hii.