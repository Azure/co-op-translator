# मेंटेनर मार्गदर्शक

हे पृष्ठ API, CLI, आणि दस्तऐवजीकरण साइट एकत्र कशा प्रकारे जोडलेल्या आहेत याचा सारांश देते.

## सार्वजनिक API सीमा

स्थिर Python API खालीलपासून निर्यात केले जाते:

```python
co_op_translator.api
```

सार्वजनिक API चे आयोजन सामग्री अनुवाद सहाय्यक, मार्ग पुनर्लेखन सहाय्यक, प्रकल्प समन्वय, आणि पुनरावलोकन या विभागांत केलेले आहे:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
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

`TranslationStateProvider` हा होस्ट केलेल्या इंटिग्रेशन्ससाठी टिकवून ठेवण्याची सीमा आहे.
हे तयार केलेले उमेदवार स्वीकारलेल्या बेसलाइनपासून वेगळे ठेवले पाहिजेत जेणेकरून
अमर्ज न झालेला अनुवाद सत्याचा स्रोत बनू नये.

नवीन सार्वजनिक API जोडताना, अपडेट करा:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

प्रकल्प त्यांना थेट समर्थन देऊ इच्छित नसल्यास, खालच्या पातळीवरील `core` मॉड्युल्सना स्थिर API म्हणून दस्तऐवजीकरण करण्याचे टाळा.

## CLI प्रवेश बिंदू

पॅकेज मध्ये हे Poetry स्क्रिप्ट्स परिभाषित आहेत:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` स्क्रिप्ट नावानुसार डिस्पॅच करते:

- `translate` हे `co_op_translator.cli.translate.translate_command` ला कॉल करते
- `evaluate` हे `co_op_translator.cli.evaluate.evaluate_command` ला कॉल करते
- `migrate-links` हे `co_op_translator.cli.migrate_links.migrate_links_command` ला कॉल करते
- `co-op-review` हे `co_op_translator.cli.review.review_command` ला कॉल करते

`co-op-translator-mcp` `__main__.py` वगळून थेट `co_op_translator.mcp.server:main` ला कॉल करते.

CLI पर्याय जोडताना किंवा बदलताना, अद्यतन करा:

- the relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- वर्तन बदलल्यास CLI-संबंधी चाचण्या

## MCP server

MCP सर्व्हर खालील ठिकाणी अंमलात आणले गेले आहे:

```python
co_op_translator.mcp.server
```

सर्व्हर खालच्या पातळीवरील `core` मॉड्युल्सना कॉल करण्याऐवजी उद्देशपूर्वक सार्वजनिक Python API ला रॅप करते. हा सीमारेषा अखंड ठेवणे आवश्यक आहे जेणेकरून MCP क्लायंट्स, Python कॉलर्स, आणि CLI एकसारखे वर्तन शेअर करतील.

MCP टूल्स जोडताना किंवा बदलताना, अद्यतनित करा:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

रिपॉझिटरी अनुवाद साधने MCP मार्फत मॉडेल-कॉल करण्यायोग्य आहेत आणि अनेक फायली लिहू शकतात. डिफॉल्ट म्हणून `dry_run=True` ठेवा आणि नॉन-ड्राय-रन प्रोजेक्ट अनुवादापूर्वी `confirm_write=True` आवश्यक करा.

## अनुवाद प्रवाह

उच्च-स्तरीय प्रकल्प अनुवाद प्रवाह असा आहे:

1. CLI आर्ग्युमेंट्स किंवा API पॅरामीटर्स पार्स करा.
2. `LLMConfig` वापरून LLM कॉन्फिगरेशन सत्यापित करा.
3. इमेज अनुवाद निवडले गेल्यास Azure AI Vision चे सत्यापन करा.
4. भाषा कोड सामान्य करा.
5. जुन्या (legacy) भाषा फोल्डर उपनाम ओळखा.
6. अनुवाद प्रमाणाचा अंदाज लावा.
7. लागू असल्यास README मधील भाषा/कोर्स विभाग अद्यतित करा.
8. प्रोजेक्ट अनुवाद `ProjectTranslator` ला सोपवा.
9. `ProjectTranslator` फाइल प्रक्रिया `TranslationManager` कडे सोपवते.

`TranslationManager` फोकस केलेल्या फाईल-प्रकार मिक्सिन्समधून बनलेले आहे:

- `ProjectMarkdownTranslationMixin` Markdown फाइल वाचणे, सामग्री अनुवाद, पथ पुन्हा लिहिणे, मेटाडेटा, अस्वीकरणे आणि लेखन हाताळतो.
- `ProjectNotebookTranslationMixin` नोटबुक फाइल वाचन, Markdown-सेलचे अनुवाद, पथ पुन्हा लिहिणे, मेटाडेटा, अस्वीकरणे आणि लेखन हाताळतो.
- `ProjectImageTranslationMixin` प्रतिमा शोध, मजकूर काढणे/अनुवाद, रेंडर केलेल्या प्रतिमांचे लेखन आणि मेटाडेटा हाताळतो.

निम्न-स्तरीय कंटेंट API प्रोजेक्ट वर्कफ्लो वगळतात:

1. `translate_markdown_content` and `translate_notebook_content` translate in-memory content only.
2. `translate_image_content` एका इमेजमधील मजकूर अनुवादतो आणि एक रेंडर केलेले इमेज ऑब्जेक्ट परत करतो.
3. `rewrite_markdown_paths` आणि `rewrite_notebook_paths` स्पष्ट पोस्ट-प्रोसेसिंग सहाय्यक आहेत. ते कोणताही अनुवाद करीत नाहीत आणि प्रकल्पात कोणतेही लेखन करत नाहीत.

## पुनरावलोकन प्रवाह

The deterministic review flow is:

1. CLI आर्ग्युमेंट्स किंवा API पॅरामीटर्स पार्स करा.
2. विनंती केलेले भाषा कोड सामान्य करा.
3. `root_dir`, `root_dirs`, किंवा `groups` मधून एक किंवा अधिक पुनरावलोकन लक्ष्य तयार करा.
4. पर्यायीपणे स्रोत फाइल्स `--changed-from` ने मर्यादित करा.
5. स्ट्रक्चर, अनुवाद ताजेपणा, Markdown अखंडता, आणि स्थानिक लिंक/प्रतिमा पाथसाठी निर्धारित तपासण्या चालवा.
6. मजकूर आउटपुट किंवा GitHub-फ्लेवर्ड Markdown पैकी एक प्रदर्शित करा.
7. पुनरावलोकन चुका आढळल्यास अयशस्वी स्थितीने बाहेर पडा.

पुनरावलोकन प्रवाहासाठी API कींची आवश्यकता नाही आणि तो स्थानिक तपासणी किंवा ऑप्ट-इन कन्स्युमर CI साठी उपलब्ध राहतो. हा रिपॉझिटरी प्रत्येक पुल रिक्वेस्टवर आपोआप `co-op-review` चालवित नाही.

## दस्तऐवजीकरण साइट

डॉक्स साइट खालीलप्रमाणे कॉन्फिगर केली जाते:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` निर्देशिका ही प्रमाणिक दस्तऐवजीकरण स्रोत आहे. हा निर्देशिकेबाहेर नवीन end-user मार्गदर्शक जोडू नका, जोपर्यंत प्रकल्प उद्देशपूर्वक दुसरी प्रकाशित दस्तऐवजीकरण पृष्ठभाग सादर करत नाही.

