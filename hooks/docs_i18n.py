"""Build navigation availability from the documentation actually being published."""

import gzip
from html import escape
import json
from pathlib import Path
import re
from urllib.parse import urljoin
import xml.etree.ElementTree as ET

from mkdocs.structure.files import File

SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
XHTML_NS = "http://www.w3.org/1999/xhtml"
LANGUAGE_ALTERNATE = re.compile(
    r"<link\b(?=[^>]*\brel=[\"']alternate[\"'])(?=[^>]*\bhreflang=)[^>]*>\s*",
    re.IGNORECASE,
)


def on_files(files, config):
    pages = {}
    for file in files.documentation_pages():
        parts = file.src_uri.split("/")
        language = "en"
        source = file.src_uri
        if parts[0] == "i18n" and len(parts) > 2:
            language = parts[1]
            source = "/".join(parts[2:])
            # The canonical English pages live at the site root.
            if language == "en":
                continue
        pages.setdefault(source, {})[language] = file.url

    files.append(
        File.generated(
            config,
            "javascripts/i18n-pages.js",
            content=(
                "window.coOpI18n = "
                + json.dumps({"pages": pages}, sort_keys=True)
                + ";\nwindow.coOpI18n.root = new URL('../', document.currentScript.src).href;\n"
            ),
        )
    )
    return files


def on_post_page(output, **kwargs):
    # Material interprets head alternates as separately built sites and requests
    # a sitemap beneath each one. All our languages share a single build. Keep
    # the selector, but let i18n-navigation.js handle it without a competing
    # click handler. Search engines receive page alternates in sitemap.xml.
    return LANGUAGE_ALTERNATE.sub("", output)


def _headings(toc):
    for item in toc:
        yield item.level, item.id
        yield from _headings(item.children)


def on_env(env, config, files):
    # Translation preserves cross-document English fragments. Both pages have
    # been rendered at this point, so use MkDocs' actual IDs to add aliases
    # while keeping the translated headings and their table of contents.
    for file in files.documentation_pages():
        parts = file.src_uri.split("/")
        if len(parts) < 3 or parts[0] != "i18n" or parts[1] == "en":
            continue
        source = files.get_file_from_path("/".join(parts[2:]))
        if source is None or source.page is None or file.page is None:
            continue
        original = list(_headings(source.page.toc))
        translated = list(_headings(file.page.toc))
        # Never guess positions for an outdated or structurally different page.
        if [level for level, _ in original] != [level for level, _ in translated]:
            continue
        for (level, source_id), (_, translated_id) in zip(original, translated):
            if source_id in file.page.present_anchor_ids:
                continue
            pattern = rf'(<h{level}\b[^>]*\bid="{re.escape(escape(translated_id, quote=True))}"[^>]*>)'
            alias = f'<span id="{escape(source_id, quote=True)}"></span>'
            content, count = re.subn(
                pattern, lambda match: match[0] + alias, file.page.content, count=1
            )
            if count:
                file.page.content = content
                file.page.present_anchor_ids.add(source_id)
    return env


def on_post_build(config):
    site = Path(config.site_dir)
    sitemap = site / "sitemap.xml"
    if not config.site_url or not sitemap.exists():
        return

    manifest = (site / "javascripts/i18n-pages.js").read_text(encoding="utf-8")
    pages = json.loads(manifest.split(" = ", 1)[1].split(";\n", 1)[0])["pages"]
    alternates = {}
    for translations in pages.values():
        urls = {
            lang: urljoin(config.site_url, url) for lang, url in translations.items()
        }
        for url in urls.values():
            alternates[url] = urls

    ET.register_namespace("", SITEMAP_NS)
    ET.register_namespace("xhtml", XHTML_NS)
    tree = ET.parse(sitemap)
    for entry in tree.getroot():
        location = entry.findtext(f"{{{SITEMAP_NS}}}loc")
        for language, url in alternates.get(location, {}).items():
            ET.SubElement(
                entry,
                f"{{{XHTML_NS}}}link",
                rel="alternate",
                hreflang=language,
                href=url,
            )
    content = ET.tostring(tree.getroot(), encoding="utf-8", xml_declaration=True)
    sitemap.write_bytes(content)
    (site / "sitemap.xml.gz").write_bytes(gzip.compress(content, mtime=0))
