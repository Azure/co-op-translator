<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:29:27+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "tl"
}
-->
# Microsoft Co-op Translator Troubleshooting Guide


## Overview
Ang Microsoft Co-Op Translator ay isang makapangyarihang kasangkapan para sa tuloy-tuloy na pagsasalin ng mga Markdown na dokumento. Ang gabay na ito ay tutulong sa iyo na ayusin ang mga karaniwang problema kapag ginagamit ang tool.

## Common Issues and Solutions

### 1. Markdown Tag Issue
**Problem:** Ang isinalin na Markdown na dokumento ay may kasamang `markdown` tag sa itaas, na nagdudulot ng problema sa pagpapakita.

**Solution:** Para ayusin ito, tanggalin lamang ang `markdown` tag sa itaas ng file. Makakatulong ito upang maipakita nang tama ang Markdown file.

**Steps:**
1. Buksan ang isinaling Markdown (`.md`) na file.
2. Hanapin ang `markdown` tag sa itaas ng dokumento.
3. Tanggalin ang `markdown` tag.
4. I-save ang mga pagbabago sa file.
5. Buksan muli ang file upang matiyak na tama ang pagpapakita nito.

### 2. Embedded Images URL Issue
**Problem:** Ang mga URL ng naka-embed na mga larawan ay hindi tumutugma sa wika o locale, kaya nagreresulta sa maling o nawawalang mga larawan.

**Solution:** Suriin ang URL ng mga naka-embed na larawan at tiyaking tumutugma ito sa wika o locale. Lahat ng larawan ay nasa `translated_images` folder at bawat larawan ay may tag ng wika sa pangalan ng file.

**Steps:**
1. Buksan ang isinaling Markdown na dokumento.
2. Tukuyin ang mga naka-embed na larawan at ang kanilang mga URL.
3. Siguraduhing tumutugma ang wika o locale sa pangalan ng larawan sa wika ng dokumento.
4. I-update ang mga URL kung kinakailangan.
5. I-save ang mga pagbabago at buksan muli ang dokumento upang matiyak na tama ang pagpapakita ng mga larawan.

### 3. Translation Accuracy
**Problem:** Hindi tumpak ang isinaling nilalaman o kailangan pa ng karagdagang pag-edit.

**Solution:** Suriin ang isinaling dokumento at gawin ang kinakailangang mga pagbabago upang mapabuti ang katumpakan at pagiging madaling basahin.

**Steps:**
1. Buksan ang isinaling dokumento.
2. Maingat na suriin ang nilalaman.
3. Gawin ang mga kinakailangang pag-edit upang mapabuti ang katumpakan ng pagsasalin.
4. I-save ang mga pagbabago.

### 4. File Formatting Issues
**Problem:** Mali ang pag-format ng isinaling dokumento. Maaaring mangyari ito sa mga talahanayan; dito, ang karagdagang ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` ay tutugon sa mga isyu sa talahanayan.

**Steps:**
1. Buksan ang isinaling dokumento.
2. Ihambing ito sa orihinal na dokumento upang matukoy ang mga isyu sa pag-format.
3. Ayusin ang pag-format upang tumugma sa orihinal na dokumento.
4. I-save ang mga pagbabago.

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami na maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.