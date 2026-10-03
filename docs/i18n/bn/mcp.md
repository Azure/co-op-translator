# MCP সার্ভার

Co-op Translator এজেন্ট, সম্পাদক, এবং MCP-সমর্থ ক্লায়েন্টদের জন্য একটি Model Context Protocol সার্ভার অন্তর্ভুক্ত করে।

ডিফল্ট লোকাল সেটআপের জন্য, ব্যবহারকারীরা আলাদা কোনো সার্ভার আলাদাভাবে চালিয়ে রাখেন না। তারা তাদের MCP ক্লায়েন্ট কনফিগার করে, এবং ক্লায়েন্ট যখন Co-op Translator টুলস প্রয়োজন তখন এটি `stdio`-এর মাধ্যমে স্বয়ংক্রিয়ভাবে `co-op-translator-mcp` শুরু করে।

যদি আপনি CLI, Python API, এবং MCP-এর মধ্যে সিদ্ধান্ত নিচ্ছেন, তাহলে [আপনার কর্মপ্রবাহ নির্বাচন করুন](workflows.md) দিয়ে শুরু করুন।

যখন কোনো এজেন্ট বা সম্পাদক সরাসরি Co-op Translator কল করতে হবে তখন MCP ব্যবহার করুন:

| ব্যবহারকারীর লক্ষ্য | MCP টুলস |
| --- | --- |
| একটি Markdown ডকুমেন্ট, নোটবুক, বা ইমেজ অনুবাদ করুন | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| হোস্ট এজেন্ট মডেলের সাথে Markdown বা নোটবুক সামগ্রী অনুবাদ করুন | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| আউটপুট পথে সিদ্ধান্ত নেওয়ার পর অনুবাদিত Markdown বা নোটবুক লিঙ্কগুলো পুনরায় লিখুন | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI-এর মতো একটি সম্পূর্ণ রিপোজিটরি অনুবাদ করুন | `run_translation`, `translate_project` |
| LLM ক্রেডেনশিয়াল ছাড়া অনুবাদিত আউটপুট পর্যালোচনা করুন | `run_review` |
| ক্ষমতা এবং পরিবেশের অবস্থা পরিদর্শন করুন | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP সার্ভারটি [Python API](api.md)-এ ডকুমেন্ট করা একই পাবলিক Python API-কে মোড়ে ঢেকে দেয়। Provider-backed টুলগুলি CLI এবং Python API-র সাথে কনফিগার করা একই প্রোভাইডার ব্যবহার করে। Agent-assisted টুলগুলি MCP হোস্ট এজেন্টের অনুবাদের জন্য চাঙ্ক প্রস্তুত করে, তারপর চূড়ান্ত Markdown বা নোটবুক পুনর্গঠনের জন্য Co-op Translator ব্যবহার করে।

## ধাপ 1: Co-op Translator ইনস্টল এবং কনফিগার করুন

আপনার MCP ক্লায়েন্ট যে Python পরিবেশ ব্যবহার করবে সেখানে Co-op Translator ইনস্টল করুন:

```bash
pip install co-op-translator
```

এই রিপোজিটরি থেকে লোকাল ডেভেলপমেন্টের জন্য, প্যাকেজটি সম্পাদনাযোগ্য মোডে ইনস্টল করুন:

```bash
pip install -e .
```

আপনার MCP ক্লায়েন্ট যে অনুবাদ মোড ব্যবহার করবে তা নির্বাচন করুন:

