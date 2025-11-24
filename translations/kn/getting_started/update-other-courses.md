<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-24T06:39:07+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "kn"
}
-->
# "ಇತರ ಕೋರ್ಸ್‌ಗಳು" ವಿಭಾಗವನ್ನು ನವೀಕರಿಸಿ (Microsoft Beginners repos)

ಈ ಮಾರ್ಗದರ್ಶಿ "ಇತರ ಕೋರ್ಸ್‌ಗಳು" ವಿಭಾಗವನ್ನು Co‑op Translator ಬಳಸಿ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸಮನ್ವಯಗೊಳಿಸುವುದು ಹೇಗೆ ಎಂಬುದನ್ನು ವಿವರಿಸುತ್ತದೆ, ಮತ್ತು ಎಲ್ಲಾ repos ಗಾಗಿ ಜಾಗತಿಕ ಟೆಂಪ್ಲೇಟನ್ನು ಹೇಗೆ ನವೀಕರಿಸಬೇಕು ಎಂಬುದನ್ನು ತಿಳಿಸುತ್ತದೆ.

- ಅನ್ವಯಿಸುತ್ತದೆ: Microsoft Beginners repositories ಮಾತ್ರ
- ಕೆಲಸ ಮಾಡುತ್ತದೆ: Co‑op Translator CLI ಮತ್ತು GitHub Actions
- ಟೆಂಪ್ಲೇಟು ಮೂಲ: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## ಶೀಘ್ರ ಪ್ರಾರಂಭ: ನಿಮ್ಮ repo ನಲ್ಲಿ ಸ್ವಯಂಚಾಲಿತ-ಸಮನ್ವಯವನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ

ನಿಮ್ಮ README ನಲ್ಲಿ "ಇತರ ಕೋರ್ಸ್‌ಗಳು" ವಿಭಾಗದ ಸುತ್ತ ಈ ಮಾರ್ಕರ್‌ಗಳನ್ನು ಸೇರಿಸಿ. Co‑op Translator ಪ್ರತಿ ಬಾರಿ ಈ ಮಾರ್ಕರ್‌ಗಳ ನಡುವೆ ಇರುವ ಎಲ್ಲವನ್ನು ಬದಲಾಯಿಸುತ್ತದೆ.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

ಪ್ರತಿ ಬಾರಿ Co‑op Translator CLI (ಉದಾ., `translate -l "<language codes>"`) ಅಥವಾ GitHub Actions ಮೂಲಕ ಕಾರ್ಯನಿರ್ವಹಿಸಿದಾಗ, ಈ ಮಾರ್ಕರ್‌ಗಳಿಂದ ಸುತ್ತುವರಿದ "ಇತರ ಕೋರ್ಸ್‌ಗಳು" ವಿಭಾಗವನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನವೀಕರಿಸುತ್ತದೆ.

> [!NOTE]
> ನೀವು ಈಗಾಗಲೇ ಇರುವ ಪಟ್ಟಿ ಹೊಂದಿದ್ದರೆ, ಅದನ್ನು ಈ ಮಾರ್ಕರ್‌ಗಳೊಂದಿಗೆ ಸುತ್ತುವರಿಸಿ. ಮುಂದಿನ ಕಾರ್ಯಾಚರಣೆಯಲ್ಲಿ ಅದನ್ನು ಇತ್ತೀಚಿನ ಮಾನದಂಡಿತ ವಿಷಯದಿಂದ ಬದಲಾಯಿಸಲಾಗುತ್ತದೆ.

---

## ಜಾಗತಿಕ ವಿಷಯವನ್ನು ಹೇಗೆ ಬದಲಾಯಿಸಬೇಕು

ನೀವು ಎಲ್ಲಾ Beginners repos ನಲ್ಲಿ ಕಾಣುವ ಮಾನದಂಡಿತ ವಿಷಯವನ್ನು ನವೀಕರಿಸಲು ಬಯಸಿದರೆ:

1. ಟೆಂಪ್ಲೇಟು ಸಂಪಾದಿಸಿ: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. ನಿಮ್ಮ ಬದಲಾವಣೆಗಳೊಂದಿಗೆ Co-op Translator repo ಗೆ pull request ಅನ್ನು ತೆರೆಯಿರಿ
3. PR ವಿಲೀನಗೊಂಡ ನಂತರ, Co‑op Translator ಆವೃತ್ತಿಯನ್ನು ನವೀಕರಿಸಲಾಗುತ್ತದೆ
4. ಗುರಿ repo ನಲ್ಲಿ Co‑op Translator (CLI ಅಥವಾ GitHub Action) ಮುಂದಿನ ಕಾರ್ಯಾಚರಣೆಯಲ್ಲಿ, ನವೀಕರಿಸಿದ ವಿಭಾಗವನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸಮನ್ವಯಗೊಳಿಸಲಾಗುತ್ತದೆ

ಇದು ಎಲ್ಲಾ Beginners repositories ನಲ್ಲಿ "ಇತರ ಕೋರ್ಸ್‌ಗಳು" ವಿಷಯಕ್ಕಾಗಿ ಒಂದು ಏಕಮೂಲ ಸತ್ಯವನ್ನು ಖಚಿತಪಡಿಸುತ್ತದೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸಮಾಕ್ಷ್ಯತೆ**:  
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಮಾಕ್ಷ್ಯತೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->