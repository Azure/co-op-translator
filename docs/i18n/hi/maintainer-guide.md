# रखरखाव मार्गदर्शिका

यह पृष्ठ संक्षेप में बताता है कि API, CLI, और दस्तावेज़ साइट कैसे एक साथ जुड़े हुए हैं।

## सार्वजनिक API सीमा

स्थिर Python API निम्न स्थान से निर्यात किया गया है:

```python
co_op_translator.api
```

सार्वजनिक API को सामग्री अनुवाद हेल्पर्स, पाथ रीराइटिंग हेल्पर्स, परियोजना ऑर्केस्ट्रेशन, और समीक्षा में व्यवस्थित किया गया है:

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

नए सार्वजनिक API जोड़ने पर, इनको अपडेट करें:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

निचले स्तर के `core` मॉड्यूल्स को स्थिर API के रूप में दस्तावेज़ करने से बचें जब तक कि परियोजना उन्हें सीधे समर्थन करने का इरादा न रखती हो।

## CLI प्रवेश बिंदु

यह पैकेज इन Poetry स्क्रिप्ट्स को परिभाषित करता है:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` स्क्रिप्ट नाम के अनुसार डिस्पैच करता है:

- `translate` कॉल करता है `co_op_translator.cli.translate.translate_command`
- `evaluate` कॉल करता है `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` कॉल करता है `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` कॉल करता है `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` `__main__.py` को बाइपास करता है और सीधे `co_op_translator.mcp.server:main` को कॉल करता है।

CLI विकल्प जोड़ते या बदलते समय, अपडेट करें:

- संबंधित `src/co_op_translator/cli/*.py` कमांड
- `docs/cli.md`
- CLI-संबंधी टेस्ट, यदि व्यवहार बदलता है

## MCP सर्वर

MCP सर्वर में लागू किया गया है:

```python
co_op_translator.mcp.server
```

सर्वर जानबूझकर सार्वजनिक Python API को रैप करता है बजाय इसके कि वह निचले स्तर के `core` मॉड्यूल्स को कॉल करे। इस सीमा को बरकरार रखें ताकि MCP क्लाइंट्स, Python कॉलर्स, और CLI का व्यवहार समान रहे।

MCP टूल्स जोड़ते या बदलते समय, अपडेट करें:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` अगर सार्वजनिक API सतह बदलती है

रिपॉजिटरी अनुवाद उपकरण MCP के माध्यम से मॉडल-काल करने योग्य हैं और कई फाइलें लिख सकते हैं। डिफ़ॉल्ट के रूप में `dry_run=True` रखें और ड्राई-रन न होने वाले परियोजना अनुवाद से पहले `confirm_write=True` आवश्यक करें।

## अनुवाद प्रवाह

उच्च-स्तरीय परियोजना अनुवाद प्रवाह इस प्रकार है:

1. CLI आर्ग्यूमेंट्स या API पैरामीटर्स पार्स करें।
2. LLM कॉन्फ़िगरेशन को `LLMConfig` से सत्यापित करें।
3. जब इमेज अनुवाद चुना गया हो तो Azure AI Vision को सत्यापित करें।
4. भाषा कोड्स को सामान्यीकृत करें।
5. पुराने भाषा फ़ोल्डर उपनामों का पता लगाएँ।
6. अनुवाद मात्रा का अनुमान लगाएँ।
7. प्रासंगिक होने पर README भाषा/कोर्स अनुभागों को अपडेट करें।
8. परियोजना अनुवाद को `ProjectTranslator` को सौंपें।
9. `ProjectTranslator` फ़ाइल प्रसंस्करण को `TranslationManager` को सौंपता है।

`TranslationManager` विशेष फाइल-टाइप मिक्सिन्स से बना है:

- `ProjectMarkdownTranslationMixin` Markdown फ़ाइल पढ़ने, सामग्री अनुवाद, पाथ पुनःलेखन, मेटाडेटा, अस्वीकरण, और लिखने को संभालता है।
- `ProjectNotebookTranslationMixin` नोटबुक फ़ाइल पढ़ने, Markdown-सेल अनुवाद, पाथ पुनःलेखन, मेटाडेटा, अस्वीकरण, और लिखने को संभालता है।
- `ProjectImageTranslationMixin` इमेज की खोज, टेक्स्ट निकालना/अनुवाद, रेंडर की गई इमेज लिखना, और मेटाडेटा को संभालता है।

निचले-स्तर की सामग्री API परियोजना वर्कफ़्लो को छोड़ती हैं:

1. `translate_markdown_content` और `translate_notebook_content` केवल इन-मेमोरी सामग्री का अनुवाद करते हैं।
2. `translate_image_content` एक इमेज में टेक्स्ट का अनुवाद करता है और एक रेंडर की गई इमेज ऑब्जेक्ट लौटाता है।
3. `rewrite_markdown_paths` और `rewrite_notebook_paths` स्पष्ट पोस्ट-प्रोसेसिंग सहायक हैं। वे कोई अनुवाद या परियोजना लेखन नहीं करते।

## समीक्षा प्रवाह

निर्धारित समीक्षा प्रवाह इस प्रकार है:

1. CLI आर्ग्यूमेंट्स या API पैरामीटर्स पार्स करें।
2. अनुरोधित भाषा कोड्स को सामान्यीकृत करें।
3. एक या अधिक समीक्षा लक्ष्य बनाएं `root_dir`, `root_dirs`, या `groups` से।
4. वैकल्पिक रूप से स्रोत फ़ाइलों को `--changed-from` के साथ सीमित करें।
5. संरचना, अनुवाद ताजगी, Markdown अखंडता, और स्थानीय लिंक/इमेज पाथ के लिए निर्धारित जांच चलाएँ।
6. या तो टेक्स्ट आउटपुट या GitHub-स्वाद वाला Markdown प्रिंट करें।
7. जब समीक्षा त्रुटियाँ पाई जाएँ तो फेल्योर के साथ बाहर निकलें।

समीक्षा प्रवाह को API कीज़ की आवश्यकता नहीं होती और यह पुल रिक्वेस्ट CI के लिए उपयुक्त रहना चाहिए। पुल रिक्वेस्ट वर्कफ़्लो हर रन पर एक चेक सारांश लिखता है और केवल तभी PR टिप्पणी पोस्ट करता है जब `co-op-review` असफल होता है।

## डॉक्स साइट

डॉक्स साइट निम्न से कॉन्फ़िगर की जाती है:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` निर्देशिका प्रमुख दस्तावेज़ स्रोत है। इस निर्देशिका के बाहर नए एंड-यूज़र गाइड न जोड़ें जब तक कि परियोजना जानबूझकर कोई और प्रकाशित दस्तावेज़ सतह न पेश न करे।

स्थानीय रूप से बिल्ड करें:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

स्थानीय रूप से पूर्वावलोकन करें:

```bash
python -m mkdocs serve
```

जनरेट की गई साइट `site/` में लिखी जाती है, जिसे git द्वारा अनदेखा किया जाता है।

## GitHub Pages वर्कफ़्लो

`.github/workflows/docs.yml` पुल रिक्वेस्ट पर साइट को बिल्ड करता है और `main` पर पुश होने पर इसे डिप्लॉए करता है।

वर्कफ़्लो निम्न इंस्टॉल करता है:

```bash
pip install -r requirements-docs.txt
```

डॉक्स वर्कफ़्लो केवल डॉक्यूमेंटेशन टूलचेन इंस्टॉल करता है। `mkdocs.yml` `mkdocstrings` को `src/` की ओर इंगित करता है ताकि सार्वजनिक API पेज स्रोत ट्री से पूर्ण रनटाइम डिपेंडेंसी सेट इंस्टॉल किए बिना रेंडर किए जा सकें। यदि भविष्य के API डॉक्स को बिल्ड के दौरान वैकल्पिक रनटाइम प्रोवाइडर्स को इम्पोर्ट करने की आवश्यकता हो, तो `.github/workflows/docs.yml` और इस गाइड दोनों को एक साथ अपडेट करें।

## डॉक्स गुणवत्ता मानदंड

दस्तावेज़ परिवर्तनों को मर्ज करने से पहले, चलाएँ:

```bash
python -m mkdocs build --strict
git diff --check
```

कठोर बिल्ड्स का उपयोग करें ताकि टूटी हुई लिंकें, अमान्य नेविगेशन प्रविष्टियाँ, और API रेंडरिंग समस्याएँ जल्दी फेल हों।