| মোড | এটি ব্যবহারের জন্য | ক্রেডেনশিয়াল |
| --- | --- | --- |
| Provider-backed | Co-op Translator `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, or `run_translation` কল করে। | অনুবাদের জন্য Azure OpenAI, OpenAI, বা Anthropic প্রয়োজন। ইমেজ অনুবাদের জন্যও Azure AI Vision প্রয়োজন। |
| Agent-assisted | MCP হোস্ট এজেন্ট `start_markdown_agent_translation` বা `start_notebook_agent_translation` দ্বারা ফিরিয়ে দেয়া চাঙ্কগুলো অনুবাদ করে। | Markdown বা নোটবুক চাঙ্কগুলোর জন্য Co-op Translator LLM প্রোভাইডার ক্রেডেনশিয়ালের প্রয়োজন নেই। ইমেজ অনুবাদটি এখনও agent-assisted মোডে অন্তর্ভুক্ত নয়। |

যদি আপনি Codex বা Claude Code-এর মতো কোনো এজেন্টের ভিতরে Markdown বা নোটবুক অনুবাদ দিয়ে শুরু করছেন, তাহলে agent-assisted মোড দিয়ে শুরু করুন। যখন আপনি চান Co-op Translator নিজেই আপনার কনফিগার করা প্রোভাইডারগুলো কল করুক, যখন আপনি ইমেজ অনুবাদ করছেন, বা যখন আপনি CLI অনুরূপ রিপোজিটরি-স্তরের অনুবাদ চালাচ্ছেন তখন provider-backed মোড ব্যবহার করুন।

Provider-backed ওয়ার্কফ্লো-এর জন্য একটি প্রোভাইডার কনফিগার করুন:

```bash
# অ্যাজিউর ওপেনএআই
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# অথবা ওপেনএআই
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# অথবা অ্যানথ্রোপিক
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Provider-backed ইমেজ অনুবাদের জন্য অতিরিক্তভাবে দরকার:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted মোড বর্তমানে Markdown এবং নোটবুকের Markdown সেলগুলোকেই কাভার করে। ইমেজ অনুবাদ এখনও provider-backed ইমেজ পাইপলাইন ব্যবহার করে এবং OCR ও লেআউট-সচেতন রেন্ডারিং-এর জন্য Azure AI Vision প্রয়োজন।

## ধাপ 2: আপনার MCP ক্লায়েন্ট কনফিগার করুন

সাধারণ লোকাল `stdio` সেটআপের জন্য, আপনার MCP ক্লায়েন্ট কনফিগারেশনে Co-op Translator যোগ করুন। ক্লায়েন্ট স্বয়ংক্রিয়ভাবে প্রসেসটি শুরু ও বন্ধ করবে।

ইনস্টল করা প্যাকেজ কনফিগারেশন:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

Windows-এ সোর্স চেকআউট কনফিগারেশন:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

macOS বা Linux-এ সোর্স চেকআউট কনফিগারেশন:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

MCP ক্লায়েন্ট কনফিগারেশন পরিবর্তন করার পর, ক্লায়েন্টটিকে নতুন সার্ভার খুঁজে পেতে রিস্টার্ট বা রিলোড করুন।

## ধাপ 3: ক্লায়েন্টে সার্ভার যাচাই করুন

উপলব্ধ টুলগুলো তালিকাভুক্ত করতে MCP ক্লায়েন্টকে বলুন, অথবা প্রথমে read-only হেল্পারদের মধ্যে একটি কল করুন:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

প্রাথমিক উপকারী চেকসমূহ:

| টুল | কী যাচাই করবেন |
| --- | --- |
| `get_api_overview` | সার্ভারটি পৌঁছনযোগ্য কিনা নিশ্চিত করে এবং উপলব্ধ ওয়ার্কফ্লো দেখায়। |
| `list_supported_languages` | প্যাকেজ করা ভাষা ডেটা লোড করা যায় কিনা নিশ্চিত করে। |
| `get_configuration_status` | সিক্রেট মান না ফাঁস করে LLM এবং Vision প্রোভাইডারের উপলব্ধতা নিশ্চিত করে। |

## ধাপ 4: একটি ওয়ার্কফ্লো নির্বাচন করুন

### ব্যক্তিগত ফাইল বা ডকুমেন্ট অনুবাদ করুন

যখন MCP ক্লায়েন্টের ইতোমধ্যে ডকুমেন্ট কন্টেন্ট বা একটি ইমেজ পাথ থাকে এবং Co-op Translator কনফিগার করা ট্রান্সলেশন প্রোভাইডারগুলো কল করবে তখন provider-backed কন্টেন্ট টুলগুলো ব্যবহার করুন।

