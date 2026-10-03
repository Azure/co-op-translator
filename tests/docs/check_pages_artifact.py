"""Validate the built Pages artifact without a server or URL rewrite fallback."""

import gzip
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET

BASE = "https://azure.github.io/co-op-translator/"
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
XHTML_NS = "http://www.w3.org/1999/xhtml"


class PageAssets(HTMLParser):
    def __init__(self):
        super().__init__()
        self.assets = []
        self.scripts = []
        self.language_metadata = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"script", "img"} and attrs.get("src"):
            self.assets.append(attrs["src"])
            if tag == "script":
                self.scripts.append(attrs["src"])
        if tag == "link":
            if attrs.get("rel") in {"stylesheet", "icon"}:
                self.assets.append(attrs["href"])
            if attrs.get("rel") == "alternate" and "hreflang" in attrs:
                self.language_metadata.append(attrs["href"])


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

    # Exercise the assets and script ordering on both shallow and deep guides.
    guides = [
        "index.md",
        "configuration.md",
        "first-translation.md",
        "github-actions.md",
    ]
    inspected = 0
    for source in guides:
        for language in ["en", "ko"]:
            url = urljoin(BASE, pages[source][language])
            page = local_file(url)
            if page is None:
                continue
            inspected += 1
            parser = PageAssets()
            parser.feed(page.read_text(encoding="utf-8"))
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
        f"Pages artifact passed: {routes} routes, {inspected} guide asset checks, "
        f"{len(sitemap_urls)} sitemap entries under /co-op-translator/."
    )


if __name__ == "__main__":
    check(Path(sys.argv[1] if len(sys.argv) > 1 else "site"))
