"""Validate the built Pages artifact without a server or URL rewrite fallback."""

from collections import Counter
import gzip
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET

BASE = "https://azure.github.io/co-op-translator/"
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
XHTML_NS = "http://www.w3.org/1999/xhtml"
CODE_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class PageAssets(HTMLParser):
    def __init__(self):
        super().__init__()
        self.assets = []
        self.scripts = []
        self.language_metadata = []
        self.ids = set()
        self.article_links = []
        self.code_examples = []
        self._code_parts = None
        self.in_article = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "article":
            self.in_article = True
        if self.in_article and tag == "code":
            self._code_parts = []
        if self.in_article and tag == "a" and attrs.get("href"):
            self.article_links.append(attrs["href"])
        if tag in {"script", "img"} and attrs.get("src"):
            self.assets.append(attrs["src"])
            if tag == "script":
                self.scripts.append(attrs["src"])
        if tag == "link":
            if attrs.get("rel") in {"stylesheet", "icon"}:
                self.assets.append(attrs["href"])
            if attrs.get("rel") == "alternate" and "hreflang" in attrs:
                self.language_metadata.append(attrs["href"])

    def handle_data(self, data):
        if self._code_parts is not None:
            self._code_parts.append(data)

    def handle_endtag(self, tag):
        if tag == "code" and self._code_parts is not None:
            self.code_examples.append("".join(self._code_parts))
            self._code_parts = None
        if tag == "article":
            self.in_article = False

    def literal_link_destinations(self):
        return Counter(
            target
            for example in self.code_examples
            for target in CODE_LINK.findall(example)
        )


def check(site):
    # A set of exact filenames also catches case errors on Windows that would
    # otherwise appear only after deployment to GitHub Pages.
    files = {
        path.relative_to(site).as_posix() for path in site.rglob("*") if path.is_file()
    }
    errors = []

    def local_file(url):
        parsed = urlsplit(url)
        if parsed.netloc != urlsplit(BASE).netloc:
            return None
        prefix = urlsplit(BASE).path
        if not parsed.path.startswith(prefix):
            errors.append(f"URL escapes the Pages project path: {url}")
            return None
        path = unquote(parsed.path[len(prefix) :])
        if not path or path.endswith("/"):
            path += "index.html"
        if path not in files:
            errors.append(f"Missing static file (case-sensitive): {url} -> {path}")
            return None
        return site / path

    manifest = (site / "javascripts/i18n-pages.js").read_text(encoding="utf-8")
    pages = json.loads(manifest.split(" = ", 1)[1].split(";\n", 1)[0])["pages"]
    routes = 0
    for translations in pages.values():
        for route in translations.values():
            routes += 1
            local_file(urljoin(BASE, route))

    # Every published language needs valid assets and article links. A successful
    # MkDocs build alone does not reject missing fragment targets by default.
    inspected = 0
    rendered = {}
    page_urls = {}
    for translations in pages.values():
        for route in translations.values():
            url = urljoin(BASE, route)
            page = local_file(url)
            if page is None:
                continue
            inspected += 1
            parser = PageAssets()
            parser.feed(page.read_text(encoding="utf-8"))
            rendered[page] = parser
            page_urls[page] = url
            for asset in parser.assets:
                local_file(urljoin(url, asset))
            scripts = [urljoin(url, script) for script in parser.scripts]
            manifest_url = urljoin(BASE, "javascripts/i18n-pages.js")
            navigation_url = urljoin(BASE, "javascripts/i18n-navigation.js")
            if (
                manifest_url not in scripts
                or navigation_url not in scripts
                or scripts.index(manifest_url) > scripts.index(navigation_url)
            ):
                errors.append(
                    f"Missing or incorrectly ordered navigation scripts: {url}"
                )
            if parser.language_metadata:
                errors.append(f"Theme would request separate language sitemaps: {url}")

    # Code samples are copied by readers. They must keep the source example's
    # destinations, rather than acquire the translated page's relative paths.
    for translations in pages.values():
        if "en" not in translations:
            continue
        source = local_file(urljoin(BASE, translations["en"]))
        if source not in rendered:
            continue
        expected = rendered[source].literal_link_destinations()
        for language, route in translations.items():
            if language == "en":
                continue
            page = local_file(urljoin(BASE, route))
            if (
                page in rendered
                and rendered[page].literal_link_destinations() != expected
            ):
                errors.append(
                    f"Changed link destinations inside code examples: {page_urls[page]}"
                )

    article_links = 0
    for page, parser in rendered.items():
        for href in parser.article_links:
            target = urljoin(page_urls[page], href)
            destination = local_file(target)
            if destination is None:
                continue
            article_links += 1
            fragment = unquote(urlsplit(target).fragment)
            target_page = rendered.get(destination)
            if fragment and target_page is not None and fragment not in target_page.ids:
                errors.append(
                    f"Missing article fragment: {page_urls[page]} -> {target}"
                )

    sitemap = (site / "sitemap.xml").read_bytes()
    if gzip.decompress((site / "sitemap.xml.gz").read_bytes()) != sitemap:
        errors.append("Compressed sitemap differs from sitemap.xml")
    entries = ET.fromstring(sitemap)
    sitemap_urls = set()
    for entry in entries:
        location = entry.findtext(f"{{{SITEMAP_NS}}}loc")
        sitemap_urls.add(location)
        local_file(location)
        for alternate in entry.findall(f"{{{XHTML_NS}}}link"):
            local_file(alternate.get("href"))
    for translations in pages.values():
        for route in translations.values():
            if urljoin(BASE, route) not in sitemap_urls:
                errors.append(f"Published route missing from sitemap: {route}")

    if errors:
        raise SystemExit("\n".join(errors))
    print(
        f"Pages artifact passed: {routes} routes, {inspected} page asset checks, "
        f"{article_links} local article links, "
        f"{len(sitemap_urls)} sitemap entries under /co-op-translator/."
    )


if __name__ == "__main__":
    check(Path(sys.argv[1] if len(sys.argv) > 1 else "site"))
