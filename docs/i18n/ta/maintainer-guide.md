# பராமரிப்பாளர் கையேடு

இந்த பக்கம் API, CLI மற்றும் ஆவண தளம் எவ்வாறு ஒன்றாக இணைக்கப்பட்டுள்ளன என்பதைக் சுருக்கமாகக் கூறுகிறது.

## பொது API எல்லை

நிலையான Python API இதிலிருந்து ஏற்றப்படுகிறது:

```python
co_op_translator.api
```

பொது API உள்ளடக்க மொழிபெயர்ப்பு உதவியாளர்கள், பாதை மீளுரைத்தல் உதவியாளர்கள், திட்ட ஒருங்கிணைப்பு மற்றும் பரிசீலனை ஆகியவையாக அமைக்கப்பட்டுள்ளது:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

புதிய பொது APIகளைச் சேர்க்கும் போது, பின்வரும்களை புதுப்பிக்கவும்:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- பொருந்தும் API சோதனைகள் `tests/co_op_translator/` கீழே, உதாரணமாக `test_api.py` அல்லது `test_review_api.py`

திட்டம் அவற்றை நேரடியாக ஆதரிக்க எண்ணானால் தவிர, `core` போன்ற குறைந்தநிலை தொகுப்புகளை நிலையான API என ஆவணமாக்குவதிலிருந்து தவிர்க்கவும்.

## CLI entry points

