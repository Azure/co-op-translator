# रखरखाव मार्गदर्शक

हे पृष्ठ API, CLI आणि दस्तऐवजीकरण साइट कशा प्रकारे एकत्र जोडलेल्या आहेत हे सारांशित करते.

## सार्वजनिक API सीमा

स्थिर Python API खालील ठिकाणाहून एक्सपोर्ट केले जाते:

```python
co_op_translator.api
```

सार्वजनिक API सामग्री भाषांतर सहाय्यक, मार्ग पुनर्लेखन सहाय्यक, प्रकल्प समन्वय, आणि पुनरावलोकन असे विभागलेले आहे:

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

नवीन सार्वजनिक API जोडताना, पुढील अद्यतन करा:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

परियोजनेने थेट समर्थन देण्याचा हेतू नसल्यास कमी-स्तरीय `core` मॉड्यूल्सना स्थिर API म्हणून दस्तऐवजीकरण करणे टाळा.

## CLI प्रवेश बिंदू

पॅकेज या Poetry स्क्रिप्ट्स परिभाषित करते:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` स्क्रिप्ट नावानुसार डिस्पॅच करते:

- `translate` आह्वान करते `co_op_translator.cli.translate.translate_command`
- `evaluate` आह्वान करते `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` आह्वान करते `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` आह्वान करते `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` `__main__.py` बायपास करते आणि थेट `co_op_translator.mcp.server:main` ला कॉल करते.

CLI पर्याय जोडत किंवा बदलत असाल तर, अद्यतन करा:

- the relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- CLI-related tests, if behavior changes

## MCP server

MCP सर्व्हर पुढील ठिकाणी अंमलात आणला गेला आहे:

```python
co_op_translator.mcp.server
```

सर्व्हर जाणूनबुजून सार्वजनिक Python API ला रॅप करतो, कमी-स्तरीय `core` मॉड्यूल्स कॉल करण्याऐवजी. ही सीमा अखंड ठेवा जेणेकरून MCP क्लायंट्स, Python कॉलर्स, आणि CLI यांना एकसारखे वर्तन मिळेल.

MCP साधने जोडत किंवा बदलत असाल तर, अद्यतन करा:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

रेपॉझिटरी ट्रान्सलेशन टूल्स MCP मार्फत मॉडेल-कॉल करण्यायोग्य आहेत आणि अनेक फाइल्स लिहू शकतात. डीफॉल्ट म्हणून `dry_run=True` ठेवा आणि नॉन-ड्राय-रन प्रोजेक्ट ट्रान्सलेशनपूर्वी `confirm_write=True` आवश्यक ठेवा.

## भाषांतर प्रवाह

उच्च-स्तरीय प्रकल्प भाषांतर प्रवाह पुढीलप्रमाणे आहे:

1. CLI आर्ग्युमेंट्स किंवा API पॅरामिटर्स पार्स करा.
2. `LLMConfig` ने LLM कॉन्फिगरेशनची वैधता तपासा.
3. इमेज भाषांतर निवडल्यास Azure AI Vision ची वैधता तपासा.
4. भाषा कोड सामान्यीकरण करा.
5. जुने भाषा फोल्डर उपनावे ओळखा.
6. भाषांतराचे प्रमाण अंदाज करा.
7. लागू असल्यास README ची भाषा/कोर्स विभागे अपडेट करा.
8. प्रकल्प भाषांतर `ProjectTranslator` कडे सोपवा.
9. `ProjectTranslator` फाइल प्रक्रिया `TranslationManager` कडे सोपवते.

`TranslationManager` लक्ष केंद्रित फाईल-टाइप mixins पासून बनलेले आहे:

- `ProjectMarkdownTranslationMixin` Markdown फाइल वाचन, सामग्री भाषांतर, मार्ग पुनर्लेखन, मेटाडेटा, अस्वीकरणे, आणि लेखन हाताळते.
- `ProjectNotebookTranslationMixin` नोटबुक फाइल वाचन, Markdown-सेलचे भाषांतर, मार्ग पुनर्लेखन, मेटाडेटा, अस्वीकरणे, आणि लेखन हाताळते.
- `ProjectImageTranslationMixin` इमेज शोध, मजकूर काढणे/भाषांतर, रेंडर केलेल्या इमेजची लेखन, आणि मेटाडेटा हाताळते.

खाली-स्तरीय सामग्री API प्रकल्प वर्कफ्लो वगळतात:

1. `translate_markdown_content` आणि `translate_notebook_content` फक्त इन-मेमरी सामग्रीचे भाषांतर करतात.
2. `translate_image_content` एका इमेजमधील मजकूराचे भाषांतर करते आणि एक रेंडर केलेली इमेज ऑब्जेक्ट परत करते.
3. `rewrite_markdown_paths` आणि `rewrite_notebook_paths` स्पष्ट पोस्ट-प्रोसेसिंग सहाय्यक आहेत. त्या कोणतेही भाषांतर किंवा प्रकल्प लेखन करत नाहीत.

## पुनरावलोकन प्रवाह

निश्चित पुनरावलोकन प्रवाह पुढीलप्रमाणे आहे:

1. CLI आर्ग्युमेंट्स किंवा API पॅरामिटर्स पार्स करा.
2. विनंती केलेले भाषा कोड सामान्य करा.
3. एक किंवा अधिक पुनरावलोकन लक्ष्य `root_dir`, `root_dirs`, किंवा `groups` पासून तयार करा.
4. ऐच्छिकरीत्या स्रोत फायली `--changed-from` सोबत मर्यादित करा.
5. रचना, भाषांतर ताजेपणा, Markdown अखंडता, आणि स्थानिक लिंक/इमेज पाथसाठी निश्चित तपासण्या चालवा.
6. टेक्स्ट आउटपुट किंवा GitHub-शैलीतील Markdown प्रिंट करा.
7. पुनरावलोकन त्रुटी आढळल्यास अपयशी स्थितीसह बाहेर पडा.

पुनरावलोकन प्रवाहासाठी API की आवश्यक नाहीत आणि हे पुल रिक्वेस्ट CI साठी योग्य राहावे. पुल रिक्वेस्ट वर्कफ्लो प्रत्येक रनवर एक चेक सारांश लिहितो आणि फक्त तेव्हाच PR कमेंट पोस्ट करतो जेव्हा `co-op-review` अयशस्वी होते.

## दस्तऐवजीकरण साइट

डॉक्स साइट खालीलद्वारे कॉन्फिगर केलेली आहे:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` निर्देशिका ही प्रामाणिक दस्तऐवजीकरण स्त्रोत आहे. प्रकल्पाने हेतुपुरस्सर दुसरे प्रकाशित दस्तऐवजीकरण क्षेत्र ओळखून न दिले असल्यास या निर्देशिकेबाहेर नवीन एंड-यूजर मार्गदर्शक जोडू नका.

