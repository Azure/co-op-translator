# रखरखाव गाइड

यह पृष्ठ संक्षेप में बताता है कि API, CLI, और दस्तावेज़ साइट कैसे एक साथ जुड़े हुए हैं।

## सार्वजनिक API सीमा

स्थिर Python API निम्न से निर्यात किया गया है:

```python
co_op_translator.api
```

सार्वजनिक API को सामग्री अनुवाद सहायक, पथ पुनर्लेखन सहायक, परियोजना समन्वयन, और समीक्षा में व्यवस्थित किया गया है:

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

`TranslationStateProvider` होस्टेड एकीकरणों के लिए पर्सिस्टेंस सीमा है।
यह जनरेट किए गए उम्मीदवारों को स्वीकार किए गए बेसलाइनों से अलग रखना चाहिए ताकि एक
अनमर्ज अनुवाद सत्य का स्रोत न बन सके।

नए सार्वजनिक API जोड़ते समय, अपडेट करें:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- संबंधित API टेस्ट `tests/co_op_translator/` के अंतर्गत, जैसे `test_api.py` या `test_review_api.py`

प्रोजेक्ट सीधे उनका समर्थन करने का इरादा नहीं रखता हो तो निचले-स्तर के `core` मॉड्यूलों को स्थिर API के रूप में दस्तावेज़ करने से बचें।

## CLI प्रवेश बिंदु

