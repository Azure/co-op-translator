<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:42:38+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "tl"
}
-->
# Sanggunian ng mga Utos

Nag-aalok ang **Co-op Translator** CLI ng iba't ibang opsyon para i-customize ang proseso ng pagsasalin:

Utos                                         | Paglalarawan
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Isinasalin ang iyong proyekto sa mga tinukoy na wika. Halimbawa: translate -l "es fr de" ay isasalin sa Spanish, French, at German. Gamitin ang translate -l "all" para isalin sa lahat ng suportadong wika.
translate -l "language_codes" -u              | Ina-update ang mga salin sa pamamagitan ng pagbura ng mga kasalukuyang salin at muling paglikha ng mga ito. Babala: Mabubura ang lahat ng kasalukuyang salin para sa mga tinukoy na wika.
translate -l "language_codes" -img            | Isinasalin lamang ang mga image file.
translate -l "language_codes" -md             | Isinasalin lamang ang mga Markdown file.
translate -l "language_codes" -nb             | Isinasalin lamang ang mga Jupyter notebook file (.ipynb).
translate -l "language_codes" --fix           | Muling isinasalin ang mga file na may mababang confidence score batay sa nakaraang resulta ng pagsusuri.
translate -l "language_codes" -d              | Pinapagana ang debug mode para sa mas detalyadong logging.
translate -l "language_codes" --save-logs, -s | Sine-save ang DEBUG-level logs sa mga file sa <root_dir>/logs/ (ang console ay kontrolado pa rin ng -d)
translate -l "language_codes" -r "root_dir"   | Itinatakda ang root directory ng proyekto
translate -l "language_codes" -f              | Gumagamit ng fast mode para sa pagsasalin ng image (hanggang 3x mas mabilis ang plotting, ngunit bahagyang bababa ang kalidad at alignment).
translate -l "language_codes" -y              | Awtomatikong kinukumpirma ang lahat ng prompt (kapaki-pakinabang para sa CI/CD pipelines)
translate -l "language_codes" --help          | Detalye ng tulong sa loob ng CLI na nagpapakita ng mga available na utos
evaluate -l "language_code"                  | Sinusuri ang kalidad ng salin para sa isang partikular na wika at nagbibigay ng confidence scores
evaluate -l "language_code" -c 0.8           | Sinusuri ang mga salin gamit ang custom na confidence threshold
evaluate -l "language_code" -f               | Mabilis na pagsusuri (rule-based lang, walang LLM)
evaluate -l "language_code" -D               | Malalim na pagsusuri (LLM-based lang, mas masusi pero mas mabagal)
evaluate -l "language_code" --save-logs, -s  | Sine-save ang DEBUG-level logs sa mga file sa <root_dir>/logs/
migrate-links -l "language_codes"             | Muling pinoproseso ang mga isinaling Markdown file para i-update ang mga link papunta sa notebooks (.ipynb). Mas pinipili ang isinaling notebooks kung available; kung wala, maaaring bumalik sa orihinal na notebooks.
migrate-links -l "language_codes" -r          | Itakda ang root directory ng proyekto (default: kasalukuyang directory).
migrate-links -l "language_codes" --dry-run   | Ipakita kung aling mga file ang magbabago nang hindi nagsusulat ng pagbabago.
migrate-links -l "language_codes" --no-fallback-to-original | Huwag i-rewrite ang mga link papunta sa orihinal na notebooks kapag wala ang isinaling katumbas (i-update lang kapag may isinaling notebook).
migrate-links -l "language_codes" -d          | I-enable ang debug mode para sa detalyadong logging.
migrate-links -l "language_codes" --save-logs, -s | Sine-save ang DEBUG-level logs sa mga file sa <root_dir>/logs/
migrate-links -l "all" -y                      | Iproseso ang lahat ng wika at awtomatikong kumpirmahin ang warning prompt.

## Mga Halimbawa ng Paggamit

  1. Default na kilos (magdagdag ng bagong salin nang hindi binubura ang mga dati):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Magdagdag lang ng bagong Korean image translations (hindi binubura ang mga dati):    translate -l "ko" -img

  3. I-update lahat ng Korean translations (Babala: Buburahin muna ang lahat ng kasalukuyang Korean translations bago muling isalin):    translate -l "ko" -u

  4. I-update lang ang Korean images (Babala: Buburahin muna ang lahat ng kasalukuyang Korean images bago muling isalin):    translate -l "ko" -img -u

  5. Magdagdag ng bagong markdown translations para sa Korean nang hindi naaapektuhan ang ibang salin:    translate -l "ko" -md

  6. Ayusin ang mga salin na may mababang confidence batay sa nakaraang resulta ng pagsusuri: translate -l "ko" --fix

  7. Ayusin ang mga salin na may mababang confidence para sa partikular na mga file lang (markdown): translate -l "ko" --fix -md

  8. Ayusin ang mga salin na may mababang confidence para sa partikular na mga file lang (images): translate -l "ko" --fix -img

  9. Gumamit ng fast mode para sa pagsasalin ng image:    translate -l "ko" -img -f

  10. Ayusin ang mga salin na may mababang confidence gamit ang custom na threshold: translate -l "ko" --fix -c 0.8

  11. Halimbawa ng debug mode: - translate -l "ko" -d: I-enable ang debug logging.
  12. I-save ang logs sa mga file: translate -l "ko" -s
  13. Console DEBUG at file DEBUG: translate -l "ko" -d -s

  14. I-migrate ang notebook links para sa Korean translations (i-update ang mga link papunta sa isinaling notebooks kung available):    migrate-links -l "ko"

  15. I-migrate ang links gamit ang dry-run (walang pagbabago sa file):    migrate-links -l "ko" --dry-run

  16. I-update lang ang mga link kapag may isinaling notebook (huwag bumalik sa orihinal):    migrate-links -l "ko" --no-fallback-to-original

  17. Iproseso ang lahat ng wika na may kumpirmasyon:    migrate-links -l "all"

  18. Iproseso ang lahat ng wika at awtomatikong kumpirmahin:    migrate-links -l "all" -y
  19. I-save ang logs sa mga file para sa migrate-links:    migrate-links -l "ko ja" -s

### Mga Halimbawa ng Pagsusuri

> [!WARNING]  
> **Beta Feature**: Ang evaluation functionality ay kasalukuyang nasa beta. Inilabas ang feature na ito para suriin ang mga isinaling dokumento, at ang mga evaluation method at detalye ng implementasyon ay patuloy pang dinidevelop at maaaring magbago.

  1. Suriin ang Korean translations: evaluate -l "ko"

  2. Suriin gamit ang custom na confidence threshold: evaluate -l "ko" -c 0.8

  3. Mabilis na pagsusuri (rule-based lang): evaluate -l "ko" -f

  4. Malalim na pagsusuri (LLM-based lang): evaluate -l "ko" -D

---

**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring lumitaw mula sa paggamit ng pagsasaling ito.