Markdown-এর জন্য:

1. `document`, `language_code`, এবং ঐচ্ছিকভাবে `source_path` দিয়ে `translate_markdown_content` কল করুন।
2. যদি অনুবাদিত ফলাফল Co-op Translator আউটপুট লেআউটে লেখা হবে, তাহলে `rewrite_markdown_paths` কল করুন।
3. ক্লায়েন্টকে চূড়ান্ত `content` লেখা বা ফেরত দিতে দিন।

নোটবুকগুলোর জন্য:

1. নোটবুক JSON এবং `language_code` দিয়ে `translate_notebook_content` কল করুন।
2. যদি অনুবাদিত নোটবুক লিঙ্কগুলো লক্ষ্য পাথ অনুযায়ী সমন্বয় করতে হয় তবে `rewrite_notebook_paths` কল করুন।
3. চূড়ান্ত নোটবুক JSON লিখুন বা ফেরত দিন।

ইমেজগুলোর জন্য:

1. `image_path`, `language_code`, এবং ঐচ্ছিকভাবে `root_dir` বা `fast_mode` দিয়ে `translate_image_content` কল করুন।
2. ফিরিয়ে দেয়া `data_base64` এবং `mime_type` পড়ুন।
3. যদি `output_path` প্রদান করা হয়, অনুবাদিত ইমেজটি সেই পাথে সংরক্ষিত হয়।

কনটেন্ট টুলগুলো প্রকল্প আবিষ্কার, মেটাডেটা আপডেট, ডিসক্লেইমার, বা স্বয়ংক্রিয় পাথ পুনরায়লেখন করে না। যদি আপনি চান হোস্ট এজেন্ট Co-op Translator LLM প্রোভাইডার ক্রেডেনশিয়াল ছাড়াই Markdown বা নোটবুক চাঙ্ক অনুবাদ করুক, তবে নিচের agent-assisted ওয়ার্কফ্লো ব্যবহার করুন।

### হোস্ট এজেন্ট মডেল দিয়ে অনুবাদ করুন

যখন আপনি Co-op Translator-এর জন্য LLM প্রোভাইডার কনফিগার করার পরিবর্তে MCP হোস্ট এজেন্ট (যেমন একটি কোডিং সহকারী) অনুবাদিত টেক্সট উৎপাদন করুক তখন agent-assisted টুলগুলো ব্যবহার করুন।

একটি চ্যাট-ভিত্তিক MCP ক্লায়েন্টে, সাধারণত আপনাকে নিজে টুল JSON লিখতে হয় না। এজেন্টকে agent-assisted ওয়ার্কফ্লো ব্যবহার করতে বলুন:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

নোটবুকগুলোর জন্য একই প্যাটার্ন ব্যবহার করুন:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

যদি আপনার MCP ক্লায়েন্ট সার্ভার প্রোম্পট সমর্থন করে, তাহলে একই ওয়ার্কফ্লো নির্দেশনাগুলো ক্লায়েন্ট লোড করার জন্য `agent_assisted_markdown_translation_prompt` ব্যবহার করুন।

Markdown-এর জন্য:

1. `document`, `language_code`, এবং ঐচ্ছিকভাবে `source_path` দিয়ে `start_markdown_agent_translation` কল করুন।
2. চাঙ্কের `prompt` অনুসরণ করে হোস্ট এজেন্টে প্রত্যেকটি ফেরত দেওয়া চাঙ্ক অনুবাদ করুন।
3. মুল `job` এবং অনুবাদ করা চাঙ্কগুলো `chunk_id` এবং `translated_text` ব্যবহার করে `finish_markdown_agent_translation` কল করুন।
4. যদি কনটেন্ট অনুবাদিত টার্গেট পথে লেখা হবে, তাহলে `rewrite_markdown_paths` কল করুন।

নোটবুকগুলোর জন্য:

1. নোটবুক JSON এবং `language_code` দিয়ে `start_notebook_agent_translation` কল করুন।
2. হোস্ট এজেন্টে প্রত্যেকটি ফেরত দেওয়া চাঙ্ক অনুবাদ করুন।
 3. মূল `job` এবং অনুবাদকৃত খণ্ডগুলির সাথে `finish_notebook_agent_translation` কল করুন.
 4. যদি অনুবাদ করা নোটবুক লিঙ্কগুলির লক্ষ্য-পাথ সমন্বয় প্রয়োজন হয় তবে `rewrite_notebook_paths` কল করুন.

 Agent-সহায়িত টুলগুলো Co-op Translator থেকে কনফিগার করা LLM প্রোভাইডারকে কল করে না। হোস্ট এজেন্ট ফেরত দেওয়া খণ্ডগুলো অনুবাদ করার জন্য দায়িত্বশীল। Co-op Translator Markdown খণ্ডকরণ, প্লেসহোল্ডার সংরক্ষণ, frontmatter পুনর্নির্মাণ, নোটবুক সেল প্রতিস্থাপন, এবং অনুবাদের পর স্বরূপকরণ পরিচালনা করে।

 ### একটি সম্পূর্ণ রিপোজিটরি অনুবাদ করুন

 যখন ব্যবহারকারী চায় Co-op Translator `translate` CLI-এর মতো আচরণ করুক তখন `run_translation` ব্যবহার করুন।

 রিপোজিটরি অনুবাদ ডিফল্টভাবে `dry_run=true` থাকে যাতে কোনো এজেন্ট ফাইল পরিবর্তনের আগে পরিধি পরীক্ষা করতে পারে:

 ```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

 `run_translation` ফলাফলটিতে ভার্সনকৃত একটি `events` অ্যারে রয়েছে
 `co-op.translation.event.v1` প্রগ্রেস ইভেন্টসমূহ। MCP ক্লায়েন্টরা নিম্নলিখিত ফিল্ডগুলো ব্যবহার করা উচিত
 `type`, `stage_key`, `completed`, `total`, এবং `current_path` — ক্যাপচার করা কনসোল টেক্সট পার্স করার পরিবর্তে
 ঐ ইভেন্টগুলোও লেখার জন্য `json_events_path` পাস করুন
 একটি NDJSON ফাইলে।

 লেখার অনুমতি দিতে, কলকারীকে উভয় `dry_run=false` এবং `confirm_write=true` সেট করতে হবে:

 ```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

 `translate_project` একটি সামঞ্জস্যপূর্ণ উপনাম হিসেবে `run_translation` এর জন্য উন্মুক্ত করা হয়েছে।

 ### অনুবাদিত আউটপুট পর্যালোচনা

 নির্ধারিত (deterministic) চেকগুলোর জন্য যা LLM বা Vision ক্রেডেনশিয়াল প্রয়োজন করে না, `run_review` ব্যবহার করুন:

 !!! note "Beta"
     MCP বেটা `run_review` API উন্মোচন করে। এটি শুধুমাত্র-পড়ার পর্যালোচনা ওয়ার্কফ্লোগুলোর জন্য নিরাপদ, তবে পর্যালোচনা চেক এবং ইস্যু স্কিমাগুলো পরিবর্তনশীল হতে পারে।

 ```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

 ফলাফলে ক্যাপচার করা টেক্সট আউটপুট এবং উপলব্ধ থাকলে একটি কাঠামোবদ্ধ রিভিউ সারাংশ অন্তর্ভুক্ত থাকে।

## ম্যানুয়াল সার্ভার রান

 ম্যানুয়াল রনগুলো প্রধানত ডিবাগিং বা দীর্ঘমেয়াদি সার্ভারের মতো আচরণকারী ট্রান্সপোর্টগুলোর জন্য।

 ডিফল্ট stdio সার্ভার ডিবাগ করুন:

 ```bash
co-op-translator-mcp
```

 সোর্স চেকআউট থেকে চালান:

 ```bash
