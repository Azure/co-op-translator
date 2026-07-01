# MCP Server

Co-op Translator agents, editors, এবং MCP-সমর্থিত ক্লায়েন্টদের জন্য একটি Model Context Protocol সার্ভার অন্তর্ভুক্ত করে।

ডিফল্ট লোকাল সেটআপে, ব্যবহারকারীরা আলাদাভাবে সার্ভার হাতে চালিয়ে রাখে না। তারা তাদের MCP ক্লায়েন্ট কনফিগার করে, এবং ক্লায়েন্ট যখন Co-op Translator টুলস প্রয়োজন তখন `co-op-translator-mcp` স্বয়ংক্রিয়ভাবে `stdio` এর উপর শুরু করে।

আপনি যদি CLI, Python API, এবং MCP-এর মধ্যে সিদ্ধান্ত করতে চান, তাহলে শুরু করুন [Choose Your Workflow](workflows.md) থেকে।

যখন একটি এজেন্ট বা এডিটর Co-op Translator-কে সরাসরি কল করা উচিত তখন MCP ব্যবহার করুন:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP সার্ভার একই public Python API মোড়ানো করে যা [Python API](api.md)-এ ডকুমেন্টেড আছে। Provider-backed টুলস CLI এবং Python API-র মতো একই কনফিগার করা providers ব্যবহার করে। Agent-assisted টুলস MCP host agent-এর জন্য chunks প্রস্তুত করে অনুবাদ করার জন্য, তারপর Co-op Translator ব্যবহার করে চূড়ান্ত Markdown বা notebook পুনর্গঠন করে।

## Step 1: Install and Configure Co-op Translator

আপনার MCP ক্লায়েন্ট যে Python পরিবেশ ব্যবহার করবে সেখানে Co-op Translator ইনস্টল করুন:

```bash
pip install co-op-translator
```

এই রেপোজিটরি থেকে লোকাল ডেভেলপমেন্টের জন্য, প্যাকেজটি editable মোডে ইনস্টল করুন:

```bash
pip install -e .
```