स्थानिक पद्धतीने बांधा:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

स्थानिकरित्या पूर्वावलोकन करा:

```bash
python -m mkdocs serve
```

निर्मित साइट `site/` मध्ये लिहिली जाते, जी git द्वारे नजरेआड केलेली आहे.

## GitHub Pages वर्कफ्लो

`.github/workflows/docs.yml` पुल रिक्वेस्टवर साइट बिल्ड करते आणि `main` वर पुश झाल्यावर ती तैनात करते.

वर्कफ्लो खालील गोष्टी इंस्टॉल करते:

```bash
pip install -r requirements-docs.txt
```

डॉक्स वर्कफ्लो फक्त दस्तऐवजीकरण टूलचेन इंस्टॉल करतो. `mkdocs.yml` `mkdocstrings` ला `src/` कडे निर्देशित करते जेणेकरून सार्वजनिक API पृष्ठे स्रोत वृक्षातून पूर्ण रनटाइम अवलंबित्व सेट इन्स्टॉल न करता रेंडर केली जाऊ शकतात. भविष्यात API डॉक्सना बिल्ड दरम्यान ऐच्छिक रनटाइम प्रोव्हायडर्स आयात करण्याची गरज भासली तर, `.github/workflows/docs.yml` आणि हा मार्गदर्शक दोन्ही एकत्र अद्यतन करा.

## दस्तऐवजीकरण गुणवत्ता निकष

दस्तऐवजीकरण बदल विलीन करण्यापूर्वी, चालवा:

```bash
python -m mkdocs build --strict
git diff --check
```

तुटलेले दुवे, अवैध नेव्हिगेशन एन्ट्रीज, आणि API रेंडरिंग समस्या लवकरच अयशस्वी होतील म्हणून कठोर बिल्ड वापरा.