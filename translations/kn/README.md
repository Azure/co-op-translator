# ಕೋ-ಆಪ್ ಅನುವಾದಕ

_ನಿಮ್ಮ ಯೋಜನೆ ವಿಕಸಿಸುತ್ತಿರುವಂತೆ, ಬಹುಭಾಷೆಗಳಲ್ಲಿ ನಿಮ್ಮ ಶೈಕ್ಷಣಿಕ GitHub ವಿಷಯಗಳ ಅನುವಾದಗಳನ್ನು ಸುಲಭವಾಗಿ ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸಿ ಮತ್ತು ನಿರ್ವಹಿಸಿ._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**ಇಲ್ಲಿಯಿಂದ ಪ್ರಾರಂಭಿಸಿ:** [Choose your workflow](https://azure.github.io/co-op-translator/workflows/) | [Configuration](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 ಬಹು-ಭಾಷಾ ಬೆಂಬಲ

#### Supported by [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](./README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ಸ್ಥಳೀಯವಾಗಿ ক্লೋನ್ ಮಾಡೋದು ಇಷ್ಟವೇ?**
>
> ಈ ರೆಪೊಸಿಟರಿ 50+ ಭಾಷೆಗಳ ಅನುವಾದಗಳನ್ನು ಒಳಗೊಂಡಿದೆ, ಅದು ಡೌನ್‌ಲೋಡ್ ಗಾತ್ರವನ್ನು ಬಹಾಗಿ ಹೆಚ್ಚಿಸುತ್ತದೆ. ಅನುವಾದಗಳನ್ನು ಹೊರತುಪಡಿಸಿ ಕ್ಲೋನ್ ಮಾಡಲು, sparse checkout ಬಳಸಿ:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> ಇದರಿಂದ ನೀವು курса ಪೂರ್ಣಗೊಳಿಸಲು ಬೇಕಾದ ಎಲ್ಲವನ್ನೂ ಕಡಿಮೆ ಡೌನ್‌ಲೋಡ್ ಸಮಯದ ಜೊತೆ ಪಡೆಯುತ್ತೀರಿ.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## ಅವಲೋಕನ

**ಕೋ-ಆಪ್ ಅನುವಾದಕ** ನಿಮ್ಮ ಶೈಕ್ಷಣಿಕ GitHub ವಿಷಯಗಳನ್ನು ಬಹುಭಾಷೆಗಳಲ್ಲಿ ಸುಲಭವಾಗಿ ಸ್ಥಳೀಯಗೊಳಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.
ನೀವು Markdown ಫೈಲ್‌ಗಳು, ಚಿತ್ರಗಳು ಅಥವಾ ನೋಟ್ಬುಕ್‌ಗಳನ್ನು ನವೀಕರಿಸಿದಾಗ, ಅನುವಾದಗಳು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸಿಂಕ್ರೊನೈಜ್ ಆಗುತ್ತವೆ ಮತ್ತು ನಿಮ್ಮ ವಿಷಯವು ವಿಶ್ವದ ವಿದ್ಯಾರ್ಥಿಗಳಿಗಾಗಿ ನಿಖರವಾಗಿಯೇ ಮತ್ತು ನವೀಕರಿಸಿದಂತೆಯೇ ಇರುತ್ತದೆ.

ಇದನ್ನು ರೆಪೊಸಿಟರಿ ಅನುವಾದಕ್ಕೆ CLI ಮೂಲಕ, ಸ್ವಯಂಚಾಲನಾ ಕೆಲಸಕ್ಕೆ Python API ಮೂಲಕ, ಅಥವಾ ಏಜೆಂಟ್ ಮತ್ತು ಸಂಪಾದಕ ವರ್ಕ್‍ಫ್ಲೋಗಳಿಗಾಗಿ MCP ಸರ್ವರ್ ಮೂಲಕ ಬಳಸಿ.

ಅನುವಾದಿತ ವಿಷಯವು ಹೇಗೆ ಸಂಘಟಿಸಲ್ಪಡುತ್ತದೆ ಎಂಬ ಉದಾಹರಣೆ:

![Example](../../imgs/translation-ex.png)

## ಯಾಕೆ ಕೋ-ಆಪ್ ಅನುವಾದಕ?

ಒಂದು ಫೈಲನ್ನು ಅನುವಾದಿಸುವುದು ಸುಲಭ. ಒಂದು ಸಂಪೂರ್ಣ ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ರೆಪೊಸಿಟರಿಯನ್ನು
ಅನುವಾದಿತವಾಗಿಟ್ಟು, ಲಿಂಕ್ ಮಾಡಿ ಮತ್ತು ನವೀಕರಿಸಿದಂತೆಯೇ ಇಟ್ಟುಕೊಳ್ಳುವುದು ಕಠಿಣ ಕಾರ್ಯ.

| Problem | How Co-op Translator helps |
| --- | --- |
| Long docs are not one prompt | ದೊಡ್ಡ Markdown ಫೈಲ್‌ಗಳು ಚಂಕ್‌ಗಳಾಗಿ ವಿಭಜಿಸಲಾಗುತ್ತವೆ, ಆದ್ದರಿಂದ ಒಂದು ದೀರ್ಘ README ಒಂದೇ ನಾಜೂಕಾದ ಮಾದರಿ ಪ್ರತಿಕ್ರಿಯೆಯ ಮೇಲೆ ಅವಲಂಬಿತವಾಗುವುದಿಲ್ಲ. ಯಾವುದೇ ಚಂಕ್ ವಿಫಲವಾದರೆ, ಕೋ-ಆಪ್ ಅನುವಾದಕ ಆ ವಿಫಲ ಭಾಗವನ್ನು ಮಾತ್ರ ಮರುಪ್ರಯತ್ನಿಸಿ ಮರು-ಚಂಕ್ ಮಾಡಬಹುದು. |
| Incomplete translations should not be marked current | ಕciosಡಾದ ಅನುವಾದವನ್ನು ಎಂದಿಗೂ ನವೀನವಾಗಿದೆ ಎಂದು ಚಿಹ್ನೆ ಮಾಡಬಾರದು. ಕೋ-ಆಪ್ ಅನುವಾದಕವು ಉಳಿಸುವ ಮೊದಲು ಅನುವಾದದ ಸಮಗ್ರತೆಯನ್ನು ಪರಿಶೀಲಿಸುತ್ತದೆ ಮತ್ತು ರಚನಾ ರೀತಿಯಲ್ಲಿ ಅಪೂರ್ಣವಿರುವ ಈಗಿನ ಅನುವಾದಗಳನ್ನು ಪತ್ತೆಹಚ್ಚಬಹುದು. |
| Links should match the translated repo structure | ಕೈಯಿಂದ ಮಾಡಿದ ಅನುವಾದಗಳು ಹೆಚ್ಚಿನವಾಗಿ ಸಾಪೇಕ್ಷ ಲಿಂಕ್‌ಗಳನ್ನು ಮೂಲ ಫೈಲ್ಗೆ ಸೂಚಿಸುವಂತೆ ಬಿಡುತ್ತವೆ. ಕೋ-ಆಪ್ ಅನುವಾದಕವು Markdown, ನೋಟ್ಬುಕ್, ಚಿತ್ರ ಮತ್ತು README ಲಿಂಕ್‌ಗಳನ್ನು `translations/<lang>/...` ರಚನೆಗೆ ಹೊಂದಿಸುವಂತೆ ಮರುಲೇಖನ ಮಾಡುತ್ತದೆ. |
| Translation should work across an entire repo | ಕೋ-ಆಪ್ ಅನುವಾದಕವು README ಫೈಲ್‌ಗಳು, ಡಾಕ್ಸ್, ನೋಟ್ಬುಕ್‌ಗಳು ಮತ್ತು ಚಿತ್ರ ಪಠ್ಯವನ್ನು ಒಟ್ಟಾರೆ ರೆಪೊಸಿಟರಿ ವರ್ಕ್‌ಫ್ಲೋ ಭಾಗವಾಗಿ ನಿರ್ವಹಿಸುತ್ತದೆ, ಫೈಲ್‌ಗಳನ್ನೊಂದು ಒಂದಾಗಿ ಅನುವಾದಿಸುವ ಬದಲು. |
| Maintaining translations matters more than creating them once | ಮೂಲ ಹ್ಯಾಶ್‌ಗಳು ಮತ್ತು ಅನುವಾದ ಮೆಟಾಡೇಟಾ ಕೋ-ಆಪ್ ಅನುವಾದಕಕ್ಕೆ ಅವಮಾನಗೊಳ್ಳಿದ ಫೈಲ್‌ಗಳನ್ನು ಕಂಡುಹಿಡಿಯಲು, ಬದಲಾವಣೆ ಇಲ್ಲದ ಫೈಲ್‌ಗಳನ್ನು ಉಳಿತಾಯ ಮಾಡಲು ಮತ್ತು ಮೂಲ ರೆಪೊ ಉದ್ಧಾರವಾಗುತ್ತಿರುವಂತೆ ಅನುವಾದಿತ ವಿಷಯವನ್ನು 同步 ನಿಗದಿಪಡಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ. |

## ಅನುವಾದ ಸ್ಥಿತಿಯನ್ನು ಹೇಗೆ ನಿರ್ವಹಿಸಲಾಗುತ್ತದೆ

ಕೋ-ಆಪ್ ಅನುವಾದಕ ಅನುವಾದಿತ ವಿಷಯವನ್ನು **ಆವೃತ್ತಿಯುಕ್ತ ಸಾಫ್ಟ್‌ವೇರ್ ಕಾರ್ಯಾಚರಣೆಗಳಾಗಿ** ನಿರ್ವಹಿಸುತ್ತದೆ,  
ಸ್ಥಿರ ಫೈಲ್‌ಗಳಾಗಿ ಅಲ್ಲ.

ಈ ಉಪಕರಣವು Markdown, ಚಿತ್ರಗಳು ಮತ್ತು ನೋಟ್ಬುಕ್‌ಗಳ ಅನುವಾದಿತ состಿತಿಯನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡುತ್ತದೆ
**ಭಾಷಾ-ವ್ಯಾಪ್ತ ಮೆಟಾಡೇಟಾ** ಬಳಸಿ.

ಈ ವಿನ್ಯಾಸ ಕೋ-ಆಪ್ ಅನುವಾದಕಕ್ಕೆ ಅವಕಾಶ ನೀಡುತ್ತದೆ:

- ಆವೃತ್ತಿ ಹಳೆಯಾದ ಅನುವಾದಗಳನ್ನು ನಂಬಿಕೆಯಿಂದ ಪತ್ತೆಹಚ್ಚಲು
- Markdown, ಚಿತ್ರಗಳು ಮತ್ತು ನೋಟ್ಬುಕ್‌ಗಳನ್ನು ಸಮ್ಮತವಾಗಿ ಚಿಕಿತ್ಸೆಮಾಡಲು
- ದೊಡ್ಡ, ವೇಗವಾಗಿ ಚಲಿಸುವ, ಬಹು-ಭಾಷಾ ರೆಪೊಸ್ ನಲ್ಲಿ ಸುರಕ್ಷಿತವಾಗಿ ಹೆಚ್ಚಾಗಲು

ಅನುವಾದಗಳನ್ನು ನಿರ್ವಹಿತ ಆರ್ಟಿಫ್ಯಾಕ್ಟ್‌ಗಳಾಗಿ ಮಾದರಿಮಾಡುವ ಮೂಲಕ,
ಅನುವಾದ ವರ್ಕ್‌ಫ್ಲೋಗಳು ಆಧುನಿಕ
ಸಾಫ್ಟ್‌ವೇರ್ ಅವಲಂಬನೆ ಮತ್ತು ಆರ್ಟಿಫ್ಯಾಕ್ಟ್ ನಿರ್ವಹಣಾ ಅಭ್ಯಾಸಗಳೊಂದಿಗೆ ಸ್ವಾಭಾವಿಕವಾಗಿ ಹೊಂದಿಕೊಳ್ಳುತ್ತವೆ.

→ [How translation state is managed](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### ಸಂಬಂಧಿತ ಆಳವಾದ ವಿಶ್ಲೇಷಣೆಗಳು

- [Fixing Broken Markdown in AI Translation: Hardening a Production Pipeline](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## ಪ್ರಾರಂಭಿಸುವುದು

ಕೋ-ಆಪ್ ಅನುವಾದಕವನ್ನು CLI, Python API, ಅಥವಾ MCP ಸರ್ವರ್‌ನಿಂದ ಬಳಸಬಹುದು. ಸ್ಥಳೀಯ ಅನುವಾದ, ಸ್ವಯಂಚಾಲನೆ, CI ಮತ್ತು ಏಜೆಂಟ್/ಸಂಪಾದಕ ಏಕೀಕರಣದ ನಡುವೆ ಆಯ್ಕೆ ಮಾಡುತ್ತಿರುವಾಗ ಕಾರ್ಯಪ್ರವಾಹ ಮಾರ್ಗದರ್ಶಿಯಿಂದ ಪ್ರಾರಂಭಿಸಿ.

- [Choose your workflow](../../docs/workflows.md)
- [Configure credentials](../../docs/configuration.md)
- [Translate from the CLI](../../docs/cli.md)
- [Automate with the Python API](../../docs/api.md)
- [Connect with the MCP Server](../../docs/mcp.md)
- [Run in GitHub Actions](../../docs/github-actions.md)

ವಿನ್ಯಾಸದ ನಂತರ ಕನಿಷ್ಠ CLI ಉದಾಹರಣೆ:

```bash
python -m venv .venv
# ವಿಂಡೋಸ್
.venv\Scripts\activate
# ಮ್ಯಾಕ್‌ಒಎಸ್/ಲಿನಕ್ಸ
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

ದೊಡ್ಡ ರೆಪೊಗಳ ಮೇಲೆ ಮೊದಲಿರನೆ ಚಾಲನೆಗಳಿಗಾಗಿ, ಅನುವಾದಿತ ಫೈಲ್‌ಗಳನ್ನು ಬರೆಯುವ ಮೊದಲು `--dry-run` ಬಳಸಿ. ವಿಷಯ ಪ್ರಕಾರದ ಫ್ಲಾಗ್‌ಗಳು, ಲಾಗ್‌ಗಳು, ಪರಿಶೀಲನೆ ಮತ್ತು ಲಿಂಕ್ ಸ್ಥಾಂತರದ ಕುರಿತು [CLI Reference](../../docs/cli.md) ನೋಡಿ.

Container ಸರಳ ಚಲನೆ Bash/Zshೊಂದಿಗೆ:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Container ಸರಳ ಚಲನೆ PowerShell ಜೊತೆಗೆ:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## ವೈಶಿಷ್ಟ್ಯಗಳು

- Markdown, ನೋಟ್ಬುಕ್‌ಗಳು ಮತ್ತು ಚಿತ್ರಗಳಿಗಾಗಿ ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದ
- ಮೂಲ ಬದಲಾವಣೆಗಳೊಂದಿಗೆ ಅನುವಾದಗಳನ್ನು ಸಾಮರಸ್ಯದಲ್ಲಿರಿಸುತ್ತದೆ
- ಸ್ಥಳೀಯವಾಗಿ (CLI) ಅಥವಾ CI (GitHub Actions) ನಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ
- MCP ಮೂಲಕ Markdown, ನೋಟ್ಬುಕ್, ಚಿತ್ರ, ವಿಮರ್ಶೆ ಮತ್ತು ಪ್ರಾಜೆಕ್ಟ್ ಅನುವಾದ ಸಾಧನಗಳನ್ನು ಅನಾವರಣ ಮಾಡುತ್ತದೆ
- ಪೂರೈಕೆದಾರ-ಬೆಂಬಲಿತ ಅನುವಾದಕ್ಕಾಗಿ Azure OpenAI ಅಥವಾ OpenAI ಬಳಸುತ್ತದೆ
- MCP ಅನ್ನು ಆಯೋಜಿಸುವ ಮೂಲಕ ಏಜೆಂಟ್‌ಗಳು Markdown ಮತ್ತು ನೋಟ್ಬುಕ್ ಚಂಕ್‌ಗಳನ್ನು ಕೋ-ಆಪ್ ಅನುವಾದಕ LLM ಕ್ರೆಡೆನ್ಷಿಯಲ್ಸ್ ಇಲ್ಲದೆ ಅನುವಾದಿಸಲುHosts ಮಾಡಲು ಅನುಮತಿಸುತ್ತದೆ
- ಚಿತ್ರ ಪಠ್ಯ ಹೊರತೆಗೆಮಕೆಗೆ ಮತ್ತು ಅನುವಾದಕ್ಕೆ Azure AI Vision ಬಳಸುತ್ತದೆ
- ನಿರ್ಧಾರಾತ್ಮಕ ಪರೀಕ್ಷೆಗಳ ಮೂಲಕ ಅನುವಾದದ ರಚನೆ ಮತ್ತು تازಾ स्थिति ಪರಿಶೀಲಿಸುತ್ತದೆ
- Markdown ಫಾರ್ಮ್ಯಾಟಿಂಗ್ ಮತ್ತು ರಚನೆಯನ್ನು ಸಂರಕ್ಷಿಸುತ್ತದೆ

## ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳು

- [Documentation site](https://azure.github.io/co-op-translator/)
- [Choose your workflow](../../docs/workflows.md)
- [Configuration](../../docs/configuration.md)
- [Azure AI Setup](../../docs/azure-ai-setup.md)
- [CLI Reference](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README languages template](../../docs/readme-languages-template.md)
- [Supported languages](../../docs/supported-languages.md)
- [Contributing](../../CONTRIBUTING.md)
- [Troubleshooting](../../docs/troubleshooting.md)

### ಮೈಕ್ರೋಸಾಫ್ಟ್-ನಿರ್ದಿಷ್ಟ ಮಾರ್ಗದರ್ಶಿ
> [!NOTE]
> ಮೈಕ್ರೋಸಾಫ್ಟ್ “For Beginners” ರೆಪೊಗಳ ನಿರ್ವಾಹಕರಿಗಾಗಿ ಮಾತ್ರ.

- [Updating the “other courses” list (for MS Beginners repositories only)](../../docs/microsoft-beginners.md)

## ನಮ್ಮನ್ನು ಬೆಂಬಲಿಸಿ ಮತ್ತು ಜಾಗತಿಕ ಕಲಿಕೆಯನ್ನು ಉತ್ತೇಜಿಸಿ

ಶೈಕ್ಷಣಿಕ ವಿಷಯವನ್ನು ಜಾಗತಿಕವಾಗಿ ಹಂಚುವ ರೀತಿಯನ್ನು ನಾವು ಪರಿವರ್ತಿಸಲು ನಮ್ಮೊಂದಿಗೆ ಸೇರಿ! GitHub ನಲ್ಲಿ [Co-op Translator](https://github.com/azure/co-op-translator) ಗೆ ⭐ ನೀಡಿ ಮತ್ತು ಕಲಿಕೆ ಮತ್ತು ತಂತ್ರಜ್ಞಾನದಲ್ಲಿ ಭಾಷಾ ಅಡಚಣೆಗಳನ್ನು ಮುರಿದುಹಾಕುವ ನಮ್ಮ ವಾರಸತೆಗೆ ಬೆಂಬಲ ನೀಡಿ. ನಿಮ್ಮ ಆಸಕ್ತಿ ಮತ್ತು ಕೊಡುಗೆಗಳು ಮಹತ್ವದ ಪರಿಣಾಮ ಬೀರುತ್ತವೆ! ಕೋಡ್ ಕೊಡುಗೆಗಳು ಮತ್ತು ವೈಶಿಷ್ಟ್ಯ ಶಿಫಾರಸುಗಳು ಯಾವಾಗಲೂ ಸ್ವಾಗತಾರ್ಹ.

### ನಿಮ್ಮ ಭಾಷೆಯಲ್ಲಿ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಶೈಕ್ಷಣಿಕ ವಿಷಯವನ್ನು ಅನ್ವೇಷಿಸಿ
- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## ವಿಡಿಯೋ ಪ್ರಸ್ತುತಿಗಳು

👉 YouTube‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಲು ಕೆಳಗಿನ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ.

- **Microsoft ನಲ್ಲಿ ತೆರೆಯಿರಿ**: Co-op Translator ಅನ್ನು ಬಳಸುವ ಬಗ್ಗೆ ಸಂಕ್ಷಿಪ್ತ 18 ನಿಮಿಷಗಳ ಪರಿಚಯ ಮತ್ತು ತ್ವರಿತ ಮಾರ್ಗದರ್ಶಿ.

  [![Microsoft ನಲ್ಲಿ ತೆರೆಯಿರಿ](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## ಕೊಡುಗೆಗಳು

ಈ ಪ್ರಾಜೆಕ್ಟ್ ಕೊಡುಗೆಗಳು ಮತ್ತು ಸಲಹೆಗಳನ್ನು ಸ್ವಾಗತಿಸುತ್ತದೆ. Azure Co-op Translator ಗೆ ಕೊಡುಗೆ ನೀಡಲು ಆಸಕ್ತಿ ಇದೆಯೆ? Co-op Translator ಅನ್ನು ಇನ್ನಷ್ಟು ಪ್ರವೇಶನೀಯಗೊಳಿಸಲು ನೀವು ಹೇಗೆ ಸಹಾಯ ಮಾಡಬಹುದು ಎಂಬ ಮಾರ್ಗದರ್ಶಿಗಾಗಿ ದಯವಿಟ್ಟು ನಮಗೆ [CONTRIBUTING.md](../../CONTRIBUTING.md) ಅನ್ನು ನೋಡಿ.

## ಕೊಡುಗೆಯವರು

[![co-op-translator ಕೊಡುಗையாளರು](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## ವರ್ತನೆ ಸಂಹಿತೆ

ಈ ಪ್ರಾಜೆಕ್ಟ್ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ಅನ್ನು ಅಳವಡಿಸಿಕೊಂಡಿದೆ.
ಇನ್ನಷ್ಟು ಮಾಹಿತಿಗಾಗಿ [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ಅನ್ನು ನೋಡಿ ಅಥವಾ ಯಾವುದೇ ಹೆಚ್ಚುವರಿ ಪ್ರಶ್ನೆಗಳು ಅಥವಾ ಕಾಮೆಂಟ್‌ಗಳಿಗಾಗಿ [opencode@microsoft.com](mailto:opencode@microsoft.com) ಅನ್ನು ಸಂಪರ್ಕಿಸಿ.

## ಜವಾಬ್ದಾರಿಯುತ AI

Microsoft ನಮ್ಮ ಗ್ರಾಹಕರು ನಮ್ಮ AI ಉತ್ಪನ್ನಗಳನ್ನು ಜವಾಬ್ದಾರಿಯಾಗಿ ಬಳಸಿಕೊಳ್ಳುವಂತೆ ಸಹಾಯ ಮಾಡುವುದು, ನಮ್ಮ ಪಾಠಗಳನ್ನು ಹಂಚಿಕೊಳ್ಳುವುದು, Transparency Notes ಮತ್ತು Impact Assessments ಹೀಗೆ ಉಪಕರಣಗಳ ಮೂಲಕ ನಂಬಿಕೆಯನ್ನು ಆಧರಿಸಿದ ಪಾಲುದಾರಿಕೆಗಳನ್ನು ನಿರ್ಮಿಸುವುದಕ್ಕೆ ಬದ್ಧವಾಗಿದೆ. ಈ ಸಂಪನ್ಮೂಲಗಳ ಬಹುತೇಕವನ್ನು [https://aka.ms/RAI](https://aka.ms/RAI) ನಲ್ಲಿ ಕಂಡುಹಿಡಿಯಬಹುದು.
Microsoft ನ ಜವಾಬ್ದಾರಿಯುತ AIಗಾಗಿ的方法ವು ನೇರವಾಗಿ ನ್ಯಾಯತೀತೆ, ವಿಶ್ವಾಸಾರ್ಹತೆ ಮತ್ತು ಭದ್ರತೆ, ಗೌಪ್ಯತೆ ಮತ್ತು ಭದ್ರತೆ, ಸಮಾವೇಶ, ಪಾರದರ್ಶಕತೆ, ಮತ್ತು ಹೊಣೆಗಾರಿಕೆ ಎಂಬ ನಮ್ಮ AI ತತ್ವಗಳ ಮೇಲೆ ಆಧಾರಿತವಾಗಿದೆ.

ದೊಡ್ಡ ಪ್ರಮಾಣದ ನೈಸರ್ಗಿಕ ಭಾಷೆ, ಚಿತ್ರ ಮತ್ತು ಧ್ವನಿ ಮಾದರಿಗಳು — ಈ ಉದಾಹರಣೆಯಲ್ಲಿ ಬಳಕೆಯಾದವುಗಳಂತೆ — ಅನ್ಯಾಯಕರ, ನಿರ್ಭರವಿಲ್ಲದ ಅಥವಾ ಅಪಮಾನಕಾರಿಯಾದ ರೀತಿಯಲ್ಲಿ ವರ್ತಿಸಬಹುದಾದ ಅವಕಾಶಗಳಿವೆ ಮತ್ತು ಪರಿಣಾಮವಾಗಿ ಹಾನಿ ಉಂಟುಮಾಡಬಹುದು. ಅಪಾಯಗಳು ಮತ್ತು ಮಿತಿಗಳ ಬಗ್ಗೆ ಮಾಹಿತಿ ಪಡೆಯಲು ದಯವಿಟ್ಟು [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ಅನ್ನು ಪರಾಮರ್ಶಿಸಿ.

ಈ ಅಪಾಯಗಳನ್ನು ಕಡಿಮೆಗೊಳಿಸುವ ಶಿಫಾರಸುಮಾಡಲಾದ ವಿಧಾನವೆಂದರೆ ನಿಮ್ಮ ಆರ್ಕಿಟೆಕ್ಚರ್‌ನಲ್ಲಿ ಹಾನಿಕರ ವರ್ತನೆಯನ್ನು ಪತ್ತೆ ಹಚ್ಚಿ ತಡೆಯುವಂತಹ ಸುರಕ್ಷತಾ ವ್ಯವಸ್ಥೆಯನ್ನು ಸೇರಿಸುವುದು. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ಅನ್ವಯಗಳು ಮತ್ತು ಸೇವೆಗಳಲ್ಲಿ ಬಳಕೆದಾರರ ಸೃಷ್ಟಿ ಮತ್ತು AI ಮೂಲಕ ಸೃಷ್ಟಿಯಾದ ಹಾನಿಕರ ವಿಷಯವನ್ನು ಪತ್ತೆಹಚ್ಚಲು ಸಾಮರ್ಥ್ಯದಿರುವ ಸ್ವತಂತ್ರ ರಕ್ಷಣಾ ಪದರವನ್ನು ಒದಗಿಸುತ್ತದೆ. Azure AI Content Safety ಪಠ್ಯ ಮತ್ತು ಚಿತ್ರ APIಗಳನ್ನು ಒಳಗೊಂಡಿದೆ, ಅವು ಹಾನಿಕರ ವಿಷಯವನ್ನು ಪತ್ತೆಹಾಕಲು ನಿಮಗೆ ಸಹಾಯ ಮಾಡುತ್ತವೆ. ನಾವು ವಿವಿಧ ಮಾದರಿಗಳಲ್ಲಿ ಹಾನಿಕರ ವಿಷಯವನ್ನು ಪತ್ತೆ ಹಚ್ಚಲು ನಿದರ್ಶನ ಕೋಡ್‌ಗಳನ್ನು ವೀಕ್ಷಿಸಲು, ಅನ್ವೇಷಿಸಲು ಮತ್ತು ಪ್ರಯತ್ನಿಸಲು ಅನುಮತಿಸುವ ಸಂವಹನಾತ್ಮಕ Content Safety Studio ಲಭ್ಯವಿದೆ. ಕೆಳಗಿನ [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ನಿಮಗೆ ಹೇಗೆ ಸೇವೆಗೆ ವಿನಂತಿಗಳನ್ನು ಮಾಡುವುದು ಎಂಬುದಕ್ಕೆ ಮಾರ್ಗದರ್ಶನ ನೀಡುತ್ತದೆ.

ಒಟ್ಟು ಅಪ್ಲಿಕೇಶನ್ ಕಾರ್ಯಕ್ಷಮತೆ ಮತ್ತೊಂದು ಪರಿಗಣನೀಯ ಅಂಶ. ಬಹು-ಮೋಡಲ್ ಮತ್ತು ಬಹು-ಮಾಡಲ್ ಅಪ್ಲಿಕೇಶನ್ಗಳಲ್ಲಿ, ಕಾರ್ಯಕ್ಷಮತೆ ಎಂಬದು ವ್ಯವಸ್ಥೆ ನೀವು ಮತ್ತು ನಿಮ್ಮ ಬಳಕೆದಾರರು ನಿರೀಕ್ಷಿಸುವಂತೆ ಕಾರ್ಯನಿರ್ವಹಿಸುವುದಾಗಿದ್ದು, ಹಾನಿಕರ ಔಟ್‌ಪುಟ್‌ಗಳನ್ನು ರಚಿಸದಿರುವುದನ್ನು ಒಳಗೊಂಡಿರುತ್ತದೆ. ನಿಮ್ಮ ಒಟ್ಟು ಅಪ್ಲಿಕೇಶನ್ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಅಳೆಯಲು [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ಅನ್ನು ಬಳಸಿ ಮೌಲ್ಯಮಾಪನ ಮಾಡುವುದು ಬಹುಮುಖ್ಯ.

ನೀವು ನಿಮ್ಮ ಡೆವಲಪ್‌ಮೆಂಟ್ ಪರಿಸರದಲ್ಲಿ [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ಉಪಯೋಗಿಸಿ ನಿಮ್ಮ AI ಅಪ್ಲಿಕೇಶನನ್ನು ಮೌಲ್ಯಮಾಪನ ಮಾಡಬಹುದು. ಪರೀಕ್ಷಾ ಡೇಟಾಸೆಟ್ ಅಥವಾ ಗುರಿಯನ್ನು ನೀಡಿದಾಗ, ನಿಮ್ಮ ಜನರೇಟಿವ್ AI ಅಪ್ಲಿಕೇಶನ್‌ನ ಜನರೇಷನ್‌ಗಳನ್ನು built-inಾನ್ಯ ಮೌಲ್ಯಮಾಪಕರು ಅಥವಾ ನೀವು ಆಯ್ಕೆಮಾಡಿದ ಕಸ್ಟಮ್ ಮೌಲ್ಯಮಾಪಕರ ಮೂಲಕ ಪ್ರಮಾಣಾತ್ಮಕವಾಗಿ ಅಳೆಯಲಾಗುತ್ತದೆ. ನಿಮ್ಮ ವ್ಯವಸ್ಥೆಯನ್ನು ಮೌಲ್ಯಮಾಪನ ಮಾಡಲು prompt flow SDK ನೊಂದಿಗೆ ಪ್ರಾರಂಭಿಸಲು, ನೀವು [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ಅನ್ನು ಅನುಸರಿಸಬಹುದು. ಒಂದು ಮೌಲ್ಯಮಾಪನ ಓಟವನ್ನು ನಡೆಸಿರುವ ಬಳಿಕ, ನೀವು [visualize the results in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) ನಲ್ಲಿ ಫಲಿತಾಂಶಗಳನ್ನು ದೃಶ್ಯೀಕರಿಸಬಹುದು.

## ಟ್ರೇಡ್‌ಮಾರ್ಕ್‌ಗಳು

ಈ ಪ್ರಾಜೆಕ್ಟ್ ಯೋಜನೆಗಳು, ಉತ್ಪನ್ನಗಳು, ಅಥವಾ ಸೇವೆಗಳ ಟ್ರೇಡ್‌ಮಾರ್ಕ್‌ಗಳು ಅಥವಾ ಲೋಗೋಗಳನ್ನು ಒಳಗೊಂಡಿರಬಹುದು. Microsoft ಟ್ರೇಡ್‌ಮಾರ್ಕ್‌ಗಳು ಅಥವಾ ಲೋಗೋಗಳ ಮಾನ್ಯ ಬಳಕೆ [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) ಅನ್ನು ಅನುಸರಿಸಬೇಕು ಮತ್ತು ಅದರ ನಿಯಮಗಳಿಗೆ ಒಳಪಟ್ಟಿರುತ್ತದೆ.
ಈ ಪ್ರಾಜೆಕ್ಟ್‌ನ ತಿದ್ದುಪಡಿಸಲಾದ ಆವೃತ್ತಿಗಳಲ್ಲಿ Microsoft ಟ್ರೇಡ್‌ಮಾರ್ಕ್‌ಗಳು ಅಥವಾ ಲೋಗೋಗಳನ್ನು ಬಳಸುವಾಗ ಗೊಂದಲ ಉಂಟುಮಾಡಬಾರದು ಅಥವಾ Microsoft ಪ್ರಾಯೋಜನೆಯನ್ನು ಸೂಚಿಸಬಾರದು.
ತೃತೀಯ ಪಕ್ಷದ ಟ್ರೇಡ್‌ಮಾರ್ಕ್‌ಗಳು ಅಥವಾ ಲೋಗೋಗಳ ಯಾವುದೇ ಬಳಕೆ ಅದಕ್ಕೆ ಸಂಬಂಧಿಸಿದ ತೃತೀಯ ಪಕ್ಷದ ನೀತಿಗಳಿಗೆ ಒಳಪಡುತ್ತದೆ.

## ಸಹಾಯ ಪಡೆಯುವುದು

ನೀವು ಅಡೆತಡೆಯಾಗಿದರೆ ಅಥವಾ AI ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವ ಬಗ್ಗೆ ಯಾವುದೇ ಪ್ರಶ್ನೆಗಳಿದ್ದರೆ, ಸೇರಿ:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

ನೀವು ನಿರ್ಮಿಸುವಾಗ ಉತ್ಪನ್ನ ಪ್ರತಿಕ್ರಿಯೆ ಅಥವಾ ದೋಷಗಳು ಇದ್ದರೆ ಭೇಟಿ ಮಾಡಿ:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)