আপনার MCP ক্লায়েন্ট যে অনুবাদ মোড ব্যবহার করবে তা নির্বাচন করুন:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator কল করে `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, অথবা `run_translation`. | Markdown এবং notebook অনুবাদের জন্য Azure OpenAI বা OpenAI দরকার। Image অনুবাদের জন্য অতিরিক্তভাবে Azure AI Vision দরকার। |
| Agent-assisted | MCP host agent অনুবাদ করে `start_markdown_agent_translation` বা `start_notebook_agent_translation` থেকে ফেরত আসা chunks। | Markdown বা notebook chunks-এর জন্য Co-op Translator LLM provider ক্রেডেনশিয়াল দরকার নেই। Image অনুবাদ এখনও agent-assisted মোডে কভার করা হয়নি। |

আপনি যদি Codex বা Claude Code-এর মতো এজেন্টের ভেতরে Markdown বা notebook অনুবাদ দিয়ে শুরু করছেন, তাহলে agent-assisted মোড দিয়ে শুরু করুন। যখন আপনি চান Co-op Translator নিজের configured providers-কে কল করুক, যখন আপনি ইমেজ অনুবাদ করছেন, বা যখন আপনি CLI-র মতো রেপোজিটরি-স্তরের অনুবাদ চালাচ্ছেন তখন provider-backed মোড ব্যবহার করুন।

Provider-backed workflow-গুলোর জন্য কেবলমাত্র provider credentials কনফিগার করুন:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provider-backed image অনুবাদ অতিরিক্তভাবে প্রয়োজন:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted মোড এই মুহুর্তে Markdown এবং notebook Markdown সেলগুলো কভার করে। ইমেজ অনুবাদ এখনও provider-backed image পাইপলাইন ব্যবহার করে এবং OCR ও layout-aware রেন্ডারিংয়ের জন্য Azure AI Vision প্রয়োজন।

## Step 2: Configure Your MCP Client

সাধারণ লোকাল `stdio` সেটআপের জন্য, আপনার MCP ক্লায়েন্ট কনফিগারেশনে Co-op Translator যোগ করুন। ক্লায়েন্ট প্রসেসটি স্বয়ংক্রিয়ভাবে শুরু এবং বন্ধ করবে।

Installed package configuration:

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

Source checkout configuration on Windows:

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

Source checkout configuration on macOS or Linux:

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

MCP ক্লায়েন্ট কনফিগারেশন বদলানোর পরে, ক্লায়েন্টটিকে পুনরায় চালু বা রিলোড করুন যাতে এটি নতুন সার্ভার আবিষ্কার করতে পারে।

## Step 3: Verify the Server in the Client

MCP ক্লায়েন্টকে উপলব্ধ টুলস তালিকা করতে বলুন, অথবা প্রথমে একটি read-only হেল্পার কল করুন:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

উপকারী প্রথম চেকসমূহ:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | নিশ্চিত করে যে সার্ভারে পৌঁছানো যায় এবং উপলব্ধ workflow দেখায়। |
| `list_supported_languages` | নিশ্চিত করে যে প্যাকেজ করা ভাষা ডেটা লোড করা যেতে পারে। |
| `get_configuration_status` | নিশ্চিত করে LLM এবং Vision provider-গুলোর প্রাপ্যতা গোপন ক্রেডেনশিয়ালগুলি প্রকাশ না করেই। |

## Step 4: Choose a Workflow

### Translate Individual Files or Documents

যখন MCP ক্লায়েন্টের কাছে ইতিমধ্যেই ডকুমেন্ট কনটেন্ট বা একটি ইমেজ পাথ থাকে এবং Co-op Translator-কে configured translation providers কল করা উচিত তখন provider-backed content টুলস ব্যবহার করুন।

Markdown-এর জন্য:

1. `translate_markdown_content` কল করুন `document`, `language_code`, এবং ঐচ্ছিকভাবে `source_path` সহ।
2. যদি অনুবাদিত ফলাফল Co-op Translator আউটপুট লেআউট-এ লেখা হবে, তাহলে `rewrite_markdown_paths` কল করুন।
3. ক্লায়েন্টকে চূড়ান্ত `content` লিখতে বা রিটার্ন করতে দিন।

Notebooks-এর জন্য:

1. `translate_notebook_content` কল করুন notebook JSON এবং `language_code` সহ।
2. যদি অনুবাদিত notebook লিংকগুলি টার্গেট পাথের জন্য সামঞ্জস্য করতে হয় তাহলে `rewrite_notebook_paths` কল করুন।
3. চূড়ান্ত notebook JSON লিখুন বা রিটার্ন করুন।

ইমেজগুলির জন্য:

1. `translate_image_content` কল করুন `image_path`, `language_code`, এবং ঐচ্ছিক `root_dir` বা `fast_mode` সহ।
2. ফেরত আসা `data_base64` এবং `mime_type` পড়ুন।
3. যদি `output_path` প্রদান করা থাকে, অনুবাদিত ইমেজটি ঐ পাথেও সংরক্ষিত হবে।

Content টুলস প্রজেক্ট ডিসকভারি, মেটাডেটা আপডেট, ডিসক্লেইমার, বা স্বয়ংক্রিয় পাথ রিরাইটিং করে না। যদি আপনি চান host agent Markdown বা notebook chunks অনুবাদ করুক Co-op Translator LLM provider ক্রেডেনশিয়াল ছাড়া, তাহলে নিচের agent-assisted workflow ব্যবহার করুন।

### Translate with the Host Agent Model

যখন আপনি চান MCP host agent (যেমন একটি কোডিং সহকারী) অনুবাদিত টেক্সট উৎপাদন করুক Co-op Translator-এর জন্য Azure OpenAI বা OpenAI কনফিগার না করে, তখন agent-assisted টুলস ব্যবহার করুন।

একটি চ্যাট-ভিত্তিক MCP ক্লায়েন্টে, সাধারণত আপনাকে নিজে টুল JSON লেখার প্রয়োজন হয় না। এজেন্টকে agent-assisted workflow ব্যবহার করতে বলুন:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Notebooks-এর জন্য, একই প্যাটার্ন ব্যবহার করুন:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

আপনার MCP ক্লায়েন্ট যদি সার্ভার প্রম্পট সমর্থন করে, তাহলে `agent_assisted_markdown_translation_prompt` ব্যবহার করুন যাতে ক্লায়েন্ট একই workflow নির্দেশাবলী লোড করে।

Markdown-এর জন্য:

1. `start_markdown_agent_translation` কল করুন `document`, `language_code`, এবং ঐচ্ছিকভাবে `source_path` সহ।
2. host agent-এ প্রত্যেক ফেরত আসা chunk-এর `prompt` অনুসরণ করে অনুবাদ করুন।
3. মূল `job` এবং অনুবাদ করা chunks `chunk_id` এবং `translated_text` ব্যবহার করে `finish_markdown_agent_translation` কল করুন।
4. যদি কনটেন্টটি অনুবাদিত টার্গেট পাথে লেখা হবে, তাহলে `rewrite_markdown_paths` কল করুন।

Notebooks-এর জন্য:

1. `start_notebook_agent_translation` কল করুন notebook JSON এবং `language_code` সহ।
2. host agent-এ প্রত্যেক ফেরত আসা chunk অনুবাদ করুন।
3. মূল `job` এবং অনুবাদ করা chunks দিয়ে `finish_notebook_agent_translation` কল করুন।
4. যদি অনুবাদিত notebook লিংকগুলো টার্গেট-পাথ সামঞ্জস্য প্রয়োজন হয় তাহলে `rewrite_notebook_paths` কল করুন।

Agent-assisted টুলস Co-op Translator থেকে Azure OpenAI বা OpenAI কল করে না। host agent ফেরত আসা chunks অনুবাদ করার জন্য দায়ী। Co-op Translator Markdown chunking, placeholder সংরক্ষণ, frontmatter পুনর্নির্মাণ, notebook সেল রিপ্লেসমেন্ট, এবং পোস্ট-অনুবাদ নরমালাইজেশন পরিচালনা করে।

### Translate an Entire Repository

যখন ব্যবহারকারী চান Co-op Translator CLI-র মতো আচরণ করুক তখন `run_translation` ব্যবহার করুন।

রেপোজিটরি অনুবাদ ডিফল্টভাবে `dry_run=true` থাকে যাতে একটি এজেন্ট scope পরীক্ষা করতে পারে ফাইল পরিবর্তনের আগে:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

লেখার অনুমতি দিতে, কলারকে উভয় `dry_run=false` এবং `confirm_write=true` সেট করতে হবে:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` `run_translation`-এর জন্য একটি compatibility alias হিসেবে প্রকাশ করা হয়েছে।

