# रखरखावकर्ता मार्गदर्शिका

यो पृष्ठले API, CLI, र डकुमेन्टेशन साइट कसरी जोडिएका छन् भन्ने सारांश प्रस्तुत गर्छ।

## सार्वजनिक API सीमा

स्थिर Python API निम्नबाट निर्यात गरिन्छ:

```python
co_op_translator.api
```

सार्वजनिक API सामग्री अनुवाद सहायकहरू, पथ पुन:लेखन सहायकहरू, प्रोजेक्ट समन्वयन, र समीक्षा मा व्यवस्थित गरिएको छ:

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

`TranslationStateProvider` होस्ट गरिएको एकीकरणहरूको लागि परिरक्षण सीमा हो।
यसले उत्पन्न गरिएको उम्मेदवारहरूलाई स्वीकार गरिएका बेसलाइनहरूबाट अलग राख्नुपर्छ ताकि
अनमर्ज गरिएको अनुवाद सत्यताको स्रोत नबनोस्।

नयाँ सार्वजनिक APIs थप्दा, अपडेट गर्नुहोस्:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

प्रोजेक्टले तिनीहरूलाई सिधै समर्थन गर्ने इरादा नभएसम्म, कम-स्तरका `core` मोड्युलहरूलाई स्थिर API को रूपमा डकुमेन्ट गर्नबाट बच्नुहोस्।

## CLI प्रवेश बिन्दुहरू

प्याकेजले यी Poetry स्क्रिप्टहरू परिभाषित गर्छ:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` स्क्रिप्ट नामअनुसार डिस्प्याच गर्छ:

- `translate` ले `co_op_translator.cli.translate.translate_command` लाई कल गर्छ
- `evaluate` ले `co_op_translator.cli.evaluate.evaluate_command` लाई कल गर्छ
- `migrate-links` ले `co_op_translator.cli.migrate_links.migrate_links_command` लाई कल गर्छ
- `co-op-review` ले `co_op_translator.cli.review.review_command` लाई कल गर्छ

`co-op-translator-mcp` ले `__main__.py` लाई बाइपास गरी सिधै `co_op_translator.mcp.server:main` लाई कल गर्छ।

CLI विकल्पहरू थप्दा वा परिवर्तन गर्दा, अपडेट गर्नुहोस्:

- the relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- CLI-सँग सम्बन्धित परीक्षणहरू, व्यवहार परिवर्तन भएमा

## MCP server

MCP सर्भर निम्नमा कार्यान्वित गरिएको छ:

```python
co_op_translator.mcp.server
```

सर्भरले जानेजानी सार्वजनिक Python API लाई र्याप गर्छ नकि कम-स्तरका `core` मोड्युलहरूलाई कल गर्छ। यो सीमा अक्षुण्ण राख्नुहोस् ताकि MCP क्लाइन्टहरू, Python कलरहरू, र CLI ले एउटै व्यवहार साझेदारी गरोस्।

MCP उपकरणहरू थप्दा वा परिवर्तन गर्दा, अपडेट गर्नुहोस्:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

रिपोजिटरी अनुवाद उपकरणहरू MCP मार्फत मोडल-कल योग्य छन् र धेरै फाइलहरू लेख्न सक्छन्। `dry_run=True` लाई डिफल्ट राख्नुहोस् र non-dry-run प्रोजेक्ट अनुवाद अघि `confirm_write=True` आवश्यक पार्नुहोस्।

## अनुवाद प्रवाह

उच्च-स्तरको प्रोजेक्ट अनुवाद प्रवाह यसरी छ:

1. CLI आर्गुमेन्टहरू वा API प्यारामिटरहरू पार्स गर्नुहोस्.
2. Validate LLM configuration with `LLMConfig`.
3. छवि अनुवाद चयन गर्दा Azure AI Vision लाई मान्य गर्नुहोस्।
4. Normalize language codes.
5. Detect legacy language folder aliases.
6. Estimate translation volume.
7. लागू परेमा README को भाषा/कोर्स सेक्सनहरू अद्यावधिक गर्नुहोस्.
8. Delegate project translation to `ProjectTranslator`.
9. `ProjectTranslator` delegates file processing to `TranslationManager`.

`TranslationManager` फाइल-प्रकार केन्द्रित मिक्सिनहरूबाट बनेको छ:

- `ProjectMarkdownTranslationMixin` ले Markdown फाइल पढाइ, सामग्री अनुवाद, पथ पुन:लेखन, मेटाडाटा, अस्वीकरणहरू, र लेखनहरू सम्हाल्छ।
- `ProjectNotebookTranslationMixin` ले नोटबुक फाइल पढाइ, Markdown-सेल अनुवाद, पथ पुन:लेखन, मेटाडाटा, अस्वीकरणहरू, र लेखनहरू सम्हाल्छ।
- `ProjectImageTranslationMixin` ले छवि पत्ता लगाउने, टेक्स्ट निकाल्ने/अनुवाद गर्ने, र रेंडर्ड इमेज लेख्ने तथा मेटाडाटा सम्हाल्छ।

कम-स्तरका सामग्री API हरूले प्रोजेक्ट वर्कफ्लो छोड्छन्:

1. `translate_markdown_content` and `translate_notebook_content` केवल इन-मेमोरी सामग्री अनुवाद गर्छन्।
2. `translate_image_content` ले एकल छविमा टेक्स्ट अनुवाद गर्छ र रेंडर्ड इमेज वस्तु फर्काउँछ।
3. `rewrite_markdown_paths` and `rewrite_notebook_paths` स्पष्ट पोस्ट-प्रोसेसिङ सहायकहरू हुन्। यीले कुनै अनुवाद गर्दैनन् र कुनै प्रोजेक्ट लेखन गर्दैनन्।

## समीक्षा प्रवाह

निर्णायक समीक्षा प्रवाह यस प्रकार छ:

1. CLI आर्गुमेन्टहरू वा API प्यारामिटरहरू पार्स गर्नुहोस्.
2. Normalize requested language codes.
3. `root_dir`, `root_dirs`, वा `groups` बाट एक वा बढी समीक्षा लक्ष्यहरू निर्माण गर्नुहोस्.
4. Optionally limit source files with `--changed-from`.
5. संरचना, अनुवाद ताजगी, Markdown अखण्डता, र स्थानीय लिंक/छवि पथहरूको लागि निर्धारक जाँचहरू चलाउनुहोस्।
6. टेक्स्ट आउटपुट वा GitHub-प्रकारको मार्कडाउन मध्ये कुनै एक प्रिन्ट गर्नुहोस्.
7. समीक्षा त्रुटिहरू भेटिएमा असफलतासहित निकास गर्नुहोस्.

समीक्षा प्रवाहले API कुञ्जीहरू आवश्यक गर्दैन र स्थानीय जाँचहरू वा इच्छानुसार उपभोक्ता CI का लागि उपलब्ध रहन्छ। यो रिपोजिटरी हरेक पुल अनुरोधमा `co-op-review` स्वचालित रूपमा चलाउँदैन।

## प्रलेखन साइट

डकुमेन्टेसन साइट यसले कन्फिगर गरिएको छ:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` निर्देशिका क्यानोनिकल डकुमेन्टेशन स्रोत हो। प्रोजेक्टले जान्जानेर अर्को प्रकाशित डकुमेन्टेसन सतह परिचय नगरिएको खण्डमा यस निर्देशिकाबाहिर नयाँ अन्त-प्रयोगकर्ता गाइडहरू नथप्नुहोस्।

