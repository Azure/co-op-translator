<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T11:57:23+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "tl"
}
-->
# Sanggunian ng mga utos

Nagbibigay ang **Co-op Translator** CLI ng ilang mga opsyon upang i-customize ang proseso ng pagsasalin:

Utos                                         | Paglalarawan
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Isinasalin ang iyong proyekto sa mga tinukoy na wika. Halimbawa: translate -l "es fr de" ay nagsasalin sa Espanyol, Pranses, at Aleman. Gamitin ang translate -l "all" para isalin sa lahat ng suportadong wika.
translate -l "language_codes" -u              | Ina-update ang mga pagsasalin sa pamamagitan ng pagtanggal ng mga kasalukuyang pagsasalin at muling paggawa ng mga ito. Babala: Tatanggalin nito ang lahat ng kasalukuyang pagsasalin para sa mga tinukoy na wika.
translate -l "language_codes" -img            | Isinasalin lamang ang mga file ng larawan.
translate -l "language_codes" -md             | Isinasalin lamang ang mga Markdown na file.
translate -l "language_codes" -nb             | Isinasalin lamang ang mga Jupyter notebook na file (.ipynb).
translate -l "language_codes" --fix           | Muling isinasalin ang mga file na may mababang confidence score base sa mga naunang resulta ng pagsusuri.
translate -l "language_codes" -d              | Pinapagana ang debug mode para sa mas detalyadong pag-log.
translate -l "language_codes" --save-logs, -s | I-save ang mga DEBUG-level na log sa mga file sa ilalim ng <root_dir>/logs/ (ang console ay nananatiling kontrolado ng -d)
translate -l "language_codes" -r "root_dir"   | Itinatakda ang root directory ng proyekto
translate -l "language_codes" -f              | Ginagamit ang fast mode para sa pagsasalin ng mga larawan (hanggang 3x na mas mabilis ang pag-plot sa kaunting kompromiso sa kalidad at pagkaka-align).
translate -l "language_codes" -y              | Awtomatikong kinukumpirma ang lahat ng mga prompt (kapaki-pakinabang para sa CI/CD pipelines)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Pinapagana o pinapahinto ang pagdagdag ng seksyon ng machine translation disclaimer sa mga isinaling markdown at notebook (default: pinapagana).
translate -l "language_codes" --help          | mga detalye ng tulong sa loob ng CLI na nagpapakita ng mga magagamit na utos
evaluate -l "language_code"                  | Sinusuri ang kalidad ng pagsasalin para sa isang partikular na wika at nagbibigay ng mga confidence score
evaluate -l "language_code" -c 0.8           | Sinusuri ang mga pagsasalin gamit ang custom na confidence threshold
evaluate -l "language_code" -f               | Mabilis na mode ng pagsusuri (rule-based lamang, walang LLM)
evaluate -l "language_code" -D               | Malalim na mode ng pagsusuri (LLM-based lamang, mas masinsin ngunit mas mabagal)
evaluate -l "language_code" --save-logs, -s  | I-save ang mga DEBUG-level na log sa mga file sa ilalim ng <root_dir>/logs/
migrate-links -l "language_codes"             | Muling pinoproseso ang mga isinaling Markdown na file upang i-update ang mga link sa mga notebook (.ipynb). Mas pinipili ang mga isinaling notebook kapag available; kung wala, maaaring bumalik sa orihinal na mga notebook.
migrate-links -l "language_codes" -r          | Itinakda ang root directory ng proyekto (default: kasalukuyang direktoryo).
migrate-links -l "language_codes" --dry-run   | Ipinapakita kung aling mga file ang mababago nang hindi isinusulat ang mga pagbabago.
migrate-links -l "language_codes" --no-fallback-to-original | Huwag isulat muli ang mga link sa orihinal na mga notebook kapag wala ang mga isinaling katumbas (i-update lamang kapag may isinalin).
migrate-links -l "language_codes" -d          | Pinapagana ang debug mode para sa mas detalyadong pag-log.
migrate-links -l "language_codes" --save-logs, -s | I-save ang mga DEBUG-level na log sa mga file sa ilalim ng <root_dir>/logs/
migrate-links -l "all" -y                      | Pinoproseso ang lahat ng wika at awtomatikong kinukumpirma ang babalang prompt.