### Review Translated Output

Deterministic চেকগুলির জন্য যা LLM বা Vision ক্রেডেনশিয়াল প্রয়োজন করে না `run_review` ব্যবহার করুন:

!!! note "Beta"
    MCP beta `run_review` API প্রকাশ করে। এটি read-only review workflow-এর জন্য নিরাপদ, কিন্তু review চেক এবং ইস্যু স্কিমাগুলি পরিবর্তিত হতে পারে।

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

ফলাফলে ক্যাপচার করা টেক্সট আউটপুট এবং একটি স্ট্রাকচারড রিভিউ সারাংশ যখন উপলব্ধ থাকে তা অন্তর্ভুক্ত থাকে।

## Manual Server Runs

ম্যানুয়াল রানগুলি প্রধানত ডিবাগিং বা এমন ট্রান্সপোর্টের জন্য যেখানে লম্বা-চলমান সার্ভার হিসেবে আচরণ করে।

ডিফল্ট stdio সার্ভার ডিবাগ করুন:

```bash
co-op-translator-mcp
```

Source checkout থেকে চালান:

```bash
python -m co_op_translator.mcp.server
```

দীর্ঘজীবী HTTP বা SSE সার্ভার চালান:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

লোকাল এডিটর এবং এজেন্ট ইন্টিগ্রেশনের জন্য, ধাপ 2-এ ক্লায়েন্ট-ম্যানেজ্ড `stdio` কনফিগারেশন পছন্দ করুন।

## Tools

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | একটি Markdown স্ট্রিং অনুবাদ করুন। | No |
| `translate_notebook_content` | notebook JSON-এর Markdown সেলগুলো অনুবাদ করুন। | No |
| `translate_image_content` | একটি ইমেজে টেক্সট অনুবাদ করুন এবং base64 ইমেজ ডেটা রিটার্ন করুন। | Optional, only when `output_path` is provided |
| `start_markdown_agent_translation` | Host agent-কে Co-op Translator LLM ক্রেডেনশিয়াল ছাড়া অনুবাদ করার জন্য Markdown chunks প্রস্তুত করুন। | No |
| `finish_markdown_agent_translation` | host-agent অনুবাদকৃত chunks থেকে Markdown পুনর্গঠন করুন। | No |
| `start_notebook_agent_translation` | host agent-কে অনুবাদ করার জন্য notebook Markdown-cell chunks প্রস্তুত করুন। | No |
| `finish_notebook_agent_translation` | host-agent অনুবাদকৃত chunks থেকে notebook JSON পুনর্গঠন করুন। | No |
| `rewrite_markdown_paths` | অনুবাদিত টার্গেটের জন্য Markdown বডি এবং frontmatter paths পুনরায় লিখুন। | No |
| `rewrite_notebook_paths` | notebook Markdown সেলগুলোর ভিতরে পাথগুলো পুনরায় লিখুন। | No |
| `run_translation` | CLI-র মতো প্রজেক্ট-লেভেল অনুবাদ চালান। | Yes when `dry_run=false` and `confirm_write=true` |
| `translate_project` | `run_translation`-এর জন্য compatibility alias। | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | deterministic review চেক চালান। | No |
| `get_configuration_status` | কনফিগার করা LLM এবং Vision providers রিপোর্ট করুন গোপন মান ছাড়া। | No |
| `list_supported_languages` | সমর্থিত লক্ষ্য ভাষার কোড তালিকা করুন। | No |
| `get_api_overview` | উপলব্ধ MCP workflows এবং টুলস বর্ণনা করুন। | No |

