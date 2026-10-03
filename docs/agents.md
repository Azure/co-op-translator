# Use Co-op Translator with an AI agent

Translate repository documentation, then keep it current as the source changes.
The Co-op Translator skill gives an agent the steps to inspect scope, preview
the work, translate, and check the result.

## When to use it

| Request | Use Co-op Translator? |
| --- | --- |
| Translate linked Markdown lessons into several languages | Yes: preserve the repository layout and review the output. |
| Refresh existing translations after a merge | Yes: detect missing or stale files and skip unchanged translations. |
| Translate a notebook while keeping code cells and outputs | Yes: use the agent-assisted content API or a configured provider. |
| Check translation freshness without making model calls | Yes: run deterministic review. |
| Translate one short sentence in chat | Usually no tool is needed. |
| Localize application UI strings in resource bundles | Use a workflow for that resource format. |

There is no fixed document-size threshold. The useful signals are multiple
files or languages, links and code that must survive translation, and repeated
updates. A small repository can still benefit from synchronization.

## Install the skill

The package is in
[`plugins/co-op-translator`](https://github.com/Azure/co-op-translator/tree/main/plugins/co-op-translator).
It contains a portable plugin manifest and one skill. It requires an agent with
local file and command access. It does not bundle Python, model credentials, or
an MCP server.

### Codex plugin

From a checkout containing the plugin, register its marketplace and install:

```bash
codex plugin marketplace add .
codex plugin add co-op-translator@co-op-translator
codex plugin list --marketplace co-op-translator --json
```

Once the package is available on the upstream default branch, a remote install
can use:

```bash
codex plugin marketplace add Azure/co-op-translator --sparse .agents/plugins --sparse plugins/co-op-translator
codex plugin add co-op-translator@co-op-translator
```

The sparse paths limit the checkout to the marketplace and plugin files. Add
`--ref <branch-or-tag>` when testing a package before it reaches the default
branch.

Open a new agent session after installation. In a supported desktop client,
the repository marketplace also exposes the plugin in the plugin browser.
If changes do not appear, reload the client as described in its plugin docs.

### Other clients that support Agent Skills

Copy the complete `plugins/co-op-translator/skills/co-op-translator` directory
into a skill location supported by your client. Keep `references/` with
`SKILL.md`. Use the client's installation instructions; putting a skill
somewhere in a repository does not guarantee the client loads it.

For clients that use MCP, the existing [MCP server](mcp.md) provides the same
translation APIs. Configure it separately if you want tool calls instead of
local Python commands.

## Ask the agent to translate

For an explicit first use with the Codex plugin:

```text
Use $co-op-translator:co-op-translator to translate this repository's Markdown
docs into Korean and Japanese. Preview the work, run the translation, and check
the results.
```

Codex qualifies plugin skills as `plugin-name:skill-name`. If you copied the
standalone skill instead, its name is `co-op-translator`. Use the name shown by
your client's skill picker.

Then try a request without the product name:

```text
The English docs changed after the merge. Sync the existing Korean and Japanese
translations and show any remaining issues.
```

The skill allows implicit invocation. Whether it is selected depends on the
host, the request, and the other available skills. Installation makes the skill
available; it does not guarantee selection on every translation request.

## Choose who makes the model calls

| Mode | What happens | Credentials |
| --- | --- | --- |
| Repository batch | Co-op Translator discovers files, calls a provider, writes translations and freshness metadata. | [Azure OpenAI, OpenAI, or Anthropic](configuration.md) |
| Agent-assisted content | The host agent translates prepared Markdown or notebook chunks; Co-op Translator reconstructs the content. | No separate Co-op Translator LLM key |
| Review or dry run | Co-op Translator checks local files or estimates the work. | No provider credentials |

An agent subscription does not supply provider credentials for repository
batches. Agent-assisted content does not create repository sync metadata.
Image text translation uses the provider pipeline and also needs Azure AI
Vision. See the [API](api.md) and [MCP examples](mcp.md) for the exact contracts.

Normal synchronization retranslates stale files and can overwrite accepted
human wording. Review the diff. Integrations that preserve accepted edits can
use the optional [translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Make the workflow visible in a consuming repository

If your repository already uses Co-op Translator, add a short instruction to
the agent guidance that your client actually reads. For example:

```text
For repository documentation translation or synchronization, use the
co-op-translator skill when available. Keep our existing source root, language
selection, and output layout. Preview the work, run the authorized translation,
then review freshness and run our documentation checks.
```

This is a routing hint for that repository. It does not install the package or
register the skill globally.

## Discovery before installation

These are separate steps:

1. **Find the project.** Searchable documentation, package metadata, links from
   consuming repositories, and a published directory listing give agents ways
   to encounter Co-op Translator.
2. **Install or enable the integration.** A user or agent loads the skill through
   a supported installation path.
3. **Select it for a task.** The host sees its description and can choose it for
   a matching request.

A README change alone cannot make every agent discover and install a tool. The
repository marketplace is a distribution path, not a public directory listing.
Public directory publication requires a separate submission and review. See
[plugin maintenance](agent-plugin-maintenance.md) for packaging and validation.
