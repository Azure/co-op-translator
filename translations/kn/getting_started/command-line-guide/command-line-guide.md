<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c64ba65e091e5d87385490fa63a8f574",
  "translation_date": "2025-11-24T06:39:25+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "kn"
}
-->
# Co-op Translator ಕಮಾಂಡ್ ಲೈನ್ ಇಂಟರ್ಫೇಸ್ (CLI) ಬಳಸುವ ವಿಧಾನ

## ಅಗತ್ಯವಿರುವವುಗಳು

- **Python 3.10 ಅಥವಾ ಹೆಚ್ಚು**: Co-op Translator ಅನ್ನು ಚಲಾಯಿಸಲು ಅಗತ್ಯವಿದೆ.

## ವಿಷಯಗಳ ಪಟ್ಟಿಯು

1. [ಮೂಲ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ '.env' ಫೈಲ್ ಅನ್ನು ರಚಿಸಿ](./create-env-file.md)
   - ಆಯ್ದ ಭಾಷಾ ಮಾದರಿ ಸೇವೆಗೆ ಅಗತ್ಯವಿರುವ ಕೀಗಳನ್ನು ಸೇರಿಸಿ.
   - Azure Computer Vision ಕೀಗಳನ್ನು ಸೇರಿಸದಿದ್ದರೆ ಅಥವಾ `-md` ಅನ್ನು ನಿರ್ದಿಷ್ಟಪಡಿಸಿದರೆ, ಅನುವಾದಕವು Markdown ಮಾತ್ರ ಮೋಡ್‌ನಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ.
1. [Co-op translator ಪ್ಯಾಕೇಜ್ ಅನ್ನು ಸ್ಥಾಪಿಸಿ](./install-package.md)
1. [Co-op Translator ಬಳಸಿ ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಅನ್ನು ಅನುವಾದಿಸಿ](./translator-your-project.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:  
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳು ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->