# ಸಮಸ್ಯೆ ಪರಿಹಾರ

Use this page when a translation run succeeds unexpectedly, fails during configuration, or produces output that needs review.

## ಇಲ್ಲಿ ಪ್ರಾರಂಭಿಸಿ

1. ಮೊದಲಿಗೆ ಕೇಂದ್ರೀಕೃತ ಆದೇಶವನ್ನು ಚಾಲನೆ ಮಾಡಿ, ಉದಾಹರಣೆಗೆ `translate -l "ko" -md`.
2. ಕನ್ಸೋಲ್ ಡಿಬಗ್ ಲಾಗ್ಗಳಿಗಾಗಿ `-d` ಸೇರಿಸಿ.
3. ಡಿಬಗ್ ಲಾಗ್‌ಗಳನ್ನು `<root-dir>/logs/` ಅಡಿಯಲ್ಲಿ ಉಳಿಸಲು `-s` ಸೇರಿಸಿ.
4. ಅನುವಾದದ ನಂತರ ತಾಜತ್ವ, ರಚನೆ, ಮತ್ತು ಸ್ಥಳೀಯ ಲಿಂಕ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಲು `co-op-review` ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## ಸಂರಚನಾ ದೋಷಗಳು

### ಭಾಷಾ ಮಾದರಿ ಪೂರೈಕೆದಾರರಿಲ್ಲ

ದೋಷ:

```text
No language model configuration found.
```

ಪರಿಹಾರ:

- Azure OpenAI ಅಥವಾ OpenAI ಅನ್ನು ಸಂರಚಿಸಿ.
- ಕಮಾಂಡ್ ಚಾಲನೆಯಾದ ಪರಿಸರದಲ್ಲಿ ವೇರಿಯಬಲ್‌ಗಳು ಇರುವುದನ್ನು ಪರಿಶೀಲಿಸಿ.
- ಸ್ಥಳೀಯ ಬಳಕೆಗೆ, ಅವುಗಳನ್ನು ಪ್ರಾಜೆಕ್ಟ್ ರೂಟ್‌ನಲ್ಲಿ `.env` ನಲ್ಲಿ ಇರಿಸಿ.

ವಿವರಗಳಿಗಾಗಿ [ಸಂರಚನೆ](configuration.md) ನೋಡಿ.

### Azure AI Vision ಇಲ್ಲದೆ ಚಿತ್ರ ಅನುವಾದ

ದೋಷ:

```text
Image translation requested but Azure AI Service is not configured.
```

ಪರಿಹಾರ:

- `AZURE_AI_SERVICE_API_KEY` ಅನ್ನು ಸೇರಿಸಿ.
- `AZURE_AI_SERVICE_ENDPOINT` ಅನ್ನು ಸೇರಿಸಿ.
- ಅಥವಾ `translate -l "ko" -md` ಎಂಬ ಪಠ್ಯ-ಮಾತ್ರ ಆದೇಶವನ್ನು ನಡೆಸಿ.

### ಅಮಾನ್ಯ ಕೀ ಅಥವಾ ಎಂಡ್ಪಾಯಿಂಟ್

ಲಕ್ಷಣಗಳಲ್ಲಿ `401`, ರಿಡ್ಯಾಕ್ಟೆಡ್ ಅನುಮತಿ ದೋಷಗಳು, ಅಥವಾ ಎಂಡ್ಪಾಯಿಂಟ್ ಪ್ರವೇಶ ದೋಷಗಳು ಸೇರಬಹುದು.

ಪರಿಹಾರ:

- ಕೀ ಆ ಎಂಡ್ಪಾಯಿಂಟ್ ಹೊಂದಿರುವ ಅದೇ Azure ಸಂಪನ್ಮೂಲಕ್ಕೆ ಸೇರಿರುವುದು ಎಂದು ದೃಢಪಡಿಸಿ.
- `-img` ಬಳಸುವಾಗ ಆ ಸಂಪನ್ಮೂಲವು Vision ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತಿದೆ ಎಂದು ದೃಢಪಡಿಸಿ.
- Azure OpenAI ನಿಯೋಜನಾ ಹೆಸರು ಮತ್ತು API ಆವೃತ್ತಿ ನಿಮ್ಮ ನಿಯೋಜನೆಯೊಂದಿಗೆ ಹೊಂದಾಣಿಕೆ ಹೊಂದಿದೆ ಎಂದು ದೃಢಪಡಿಸಿ.
- ಡಿಬಗ್ ಲಾಗ್‌ಗಳೊಂದಿಗೆ ಚಾಲನೆ ಮಾಡಿ: `translate -l "ko" -md -d -s`.

