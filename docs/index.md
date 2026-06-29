<section class="home-hero">
  <p class="home-eyebrow">Getting started</p>
  <h1>Co-op Translator Documentation</h1>
  <p class="home-lede">
    Configure an LLM provider, choose your target languages, and use Co-op
    Translator from the CLI, Python API, or MCP server to translate and review
    project content as the source changes.
  </p>
  <a class="home-link" href="workflows/">Choose your workflow -></a>
</section>

## Quick start

These `docs/` pages are the canonical Co-op Translator documentation. Older setup guides have been consolidated here so CLI, API, MCP, CI, and troubleshooting guidance stay in one place.

<div class="quickstart-grid">
  <a class="quickstart-card" href="configuration/">
    <span class="quickstart-step">Step 1</span>
    <strong>Configure your project</strong>
    <span>Set up providers, credentials, target languages, and output directories.</span>
    <em>Read the guide -></em>
  </a>

  <a class="quickstart-card" href="cli/">
    <span class="quickstart-step">Step 2</span>
    <strong>Translate with CLI</strong>
    <span>Run translation, evaluation, review, and link migration commands.</span>
    <em>Read the guide -></em>
  </a>

  <a class="quickstart-card" href="api/">
    <span class="quickstart-step">Step 3</span>
    <strong>Automate with the Python API</strong>
    <span>Use Co-op Translator from scripts and automation workflows.</span>
    <em>Read the guide -></em>
  </a>

  <a class="quickstart-card" href="mcp/">
    <span class="quickstart-step">Step 4</span>
    <strong>Connect with the MCP Server</strong>
    <span>Expose Co-op Translator tools to agents, editors, and MCP-compatible clients.</span>
    <em>Read the guide -></em>
  </a>
</div>

## Before translating private content

Provider-backed translation can send Markdown, notebook Markdown cells, image data, or extracted image text to configured AI services. Review [Privacy and Data Flow](privacy.md) before processing private repositories, sensitive screenshots, or untrusted source content.
