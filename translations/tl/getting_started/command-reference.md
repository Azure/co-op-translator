<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:31:39+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "tl"
}
-->
# Command reference
Nagbibigay ang **Co-op Translator** CLI ng ilang mga opsyon para i-customize ang proseso ng pagsasalin:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Isinasalin ang iyong proyekto sa mga tinukoy na wika. Halimbawa: translate -l "es fr de" ay nagsasalin sa Spanish, French, at German. Gamitin ang translate -l "all" para isalin sa lahat ng suportadong wika.
translate -l "language_codes" -u              | Ina-update ang mga pagsasalin sa pamamagitan ng pagtanggal ng mga kasalukuyang pagsasalin at muling paggawa nito. Babala: Tatanggalin nito ang lahat ng kasalukuyang pagsasalin para sa tinukoy na mga wika.
translate -l "language_codes" -img            | Isinasalin lamang ang mga image file.
translate -l "language_codes" -md             | Isinasalin lamang ang mga Markdown file.
translate -l "language_codes" -chk            | Sinusuri ang mga naisaling file para sa mga error at inuulit ang pagsasalin kung kinakailangan.
translate -l "language_codes" -d              | Pinapagana ang debug mode para sa detalyadong logging.
translate -l "language_codes" -r "root_dir"   | Tinutukoy ang root directory ng proyekto
translate -l "language_codes" -f              | Ginagamit ang fast mode para sa pagsasalin ng mga larawan (hanggang 3x na mas mabilis sa pag-plot ngunit may bahagyang epekto sa kalidad at pagkaka-align).
translate -l "language_codes" -y              | Awtomatikong kinukumpirma ang lahat ng prompt (kapaki-pakinabang para sa CI/CD pipelines)
translate -l "language_codes" --help          | detalye ng tulong sa loob ng CLI na nagpapakita ng mga magagamit na command

### Mga halimbawa ng paggamit:

  1. Default na kilos (magdagdag ng bagong pagsasalin nang hindi tinatanggal ang mga kasalukuyan):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Magdagdag lamang ng bagong pagsasalin ng mga larawan sa Korean (hindi tinatanggal ang mga kasalukuyang pagsasalin):    translate -l "ko" -img

  3. I-update ang lahat ng pagsasalin sa Korean (Babala: Tatanggalin nito ang lahat ng kasalukuyang pagsasalin sa Korean bago muling isalin):    translate -l "ko" -u

  4. I-update lamang ang mga larawan sa Korean (Babala: Tatanggalin nito ang lahat ng kasalukuyang larawan sa Korean bago muling isalin):    translate -l "ko" -img -u

  5. Magdagdag ng bagong pagsasalin ng markdown para sa Korean nang hindi naaapektuhan ang ibang pagsasalin:    translate -l "ko" -md

  6. Suriin ang mga naisaling file para sa mga error at subukang muli ang pagsasalin kung kinakailangan: translate -l "ko" -chk

  7. Suriin ang mga naisaling file para sa mga error at subukang muli ang pagsasalin (markdown lamang): translate -l "ko" -chk -md

  8. Suriin ang mga naisaling file para sa mga error at subukang muli ang pagsasalin (mga larawan lamang): translate -l "ko" -chk -img

  9. Gamitin ang fast mode para sa pagsasalin ng mga larawan:    translate -l "ko" -img -f

  10. Halimbawa ng debug mode: - translate -l "ko" -d: Paganahin ang debug logging.

**Pagtatanggol**:  
Ang dokumentong ito ay isinalin gamit ang serbisyong AI na pagsasalin [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.