# Privacy and Data Flow

Co-op Translator translates user-selected repository content by calling configured AI providers or MCP host agents. This page explains what data can leave your local environment, which workflows avoid model calls, and what to consider before using the tool with private or sensitive material.

This page is not a replacement for the privacy, security, or data processing terms of Azure OpenAI, Azure AI Vision, OpenAI, GitHub, your MCP host, or any other service you configure.

## Quick guidance

- Run `--dry-run` first when translating a new repository or a large private project.
- Do not translate secrets, credentials, access tokens, private keys, or files that should not be sent to your configured AI provider or MCP host.
- Treat Markdown, notebook Markdown cells, and image text as data that may be sent outside the local machine during provider-backed translation.
- Review generated translations before publishing them, especially when source content is untrusted, user-generated, or security-sensitive.
- Share logs publicly only after checking that they do not contain private paths, translated text, project names, or other sensitive context.

## What stays local

Co-op Translator performs project discovery, file reads and writes, link rewriting, metadata updates, deterministic review checks, and most output organization locally.

These operations do not require model provider calls:

- `co-op-review`
- `run_review`
- `rewrite_markdown_paths`
- `rewrite_notebook_paths`
- Markdown and notebook path migration logic
- Translation freshness and structure checks

These operations may still read local files and write output files, so use `--dry-run` or API dry-run options when you want to inspect the plan before writing changes.

## Provider-backed translation

Provider-backed translation means Co-op Translator calls Azure OpenAI or OpenAI directly using the credentials you configured.

| Content type | Data sent to provider | Provider |
| --- | --- | --- |
| Markdown | Translation instructions plus source Markdown chunks | Azure OpenAI or OpenAI |
| Notebook | Translation instructions plus Markdown cell chunks; code cells are preserved by Co-op Translator | Azure OpenAI or OpenAI |
| Image | Source image data for OCR/text extraction, then extracted text for translation | Azure AI Vision plus Azure OpenAI or OpenAI |
| Evaluation | Source and translated Markdown content selected for LLM-based evaluation | Azure OpenAI or OpenAI |

The exact handling, retention, logging, and abuse-monitoring behavior for provider requests is governed by the provider and account configuration you use. Review your provider terms and enterprise settings before processing private repositories.

## MCP and agent-assisted translation

The MCP server exposes the same project and content workflows to MCP-compatible clients.

There are two important modes:

- Provider-backed MCP tools call the configured Azure OpenAI, OpenAI, and Azure AI Vision providers from Co-op Translator.
- Agent-assisted MCP tools prepare Markdown or notebook chunks and return them to the MCP host agent. The host agent, not Co-op Translator, performs the translation with its own model or provider.

Use agent-assisted mode only with content you are comfortable sending to the MCP host and any model provider behind that host. Co-op Translator reconstructs the translated Markdown or notebook after the host returns translated chunks, but it does not control the host model's data handling.

## Secrets and configuration

Keep provider credentials in environment variables, local `.env` files, or CI secrets. Do not commit real credentials.

Sensitive values include:

- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
- `OPENAI_API_KEY`
- `OPENAI_ORG_ID`
- `OPENAI_BASE_URL`
- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

The MCP configuration status tool reports provider availability without returning secret values. That does not make it safe to publish your `.env` file, CI logs, or provider-specific configuration screenshots.

## Logs and generated files

Debug logs can include file paths, provider health-check status, progress information, warnings, and in some workflows translated text or other project context. Before sharing logs in issues or pull requests, remove:

- API keys, tokens, and private endpoints
- Private repository paths or organization names
- Source or translated text that should not be public
- Customer, learner, or user data

Generated translations and translated images are normal project artifacts. Review them before committing, especially when translating private source material or images that contain names, email addresses, screenshots, diagrams, or proprietary content.

## Prompt injection and untrusted content

Repository content can contain instructions that are meaningful to a language model, even when the content is only meant to be translated. Co-op Translator prompts the model to preserve structure and translate content, but untrusted source text can still attempt to influence model behavior.

When translating untrusted or user-generated content:

- Use `--dry-run` and review planned files before writing changes.
- Keep provider credentials scoped to the minimum access needed.
- Do not combine translation with unrelated privileged actions in the same automation job.
- Review translated Markdown links, images, code fences, and notebook Markdown cells before publishing.
- Run `co-op-review` after translation to catch deterministic structure and freshness issues.

## CI and private repositories

GitHub Actions workflows can send repository content to configured providers when they run translation commands. Before enabling translation workflows in private repositories:

- Confirm which branches and events can trigger provider-backed translation.
- Store provider credentials as repository or organization secrets.
- Avoid running provider-backed translation on untrusted pull requests.
- Prefer deterministic `co-op-review` for pull request validation when model calls are not required.

See [GitHub Actions](github-actions.md) for workflow examples and [Configuration](configuration.md) for provider requirements.
