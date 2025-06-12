<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:34:31+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "my"
}
-->
# Command reference
**Co-op Translator** CLI waxay bixisaa dhowr ikhtiyaar si loo habeeyo habka turjumaadda:

Command                                       | Sharaxaad
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Waxay turjumaysaa mashruucaaga luqadaha la cayimay. Tusaale: translate -l "es fr de" waxay turjumaysaa Isbaanish, Faransiis, iyo Jarmal. Isticmaal translate -l "all" si loogu turjumo dhammaan luqadaha la taageerayo.
translate -l "language_codes" -u              | Waxay cusboonaysiisaa turjumaadaha adigoo tirtiraya kuwii jiray oo dib u abuuraya. Digniin: Tani waxay tirtiri doontaa dhammaan turjumaadaha hadda jira ee luqadaha la cayimay.
translate -l "language_codes" -img            | Waxay turjumaysaa kaliya faylasha sawirrada.
translate -l "language_codes" -md             | Waxay turjumaysaa kaliya faylasha Markdown.
translate -l "language_codes" -chk            | Waxay hubisaa faylasha turjuman khaladaadka, waxayna mar kale isku daydaa turjumaadda haddii loo baahdo.
translate -l "language_codes" -d              | Waxay shiddaa habka debug si loo helo diiwaan faahfaahsan.
translate -l "language_codes" -r "root_dir"   | Waxay qeexaysaa galka asalka ee mashruuca
translate -l "language_codes" -f              | Waxay isticmaashaa habka degdega ah ee turjumaadda sawirrada (illaa 3 jeer ka dhakhso badan, iyadoo tayada iyo isku-duwidda yar laga yaabo inay yara saameyso).
translate -l "language_codes" -y              | Si toos ah u xaqiiji dhammaan su'aalaha (wax ku ool ah CI/CD pipelines)
translate -l "language_codes" --help          | faahfaahinta caawinta ee CLI-ga oo muujinaya amarrada la heli karo

### Tusaalooyin Isticmaal:

  1. Dhaqanka caadiga ah (ku dar turjumaad cusub adigoon tirtirin kuwii jiray):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Kaliya ku dar turjumaadaha sawirrada cusub ee Korean (ma tirtirna turjumaadaha jira):    translate -l "ko" -img

  3. Cusboonaysii dhammaan turjumaadaha Korean (Digniin: Tani waxay tirtiraysaa dhammaan turjumaadaha Korean ee jira ka hor inta aan dib loo turjumin):    translate -l "ko" -u

  4. Cusboonaysii kaliya sawirrada Korean (Digniin: Tani waxay tirtiraysaa dhammaan sawirrada Korean ee jira ka hor inta aan dib loo turjumin):    translate -l "ko" -img -u

  5. Kaliya ku dar turjumaadaha markdown cusub ee Korean adigoon wax saameyn ku yeelan turjumaadaha kale:    translate -l "ko" -md

  6. Hubi faylasha turjuman khaladaadka oo mar kale isku day turjumaadda haddii loo baahdo: translate -l "ko" -chk

  7. Hubi faylasha turjuman khaladaadka oo mar kale isku day turjumaadda (kaliya markdown): translate -l "ko" -chk -md

  8. Hubi faylasha turjuman khaladaadka oo mar kale isku day turjumaadda (kaliya sawirro): translate -l "ko" -chk -img

  9. Isticmaal habka degdega ah ee turjumaadda sawirrada:    translate -l "ko" -img -f

  10. Tusaale habka debug: - translate -l "ko" -d: Shid diiwaangelinta debug.

Could you please specify which language "my" refers to? For example, is it Burmese (Myanmar), Malay, or another language? This will help me provide an accurate translation.