## Mga Halimbawa ng Paggamit

  1. Default na pag-uugali (magdagdag ng mga bagong pagsasalin nang hindi tinatanggal ang mga kasalukuyan):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Magdagdag lamang ng mga bagong pagsasalin ng larawan sa Korean (hindi tinatanggal ang mga kasalukuyang pagsasalin):    translate -l "ko" -img

  3. I-update ang lahat ng pagsasalin sa Korean (Babala: Tatanggalin nito ang lahat ng kasalukuyang pagsasalin sa Korean bago muling isalin):    translate -l "ko" -u

  4. I-update lamang ang mga larawan sa Korean (Babala: Tatanggalin nito ang lahat ng kasalukuyang larawan sa Korean bago muling isalin):    translate -l "ko" -img -u

  5. Magdagdag ng mga bagong pagsasalin ng markdown para sa Korean nang hindi naaapektuhan ang ibang mga pagsasalin:    translate -l "ko" -md

  6. Ayusin ang mga pagsasalin na may mababang confidence base sa mga naunang resulta ng pagsusuri: translate -l "ko" --fix

  7. Ayusin ang mga pagsasalin na may mababang confidence para sa mga partikular na file lamang (markdown): translate -l "ko" --fix -md

  8. Ayusin ang mga pagsasalin na may mababang confidence para sa mga partikular na file lamang (mga larawan): translate -l "ko" --fix -img

  9. Gamitin ang fast mode para sa pagsasalin ng larawan:    translate -l "ko" -img -f

  10. Ayusin ang mga pagsasalin na may mababang confidence gamit ang custom na threshold: translate -l "ko" --fix -c 0.8

  11. Halimbawa ng debug mode: - translate -l "ko" -d: Pinapagana ang debug logging.
  12. I-save ang mga log sa mga file: translate -l "ko" -s
  13. Console DEBUG at file DEBUG: translate -l "ko" -d -s
  14. Isalin nang hindi nagdadagdag ng machine translation disclaimers sa mga output: translate -l "ko" --no-disclaimer

  15. I-migrate ang mga link ng notebook para sa mga pagsasalin sa Korean (i-update ang mga link sa mga isinaling notebook kapag available):    migrate-links -l "ko"

  15. I-migrate ang mga link gamit ang dry-run (hindi nagsusulat sa file):    migrate-links -l "ko" --dry-run

  16. I-update lamang ang mga link kapag may mga isinaling notebook (huwag bumalik sa mga orihinal):    migrate-links -l "ko" --no-fallback-to-original

  17. Iproseso ang lahat ng wika na may prompt ng kumpirmasyon:    migrate-links -l "all"

  18. Iproseso ang lahat ng wika at awtomatikong kumpirmahin:    migrate-links -l "all" -y
  19. I-save ang mga log sa mga file para sa migrate-links:    migrate-links -l "ko ja" -s

### Mga Halimbawa ng Pagsusuri

> [!WARNING]  
> **Beta Feature**: Ang functionality ng pagsusuri ay kasalukuyang nasa beta. Ang tampok na ito ay inilabas upang suriin ang mga isinaling dokumento, at ang mga pamamaraan ng pagsusuri at detalyadong implementasyon ay patuloy pang dine-develop at maaaring magbago.

  1. Suriin ang mga pagsasalin sa Korean: evaluate -l "ko"

  2. Suriin gamit ang custom na confidence threshold: evaluate -l "ko" -c 0.8

  3. Mabilis na pagsusuri (rule-based lamang): evaluate -l "ko" -f

  4. Malalim na pagsusuri (LLM-based lamang): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->