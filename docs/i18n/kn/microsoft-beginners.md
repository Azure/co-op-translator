# Microsoft ಆರಂಭಿಕರ ರೆಪೊಸಿಟೋರಿಗಳು

ಈ ಪುಟವು Microsoft "For Beginners" ರೆಪೊಸಿಟೋರಿಗಳ ನಿರ್ವಾಹಕರಿಗಾಗಿ, ಅವುಗಳು ಹಂಚಿಕೊಂಡ "Other Courses" README ವಿಭಾಗವನ್ನು ಬಳಸುತ್ತಿರುವಾಗದಿರುತ್ತದೆ.

ಬಹುತೇಕ Co-op Translator ಬಳಕೆದಾರರಿಗೆ ಈ ಪುಟ ಅಗತ್ಯವಿಲ್ಲ.

## Auto-Sync the Other Courses Section

ನಿಮ್ಮ READMEದಲ್ಲಿರುವ "Other Courses" ವಿಭಾಗದ ಸುತ್ತ ಈ ಮಾರುಕಟ್ಟೆಗಳನ್ನು ಸೇರಿಸಿ:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

ಪ್ರತಿ ಬಾರಿ Co-op Translator CLI ಅಥವಾ GitHub Actions ಮೂಲಕ ಚಲಿಸಿದಾಗ, ಇದು ಮಾರುಕಟ್ಟೆಗಳ ನಡುವೆ ಇರುವ ವಿಷಯವನ್ನು ಪ್ಯಾಕೇಜ್ಡ್ ಟೆಂಪ್ಲೇಟಿನಿಂದ ಬದಲಿಸುತ್ತೆ.

## ಹಂಚಿಕೊಂಡ ಟೆಂಪ್ಲೇಟನ್ನು ನವೀಕರಿಸಿ

ಟೆಂಪ್ಲೇಟಿನ ಮೂಲ ಇವೆ:

```text
src/co_op_translator/templates/other_courses.md
```

ಹಂಚಿಕೊಂಡ ವಿಷಯವನ್ನು ನವೀಕರಿಸಲು:

1. ಟೆಂಪ್ಲೇಟನ್ನು ಸಂಪಾದಿಸಿ.
2. Co-op Translator ಗೆ pull request ತೆರೆಯಿರಿ.
3. ಬದಲಾವಣೆ ಬಿಡುಗಡೆಯಾದ ನಂತರ, ಗುರಿ ರೆಪೊಸಿಟರಿಯಲ್ಲಿ Co-op Translator ಅನ್ನು ರನ್ ಮಾಡಿ.

## Sparse Checkout ಸಲಹೆ

ಬಹುಪರಿಮಾಣದ ಕೋರ್ಸ್ ರೆಪೊಸಿಟೋರಿಗಳು ಅನೇಕ ಅನುವಾದಿತ ಫಲಿತಾಂಶಗಳನ್ನು ಒಳಗೊಂಡಿದ್ದರೆ ಕ್ಲೋನ್ ಮಾಡಲು ದುಬಾರಿಯಾಗಬಹುದು. ನೀವು ರಚಿಸಿದ ಭಾಷಾ ವಿಭಾಗಗಳಲ್ಲಿ ಈ ಸಲಹೆಯನ್ನು ಸೇರಿಸಬಹುದು:

```markdown
> **Prefer to Clone Locally?**
>
> This repository includes many language translations, which can significantly increase download size. To clone without translations, use sparse checkout:
>
> ```bash
> git clone --filter=blob:none --sparse https://github.com/org/repo.git
> cd repo
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
```