स्थानीय रूपमा बिल्ड गर्नुहोस्:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

स्थानीय रूपमा पूर्वावलोकन गर्नुहोस्:

```bash
python -m mkdocs serve
```

उत्पन्न साइट `site/` मा लेखिन्छ, जुन git द्वारा बेवास्ता गरिएको हुन्छ।

## GitHub Pages कार्यप्रवाह

`.github/workflows/docs.yml` ले पुल अनुरोधहरूमा साइट बनाउँछ र `main` मा पुश हुँदा तैनाथ गर्छ।

वर्कफ्लोले निम्न इन्स्टल गर्छ:

```bash
pip install -r requirements-docs.txt
```

डक्स वर्कफ्लोले केवल डकुमेन्टेसन टुलचेन इन्स्टल गर्छ। `mkdocs.yml` ले `mkdocstrings` लाई `src/` तर्फ संकेत गर्छ ताकि सार्वजनिक API पृष्ठहरू स्रोत रूखबाट पूर्ण रनटाइम निर्भरता सेट इन्स्टल नगरी रेंडर गर्न सकियोस्। भविश्यमा API डकहरू बिल्डको समयमा वैकल्पिक रनटाइम प्रोभाइडरहरू आयात गर्न आवश्यक परेमा, दुवै `.github/workflows/docs.yml` र यो गाइड सँगै अपडेट गर्नुहोस्।

## प्रलेखन गुणस्तर मापदण्ड

डकुमेन्टेसन परिवर्तनहरू मर्ज गर्नु अघि, रन गर्नुहोस्:

```bash
python -m mkdocs build --strict
git diff --check
```

कडा बिल्डहरू प्रयोग गर्नुहोस् ताकि टुक्रिएको लिंकहरू, अमान्य नेभिगेशन प्रविष्टिहरू, र API रेंडरिङ समस्याहरू छिटो असफल हुन्।