python -m co_op_translator.mcp.server
```

 দীর্ঘস্থায়ী HTTP বা SSE সার্ভার চালান:

 ```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

 লোকাল এডিটর এবং এজেন্ট ইন্টিগ্রেশনের জন্য, স্টেপ 2-এ ক্লায়েন্ট-ম্যানেজ করা `stdio` কনফিগারেশনকে অগ্রাধিকার দিন।

 ## Tools

 | টুল | উদ্দেশ্য | ফাইল লেখে |
| --- | --- | --- |
 | `translate_markdown_content` | একটি Markdown স্ট্রিং অনুবাদ করুন। | না |
 | `translate_notebook_content` | নোটবুক JSON-এ Markdown সেলগুলিকে অনুবাদ করুন। | না |
 | `translate_image_content` | একটি ইমেজের টেক্সট অনুবাদ করুন এবং base64 ইমেজ ডেটা ফেরত দিন। | ঐচ্ছিক, শুধুমাত্র যখন `output_path` প্রদান করা হয় |
 | `start_markdown_agent_translation` | হোস্ট এজেন্টকে Co-op Translator LLM ক্রেডেনশিয়াল ছাড়াই অনুবাদ করার জন্য Markdown খণ্ড প্রস্তুত করে। | না |
 | `finish_markdown_agent_translation` | হোস্ট-এজেন্ট অনুবাদিত খণ্ডগুলি থেকে Markdown পুনর্নির্মাণ করুন। | না |
 | `start_notebook_agent_translation` | হোস্ট এজেন্টের জন্য নোটবুকের Markdown-সেল খণ্ডগুলি অনুবাদ করার জন্য প্রস্তুত করুন। | না |
 | `finish_notebook_agent_translation` | হোস্ট-এজেন্ট অনুবাদিত খণ্ডগুলো থেকে নোটবুক JSON পুনর্নির্মাণ করুন। | না |
 | `rewrite_markdown_paths` | অনুবাদকৃত টার্গেটের জন্য Markdown বডি এবং frontmatter পাথগুলো পুনঃলিখন করুন। | না |
 | `rewrite_notebook_paths` | নোটবুক Markdown সেলগুলোর ভিতরের পাথগুলো পুনঃলিখন করুন। | না |
 | `run_translation` | CLI-এর মতো প্রজেক্ট-স্তরের অনুবাদ চালান। | হ্যাঁ যখন `dry_run=false` এবং `confirm_write=true` |
 | `translate_project` | `run_translation` এর সাথে সামঞ্জস্যপূর্ণ উপনাম। | হ্যাঁ যখন `dry_run=false` এবং `confirm_write=true` |
 | `run_review` | নির্ধারিত রিভিউ চেক চালান। | না |
 | `get_configuration_status` | সিক্রেট ফাঁস না করে কনফিগার করা LLM এবং Vision প্রোভাইডারের রিপোর্ট করুন। | না |
 | `list_supported_languages` | সমর্থিত লক্ষ্য ভাষার কোডগুলোর তালিকা দেখান। | না |
 | `get_api_overview` | উপলব্ধ MCP ওয়ার্কফ্লো এবং টুলস বর্ণনা করুন। | না |

 ## Resources

 | রিসোর্স URI | উদ্দেশ্য |
| --- | --- |
 | `co-op://api` | ওয়ার্কফ্লো এবং টুলগুলোর JSON ওভারভিউ। |
 | `co-op://supported-languages` | সমর্থিত ভাষা কোডগুলোর JSON তালিকা। |
 | `co-op://configuration` | সিক্রেট ছাড়া JSON প্রোভাইডার উপলভ্যতার সারসংক্ষেপ। |

 ## Prompts

 | প্রম্পট | উদ্দেশ্য |
| --- | --- |
 | `translate_markdown_document_prompt` | বিষয়বস্তু অনুবাদ ও ঐচ্ছিক পাথ পুনঃলিখনের মাধ্যমে MCP ক্লায়েন্টকে গাইড করে। |
 | `agent_assisted_markdown_translation_prompt` | Co-op Translator LLM প্রোভাইডার ক্রেডেনশিয়াল ছাড়াই হোস্ট-এজেন্ট Markdown অনুবাদের মাধ্যমে MCP ক্লায়েন্টকে গাইড করে। |
 | `translate_repository_prompt` | প্রথমে dry-run করে রিপোজিটরি অনুবাদের মাধ্যমে MCP ক্লায়েন্টকে গাইড করে। |