பேக்கேஜ் இவை Poetry ஸ்கிரிப்ட்களை வரையறுக்கிறது:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` ஸ்கிரிப்ட் பெயரின்படி இயக்கத்தை வினியோகிக்கிறது:

- `translate` `co_op_translator.cli.translate.translate_command` ஐ அழைக்கிறது
- `evaluate` `co_op_translator.cli.evaluate.evaluate_command` ஐ அழைக்கிறது
- `migrate-links` `co_op_translator.cli.migrate_links.migrate_links_command` ஐ அழைக்கிறது
- `co-op-review` `co_op_translator.cli.review.review_command` ஐ அழைக்கிறது

`co-op-translator-mcp` `__main__.py`ஐத் தவிர்த்து `co_op_translator.mcp.server:main` ஐ நேரடியாக அழைக்கிறது.

CLI விருப்பங்களைச் சேர்க்கும் அல்லது மாற்றும் போது, பின்வரும்களை புதுப்பிக்கவும்:

- சம்பந்தப்பட்ட `src/co_op_translator/cli/*.py` கட்டளை
- `docs/cli.md`
- நடத்தை மாற்றப்பட்டால் CLI தொடர்புடைய சோதனைகள்

## MCP server

MCP சர்வர் இங்கு நடைமுறைப்படுத்தப்பட்டுள்ளது:

```python
co_op_translator.mcp.server
```

சேவையகம் குறைந்தநிலையில் உள்ள `core` தொகுப்புகளை நேரடியாக அழைக்கும் பதிலாக பொது Python API-ஐ மடக்குகிறது. இந்த எல்லையை பாதுகாப்பதனால் MCP கிளையன்டுகள், Python அழைப்பாளர்கள் மற்றும் CLI ஒரே நடத்தை பகிர்வது உறுதி செய்யப்படுகிறது.

MCP கருவிகளை சேர்க்கும் அல்லது மாற்றும் போது, புதுப்பிக்கவும்:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` பொது API மேற்பரப்பில் மாற்றம் ஏற்பட்டால்

கிடைபிடி மொழிபெயர்ப்பு கருவிகள் MCP மூலம் மாடலைக் கூப்பிட்டு, பல கோப்புகளை எழுதக்கூடியவையாக இருக்கும். இயல்பாக `dry_run=True` ஐ வைத்திருங்கள் மற்றும் non-dry-run திட்ட மொழிபெயர்ப்புக்கு முன் `confirm_write=True` தேவைப்படும்ன்னு உரிமையை கேட்கவும்.

## Translation flow

மேல்நிலை திட்ட மொழிபெயர்ப்பின் ஓட்டம்:

1. CLI வாதங்கள் அல்லது API அளவுருக்களை பகுப்பாய்வு செய்க.
2. `LLMConfig` கொண்டு LLM கட்டமைப்பைச் சரிபார்க்கவும்.
3. பட மொழிபெயர்ப்பு தேர்ந்தெடுக்கப்பட்டால் Azure AI Vision ஐச் சரிபார்க்கவும்.
4. மொழிக் குறியீடுகளை சாதாரணப்படுத்தவும்.
5. பழைய மொழி கோப்புறை மாறுபெயர்களை கண்டறியவும்.
6. மொழிபெயர்ப்பு அளவை கணிக்கவும்.
7. பொருந்தும் போது README மொழி/course பிரிவுகளை புதுப்பிக்கவும்.
8. திட்ட மொழிபெயர்ப்பை `ProjectTranslator`க்கு ஒப்படிக்கவும்.
9. `ProjectTranslator` கோப்பு செயலாக்கத்தை `TranslationManager`-க்கு ஒப்படைக்கிறது.

`TranslationManager` குறிப்பிட்ட கோப்பு வகை mixin-களால் உருவாக்கப்பட்டுள்ளது:

- `ProjectMarkdownTranslationMixin` Markdown கோப்புகளின் வாசிப்பு, உள்ளடக்க மொழிபெயர்ப்பு, பாதை மறுஅரைத்தல், metadata, விலக்குறிப்புகள் மற்றும் எழுதுதல் ஆகியவற்றை கையாள்கிறது.
- `ProjectNotebookTranslationMixin` நோட்புக் கோப்புகளின் வாசிப்பு, Markdown-செல் மொழிபெயர்ப்பு, பாதை மறுஅரைத்தல், metadata, விலக்குறிப்புகள் மற்றும் எழுதுதல் ஆகியவற்றை கையாள்கிறது.
- `ProjectImageTranslationMixin` படங்களை கண்டுபிடித்தல், உரை எடுப்பு/மொழிபெயர்ப்பு, உருவாக்கப்பட்ட படங்களின் எழுதுதல் மற்றும் metadata ஆகியவற்றை கையாள்கிறது.

குறைந்தநிலை உள்ளடக்க APIகள் திட்டப் பணிநெறியை தவிர்க்கின்றன:

1. `translate_markdown_content` மற்றும் `translate_notebook_content` நினைவகத்தில் உள்ள உள்ளடக்கங்களை மட்டும் மொழிபெயர்க்கின்றன.
2. `translate_image_content` ஒரு படத்தில் உள்ள உரையை மொழிபெயர்க்கின்றது மற்றும் ஒரு உருவாக்கப்பட்ட படம் பொருளை திருப்பிப் தருகின்றது.
3. `rewrite_markdown_paths` மற்றும் `rewrite_notebook_paths` தெளிவான பின்னர் செயலாக்க உதவியாளர்கள். அவை எந்த மொழிபெயர்ப்பையும் அல்லது திட்ட எழுதுதலையும் செய்யாது.

## Review flow

தீர்மானப்பட்ட பரிசீலனை ஓட்டம்:

1. CLI வாதங்கள் அல்லது API அளவுருக்களை பகுப்பாய்வு செய்க.
2. கோரப்பட்ட மொழிக் குறியீடுகளை சீரமைக்கவும்.
3. `root_dir`, `root_dirs`, அல்லது `groups` இலிருந்து ஒன்று அல்லது அதற்கு மேற்பட்ட பரிசீலனை இலக்குகளை உருவாக்கவும்.
4. விரும்பின் `--changed-from` கொண்டு மூல கோப்புகளை வரையறுக்கவும்.
5. அமைப்பு, மொழிபெயர்ப்பின் புதுமைத்தன்மை, Markdown ஒருமை மற்றும் உள்ளூர் இணைப்பு/பட பாதைகளுக்கான தீர்மான சோதனைகளை இயக்கவும்.
6. உரை வெளியீடு அல்லது GitHub-சார்ந்த Markdown ஒன்றாக பிரிண்ட் செய்யவும்.
7. பரிசீலனை பிழைகள் கண்டுபிடிக்கப்பட்டால் தோல்வியுடன் வெளியேறு.

பரிசீலனை ஓட்டத்திற்கு API விசைகள் தேவையில்லை மற்றும் அது pull request CIக்குத் தகுதியானதாகவே இருக்க வேண்டும். புல் ரிக្វெஸ்ட் பணிநெறி ஒவ்வொரு ஓட்டத்திலும் ஒரு சரிபார்ப்பு சுருக்கத்தை எழுதுகிறது மற்றும் `co-op-review` தோல்வியடைந்தபோது மட்டுமே PR கருத்தை இடுகிறது.

## Documentation site

ஆவண தளம் இதினால் கட்டமைக்கப்பட்டுள்ளது:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` அடைவு அசல் ஆவண மூலமாகும். திட்டம் உண்மையில் மற்றொரு வெளியீட்டு ஆவண மேற்பரப்பை அறிமுகப்படுத்தவல்லது தவிர, இந்த அடைவுக்கு வெளியே புதிய இறுதி பயனர் வழிகாட்டிகளைச் சேர்க்காதீர்கள்.

Build locally:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview locally:

```bash
python -m mkdocs serve
```

உருவாக்கப்பட்ட தளம் `site/` அடைவிற்கு எழுதி வைக்கப்படுகிறது, இது git மூலம் புறக்கணிக்கப்படுகிறது.

## GitHub Pages workflow

`.github/workflows/docs.yml` புல் ரிக்வெஸ்டுகளில் தளத்தை கட்டி, `main`க்கு push செய்யும்போது அதை deploy செய்கிறது.

The workflow installs:

```bash
pip install -r requirements-docs.txt
```

ஆவணப் பணிநெறி மட்டும் ஆவண உபகரண சங்கிலியை நிறுவுகிறது. `mkdocs.yml` `mkdocstrings`-ஐ `src/` நோக்கி குறிக்கிறது, இதனால் பொது API பக்கங்கள் முழு ரன்டைம் சார்புகளை நிறுவாமலேயே மூலக் கோப்பு மரத்திலிருந்து உருவாக்கப்படலாம். எதிர்கால API ஆவணங்கள் பில்டின் போது விருப்ப ரன்டைம் வழங்குநர்களைப் இறக்குமதி செய்யவேண்டியமானால், `.github/workflows/docs.yml` மற்றும் இந்த கையேடையும் ஒரே நேரத்தில் புதுப்பிக்கவும்.

## Docs quality bar

ஆவண மாற்றங்களை ஒன்றிணைக்கும் முன், இயக்கு:

```bash
python -m mkdocs build --strict
git diff --check
```

உடைந்த இணைப்புகள், செல்லாத navigation நுழைவுகள் மற்றும் API வரைபடப் பிரச்சினைகள் விரைவில் தோல்வியடையச் செய்வதற்காக கடுமையான கட்டமைப்புகளைப் பயன்படுத்தவும்.