Build locally:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview locally:

```bash
python -m mkdocs serve
```

The generated site is written to `site/`, which is ignored by git.

## GitHub Pages कार्यप्रवाह

`.github/workflows/docs.yml` पुल रिप्वेस्टवर साइट बिल्ड करतो आणि `main` वर पुश केल्यावर ते डिप्लॉय करतो.

The workflow installs:

```bash
pip install -r requirements-docs.txt
```

डॉक्स वर्कफ्लो फक्त दस्तऐवजीकरण टूलचेन स्थापित करते. `mkdocs.yml` `mkdocstrings` ला `src/` कडे निर्देशित करते, जेणेकरून संपूर्ण रनटाइम निर्भरता संच स्थापित न करता स्रोत ट्रीमधून सार्वजनिक API पृष्ठे रेंडर केली जाऊ शकतात. जर भविष्यातील API डॉक्सना बिल्ड दरम्यान ऐच्छिक रनटाइम प्रदाते आयात करण्याची गरज पडली, तर `.github/workflows/docs.yml` आणि हे मार्गदर्शक एकत्र अद्ययावत करा.

## दस्तऐवज गुणवत्ता निकष

Before merging documentation changes, run:

```bash
python -m mkdocs build --strict
git diff --check
```

कठोर बिल्ड वापरा जेणेकरून तुटलेले दुवे, अवैध नेव्हिगेशन एंट्रीज, आणि API रेंडरिंग समस्या लवकरच त्रुटी दाखवतील.