## Resources

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON ওভারভিউ workflows এবং টুলসের। |
| `co-op://supported-languages` | সমর্থিত ভাষা কোডগুলোর JSON তালিকা। |
| `co-op://configuration` | গোপন ছাড়া provider প্রাপ্যতার সারাংশ JSON। |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | কনটেন্ট অনুবাদ এবং ঐচ্ছিক পাথ রিরাইটিং সহ MCP ক্লায়েন্টকে নির্দেশনা দিন। |
| `agent_assisted_markdown_translation_prompt` | Co-op Translator LLM provider ক্রেডেনশিয়াল ছাড়া host-agent Markdown অনুবাদের জন্য MCP ক্লায়েন্টকে নির্দেশনা দিন। |
| `translate_repository_prompt` | dry-run-first রেপোজিটরি অনুবাদের জন্য MCP ক্লায়েন্টকে নির্দেশনা দিন। |

## Copy-Paste Examples

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
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

Translate Markdown with the host agent model:

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

Host agent যখন প্রতিটি ফেরত আসা chunk অনুবাদ করবে, তখন সমাপ্ত কাজটি `start_markdown_agent_translation` দ্বারা ফেরত দেওয়া সম্পূর্ণ `job` অবজেক্ট ব্যবহার করে শেষ করুন:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

রেপোজিটরি অনুবাদ প্রিভিউ করুন:

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

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Absolute Python executable পাথ এবং `["-m", "co_op_translator.mcp.server"]` source checkout কনফিগারেশন ব্যবহার করুন। |
| The server is listed but translation fails. | `get_configuration_status` কল করুন এবং একটি LLM provider উপলব্ধ আছে কি না নিশ্চিত করুন। |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | `start_markdown_agent_translation` / `finish_markdown_agent_translation` অথবা notebook সমতুল্যগুলো ব্যবহার করুন যাতে host agent chunks অনুবাদ করে। |
| Image translation fails. | নিশ্চিত করুন Azure AI Vision ভ্যারিয়েবলগুলো সেট আছে এবং `get_configuration_status` কল করুন। |
| Repository translation does not write files. | কেবলমাত্র স্পষ্ট ব্যবহারকারী অনুমোদনের পরে `dry_run=false` এবং `confirm_write=true` সেট করুন। |
| Changes to client config do not appear. | MCP ক্লায়েন্ট পুনরায় চালু বা রিলোড করুন। |

## Safety Notes

- MCP টুল কলগুলো host application দ্বারা মডেল-নিয়ন্ত্রিত, তাই রেপোজিটরি অনুবাদ ডিফল্টভাবে dry-run হয়।
- পূর্ণ রেপোজিটরি অনুবাদ অনেক ফাইল তৈরি, আপডেট, বা মোছা করতে পারে। `confirm_write=true` সেট করার আগে স্পষ্ট ব্যবহারকারী অনুমোদন আবশ্যক।
- configuration status টুল কখনো API কী, endpoints, বা অন্যান্য গোপন মান ফেরত দেয় না।
- ইমেজ অনুবাদ base64 ইমেজ ডেটা রিটার্ন করে। বড় ইমেজগুলো বড় টুল রেসপন্স produce করতে পারে।
- Agent-assisted টুলস সোর্স chunks এবং prompts MCP host-এ রিটার্ন করে। এগুলো শুধুমাত্র সেই কনটেন্টের সাথে ব্যবহার করুন যেটি ব্যবহারকারী সেই host agent মডেলে পাঠাতে স্বাচ্ছন্দ্যবোধ করে।