## ಯಾವುದೇ ಫೈಲ್‌ಗಳು ಅನುವಾದವಾಗಲಿಲ್ಲ

ಸಾಮಾನ್ಯ ಕಾರಣಗಳು:

- ಆಯ್ದ ಫ್ಲಾಗ್‌ಗಳು ನಿಮ್ಮ ಫೈಲ್‌ಗಳಿಗೆ ಹೊಂದಾಣಿಕೆ ಹೊಂದುತ್ತವೆಯೆಂದು ಖಚಿತವಾಗಿಲ್ಲ.
- ಇಲ್ಲಿದುವು ಈಗಾಗಲೇ ಅನುವಾದಿತ ಫೈಲ್‌ಗಳು ಇವೆ.
- ಮೂಲ ಫೈಲ್‌ಗಳು ಹೊರಗಿಟ್ಟ ಡೈರೆಕ್ಟರಿಗಳಲ್ಲಿ ಇವೆ.
- ಕಮಾಂಡ್ ತಪ್ಪಾದ ಪ್ರಾಜೆಕ್ಟ್ ರೂಟ್‌ನಿಂದ ಚಾಲನೆ ಆಗುತ್ತಿದೆ.

ಪರಿಶೀಲನೆಗಳು:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

ಕಮಾಂಡ್ ಪ್ರಾಜೆಕ್ಟ್ ರೂಟ್ ಹೊರಗಡೆ ಚಾಲನೆ ಆಗುತ್ತಿದ್ದರೆ `--root-dir` ಅನ್ನು ಬಳಸಿ.

## ಅನಿರೀಕ್ಷಿತ ಲಿಂಕ್ ವರ್ತನೆ

ಲಿಂಕ್ ಮರುಬರಹ ಆಯ್ದ ವಿಷಯ ಪ್ರಕಾರಗಳ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿದೆ:

- `-nb` included: notebook links can point to translated notebooks.
- `-nb` excluded: notebook links can remain pointed at source notebooks.
- `-img` included: image links can point to translated images.
- `-img` excluded: image links can remain pointed at source images.

ಒಟ್ಟು ಆಂತರಿಕ ಲಿಂಕ್‌ಗಳು ಅನುವಾದಿತ ಫಲಿತಾಂಶಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡಬೇಕಾದರೆ ಸಂಪೂರ್ಣ ವಿಷಯ ಅನುವಾದವನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ:

```bash
translate -l "ko" -md -nb -img
```

ಅನುವಾದದ ನಂತರ ಲಿಂಕ್ ಪರಿಶೀಲನೆಯನ್ನು ನಡೆಸಿ:

```bash
co-op-review -l "ko"
```

## ಮಾರ್ಕ್‌ಡೌನ್ ಪ್ರದರ್ಶನ ಸಮಸ್ಯೆಗಳು

ಅನುವಾದಿತ Markdown ತಪ್ಪಾಗಿ ಪ್ರದರ್ಶನವಾಗುತ್ತಿದ್ದರೆ:

- frontmatter `---` ರಿಂದ ಪ್ರಾರಂಭವಾಗುತ್ತದೆಯೇ ಮತ್ತು `---` ನಲ್ಲಿ ಕೊನೆಯಾಗುತ್ತದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ.
- ಕೋಡ್ ಫೆನ್ಸಿನ ಸಂಖ್ಯೆಗಳು ಮೂಲ ಮತ್ತು ಅನುವಾದಿತ ಫೈಲ್‌ಗಳ ನಡುವೆ ಹೊಂದಿಕೆಯಾಗಿದ್ದಾರಾ ಎಂದು ಪರಿಶೀಲಿಸಿ.
- ಸಾಮಾನ್ಯ ರಚನೆ ಸಮಸ್ಯೆಗಳನ್ನು ಹಿಡಿಯಲು `co-op-review` ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ.
- ಫಲಿತಾಂಶ ಹಾಳಾದರೆ ನಿರ್ದಿಷ್ಟ ಫೈಲ್ ಅನ್ನು ಪುನಃಅನುವಾದಿಸಿ.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action ಚಾಲಿತವಾದರೂ ಯಾವುದೇ Pull Request ರಚಿಸಲ್ಪಟ್ಟಿಲ್ಲ