## কপি-পেস্ট উদাহরণ

 Translate Markdown content:

 ```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

 Rewrite translated Markdown links:

 ```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

 হোস্ট এজেন্ট মডেলের সাথে Markdown অনুবাদ করুন:

 ```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

 হোস্ট এজেন্ট প্রত্যেকটি ফেরত দেওয়া খণ্ড অনুবাদ করার পরে, `start_markdown_agent_translation` দ্বারা ফেরত দেয়া সম্পূর্ণ `job` অবজেক্ট দিয়ে কাজটি সম্পন্ন করুন:

 ```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

 Preview repository translation:

 ```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

 ## Troubleshooting

 | সমস্যা | কী চেষ্টা করবেন |
| --- | --- |
 | MCP ক্লায়েন্ট `co-op-translator-mcp` খুঁজে পাচ্ছে না। | সম্পূর্ণ Python executable পাথ ব্যবহার করুন এবং `["-m", "co_op_translator.mcp.server"]` সোর্স চেকআউট কনফিগারেশন দিন। |
 | সার্ভার তালিকাভুক্ত আছে কিন্তু অনুবাদ ব্যর্থ হচ্ছে। | `get_configuration_status` কল করুন এবং একটি LLM প্রোভাইডার উপলব্ধ আছে কিনা নিশ্চিত করুন। |
 | আপনি প্রোভাইডার ক্রেডেনশিয়াল ছাড়া Markdown বা নোটবুক অনুবাদ চান। | `start_markdown_agent_translation` / `finish_markdown_agent_translation` বা নোটবুক সমতুল্যগুলো ব্যবহার করুন যাতে হোস্ট এজেন্ট খণ্ডগুলো অনুবাদ করে। |
 | ইমেজ অনুবাদ ব্যর্থ হচ্ছে। | নিশ্চিত করুন Azure AI Vision ভ্যারিয়েবলগুলি সেট আছে এবং `get_configuration_status` কল করুন। |
 | রিপোজিটরি অনুবাদ ফাইল লেখছে না। | স্পষ্ট ব্যবহারকারীর অনুমোদনের পরে মাত্র `dry_run=false` এবং `confirm_write=true` সেট করুন। |
 | ক্লায়েন্ট কনফিগ পরিবর্তন দৃশ্যমান নয়। | MCP ক্লায়েন্ট রিস্টার্ট বা রিলোড করুন। |

## নিরাপত্তা নোট

 - MCP টুল কলগুলো হোস্ট অ্যাপ্লিকেশন দ্বারা মডেল-নিয়ন্ত্রিত, তাই রিপোজিটরি অনুবাদ ডিফল্টভাবে dry-run হয়।
 - পূর্ণ রিপোজিটরি অনুবাদ অনেক ফাইল তৈরি, আপডেট, বা মুছে ফেলতে পারে। `confirm_write=true` সেট করার আগে স্পষ্ট ব্যবহারকারী অনুমোদন প্রয়োজন।
 - কনফিগারেশন স্ট্যাটাস টুল কখনো API কী, এন্ডপয়েন্ট, বা অন্য সিক্রেট মান ফেরত দেয় না।
 - ইমেজ অনুবাদ base64 ইমেজ ডেটা ফেরত দেয়। বড় ইমেজগুলো বড় টুল প্রতিক্রিয়া তৈরি করতে পারে।
 - এজেন্ট-সহায়িত টুলগুলো সোর্স খণ্ড এবং প্রম্পট MCP হোস্টকে ফেরত দেয়। ব্যবহারকারী যদি সেই হোস্ট এজেন্ট মডেলে পাঠাতে আরামবোধ করেন তখনই এগুলো ব্যবহার করুন।