पैकेज ये Poetry स्क्रिप्ट्स परिभाषित करता है:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` स्क्रिप्ट नाम द्वारा डिस्पैच करता है:

- `translate` कॉल करता है `co_op_translator.cli.translate.translate_command`
- `evaluate` कॉल करता है `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` कॉल करता है `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` कॉल करता है `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` सीधे `__main__.py` बायपास करता है और सीधे `co_op_translator.mcp.server:main` को कॉल करता है।

CLI विकल्प जोड़ते या बदलते समय, अपडेट करें:

- प्रासंगिक `src/co_op_translator/cli/*.py` कमांड
- `docs/cli.md`
- व्यवहार बदलने पर CLI-संबंधित टेस्ट

## MCP सर्वर

MCP सर्वर निम्न में लागू है:

```python
co_op_translator.mcp.server
```

सर्वर जानबूझकर सार्वजनिक Python API को रैप करता है बजाय इसके कि यह निचले-स्तर के `core` मॉड्यूल्स को कॉल करे। इस सीमा को अखंड रखें ताकि MCP क्लाइंट, Python कॉलर, और CLI एक समान व्यवहार साझा करें।

MCP टूल जोड़ते या बदलते समय, अपडेट करें:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- यदि सार्वजनिक API सतह बदलती है तो `docs/api.md`

रिपोजिटरी अनुवाद टूल MCP के माध्यम से मॉडल-काल करने योग्य हैं और कई फ़ाइलें लिख सकते हैं। डिफ़ॉल्ट के रूप में `dry_run=True` रखें और नॉन-ड्राय-रन परियोजना अनुवाद से पहले `confirm_write=True` आवश्यक करें।

## अनुवाद प्रवाह

उच्च-स्तरीय परियोजना अनुवाद प्रवाह यह है:

1. CLI आर्गुमेंट्स या API पैरामीटर पार्स करें।
2. `LLMConfig` के साथ LLM कॉन्फ़िगरेशन को सत्यापित करें।
3. जब इमेज अनुवाद चुना गया हो तब Azure AI Vision को सत्यापित करें।
4. भाषा कोड सामान्यीकृत करें।
5. विरासत भाषा फ़ोल्डर उपनामों का पता लगाएं।
6. अनुवाद मात्रा का अनुमान लगाएं।
7. लागू होने पर README भाषा/कोर्स अनुभाग अपडेट करें।
8. परियोजना अनुवाद को `ProjectTranslator` को सौंपें।
9. `ProjectTranslator` फ़ाइल प्रोसेसिंग को `TranslationManager` को सौंपता है।

`TranslationManager` विशेष फ़ाइल-प्रकार मिक्सिन्स से बना है:

- `ProjectMarkdownTranslationMixin` Markdown फ़ाइल पढ़ने, सामग्री अनुवाद, पथ पुनर्लेखन, मेटाडेटा, अस्वीकरण, और लिखने को संभालता है।
- `ProjectNotebookTranslationMixin` नोटबुक फ़ाइल पढ़ना, Markdown-सेल अनुवाद, पथ पुनर्लेखन, मेटाडाटा, अस्वीकरण, और लिखना संभालता है।
- `ProjectImageTranslationMixin` इमेज खोज, टेक्स्ट निष्कर्षण/अनुवाद, रेंडर की गई इमेज लिखना, और मेटाडेटा संभालता है।

निचले-स्तर की कंटेंट API परियोजना वर्कफ़्लो को छोड़ देती हैं:

1. `translate_markdown_content` और `translate_notebook_content` केवल इन-मेमोरी कंटेंट का अनुवाद करते हैं।
2. `translate_image_content` एक इमेज में मौजूद टेक्स्ट का अनुवाद करता है और एक रेंडर की गई इमेज ऑब्जेक्ट लौटाता है।
3. `rewrite_markdown_paths` और `rewrite_notebook_paths` स्पष्ट पोस्ट-प्रोसेसिंग सहायक हैं। वे न तो अनुवाद करते हैं और न ही परियोजना में कोई फ़ाइल लिखते हैं।

## समीक्षा प्रवाह

निर्धारित समीक्षा प्रवाह यह है:

1. CLI आर्गुमेंट्स या API पैरामीटर पार्स करें।
2. अनुरोधित भाषा कोड सामान्यीकृत करें।
3. `root_dir`, `root_dirs`, या `groups` से एक या अधिक समीक्षा लक्ष्य बनाएं।
4. वैकल्पिक रूप से स्रोत फ़ाइलों को `--changed-from` के साथ सीमित करें।
5. संरचना, अनुवाद ताज़गी, Markdown अखंडता, और स्थानीय लिंक/इमेज पाथ के लिए निर्धारित जाँच चलाएँ।
6. टेक्स्ट आउटपुट या GitHub-स्टाइल Markdown में प्रिंट करें।
7. जब समीक्षा त्रुटियाँ पाई जाती हैं तो विफलता के साथ बाहर निकलें।

समीक्षा प्रवाह के लिए API कुंजियाँ आवश्यक नहीं हैं और यह लोकल जाँचों या ऑप्ट-इन कंज्यूमर CI के लिए उपलब्ध रहता है। यह रिपोजिटरी हर पुल रिक्वेस्ट पर स्वतः `co-op-review` नहीं चलाती।

## दस्तावेज़ साइट

डॉक्स साइट का कॉन्फ़िगरेशन निम्न से किया गया है:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` डायरेक्टरी सामान्य प्रलेखन स्रोत है। इस डायरेक्टरी के बाहर नए एंड-यूज़र गाइड न जोड़ें जब तक परियोजना जानबूझकर कोई अन्य प्रकाशित दस्तावेज़ सतह पेश न करे।

स्थानीय रूप से बिल्ड करें:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

स्थानीय रूप से पूर्वावलोकन करें:

```bash
python -m mkdocs serve
```

जनरेट की गई साइट `site/` में लिखी जाती है, जिसे git द्वारा इग्नोर किया गया है।

## GitHub Pages वर्कफ़्लो

`.github/workflows/docs.yml` पुल रिक्वेस्ट पर साइट बिल्ड करता है और `main` पर पुश होने पर इसे डिप्लॉय करता है।

वर्कफ़्लो इंस्टॉल करता है:

```bash
pip install -r requirements-docs.txt
```

डॉक्स वर्कफ़्लो केवल डॉक्यूमेंटेशन टूलचेन इंस्टॉल करता है। `mkdocs.yml` `mkdocstrings` को `src/` की ओर इंगित करता है ताकि सार्वजनिक API पेज स्रोत ट्री से पूर्ण रनटाइम डिपेंडेंसी सेट इंस्टॉल किए बिना रेंडर किए जा सकें। यदि भविष्य के API डॉक्स को निर्माण के दौरान वैकल्पिक रनटाइम प्रोवाइडर्स को इम्पोर्ट करने की आवश्यकता हो, तो `.github/workflows/docs.yml` और इस गाइड दोनों को साथ अपडेट करें।

## डॉक्स गुणवत्ता मानक

डॉक्स में बदलाव मर्ज करने से पहले, चलाएँ:

```bash
python -m mkdocs build --strict
git diff --check
```

कठोर बिल्ड्स का उपयोग करें ताकि टूटे हुए लिंक, अमान्य नेविगेशन एंट्रीज़, और API रेंडरिंग समस्याएँ जल्दी ही फ़ेल कर सकें।