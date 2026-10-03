# Maintain the agent plugin

The plugin lives in `plugins/co-op-translator`. The repository marketplace is
`.agents/plugins/marketplace.json`. Plugin versions are separate from the
Python package version; the initial skill uses public APIs from 0.22.0.

## Package and inspect

After committing the plugin files, create a ZIP with `plugin.json` at its root:

```bash
git archive --format=zip --output=../co-op-translator-plugin-0.1.0.zip HEAD:plugins/co-op-translator
```

The archive contains the skill, its references, interface metadata, icon, and
license. It does not include the whole repository, credentials, or environments.
Extract it into an empty directory and check that all referenced paths resolve
inside the extracted package. Validate the root manifest against the
[Agent Plugins schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json).

## Verify installation and task selection separately

First confirm that the client lists the plugin from the repository marketplace.
Then install it in a test profile and open a new session. Do not change a user's
global plugin settings just to run a test.

Also test the pushed branch through the remote marketplace path in a separate
profile. Replace the repository and ref with the ones under review:

```bash
codex plugin marketplace add OWNER/REPO --ref BRANCH --sparse .agents/plugins --sparse plugins/co-op-translator
codex plugin add co-op-translator@co-op-translator
codex plugin list --marketplace co-op-translator --json
```

Compare the installed plugin files with the reviewed commit. A local install
does not test the Git source or sparse paths.

Use the requests below without naming the product or adding hidden hints. Record
the client and model version, enabled skills, request, selected skill, tool calls,
and outcome. Explicit `$co-op-translator` invocation only tests explicit use.
Reading a manifest or checking a description does not measure automatic selection.

Before a model-driven trial, use the client's command interface to read a small
fixture and check the Python environment under the same sandbox policy. This
preflight needs no model call. If local execution is blocked, fix the test
environment before spending more model usage on execution trials. Record skill
selection separately from reading its instructions and completing its workflow.
A selected skill with a blocked command is not a successful dry run.

Record the actual runtime skill catalog, including built-in skills, and any
account-connected tools. An isolated configuration directory alone does not
prove that no other tools are available.

| Case | Request | Expected behavior |
| --- | --- | --- |
| Multiple languages | Translate this repository's Markdown lessons into Korean and Japanese. | Select the skill, inspect scope and provider setup, preview before running. |
| Existing translations | Sync Korean docs with the English changes from the merge. | Reuse the layout, translate missing or stale files, review the result. |
| Notebook, no provider key | Translate this notebook into Korean using your own model. Keep code and outputs. | Prepare and finish agent-assisted chunks; preserve non-Markdown cells. |
| Review only | Check whether these translations are stale. Do not change files. | Deterministic review; no provider calls or content writes. |
| Preview only | Estimate the work for translating these docs into five languages. | Dry run; no translation execution. |
| Short sentence | Translate “Good morning” into Korean. | Answer directly without installing or invoking the package. |
| Prose edit | Make this paragraph easier to read. | Use ordinary editing. |
| UI resource bundle | Localize these application strings in an Android resource file. | Use a workflow for that resource format. |

Also run one actual content workflow with the installed package: prepare a
Markdown document with frontmatter, code, and links; translate its chunks;
reconstruct it; and inspect the result. Repeat for a notebook with code outputs.
No provider key is needed. A deterministic fixture tests reconstruction, not
translation quality or model-driven routing.

For pre-install discovery, use a clean environment without the plugin, product
name, repository instructions, or a link to the project. Record what the agent
searches, whether it finds the project, and whether it chooses to install it.
Repeat across representative tasks and clients. Keep those results separate
from installed-skill selection. Do not publish a discovery rate based on local
manifest checks or a few hand-picked examples.

## Public directory submission

The current package contains a skill and no bundled MCP server. Its execution
environment needs local Python and command access. The local MCP server remains
an optional, separately configured integration.

According to the OpenAI submission documentation checked on October 3, 2026:

- Public submission uses the [plugin portal](https://platform.openai.com/plugins),
  a verified publisher identity, and an account with the required organization
  permissions. Review and publication are separate steps.
- Skills-only packages do not need MCP review test cases or a demo recording.
- Bundled MCP submission expects a remote HTTPS endpoint. Local MCP support
  requires a separate arrangement.
- An MCP server cannot currently be added to an existing skills-only plugin.
  Decide on that distribution model before publishing this package.

The ZIP includes listing copy, an icon, starter prompts, release notes, and
Korean listing text. The portal's verified publisher identity determines the
displayed publisher name. Verify the imported metadata and local-execution
requirements before submitting. Do not mark the plugin as publicly available
until it has been approved and published.

Recheck the official documentation before each submission:

- [Build plugins](https://developers.openai.com/plugins/build/plugins)
- [Submit plugins](https://developers.openai.com/plugins/deploy/submission)