If `peter-evans/create-pull-request` reports that the branch is not ahead of base, the workflow found no files to commit.

ಸಾಧ್ಯ ಕಾರಣಗಳು:

- ಅನುವಾದ ಚಾಲನೆಯು ಯಾವುದೇ ಬದಲಾವಣೆಗಳನ್ನು ನಿರ್ಮಿಸಲಿಲ್ಲ.
- `.gitignore` `translations/`, `translated_images/`, ಅಥವಾ ಅನುವಾದಿತ ನೋಟ್‌ಬುಕ್‌ಗಳನ್ನು ಹೊರಗಿಟ್ಟಿದೆ.
- `add-paths` ಜನರೇಟ್ ಮಾಡಿದ ಔಟ್‌ಪುಟ್ ಡೈರೆಕ್ಟರಿಗಳೊಡನೆ ಹೊಂದಿಕೆಯಾಗುತ್ತಿಲ್ಲ.
- ಅನುವಾದ ಹಂತವು ಮುಂಚಿತವಾಗಿ ನಿಲ್ಲಿತು.

ಸರಿ ಮಾಡುವ ಕ್ರಮಗಳು:

1. ಜನರೇಟ್ ಆದ ಫೈಲ್‌ಗಳು `translations/` ಅಥವಾ `translated_images/` ನಲ್ಲಿ_exist_ ಇರುವುದನ್ನು ದೃಢಪಡಿಸಿ.
2. `.gitignore` ಜನರೇಟ್ ಆದ ಔಟ್‌ಪುಟ್‌ಗಳನ್ನು ನಿರಾಕರಿಸುತ್ತಿಲ್ಲ ಎಂಬುದನ್ನು ದೃಢಪಡಿಸಿ.
3. ಹೋಲುವ `add-paths` ಅನ್ನು ಬಳಸಿ:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. ತಾತ್ಕಾಲಿಕವಾಗಿ ಡಿಬಗ್ ಫ್ಲಾಗ್‌ಗಳನ್ನು translate ಆಜ್ಞೆಗೆ ಸೇರಿಸಿ:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. ವರ್ಕ್‌ಫ್ಲೋ ಅನುಮತಿಯು ಕೆಳಕಂಡವುಗಳನ್ನು ಒಳಗೊಂಡಿರುವುದನ್ನು ದೃಢಪಡಿಸಿ:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## ಅನುವಾದ ಗುಣಮಟ್ಟ

ಯಂತ್ರ ಅನುವಾದಗಳಿಗೆ ಮಾನವ ಪರಿಶೀಲನೆ ಅಗತ್ಯವಾಗಬಹುದು. ಪ್ರಯೋಗಾತ್ಮಕ ಗುಣಮಟ್ಟದ ಸ್ಕೋರಿಂಗ್ ಮತ್ತು ಕಡಿಮೆ-ಆತ್ಮವಿಶ್ವಾಸದ ಮರುವೇಟನ ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ಬಯಸುವಾಗ ಮಾತ್ರ `evaluate` ಅನ್ನು ಬಳಸಿ.

!!! warning "Experimental"
    `evaluate` ನಿಯಮಾಧಾರಿತ ಮತ್ತು LLM-ಆಧಾರಿತ ತಪಾಸಣೆಗಳನ್ನು ಬಳಸಬಹುದು, ಮತ್ತು ಅದರ ಸ್ಕೋರಿಂಗ್ ಮಾದರಿ ಮತ್ತು ಮೆಟಾಡೇಟಾ ವರ್ತನೆ ಬದಲಾಗಬಹುದು. ನಿಮ್ಮ ಕಾರ್ಯಪ್ರವಾಹ ಬದಲಾವಣೆಗಳಿಗೆ ಸಿದ್ಧವಾಗದಿದ್ದರೆ ಇದನ್ನು ಅಗತ್ಯವಾದ CI ಗೇಟ್‌ಗಳ ಹೊರತಾಗಿಡಿ.

For deterministic CI checks, use `co-op-review` instead.