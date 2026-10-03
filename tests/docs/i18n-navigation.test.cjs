const assert = require("node:assert/strict");
const { readFileSync } = require("node:fs");
const path = require("node:path");
const { test } = require("node:test");
const { runInNewContext } = require("node:vm");

const script = readFileSync(path.join(__dirname, "../../docs/javascripts/i18n-navigation.js"), "utf8");

function link(attributes = {}, toc = false) {
  const classes = new Set();
  const element = {
    attributes: { ...attributes },
    labels: [],
    classList: {
      toggle(name, enabled) { enabled ? classes.add(name) : classes.delete(name); },
      contains(name) { return classes.has(name); },
    },
    getAttribute(name) { return this.attributes[name] ?? null; },
    setAttribute(name, value) { this.attributes[name] = value; },
    removeAttribute(name) { delete this.attributes[name]; },
    querySelector() { return this.labels[0] || null; },
    appendChild(label) {
      this.labels.push(label);
      label.remove = () => { this.labels = this.labels.filter(value => value !== label); };
    },
    closest(selector) { return selector === ".md-nav--secondary" && toc ? {} : null; },
  };
  return element;
}

function browser(route, rootPath = "/co-op-translator/", mode = "instant") {
  const root = "https://docs.example" + rootPath;
  const alternatives = ["en", "ko", "fr"].map(lang => link({ hreflang: lang }));
  const nav = ["index.md", "github-actions/", "first-translation/", "only-english/"].map(
    url => link({ href: root + (url === "index.md" ? "" : url) })
  );
  const external = link({ href: "https://other.example/github-actions/", "aria-current": "keep" });
  const toc = link({ href: "#section", "aria-current": "location" }, true);
  nav.push(external, toc);
  const pages = {
    "index.md": { en: "", ko: "i18n/ko/", fr: "i18n/fr/" },
    "github-actions.md": { en: "github-actions/", ko: "i18n/ko/github-actions/", fr: "i18n/fr/github-actions/" },
    "first-translation.md": { en: "first-translation/", ko: "i18n/ko/first-translation/" },
    "only-english.md": { en: "only-english/" },
    "nested/guide.md": { en: "nested/guide/", ko: "i18n/ko/nested/guide/" },
  };
  let refresh;
  const events = {};
  const window = {
    coOpI18n: { root, pages },
    location: { href: root + route },
    addEventListener(name, callback) { events[name] = callback; },
  };
  const document = {
    readyState: mode === "loading" ? "loading" : "complete",
    createElement() { return {}; },
    querySelectorAll(selector) { return selector.includes("hreflang") ? alternatives : nav; },
    addEventListener(name, callback) { events[name] = callback; },
  };
  const context = { window, document, URL };
  if (mode === "instant") context.document$ = { subscribe(callback) { refresh = callback; callback(); } };
  runInNewContext(script, context);
  return { root, window, alternatives, nav, external, toc, events, refresh };
}

test("language switching preserves the current guide in both directions", () => {
  const b = browser("github-actions/");
  assert.equal(b.alternatives[1].getAttribute("href"), b.root + "i18n/ko/github-actions/");
  b.window.location.href = b.alternatives[1].getAttribute("href");
  b.refresh();
  assert.equal(b.alternatives[0].getAttribute("href"), b.root + "github-actions/");
  assert.equal(b.nav[1].getAttribute("aria-current"), "page");
  assert.equal(b.nav[2].getAttribute("href"), b.root + "i18n/ko/first-translation/");
});

test("missing translations stay on the English page with an explicit label", () => {
  const b = browser("first-translation/");
  const french = b.alternatives[2];
  assert.equal(french.getAttribute("href"), b.root + "first-translation/");
  assert.equal(french.getAttribute("hreflang"), "en");
  assert.equal(french.labels[0].textContent, " (English)");
  b.refresh();
  assert.equal(french.labels.length, 1);
  b.window.location.href = b.root + "github-actions/";
  b.refresh();
  assert.equal(french.getAttribute("href"), b.root + "i18n/fr/github-actions/");
  assert.equal(french.getAttribute("hreflang"), "fr");
  assert.equal(french.labels.length, 0);
  assert.equal(french.getAttribute("title"), null);
});

test("instant navigation updates sidebar language, fallback labels and active states", () => {
  const b = browser("i18n/ko/github-actions/");
  assert.equal(b.nav[3].getAttribute("href"), b.root + "only-english/");
  assert.equal(b.nav[3].labels[0].textContent, " (English)");
  b.window.location.href = b.root + "first-translation/";
  b.refresh();
  assert.equal(b.nav[1].getAttribute("href"), b.root + "github-actions/");
  assert.equal(b.nav[1].getAttribute("aria-current"), null);
  assert.equal(b.nav[2].getAttribute("aria-current"), "page");
  assert.equal(b.nav[3].labels.length, 0);
});

test("external links and the nested table of contents are unchanged", () => {
  const b = browser("i18n/ko/github-actions/");
  assert.equal(b.external.getAttribute("href"), "https://other.example/github-actions/");
  assert.equal(b.external.getAttribute("aria-current"), "keep");
  assert.equal(b.toc.getAttribute("href"), "#section");
  assert.equal(b.toc.getAttribute("aria-current"), "location");
});

test("supports root hosting, nested guides and index.html URLs", () => {
  for (const root of ["/", "/preview/project/"]) {
    for (const route of ["nested/guide/", "nested/guide", "nested/guide/index.html"]) {
      const b = browser(route, root);
      assert.equal(b.alternatives[1].getAttribute("href"), b.root + "i18n/ko/nested/guide/");
    }
  }
});

test("preserves queries but does not carry translated heading fragments across languages", () => {
  const b = browser("github-actions/?q=token#prerequisites");
  assert.equal(b.alternatives[0].getAttribute("href"), b.root + "github-actions/?q=token#prerequisites");
  assert.equal(b.alternatives[1].getAttribute("href"), b.root + "i18n/ko/github-actions/?q=token");
  b.window.location.href = b.root + "github-actions/#standard-setup";
  b.events.hashchange();
  assert.equal(b.alternatives[0].getAttribute("href"), b.root + "github-actions/#standard-setup");
});

test("initializes without Material instant navigation", () => {
  const loaded = browser("github-actions/", "/", "complete");
  assert.equal(loaded.alternatives[1].getAttribute("href"), loaded.root + "i18n/ko/github-actions/");
  const loading = browser("github-actions/", "/", "loading");
  loading.events.DOMContentLoaded();
  assert.equal(loading.alternatives[1].getAttribute("href"), loading.root + "i18n/ko/github-actions/");
});

test("unknown routes leave navigation untouched", () => {
  const b = browser("404.html");
  assert.equal(b.alternatives[1].getAttribute("href"), null);
  assert.equal(b.nav[1].getAttribute("href"), b.root + "github-actions/");
});
