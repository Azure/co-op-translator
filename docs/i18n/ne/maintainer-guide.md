# मेन्टेनर मार्गदर्शिका

यो पृष्ठले API, CLI, र दस्तावेज साइट कसरी एकसाथ जोडिएका छन् भनी संक्षेपमा बताउँछ।

## सार्वजनिक API सीमा

स्थिर Python API बाट निर्यात गरिन्छ:

```python
co_op_translator.api
```

सार्वजनिक API सामग्री अनुवाद सहायकहरू, पथ पुन:लेखन सहायकहरू, परियोजना संयोजन, र समीक्षा अन्तर्गत व्यवस्थित गरिएको छ:

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

नयाँ सार्वजनिक API थप्दा, यी अद्यावधिक गर्नुहोस्:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- सम्बन्धित API परीक्षणहरू `tests/co_op_translator/` भित्र, जस्तै `test_api.py` वा `test_review_api.py`

परियोजनाले तिनलाई सिधै समर्थन गर्ने योजना नभएको अवस्थामा कम-स्तरको `core` मोड्युलहरूलाई स्थिर API को रूपमा दस्तावेजमा समावेश नगर्नुहोस्।

## CLI प्रवेश बिन्दुहरू

प्याकेजले यी Poetry स्क्रिप्टहरू परिभाषित गर्दछ:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` स्क्रिप्ट नामअनुसार डिस्प्याच गर्दछ:

- `translate` ले `co_op_translator.cli.translate.translate_command` लाई कल गर्छ
- `evaluate` ले `co_op_translator.cli.evaluate.evaluate_command` लाई कल गर्छ
- `migrate-links` ले `co_op_translator.cli.migrate_links.migrate_links_command` लाई कल गर्छ
- `co-op-review` ले `co_op_translator.cli.review.review_command` लाई कल गर्छ

`co-op-translator-mcp` ले `__main__.py` छोड्छ र सिधै `co_op_translator.mcp.server:main` लाई कल गर्छ।

CLI विकल्प थप्दा वा परिवर्तन गर्दा, निम्न अद्यावधिक गर्नुहोस्:

- सम्बन्धित `src/co_op_translator/cli/*.py` कमाण्ड
- `docs/cli.md`
- CLI-सम्बन्धित परीक्षणहरू, यदि व्यवहार परिवर्तन हुन्छ भने

## MCP सर्भर

MCP सर्भर निम्नमा कार्यान्वित गरिएको छ:

```python
co_op_translator.mcp.server
```

सर्भरले जानबुझेर सार्वजनिक Python API लाई र्याप गर्छ, तलको स्तरका `core` मोड्युलहरूलाई कल नगरी। यो सीमा अपरिवर्तित राख्नुहोस् ताकि MCP क्लाइन्टहरू, Python कल गर्नेहरू, र CLI ले एउटै व्यवहार साझा गरोस्।

MCP उपकरणहरू थप्दा वा परिवर्तन गर्दा, यी अद्यावधिक गर्नुहोस्:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- यदि सार्वजनिक API सतह परिवर्तन हुन्छ भने `docs/api.md`

रिपोजिटरी अनुवाद उपकरणहरू MCP मार्फत मोडेल-कलयोग्य छन् र धेरै फाइलहरू लेख्न सक्छन्। डिफल्टका रूपमा `dry_run=True` राख्नुहोस् र non-dry-run परियोजना अनुवाद अघि `confirm_write=True` आवश्यक बनाउनुहोस्।

## अनुवाद प्रवाह

उच्च-स्तरीय परियोजना अनुवाद प्रवाह यस्तो छ:

1. CLI आर्गुमेन्टहरू वा API प्यारामिटरहरू पार्स गर्नुहोस्।
2. `LLMConfig` प्रयोग गरेर LLM कन्फिगरेसन मान्य गर्नुहोस्।
3. इमेज अनुवाद छानिएको बेला Azure AI Vision मान्य गर्नुहोस्।
4. भाषा कोडहरू सामान्यीकरण गर्नुहोस्।
5. पुराना भाषा फोल्डर उपनामहरू पत्ता लगाउनुहोस्।
6. अनुवादको परिमाण अनुमान लगाउनुहोस्।
7. लागू भएको बेला README भाषा/कोर्स खण्डहरू अद्यावधिक गर्नुहोस्।
8. परियोजना अनुवाद `ProjectTranslator` लाई सुपुर्द गर्नुहोस्।
9. `ProjectTranslator` ले फाइल प्रशोधन `TranslationManager` लाई सुपुर्द गर्छ।

`TranslationManager` लक्षित फाइल-प्रकार मिक्सिनहरूबाट बनेको छ:

- `ProjectMarkdownTranslationMixin` Markdown फाइल पढाइ, सामग्री अनुवाद, पथ पुन:लेखन, मेटाडाटा, डिस्क्लेमरहरू, र लेखनहरू सम्हाल्छ।
- `ProjectNotebookTranslationMixin` नोटबुक फाइल पढाइ, Markdown-सेल अनुवाद, पथ पुन:लेखन, मेटाडाटा, डिस्क्लेमरहरू, र लेखनहरू सम्हाल्छ।
- `ProjectImageTranslationMixin` इमेज खोज, पाठ निकासा/अनुवाद, रेंडर्ड इमेज लेखनहरू, र मेटाडाटा सम्हाल्छ।

कम-स्तरको सामग्री API हरू परियोजना कार्यप्रवाह छोड्छन्:

1. `translate_markdown_content` र `translate_notebook_content` ले केवल मेमोरीमा रहेको सामग्री अनुवाद गर्छन्।
2. `translate_image_content` ले एउटै इमेजमा रहेको टेक्स्ट अनुवाद गर्छ र एक रेंडर्ड इमेज वस्तु फर्काउँछ।
3. `rewrite_markdown_paths` र `rewrite_notebook_paths` स्पष्ट पोस्ट-प्रोसेसिङ सहायक हुन्। तिनीहरूले कुनै अनुवाद वा परियोजना लेखन गर्दैनन्।

## समीक्षा प्रवाह

निर्धारित समीक्षा प्रवाह यस्तो छ:

1. CLI आर्गुमेन्टहरू वा API प्यारामिटरहरू पार्स गर्नुहोस्।
2. अनुरोध गरिएको भाषा कोडहरू सामान्यीकरण गर्नुहोस्।
3. `root_dir`, `root_dirs`, वा `groups` बाट एक वा बढी समीक्षा लक्ष्यहरू बनाउनुहोस्।
4. वैकल्पिक रूपमा स्रोत फाइलहरू `--changed-from` सँग सीमित गर्नुहोस्।
5. संरचना, अनुवाद ताजगी, Markdown अखण्डता, र स्थानीय लिंक/इमेज पथहरूको लागि निर्धारित जाचहरू चलाउनुहोस्।
6. टेक्स्ट आउटपुट वा GitHub-flavored Markdown मध्ये कुनै एक प्रिन्ट गर्नुहोस्।
7. समीक्षा त्रुटिहरू फेला परेमा असफलतासहित बाहिर निस्किनुहोस्।

समीक्षा प्रवाहले API कुञ्जीहरू आवश्यक पर्दैन र pull request CI का लागि उपयुक्त रहनुपर्छ। Pull request कार्यप्रवाहले हरेक रनमा एक चेक सारांश लेख्छ र केवल `co-op-review` असफल हुँदा मात्रै PR टिप्पणी पोस्ट गर्छ।

## डकुमेन्टेसन साइट

डकुमेन्टेसन साइट निम्नद्वारा कन्फिगर गरिएको छ:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` निर्देशिका प्रमाणिक दस्तावेज स्रोत हो। परियोजनाले जानबुझेर अर्को प्रकाशित दस्तावेज सतह प्रस्तुत नगरेसम्म यस निर्देशिकाको बाहिर नयाँ अन्त-प्रयोगकर्ता मार्गदर्शकहरू थप्नुहोस् हुन्न।

लोकलमा बनाउनुहोस्:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

लोकलमा पूर्वावलोकन गर्नुहोस्:

```bash
python -m mkdocs serve
```

उत्पन्न साइट `site/` मा लेखिन्छ, जुन git द्वारा ignore गरिएको छ।

## GitHub Pages कार्यप्रवाह

`.github/workflows/docs.yml` ले साइटलाई pull request हरूमा बनाउँछ र `main` मा push हुँदा डिप्लोय गर्छ।

वर्कफ्लोले यी स्थापना गर्छ:

```bash
pip install -r requirements-docs.txt
```

डकुमेन्टेसन कार्यप्रवाहले केवल डकुमेन्टेसन टूलचेन स्थापना गर्छ। `mkdocs.yml` ले `mkdocstrings` लाई `src/` तिर पोइन्ट गर्छ जसले सार्वजनिक API पृष्ठहरूलाई स्रोत ट्रीबाट पूर्ण रनटाइम निर्भरता सेट स्थापना नगरिकन रेंडर गर्न दिन्छ। यदि भविष्यका API डकहरू निर्माणको क्रममा वैकल्पिक रनटाइम प्रदायकहरू इम्पोर्ट गर्न आवश्यक परे, दुबै `.github/workflows/docs.yml` र यो मार्गदर्शिका सँगै अद्यावधिक गर्नुहोस्।

## डक्स गुणस्तर मापदण्ड

डकुमेन्टेसन परिवर्तनहरू मर्ज गर्नु अघि, चलाउनुहोस्:

```bash
python -m mkdocs build --strict
git diff --check
```

कडा बिल्डहरू प्रयोग गर्नुहोस् ताकि भाँचिएका लिंकहरू, अमान्य नेभिगेसन प्रविष्टिहरू, र API रेंडरिङ सम्बन्धी समस्याहरू छिट्टै असफल हुन सकोस्।